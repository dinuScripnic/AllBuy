# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewmore.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import base64

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import requests

from categories import *


class Ui_Form(object):
    def setupUi(self, Form, product):
        self.product = product
        Form.setObjectName("Form")
        Form.resize(740, 490)
        Form.setStyleSheet("background-color: rgb(146,170,157);")
        self.image = QtWidgets.QLabel(Form)
        self.image.setGeometry(QtCore.QRect(20, 60, 410, 380))
        self.image.setText("")
        self.image.setObjectName("image")
        self.label_name = QtWidgets.QLabel(Form)
        self.label_name.setGeometry(QtCore.QRect(20, 9, 700, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet("background-color: rgb(208, 219, 189);")
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.main_info = QtWidgets.QGroupBox(Form)
        self.main_info.setGeometry(QtCore.QRect(440, 60, 280, 330))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.main_info.setFont(font)
        self.main_info.setTitle("")
        self.main_info.setObjectName("main_info")
        self.label_brand = QtWidgets.QLabel(self.main_info)
        self.label_brand.setGeometry(QtCore.QRect(10, 20, 250, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_brand.setFont(font)
        self.label_brand.setObjectName("label_brand")
        self.label_model = QtWidgets.QLabel(self.main_info)
        self.label_model.setGeometry(QtCore.QRect(10, 50, 250, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_model.setFont(font)
        self.label_model.setObjectName("label_model")
        self.description = QtWidgets.QTextBrowser(self.main_info)
        self.description.setGeometry(QtCore.QRect(10, 230, 260, 90))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.description.setFont(font)
        self.description.setObjectName("description")
        self.label_quality = QtWidgets.QLabel(self.main_info)
        self.label_quality.setGeometry(QtCore.QRect(135, 140, 142, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_quality.setFont(font)
        self.label_quality.setObjectName("label_quality")
        self.label_extra = QtWidgets.QLabel(self.main_info)
        self.label_extra.setGeometry(QtCore.QRect(10, 200, 260, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_extra.setFont(font)
        self.label_extra.setObjectName("label_extra")
        self.label_storage = QtWidgets.QLabel(self.main_info)
        self.label_storage.setGeometry(QtCore.QRect(10, 170, 260, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_storage.setFont(font)
        self.label_storage.setObjectName("label_storage")
        self.label_processor = QtWidgets.QLabel(self.main_info)
        self.label_processor.setGeometry(QtCore.QRect(10, 100, 160, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_processor.setFont(font)
        self.label_processor.setObjectName("label_processor")
        self.label_ram = QtWidgets.QLabel(self.main_info)
        self.label_ram.setGeometry(QtCore.QRect(180, 100, 90, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_ram.setFont(font)
        self.label_ram.setText(f"RAM {self.product.ram} GB")
        self.label_ram.setObjectName("label_ram")
        self.label_size = QtWidgets.QLabel(self.main_info)
        self.label_size.setGeometry(QtCore.QRect(10, 140, 115, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_size.setFont(font)
        self.label_size.setObjectName("label_size")
        self.basket_button = QtWidgets.QPushButton(Form)
        self.basket_button.setGeometry(QtCore.QRect(600, 450, 110, 30))
        self.basket_button.setStyleSheet("background-color: rgb(208, 219, 189);")
        self.basket_button.setObjectName("basket_button")
        self.reviews_button = QtWidgets.QPushButton(Form)
        self.reviews_button.setGeometry(QtCore.QRect(600, 400, 110, 30))
        self.reviews_button.setStyleSheet("background-color: rgb(208, 219, 189);")
        self.reviews_button.setObjectName("reviews_button")
        self.label_price = QtWidgets.QLabel(Form)
        self.label_price.setGeometry(QtCore.QRect(450, 450, 131, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_price.setFont(font)
        self.label_price.setObjectName("label_price")


        # displays the right information and image according to category
        if self.product.category == 1:
            if self.product.image:
                try:
                    image = requests.get(str(self.product.image))
                    self.pixmap = QPixmap()
                    self.pixmap.loadFromData(image.content)
                except:
                    self.pixmap = QPixmap('photos/laptop.jpg')
            else:
                self.pixmap = QPixmap('photos/laptop.jpg')
            if self.product.ssd:
                self.label_storage.setText(f"Storage: SSD {self.product.storage} GB")
            if not self.product.ssd:
                self.label_storage.setText(f"Storage: HDD {self.product.storage} GB")
            if self.product.graphics:
                self.label_extra.setText(f"Graphics:  Discrete {self.product.vram} GB")
            if not self.product.graphics:
                self.label_extra.setText(f"Graphics:  Integrated")

        if self.product.category == 2:
            if self.product.image:
                try:
                    image = requests.get(str(self.product.image))
                    self.pixmap = QPixmap()
                    self.pixmap.loadFromData(image.content)
                except:
                    self.pixmap = QPixmap('photos/tablet.jpg')
            else:
                self.pixmap = QPixmap('photos/tablet.jpg')
            if self.product.network:
                network = 'Wifi + LTE'
            else:
                network = 'Wifi'
            self.label_storage.setText(f"Storage: {self.product.storage} GB              {network}")
            self.label_extra.setText(f"Battery: {self.product.battery} mAh")

        if self.product.category == 3:
            if self.product.image:
                try:
                    image = requests.get(str(self.product.image))
                    self.pixmap = QPixmap()
                    self.pixmap.loadFromData(image.content)
                except:
                    self.pixmap = QPixmap('photos/smartphone.jpg')
            else:
                self.pixmap = QPixmap('photos/smartphone.jpg')
            if self.product.double_sim:
                sim = 'Double Sim'
            else:
                sim = 'Mono Sim'
            self.label_storage.setText(f"Storage: {self.product.storage} GB              {sim}")
            self.label_extra.setText(f"Battery: {self.product.battery} mAh")

        self.image.setPixmap(self.pixmap)
        self.image.setScaledContents(True)
        self.description.setText(f'Description:\n{self.product.description}')

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_name.setText(_translate("Form", f"{self.product.name}"))
        self.label_brand.setText(_translate("Form", f"Brand {self.product.brand}"))
        self.label_model.setText(_translate("Form", f"Model {self.product.model}"))
        self.label_processor.setText(_translate("Form", f"Processor {self.product.processor}"))
        self.label_size.setText(_translate("Form", f"Screen Size {self.product.display_size}`"))
        self.label_quality.setText(_translate("Form", f"Resolution {self.product.display_quality}"))
        self.basket_button.setText(_translate("Form", "Add to basket"))
        self.reviews_button.setText(_translate("Form", "See Reviews"))
        self.label_price.setText(_translate("Form", f"Price:  {self.product.price} {self.product.currency}"))
