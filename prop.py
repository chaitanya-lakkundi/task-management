# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Properties.ui'

from PyQt5 import QtCore, QtGui, QtWidgets
import shelve,time
import mainwin, task_settings

class Ui_Properties_dialog(object):
    def setupUi(self, Properties_dialog, MainWindow_Ui):
        self.MainWindow_Ui = MainWindow_Ui
        self.Prop_Ui = Properties_dialog
        Properties_dialog.setObjectName("Properties_dialog")
        Properties_dialog.resize(573, 566)
        font = QtGui.QFont()
        font.setPointSize(15)
        Properties_dialog.setFont(font)
        self.formLayoutWidget = QtWidgets.QWidget(Properties_dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 551, 551))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName("formLayout")
        self.task_name_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.task_name_label.setObjectName("task_name_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.task_name_label)
        self.task_name_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.task_name_lineEdit.setObjectName("task_name_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.task_name_lineEdit)
        self.priority_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.priority_label.setObjectName("priority_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.priority_label)
        self.priority_spinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.priority_spinBox.setObjectName("priority_spinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.priority_spinBox)
        self.start_date_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.start_date_label.setObjectName("start_date_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.start_date_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.start_date_dateEdit = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.start_date_dateEdit.setCalendarPopup(True)
        self.start_date_dateEdit.setDate(QtCore.QDate(2016, 3, 24))
        self.start_date_dateEdit.setObjectName("start_date_dateEdit")
        self.horizontalLayout_2.addWidget(self.start_date_dateEdit)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.deadline_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.deadline_label.setObjectName("deadline_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.deadline_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.deadline_dateEdit = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.deadline_dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.deadline_dateEdit.setCalendarPopup(True)
        self.deadline_dateEdit.setObjectName("deadline_dateEdit")
        self.horizontalLayout.addWidget(self.deadline_dateEdit)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.progress_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.progress_label.setObjectName("progress_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.progress_label)
        self.progress_progressBar = QtWidgets.QProgressBar(self.formLayoutWidget)
        self.progress_progressBar.setProperty("value", 0)
        self.progress_progressBar.setObjectName("progress_progressBar")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.progress_progressBar)
        self.resources_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.resources_label.setObjectName("resources_label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.resources_label)
        self.resources_plainTextEdit = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.resources_plainTextEdit.setObjectName("resources_plainTextEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.resources_plainTextEdit)
        self.save_details_pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.save_details_pushButton.setObjectName("save_details_pushButton")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.save_details_pushButton)
        self.project_started_checkBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.project_started_checkBox.setObjectName("project_started_checkBox")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.project_started_checkBox)
        self.description_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.description_label.setObjectName("description_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.description_label)
        self.description_textEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.description_textEdit.setObjectName("description_textEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.description_textEdit) 
        self.new_details = True
        self.id_of_task = 0
        #   
        self.save_details_pushButton.clicked.connect(self.saveAllDetails)
#        self.save_details_pushButton.clicked.connect(Properties_dialog.close)
        self.start_date_dateEdit.setDate(QtCore.QDate.currentDate())
        self.deadline_dateEdit.setDate(QtCore.QDate.currentDate())

        self.retranslateUi(Properties_dialog)
        QtCore.QMetaObject.connectSlotsByName(Properties_dialog)
        Properties_dialog.setTabOrder(self.task_name_lineEdit, self.description_textEdit)
        Properties_dialog.setTabOrder(self.description_textEdit, self.priority_spinBox)
        Properties_dialog.setTabOrder(self.priority_spinBox, self.start_date_dateEdit)
        Properties_dialog.setTabOrder(self.start_date_dateEdit, self.deadline_dateEdit)
        Properties_dialog.setTabOrder(self.deadline_dateEdit, self.resources_plainTextEdit)
        Properties_dialog.setTabOrder(self.resources_plainTextEdit, self.project_started_checkBox)
        Properties_dialog.setTabOrder(self.project_started_checkBox, self.save_details_pushButton)
        print "setup_Ui PropWindow"

    def retranslateUi(self, Properties_dialog):
        _translate = QtCore.QCoreApplication.translate
        Properties_dialog.setWindowTitle(_translate("Properties_dialog", "Properties"))
        self.task_name_label.setText(_translate("Properties_dialog", "Task Name *"))
        self.priority_label.setText(_translate("Properties_dialog", "Priority"))
        self.start_date_label.setText(_translate("Properties_dialog", "Start Date"))
        self.deadline_label.setText(_translate("Properties_dialog", "Deadline"))
        self.progress_label.setText(_translate("Properties_dialog", "Progress"))
        self.resources_label.setText(_translate("Properties_dialog", "Resources"))
        self.save_details_pushButton.setText(_translate("Properties_dialog", "Save Details"))
        self.project_started_checkBox.setText(_translate("Properties_dialog", "Project Yet to START"))
        self.description_label.setText(_translate("Properties_dialog", "Description"))
        
    def saveAllDetails(self):
        #Here save all details in a file. Use Pickle
        details={}
        #a dict of all details
        if self.task_name_lineEdit.text() == "":
            self.task_name_lineEdit.setPlaceholderText("Task name cannot be empty")
            return
        details['task_name']    = self.task_name_lineEdit.text()
        details['description']  = self.description_textEdit.toPlainText()
        details['priority']     = self.priority_spinBox.value()
        details['start_date']   = self.start_date_dateEdit.date()
        details['deadline_date']= self.deadline_dateEdit.date()
        details['resources']    = self.resources_plainTextEdit.toPlainText()
        details['started_check']= self.project_started_checkBox.checkState()
        if (self.new_details == True):
            details['id'] = int(time.time())
        else:
            details['id'] = self.id_of_task
        #save into database file

        d = shelve.open(task_settings.get_path()+"database")
        d[str(details['id'])] = details
        d.close()
#        mainwin.load_task_names_external(self.MainWindow_Ui)
        self.MainWindow_Ui.load_task_names()
        self.MainWindow_Ui.calculate_progress()
        self.Prop_Ui.close()
        
    def loadAllDetails(self,required_task_id,only_progress = False):
        #Here save all details in a file. Use shelve
        d = shelve.open(task_settings.get_path()+"database")
        details={}
        print "Required TaskId : ",str(required_task_id)
        try:
            details = d[required_task_id]
        except KeyError:
            self.resetAllDetails()
            print "Key does not exist"
            return
        finally:
            d.close()
            
        progress = 0
        if details['started_check'] == False:
            total_days = details['start_date'].daysTo(details['deadline_date'])
            days_rem = total_days - QtCore.QDate.currentDate().daysTo(details['deadline_date'])
            print "Days remaining = ",days_rem
            try:
                progress = days_rem*100/total_days
            except ZeroDivisionError:
                progress = 0
            print "Progress ",progress,"%"
        else:
            progress = 0
 
        if only_progress == True:
            return progress
                                                    
        #a dict of all details
        self.id_of_task = details['id']
        self.task_name_lineEdit.setText(details['task_name'])
        self.description_textEdit.setPlainText(details['description'])
        self.priority_spinBox.setValue(details['priority'])
        self.start_date_dateEdit.setDate(details['start_date'])
        self.deadline_dateEdit.setDate(details['deadline_date'])
        self.resources_plainTextEdit.setPlainText(details['resources'])
        self.project_started_checkBox.setCheckState(details['started_check'])
        self.progress_progressBar.setValue(int(progress))

    def resetAllDetails(self):        
        self.task_name_lineEdit.setText("")
        self.description_textEdit.setPlainText("")
        self.set_priority_value()
        self.start_date_dateEdit.setDate(QtCore.QDate.currentDate())
        self.deadline_dateEdit.setDate(QtCore.QDate.currentDate())
        self.resources_plainTextEdit.setPlainText("")
        self.project_started_checkBox.setCheckState(False)
        self.progress_progressBar.setValue(0)

    def set_priority_value(self):
        count=0
        try:
            d = shelve.open(task_settings.get_path()+"database")
            count = len(d.keys())
            print "Count = ",count
        except IOError:
            print "Database file does not exist"
        finally:
            d.close()
        count+=1
        self.priority_spinBox.setValue(count)

        print "Set priority value = ",count
        
def getObject():
    return Ui_Properties_dialog()
