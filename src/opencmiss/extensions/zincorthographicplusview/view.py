

from opencmiss.neon.extensions.zinc_views import ZincOrthographicPlusView as BaseZincView

from opencmiss.extensions.zincorthographicplusview.ui_orthographicpluswidget import Ui_OrthographicPlusWidget


class ZincOrthographicPlusView(BaseZincView):

    def __init__(self, context, shared_opengl_widget, parent=None):
        super(ZincOrthographicPlusView, self).__init__(parent)
        self._ui = Ui_OrthographicPlusWidget()
        self._ui.setupUi(self, shared_opengl_widget)
        self._context = context
        self._ui.xOrthographicView_widget.setContext(context)
        self._ui.yOrthographicView_widget.setContext(context)
        self._ui.zOrthographicView_widget.setContext(context)
        self._ui.full3DView_widget.setContext(context)
        self._orthographic_rev_normal_map = {self._ui.xOrthographicView_widget: [-1, 0, 0],
                                      self._ui.yOrthographicView_widget: [0, -1, 0],
                                      self._ui.zOrthographicView_widget: [0, 0, -1]}

        self._make_connections()

    def get_orthographic_view(self, axis):
        """
        Return the Sceneveiwer widget for the given axis, axis must be one of 'x', 'y', or 'z'.
        :param axis: one of 'x', 'y', or 'z'.
        :return: Handle to Sceneviewer widget corresponding to axis.
        """
        return getattr(self._ui, '%sOrthographicView_widget' % axis)

    def get_3d_view(self):
        return self._ui.full3DView_widget

    def _make_connections(self):
        self._ui.xOrthographicView_widget.graphicsInitialized.connect(self._graphics_initialized)
        self._ui.yOrthographicView_widget.graphicsInitialized.connect(self._graphics_initialized)
        self._ui.zOrthographicView_widget.graphicsInitialized.connect(self._graphics_initialized)

    def _graphics_initialized(self):
        sender = self.sender()
        if sender in [self._ui.xOrthographicView_widget,
                      self._ui.yOrthographicView_widget,
                      self._ui.zOrthographicView_widget]:
            sender.setTumbleRate(0)
            eye, look_at, up, angle = sender.getViewParameters()
            rev_n = self._orthographic_rev_normal_map[sender]
            eye = [look_at[0] - rev_n[0], look_at[1] - rev_n[1], look_at[2] - rev_n[2]]
            sender.setViewParameters(eye, look_at, up, angle)
            sender.viewAll()
