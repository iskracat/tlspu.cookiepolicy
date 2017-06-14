from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from plone.app.layout.viewlets import ViewletBase
from plone.registry.interfaces import IRegistry
from zope.component import getUtility


class CookiePolicyViewlet(ViewletBase):

    enabled = False
    title = ""
    message = ""

    render = ViewPageTemplateFile("templates/cookiepolicy.pt")

    def __init__(self, context, request, view, manager):
        super(CookiePolicyViewlet, self).__init__(context, request, view,
                                                  manager)

        registry = getUtility(IRegistry)
        enabled = registry.records.get('tlspu.cookiepolicy.TCP_enabled').value
        title = registry.records.get('tlspu.cookiepolicy.TCP_title').value
        message = registry.records.get('tlspu.cookiepolicy.TCP_message').value

        self.enabled = enabled
        self.title = title or "Cookie Warning"
        self.message = (message or
                "This site uses cookies but the owner has not explained why!")

    def update(self):
        return
