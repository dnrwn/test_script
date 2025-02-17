import os

# result 하위 폴더 생성 코드 / pytest, unittest 별도

# test 종류 선택 코드
# a = input('1. pytest \n2. unittest')
a = '1'


if a == '1':
    os.system('pytest -c .\pytest.ini .\item\pytest\Selenium_script.py')

elif a != '1':
    os.system('unittest ')