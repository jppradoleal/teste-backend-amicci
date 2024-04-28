from unittest.mock import Mock

from rest_framework.test import APITestCase

from core.models import User
from core.permissions import IsOwnerOrReadOnly


class IsOwnerOrReadOnlyPermissionTest(APITestCase):
    def setUp(self):
        self.owner = User(email="owner@gmail.com")
        self.not_owner = User(email="not_owner@gmail.com")

        self.permission = IsOwnerOrReadOnly()

    def test_has_object_permission_safe_method_not_owner(self):
        request = Mock(user=self.not_owner, method="GET")
        obj = Mock(owner=self.owner)

        self.assertTrue(self.permission.has_object_permission(request, None, obj))

    def test_has_object_permission_unsafe_method_not_owner(self):
        request = Mock(user=self.not_owner, method="POST")
        obj = Mock(owner=self.owner)

        self.assertFalse(self.permission.has_object_permission(request, None, obj))

    def test_has_object_permission_unsafe_method_owner(self):
        request = Mock(user=self.owner, method="POST")
        obj = Mock(owner=self.owner)

        self.assertTrue(self.permission.has_object_permission(request, None, obj))
