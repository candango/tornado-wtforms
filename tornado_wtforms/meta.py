from wtforms.meta import DefaultMeta
from .i18n import TornadoTranslations


class TornadoMeta(DefaultMeta):

    def get_translations(self, form):
        return TornadoTranslations(form)
