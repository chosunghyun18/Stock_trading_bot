# version 1.3.2

#매일 장마감후 데이터 베이스에 입력을 한다 데이터 수집용

print("collector v3 프로그램이 시작 되었습니다!")

from library.collector_api import *

class Collector:
    print("collector 클래스에 들어왔습니다.")

    def __init__(self):
        print("__init__ 함수에 들어왔습니다.")
        self.collector_api = collector_api()

    def collecting(self):
        self.collector_api.code_update_check()

if __name__ == "__main__":
    print("__main__에 들어왔습니다.")
    # 아래는 키움증권 openapi를 사용하기 위해 사용하는 한 줄! 이해 할 필요 X
    app = QApplication(sys.argv)
    c = Collector()
    # 데이터 수집 시작 -> 주식 종목, 종목별 금융 데이터 모두 데이터베이스에 저장.
    c.collecting()
