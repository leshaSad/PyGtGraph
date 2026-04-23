import io
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>922</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="PlotWidget" name="graphicsView">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>921</width>
      <height>431</height>
     </rect>
    </property>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>430</y>
      <width>651</width>
      <height>101</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <widget class="QLabel" name="label">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
         <horstretch>0</horstretch>
         <verstretch>10</verstretch>
        </sizepolicy>
       </property>
       <property name="text">
        <string>Для построения графика необходимо писать, так x^2+6x+10 </string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="label_2">
       <property name="text">
        <string>Для умножения используйте *, для деления /, для сложения +, для вычетания -, возведение в степень ^</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLineEdit" name="lineEdit"/>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="horizontalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>669</x>
      <y>440</y>
      <width>221</width>
      <height>80</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout">
     <item>
      <widget class="QPushButton" name="pushButton">
       <property name="text">
        <string>Построить</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton_2">
       <property name="text">
        <string>Удалить</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>922</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <customwidgets>
  <customwidget>
   <class>PlotWidget</class>
   <extends>QGraphicsView</extends>
   <header>pyqtgraph</header>
  </customwidget>
 </customwidgets>
 <resources/>
 <connections/>
</ui>
"""

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.dele)

    def run(self):
        text = self.lineEdit.text()
        print(text)
        if '^' not in text:
            self.graphicsView.clear()
            self.graphicsView.plot([i for i in range(10)], [i for i in range(10)], pen='r')
        elif '^2' in text:
            self.graphicsView.clear()
            self.graphicsView.plot([i for i in range(10)], [i ** 2 for i in range(10)], pen='r')
        elif '^3' in text:
            self.graphicsView.clear()
            self.graphicsView.plot([i for i in range(10)], [i ** 3 for i in range(10)], pen='r')

    def dele(self):
        self.lineEdit.clear()
        self.graphicsView.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())