# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainJpbgXa.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(632, 557)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalFrame = QFrame(self.centralwidget)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setGeometry(QRect(60, 30, 511, 466))
        self.verticalLayout = QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalFrame1 = QFrame(self.verticalFrame)
        self.verticalFrame1.setObjectName(u"verticalFrame1")
        self.verticalFrame1.setMaximumSize(QSize(16777215, 130))
        self.verticalLayout_2 = QVBoxLayout(self.verticalFrame1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalFrame_2 = QFrame(self.verticalFrame1)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.horizontalFrame_2.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalFrame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(15, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.ip_lineEdit = QLineEdit(self.horizontalFrame_2)
        self.ip_lineEdit.setObjectName(u"ip_lineEdit")

        self.horizontalLayout_3.addWidget(self.ip_lineEdit)


        self.verticalLayout_2.addWidget(self.horizontalFrame_2)

        self.horizontalFrame = QFrame(self.verticalFrame1)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(150, 65))
        self.label_2.setFont(font)
        self.label_2.setTextFormat(Qt.TextFormat.AutoText)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(15, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalFrame2 = QFrame(self.horizontalFrame)
        self.verticalFrame2.setObjectName(u"verticalFrame2")
        self.verticalLayout_4 = QVBoxLayout(self.verticalFrame2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.nmap_comboBox = QComboBox(self.verticalFrame2)
        self.nmap_comboBox.addItem("")
        self.nmap_comboBox.addItem("")
        self.nmap_comboBox.addItem("")
        self.nmap_comboBox.addItem("")
        self.nmap_comboBox.setObjectName(u"nmap_comboBox")

        self.verticalLayout_4.addWidget(self.nmap_comboBox)

        self.custom_nmap_lineEdit = QLineEdit(self.verticalFrame2)
        self.custom_nmap_lineEdit.setObjectName(u"custom_nmap_lineEdit")
        self.custom_nmap_lineEdit.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.custom_nmap_lineEdit)


        self.horizontalLayout.addWidget(self.verticalFrame2)


        self.verticalLayout_2.addWidget(self.horizontalFrame)


        self.verticalLayout.addWidget(self.verticalFrame1)

        self.verticalFrame_2 = QFrame(self.verticalFrame)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        self.verticalLayout_3 = QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.startButton = QPushButton(self.verticalFrame_2)
        self.startButton.setObjectName(u"startButton")
        font1 = QFont()
        font1.setPointSize(11)
        self.startButton.setFont(font1)

        self.verticalLayout_3.addWidget(self.startButton)

        self.output_textEdit = QTextEdit(self.verticalFrame_2)
        self.output_textEdit.setObjectName(u"output_textEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_textEdit.sizePolicy().hasHeightForWidth())
        self.output_textEdit.setSizePolicy(sizePolicy)
        self.output_textEdit.setMaximumSize(QSize(16777215, 335))
        self.output_textEdit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.output_textEdit)


        self.verticalLayout.addWidget(self.verticalFrame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"IP (\u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 192.168.0.1, 192.168.0.55)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"NMAP settings", None))
        self.nmap_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Default", None))
        self.nmap_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Intense", None))
        self.nmap_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Quick", None))
        self.nmap_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Custom", None))

        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi

