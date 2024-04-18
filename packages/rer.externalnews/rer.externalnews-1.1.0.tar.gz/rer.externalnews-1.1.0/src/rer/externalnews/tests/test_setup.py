# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from rer.externalnews.testing import RER_EXTERNALNEWS_INTEGRATION_TESTING  # noqa

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that rer.externalnews is properly installed."""

    layer = RER_EXTERNALNEWS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if rer.externalnews is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'rer.externalnews'))

    def test_browserlayer(self):
        """Test that IRerExternalnewsLayer is registered."""
        from rer.externalnews.interfaces import (
            IRerExternalnewsLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IRerExternalnewsLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = RER_EXTERNALNEWS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['rer.externalnews'])

    def test_product_uninstalled(self):
        """Test if rer.externalnews is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'rer.externalnews'))

    def test_browserlayer_removed(self):
        """Test that IRerExternalnewsLayer is removed."""
        from rer.externalnews.interfaces import \
            IRerExternalnewsLayer
        from plone.browserlayer import utils
        self.assertNotIn(
           IRerExternalnewsLayer,
           utils.registered_layers())
