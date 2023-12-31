# DemoForm3.py
# DemoForm3.ui(화면단) + DemoForm.py(로직단)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#디자인 된 문서 로딩(시그널+슬롯)
form_class = uic.loadUiType("DemoForm3.ui")[0]
#폼 클래스 정의(QMainWindow)
class DemoForm(QMainWindow, form_class):
    #초기화 메서드
    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 화면")
    #슬롯메서드
    def firstClick(self):
        self.label.setText("첫번째 버튼")
    def secondClick(self):
        self.label.setText("두번째 버튼을 클릭")
    def thirdClick(self):
        self.label.setText("세번째 버튼을 클릭~~")

#직접 모듈을 실행했는지 체크(진입점)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()