# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Archives.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import shelve
import task_settings
class Ui_tasks_TabWidget(object):
    def setupUi(self, tasks_TabWidget):
        self.window = tasks_TabWidget
        tasks_TabWidget.setObjectName("tasks_TabWidget")
        tasks_TabWidget.setWindowModality(QtCore.Qt.WindowModal)
        tasks_TabWidget.resize(467, 414)
        tasks_TabWidget.setAcceptDrops(False)
        tasks_TabWidget.setMovable(True)
        self.ongoing_tab = QtWidgets.QWidget()
        self.ongoing_tab.setObjectName("ongoing_tab")
        self.ongoing_treeWidget = QtWidgets.QTreeWidget(self.ongoing_tab)
        self.ongoing_treeWidget.setGeometry(QtCore.QRect(0, 0, 461, 381))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ongoing_treeWidget.setFont(font)
        self.ongoing_treeWidget.setObjectName("ongoing_treeWidget")
        tasks_TabWidget.addTab(self.ongoing_tab, "")
        self.completed_tab = QtWidgets.QWidget()
        self.completed_tab.setObjectName("completed_tab")
        self.completed_treeWidget = QtWidgets.QTreeWidget(self.completed_tab)
        self.completed_treeWidget.setGeometry(QtCore.QRect(0, 0, 461, 381))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.completed_treeWidget.setFont(font)
        self.completed_treeWidget.setObjectName("completed_treeWidget")
        tasks_TabWidget.addTab(self.completed_tab, "")

        self.retranslateUi(tasks_TabWidget)
        tasks_TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(tasks_TabWidget)
    
    def set_completed(self):
        self.completed_treeWidget.clear()
        self.ongoing_treeWidget.clear()
        self.load_task_names()
        self.window.setCurrentIndex(1)
        
    def set_ongoing(self):
        self.completed_treeWidget.clear()
        self.ongoing_treeWidget.clear()
        self.load_task_names()
        self.window.setCurrentIndex(0)
    
    def load_task_names(self):
        #Here save all details in a file. Use shelve
        try:
            d = shelve.open(task_settings.get_path()+"database")
        except Exception as e:
            print "Database not found E:",e
            return
        details={}
           
        progress = 0
        for key in d.keys():
            details = d[key]
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
            
            if progress != 100 and details['started_check'] == False:
                item = QtWidgets.QTreeWidgetItem(self.ongoing_treeWidget)
                item.setText(0,details['task_name'])
                item.setText(1,str(details['id']))
            elif progress == 100:
                item = QtWidgets.QTreeWidgetItem(self.completed_treeWidget)
                item.setText(0,details['task_name'])
                item.setText(1,str(details['id']))
        d.close()
        
    def retranslateUi(self, tasks_TabWidget):
        _translate = QtCore.QCoreApplication.translate
        tasks_TabWidget.setWindowTitle(_translate("tasks_TabWidget", "Archives"))
        self.ongoing_treeWidget.headerItem().setText(0, _translate("tasks_TabWidget", "Tasks"))
        tasks_TabWidget.setTabText(tasks_TabWidget.indexOf(self.ongoing_tab), _translate("tasks_TabWidget", "OnGoing Tasks"))
        self.completed_treeWidget.headerItem().setText(0, _translate("tasks_TabWidget", "Tasks"))
        tasks_TabWidget.setTabText(tasks_TabWidget.indexOf(self.completed_tab), _translate("tasks_TabWidget", "Completed Tasks"))

    
def getObject():
    return Ui_tasks_TabWidget()
