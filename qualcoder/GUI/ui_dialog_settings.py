# Form implementation generated from reading ui file 'c:\Users\kai\Documents\Programmierung\2023QualCoder\GUI_UIs\ui_dialog_settings.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_settings(object):
    def setupUi(self, Dialog_settings):
        Dialog_settings.setObjectName("Dialog_settings")
        Dialog_settings.resize(832, 651)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog_settings.sizePolicy().hasHeightForWidth())
        Dialog_settings.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_settings)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(parent=Dialog_settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 795, 601))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 3)
        self.widget_ai = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
        self.widget_ai.setObjectName("widget_ai")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_ai)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_9 = QtWidgets.QLabel(parent=self.widget_ai)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.gridLayout_6.addWidget(self.label_9, 0, 0, 1, 1)
        self.checkBox_AI_enable = QtWidgets.QCheckBox(parent=self.widget_ai)
        self.checkBox_AI_enable.setChecked(True)
        self.checkBox_AI_enable.setObjectName("checkBox_AI_enable")
        self.gridLayout_6.addWidget(self.checkBox_AI_enable, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(parent=self.widget_ai)
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_6.addWidget(self.label_10, 2, 0, 1, 1)
        self.comboBox_ai_model = QtWidgets.QComboBox(parent=self.widget_ai)
        self.comboBox_ai_model.setObjectName("comboBox_ai_model")
        self.gridLayout_6.addWidget(self.comboBox_ai_model, 2, 2, 1, 1)
        self.label_openai_api_key = QtWidgets.QLabel(parent=self.widget_ai)
        self.label_openai_api_key.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_openai_api_key.setObjectName("label_openai_api_key")
        self.gridLayout_6.addWidget(self.label_openai_api_key, 4, 0, 1, 2)
        self.lineEdit_ai_api_key = QtWidgets.QLineEdit(parent=self.widget_ai)
        self.lineEdit_ai_api_key.setObjectName("lineEdit_ai_api_key")
        self.gridLayout_6.addWidget(self.lineEdit_ai_api_key, 4, 2, 1, 1)
        self.checkBox_ai_project_memo = QtWidgets.QCheckBox(parent=self.widget_ai)
        self.checkBox_ai_project_memo.setChecked(True)
        self.checkBox_ai_project_memo.setObjectName("checkBox_ai_project_memo")
        self.gridLayout_6.addWidget(self.checkBox_ai_project_memo, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_ai, 10, 0, 1, 3)
        self.widget_ui = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_ui.sizePolicy().hasHeightForWidth())
        self.widget_ui.setSizePolicy(sizePolicy)
        self.widget_ui.setObjectName("widget_ui")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_ui)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_ui_left = QtWidgets.QWidget(parent=self.widget_ui)
        self.widget_ui_left.setObjectName("widget_ui_left")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_ui_left)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(parent=self.widget_ui_left)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.comboBox_language = QtWidgets.QComboBox(parent=self.widget_ui_left)
        self.comboBox_language.setObjectName("comboBox_language")
        self.gridLayout_3.addWidget(self.comboBox_language, 0, 1, 1, 2)
        self.label = QtWidgets.QLabel(parent=self.widget_ui_left)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 3)
        self.fontComboBox = QtWidgets.QFontComboBox(parent=self.widget_ui_left)
        self.fontComboBox.setObjectName("fontComboBox")
        self.gridLayout_3.addWidget(self.fontComboBox, 2, 0, 1, 2)
        self.spinBox = QtWidgets.QSpinBox(parent=self.widget_ui_left)
        self.spinBox.setMinimum(8)
        self.spinBox.setMaximum(32)
        self.spinBox.setSingleStep(2)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_3.addWidget(self.spinBox, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.widget_ui_left)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 2)
        self.spinBox_treefontsize = QtWidgets.QSpinBox(parent=self.widget_ui_left)
        self.spinBox_treefontsize.setMinimum(8)
        self.spinBox_treefontsize.setMaximum(32)
        self.spinBox_treefontsize.setSingleStep(2)
        self.spinBox_treefontsize.setObjectName("spinBox_treefontsize")
        self.gridLayout_3.addWidget(self.spinBox_treefontsize, 3, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.widget_ui_left)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 4, 0, 1, 2)
        self.spinBox_docfontsize = QtWidgets.QSpinBox(parent=self.widget_ui_left)
        self.spinBox_docfontsize.setMinimum(8)
        self.spinBox_docfontsize.setMaximum(32)
        self.spinBox_docfontsize.setSingleStep(2)
        self.spinBox_docfontsize.setObjectName("spinBox_docfontsize")
        self.gridLayout_3.addWidget(self.spinBox_docfontsize, 4, 2, 1, 1)
        self.label_reports_text_context = QtWidgets.QLabel(parent=self.widget_ui_left)
        self.label_reports_text_context.setObjectName("label_reports_text_context")
        self.gridLayout_3.addWidget(self.label_reports_text_context, 5, 0, 1, 3)
        self.label_chars_before_after = QtWidgets.QLabel(parent=self.widget_ui_left)
        self.label_chars_before_after.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_chars_before_after.setObjectName("label_chars_before_after")
        self.gridLayout_3.addWidget(self.label_chars_before_after, 6, 0, 1, 2)
        self.spinBox_chars_before_after = QtWidgets.QSpinBox(parent=self.widget_ui_left)
        self.spinBox_chars_before_after.setMinimum(20)
        self.spinBox_chars_before_after.setMaximum(300)
        self.spinBox_chars_before_after.setSingleStep(5)
        self.spinBox_chars_before_after.setProperty("value", 150)
        self.spinBox_chars_before_after.setObjectName("spinBox_chars_before_after")
        self.gridLayout_3.addWidget(self.spinBox_chars_before_after, 6, 2, 1, 1)
        self.label_coded_text_style = QtWidgets.QLabel(parent=self.widget_ui_left)
        self.label_coded_text_style.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_coded_text_style.setObjectName("label_coded_text_style")
        self.gridLayout_3.addWidget(self.label_coded_text_style, 7, 0, 1, 2)
        self.comboBox_text_style = QtWidgets.QComboBox(parent=self.widget_ui_left)
        self.comboBox_text_style.setObjectName("comboBox_text_style")
        self.gridLayout_3.addWidget(self.comboBox_text_style, 7, 2, 1, 1)
        self.horizontalLayout.addWidget(self.widget_ui_left)
        self.widget_ui_right = QtWidgets.QWidget(parent=self.widget_ui)
        self.widget_ui_right.setObjectName("widget_ui_right")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_ui_right)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.comboBox_speaker = QtWidgets.QComboBox(parent=self.widget_ui_right)
        self.comboBox_speaker.setObjectName("comboBox_speaker")
        self.gridLayout_4.addWidget(self.comboBox_speaker, 4, 1, 1, 2)
        self.checkBox = QtWidgets.QCheckBox(parent=self.widget_ui_right)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_4.addWidget(self.checkBox, 0, 1, 1, 2)
        self.comboBox_timestamp = QtWidgets.QComboBox(parent=self.widget_ui_right)
        self.comboBox_timestamp.setObjectName("comboBox_timestamp")
        self.gridLayout_4.addWidget(self.comboBox_timestamp, 3, 1, 1, 2)
        self.comboBox_style = QtWidgets.QComboBox(parent=self.widget_ui_right)
        self.comboBox_style.setObjectName("comboBox_style")
        self.gridLayout_4.addWidget(self.comboBox_style, 1, 1, 1, 2)
        self.comboBox_text_chunk_size = QtWidgets.QComboBox(parent=self.widget_ui_right)
        self.comboBox_text_chunk_size.setObjectName("comboBox_text_chunk_size")
        self.comboBox_text_chunk_size.addItem("")
        self.comboBox_text_chunk_size.addItem("")
        self.comboBox_text_chunk_size.addItem("")
        self.comboBox_text_chunk_size.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_text_chunk_size, 2, 2, 1, 1)
        self.label_style = QtWidgets.QLabel(parent=self.widget_ui_right)
        self.label_style.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_style.setObjectName("label_style")
        self.gridLayout_4.addWidget(self.label_style, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.widget_ui_right)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 2, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(parent=self.widget_ui_right)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.widget_ui_right)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 5, 1, 1, 1)
        self.horizontalLayout.addWidget(self.widget_ui_right)
        self.gridLayout.addWidget(self.widget_ui, 2, 0, 1, 3)
        self.widget_backup = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
        self.widget_backup.setObjectName("widget_backup")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_backup)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_backup_left = QtWidgets.QWidget(parent=self.widget_backup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_backup_left.sizePolicy().hasHeightForWidth())
        self.widget_backup_left.setSizePolicy(sizePolicy)
        self.widget_backup_left.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_backup_left.setObjectName("widget_backup_left")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget_backup_left)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButton_choose_directory = QtWidgets.QPushButton(parent=self.widget_backup_left)
        self.pushButton_choose_directory.setObjectName("pushButton_choose_directory")
        self.gridLayout_7.addWidget(self.pushButton_choose_directory, 3, 0, 1, 2)
        self.checkBox_backup_AV_files = QtWidgets.QCheckBox(parent=self.widget_backup_left)
        self.checkBox_backup_AV_files.setChecked(True)
        self.checkBox_backup_AV_files.setObjectName("checkBox_backup_AV_files")
        self.gridLayout_7.addWidget(self.checkBox_backup_AV_files, 2, 0, 1, 2)
        self.checkBox_auto_backup = QtWidgets.QCheckBox(parent=self.widget_backup_left)
        self.checkBox_auto_backup.setChecked(True)
        self.checkBox_auto_backup.setObjectName("checkBox_auto_backup")
        self.gridLayout_7.addWidget(self.checkBox_auto_backup, 1, 0, 1, 2)
        self.spinBox_backups = QtWidgets.QSpinBox(parent=self.widget_backup_left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_backups.sizePolicy().hasHeightForWidth())
        self.spinBox_backups.setSizePolicy(sizePolicy)
        self.spinBox_backups.setMinimum(1)
        self.spinBox_backups.setMaximum(10)
        self.spinBox_backups.setProperty("value", 5)
        self.spinBox_backups.setObjectName("spinBox_backups")
        self.gridLayout_7.addWidget(self.spinBox_backups, 0, 1, 1, 1)
        self.label_backups_to_keep = QtWidgets.QLabel(parent=self.widget_backup_left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_backups_to_keep.sizePolicy().hasHeightForWidth())
        self.label_backups_to_keep.setSizePolicy(sizePolicy)
        self.label_backups_to_keep.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_backups_to_keep.setWordWrap(True)
        self.label_backups_to_keep.setObjectName("label_backups_to_keep")
        self.gridLayout_7.addWidget(self.label_backups_to_keep, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.widget_backup_left)
        self.widget_backup_right = QtWidgets.QWidget(parent=self.widget_backup)
        self.widget_backup_right.setObjectName("widget_backup_right")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_backup_right)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(362, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2.addWidget(self.widget_backup_right)
        self.gridLayout.addWidget(self.widget_backup, 4, 0, 1, 3)
        self.line_3 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 7, 0, 1, 3)
        self.line_2 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 3)
        self.widget_coder = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_coder.sizePolicy().hasHeightForWidth())
        self.widget_coder.setSizePolicy(sizePolicy)
        self.widget_coder.setObjectName("widget_coder")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_coder)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox_coders = QtWidgets.QComboBox(parent=self.widget_coder)
        self.comboBox_coders.setObjectName("comboBox_coders")
        self.gridLayout_2.addWidget(self.comboBox_coders, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.widget_coder)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_new_coder = QtWidgets.QLabel(parent=self.widget_coder)
        self.label_new_coder.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_new_coder.setObjectName("label_new_coder")
        self.gridLayout_2.addWidget(self.label_new_coder, 3, 0, 1, 1)
        self.lineEdit_coderName = QtWidgets.QLineEdit(parent=self.widget_coder)
        self.lineEdit_coderName.setObjectName("lineEdit_coderName")
        self.gridLayout_2.addWidget(self.lineEdit_coderName, 3, 1, 1, 1)
        self.pushButton_set_coder = QtWidgets.QPushButton(parent=self.widget_coder)
        self.pushButton_set_coder.setObjectName("pushButton_set_coder")
        self.gridLayout_2.addWidget(self.pushButton_set_coder, 3, 2, 1, 1)
        self.label_current_coder = QtWidgets.QLabel(parent=self.widget_coder)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_current_coder.sizePolicy().hasHeightForWidth())
        self.label_current_coder.setSizePolicy(sizePolicy)
        self.label_current_coder.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_current_coder.setObjectName("label_current_coder")
        self.gridLayout_2.addWidget(self.label_current_coder, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 3, 3, 1, 1)
        self.gridLayout.addWidget(self.widget_coder, 0, 0, 1, 1)
        self.label_directory = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_directory.setObjectName("label_directory")
        self.gridLayout.addWidget(self.label_directory, 6, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Dialog_settings)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog_settings)
        self.buttonBox.accepted.connect(Dialog_settings.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog_settings.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog_settings)

    def retranslateUi(self, Dialog_settings):
        _translate = QtCore.QCoreApplication.translate
        Dialog_settings.setWindowTitle(_translate("Dialog_settings", "Settings"))
        self.label_9.setText(_translate("Dialog_settings", "AI Integration"))
        self.checkBox_AI_enable.setText(_translate("Dialog_settings", "enable AI integration"))
        self.label_10.setText(_translate("Dialog_settings", "AI Model"))
        self.label_openai_api_key.setText(_translate("Dialog_settings", "API key"))
        self.checkBox_ai_project_memo.setToolTip(_translate("Dialog_settings", "You can use the Project Memo (found in the menu: Project > Project Memo) to convey background information about your research, including objectives, methodology, and data, to the AI. This will help the AI generate more accurate and relevant responses. Deselect this option if you use the Project Memo for other purposes."))
        self.checkBox_ai_project_memo.setText(_translate("Dialog_settings", "Send project memo to AI"))
        self.label_4.setText(_translate("Dialog_settings", "Language"))
        self.comboBox_language.setToolTip(_translate("Dialog_settings", "<html><head/><body><p>Close and open the software for the change in language to occur.</p></body></html>"))
        self.label.setText(_translate("Dialog_settings", "General font and size"))
        self.label_3.setText(_translate("Dialog_settings", "Font size for codes tree"))
        self.label_7.setText(_translate("Dialog_settings", "Font size for documents"))
        self.label_reports_text_context.setText(_translate("Dialog_settings", "Reports with text context"))
        self.label_chars_before_after.setText(_translate("Dialog_settings", "Characters before and after"))
        self.label_coded_text_style.setText(_translate("Dialog_settings", "Text context, coded text style"))
        self.checkBox.setToolTip(_translate("Dialog_settings", "<html><head/><body><p>Show the identifying numbers for files, cases, codes, et cetera.</p></body></html>"))
        self.checkBox.setText(_translate("Dialog_settings", "Show IDs"))
        self.comboBox_text_chunk_size.setItemText(0, _translate("Dialog_settings", "50000"))
        self.comboBox_text_chunk_size.setItemText(1, _translate("Dialog_settings", "40000"))
        self.comboBox_text_chunk_size.setItemText(2, _translate("Dialog_settings", "30000"))
        self.comboBox_text_chunk_size.setItemText(3, _translate("Dialog_settings", "20000"))
        self.label_style.setText(_translate("Dialog_settings", "Style"))
        self.label_8.setToolTip(_translate("Dialog_settings", "Very large text documents. Load text chunks by number of characters."))
        self.label_8.setText(_translate("Dialog_settings", "Code text chunk size"))
        self.label_5.setToolTip(_translate("Dialog_settings", "<html><head/><body><p>Used when entering time position in transcription</p></body></html>"))
        self.label_5.setText(_translate("Dialog_settings", "Time format"))
        self.label_6.setToolTip(_translate("Dialog_settings", "<html><head/><body><p>Used when entering speaker name in transcription</p></body></html>"))
        self.label_6.setText(_translate("Dialog_settings", "Speaker format"))
        self.pushButton_choose_directory.setText(_translate("Dialog_settings", "Default project directory"))
        self.checkBox_backup_AV_files.setText(_translate("Dialog_settings", "Backup video and audio files. Uncheck to speed up backups.\n"
"Not recommended unless you have many large files slowing the backup."))
        self.checkBox_auto_backup.setText(_translate("Dialog_settings", "Backup project folder every time project is opened"))
        self.label_backups_to_keep.setText(_translate("Dialog_settings", "Backups"))
        self.label_2.setToolTip(_translate("Dialog_settings", "Select another coder in this project"))
        self.label_2.setText(_translate("Dialog_settings", "Other coders"))
        self.label_new_coder.setText(_translate("Dialog_settings", "New coder"))
        self.pushButton_set_coder.setToolTip(_translate("Dialog_settings", "Set this name as the current coder.\n"
""))
        self.pushButton_set_coder.setText(_translate("Dialog_settings", "Apply"))
        self.label_current_coder.setText(_translate("Dialog_settings", "Current coder: "))
        self.label_directory.setText(_translate("Dialog_settings", "/"))
