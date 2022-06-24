# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1041, 630)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 30, 581, 251))
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 30, 561, 211))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_cititre = QPushButton(self.verticalLayoutWidget)
        self.btn_cititre.setObjectName(u"btn_cititre")

        self.verticalLayout.addWidget(self.btn_cititre)

        self.tb_citire = QLineEdit(self.verticalLayoutWidget)
        self.tb_citire.setObjectName(u"tb_citire")
        self.tb_citire.setReadOnly(True)

        self.verticalLayout.addWidget(self.tb_citire)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tb_n = QLineEdit(self.verticalLayoutWidget)
        self.tb_n.setObjectName(u"tb_n")

        self.horizontalLayout_3.addWidget(self.tb_n)

        self.tb_m = QLineEdit(self.verticalLayoutWidget)
        self.tb_m.setObjectName(u"tb_m")

        self.horizontalLayout_3.addWidget(self.tb_m)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 280, 991, 311))
        self.input_matrix = QTextEdit(self.groupBox_2)
        self.input_matrix.setObjectName(u"input_matrix")
        self.input_matrix.setGeometry(QRect(0, 20, 991, 291))
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(610, 30, 401, 251))
        self.verticalLayoutWidget_2 = QWidget(self.groupBox_3)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 30, 381, 211))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.lb_index_max = QLineEdit(self.verticalLayoutWidget_2)
        self.lb_index_max.setObjectName(u"lb_index_max")

        self.horizontalLayout_4.addWidget(self.lb_index_max)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_dendrograma = QPushButton(self.verticalLayoutWidget_2)
        self.btn_dendrograma.setObjectName(u"btn_dendrograma")

        self.horizontalLayout_2.addWidget(self.btn_dendrograma)

        self.sp_nr_clusteri = QSpinBox(self.verticalLayoutWidget_2)
        self.sp_nr_clusteri.setObjectName(u"sp_nr_clusteri")

        self.horizontalLayout_2.addWidget(self.sp_nr_clusteri)

        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.btn_histograme = QPushButton(self.verticalLayoutWidget_2)
        self.btn_histograme.setObjectName(u"btn_histograme")

        self.verticalLayout_2.addWidget(self.btn_histograme)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Citire date", None))
        self.btn_cititre.setText(QCoreApplication.translate("MainWindow", u"Alege document cvs", None))
        self.tb_n.setText(QCoreApplication.translate("MainWindow", u"n=", None))
        self.tb_m.setText(QCoreApplication.translate("MainWindow", u"m=", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Vizualizare linkage matrix", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Grafice", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Index cel mai mare element:", None))
        self.btn_dendrograma.setText(QCoreApplication.translate("MainWindow", u"Afiseaza dendrograma", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"clusteri:", None))
        self.btn_histograme.setText(QCoreApplication.translate("MainWindow", u"Afiseaza histograme", None))
    # retranslateUi

