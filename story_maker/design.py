# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_template_new.ui'
#
# Created: Mon May 16 18:10:50 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_StrategicLayer(object):
    def setupUi(self, StrategicLayer):
        StrategicLayer.setObjectName(_fromUtf8("StrategicLayer"))
        StrategicLayer.resize(1448, 826)
        self.centralwidget = QtGui.QWidget(StrategicLayer)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.main_splitter = QtGui.QSplitter(self.centralwidget)
        self.main_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.main_splitter.setObjectName(_fromUtf8("main_splitter"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.main_splitter)
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.main_frame = QtGui.QWidget(self.verticalLayoutWidget_2)
        self.main_frame.setObjectName(_fromUtf8("main_frame"))
        self.verticalLayout_4.addWidget(self.main_frame)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.showCapacities = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.showCapacities.setObjectName(_fromUtf8("showCapacities"))
        self.gridLayout.addWidget(self.showCapacities, 0, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(6, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_10 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_3.addWidget(self.label_10)
        self.label_9 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_3.addWidget(self.label_9)
        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_3.addWidget(self.label_8)
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_3.addWidget(self.label_7)
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.label_25 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.horizontalLayout_3.addWidget(self.label_25)
        self.label_24 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.horizontalLayout_3.addWidget(self.label_24)
        self.label_23 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.horizontalLayout_3.addWidget(self.label_23)
        self.label_22 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_3.addWidget(self.label_22)
        self.label_21 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_3.addWidget(self.label_21)
        self.label_20 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_3.addWidget(self.label_20)
        self.label_19 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_3.addWidget(self.label_19)
        self.label_18 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_3.addWidget(self.label_18)
        self.label_17 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_3.addWidget(self.label_17)
        self.label_16 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_3.addWidget(self.label_16)
        self.label_15 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_3.addWidget(self.label_15)
        self.label_14 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_3.addWidget(self.label_14)
        self.label_13 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_3.addWidget(self.label_13)
        self.label_12 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_3.addWidget(self.label_12)
        self.label_29 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.horizontalLayout_3.addWidget(self.label_29)
        self.label_30 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.horizontalLayout_3.addWidget(self.label_30)
        self.label_31 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.horizontalLayout_3.addWidget(self.label_31)
        self.label_32 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.horizontalLayout_3.addWidget(self.label_32)
        self.label_33 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.horizontalLayout_3.addWidget(self.label_33)
        self.label_34 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.horizontalLayout_3.addWidget(self.label_34)
        self.label_35 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.horizontalLayout_3.addWidget(self.label_35)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.capacitySlider = QtGui.QSlider(self.verticalLayoutWidget_2)
        self.capacitySlider.setMaximum(30)
        self.capacitySlider.setTracking(True)
        self.capacitySlider.setOrientation(QtCore.Qt.Horizontal)
        self.capacitySlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.capacitySlider.setTickInterval(1)
        self.capacitySlider.setObjectName(_fromUtf8("capacitySlider"))
        self.horizontalLayout_4.addWidget(self.capacitySlider)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.magicButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.magicButton.setObjectName(_fromUtf8("magicButton"))
        self.horizontalLayout_2.addWidget(self.magicButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_28 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.horizontalLayout_2.addWidget(self.label_28)
        self.speedSpinBox = QtGui.QSpinBox(self.verticalLayoutWidget_2)
        self.speedSpinBox.setProperty("value", 1)
        self.speedSpinBox.setObjectName(_fromUtf8("speedSpinBox"))
        self.horizontalLayout_2.addWidget(self.speedSpinBox)
        self.oneStepBackward = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.oneStepBackward.setObjectName(_fromUtf8("oneStepBackward"))
        self.horizontalLayout_2.addWidget(self.oneStepBackward)
        self.pause = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.pause.setObjectName(_fromUtf8("pause"))
        self.horizontalLayout_2.addWidget(self.pause)
        self.play = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.play.setObjectName(_fromUtf8("play"))
        self.horizontalLayout_2.addWidget(self.play)
        self.play_one_step = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.play_one_step.setObjectName(_fromUtf8("play_one_step"))
        self.horizontalLayout_2.addWidget(self.play_one_step)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_36 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.horizontalLayout_2.addWidget(self.label_36)
        self.jumpSpinBox = QtGui.QSpinBox(self.verticalLayoutWidget_2)
        self.jumpSpinBox.setObjectName(_fromUtf8("jumpSpinBox"))
        self.horizontalLayout_2.addWidget(self.jumpSpinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.main_splitter)
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.departureTimes = QtGui.QWidget(self.verticalLayoutWidget_3)
        self.departureTimes.setObjectName(_fromUtf8("departureTimes"))
        self.verticalLayout_3.addWidget(self.departureTimes)
        self.satisfaction = QtGui.QWidget(self.verticalLayoutWidget_3)
        self.satisfaction.setObjectName(_fromUtf8("satisfaction"))
        self.verticalLayout_3.addWidget(self.satisfaction)
        self.normalized = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.normalized.setObjectName(_fromUtf8("normalized"))
        self.verticalLayout_3.addWidget(self.normalized)
        self.line = QtGui.QFrame(self.verticalLayoutWidget_3)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.label_27 = QtGui.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.horizontalLayout_5.addWidget(self.label_27)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.satisfactionSlider = QtGui.QSlider(self.verticalLayoutWidget_3)
        self.satisfactionSlider.setMaximum(1)
        self.satisfactionSlider.setOrientation(QtCore.Qt.Horizontal)
        self.satisfactionSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.satisfactionSlider.setObjectName(_fromUtf8("satisfactionSlider"))
        self.verticalLayout_3.addWidget(self.satisfactionSlider)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_26 = QtGui.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.horizontalLayout.addWidget(self.label_26)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.label_11 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_11.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout.addWidget(self.label_11)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.saveGraphs = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.saveGraphs.setObjectName(_fromUtf8("saveGraphs"))
        self.verticalLayout_3.addWidget(self.saveGraphs)
        self.verticalLayoutWidget = QtGui.QWidget(self.main_splitter)
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.story = QtGui.QTextBrowser(self.verticalLayoutWidget)
        self.story.setObjectName(_fromUtf8("story"))
        self.verticalLayout.addWidget(self.story)
        self.information = QtGui.QTextBrowser(self.verticalLayoutWidget)
        self.information.setObjectName(_fromUtf8("information"))
        self.verticalLayout.addWidget(self.information)
        self.verticalLayout_5.addWidget(self.main_splitter)
        StrategicLayer.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(StrategicLayer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1448, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        StrategicLayer.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(StrategicLayer)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        StrategicLayer.setStatusBar(self.statusbar)

        self.retranslateUi(StrategicLayer)
        QtCore.QMetaObject.connectSlotsByName(StrategicLayer)

    def retranslateUi(self, StrategicLayer):
        StrategicLayer.setWindowTitle(_translate("StrategicLayer", "MainWindow", None))
        self.showCapacities.setText(_translate("StrategicLayer", "Show Capacities", None))
        self.label_10.setText(_translate("StrategicLayer", "0", None))
        self.label_9.setText(_translate("StrategicLayer", "1", None))
        self.label_8.setText(_translate("StrategicLayer", "2", None))
        self.label_7.setText(_translate("StrategicLayer", "3", None))
        self.label_6.setText(_translate("StrategicLayer", "4", None))
        self.label_5.setText(_translate("StrategicLayer", "5", None))
        self.label_4.setText(_translate("StrategicLayer", "6", None))
        self.label_3.setText(_translate("StrategicLayer", "7", None))
        self.label_2.setText(_translate("StrategicLayer", "8", None))
        self.label.setText(_translate("StrategicLayer", "9", None))
        self.label_25.setText(_translate("StrategicLayer", "10", None))
        self.label_24.setText(_translate("StrategicLayer", "11", None))
        self.label_23.setText(_translate("StrategicLayer", "12", None))
        self.label_22.setText(_translate("StrategicLayer", "13", None))
        self.label_21.setText(_translate("StrategicLayer", "14", None))
        self.label_20.setText(_translate("StrategicLayer", "15", None))
        self.label_19.setText(_translate("StrategicLayer", "16", None))
        self.label_18.setText(_translate("StrategicLayer", "17", None))
        self.label_17.setText(_translate("StrategicLayer", "18", None))
        self.label_16.setText(_translate("StrategicLayer", "19", None))
        self.label_15.setText(_translate("StrategicLayer", "20", None))
        self.label_14.setText(_translate("StrategicLayer", "21", None))
        self.label_13.setText(_translate("StrategicLayer", "22", None))
        self.label_12.setText(_translate("StrategicLayer", "23", None))
        self.label_29.setText(_translate("StrategicLayer", "24", None))
        self.label_30.setText(_translate("StrategicLayer", "25", None))
        self.label_31.setText(_translate("StrategicLayer", "26", None))
        self.label_32.setText(_translate("StrategicLayer", "27", None))
        self.label_33.setText(_translate("StrategicLayer", "28", None))
        self.label_34.setText(_translate("StrategicLayer", "29", None))
        self.label_35.setText(_translate("StrategicLayer", "30", None))
        self.magicButton.setText(_translate("StrategicLayer", "Magic Button", None))
        self.label_28.setText(_translate("StrategicLayer", "Step per second", None))
        self.oneStepBackward.setText(_translate("StrategicLayer", "One Step Backward", None))
        self.pause.setText(_translate("StrategicLayer", "Pause", None))
        self.play.setText(_translate("StrategicLayer", "Play", None))
        self.play_one_step.setText(_translate("StrategicLayer", "One Step Forward", None))
        self.label_36.setText(_translate("StrategicLayer", "Jump to Step", None))
        self.normalized.setText(_translate("StrategicLayer", "Normalized Departure Times", None))
        self.label_27.setText(_translate("StrategicLayer", "Satisfaction", None))
        self.label_26.setText(_translate("StrategicLayer", "Absolute", None))
        self.label_11.setText(_translate("StrategicLayer", "Diff.", None))
        self.saveGraphs.setText(_translate("StrategicLayer", "Save Graphs and History", None))

