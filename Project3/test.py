# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 454)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_refresh.setGeometry(QtCore.QRect(510, 330, 221, 41))
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.doubleSpinBox_temp = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_temp.setGeometry(QtCore.QRect(520, 100, 71, 32))
        self.doubleSpinBox_temp.setObjectName("doubleSpinBox_temp")
        self.doubleSpinBox_hum = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_hum.setGeometry(QtCore.QRect(680, 100, 71, 32))
        self.doubleSpinBox_hum.setObjectName("doubleSpinBox_hum")
        self.label_temp = QtWidgets.QLabel(self.centralwidget)
        self.label_temp.setGeometry(QtCore.QRect(460, 60, 171, 41))
        self.label_temp.setObjectName("label_temp")
        self.label_hum = QtWidgets.QLabel(self.centralwidget)
        self.label_hum.setGeometry(QtCore.QRect(650, 60, 141, 41))
        self.label_hum.setObjectName("label_hum")
        self.pushButton_temp_graph = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_temp_graph.setGeometry(QtCore.QRect(470, 170, 151, 41))
        self.pushButton_temp_graph.setObjectName("pushButton_temp_graph")
        self.pushButton_hum_graph = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_hum_graph.setGeometry(QtCore.QRect(640, 170, 141, 41))
        self.pushButton_hum_graph.setObjectName("pushButton_hum_graph")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 70, 381, 361))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(410, 40, 41, 391))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 30, 771, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.radioButton_celsius = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_celsius.setGeometry(QtCore.QRect(510, 270, 119, 27))
        self.radioButton_celsius.setObjectName("radioButton_celsius")
        self.radioButton_fahrenheit = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_fahrenheit.setGeometry(QtCore.QRect(650, 270, 119, 27))
        self.radioButton_fahrenheit.setObjectName("radioButton_fahrenheit")
        self.label_units = QtWidgets.QLabel(self.centralwidget)
        self.label_units.setGeometry(QtCore.QRect(560, 240, 141, 22))
        self.label_units.setTextFormat(QtCore.Qt.AutoText)
        self.label_units.setObjectName("label_units")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 430, 781, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_heading = QtWidgets.QLabel(self.centralwidget)
        self.label_heading.setGeometry(QtCore.QRect(370, 10, 131, 22))
        self.label_heading.setObjectName("label_heading")
        self.label_statusbox = QtWidgets.QLabel(self.centralwidget)
        self.label_statusbox.setGeometry(QtCore.QRect(180, 42, 91, 31))
        self.label_statusbox.setObjectName("label_statusbox")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Satya_Siddhant"))
        self.pushButton_refresh.setText(_translate("MainWindow", "Refresh"))
        self.label_temp.setText(_translate("MainWindow", "Temperature Threshold"))
        self.label_hum.setText(_translate("MainWindow", "Humidity Threshold"))
        self.pushButton_temp_graph.setText(_translate("MainWindow", "Temperature Graph"))
        self.pushButton_hum_graph.setText(_translate("MainWindow", "Humidity Graph"))
        self.radioButton_celsius.setText(_translate("MainWindow", "Celsius"))
        self.radioButton_fahrenheit.setText(_translate("MainWindow", "Fahrenheit"))
        self.label_units.setText(_translate("MainWindow", "Temperature Units"))
        self.label_heading.setText(_translate("MainWindow", "SATYA_SIDDHANT"))
        self.label_statusbox.setText(_translate("MainWindow", "STATUS BOX"))
