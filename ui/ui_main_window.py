# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(888, 443)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/img/django.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.gridLayout.setObjectName("gridLayout")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabs.setFont(font)
        self.tabs.setObjectName("tabs")
        self.gettingStartedTab = QtWidgets.QWidget()
        self.gettingStartedTab.setObjectName("gettingStartedTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gettingStartedTab)
        self.gridLayout_2.setContentsMargins(-1, 9, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.gettingStartedTab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 839, 584))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_7.addWidget(self.label_3, 1, 0, 1, 2)
        self.copyExeFilenameButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.copyExeFilenameButton.setObjectName("copyExeFilenameButton")
        self.gridLayout_7.addWidget(self.copyExeFilenameButton, 2, 1, 1, 1)
        self.exeFilenameLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.exeFilenameLine.setDragEnabled(True)
        self.exeFilenameLine.setReadOnly(True)
        self.exeFilenameLine.setObjectName("exeFilenameLine")
        self.gridLayout_7.addWidget(self.exeFilenameLine, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_7.addWidget(self.label_4, 5, 0, 1, 2)
        self.djangoProjectRootLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.djangoProjectRootLine.setDragEnabled(True)
        self.djangoProjectRootLine.setReadOnly(False)
        self.djangoProjectRootLine.setObjectName("djangoProjectRootLine")
        self.gridLayout_7.addWidget(self.djangoProjectRootLine, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_7.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_7.addWidget(self.label_2, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/img/bss-export-settings-screen.png"))
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 6, 0, 1, 1)
        self.djangoProjectBrowseButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.djangoProjectBrowseButton.setObjectName("djangoProjectBrowseButton")
        self.gridLayout_7.addWidget(self.djangoProjectBrowseButton, 4, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabs.addTab(self.gettingStartedTab, "")
        self.statusLogTab = QtWidgets.QWidget()
        self.statusLogTab.setObjectName("statusLogTab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.statusLogTab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.clearLogButton = QtWidgets.QPushButton(self.statusLogTab)
        self.clearLogButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.clearLogButton.setObjectName("clearLogButton")
        self.gridLayout_5.addWidget(self.clearLogButton, 1, 0, 1, 1)
        self.copyLogToClipboardButton = QtWidgets.QPushButton(self.statusLogTab)
        self.copyLogToClipboardButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.copyLogToClipboardButton.setObjectName("copyLogToClipboardButton")
        self.gridLayout_5.addWidget(self.copyLogToClipboardButton, 1, 1, 1, 1)
        self.statusLogText = QtWidgets.QPlainTextEdit(self.statusLogTab)
        self.statusLogText.setReadOnly(True)
        self.statusLogText.setObjectName("statusLogText")
        self.gridLayout_5.addWidget(self.statusLogText, 0, 0, 1, 3)
        self.openIssuesForumButton = QtWidgets.QPushButton(self.statusLogTab)
        self.openIssuesForumButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.openIssuesForumButton.setObjectName("openIssuesForumButton")
        self.gridLayout_5.addWidget(self.openIssuesForumButton, 1, 2, 1, 1)
        self.tabs.addTab(self.statusLogTab, "")
        self.helpTab = QtWidgets.QWidget()
        self.helpTab.setObjectName("helpTab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.helpTab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.textEdit = QtWidgets.QTextEdit(self.helpTab)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_6.addWidget(self.textEdit, 0, 0, 1, 1)
        self.tabs.addTab(self.helpTab, "")
        self.gridLayout.addWidget(self.tabs, 0, 0, 1, 2)
        self.runExporterButton = QtWidgets.QPushButton(self.centralwidget)
        self.runExporterButton.setMinimumSize(QtCore.QSize(100, 0))
        self.runExporterButton.setMaximumSize(QtCore.QSize(150, 24))
        self.runExporterButton.setObjectName("runExporterButton")
        self.gridLayout.addWidget(self.runExporterButton, 1, 0, 1, 1)
        self.exportProgress = QtWidgets.QProgressBar(self.centralwidget)
        self.exportProgress.setMaximumSize(QtCore.QSize(16777215, 24))
        self.exportProgress.setProperty("value", 0)
        self.exportProgress.setObjectName("exportProgress")
        self.gridLayout.addWidget(self.exportProgress, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bootstrap Studio To Django"))
        self.label_3.setText(_translate("MainWindow", "2. Copy the following EXE filename (namely this app itself) to the BSS > Export Settings > Export Script field \n"
" (see green rectangle below)."))
        self.copyExeFilenameButton.setToolTip(_translate("MainWindow", "Copy this EXE\'s filename to your clipboard."))
        self.copyExeFilenameButton.setText(_translate("MainWindow", "📋"))
        self.label_4.setText(_translate("MainWindow", "4. In BSS click Save to exit the settings screen, save your design and click the Export button."))
        self.djangoProjectRootLine.setPlaceholderText(_translate("MainWindow", "Enter in or browse for your Django project\'s root directory (usually where manage.py sits)"))
        self.label_5.setText(_translate("MainWindow", "3. Provide the root directory of your Django project:"))
        self.label_2.setText(_translate("MainWindow", "1. Decide where you\'d like BSS to copy intermediate project files and specify this in BSS > Export Settings \n"
" (see blue rectangle below)."))
        self.djangoProjectBrowseButton.setToolTip(_translate("MainWindow", "Copy this EXE\'s filename to your clipboard."))
        self.djangoProjectBrowseButton.setText(_translate("MainWindow", "Browse..."))
        self.tabs.setTabText(self.tabs.indexOf(self.gettingStartedTab), _translate("MainWindow", "Getting Started"))
        self.clearLogButton.setText(_translate("MainWindow", "Clear"))
        self.copyLogToClipboardButton.setText(_translate("MainWindow", "Copy To Clipboard 📋"))
        self.openIssuesForumButton.setText(_translate("MainWindow", "Open the Issues Forum 🔗"))
        self.tabs.setTabText(self.tabs.indexOf(self.statusLogTab), _translate("MainWindow", "Status Log"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">BSS files in their root folder will go into the root of the Django project.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">(TODO)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>"))
        self.tabs.setTabText(self.tabs.indexOf(self.helpTab), _translate("MainWindow", "Help"))
        self.runExporterButton.setText(_translate("MainWindow", "Run Exporter"))
import resources_rc
