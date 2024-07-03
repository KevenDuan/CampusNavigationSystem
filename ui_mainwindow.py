# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1086, 774)
        MainWindow.setMinimumSize(QtCore.QSize(1086, 774))
        MainWindow.setMaximumSize(QtCore.QSize(1086, 774))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/snow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.map = QtWidgets.QLabel(self.centralwidget)
        self.map.setGeometry(QtCore.QRect(20, 20, 821, 721))
        self.map.setMaximumSize(QtCore.QSize(821, 721))
        self.map.setText("")
        self.map.setPixmap(QtGui.QPixmap(":/map/jju.jpg"))
        self.map.setWordWrap(False)
        self.map.setObjectName("map")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(870, 30, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(870, 80, 89, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(960, 80, 89, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(860, 380, 211, 131))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(870, 330, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(860, 140, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(860, 190, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(860, 250, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(860, 110, 231, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(860, 310, 231, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(860, 530, 211, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(860, 590, 211, 131))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(860, 160, 211, 21))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(860, 210, 211, 21))
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(970, 250, 101, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1086, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 添加条目
        self.radioButton_2.setChecked(True)  # 设置floyd为默认选中
        self.comboBox.addItems(
            ['电子信息实验楼', '电子工程学院', '历史文化研究中心', '信息技术中心', '向学楼', '竞秀楼', '学生宿舍管理中心', '学生一食堂', '旅游与国土资源学院', '万福超市'])
        self.comboBox_2.addItems(
            ['电子信息实验楼', '电子工程学院', '历史文化研究中心', '信息技术中心', '向学楼', '竞秀楼', '学生宿舍管理中心', '学生一食堂', '旅游与国土资源学院', '万福超市'])
        # 绑定事件
        # self.comboBox.currentIndexChanged.connect(self.selectionchange1)
        # self.comboBox_2.currentIndexChanged.connect(self.selectionchange2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1086, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 存在request爬取数据，如果网络不好就会卡住。
        self.check_wearth()  # 查询天气

        self.msg = QMessageBox()
        # 给按钮绑定槽函数
        self.pushButton_2.clicked.connect(self.message)
        self.pushButton.clicked.connect(self.dijkstra)
        self.pushButton_3.clicked.connect(self.car_dijkstra)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "九江学院校园导航系统"))
        self.label_1.setText(_translate("MainWindow", "Shortest Path Algorithm:"))
        self.radioButton.setText(_translate("MainWindow", "Floyd"))
        self.radioButton_2.setText(_translate("MainWindow", "Dijkstra"))
        self.label_2.setText(_translate("MainWindow", "Recommended route:"))
        self.label.setText(_translate("MainWindow", "current location:"))
        self.label_3.setText(_translate("MainWindow", "destination:"))
        self.pushButton.setText(_translate("MainWindow", "Walk Route"))
        self.label_4.setText(_translate("MainWindow", "-----------------------------------"))
        self.label_5.setText(_translate("MainWindow", "-----------------------------------"))
        self.pushButton_2.setText(_translate("MainWindow", "Draw the route"))
        self.pushButton_3.setText(_translate("MainWindow", "Car Route"))

    def message(self):
        self.msg.information(self,"2024年5月1日宣","对不起，此功能正在维护中。",QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
import picture_rc
