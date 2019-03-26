import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from interface2 import *
import psutil
import subprocess
import os


class mainWindow_1(QMainWindow):

    def __init__(self):
        super().__init__()
        self.interface()

    def interface(self):
        
        #pengaturan window
        self.setWindowTitle('Forensic Imaging Application')
        #self.resize(770, 520)
        self.resize(480, 250)
        #self.setStyleSheet("QMainWindow {background:rgb(102,153,153)}")
        self.setWindowIcon(QtGui.QIcon("D:/Tugas/Skripsi/Icon Button/aplikasi.png"))

        #pengaturan menu bar
        menuFile = self.menuBar().addMenu('File')
        actionScan = menuFile.addAction('Scan')
        actionScan.triggered.connect(self.menuScan)
        actionExit = menuFile.addAction("Exit")
        actionExit.triggered.connect(self.menuExit)
        
        #pengaturan label device
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lblDevice = QLabel("Select Device Number: ", self)
        self.lblDevice.setFont(font)
        self.lblDevice.setGeometry(QtCore.QRect(30,22,181,31))

        #pengturan display disk
        self.display = QTableWidget(self)
        #self.display.setGeometry(170,100,420,140)
        self.display.setGeometry(27,55,420,140)
        self.display.horizontalHeader().setStyleSheet("QHeaderView::section{Background-color:rgb(255,153,0);font:bold}")
        self.display.verticalHeader().sectionClicked.connect(self.getValue)
        #self.display.cellClicked.connect(self.getValue)
        
        diskx = [s.split() for s in os.popen("lsblk | grep disk").read().splitlines()]
        i=0
        j=0
        k=0
        for line in diskx:
            listAx = line[0]
            listBx = line[3]
            listCx = line[5]
            mystruct = {'A':listAx, 'B':listBx, 'C':listCx}
            self.datax = mystruct
            jmlhRow = len(diskx)
            self.display.setRowCount(jmlhRow)
            self.display.setColumnCount(3)
            self.display.setHorizontalHeaderLabels(["Device", "Size", "Type"])
            
            for itemx in self.datax:
                device = QTableWidgetItem(listAx)
                self.display.setItem(i,0, device)
                #device.setFlags(QtCore.Qt.ItemIsEnabled)
            i += 1
            
            for item2x in self.datax:
                size = QTableWidgetItem(listBx)
                self.display.setItem(j,1, size)
                #size.setFlags(QtCore.Qt.ItemIsEnabled)
            j += 1
            
            for item3x in self.datax:
                type = QTableWidgetItem(listCx)
                self.display.setItem(k,2, type)
                #type.setFlags(QtCore.Qt.ItemIsEnabled)
            k += 1
            
        header = self.display.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        headerX = self.display.verticalHeader()
        headerX.setSectionResizeMode(QHeaderView.Stretch)
        
        
        #pengaturan button
        self.btnNext = QPushButton("Next", self)
        #self.btnNext.setGeometry(QtCore.QRect(620, 450, 93, 28))
        self.btnNext.setGeometry(QtCore.QRect(374, 211, 75, 25))
        iconNext = QtGui.QIcon()
        iconNext.addPixmap(QtGui.QPixmap("/home/pi/Icon Button/next(1).png"),
                           QtGui.QIcon.Normal)
        self.btnNext.setIcon(iconNext)
        self.btnNext.clicked.connect(self.createInterface2)
        self.btnNext.setDisabled(True)
    
        self.show()
        
    def getValue(self):
        self.display.setStyleSheet("QTableWidget::item::selected{Background-color:rgb(153,153,153);font:bold}")
        
        row = self.display.currentRow()
        #column = self.display.currentColumn()
        #percobaan_2.hasil = self.display.item(row,0).text()
        mainWindow_2.hasil = self.display.item(row,0).text()
        mainWindow_2.size = self.display.item(row,1).text()
        self.btnNext.setDisabled(False)
        #print("Device: ", percobaan_2.hasil)
        print(mainWindow_2.hasil, mainWindow_2.size)
        
    
    def menuScan(self):
        # disk = psutil.disk_partitions()
        # text = "disk: {disk}".format(disk=disk)
        #hasil = subprocess.check_output('lsblk')
        #text = "{hasil}".format(hasil=hasil)
        
        disk = [s.split() for s in os.popen("lsblk | grep disk").read().splitlines()]
        i=0
        j=0
        k=0
        for line in disk:
            listA = line[0]
            listB = line[3]
            listC = line[5]
            mystruct = {'A':listA, 'B':listB, 'C':listC}
            self.data = mystruct
            jmlhRow = len(disk)
            self.display.setRowCount(jmlhRow)
            self.display.setColumnCount(3)
            self.display.setHorizontalHeaderLabels(["Device", "Size", "Type"])
            
            for item in self.data:
                device = QTableWidgetItem(listA)
                self.display.setItem(i,0, device)
            i += 1
            
            for item2 in self.data:
                size = QTableWidgetItem(listB)
                self.display.setItem(j,1, size)
            j += 1
            
            for item3 in self.data:
                type = QTableWidgetItem(listC)
                self.display.setItem(k,2, type)
            k += 1
            
        header = self.display.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        headerX = self.display.verticalHeader()
        headerX.setSectionResizeMode(QHeaderView.Stretch)
                         
    def menuExit(self):
        reply = QMessageBox.question(self, "Caution",
                                     "Are you sure to exit?", QMessageBox.No |
                                     QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            QApplication.quit()
        else:
            pass

    def menuAbout(self):
        self.tulisan = QLabel('Aplikasi Forensic Imaging yang dibuat oleh Razan Maulida K', self)
        self.tulisan.setGeometry(30, 20, 500, 50)
        self.tulisan.show()

    def createInterface2(self):
        #self.window2 = mainWindow_2()
        #self.window2.show()
        #self.hide()
        
        self.window2 = mainWindow_2()
        self.window2.window1 = self
        self.window2.show()
        self.hide()


if __name__ == '__main__':
    aplikasi = QApplication(sys.argv)
    ex = mainWindow_1()
    sys.exit(aplikasi.exec())
