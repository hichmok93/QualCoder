# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dialog_report_codings.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_reportCodings(object):
    def setupUi(self, Dialog_reportCodings):
        Dialog_reportCodings.setObjectName("Dialog_reportCodings")
        Dialog_reportCodings.setWindowModality(QtCore.Qt.NonModal)
        Dialog_reportCodings.resize(989, 580)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_reportCodings)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog_reportCodings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 120))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 120))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 80, 211, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 60, 211, 21))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.pushButton_search = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_search.setGeometry(QtCore.QRect(440, 20, 121, 27))
        self.pushButton_search.setObjectName("pushButton_search")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 0, 61, 22))
        self.label_2.setObjectName("label_2")
        self.comboBox_coders = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_coders.setGeometry(QtCore.QRect(10, 20, 211, 30))
        self.comboBox_coders.setObjectName("comboBox_coders")
        self.pushButton_attributeselect = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_attributeselect.setGeometry(QtCore.QRect(240, 20, 191, 27))
        self.pushButton_attributeselect.setObjectName("pushButton_attributeselect")
        self.label_exports = QtWidgets.QLabel(self.groupBox)
        self.label_exports.setGeometry(QtCore.QRect(660, 27, 131, 16))
        self.label_exports.setObjectName("label_exports")
        self.comboBox_export = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_export.setGeometry(QtCore.QRect(660, 50, 91, 25))
        self.comboBox_export.setObjectName("comboBox_export")
        self.comboBox_export.addItem("")
        self.comboBox_export.setItemText(0, "")
        self.comboBox_export.addItem("")
        self.comboBox_export.addItem("")
        self.comboBox_export.addItem("")
        self.comboBox_export.addItem("")
        self.label_counts = QtWidgets.QLabel(self.groupBox)
        self.label_counts.setGeometry(QtCore.QRect(240, 60, 331, 50))
        self.label_counts.setMinimumSize(QtCore.QSize(0, 50))
        self.label_counts.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_counts.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_counts.setWordWrap(True)
        self.label_counts.setObjectName("label_counts")
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog_reportCodings)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setContentsMargins(-1, 5, -1, 2)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.splitter_vert = QtWidgets.QSplitter(self.splitter)
        self.splitter_vert.setOrientation(QtCore.Qt.Vertical)
        self.splitter_vert.setObjectName("splitter_vert")
        self.listWidget_files = QtWidgets.QListWidget(self.splitter_vert)
        self.listWidget_files.setObjectName("listWidget_files")
        self.listWidget_cases = QtWidgets.QListWidget(self.splitter_vert)
        self.listWidget_cases.setObjectName("listWidget_cases")
        self.treeWidget = QtWidgets.QTreeWidget(self.splitter_vert)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "Code Tree")
        self.textEdit = QtWidgets.QTextEdit(self.splitter)
        self.textEdit.setObjectName("textEdit")
        self.tableWidget = QtWidgets.QTableWidget(self.splitter)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(Dialog_reportCodings)
        QtCore.QMetaObject.connectSlotsByName(Dialog_reportCodings)
        Dialog_reportCodings.setTabOrder(self.comboBox_coders, self.lineEdit)
        Dialog_reportCodings.setTabOrder(self.lineEdit, self.pushButton_search)
        Dialog_reportCodings.setTabOrder(self.pushButton_search, self.treeWidget)
        Dialog_reportCodings.setTabOrder(self.treeWidget, self.textEdit)

    def retranslateUi(self, Dialog_reportCodings):
        _translate = QtCore.QCoreApplication.translate
        Dialog_reportCodings.setWindowTitle(_translate("Dialog_reportCodings", "Reports"))
        self.label.setText(_translate("Dialog_reportCodings", "Text limiter:"))
        self.pushButton_search.setText(_translate("Dialog_reportCodings", "Search"))
        self.label_2.setText(_translate("Dialog_reportCodings", "Coder:"))
        self.pushButton_attributeselect.setText(_translate("Dialog_reportCodings", "Attributes"))
        self.label_exports.setText(_translate("Dialog_reportCodings", "Export:"))
        self.comboBox_export.setItemText(1, _translate("Dialog_reportCodings", "html"))
        self.comboBox_export.setItemText(2, _translate("Dialog_reportCodings", "txt"))
        self.comboBox_export.setItemText(3, _translate("Dialog_reportCodings", "odt"))
        self.comboBox_export.setItemText(4, _translate("Dialog_reportCodings", "csv"))
        self.label_counts.setText(_translate("Dialog_reportCodings", "Counts:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_reportCodings = QtWidgets.QDialog()
    ui = Ui_Dialog_reportCodings()
    ui.setupUi(Dialog_reportCodings)
    Dialog_reportCodings.show()
    sys.exit(app.exec_())
