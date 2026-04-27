import sys

import io
from PyQt6 import QtCore, QtMultimedia, uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QKeySequence, QShortcut
template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>801</width>
    <height>264</height>
   </rect>
  </property>
  <property name="cursor">
   <cursorShape>OpenHandCursor</cursorShape>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>101</width>
      <height>211</height>
     </rect>
    </property>
    <property name="text">
     <string>С(До), Z</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>100</x>
      <y>0</y>
      <width>101</width>
      <height>211</height>
     </rect>
    </property>
    <property name="text">
     <string>D(Ре), X</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_3">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>0</y>
      <width>101</width>
      <height>211</height>
     </rect>
    </property>
    <property name="text">
     <string>E(Ми), C</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_4">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>0</y>
      <width>101</width>
      <height>211</height>
     </rect>
    </property>
    <property name="text">
     <string>F(Фа), V</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_5">
    <property name="geometry">
     <rect>
      <x>400</x>
      <y>0</y>
      <width>101</width>
      <height>211</height>
     </rect>
    </property>
    <property name="text">
     <string>G(Соль), B</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_6">
    <property name="geometry">
     <rect>
      <x>500</x>
      <y>0</y>
      <width>101</width>
      <height>211</height>
     </rect>
    </property>
    <property name="text">
     <string>A(Ля), N</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_7">
    <property name="geometry">
     <rect>
      <x>600</x>
      <y>0</y>
      <width>101</width>
      <height>211</height>
     </rect>
    </property>
    <property name="text">
     <string>H(Си), M</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_8">
    <property name="geometry">
     <rect>
      <x>700</x>
      <y>0</y>
      <width>101</width>
      <height>211</height>
     </rect>
    </property>
    <property name="text">
     <string>Music, whitespace</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>801</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.do)
        do = QShortcut(QKeySequence('Z'), self)
        do.activated.connect(self.do)


        self.pushButton_2.clicked.connect(self.re)
        re = QShortcut(QKeySequence('X'), self)
        re.activated.connect(self.re)


        self.pushButton_3.clicked.connect(self.mi)
        mi = QShortcut(QKeySequence('C'), self)
        mi.activated.connect(self.mi)


        self.pushButton_4.clicked.connect(self.fa)
        fa = QShortcut(QKeySequence('V'), self)
        fa.activated.connect(self.fa)


        self.pushButton_5.clicked.connect(self.sol)
        sol = QShortcut(QKeySequence('B'), self)
        sol.activated.connect(self.sol)


        self.pushButton_6.clicked.connect(self.la)
        la = QShortcut(QKeySequence('N'), self)
        la.activated.connect(self.la)


        self.pushButton_7.clicked.connect(self.si)
        si = QShortcut(QKeySequence('M'), self)
        si.activated.connect(self.si)


        self.pushButton_8.clicked.connect(self.music)
        music = QShortcut(QKeySequence(' '), self)
        music.activated.connect(self.music)



    def do(self):
        print('do')
    def re(self):
        print('re')
    def mi(self):
        print('mi')
    def fa(self):
        print('fa')
    def sol(self):
        print('sol')
    def la(self):
        print('la')
    def si(self):
        print('si')
    def music(self):
        print('music')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
