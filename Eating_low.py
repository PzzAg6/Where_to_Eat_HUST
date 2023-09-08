import sys
from PyQt6.QtWidgets import QPushButton, QLabel, QMessageBox, QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import pyqtSignal, Qt, QTimer

#不搞开始结束的版本

cantin = ["东园食堂",
"韵苑食堂",
"学一食堂",
"学二食堂",
"集锦园",
"集贤楼",
"喻园",
"百景园",
"西一食堂",
"西二食堂",
"东一食堂",
"东三食堂"]

import random

class Window(QWidget):
    button_clicked_signal = pyqtSignal()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('吃什么')
        self.resize(300, 200)
        self.cantin_size = len(cantin)
        
        hbox_lcd = QHBoxLayout()
        hbox_lcd.addStretch(10)
        self.lcd = QLabel('今天吃什么？')
        hbox_lcd.addWidget(self.lcd)
        hbox_lcd.addStretch(10)
        
        self.start_btn = QPushButton('开始', self)
        self.end_btn = QPushButton('停止', self)
        self.Press_time = 0
        #加hbox
        hbox_acc = QHBoxLayout() #水平布局管理器
        hbox_acc.addStretch(10)  #水平布局间隔
        hbox_acc.addWidget(self.start_btn) #将实例化标签账号放入
        hbox_acc.addWidget(self.end_btn) #将#单行文本编辑框放入
        hbox_acc.addStretch(10)

        #加vbox
        vbox = QVBoxLayout()
        vbox.addSpacing(10)
        vbox.addLayout(hbox_lcd)
        vbox.addSpacing(5)
        vbox.addLayout(hbox_acc)

        self.timer = QTimer()
        self.setLayout(vbox)
        self.button_clicked_signal.connect(self.resume)
        self.init_ui()
        


    def init_ui(self):

        
        self.start_btn.clicked.connect(self.start_btn_hand) #使用connect绑定事件，点击按钮时触发
        self.end_btn.clicked.connect(self.end_btn_hand)
        self.close()

    def start_btn_hand(self):
        # widget = QWidget()
        # QMessageBox.information(widget, "text", 'Start Button') #触发的事件时弹出会话框
        self.timer.setInterval(50)
        self.timer.start()
        self.timer.timeout.connect(self.Eating)
        # self.button_clicked_signal.connect(self.Eating)
    def resume(self):
        self.lcd.setText('今天吃什么？')

    def end_btn_hand(self):
        # widget = QWidget()
        # QMessageBox.information(widget, "text", 'End Button') #触发的事件时弹出会话框
        self.timer.stop()
        pick = random.randint(0, self.cantin_size - 1)
        Pick_Cantin = cantin[pick]
        sentence = "去" + Pick_Cantin + "!"
        self.lcd.setText(sentence)

    def Press_Counting(self):
        widget = QWidget()
        self.Press_time += 1
        choose = self.Press_time % self.cantin_size
        time_show = "Press {} times".format(cantin[choose])
        # QMessageBox.information(widget, 'times', time_show)
        self.lcd.setText(time_show)

    def mousePressEvent(self, event):        # 重写鼠标按下事件
        super().mousePressEvent(event)
        if event.button() == Qt.MouseButton.LeftButton:     # 当鼠标左键单击时
            self.button_clicked_signal.emit()     # 发射信号

    def Rolling_Number(self):
        count = 0
        while(1):
            count += 1
            self.lcd.setText("{}".format(count))

    def Eating(self):
        # self.timer.setInterval(50)
        # self.timer.start()
        # self.timer.timeout.connect(self.Eating)
        pick = random.randint(0, self.cantin_size - 1)
        Pick_Cantin = cantin[pick]
        sentence = "去" + Pick_Cantin
        self.lcd.setText(sentence)


        # self.btn = QPushButton('开始', self)
        # self.init_ui()

    # def init_ui(self):
    #     self.btn.resize(100, 30)
    #     self.btn.move(100, 50)   #按钮的位置
    #     self.btn.clicked.connect(self.btn_hand) #使用connect绑定事件，点击按钮时触发
    #     self.close()

    # def btn_hand(self):
    #     widget = QWidget()
    #     QMessageBox.information(widget, 'Pop messgae', 'OK') #触发的事件时弹出会话框


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = Window()
    window.show()
    sys.exit(app.exec())
