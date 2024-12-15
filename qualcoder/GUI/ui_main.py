# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_action_log = QtWidgets.QWidget()
        self.tab_action_log.setObjectName("tab_action_log")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_action_log)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit = QtWidgets.QTextEdit(parent=self.tab_action_log)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_action_log, "")
        self.tab_manage = QtWidgets.QWidget()
        self.tab_manage.setObjectName("tab_manage")
        self.label_manage = QtWidgets.QLabel(parent=self.tab_manage)
        self.label_manage.setGeometry(QtCore.QRect(20, 20, 861, 71))
        self.label_manage.setWordWrap(True)
        self.label_manage.setObjectName("label_manage")
        self.tabWidget.addTab(self.tab_manage, "")
        self.tab_coding = QtWidgets.QWidget()
        self.tab_coding.setObjectName("tab_coding")
        self.label_coding = QtWidgets.QLabel(parent=self.tab_coding)
        self.label_coding.setGeometry(QtCore.QRect(20, 20, 811, 71))
        self.label_coding.setWordWrap(True)
        self.label_coding.setObjectName("label_coding")
        self.tabWidget.addTab(self.tab_coding, "")
        self.tab_reports = QtWidgets.QWidget()
        self.tab_reports.setObjectName("tab_reports")
        self.label_reports = QtWidgets.QLabel(parent=self.tab_reports)
        self.label_reports.setGeometry(QtCore.QRect(20, 20, 831, 71))
        self.label_reports.setWordWrap(True)
        self.label_reports.setObjectName("label_reports")
        self.tabWidget.addTab(self.tab_reports, "")
        self.tab_ai_chat = QtWidgets.QWidget()
        self.tab_ai_chat.setObjectName("tab_ai_chat")
        self.tabWidget.addTab(self.tab_ai_chat, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 26))
        self.menubar.setObjectName("menubar")
        self.menuProject = QtWidgets.QMenu(parent=self.menubar)
        self.menuProject.setObjectName("menuProject")
        self.menuOpen_Recent_Project = QtWidgets.QMenu(parent=self.menuProject)
        self.menuOpen_Recent_Project.setObjectName("menuOpen_Recent_Project")
        self.menuExport = QtWidgets.QMenu(parent=self.menuProject)
        self.menuExport.setObjectName("menuExport")
        self.menuImport = QtWidgets.QMenu(parent=self.menuProject)
        self.menuImport.setObjectName("menuImport")
        self.menuFiles_and_Cases = QtWidgets.QMenu(parent=self.menubar)
        self.menuFiles_and_Cases.setObjectName("menuFiles_and_Cases")
        self.menuCoding = QtWidgets.QMenu(parent=self.menubar)
        self.menuCoding.setObjectName("menuCoding")
        self.menuReports = QtWidgets.QMenu(parent=self.menubar)
        self.menuReports.setObjectName("menuReports")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAI = QtWidgets.QMenu(parent=self.menubar)
        self.menuAI.setObjectName("menuAI")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCreate_New_Project = QtGui.QAction(parent=MainWindow)
        self.actionCreate_New_Project.setObjectName("actionCreate_New_Project")
        self.actionOpen_Project = QtGui.QAction(parent=MainWindow)
        self.actionOpen_Project.setObjectName("actionOpen_Project")
        self.actionClose_Project = QtGui.QAction(parent=MainWindow)
        self.actionClose_Project.setObjectName("actionClose_Project")
        self.actionProject_Memo = QtGui.QAction(parent=MainWindow)
        self.actionProject_Memo.setObjectName("actionProject_Memo")
        self.actionSettings = QtGui.QAction(parent=MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionManage_files = QtGui.QAction(parent=MainWindow)
        self.actionManage_files.setObjectName("actionManage_files")
        self.actionManage_cases = QtGui.QAction(parent=MainWindow)
        self.actionManage_cases.setObjectName("actionManage_cases")
        self.actionFile_categories = QtGui.QAction(parent=MainWindow)
        self.actionFile_categories.setObjectName("actionFile_categories")
        self.actionManage_journals = QtGui.QAction(parent=MainWindow)
        self.actionManage_journals.setObjectName("actionManage_journals")
        self.actionCodes = QtGui.QAction(parent=MainWindow)
        self.actionCodes.setObjectName("actionCodes")
        self.actionCategories = QtGui.QAction(parent=MainWindow)
        self.actionCategories.setObjectName("actionCategories")
        self.actionCodebook = QtGui.QAction(parent=MainWindow)
        self.actionCodebook.setObjectName("actionCodebook")
        self.actionAssign_Attributes = QtGui.QAction(parent=MainWindow)
        self.actionAssign_Attributes.setObjectName("actionAssign_Attributes")
        self.actionManage_Attributes = QtGui.QAction(parent=MainWindow)
        self.actionManage_Attributes.setObjectName("actionManage_Attributes")
        self.actionImport_Attributes = QtGui.QAction(parent=MainWindow)
        self.actionImport_Attributes.setObjectName("actionImport_Attributes")
        self.actionCoding_reports = QtGui.QAction(parent=MainWindow)
        self.actionCoding_reports.setObjectName("actionCoding_reports")
        self.actionCoding_summary = QtGui.QAction(parent=MainWindow)
        self.actionCoding_summary.setObjectName("actionCoding_summary")
        self.actionSQL_statements = QtGui.QAction(parent=MainWindow)
        self.actionSQL_statements.setObjectName("actionSQL_statements")
        self.actionContents = QtGui.QAction(parent=MainWindow)
        self.actionContents.setObjectName("actionContents")
        self.actionAbout = QtGui.QAction(parent=MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionImport_survey = QtGui.QAction(parent=MainWindow)
        self.actionImport_survey.setObjectName("actionImport_survey")
        self.actionManage_attributes = QtGui.QAction(parent=MainWindow)
        self.actionManage_attributes.setObjectName("actionManage_attributes")
        self.actionFrequency_table = QtGui.QAction(parent=MainWindow)
        self.actionFrequency_table.setObjectName("actionFrequency_table")
        self.actionCoding_comparison = QtGui.QAction(parent=MainWindow)
        self.actionCoding_comparison.setObjectName("actionCoding_comparison")
        self.actionText_mining = QtGui.QAction(parent=MainWindow)
        self.actionText_mining.setObjectName("actionText_mining")
        self.actionView_Graph = QtGui.QAction(parent=MainWindow)
        self.actionView_Graph.setObjectName("actionView_Graph")
        self.actionExport_codebook = QtGui.QAction(parent=MainWindow)
        self.actionExport_codebook.setObjectName("actionExport_codebook")
        self.actionCode_image = QtGui.QAction(parent=MainWindow)
        self.actionCode_image.setObjectName("actionCode_image")
        self.actionCode_frequencies = QtGui.QAction(parent=MainWindow)
        self.actionCode_frequencies.setObjectName("actionCode_frequencies")
        self.actionCoding_Matrix = QtGui.QAction(parent=MainWindow)
        self.actionCoding_Matrix.setObjectName("actionCoding_Matrix")
        self.actionCode_audio_video = QtGui.QAction(parent=MainWindow)
        self.actionCode_audio_video.setObjectName("actionCode_audio_video")
        self.actionProject_Exchange_Export = QtGui.QAction(parent=MainWindow)
        self.actionProject_Exchange_Export.setObjectName("actionProject_Exchange_Export")
        self.actionREFI_Codebook_export = QtGui.QAction(parent=MainWindow)
        self.actionREFI_Codebook_export.setObjectName("actionREFI_Codebook_export")
        self.actionREFI_Codebook_import = QtGui.QAction(parent=MainWindow)
        self.actionREFI_Codebook_import.setObjectName("actionREFI_Codebook_import")
        self.actionREFI_QDA_Project_import = QtGui.QAction(parent=MainWindow)
        self.actionREFI_QDA_Project_import.setObjectName("actionREFI_QDA_Project_import")
        self.actionRQDA_Project_import = QtGui.QAction(parent=MainWindow)
        self.actionRQDA_Project_import.setObjectName("actionRQDA_Project_import")
        self.actionProject_summary = QtGui.QAction(parent=MainWindow)
        self.actionProject_summary.setObjectName("actionProject_summary")
        self.actionNone = QtGui.QAction(parent=MainWindow)
        self.actionNone.setObjectName("actionNone")
        self.actionCode_relations = QtGui.QAction(parent=MainWindow)
        self.actionCode_relations.setObjectName("actionCode_relations")
        self.actionExport_coded_text_as_html = QtGui.QAction(parent=MainWindow)
        self.actionExport_coded_text_as_html.setObjectName("actionExport_coded_text_as_html")
        self.actionManage_bad_links_to_files = QtGui.QAction(parent=MainWindow)
        self.actionManage_bad_links_to_files.setEnabled(False)
        self.actionManage_bad_links_to_files.setObjectName("actionManage_bad_links_to_files")
        self.actionSpecial_functions = QtGui.QAction(parent=MainWindow)
        self.actionSpecial_functions.setObjectName("actionSpecial_functions")
        self.actionFile_summary = QtGui.QAction(parent=MainWindow)
        self.actionFile_summary.setObjectName("actionFile_summary")
        self.actionCode_summary = QtGui.QAction(parent=MainWindow)
        self.actionCode_summary.setObjectName("actionCode_summary")
        self.actionCoding_comparison_by_file = QtGui.QAction(parent=MainWindow)
        self.actionCoding_comparison_by_file.setObjectName("actionCoding_comparison_by_file")
        self.actionCode_by_case = QtGui.QAction(parent=MainWindow)
        self.actionCode_by_case.setObjectName("actionCode_by_case")
        self.actionCharts = QtGui.QAction(parent=MainWindow)
        self.actionCharts.setObjectName("actionCharts")
        self.actionExport_codebook_with_memos = QtGui.QAction(parent=MainWindow)
        self.actionExport_codebook_with_memos.setObjectName("actionExport_codebook_with_memos")
        self.actionImport_references_RIS_format = QtGui.QAction(parent=MainWindow)
        self.actionImport_references_RIS_format.setObjectName("actionImport_references_RIS_format")
        self.actionManage_references = QtGui.QAction(parent=MainWindow)
        self.actionManage_references.setObjectName("actionManage_references")
        self.actionColour_scheme = QtGui.QAction(parent=MainWindow)
        self.actionColour_scheme.setObjectName("actionColour_scheme")
        self.actionImport_plain_text_codes_list = QtGui.QAction(parent=MainWindow)
        self.actionImport_plain_text_codes_list.setObjectName("actionImport_plain_text_codes_list")
        self.actionImport_survey_2 = QtGui.QAction(parent=MainWindow)
        self.actionImport_survey_2.setObjectName("actionImport_survey_2")
        self.actionMenu_Key_Shortcuts = QtGui.QAction(parent=MainWindow)
        self.actionMenu_Key_Shortcuts.setObjectName("actionMenu_Key_Shortcuts")
        self.actionImport_twitter_data = QtGui.QAction(parent=MainWindow)
        self.actionImport_twitter_data.setObjectName("actionImport_twitter_data")
        self.actionCode_pdf = QtGui.QAction(parent=MainWindow)
        self.actionCode_pdf.setObjectName("actionCode_pdf")
        self.actionCode_text_exact_matches = QtGui.QAction(parent=MainWindow)
        self.actionCode_text_exact_matches.setObjectName("actionCode_text_exact_matches")
        self.actionAI_Setup_wizard = QtGui.QAction(parent=MainWindow)
        self.actionAI_Setup_wizard.setObjectName("actionAI_Setup_wizard")
        self.actionAI_Rebuild_internal_memory = QtGui.QAction(parent=MainWindow)
        self.actionAI_Rebuild_internal_memory.setObjectName("actionAI_Rebuild_internal_memory")
        self.actionAI_Edit_Project_Memo = QtGui.QAction(parent=MainWindow)
        self.actionAI_Edit_Project_Memo.setObjectName("actionAI_Edit_Project_Memo")
        self.actionAI_Chat = QtGui.QAction(parent=MainWindow)
        self.actionAI_Chat.setObjectName("actionAI_Chat")
        self.actionAI_Search_and_Coding = QtGui.QAction(parent=MainWindow)
        self.actionAI_Search_and_Coding.setObjectName("actionAI_Search_and_Coding")
        self.actionAI_Settings = QtGui.QAction(parent=MainWindow)
        self.actionAI_Settings.setObjectName("actionAI_Settings")
        self.actionAI_Prompts = QtGui.QAction(parent=MainWindow)
        self.actionAI_Prompts.setObjectName("actionAI_Prompts")
        self.actionCode_organiser = QtGui.QAction(parent=MainWindow)
        self.actionCode_organiser.setObjectName("actionCode_organiser")
        self.actionText_segments_by_codes = QtGui.QAction(parent=MainWindow)
        self.actionText_segments_by_codes.setObjectName("actionText_segments_by_codes")
        self.actionAI_assisted_coding = QtGui.QAction(parent=MainWindow)
        self.actionAI_assisted_coding.setObjectName("actionAI_assisted_coding")
        self.menuOpen_Recent_Project.addAction(self.actionNone)
        self.menuExport.addAction(self.actionProject_Exchange_Export)
        self.menuExport.addAction(self.actionREFI_Codebook_export)
        self.menuExport.addAction(self.actionExport_codebook)
        self.menuExport.addAction(self.actionExport_codebook_with_memos)
        self.menuImport.addAction(self.actionREFI_Codebook_import)
        self.menuImport.addAction(self.actionREFI_QDA_Project_import)
        self.menuImport.addAction(self.actionRQDA_Project_import)
        self.menuImport.addAction(self.actionImport_plain_text_codes_list)
        self.menuProject.addAction(self.actionCreate_New_Project)
        self.menuProject.addAction(self.actionOpen_Project)
        self.menuProject.addAction(self.menuOpen_Recent_Project.menuAction())
        self.menuProject.addAction(self.actionClose_Project)
        self.menuProject.addAction(self.actionProject_Memo)
        self.menuProject.addAction(self.actionSettings)
        self.menuProject.addAction(self.actionProject_summary)
        self.menuProject.addSeparator()
        self.menuProject.addAction(self.menuImport.menuAction())
        self.menuProject.addAction(self.menuExport.menuAction())
        self.menuProject.addSeparator()
        self.menuProject.addAction(self.actionExit)
        self.menuFiles_and_Cases.addAction(self.actionManage_files)
        self.menuFiles_and_Cases.addAction(self.actionManage_cases)
        self.menuFiles_and_Cases.addAction(self.actionManage_journals)
        self.menuFiles_and_Cases.addAction(self.actionManage_attributes)
        self.menuFiles_and_Cases.addAction(self.actionManage_references)
        self.menuFiles_and_Cases.addAction(self.actionImport_survey_2)
        self.menuFiles_and_Cases.addAction(self.actionManage_bad_links_to_files)
        self.menuFiles_and_Cases.addAction(self.actionImport_twitter_data)
        self.menuCoding.addAction(self.actionCodes)
        self.menuCoding.addAction(self.actionCode_image)
        self.menuCoding.addAction(self.actionCode_audio_video)
        self.menuCoding.addAction(self.actionCode_pdf)
        self.menuCoding.addAction(self.actionColour_scheme)
        self.menuCoding.addAction(self.actionCode_organiser)
        self.menuCoding.addAction(self.actionAI_assisted_coding)
        self.menuReports.addAction(self.actionCoding_reports)
        self.menuReports.addAction(self.actionCoding_comparison)
        self.menuReports.addAction(self.actionCoding_comparison_by_file)
        self.menuReports.addAction(self.actionCode_frequencies)
        self.menuReports.addAction(self.actionFile_summary)
        self.menuReports.addAction(self.actionCode_summary)
        self.menuReports.addAction(self.actionCode_relations)
        self.menuReports.addAction(self.actionCode_text_exact_matches)
        self.menuReports.addAction(self.actionText_segments_by_codes)
        self.menuReports.addAction(self.actionView_Graph)
        self.menuReports.addAction(self.actionCharts)
        self.menuReports.addAction(self.actionText_mining)
        self.menuReports.addAction(self.actionSQL_statements)
        self.menuReports.addSeparator()
        self.menuHelp.addAction(self.actionContents)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionSpecial_functions)
        self.menuHelp.addAction(self.actionMenu_Key_Shortcuts)
        self.menuAI.addAction(self.actionAI_Setup_wizard)
        self.menuAI.addAction(self.actionAI_Settings)
        self.menuAI.addAction(self.actionAI_Rebuild_internal_memory)
        self.menuAI.addAction(self.actionAI_Edit_Project_Memo)
        self.menuAI.addAction(self.actionAI_Prompts)
        self.menuAI.addSeparator()
        self.menuAI.addAction(self.actionAI_Chat)
        self.menuAI.addAction(self.actionAI_Search_and_Coding)
        self.menubar.addAction(self.menuProject.menuAction())
        self.menubar.addAction(self.menuFiles_and_Cases.menuAction())
        self.menubar.addAction(self.menuCoding.menuAction())
        self.menubar.addAction(self.menuReports.menuAction())
        self.menubar.addAction(self.menuAI.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QualCoder"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_action_log), _translate("MainWindow", "Action Log"))
        self.label_manage.setText(_translate("MainWindow", "Select an option in the Files and Cases menu. "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_manage), _translate("MainWindow", "Manage"))
        self.label_coding.setText(_translate("MainWindow", "Select an option in the Coding menu. "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_coding), _translate("MainWindow", "Coding"))
        self.label_reports.setText(_translate("MainWindow", "Select an option in the Reports menu. "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_reports), _translate("MainWindow", "Reports"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ai_chat), _translate("MainWindow", "AI Chat"))
        self.menuProject.setTitle(_translate("MainWindow", "Project"))
        self.menuOpen_Recent_Project.setTitle(_translate("MainWindow", "Open Recent Project"))
        self.menuExport.setTitle(_translate("MainWindow", "Export"))
        self.menuImport.setTitle(_translate("MainWindow", "Import"))
        self.menuFiles_and_Cases.setTitle(_translate("MainWindow", "Manage"))
        self.menuCoding.setTitle(_translate("MainWindow", "Coding"))
        self.menuReports.setTitle(_translate("MainWindow", "Reports"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuAI.setTitle(_translate("MainWindow", "AI"))
        self.actionCreate_New_Project.setText(_translate("MainWindow", "Create New Project"))
        self.actionOpen_Project.setText(_translate("MainWindow", "Open Project"))
        self.actionClose_Project.setText(_translate("MainWindow", "Close Project"))
        self.actionProject_Memo.setText(_translate("MainWindow", "Project Memo"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionManage_files.setText(_translate("MainWindow", "Manage files"))
        self.actionManage_cases.setText(_translate("MainWindow", "Manage cases"))
        self.actionFile_categories.setText(_translate("MainWindow", "File categories"))
        self.actionManage_journals.setText(_translate("MainWindow", "Manage journals"))
        self.actionCodes.setText(_translate("MainWindow", "Code text"))
        self.actionCategories.setText(_translate("MainWindow", "Categories"))
        self.actionCodebook.setText(_translate("MainWindow", "Codebook"))
        self.actionAssign_Attributes.setText(_translate("MainWindow", "Assign Attributes"))
        self.actionManage_Attributes.setText(_translate("MainWindow", "Manage Attributes"))
        self.actionImport_Attributes.setText(_translate("MainWindow", "Import Attributes"))
        self.actionCoding_reports.setText(_translate("MainWindow", "Coding reports"))
        self.actionCoding_summary.setText(_translate("MainWindow", "Coding summary"))
        self.actionSQL_statements.setText(_translate("MainWindow", "Database queries"))
        self.actionContents.setText(_translate("MainWindow", "Contents"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionImport_survey.setText(_translate("MainWindow", "Import survey"))
        self.actionManage_attributes.setText(_translate("MainWindow", "Manage attributes"))
        self.actionFrequency_table.setText(_translate("MainWindow", "Frequency table"))
        self.actionCoding_comparison.setText(_translate("MainWindow", "Coding comparison"))
        self.actionText_mining.setText(_translate("MainWindow", "Text mining"))
        self.actionView_Graph.setText(_translate("MainWindow", "View Graph"))
        self.actionExport_codebook.setText(_translate("MainWindow", "Export codebook as ODT file"))
        self.actionCode_image.setText(_translate("MainWindow", "Code image"))
        self.actionCode_frequencies.setText(_translate("MainWindow", "Code frequencies"))
        self.actionCoding_Matrix.setText(_translate("MainWindow", "Coding Matrix"))
        self.actionCode_audio_video.setText(_translate("MainWindow", "Code audio/video"))
        self.actionProject_Exchange_Export.setText(_translate("MainWindow", "REFI-QDA Project export"))
        self.actionProject_Exchange_Export.setToolTip(_translate("MainWindow", "REFI-QDA Project export"))
        self.actionREFI_Codebook_export.setText(_translate("MainWindow", "REFI-QDA Codebook export"))
        self.actionREFI_Codebook_import.setText(_translate("MainWindow", "REFI-QDA Codebook import"))
        self.actionREFI_QDA_Project_import.setText(_translate("MainWindow", "REFI-QDA Project import"))
        self.actionRQDA_Project_import.setText(_translate("MainWindow", "RQDA Project import"))
        self.actionProject_summary.setText(_translate("MainWindow", "Project summary"))
        self.actionNone.setText(_translate("MainWindow", "None"))
        self.actionCode_relations.setText(_translate("MainWindow", "Code relations"))
        self.actionExport_coded_text_as_html.setText(_translate("MainWindow", "Export coded text as html"))
        self.actionManage_bad_links_to_files.setText(_translate("MainWindow", "Manage bad links to files"))
        self.actionSpecial_functions.setText(_translate("MainWindow", "Special functions"))
        self.actionFile_summary.setText(_translate("MainWindow", "File summary"))
        self.actionCode_summary.setText(_translate("MainWindow", "Code summary"))
        self.actionCoding_comparison_by_file.setText(_translate("MainWindow", "Coding comparison by file"))
        self.actionCode_by_case.setText(_translate("MainWindow", "Code by case"))
        self.actionCharts.setText(_translate("MainWindow", "Charts"))
        self.actionExport_codebook_with_memos.setText(_translate("MainWindow", "Export codebook with memos as ODT file"))
        self.actionImport_references_RIS_format.setText(_translate("MainWindow", "Import references RIS format"))
        self.actionManage_references.setText(_translate("MainWindow", "Manage references"))
        self.actionColour_scheme.setText(_translate("MainWindow", "Colour scheme"))
        self.actionImport_plain_text_codes_list.setText(_translate("MainWindow", "Import plain text codes list"))
        self.actionImport_survey_2.setText(_translate("MainWindow", "Import survey"))
        self.actionMenu_Key_Shortcuts.setText(_translate("MainWindow", "Menu Key Shortcuts"))
        self.actionImport_twitter_data.setText(_translate("MainWindow", "Import twitter data"))
        self.actionCode_pdf.setText(_translate("MainWindow", "Code pdf"))
        self.actionCode_text_exact_matches.setText(_translate("MainWindow", "Code text exact matches"))
        self.actionAI_Setup_wizard.setText(_translate("MainWindow", "Setup Wizard"))
        self.actionAI_Rebuild_internal_memory.setText(_translate("MainWindow", "Rebuild Internal Memory"))
        self.actionAI_Edit_Project_Memo.setText(_translate("MainWindow", "Project Memo"))
        self.actionAI_Chat.setText(_translate("MainWindow", "AI Chat"))
        self.actionAI_Search_and_Coding.setText(_translate("MainWindow", "AI Assisted Coding"))
        self.actionAI_Settings.setText(_translate("MainWindow", "Settings"))
        self.actionAI_Settings.setToolTip(_translate("MainWindow", "AI related Settings"))
        self.actionAI_Prompts.setText(_translate("MainWindow", "Prompt library"))
        self.actionCode_organiser.setText(_translate("MainWindow", "Code organiser"))
        self.actionText_segments_by_codes.setText(_translate("MainWindow", "Codes by text segments"))
        self.actionAI_assisted_coding.setText(_translate("MainWindow", "AI assisted coding"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
