# Form implementation generated from reading ui file 'GUI_UIs\ui_ai_search.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_AiSearch(object):
    def setupUi(self, Dialog_AiSearch):
        Dialog_AiSearch.setObjectName("Dialog_AiSearch")
        Dialog_AiSearch.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        Dialog_AiSearch.resize(978, 580)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog_AiSearch)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Dialog_AiSearch)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=Dialog_AiSearch)
        self.groupBox_2.setStyleSheet("QGroupBox {border: none}")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.splitter_code_tree = QtWidgets.QSplitter(parent=self.groupBox_2)
        self.splitter_code_tree.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter_code_tree.setOpaqueResize(True)
        self.splitter_code_tree.setChildrenCollapsible(False)
        self.splitter_code_tree.setObjectName("splitter_code_tree")
        self.widget_what = QtWidgets.QWidget(parent=self.splitter_code_tree)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_what.sizePolicy().hasHeightForWidth())
        self.widget_what.setSizePolicy(sizePolicy)
        self.widget_what.setObjectName("widget_what")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_what)
        self.verticalLayout.setContentsMargins(0, 0, 0, 9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.widget_what)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.tabWidget = QtWidgets.QTabWidget(parent=self.widget_what)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_code_search = QtWidgets.QWidget()
        self.tab_code_search.setObjectName("tab_code_search")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_code_search)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.treeWidget = QtWidgets.QTreeWidget(parent=self.tab_code_search)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "Code Tree")
        self.verticalLayout_2.addWidget(self.treeWidget)
        self.widget_3 = QtWidgets.QWidget(parent=self.tab_code_search)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_send_memos = QtWidgets.QCheckBox(parent=self.widget_3)
        self.checkBox_send_memos.setChecked(False)
        self.checkBox_send_memos.setObjectName("checkBox_send_memos")
        self.horizontalLayout_3.addWidget(self.checkBox_send_memos)
        self.checkBox_coded_segments = QtWidgets.QCheckBox(parent=self.widget_3)
        self.checkBox_coded_segments.setObjectName("checkBox_coded_segments")
        self.horizontalLayout_3.addWidget(self.checkBox_coded_segments)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.tabWidget.addTab(self.tab_code_search, "")
        self.tab_free_search = QtWidgets.QWidget()
        self.tab_free_search.setObjectName("tab_free_search")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_free_search)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.tab_free_search)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.lineEdit_free_topic = QtWidgets.QLineEdit(parent=self.tab_free_search)
        self.lineEdit_free_topic.setObjectName("lineEdit_free_topic")
        self.verticalLayout_3.addWidget(self.lineEdit_free_topic)
        self.label_2 = QtWidgets.QLabel(parent=self.tab_free_search)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.textEdit_free_description = QtWidgets.QTextEdit(parent=self.tab_free_search)
        self.textEdit_free_description.setObjectName("textEdit_free_description")
        self.verticalLayout_3.addWidget(self.textEdit_free_description)
        self.tabWidget.addTab(self.tab_free_search, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.widget_2 = QtWidgets.QWidget(parent=self.widget_what)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(parent=self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.lineEdit_prompt = QtWidgets.QLineEdit(parent=self.widget_2)
        self.lineEdit_prompt.setAcceptDrops(False)
        self.lineEdit_prompt.setReadOnly(True)
        self.lineEdit_prompt.setObjectName("lineEdit_prompt")
        self.horizontalLayout_2.addWidget(self.lineEdit_prompt)
        self.pushButton_change_prompt = QtWidgets.QPushButton(parent=self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_change_prompt.sizePolicy().hasHeightForWidth())
        self.pushButton_change_prompt.setSizePolicy(sizePolicy)
        self.pushButton_change_prompt.setObjectName("pushButton_change_prompt")
        self.horizontalLayout_2.addWidget(self.pushButton_change_prompt)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_where = QtWidgets.QWidget(parent=self.splitter_code_tree)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_where.sizePolicy().hasHeightForWidth())
        self.widget_where.setSizePolicy(sizePolicy)
        self.widget_where.setObjectName("widget_where")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_where)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(parent=self.widget_where)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.widget_case_files = QtWidgets.QWidget(parent=self.widget_where)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_case_files.sizePolicy().hasHeightForWidth())
        self.widget_case_files.setSizePolicy(sizePolicy)
        self.widget_case_files.setObjectName("widget_case_files")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_case_files)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.splitter_case_files = QtWidgets.QSplitter(parent=self.widget_case_files)
        self.splitter_case_files.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter_case_files.setChildrenCollapsible(False)
        self.splitter_case_files.setObjectName("splitter_case_files")
        self.listWidget_files = QtWidgets.QListWidget(parent=self.splitter_case_files)
        self.listWidget_files.setObjectName("listWidget_files")
        self.listWidget_cases = QtWidgets.QListWidget(parent=self.splitter_case_files)
        self.listWidget_cases.setObjectName("listWidget_cases")
        self.verticalLayout_5.addWidget(self.splitter_case_files)
        self.widget_attributes = QtWidgets.QWidget(parent=self.widget_case_files)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_attributes.sizePolicy().hasHeightForWidth())
        self.widget_attributes.setSizePolicy(sizePolicy)
        self.widget_attributes.setMinimumSize(QtCore.QSize(0, 24))
        self.widget_attributes.setObjectName("widget_attributes")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_attributes)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_attributeselect = QtWidgets.QPushButton(parent=self.widget_attributes)
        self.pushButton_attributeselect.setObjectName("pushButton_attributeselect")
        self.horizontalLayout.addWidget(self.pushButton_attributeselect)
        self.label_attributes = QtWidgets.QLabel(parent=self.widget_attributes)
        self.label_attributes.setMaximumSize(QtCore.QSize(400, 24))
        self.label_attributes.setText("")
        self.label_attributes.setObjectName("label_attributes")
        self.horizontalLayout.addWidget(self.label_attributes)
        self.verticalLayout_5.addWidget(self.widget_attributes)
        self.verticalLayout_4.addWidget(self.widget_case_files)
        self.horizontalLayout_4.addWidget(self.splitter_code_tree)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.retranslateUi(Dialog_AiSearch)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog_AiSearch)

    def retranslateUi(self, Dialog_AiSearch):
        _translate = QtCore.QCoreApplication.translate
        Dialog_AiSearch.setWindowTitle(_translate("Dialog_AiSearch", "AI search"))
        self.label_3.setText(_translate("Dialog_AiSearch", "What do you want to search for?"))
        self.treeWidget.setToolTip(_translate("Dialog_AiSearch", "Select the code for which you want to find more data"))
        self.checkBox_send_memos.setStatusTip(_translate("Dialog_AiSearch", "Send not only the name but also the memo associated with a code to the AI?"))
        self.checkBox_send_memos.setText(_translate("Dialog_AiSearch", "Send memo to AI"))
        self.checkBox_coded_segments.setToolTip(_translate("Dialog_AiSearch", "If deselected (default), the AI searches for new material only. Segments already coded with this code are excluded from the results."))
        self.checkBox_coded_segments.setText(_translate("Dialog_AiSearch", "Include coded segments"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_code_search), _translate("Dialog_AiSearch", "Code search"))
        self.label.setText(_translate("Dialog_AiSearch", "Topic or phenomenon to search for:"))
        self.lineEdit_free_topic.setToolTip(_translate("Dialog_AiSearch", "Enter a good descriptive name for what you are looking for."))
        self.label_2.setText(_translate("Dialog_AiSearch", "Description:"))
        self.textEdit_free_description.setToolTip(_translate("Dialog_AiSearch", "Give a short description so that the AI can better understand what you are looking for"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_free_search), _translate("Dialog_AiSearch", "Free search"))
        self.label_5.setText(_translate("Dialog_AiSearch", "Search prompt:"))
        self.pushButton_change_prompt.setText(_translate("Dialog_AiSearch", "   Change Prompt   "))
        self.label_4.setText(_translate("Dialog_AiSearch", "Where do you want to search?"))
        self.pushButton_attributeselect.setToolTip(_translate("Dialog_AiSearch", "Filter with the help of attributes"))
        self.pushButton_attributeselect.setText(_translate("Dialog_AiSearch", "Select Attributes"))
