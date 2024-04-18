from .testcase import TestCase
from .permissionstestcase import PermissionsTestCase
from heaserver.service.testcase.mixin import GetOneMixin, GetAllMixin, PermissionsGetOneMixin, PermissionsGetAllMixin
from heaserver.service.representor import nvpjson
from heaobject.user import NONE_USER
from aiohttp import hdrs



class TestGet(TestCase, GetOneMixin):
    async def test_get_me(self):
        async with self.client.get((self._href / 'me').path,
                                           headers={**self._headers, hdrs.ACCEPT: nvpjson.MIME_TYPE}) as response:
                self.assertEqual(NONE_USER, (await response.json())[0]['id'])

    async def test_get_me_status(self):
        async with self.client.get((self._href / 'me').path,
                                           headers={**self._headers, hdrs.ACCEPT: nvpjson.MIME_TYPE}) as response:
                self.assertEqual(200, response.status)


class TestGetAll(TestCase, GetAllMixin):
    pass


class TestGetOneWithBadPermissions(PermissionsTestCase, PermissionsGetOneMixin):
    """A test case class for testing GET one requests with bad permissions."""
    pass


class TestGetAllWithBadPermissions(PermissionsTestCase, PermissionsGetAllMixin):
    """A test case class for testing GET all requests with bad permissions."""
    pass

