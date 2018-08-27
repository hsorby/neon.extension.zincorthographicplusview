# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'opencmiss/extensions/zincorthographicplusview/qt/orthographicpluswidget.ui',
# licensing of 'opencmiss/extensions/zincorthographicplusview/qt/orthographicpluswidget.ui' applies.
#
# Created: Mon Aug 27 16:00:34 2018
#      by: pyside2-uic  running on PySide2 5.11.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_OrthographicPlusWidget(object):
    def setupUi(self, OrthographicPlusWidget, shared_opengl_widget):
        OrthographicPlusWidget.setObjectName("OrthographicPlusWidget")
        OrthographicPlusWidget.resize(753, 573)
        self.verticalLayout = QtWidgets.QVBoxLayout(OrthographicPlusWidget)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(OrthographicPlusWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.frame = QtWidgets.QFrame(self.splitter)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.frame)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.xOrthographicView_widget = SceneviewerWidget(self.splitter_2, shared_opengl_widget)
        self.xOrthographicView_widget.setObjectName("xOrthographicView_widget")
        self.full3DView_widget = SceneviewerWidget(self.splitter_2, shared_opengl_widget)
        self.full3DView_widget.setObjectName("full3DView_widget")
        self.horizontalLayout.addWidget(self.splitter_2)
        self.frame_2 = QtWidgets.QFrame(self.splitter)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter_3 = QtWidgets.QSplitter(self.frame_2)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.zOrthographicView_widget = SceneviewerWidget(self.splitter_3, shared_opengl_widget)
        self.zOrthographicView_widget.setObjectName("zOrthographicView_widget")
        self.yOrthographicView_widget = SceneviewerWidget(self.splitter_3, shared_opengl_widget)
        self.yOrthographicView_widget.setObjectName("yOrthographicView_widget")
        self.horizontalLayout_2.addWidget(self.splitter_3)
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(OrthographicPlusWidget)
        QtCore.QMetaObject.connectSlotsByName(OrthographicPlusWidget)

    def retranslateUi(self, OrthographicPlusWidget):
        OrthographicPlusWidget.setWindowTitle(QtWidgets.QApplication.translate("OrthographicPlusWidget", "Form", None, -1))

from opencmiss.zincwidgets.sceneviewerwidget import SceneviewerWidget
