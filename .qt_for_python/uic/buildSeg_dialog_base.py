# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Youss\Documents\pp\New folder\buildseg\buildseg\buildSeg_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_buildSegDialogBase(object):
    def setupUi(self, buildSegDialogBase):
        buildSegDialogBase.setObjectName("buildSegDialogBase")
        buildSegDialogBase.resize(500, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(buildSegDialogBase.sizePolicy().hasHeightForWidth())
        buildSegDialogBase.setSizePolicy(sizePolicy)
        buildSegDialogBase.setMinimumSize(QtCore.QSize(500, 300))
        buildSegDialogBase.setMaximumSize(QtCore.QSize(500, 300))
        self.button_box = QtWidgets.QDialogButtonBox(buildSegDialogBase)
        self.button_box.setGeometry(QtCore.QRect(9, 261, 156, 30))
        self.button_box.setMinimumSize(QtCore.QSize(0, 30))
        self.button_box.setMaximumSize(QtCore.QSize(16777215, 30))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.widget = QtWidgets.QWidget(buildSegDialogBase)
        self.widget.setGeometry(QtCore.QRect(10, 210, 122, 32))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 30))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.cbxBlock = QtWidgets.QComboBox(self.widget)
        self.cbxBlock.setMinimumSize(QtCore.QSize(0, 28))
        self.cbxBlock.setMaximumSize(QtCore.QSize(16777215, 28))
        self.cbxBlock.setCurrentText("")
        self.cbxBlock.setObjectName("cbxBlock")
        self.horizontalLayout_4.addWidget(self.cbxBlock)
        self.widget1 = QtWidgets.QWidget(buildSegDialogBase)
        self.widget1.setGeometry(QtCore.QRect(138, 210, 351, 32))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.cbxOverlap = QtWidgets.QComboBox(self.widget1)
        self.cbxOverlap.setMinimumSize(QtCore.QSize(0, 28))
        self.cbxOverlap.setMaximumSize(QtCore.QSize(16777215, 28))
        self.cbxOverlap.setCurrentText("")
        self.cbxOverlap.setObjectName("cbxOverlap")
        self.horizontalLayout_3.addWidget(self.cbxOverlap)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.ccbGPU = QtWidgets.QCheckBox(self.widget1)
        self.ccbGPU.setMinimumSize(QtCore.QSize(0, 30))
        self.ccbGPU.setMaximumSize(QtCore.QSize(16777215, 30))
        self.ccbGPU.setChecked(True)
        self.ccbGPU.setObjectName("ccbGPU")
        self.horizontalLayout_3.addWidget(self.ccbGPU)
        self.widget2 = QtWidgets.QWidget(buildSegDialogBase)
        self.widget2.setGeometry(QtCore.QRect(10, 10, 475, 32))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget2)
        self.label.setMinimumSize(QtCore.QSize(150, 30))
        self.label.setMaximumSize(QtCore.QSize(150, 30))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.mMapLayerComboBoxR = QgsMapLayerComboBox(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mMapLayerComboBoxR.sizePolicy().hasHeightForWidth())
        self.mMapLayerComboBoxR.setSizePolicy(sizePolicy)
        self.mMapLayerComboBoxR.setMinimumSize(QtCore.QSize(317, 30))
        self.mMapLayerComboBoxR.setMaximumSize(QtCore.QSize(16777215, 30))
        self.mMapLayerComboBoxR.setObjectName("mMapLayerComboBoxR")
        self.horizontalLayout.addWidget(self.mMapLayerComboBoxR)
        self.widget3 = QtWidgets.QWidget(buildSegDialogBase)
        self.widget3.setGeometry(QtCore.QRect(10, 50, 477, 32))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget3)
        self.label_2.setMinimumSize(QtCore.QSize(150, 30))
        self.label_2.setMaximumSize(QtCore.QSize(150, 30))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.mQfwShape = QgsFileWidget(self.widget3)
        self.mQfwShape.setMinimumSize(QtCore.QSize(319, 30))
        self.mQfwShape.setMaximumSize(QtCore.QSize(319, 30))
        self.mQfwShape.setStorageMode(QgsFileWidget.SaveFile)
        self.mQfwShape.setObjectName("mQfwShape")
        self.horizontalLayout_2.addWidget(self.mQfwShape)
        self.widget4 = QtWidgets.QWidget(buildSegDialogBase)
        self.widget4.setGeometry(QtCore.QRect(10, 90, 477, 32))
        self.widget4.setObjectName("widget4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lblParams = QtWidgets.QLabel(self.widget4)
        self.lblParams.setMinimumSize(QtCore.QSize(150, 30))
        self.lblParams.setMaximumSize(QtCore.QSize(150, 30))
        self.lblParams.setObjectName("lblParams")
        self.horizontalLayout_5.addWidget(self.lblParams)
        self.mQfwParams = QgsFileWidget(self.widget4)
        self.mQfwParams.setMinimumSize(QtCore.QSize(319, 30))
        self.mQfwParams.setMaximumSize(QtCore.QSize(319, 30))
        self.mQfwParams.setObjectName("mQfwParams")
        self.horizontalLayout_5.addWidget(self.mQfwParams)
        self.widget5 = QtWidgets.QWidget(buildSegDialogBase)
        self.widget5.setGeometry(QtCore.QRect(10, 170, 477, 32))
        self.widget5.setObjectName("widget5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget5)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.widget5)
        self.label_5.setMinimumSize(QtCore.QSize(150, 30))
        self.label_5.setMaximumSize(QtCore.QSize(150, 30))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.mQfwSimplify = QgsFileWidget(self.widget5)
        self.mQfwSimplify.setMinimumSize(QtCore.QSize(319, 30))
        self.mQfwSimplify.setMaximumSize(QtCore.QSize(319, 30))
        self.mQfwSimplify.setStorageMode(QgsFileWidget.SaveFile)
        self.mQfwSimplify.setObjectName("mQfwSimplify")
        self.horizontalLayout_8.addWidget(self.mQfwSimplify)
        self.widget6 = QtWidgets.QWidget(buildSegDialogBase)
        self.widget6.setGeometry(QtCore.QRect(11, 131, 471, 34))
        self.widget6.setObjectName("widget6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget6)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.simplifyPolygs = QtWidgets.QCheckBox(self.widget6)
        self.simplifyPolygs.setObjectName("simplifyPolygs")
        self.horizontalLayout_7.addWidget(self.simplifyPolygs)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.widget6)
        self.label_6.setMinimumSize(QtCore.QSize(70, 30))
        self.label_6.setMaximumSize(QtCore.QSize(70, 30))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.mQgsDoubleSpinBox = QgsDoubleSpinBox(self.widget6)
        self.mQgsDoubleSpinBox.setObjectName("mQgsDoubleSpinBox")
        self.horizontalLayout_6.addWidget(self.mQgsDoubleSpinBox)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)

        self.retranslateUi(buildSegDialogBase)
        self.cbxBlock.setCurrentIndex(-1)
        self.button_box.accepted.connect(buildSegDialogBase.accept)
        self.button_box.rejected.connect(buildSegDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(buildSegDialogBase)

    def retranslateUi(self, buildSegDialogBase):
        _translate = QtCore.QCoreApplication.translate
        buildSegDialogBase.setWindowTitle(_translate("buildSegDialogBase", "buildSeg"))
        self.label_3.setText(_translate("buildSegDialogBase", "Block size"))
        self.label_4.setText(_translate("buildSegDialogBase", "Overlap size"))
        self.ccbGPU.setText(_translate("buildSegDialogBase", "Use GPU"))
        self.label.setText(_translate("buildSegDialogBase", "Input Raster Layer"))
        self.label_2.setText(_translate("buildSegDialogBase", "Output Shapefile"))
        self.lblParams.setText(_translate("buildSegDialogBase", "Parameter path"))
        self.label_5.setText(_translate("buildSegDialogBase", "Simplified Output Shapefile"))
        self.simplifyPolygs.setText(_translate("buildSegDialogBase", "Simplify Polygons"))
        self.label_6.setText(_translate("buildSegDialogBase", "Threshold"))
from qgsdoublespinbox import QgsDoubleSpinBox
from qgsfilewidget import QgsFileWidget
from qgsmaplayercombobox import QgsMapLayerComboBox
