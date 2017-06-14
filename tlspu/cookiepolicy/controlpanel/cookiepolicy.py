# -*- coding:utf-8 -*-

from zope.schema import Bool
from zope.schema import TextLine
from zope.schema import Text
from zope.component import adapts
from zope.interface import Interface
from zope.interface import implements

from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.CMFPlone.utils import getToolByName
from Products.CMFDefault.formlib.schema import ProxyFieldProperty
from Products.CMFDefault.formlib.schema import SchemaAdapterBase

from plone.app.registry.browser import controlpanel


from tlspu.cookiepolicy import TCPMessageFactory as _


class ICookiePolicySchema(Interface):
    """ Cookie Policy configuration """

    TCP_enabled = Bool(
        title=_(u"Enable Cookie Policy"),
        default=True,
        required=False,
    )

    TCP_title = TextLine(
        title=_(u'Title'),
        default=_(u'This Site Uses Cookies'),
        description=_(u'help_tcp_title',
            default=u"Enter the title for the CookiePolicy panel",
        ),
        required=True,
    )

    TCP_message = Text(
        title=_(u'Message'),
        description=_(
            u'help_tcp_message',
            default=(u"Enter the message for the CookiePolicy panel. This may "
                     u"contain HTML"),
        ),
        required=True,
    )


class BaseControlPanelAdapter(SchemaAdapterBase):
    """ Base control panel adapter """

    def __init__(self, context):
        super(BaseControlPanelAdapter, self).__init__(context)
        portal_properties = getToolByName(context, 'portal_properties')
        self.context = portal_properties.tlspu_cookiepolicy_properties


class CookiePolicyControlPanelAdapter(BaseControlPanelAdapter):
    """ Cookie Policy control panel adapter """
    adapts(IPloneSiteRoot)
    implements(ICookiePolicySchema)

    TCP_enabled = ProxyFieldProperty(ICookiePolicySchema['TCP_enabled'])
    TCP_title = ProxyFieldProperty(ICookiePolicySchema['TCP_title'])
    TCP_message = ProxyFieldProperty(ICookiePolicySchema['TCP_message'])


class CookiePolicyControlPanelForm(controlpanel.RegistryEditForm):
    """ """
    id = 'CookiePolicyControlPanel'
    label = _('Cookie Policy settings')
    description = _('Configure settings for Cookie Policy.')
    form_name = _('Cookie Policy')
    schema = ICookiePolicySchema
    schema_prefix = 'tlspu.cookiepolicy'


class CookiePolicyControlPanel(controlpanel.ControlPanelFormWrapper):
    form = CookiePolicyControlPanelForm

