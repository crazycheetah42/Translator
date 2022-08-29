"""
This is the Translator app, made by Aryaman Sriram.
This software is free to use, without a license..
Enjoy translating!
"""
# These imports are for UI config
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt
import qdarkgraystyle
import darkdetect
from PyQt5.QtGui import QIcon, QCursor
# This is for Translation
from googletrans import Translator
import googletrans
import playsound
import pycountry
# This is for Text To Speech
from gtts import gTTS
# System imports
import os
import sys

class Ui_MainWindow(object):
    # Below is for Text To Speech
    def playSoundFile(self):
        speech = os.path.basename(filename)
        playsound.playsound(f"{speech}")
    def getSaveFileName(self):
        file_filter = 'Sound File (*.mp3)'
        default = f"speech_{dest_lang}.mp3"
        response = QFileDialog.getSaveFileName(
            caption = 'Save your translated speech',
            directory = default,
            filter = file_filter,
            initialFilter = 'Sound File (*.mp3)'
        )
        print(response)
        global filename
        filename = response[0]
        tts.save(filename)
        self.playSoundFile()
    def text_to_speech(self):
        text = self.textBrowser.toPlainText()
        global tts
        tts = gTTS(text=text, lang=dest_lang, slow="False")
        self.getSaveFileName()
    # This is for Translation
    def code(self):
        translator_variable = Translator()
        text = self.textEdit.toPlainText()
        lang = str(self.combobox.currentText())
        global dest_lang
        dest_lang = lang.lower()
        out = translator_variable.translate(text, dest=dest_lang)
        self.textBrowser.setText(out.text)
    # setupUi is where you configure the UI.
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1380, 842)
        icon = QIcon()
        icon.addPixmap(QtGui.QPixmap("translator_logo.png"), QIcon.Selected, QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(515, 20, 246, 65))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(765, 30, 61, 51))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Resources/images/AryamanSoftware_Logo.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label")
        self.label_8.setGeometry(QtCore.QRect(745, 80, 61, 68))
        self.label_8.setPixmap(QtGui.QPixmap("Resources/images/translator_logo.png"))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(620, 80, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 150, 251, 41))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 200, 541, 501))
        self.textEdit.setObjectName("textEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(580, 150, 251, 41))
        self.label_5.setObjectName("label_5")
        self.countries = googletrans.LANGUAGES
        self.combobox = QtWidgets.QComboBox(self.centralwidget)
        self.combobox.setGeometry(QtCore.QRect(635, 300, 91, 31))
        self.combobox.setObjectName("combobox")
        self.combobox.addItems(self.countries)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(620, 190, 101, 41))
        self.label_6.setObjectName("label_6")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(790, 200, 541, 501))
        self.textBrowser.setObjectName("textBrowser")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(790, 150, 251, 41))
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1030, 740, 121, 22))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.text_to_speech)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QtCore.QRect(620, 400, 121, 22))
        self.pushButton_2.clicked.connect(self.code)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Translator"))
        self.label.setText(_translate("MainWindow", "Aryaman Software"))
        self.label_2.setText(_translate("MainWindow", "Translator"))
        self.label_3.setText(_translate("MainWindow", "Enter the text to translate:"))
        self.label_5.setText(_translate("MainWindow", "Language to translate to:"))
        self.label_7.setText(_translate("MainWindow", "Here\'s your text:"))
        self.pushButton.setText(_translate("MainWindow", "Save as speech"))
        self.pushButton_2.setText(QtCore.QCoreApplication.translate("MainWindow", u"Translate!", None))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    while True:
        if darkdetect.isDark() == True:
            app.setStyle("Windows")
            app.setStyleSheet(qdarkgraystyle.load_stylesheet())
            MainWindow = QtWidgets.QMainWindow()
            ui = Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()
            sys.exit(app.exec_())
        elif darkdetect.isLight() == True:
            app.setStyle("Windows")
            MainWindow = QtWidgets.QMainWindow()
            ui = Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()
            sys.exit(app.exec_())
