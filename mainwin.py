#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'

from PyQt5 import QtCore, QtGui, QtWidgets
import prop, archives, task_settings
import sys, shelve, time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, PropWindow, ArchWindow):
        self.propWin = PropWindow
        self.archWin = ArchWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(568, 524)
        font = QtGui.QFont()
        font.setPointSize(13)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.separator_line = QtWidgets.QFrame(self.centralwidget)
        self.separator_line.setGeometry(QtCore.QRect(320, 50, 20, 371))
        self.separator_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.separator_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.separator_line.setObjectName("separator_line")
        self.actions_grp_box = QtWidgets.QGroupBox(self.centralwidget)
        self.actions_grp_box.setGeometry(QtCore.QRect(340, 0, 221, 431))
        self.actions_grp_box.setTitle("")
        self.actions_grp_box.setObjectName("actions_grp_box")
        self.formLayoutWidget = QtWidgets.QWidget(self.actions_grp_box)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 70, 211, 341))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setObjectName("formLayout_2")
        self.properties_pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)        
        self.properties_pushButton.setFont(font)
        self.properties_pushButton.setObjectName("properties_pushButton")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.properties_pushButton)
        self.add_new_task_pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.add_new_task_pushButton.setFont(font)
        self.add_new_task_pushButton.setObjectName("add_new_task_pushButton")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.add_new_task_pushButton)
        self.completed_tasks_pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.completed_tasks_pushButton.setFont(font)
        self.completed_tasks_pushButton.setObjectName("completed_tasks_pushButton")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.completed_tasks_pushButton)
        self.ongoing_tasks_pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.ongoing_tasks_pushButton.setObjectName("ongoing_tasks_pushButton")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.ongoing_tasks_pushButton)
        self.exit_pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.exit_pushButton.setObjectName("exit_pushButton")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.exit_pushButton)
        self.delete_task_pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.delete_task_pushButton.setObjectName("delete_task_pushButton")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.delete_task_pushButton)
        self.main_progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.main_progressBar.setGeometry(QtCore.QRect(10, 430, 551, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.main_progressBar.setFont(font)
        self.main_progressBar.setProperty("value", 0)
        self.main_progressBar.setObjectName("main_progressBar")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 291, 341))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tasks_treeWidget = QtWidgets.QTreeWidget(self.horizontalLayoutWidget)
        self.tasks_treeWidget.setMaximumSize(QtCore.QSize(250, 339))
        self.tasks_treeWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tasks_treeWidget.setProperty("showDropIndicator", False)
        self.tasks_treeWidget.setDragEnabled(False)
        self.tasks_treeWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tasks_treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tasks_treeWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tasks_treeWidget.setObjectName("tasks_treeWidget")
        self.horizontalLayout.addWidget(self.tasks_treeWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.move_up_toolButton = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.move_up_toolButton.setMouseTracking(False)
        self.move_up_toolButton.setArrowType(QtCore.Qt.UpArrow)
        self.move_up_toolButton.setObjectName("move_up_toolButton")
        self.verticalLayout.addWidget(self.move_up_toolButton)
        self.move_down_toolButton_2 = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.move_down_toolButton_2.setArrowType(QtCore.Qt.DownArrow)
        self.move_down_toolButton_2.setObjectName("move_down_toolButton_2")
        self.verticalLayout.addWidget(self.move_down_toolButton_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.debug_label = QtWidgets.QLabel(self.centralwidget)
        self.debug_label.setGeometry(QtCore.QRect(100, 20, 401, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.debug_label.setFont(font)
        self.debug_label.setTextFormat(QtCore.Qt.RichText)
        self.debug_label.setObjectName("debug_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 568, 28))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionTasks = QtWidgets.QAction(MainWindow)
        self.actionTasks.setObjectName("actionTasks")
        self.menuFile.addAction(self.actionTasks)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        
        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)
        #
        self.tasks_treeWidget.itemDoubleClicked.connect(self.show_properties)
        self.properties_pushButton.clicked.connect(MainWindow.show)
        self.exit_pushButton.clicked.connect(MainWindow.close)
        self.properties_pushButton.clicked.connect(self.show_properties)
        self.exit_pushButton.clicked.connect(MainWindow.close)
        self.add_new_task_pushButton.clicked.connect(self.show_new_properties)
        self.delete_task_pushButton.clicked.connect(self.delete_selected_items)
        self.move_up_toolButton.clicked.connect(self.move_up)
        self.move_down_toolButton_2.clicked.connect(self.move_down)
        self.completed_tasks_pushButton.clicked.connect(self.show_arch_completed)
        self.ongoing_tasks_pushButton.clicked.connect(self.show_arch_ongoing)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.add_new_task_pushButton, self.properties_pushButton)
        MainWindow.setTabOrder(self.properties_pushButton, self.delete_task_pushButton)
        MainWindow.setTabOrder(self.delete_task_pushButton, self.ongoing_tasks_pushButton)
        MainWindow.setTabOrder(self.ongoing_tasks_pushButton, self.completed_tasks_pushButton)
        MainWindow.setTabOrder(self.completed_tasks_pushButton, self.exit_pushButton)
        print "setup_Ui MainWindow"

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Event Manager"))
        self.properties_pushButton.setText(_translate("MainWindow", "Properties"))
        self.add_new_task_pushButton.setText(_translate("MainWindow", "Add New Task"))
        self.completed_tasks_pushButton.setText(_translate("MainWindow", "Completed Tasks"))
        self.ongoing_tasks_pushButton.setText(_translate("MainWindow", "OnGoing Tasks"))
        self.exit_pushButton.setText(_translate("MainWindow", "Exit"))
        self.delete_task_pushButton.setText(_translate("MainWindow", "Delete Task"))
        self.tasks_treeWidget.headerItem().setText(0, _translate("MainWindow", "Task Name"))
        __sortingEnabled = self.tasks_treeWidget.isSortingEnabled()
        self.tasks_treeWidget.setSortingEnabled(False)
        #
        self.tasks_treeWidget.setSortingEnabled(__sortingEnabled)
        self.move_up_toolButton.setText(_translate("MainWindow", "..."))
        self.move_down_toolButton_2.setText(_translate("MainWindow", "..."))
        self.debug_label.setText("")
        self.menuFile.setTitle(_translate("MainWindow", "Menu"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionTasks.setText(_translate("MainWindow", "Completed Tasks"))
    
    def debug_fun(self,msg):
        self.debug_label.setText("<html><head/><body><p><span style=\" font-size:14pt; color:#ff0000;\">"+msg+"</span></p></body></html>") 
        print msg
                       
    def delete_selected_items(self):              
        selected_items = list(ui.tasks_treeWidget.selectedItems())
        for item in selected_items:
            self.delete_task(item)
        self.load_task_names()
            
    def delete_task(self,item):
        self.debug_fun("")        
  
        try:
            d = shelve.open(task_settings.get_path()+"database")
        
            del_item = item
            
            del_key = str(del_item.text(1))
            idx = self.tasks_treeWidget.indexOfTopLevelItem(del_item)
            set_priority_item = del_item
            for i in range(len(d.keys())):
                try:
                    rec = self.tasks_treeWidget.itemBelow(set_priority_item)
                    rec_key = str(rec.text(1))
                    print "Set new priority for ",rec.text(0)
                    rec_details = d[rec_key]
                    rec_details['priority']-=1
                    d[rec_key] = rec_details
                except Exception as e_msg:
                    print "Delete_task: ",e_msg
                set_priority_item = self.tasks_treeWidget.itemBelow(set_priority_item)
#                del set_priority_item
            #free memory
            print "Deleting :",del_key," with index :",idx
#            self.tasks_treeWidget.topLevelItem(idx).setText(idx,"")
            
            try:
                del d[del_key]
            except Exception as e_msg:
                print e_msg
                
        except AttributeError:
            self.debug_fun("Error: Task name not seleted, cannot delete")
          
        finally:
            d.close()
             
                
        #self.load_task_names() 
#        wrapper C/C++ object deleted error

    def show_arch_completed(self):
        arch_ui.set_completed()
        arch_window.show()
        
    def show_arch_ongoing(self):
        arch_ui.set_ongoing()
        arch_window.show()
 
    def show_new_properties(self):
        self.debug_fun("")
        prop_ui.resetAllDetails()
        prop_ui.new_details = True
        prop_window.show()
        
    def show_properties(self):
        self.debug_fun("")
        try:
            prop_ui.loadAllDetails(str(ui.tasks_treeWidget.currentItem().text(1)))
        except AttributeError:
            self.debug_fun("Please select task name")
            return     
        prop_ui.new_details = False       
        prop_window.show()
        
    def load_task_names(self):
        count=0        
        self.tasks_treeWidget.clear()
        
        try:            
            d = shelve.open(task_settings.get_path()+"database")  
            keys = list(d.keys())
            priority={}
            #store all priorities in order in one dict along with keys
            #displaying keys should be there in a list
            for k in keys:
                priority[str(k)] = d[k]['priority']
            keys = sorted(keys, key=priority.__getitem__)        
            print "Load Task Names"
            for key in keys:               
                details = d[key]
#                print "Load Key is : ",key
                item = QtWidgets.QTreeWidgetItem(self.tasks_treeWidget)
                item.setText(0,details['task_name'])
                item.setText(1,str(details['id']))
#                print "List ",count,":",details['task_name']
                count+=1
            d.close()            
#            prop.set_priority_value(self.propWin)
#   function already called in prop.py resetAllDetails()
        except IOError:
            print "Database doesn't exist"
        self.calculate_progress()
            
    def move_up(self):
        self.debug_fun("")
        current_item = self.tasks_treeWidget.currentItem()
        prev_item = ui.tasks_treeWidget.itemAbove(current_item)      
        try:
            self.swap_items(str(current_item.text(1)),str(prev_item.text(1)))
        except AttributeError:
            self.debug_fun("Error: Cannot move up item")
        
    def move_down(self):
        self.debug_fun("")
        current_item = self.tasks_treeWidget.currentItem()
        next_item = self.tasks_treeWidget.itemBelow(current_item)
        try:
            self.swap_items(str(current_item.text(1)),str(next_item.text(1)))
        except AttributeError:
            self.debug_fun("Error: Cannot move down item")
            
    def swap_items(self,key1,key2):
          d = shelve.open(task_settings.get_path()+"database")
          first = d[key1]
          second = d[key2]
#          print "Before Swap: ",first['priority']," ",second['priority']
          tmp = first['priority']
          first['priority'] = second['priority']
          second['priority'] = tmp
#          print "After Swap: ",first['priority']," ",second['priority']
          d[key1] = first
          d[key2] = second
          d.close()
          self.load_task_names()
          
    def calculate_progress(self):
        print "Calculating Progress"
        d = shelve.open(task_settings.get_path()+"database")
        total_progress = 0    
        count_of_keys = 0
        self.main_progressBar.setValue(0)
        for key in list(d.keys()):
            p = self.propWin.loadAllDetails(key,only_progress=True)
            if p!=100:
                total_progress += p
                count_of_keys += 1
                self.main_progressBar.setValue(total_progress/count_of_keys)
                #time.sleep(.1)
                #above time delay is for animation
        d.close()

def load_task_names_external(ui):
    ui.load_task_names()
##     

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    
    prop_window = QtWidgets.QDialog()
    prop_ui = prop.getObject()
    
    arch_window = QtWidgets.QTabWidget()
    arch_ui = archives.getObject()
    
    ui.setupUi(window,prop_ui,arch_ui)
    prop_ui.setupUi(prop_window,ui)
    arch_ui.setupUi(arch_window)
    
    ui.load_task_names()
    
    window.show()
    #arch_window.show()
    sys.exit(app.exec_())
