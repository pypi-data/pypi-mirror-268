<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>TestWidget</class>
 <widget class="QWidget" name="TestWidget">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>586</width>
    <height>74</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <layout class="QVBoxLayout" name="verticalLayout">
   <item>
    <widget class="QGroupBox" name="groupBox">
     <property name="title">
      <string>GroupBox</string>
     </property>
     <layout class="QHBoxLayout" name="horizontalLayout">
      <item>
       <widget class="QLabel" name="label">
        <property name="text">
         <string>Имя</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QLineEdit" name="lineEdit"/>
      </item>
      <item>
       <spacer name="horizontalSpacer_2">
        <property name="orientation">
         <enum>Qt::Horizontal</enum>
        </property>
        <property name="sizeHint" stdset="0">
         <size>
          <width>51</width>
          <height>20</height>
         </size>
        </property>
       </spacer>
      </item>
      <item>
       <widget class="QLabel" name="label_2">
        <property name="text">
         <string>Фамилия</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QLineEdit" name="lineEdit_2"/>
      </item>
      <item>
       <spacer name="horizontalSpacer_3">
        <property name="orientation">
         <enum>Qt::Horizontal</enum>
        </property>
        <property name="sizeHint" stdset="0">
         <size>
          <width>51</width>
          <height>20</height>
         </size>
        </property>
       </spacer>
      </item>
      <item>
       <widget class="QPushButton" name="pushButton">
        <property name="text">
         <string>Удалить</string>
        </property>
       </widget>
      </item>
     </layout>
    </widget>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
