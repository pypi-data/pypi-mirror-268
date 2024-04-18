# -*- coding: utf-8 -*-
from bda.plone.cart.interfaces import ICartDataProvider
from bda.plone.cart.interfaces import ICartExtensionLayer
from bda.plone.cart.interfaces import ICartItem
from bda.plone.cart.interfaces import ICartItemDataProvider
from bda.plone.cart.interfaces import ICartItemState
from bda.plone.cart.tests import Cart_INTEGRATION_TESTING
from decimal import Decimal
from plone.app.testing import login
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.uuid.interfaces import IUUID
from zope.component import getMultiAdapter
from zope.component import provideAdapter
from zope.interface import alsoProvides

import mock
import unittest


class TestCartDataProvider(unittest.TestCase):
    layer = Cart_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]
        alsoProvides(self.request, ICartExtensionLayer)

        # setup mocks
        alsoProvides(self.portal, ICartItem)
        from . import cartmocks

        provideAdapter(cartmocks.MockShipping, name="mock_shipping")
        provideAdapter(cartmocks.MockCartDataProvider)
        provideAdapter(cartmocks.MockCartItemDataProvider)
        provideAdapter(cartmocks.MockCartItemState)
        self.cart_data_provider = getMultiAdapter(
            (self.portal, self.request), interface=ICartDataProvider
        )
        self.cart_item_state = getMultiAdapter(
            (self.portal, self.request), interface=ICartItemState
        )

    def test_validate_set(self):
        self.assertEquals(
            self.cart_data_provider.validate_set("foo_id"),
            {"success": True, "error": ""},
        )

    @mock.patch("bda.plone.cart.utils.get_object_by_uid")
    def test_validate_count(self, mock_get_object_by_uid):
        mock_get_object_by_uid.return_value = self.portal
        self.assertEquals(
            self.cart_data_provider.validate_count("foo_id", 4),
            {"success": True, "error": ""},
        )
        self.assertEquals(
            self.cart_data_provider.validate_count("foo_id", 10),
            {
                "update": False,
                "success": False,
                "error": u"Not enough items available, abort.",
            },
        )

    def test_shipping(self):
        items = []
        res = self.cart_data_provider.shipping(items)
        self.assertEquals(res["label"], "Mock Shipping")
        self.assertEquals(res["description"], "Mock Shipping Description")
        self.assertEquals(res["net"], Decimal("10"))
        self.assertEquals(res["vat"], Decimal("2"))

    def test_item(self):
        self.assertDictEqual(
            {
                "cart_item_alert": "",
                "cart_item_comment": "",
                "cart_item_count": 5,
                "cart_item_description": "",
                "cart_item_discount": Decimal("0"),
                "cart_item_location:href": "http://foo",
                "cart_item_preview_image:src": "",
                "cart_item_price": "70.00",
                "cart_item_quantity_unit": "",
                "cart_item_title": u"Le item",
                "cart_item_uid": "foo-uid",
                "comment_required": False,
                "no_longer_available": False,
                "quantity_unit_float": False,
            },
            self.cart_data_provider.item("foo-uid", u"Le item", 5, 70.0, "http://foo"),
        )


class TestCartItemDataProvider(unittest.TestCase):
    layer = Cart_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]
        alsoProvides(self.request, ICartExtensionLayer)

        # setup mocks
        alsoProvides(self.portal, ICartItem)
        from . import cartmocks

        provideAdapter(cartmocks.MockCartItemDataProvider)

    def test_cartitemdataprovider__properties(self):
        accessor = ICartItemDataProvider(self.portal)

        # Test custom
        self.assertEquals(accessor.title, "Most awesome Plone site")
        self.assertEquals(accessor.cart_count_limit, 10)
        self.assertEquals(accessor.discount_enabled, False)

        # Test defaults
        self.assertEquals(accessor.discount_enabled, Decimal(0))

        # the rest of the props are not implemented by ICartItemDataProvider
        # execution breaks out of with statement after each raise, so we have
        # to use a with for each property access
        with self.assertRaises(NotImplementedError):
            accessor.net
        with self.assertRaises(NotImplementedError):
            accessor.vat
        with self.assertRaises(NotImplementedError):
            accessor.display_gross
        with self.assertRaises(NotImplementedError):
            accessor.comment_enabled
        with self.assertRaises(NotImplementedError):
            accessor.comment_required
        with self.assertRaises(NotImplementedError):
            accessor.quantity_unit_float
        with self.assertRaises(NotImplementedError):
            accessor.quantity_unit


class TestHelpers(unittest.TestCase):
    """Test helper methods."""

    layer = Cart_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]
        alsoProvides(self.request, ICartExtensionLayer)

        # create an object for testing
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        login(self.portal, TEST_USER_NAME)
        self.portal.invokeFactory("Document", "doc")
        self.doc = self.portal["doc"]

    def test_ascur(self):
        from bda.plone.cart import ascur

        self.assertEquals(ascur(5.0), "5.00")
        self.assertEquals(ascur(5.0, comma=True), "5,00")

    def test_extractitems_malformed_items(self):
        from bda.plone.cart import extractitems

        self.assertRaises(IndexError, extractitems, "foo")

    def test_extractitems_has_items(self):
        from bda.plone.cart import extractitems

        items = "uid-1:5,uid-2:100,uid-3:7"
        self.assertEquals(
            extractitems(items),
            [("uid-1", 5, ""), ("uid-2", 100, ""), ("uid-3", 7, "")],
        )

    def test_aggregate_cart_item_count_non_existing_uid(self):
        from bda.plone.cart import aggregate_cart_item_count

        items = [
            ("uid-1", 5, "no comment"),
            ("uid-2", 100, "no comment"),
            ("uid-1", 7, "no comment"),
        ]

        self.assertEquals(aggregate_cart_item_count("uid-foo", items), 0)

    def test_aggregate_cart_item_count_matching_uid(self):
        from bda.plone.cart import aggregate_cart_item_count

        items = [
            ("uid-1", 5, "no comment"),
            ("uid-2", 100, "no comment"),
            ("uid-1", 7, "no comment"),
        ]

        self.assertEquals(aggregate_cart_item_count("uid-1", items), 12)

    def test_get_catalog_brain(self):
        from bda.plone.cart import get_catalog_brain

        self.assertEquals(get_catalog_brain(self.portal, "foo"), None)
        brain = get_catalog_brain(self.portal, IUUID(self.doc))
        self.assertEquals(brain.getObject(), self.doc)

    def test_get_object_by_uid(self):
        from bda.plone.cart import get_object_by_uid

        self.assertEquals(get_object_by_uid(self.portal, "foo"), None)
        obj = get_object_by_uid(self.portal, IUUID(self.doc))
        self.assertEquals(obj, self.doc)


class TestCookie(unittest.TestCase):
    layer = Cart_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]
        alsoProvides(self.request, ICartExtensionLayer)

    def _set_cookie(self, value):
        # set cookie on the request
        self.request.cookies["cart"] = value

    def test_readcookie_no_cookie(self):
        from bda.plone.cart import readcookie

        self.assertEquals(readcookie(self.request), "")

    def test_readcookie_has_cookie(self):
        from bda.plone.cart import readcookie

        self._set_cookie("uid-1:5,uid-2:100,uid-3:7")
        self.assertEquals(readcookie(self.request), "uid-1:5,uid-2:100,uid-3:7")

    def test_deletecookie(self):
        from bda.plone.cart import deletecookie

        self.assertEquals(self.request.response.cookies, {})
        deletecookie(self.request)
        cookie = self.request.response.cookies["cart"]
        self.assertEquals(cookie["value"], "deleted")
