from wtforms.meta import DefaultMeta
from .i18n import TornadoTranslations


class TornadoMeta(DefaultMeta):

    def get_translations(self, form):
        """
        Override in subclasses to provide alternate translations factory.
        See the i18n documentation for more.

        :param form: The form.
        :return: An object that provides gettext() and ngettext() methods.
        """
        if form.current_locale:
            return TornadoTranslations(form.current_locale)
        return None
