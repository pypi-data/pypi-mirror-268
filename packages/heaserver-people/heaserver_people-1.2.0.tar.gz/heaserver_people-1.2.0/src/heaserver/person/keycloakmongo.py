import configparser
from typing import Any
from heaserver.service.db.mongo import MongoManager, Mongo
from heaserver.service import appproperty
from heaserver.service.client import get_property
from heaserver.service.oidcclaimhdrs import SUB
from heaobject.person import Person, Role, get_system_person, get_system_people, Group
from heaobject.user import NONE_USER, ALL_USERS, is_system_user
from heaobject.root import ShareImpl, Permission
from aiohttp.web import Request
from yarl import URL
import logging
from pathlib import Path
from datetime import datetime, timedelta
from enum import Enum
from functools import partial
from asyncio import gather
from cachetools import TTLCache
from copy import deepcopy
from collections.abc import AsyncGenerator
from asyncio import Lock


KEYCLOAK_QUERY_ADMIN_SECRET = 'KEYCLOAK_QUERY_ADMIN_SECRET'
DEFAULT_CLIENT_ID = 'hea'
DEFAULT_ADMIN_CLIENT_ID = 'admin-cli'
DEFAULT_REALM = 'hea'
DEFAULT_HOST = 'https://localhost:8444'
DEFAULT_SECRET_FILE = '.secret'
DEFAULT_VERIFY_SSL = True

CONFIG_SECTION = 'Keycloak'
KEYCLOAK_TEST_IMAGE = 'quay.io/keycloak/keycloak:15.0.2'

_ACCESS_TOKEN_LOCK = Lock()


class KeycloakCompatibility(Enum):
    """Keycloak compatibility levels:
        FIFTEEN: APIs prior to version 19. We have only tested with 15.
        NINETEEN: APIs for version 19 and later.
    """
    FIFTEEN = "15"
    NINETEEN = "19"

DEFAULT_KEYCLOAK_COMPATIBILITY = KeycloakCompatibility.FIFTEEN

class KeycloakMongo(Mongo):
    """
    Database object for accessing a keycloak server. It subclasses Mongo so that some user data that Keycloak does not
    support might be stored in Mongo.
    """
    def __init__(self, config: configparser.ConfigParser | None = None,
                 client_id: str | None = DEFAULT_CLIENT_ID,
                 admin_client_id: str | None = DEFAULT_ADMIN_CLIENT_ID,
                 realm: str | None = DEFAULT_REALM,
                 host: str | None = DEFAULT_HOST,
                 secret: str | None = None,
                 secret_file: str | None = DEFAULT_SECRET_FILE,
                 verify_ssl: bool = DEFAULT_VERIFY_SSL,
                 keycloak_compatibility: KeycloakCompatibility | None = KeycloakCompatibility.FIFTEEN):
        """
        Initializes Keycloak access with a configparser object or manually set configuration parameters. For all
        manually set configuration parameters, the empty string is treated the same as None.

        :param config: a configparser.ConfigParser object, which should have a Keycloak section with the following
        properties:

            Realm = the Keycloak realm.
            VerifySSL = whether to verify SSL certificates (defaults to yes).
            Host = the keycloak hostname.
            Secret = the secret for accessing keycloak.
            SecretFile = alternatively, a file with one line containing the secret.
            Compatibility = 15 or 19 denoting Keycloak 15-18 versus >= 19. The default is 15.
            ClientId = the client id to use. The default is hea.
            AdminClientId = the admin client id to use. The default is admin-cli.

        :param client_id: the client id to use. The default is hea.
        :param admin_client_id: the admin client id to use. The default is admin-cli.
        :param realm: the realm to use if there is no config file or the config file does not specify one. The default
        is hea.
        :param host: the hostname to use if there is no config file or the config file does not specify one. The
        default is localhost.
        :param secret: the secret to use if there is no config file or the config file does not specify one.
        :param secret_file: the path of a file with one line containing the secret if there is no config file or the
        config file does not specify one. There must be either a secret or a secret file.
        :param verify_ssl: whether to verify Keycloak's SSL certificate. The default value is True.
        :param keycloak_compatibility: the compatibility level if there is no config file or the config file does not
        specify one. Defaults to FIFTEEN.
        """
        super().__init__(config)
        self.__ttl_cache = TTLCache(maxsize=128, ttl=30)
        if config and CONFIG_SECTION in config:
            _section = config[CONFIG_SECTION]
            _realm = _section.get('Realm', realm)
            self.__realm = str(_realm) if _realm is not None else DEFAULT_REALM
            self.__verify_ssl = _section.getboolean('VerifySSL', verify_ssl if verify_ssl is not None else DEFAULT_VERIFY_SSL)
            self.__host = str(_section.get('Host', host) or DEFAULT_HOST)
            _secret = _section.get('Secret', secret)
            self.__secret = str(_secret) if _secret else None
            _secret_file = _section.get('SecretFile', secret_file)
            self.__secret_file = str(_secret_file) if _secret_file else None
            compat = _section.get('Compatibility', None) or keycloak_compatibility or DEFAULT_KEYCLOAK_COMPATIBILITY.value
            self.__keycloak_compatibility = KeycloakCompatibility(compat)
            _client_id = _section.get('ClientId', client_id)
            self.__client_id = str(_client_id) if _client_id is not None else DEFAULT_CLIENT_ID
            _admin_client_id = _section.get('AdminClientId', admin_client_id)
            self.__admin_client_id = str(_admin_client_id) if _admin_client_id is not None else DEFAULT_ADMIN_CLIENT_ID
        else:
            self.__realm = str(realm) if realm is not None else DEFAULT_REALM
            self.__verify_ssl = bool(verify_ssl) if verify_ssl is not None else DEFAULT_VERIFY_SSL
            self.__host = str(host) if host is not None else DEFAULT_HOST
            self.__secret = str(secret) if secret is not None else None
            self.__secret_file = str(secret_file) if secret_file is not None else None
            if keycloak_compatibility is not None and not isinstance(keycloak_compatibility, KeycloakCompatibility):
                raise ValueError(f'Keycloak_compatibility must be a KeycloakCompatibility enum value or None but was {keycloak_compatibility}')
            self.__keycloak_compatibility = keycloak_compatibility or DEFAULT_KEYCLOAK_COMPATIBILITY
            self.__client_id = str(client_id) if client_id is not None else DEFAULT_CLIENT_ID
            self.__admin_client_id = str(admin_client_id) if admin_client_id is not None else DEFAULT_ADMIN_CLIENT_ID
        if self.keycloak_compatibility == KeycloakCompatibility.FIFTEEN:
            self.__base_url = URL(self.host) / 'auth'
        else:
            self.__base_url = URL(self.host)
        logger = logging.getLogger(__name__)
        logger.info('Using Keycloak %s mode', self.__keycloak_compatibility.value)
        if self.__host is None:
            raise ValueError
        logger.debug('host is %s', self.__host)
        self.__expiry: datetime | None = None
        self.__access_token: str | None = None


    @property
    def client_id(self) -> str:
        """The Keycloak client id. The default is hea."""
        return self.__client_id

    @property
    def admin_client_id(self) -> str:
        """The Keycloak admin client id. The default is admin-cli."""
        return self.__admin_client_id

    @property
    def realm(self) -> str:
        return self.__realm

    @property
    def host(self) -> str:
        return self.__host

    @property
    def secret(self) -> str | None:
        return self.__secret

    @property
    def secret_file(self) -> str | None:
        return self.__secret_file

    @property
    def verify_ssl(self) -> bool:
        return self.__verify_ssl

    @property
    def keycloak_compatibility(self) -> KeycloakCompatibility:
        return self.__keycloak_compatibility

    @property
    def _base_url(self) -> URL:
        """A URL composed of the hostname and /auth or not depending on whether keycloak compatibility is set to 15 or
        19."""
        return self.__base_url

    async def get_keycloak_access_token(self, request: Request) -> str:
        """
        Request an access token from Keycloak. It tries obtaining a secret from the following places, in order:
        1) The secret parameter of this class' constructor, or the Secret property of the Keycloak section of the HEA
        config file.
        2) A file whose name is passed into the constructor, or provided in the SecretFile property of the Keycloak
        section of the HEA config file. The file must contain one line with the secret.
        3) The KEYCLOAK_QUERY_ADMIN_SECRET registry property.

        :param request: the HTTP request (request).
        :return: the access token or None if not found.
        """
        async with _ACCESS_TOKEN_LOCK:
            if self.__expiry and self.__expiry >= datetime.now() + timedelta(minutes=1):
                return self.__access_token
            else:
                session = request.app[appproperty.HEA_CLIENT_SESSION]
                logger = logging.getLogger(__name__)

                token_url = self.__base_url / 'realms' / self.realm / 'protocol' / 'openid-connect' / 'token'
                logger.debug('Requesting new access token using credentials')
                if self.secret:
                    secret = self.secret
                    logger.debug('Read secret from config or constructor')
                elif self.secret_file and (secret_file_path := Path(self.secret_file)).exists():
                    secret = secret_file_path.read_text(encoding='utf-8')
                    logger.debug('Read secret from file')
                elif secret_property := await get_property(request.app, KEYCLOAK_QUERY_ADMIN_SECRET):
                    secret = secret_property.value
                    logger.debug('Read secret from registry service')
                else:
                    raise ValueError('No secret defined')
                token_body = {
                    'client_secret': secret,
                    'client_id': self.admin_client_id,
                    'grant_type': 'client_credentials'
                }
                logger.debug('Going to verify ssl? %r', self.verify_ssl)
                async with session.post(token_url, data=token_body, verify_ssl=self.verify_ssl) as response_:
                    content = await response_.json()
                    logger.debug('content %s', content)
                    access_token = content['access_token']
                    self.__expiry = datetime.now() + timedelta(seconds=int(content['expires_in']))
                    self.__access_token = access_token
                return access_token

    async def get_users(self, request: Request, params: dict[str, str] | None = None) -> list[Person]:
        """
        Gets a list of users from Keycloak using the '/auth/admin/realms/{realm}/users' REST API call.

        :param request: the HTTP request (required).
        :param params: any query parameters to add to the users request.
        :return: a list of Person objects, or the empty list if there are none.
        """
        logger = logging.getLogger(__name__)
        cached_val = self.__ttl_cache.get(('all_users', None))
        if cached_val is not None:
            return list(cached_val)
        else:
            access_token = await self.get_keycloak_access_token(request)
            session = request.app[appproperty.HEA_CLIENT_SESSION]
            users_url = self.__base_url / 'admin' / 'realms' / self.realm / 'users'
            if params:
                params_ = {}
                for k, v in params.items():
                    match k:
                        case 'name':
                            params_['username'] = v
                        case 'first_name':
                            params_['firstName'] = v
                        case 'last_name':
                            params_['lastName'] = v
                        case _:
                            params_[k] = v
                users_url_ = users_url.with_query(params_)
            else:
                users_url_ = users_url
            logger.debug('Getting users from URL %s', users_url_)
            async with session.get(users_url_,
                                headers={'Authorization': f'Bearer {access_token}'},
                                verify_ssl=self.verify_ssl) as response_:
                response_.raise_for_status()
                user_json = await response_.json()
                logger.debug('Response was %s', user_json)
                persons = []
                for user in user_json:
                    person = self.__keycloak_user_to_person(user)
                    if not params or all(p for p in params.keys() if getattr(person, p) == params[p]):
                        persons.append(person)
                persons.extend(system_person for system_person in get_system_people() if not params or params.get('name') == system_person.name)
                self.__ttl_cache[('all_users', None)] = persons
                for person in persons:
                    self.__ttl_cache[('one_user', person.id)] = person
                return deepcopy(persons)

    async def get_user(self, request: Request, id_: str) -> Person | None:
        """
        Gets the user from Keycloak with the given id using the '/auth/admin/realms/{realm}/users/{id}' REST API call.

        :param request: the HTTP request (required).
        :param id_: the user id (required).
        :return: a Person object.
        :raises ClientResponseError if an error occurred or the person was not found.
        """
        logger = logging.getLogger(__name__)
        cached_val = self.__ttl_cache.get(('one_user', id_))
        if cached_val is not None:
            return cached_val
        else:
            if is_system_user(id_):
                person = get_system_person(id_)
                self.__ttl_cache[('one_user', id_)] = person
                return person
            else:
                access_token = await self.get_keycloak_access_token(request)
                session = request.app[appproperty.HEA_CLIENT_SESSION]
                user_url = self.__base_url / 'admin' / 'realms' / self.realm / 'users' / id_
                async with session.get(user_url,
                                    headers={'Authorization': f'Bearer {access_token}'},
                                    verify_ssl=self.verify_ssl) as response_:
                    user_json = await response_.json()
                    logger.debug('Response was %s', user_json)
                    if 'error' in user_json:
                        if user_json['error'] == 'User not found':
                            return None
                        else:
                            raise ValueError(user_json['error'])
                    person = self.__keycloak_user_to_person(user_json)
                    self.__ttl_cache[('one_user', id_)] = person
                    return deepcopy(person)


    async def get_current_user_roles(self, request: Request) -> list[Role]:
        """
        Gets the current user's roles.

        :param request: the HTTP request (required).
        :returns: a list of Role objects.
        :raises ClientResponseError: if something went wrong getting role information.
        :raises ValueError: if something went wrong getting role information.

        """
        return await self.__get_my_roles(request)

    async def has_role_current_user(self, request: Request, role_name: str) -> bool:
        """
        Returns whether the current user has the given role.

        :param request: the HTTP request (required).
        :param role_name: the role to check (required).
        :returns: True or False.
        :raises ClientResponseError: if something went wrong getting role information.
        :raises ValueError: if something went wrong getting role information.
        """
        async for role_json in self.__get_my_roles_json(request):
            if role_json['name'] == role_name:
                return True
        else:
            return False

    async def get_current_user_groups(self, request: Request) -> list[Group]:
        """
        Gets the current user's groups.

        :param request: the HTTP request (required).
        :returns: a list of Group objects.
        :raises ClientResponseError: if something went wrong getting group information.
        :raises ValueError: if something went wrong getting group information.

        """
        return await self.__get_my_groups(request)

    async def has_group_current_user(self, request: Request, group_name: str) -> bool:
        """
        Returns whether the current user has the given group.

        :param request: the HTTP request (required).
        :param group_name: the group to check (required).
        :returns: True or False.
        :raises ClientResponseError: if something went wrong getting group information.
        :raises ValueError: if something went wrong getting group information.
        """
        async for group_json in self.__get_my_groups_json(request):
            if group_json['name'] == group_name:
                return True
        else:
            return False

    async def __get_my_roles(self, request: Request) -> list[Role]:
        """
        Gets the current user's roles.

        :param request: the HTTP request (request).
        :returns: a list of Role objects. Make a deep copy of this list if you want to modify any of its values.
        :raises ClientResponseError: if something went wrong getting role information.
        :raises ValueError: if something went wrong getting role information.

        """
        logger = logging.getLogger(__name__)
        sub = request.headers.get(SUB, NONE_USER)
        cached_val = self.__ttl_cache.get(('my_roles', sub))
        if cached_val is not None:
            return cached_val
        else:
            values = [self.__new_role(sub, role_json) async for role_json in self.__get_my_roles_json(request)]
            self.__ttl_cache[('my_roles', sub)] = values
            return values

    def __new_role(self, sub: str, role_dict: dict[str, Any]) -> Role:
        """
        Returns a Role object from Keycloak role json.

        :param sub: the user id (required).
        :param role_dict: the role json (required).
        :return: a newly Role object.
        """
        role = Role()
        role.role = role_dict['name']
        role.description = role_dict['description']
        role.owner = NONE_USER
        share = ShareImpl()
        share.user = sub
        share.permissions = [Permission.VIEWER]
        role.shares = [share]
        return role

    async def __get_my_roles_json(self, request: Request) -> AsyncGenerator[dict[str, Any], None]:
        logger = logging.getLogger(__name__)
        sub = request.headers.get(SUB, NONE_USER)
        access_token = await self.get_keycloak_access_token(request)

        session = request.app[appproperty.HEA_CLIENT_SESSION]

        role_base_url = self._base_url / 'admin' / 'realms' / self.realm
        session_get = partial(session.get,
                            headers={'Authorization': f'Bearer {access_token}'},
                            verify_ssl=self.verify_ssl)
        roles = {}
        async with session_get(role_base_url / 'clients') as response_:
            for client_ in await response_.json():
                if client_['clientId'] == self.client_id:
                    client_id_ = client_['id']
                    break
            else:
                raise ValueError(f'No client with id {self.client_id}')
        async def one():
            async with session_get(role_base_url / 'users' / sub / 'role-mappings' / 'clients' / client_id_ / 'composite') as response_:
                for role_dict in await response_.json():
                    roles[role_dict['name']] = role_dict
        async def two():
            async with session_get(role_base_url / 'users' / sub / 'role-mappings' / 'clients' / client_id_) as response_:
                for role_dict in await response_.json():
                    roles[role_dict['name']] = role_dict
        await gather(one(), two())
        logger.debug('roles are %s', roles)
        for role_ in roles.values():
            yield role_

    async def __get_my_groups(self, request: Request) -> list[Role]:
        """
        Gets the current user's groups.

        :param request: the HTTP request (request).
        :returns: a list of Group objects. Make a deep copy of this list if you want to modify any of its values.
        :raises ClientResponseError: if something went wrong getting group information.
        :raises ValueError: if something went wrong getting group information.

        """
        logger = logging.getLogger(__name__)
        sub = request.headers.get(SUB, NONE_USER)
        cached_val = self.__ttl_cache.get(('my_groups', sub))
        if cached_val is not None:
            return cached_val
        else:
            values = [self.__new_group(sub, group_json) async for group_json in self.__get_my_groups_json(request)]
            self.__ttl_cache[('my_groups', sub)] = values
            return values

    def __new_group(self, sub: str, group_dict: dict[str, Any]) -> Group:
        """
        Returns a Group object from Keycloak group json.

        :param sub: the user id (required).
        :param group_dict: the group json (required).
        :return: a newly Group object.
        """
        group = Group()
        group.group = group_dict['path']
        group.owner = NONE_USER
        share = ShareImpl()
        share.user = sub
        share.permissions = [Permission.VIEWER]
        group.shares = [share]
        return group

    async def __get_my_groups_json(self, request: Request) -> AsyncGenerator[dict[str, Any], None]:
        logger = logging.getLogger(__name__)
        sub = request.headers.get(SUB, NONE_USER)
        access_token = await self.get_keycloak_access_token(request)

        session = request.app[appproperty.HEA_CLIENT_SESSION]

        group_base_url = self._base_url / 'admin' / 'realms' / self.realm
        session_get = partial(session.get,
                            headers={'Authorization': f'Bearer {access_token}'},
                            verify_ssl=self.verify_ssl)
        async with session_get(group_base_url / 'users' / sub / 'groups') as response_:
            for group_dict in await response_.json():
                logger.debug('Returning group %s', group_dict)
                yield group_dict

    @staticmethod
    def __keycloak_user_to_person(user: dict[str, Any]) -> Person:
        """
        Converts a user JSON object from Keycloak to a HEA Person object.

        :param user: a Keycloak user object as a JSON dict.
        :return: a Person object.
        """
        person = Person()
        person.id = user['id']
        person.name = user['username']
        person.first_name = user.get('firstName')
        person.last_name = user.get('lastName')
        person.email = user.get('email')
        person.created = datetime.fromtimestamp(user['createdTimestamp'] / 1000.0)
        person.owner = NONE_USER
        person.source = 'Keycloak';
        share = ShareImpl()
        share.user = ALL_USERS
        share.permissions = [Permission.VIEWER]
        person.shares = [share]
        return person


class KeycloakMongoManager(MongoManager):
    """
    Keycloak database manager object. It subclasses the Mongo database manager so that user data that Keycloak does not
    support can be stored in Mongo.
    """
    def __init__(self, config: configparser.ConfigParser | None = None,
                 client_id: str | None = DEFAULT_CLIENT_ID,
                 admin_client_id: str | None = DEFAULT_ADMIN_CLIENT_ID,
                 realm: str | None = None,
                 secret: str | None = None,
                 secret_file: str | None = None,
                 verify_ssl: bool = True):
        super().__init__(config)
        self.__client_id = str(client_id) if client_id is not None else DEFAULT_CLIENT_ID
        self.__admin_client_id = str(admin_client_id) if admin_client_id is not None else DEFAULT_ADMIN_CLIENT_ID
        self.__realm = str(realm) if realm is not None else DEFAULT_REALM
        self.__secret: str | None = str(secret) if secret is not None else None
        self.__secret_file: str | None = str(secret_file) if secret_file is not None else DEFAULT_SECRET_FILE
        self.__verify_ssl: bool = bool(verify_ssl)
        self.__keycloak_external_url: str | None = None

    @property
    def client_id(self) -> str:
        return self.__client_id

    @client_id.setter
    def client_id(self, client_id: str):
        self.__client_id = str(client_id) if client_id is not None else DEFAULT_CLIENT_ID

    @property
    def admin_client_id(self) -> str:
        return self.__admin_client_id

    @admin_client_id.setter
    def admin_client_id(self, admin_client_id: str):
        self.__admin_client_id = str(admin_client_id) if admin_client_id is not None else DEFAULT_ADMIN_CLIENT_ID

    @property
    def realm(self) -> str:
        return self.__realm

    @realm.setter
    def realm(self, realm: str):
        self.__realm = str(realm) if realm is not None else DEFAULT_REALM

    @property
    def secret(self) -> str | None:
        return self.__secret

    @secret.setter
    def secret(self, secret: str | None):
        self.__secret = str(secret) if secret is not None else None

    @property
    def secret_file(self) -> str | None:
        return self.__secret_file

    @secret_file.setter
    def secret_file(self, secret_file: str | None):
        self.__secret_file = str(secret_file) if secret_file is not None else None

    @property
    def verify_ssl(self) -> bool:
        return self.__verify_ssl

    @verify_ssl.setter
    def verify_ssl(self, verify_ssl: bool):
        self.__verify_ssl = bool(verify_ssl)

    @property
    def keycloak_external_url(self) -> str | None:
        return self.__keycloak_external_url

    def get_database(self) -> KeycloakMongo:
        return KeycloakMongo(config=self.config,
                            client_id=self.client_id,
                            admin_client_id=self.admin_client_id,
                            realm=self.realm,
                            host=self.keycloak_external_url,
                            secret=self.secret,
                            secret_file=self.secret_file,
                            verify_ssl=self.verify_ssl)
