

from opencmiss.neon.extensions.zinc_views import ZincOrthographicPlusView as BaseZincView


class ZincOrthographicPlusView(BaseZincView):

    def __init__(self, context, parent=None):
        super(ZincOrthographicPlusView, self).__init__(parent)
        self._context = context
