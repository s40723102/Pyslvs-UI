# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progress.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(514, 135)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/dimensional_synthesis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.time_label = QtWidgets.QLabel(Dialog)
        self.time_label.setObjectName("time_label")
        self.horizontalLayout_2.addWidget(self.time_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.batch_label = QtWidgets.QLabel(Dialog)
        self.batch_label.setObjectName("batch_label")
        self.horizontalLayout_2.addWidget(self.batch_label)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.loopTime = QtWidgets.QSpinBox(Dialog)
        self.loopTime.setMinimum(1)
        self.loopTime.setMaximum(10)
        self.loopTime.setObjectName("loopTime")
        self.horizontalLayout_2.addWidget(self.loopTime)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.fitness_label = QtWidgets.QLabel(Dialog)
        self.fitness_label.setObjectName("fitness_label")
        self.horizontalLayout.addWidget(self.fitness_label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.start_button = QtWidgets.QPushButton(Dialog)
        self.start_button.setObjectName("start_button")
        self.horizontalLayout.addWidget(self.start_button)
        self.interrupt_button = QtWidgets.QPushButton(Dialog)
        self.interrupt_button.setEnabled(False)
        self.interrupt_button.setObjectName("interrupt_button")
        self.horizontalLayout.addWidget(self.interrupt_button)
        self.button_box = QtWidgets.QDialogButtonBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_box.sizePolicy().hasHeightForWidth())
        self.button_box.setSizePolicy(sizePolicy)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.button_box.setObjectName("button_box")
        self.horizontalLayout.addWidget(self.button_box)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.button_box.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dimensional Synthesis"))
        self.label_6.setText(_translate("Dialog", "Time passed:"))
        self.time_label.setText(_translate("Dialog", "00:00:00"))
        self.label_4.setText(_translate("Dialog", "Batch execution:"))
        self.label_7.setText(_translate("Dialog", "with"))
        self.label_5.setText(_translate("Dialog", "time(s)."))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">※ The interrupt button will stop the process, but you can keep the result.</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "Fitness: "))
        self.fitness_label.setText(_translate("Dialog", "N/A"))
        self.start_button.setText(_translate("Dialog", "Start"))
        self.interrupt_button.setText(_translate("Dialog", "Interrupt"))

import icons_rc
