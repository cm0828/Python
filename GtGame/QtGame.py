'''
-- 剪刀、石頭、布 猜拳遊戲
'''

from PySide2.QtWidgets import QWidget, QLabel, QPushButton, QApplication, QVBoxLayout, QHBoxLayout, QGroupBox
from PySide2.QtGui import QFont
from random import randint
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Unicode 支援的 剪刀，石頭、布 編碼
        self.rock = u"\u270a"
        self.paper = u"\u270b"
        self.scissor = u"\u270c"

        # 分別產生所要的子畫面
        self.createChoiceBox()
        self.createBtnBox()
        self.createMsgBox()

        #使用 QVBoxLayout 排版子畫面
        main_layout = QVBoxLayout()
        main_layout.addLayout(self.h_layout)
        main_layout.addWidget(self.btn_groupbox)
        main_layout.addWidget(self.msg_groupbox)

        self.setLayout(main_layout)
        self.setWindowTitle("猜拳遊戲")
        self.show()


    def createChoiceBox(self):
        #生成顯示玩家&電腦出拳的畫面
        self.h_layout = QHBoxLayout()

        box_font = QFont()
        box_font.setPointSize(16)

        choice_label_font = QFont()
        choice_label_font.setPointSize(80)

        #產生顯示玩家選擇的畫面，並使用 QGroupBox & QHBoxLayout 排版
        player_groupbox = QGroupBox("玩家")
        player_groupbox.setFont(box_font)

        self.player_choice_label = QLabel(self.paper)
        self.player_choice_label.setFixedSize(120, 150)
        self.player_choice_label.setFont(choice_label_font)

        player_layout = QHBoxLayout()
        player_layout.addWidget(self.player_choice_label)
        player_groupbox.setLayout(player_layout)

        # 產生顯示電腦選擇的畫面，並使用 QGroupBox & QHBoxLayout 排版
        com_groupbox = QGroupBox("電腦")
        com_groupbox.setFont(box_font)

        self.com_choice_label = QLabel(self.paper)
        self.com_choice_label.setFixedSize(120, 150)
        self.com_choice_label.setFont(choice_label_font)

        com_layout = QHBoxLayout()
        com_layout.addWidget(self.com_choice_label)
        com_groupbox.setLayout(com_layout)

        #將玩家&電腦的畫面用 GHBoxLayout 排版
        self.h_layout.addWidget(player_groupbox)
        self.h_layout.addWidget(com_groupbox)


    def createBtnBox(self):
        #生成剪刀、石頭、布按鈕給玩家選擇的子畫面
        self.btn_groupbox = QGroupBox("請選擇:")

        btn_hlayout = QHBoxLayout()
        self.btn_groupbox.setLayout(btn_hlayout)

        scissor_btn = QPushButton("剪刀")
        scissor_btn.clicked.connect(self.btn_click)

        rock_btn = QPushButton("石頭")
        rock_btn.clicked.connect(self.btn_click)

        paper_btn = QPushButton("布")
        paper_btn.clicked.connect(self.btn_click)

        btn_hlayout.addWidget(scissor_btn)
        btn_hlayout.addWidget(rock_btn)
        btn_hlayout.addWidget(paper_btn)


    def createMsgBox(self):
        #生成訊息子畫面，顯示猜拳輸贏結果
        self.msg_groupbox = QGroupBox("結果")

        msg_hlayout = QHBoxLayout()
        self.msg_groupbox.setLayout(msg_hlayout)

        self.msg = QLabel("點選按鈕開始遊戲")
        msg_hlayout.addWidget(self.msg)

    def win_lose_judgment(self,player, com):
        #判斷猜拳 輸、贏、平手 結果，並將結果輸出到 結果訊息子畫面
        if player == com:
            self.msg.setText("平手")
        elif player == (com + 1) % 3:
            self.msg.setText("你贏了")
        else:
            self.msg.setText("你輸了")

    def com_choice(self):
        #隨機產生電腦的出拳選擇， 0 -> 剪刀， 1 -> 石頭， 2 -> 布
        choice_list = [self.scissor, self.rock, self.paper]
        choice = randint(0, 2)
        self.com_choice_label.setText(choice_list[choice])
        return choice

    def btn_click(self):
        # 1. 根據玩家點選的按鈕，判斷出拳的選擇
        choice = self.sender().text()
        # print(choice)
        if choice == "剪刀":
            self.player_choice_label.setText(self.scissor)
            player = 0
        elif choice == "石頭":
            self.player_choice_label.setText(self.rock)
            player = 1
        elif choice == "布":
            self.player_choice_label.setText(self.paper)
            player = 2

        # 2. 隨機產生電腦的選擇
        com = self.com_choice()

        # 3. 判斷結果
        self.win_lose_judgment(player, com)


app = QApplication()
ex = Window()
sys.exit(app.exec_())