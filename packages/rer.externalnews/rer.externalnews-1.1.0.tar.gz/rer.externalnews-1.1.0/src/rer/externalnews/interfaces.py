# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from rer.externalnews import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IRerExternalnewsLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IExternalNews(Interface):
    """ Interfaccia per il content type: External News"""

    externalUrl = schema.TextLine(
        title=_(u'rer_externalnews_externalurl', default=u'External url'),
        description=_(
                u'rer_ernews_externalurl_help',
                default=u'Insert a valid link to an external resource'),
        default=u'',
        required=True,
    )

    externalSource = schema.TextLine(
        title=_(u'rer_externalnews_externalsource', default=u'Source'),
        description=_(
                u'rer_externalnews_externalsource_help',
                default=u"Where the URL is from."),
        default=u'',
        required=False,
    )
