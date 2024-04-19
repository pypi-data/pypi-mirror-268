import sys
import os

file_path = os.path.abspath(__file__)
end = file_path.index('mns') + 17
project_path = file_path[0:end]
sys.path.append(project_path)

import easytrader

user = easytrader.use('ths')
user.connect(r'D:\Program Files\ths\xiadan.exe')


## 自动一键打新
def auto_ipo_buy():
    user.auto_ipo()


if __name__ == '__main__':
    auto_ipo_buy()
