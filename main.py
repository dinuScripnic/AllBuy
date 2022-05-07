# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import lists
import log_in_window as lw
import add_product as ap


class Ui_AllBuyCO(object):
    def setupUi(self, AllBuyCO):
        AllBuyCO.setObjectName("AllBuyCO")
        AllBuyCO.resize(1280, 687)
        AllBuyCO.setStyleSheet("background-color: rgb(146,170,157);")
        self.centralwidget = QtWidgets.QWidget(AllBuyCO)
        self.centralwidget.setObjectName("centralwidget")
        self.account = QtWidgets.QPushButton(self.centralwidget)
        self.account.setGeometry(QtCore.QRect(1160, 20, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.account.setFont(font)
        self.account.setStyleSheet("background-color: rgb(208, 219, 189);")
        self.account.setObjectName("account")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 20, 68, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.search = QtWidgets.QLineEdit(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(330, 20, 591, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.search.setFont(font)
        self.search.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.search.setObjectName("search")
        self.categories = QtWidgets.QComboBox(self.centralwidget)
        self.categories.setGeometry(QtCore.QRect(30, 20, 191, 41))
        self.categories.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.categories.setObjectName("categories")
        self.filter_laptop_widget = QtWidgets.QWidget(self.centralwidget)
        self.filter_laptop_widget.setGeometry(QtCore.QRect(30, 90, 191, 481))
        self.filter_laptop_widget.setStyleSheet("background-color: rgb(146,170,157);")
        self.filter_laptop_widget.setObjectName("filter_laptop_widget")
        self.filter_laptop = QtWidgets.QPushButton(self.filter_laptop_widget)
        self.filter_laptop.setGeometry(QtCore.QRect(40, 440, 93, 28))
        self.filter_laptop.setStyleSheet("\n"
"background-color: rgb(208, 219, 189);")
        self.filter_laptop.setObjectName("filter_laptop")
        self.groupBox = QtWidgets.QGroupBox(self.filter_laptop_widget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 191, 191))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color: rgb(208, 219, 189);")
        self.groupBox.setObjectName("groupBox")
        self.i3 = QtWidgets.QRadioButton(self.groupBox)
        self.i3.setGeometry(QtCore.QRect(10, 40, 76, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.i3.setFont(font)
        self.i3.setObjectName("i3")
        self.i5 = QtWidgets.QRadioButton(self.groupBox)
        self.i5.setGeometry(QtCore.QRect(10, 60, 76, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.i5.setFont(font)
        self.i5.setObjectName("i5")
        self.i7 = QtWidgets.QRadioButton(self.groupBox)
        self.i7.setGeometry(QtCore.QRect(10, 80, 76, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.i7.setFont(font)
        self.i7.setObjectName("i7")
        self.i9 = QtWidgets.QRadioButton(self.groupBox)
        self.i9.setGeometry(QtCore.QRect(10, 100, 76, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.i9.setFont(font)
        self.i9.setObjectName("i9")
        self.r3 = QtWidgets.QRadioButton(self.groupBox)
        self.r3.setGeometry(QtCore.QRect(90, 40, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.r3.setFont(font)
        self.r3.setObjectName("r3")
        self.r5 = QtWidgets.QRadioButton(self.groupBox)
        self.r5.setGeometry(QtCore.QRect(90, 60, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.r5.setFont(font)
        self.r5.setObjectName("r5")
        self.r7 = QtWidgets.QRadioButton(self.groupBox)
        self.r7.setGeometry(QtCore.QRect(90, 79, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.r7.setFont(font)
        self.r7.setObjectName("r7")
        self.r9 = QtWidgets.QRadioButton(self.groupBox)
        self.r9.setGeometry(QtCore.QRect(90, 100, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.r9.setFont(font)
        self.r9.setObjectName("r9")
        self.ram = QtWidgets.QComboBox(self.groupBox)
        self.ram.setGeometry(QtCore.QRect(10, 160, 77, 20))
        self.ram.setObjectName("ram")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 37, 19))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.m1 = QtWidgets.QRadioButton(self.groupBox)
        self.m1.setGeometry(QtCore.QRect(10, 20, 95, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.m1.setFont(font)
        self.m1.setObjectName("m1")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(90, 130, 101, 61))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.df = QtWidgets.QRadioButton(self.groupBox_4)
        self.df.setGeometry(QtCore.QRect(10, 10, 95, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.df.setFont(font)
        self.df.setObjectName("df")
        self.dt = QtWidgets.QRadioButton(self.groupBox_4)
        self.dt.setGeometry(QtCore.QRect(10, 30, 86, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.dt.setFont(font)
        self.dt.setObjectName("dt")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(0, 122, 191, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setGeometry(QtCore.QRect(90, 130, 3, 61))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.filter_laptop_widget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 310, 191, 121))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("background-color: rgb(208, 219, 189);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.lg = QtWidgets.QRadioButton(self.groupBox_2)
        self.lg.setGeometry(QtCore.QRect(10, 80, 64, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.lg.setFont(font)
        self.lg.setObjectName("lg")
        self.sml = QtWidgets.QRadioButton(self.groupBox_2)
        self.sml.setGeometry(QtCore.QRect(10, 20, 61, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.sml.setFont(font)
        self.sml.setObjectName("sml")
        self.mdm = QtWidgets.QRadioButton(self.groupBox_2)
        self.mdm.setGeometry(QtCore.QRect(10, 50, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.mdm.setFont(font)
        self.mdm.setObjectName("mdm")
        self.std = QtWidgets.QGroupBox(self.groupBox_2)
        self.std.setGeometry(QtCore.QRect(90, 10, 101, 111))
        self.std.setTitle("")
        self.std.setObjectName("std")
        self.pr = QtWidgets.QRadioButton(self.std)
        self.pr.setGeometry(QtCore.QRect(10, 70, 90, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pr.setFont(font)
        self.pr.setObjectName("pr")
        self.gd = QtWidgets.QRadioButton(self.std)
        self.gd.setGeometry(QtCore.QRect(10, 40, 65, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.gd.setFont(font)
        self.gd.setObjectName("gd")
        self.st = QtWidgets.QRadioButton(self.std)
        self.st.setGeometry(QtCore.QRect(10, 10, 85, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.st.setFont(font)
        self.st.setObjectName("st")
        self.groupBox_3 = QtWidgets.QGroupBox(self.filter_laptop_widget)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 200, 191, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("background-color: rgb(208, 219, 189);\n"
"border-color: rgb(0, 0, 0);")
        self.groupBox_3.setObjectName("groupBox_3")
        self.ssd = QtWidgets.QRadioButton(self.groupBox_3)
        self.ssd.setGeometry(QtCore.QRect(20, 20, 53, 19))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ssd.setFont(font)
        self.ssd.setObjectName("ssd")
        self.hdd = QtWidgets.QRadioButton(self.groupBox_3)
        self.hdd.setGeometry(QtCore.QRect(110, 20, 59, 19))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.hdd.setFont(font)
        self.hdd.setObjectName("hdd")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_6.setGeometry(QtCore.QRect(0, 40, 191, 61))
        self.groupBox_6.setStyleSheet("background-color: rgb(208, 219, 189);\n"
"selection-color: rgb(0, 0, 0);")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.tb2 = QtWidgets.QRadioButton(self.groupBox_6)
        self.tb2.setGeometry(QtCore.QRect(110, 10, 50, 19))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tb2.setFont(font)
        self.tb2.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.tb2.setObjectName("tb2")
        self.min = QtWidgets.QRadioButton(self.groupBox_6)
        self.min.setGeometry(QtCore.QRect(20, 10, 60, 19))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.min.setFont(font)
        self.min.setObjectName("min")
        self.tb = QtWidgets.QRadioButton(self.groupBox_6)
        self.tb.setGeometry(QtCore.QRect(20, 30, 59, 19))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tb.setFont(font)
        self.tb.setObjectName("tb")
        self.max = QtWidgets.QRadioButton(self.groupBox_6)
        self.max.setGeometry(QtCore.QRect(110, 30, 69, 19))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.max.setFont(font)
        self.max.setObjectName("max")
        self.line_3 = QtWidgets.QFrame(self.groupBox_6)
        self.line_3.setGeometry(QtCore.QRect(-3, -5, 201, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.basket = QtWidgets.QPushButton(self.centralwidget)
        self.basket.setGeometry(QtCore.QRect(1050, 20, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.basket.setFont(font)
        self.basket.setStyleSheet("background-color: rgb(208, 219, 189);")
        self.basket.setObjectName("basket")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(250, 90, 1001, 481))
        self.widget.setStyleSheet("background-color: rgb(146,170,157);")
        self.widget.setObjectName("widget")
        self.groupBox_5 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_5.setGeometry(QtCore.QRect(40, 20, 271, 211))
        self.groupBox_5.setStyleSheet("background-color: rgb(208, 219, 189);")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_7 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_7.setGeometry(QtCore.QRect(370, 20, 271, 211))
        self.groupBox_7.setStyleSheet("background-color: rgb(208, 219, 189);")
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.groupBox_8 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_8.setGeometry(QtCore.QRect(690, 20, 271, 211))
        self.groupBox_8.setStyleSheet("background-color: rgb(208, 219, 189);")
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.groupBox_9 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_9.setGeometry(QtCore.QRect(690, 250, 271, 211))
        self.groupBox_9.setStyleSheet("background-color: rgb(208, 219, 189);")
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.groupBox_11 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_11.setGeometry(QtCore.QRect(40, 250, 271, 211))
        self.groupBox_11.setStyleSheet("background-color: rgb(208, 219, 189);")
        self.groupBox_11.setTitle("")
        self.groupBox_11.setObjectName("groupBox_11")
        self.groupBox_10 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_10.setGeometry(QtCore.QRect(370, 250, 271, 211))
        self.groupBox_10.setStyleSheet("background-color: rgb(208, 219, 189);")
        self.groupBox_10.setTitle("")
        self.groupBox_10.setObjectName("groupBox_10")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(30, 580, 1221, 41))
        self.widget_2.setStyleSheet("background-color: rgb(146,170,157);")
        self.widget_2.setObjectName("widget_2")
        self.Add_product = QtWidgets.QPushButton(self.centralwidget)
        self.Add_product.setGeometry(QtCore.QRect(940, 20, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.Add_product.setFont(font)
        self.Add_product.setStyleSheet("background-color: rgb(208, 219, 189);")
        self.Add_product.setObjectName("Add_product")
        AllBuyCO.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AllBuyCO)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        AllBuyCO.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AllBuyCO)
        self.statusbar.setObjectName("statusbar")
        AllBuyCO.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(AllBuyCO)
        self.toolBar.setObjectName("toolBar")
        AllBuyCO.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(AllBuyCO)
        QtCore.QMetaObject.connectSlotsByName(AllBuyCO)

        # Stuff for laptop filtering
        # group of processors that are available to check from radiobutton
        self.user = None
        self.radio_processor = [self.i3, self.i5, self.i7, self.i9, self.r3, self.r5, self.r7, self.r9, self.m1 ]
        self.storage_size = [self.min, self.tb2, self.tb, self.max]
        self.screen_size = [self.sml, self.mdm, self.lg]
        self.screen_quality = [self.st, self.gd, self.pr]
        self.acctual_widget = 'Laptop'
        for category in lists.categories:  # add values for category in combobox
            self.categories.addItem(category)
        for ram in lists.laptop_ram:  # add values for ram in combobox
            self.ram.addItem(str(ram))
        self.ram.setCurrentIndex(self.ram.findText("8", QtCore.Qt.MatchFixedString))  # set default value for ram
        # add if user is active, go to account info
        self.account.clicked.connect(lw.log_in_window)  # connect button my_account to function
        self.filter_laptop.clicked.connect(self.get_filters)  # when press button get filters as dictionary
        self.basket.clicked.connect(self.change_widget)
        self.Add_product.clicked.connect(ap.add_product_window)
        self.categories.activated.connect(self.get_category)

    def get_category(self):
        """

        :return: change the filter widget according to category
                 and displays products
        """
        print(self.categories.currentText())
        if self.categories.currentText() == 'Laptop':
            self.filter_tablet_widget.hide()
            self.filter_smartphone_widget.hide()
            self.filter_laptop_widget.show()
        if self.categories.currentText() == 'Tablet':
            self.filter_smartphone_widget.hide()
            self.filter_laptop_widget.hide()
            self.filter_tablet_widget.show()
        if self.categories.currentText() == 'Smartphone':
            self.filter_tablet_widget.hide()
            self.filter_laptop_widget.hide()
            self.filter_smartphone_widget.show()

    def get_filters(self):
        """

        :return: dictionary with user choices
        """
        user_choices = {}
        for processor in self.radio_processor:
            if processor.isChecked():
                user_choices['processor'] = processor.text()
        for storage in self.storage_size:
            if storage.isChecked():
                user_choices['storage_size'] = storage.text()
        user_choices['ram'] = self.ram.currentText()
        for size in self.screen_size:
            if size.isChecked():
                user_choices['screen_size'] = size.text()
        for quality in self.screen_quality:
            if quality.isChecked():
                user_choices['screen_quality'] = quality.text()
        print(user_choices)

    def retranslateUi(self, AllBuyCO):
        _translate = QtCore.QCoreApplication.translate
        AllBuyCO.setWindowTitle(_translate("AllBuyCO", "MainWindow"))
        self.account.setText(_translate("AllBuyCO", "My Account"))
        self.label.setText(_translate("AllBuyCO", "Search"))
        self.filter_laptop.setText(_translate("AllBuyCO", "Filter"))
        self.groupBox.setTitle(_translate("AllBuyCO", "Power"))
        self.i3.setText(_translate("AllBuyCO", "Intel i3"))
        self.i5.setText(_translate("AllBuyCO", "Intel i5"))
        self.i7.setText(_translate("AllBuyCO", "Intel i7"))
        self.i9.setText(_translate("AllBuyCO", "Intel i9"))
        self.r3.setText(_translate("AllBuyCO", "Ryzen 3"))
        self.r5.setText(_translate("AllBuyCO", "Ryzen 5"))
        self.r7.setText(_translate("AllBuyCO", "Ryzen 7"))
        self.r9.setText(_translate("AllBuyCO", "Ryzen 9"))
        self.label_2.setText(_translate("AllBuyCO", "RAM"))
        self.m1.setText(_translate("AllBuyCO", "Apple M1"))
        self.df.setText(_translate("AllBuyCO", "Integrated"))
        self.dt.setText(_translate("AllBuyCO", "Discrete"))
        self.groupBox_2.setTitle(_translate("AllBuyCO", "Screen"))
        self.lg.setText(_translate("AllBuyCO", "17.3`"))
        self.sml.setText(_translate("AllBuyCO", "<14`"))
        self.mdm.setText(_translate("AllBuyCO", "14`-16`"))
        self.st.setText(_translate("AllBuyCO", "Standard"))
        self.pr.setText(_translate("AllBuyCO", "Premium"))
        self.gd.setText(_translate("AllBuyCO", "Good"))
        self.groupBox_3.setTitle(_translate("AllBuyCO", "Storage"))
        self.ssd.setText(_translate("AllBuyCO", "SSD"))
        self.hdd.setText(_translate("AllBuyCO", "HDD"))
        self.tb2.setText(_translate("AllBuyCO", "512"))
        self.min.setText(_translate("AllBuyCO", "<256"))
        self.tb.setText(_translate("AllBuyCO", "1024"))
        self.max.setText(_translate("AllBuyCO", "1024+"))
        self.basket.setText(_translate("AllBuyCO", "Basket"))
        self.Add_product.setText(_translate("AllBuyCO", "Add Product"))
        self.toolBar.setWindowTitle(_translate("AllBuyCO", "toolBar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AllBuyCO = QtWidgets.QMainWindow()
    ui = Ui_AllBuyCO()
    ui.setupUi(AllBuyCO)
    AllBuyCO.show()
    sys.exit(app.exec_())
