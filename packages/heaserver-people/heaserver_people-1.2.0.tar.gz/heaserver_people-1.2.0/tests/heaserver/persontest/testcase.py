"""
Creates a test case class for use with the unittest library that is built into Python.
"""

from heaserver.service.testcase.microservicetestcase import get_test_case_cls_default
from heaserver.person import service
from heaobject.user import NONE_USER, ALL_USERS
from heaserver.service.testcase.expectedvalues import Action
from heaserver.person.keycloakmockmongotestcase import KeycloakMockMongoManager

db_store = {
    service.MONGODB_PERSON_COLLECTION: [{
        'id': 'system|none',
        'created': '2022-01-01T00:00:00',
        'derived_by': None,
        'derived_from': [],
        'description': None,
        'display_name': 'Reximus Max',
        'invites': [],
        'modified': None,
        'name': 'reximusmax',
        'owner': NONE_USER,
        'shares': [{
                'invite': None,
                'permissions': ['VIEWER'],
                'type': 'heaobject.root.ShareImpl',
                'user': ALL_USERS
            }],
        'source': None,
        'source_detail': None,
        'first_name': 'Reximus',
        'last_name': 'Max',
        'type': 'heaobject.person.Person',
        'title': None,
        'phone_number': None,
        'preferred_name': None,
        'email': None,
        'type_display_name': 'Person'
    },
        {
            'id': 'system|test',
            'created': '2022-01-01T00:00:00',
            'derived_by': None,
            'derived_from': [],
            'description': None,
            'display_name': 'Luximus Max',
            'invites': [],
            'modified': None,
            'name': 'luximusmax',
            'owner': NONE_USER,
            'shares': [{
                'invite': None,
                'permissions': ['VIEWER'],
                'type': 'heaobject.root.ShareImpl',
                'user': ALL_USERS
            }],
            'source': None,
            'source_detail': None,
            'first_name': 'Luximus',
            'last_name': 'Max',
            'type': 'heaobject.person.Person',
            'title': None,
            'phone_number': None,
            'preferred_name': None,
            'email': None,
            'type_display_name': 'Person'
        }]}


TestCase = get_test_case_cls_default(coll=service.MONGODB_PERSON_COLLECTION,
                                     wstl_package=service.__package__,
                                     db_manager_cls=KeycloakMockMongoManager,
                                     href='http://localhost:8080/people',
                                     fixtures=db_store,
                                     get_actions=[Action(name='heaserver-people-person-get-properties',
                                                         rel=['hea-properties']),
                                                  Action(name='heaserver-people-person-get-self',
                                                         url='http://localhost:8080/people/{id}',
                                                         rel=['self']),
                                                  Action(name='heaserver-people-person-get-settings',
                                                             url='http://localhost:8080/collections/heaobject.settings.SettingsObject',
                                                             rel=['hea-system-menu-item', 'hea-user-menu-item', 'application/x.settingsobject', 'application/x.collection']),
                                                  # Action(name='heaserver-people-person-get-organization-collection',
                                                  #        url='http://localhost:8080/collections/heaobject.organization.Organization',
                                                  #        rel=['hea-system-menu-item', 'application/x.collection']),
                                                  Action(name='heaserver-people-person-get-organizations',
                                                         url='http://localhost:8080/organizations/',
                                                         rel=['application/x.organization']),
                                                  Action(name='heaserver-people-person-get-volumes',
                                                         url='http://localhost:8080/volumes/',
                                                         rel=['application/x.volume']),
                                                  Action(name='heaserver-people-person-get-desktop-object-actions',
                                                         url='http://localhost:8080/desktopobjectactions/',
                                                         rel=['application/x.desktopobjectaction'])
                                                  ],
                                     get_all_actions=[Action(name='heaserver-people-person-get-properties',
                                                             rel=['hea-properties']),
                                                      Action(name='heaserver-people-person-get-self',
                                                             url='http://localhost:8080/people/{id}',
                                                             rel=['self']),
                                                      Action(name='heaserver-people-person-get-settings',
                                                             url='http://localhost:8080/collections/heaobject.settings.SettingsObject',
                                                             rel=['hea-system-menu-item', 'hea-user-menu-item', 'application/x.settingsobject', 'application/x.collection']),
                                                      # Action(name='heaserver-people-person-get-organization-collection',
                                                      #        url='http://localhost:8080/collections/heaobject.organization.Organization',
                                                      #        rel=['hea-system-menu-item', 'application/x.collection']),
                                                      Action(name='heaserver-people-person-get-organizations',
                                                             url='http://localhost:8080/organizations/',
                                                             rel=['application/x.organization']),
                                                      Action(name='heaserver-people-person-get-volumes',
                                                             url='http://localhost:8080/volumes/',
                                                             rel=['application/x.volume']),
                                                      Action(name='heaserver-people-person-get-desktop-object-actions',
                                                             url='http://localhost:8080/desktopobjectactions/',
                                                             rel=['application/x.desktopobjectaction'])],
                                     duplicate_action_name=None,
        exclude=['body_put', 'body_post'])
