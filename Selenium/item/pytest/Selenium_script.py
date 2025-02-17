import pytest, logging, datetime, time, sys, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
# import Selenium.item.element_list as element_list

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import element_list as element_list


# Log 설정
LOGGER = logging.getLogger(__name__)
start_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
dir_mk = str('result/4.screencapture' + '/' + start_time)

def capture_in(type_1='', item_1='', item_2='', item_3='', item_4='', item_5=''):
    tt = dir_mk + '/' + type_1 + '/'
    Path(tt).mkdir(parents=True, exist_ok=True)
    driver.save_screenshot(tt + str(item_1) + '_' + str(item_2) + '_' + str(item_3) + '_' + str(item_4) + '_' + str(item_5) + '_' + '_in.png')

def capture_out(type_1='', item_1='', item_2='', item_3='', item_4='', item_5=''):
    tt = dir_mk + '/' + type_1 + '/'
    driver.save_screenshot(tt + str(item_1) + '_' + str(item_2) + '_' + str(item_3) + '_' + str(item_4) + '_' + str(item_5) + '_' + '_out.png')


# driver service
service = webdriver.EdgeService(executable_path=element_list.driver_path)

def gui_op(a):
    option = webdriver.EdgeOptions()
    if a == 'hide':
        option.add_argument('headless')  # browser hide
        option.add_argument('disable-gpu')  # # browser hide
    elif a == 'show':
        option.add_experimental_option("detach", True)  # browser show

    return option

driver = webdriver.Edge(service=service, options=gui_op('hide'))


# input 정의
def ui_click(a):
    try:
        driver.find_element(By.XPATH, value=a).click()
        return LOGGER.info('PASS')
    except:
        return LOGGER.info('FAIL')

def ui_input(a, b):
    try:
        driver.find_element(By.XPATH, value=a).send_keys(b)
        return LOGGER.info('PASS')
    except:
        return LOGGER.info('FAIL')

def ui_result(a):
    try:
        LOGGER.info('PASS')
        return driver.find_element(By.XPATH, value=a).text
    except:
        return LOGGER.info('FAIL')


@pytest.mark.parametrize("item_int, item_str5, item_str10, item_boolean", [
    (item_int, item_str5, item_str10, item_boolean)
    for item_int in element_list.input_value_valid['int']
    for item_str5 in element_list.input_value_valid['str5']
    for item_str10 in element_list.input_value_valid['str10']
    for item_boolean in element_list.input_value_valid['boolean']
])
def test_insert_valid(item_int, item_str5, item_str10, item_boolean):
    driver.get(element_list.url)
    ui_click(element_list.ui['insert']['category'])
    ui_input(element_list.ui['insert']['input_1'], element_list.input_value_valid['int'][item_int])
    ui_input(element_list.ui['insert']['input_2'], element_list.input_value_valid['str5'][item_str5])
    ui_input(element_list.ui['insert']['input_3'], element_list.input_value_valid['str10'][item_str10])
    ui_input(element_list.ui['insert']['input_4'], element_list.input_value_valid['boolean'][item_boolean])
    capture_in('insert_valid', item_int, item_str5, item_str10, item_boolean)
    ui_click(element_list.ui['insert']['submit'])
    time.sleep(0.3)
    capture_out('insert_valid', item_int, item_str5, item_str10, item_boolean)
    assert ui_result(element_list.ui['result']) == '"PASS"', f'FAIL: {item_int}, {item_str5}, {item_str10}, {item_boolean}'


@pytest.mark.parametrize("item_int, item_str5, item_str10, item_boolean", [
    (item_int, item_str5, item_str10, item_boolean)
    for item_int in element_list.input_value_invalid['int']
    for item_str5 in element_list.input_value_invalid['str5']
    for item_str10 in element_list.input_value_invalid['str10']
    for item_boolean in element_list.input_value_invalid['boolean']
])
def test_insert_invalid(item_int, item_str5, item_str10, item_boolean):
    driver.get(element_list.url)
    ui_click(element_list.ui['insert']['category'])
    ui_input(element_list.ui['insert']['input_1'], element_list.input_value_invalid['int'][item_int])
    ui_input(element_list.ui['insert']['input_2'], element_list.input_value_invalid['str5'][item_str5])
    ui_input(element_list.ui['insert']['input_3'], element_list.input_value_invalid['str10'][item_str10])
    ui_input(element_list.ui['insert']['input_4'], element_list.input_value_invalid['boolean'][item_boolean])
    capture_in('insert_invalid', item_int, item_str5, item_str10, item_boolean)
    ui_click(element_list.ui['insert']['submit'])
    time.sleep(0.3)
    capture_out('insert_invalid', item_int, item_str5, item_str10, item_boolean)
    assert ui_result(element_list.ui['result']) == '"insert NG"', f'FAIL: {item_int}, {item_str5}, {item_str10}, {item_boolean}'


@pytest.mark.parametrize("item_int", [
    item_int for item_int in element_list.input_value_valid['select_int']
])
def test_select_valid(item_int):
    driver.get(element_list.url)
    ui_click(element_list.ui['select']['category'])
    ui_input(element_list.ui['select']['idx'], element_list.input_value_valid['select_int'][item_int])
    capture_in('select_valid', item_int)
    ui_click(element_list.ui['select']['submit'])
    time.sleep(0.3)
    capture_out('select_valid', item_int)
    assert ui_result(element_list.ui['result']) == '"PASS"'


@pytest.mark.parametrize("item_int", [
    item_int for item_int in element_list.input_value_invalid['int']
])
def test_select_invalid(item_int):
    driver.get(element_list.url)
    ui_click(element_list.ui['select']['category'])
    ui_input(element_list.ui['select']['idx'], element_list.input_value_invalid['int'][item_int])
    capture_in('select_invalid', item_int)
    ui_click(element_list.ui['select']['submit'])
    time.sleep(0.3)
    capture_out('select_invalid', item_int)
    assert ui_result(element_list.ui['result']) == '"select NG"', f'FAIL: {item_int}'


@pytest.mark.parametrize("item_int, item_int_1, item_str5, item_str10, item_boolean", [
    (item_int, item_int_1, item_str5, item_str10, item_boolean)
    for item_int in element_list.input_value_valid['select_int']
    for item_int_1 in element_list.input_value_valid['int']
    for item_str5 in element_list.input_value_valid['str5']
    for item_str10 in element_list.input_value_valid['str10']
    for item_boolean in element_list.input_value_valid['boolean']
])
def test_update_valid(item_int, item_int_1, item_str5, item_str10, item_boolean):
    driver.get(element_list.url)
    ui_click(element_list.ui['update']['category'])
    ui_input(element_list.ui['update']['idx'], element_list.input_value_valid['select_int'][item_int])
    ui_input(element_list.ui['update']['input_1'], element_list.input_value_valid['int'][item_int_1])
    ui_input(element_list.ui['update']['input_2'], element_list.input_value_valid['str5'][item_str5])
    ui_input(element_list.ui['update']['input_3'], element_list.input_value_valid['str10'][item_str10])
    ui_input(element_list.ui['update']['input_4'], element_list.input_value_valid['boolean'][item_boolean])
    capture_in('update_valid', item_int, item_int_1, item_str5, item_str10, item_boolean)
    ui_click(element_list.ui['update']['submit'])
    time.sleep(0.3)
    capture_out('update_valid', item_int, item_int_1, item_str5, item_str10, item_boolean)
    assert ui_result(element_list.ui['result']) == '"PASS"', f'FAIL: {item_int}, {item_int_1}, {item_str5}, {item_str10}, {item_boolean}'


@pytest.mark.parametrize("item_int, item_int_1, item_str5, item_str10, item_boolean", [
    (item_int, item_int_1, item_str5, item_str10, item_boolean)
    for item_int in element_list.input_value_invalid['int']
    for item_int_1 in element_list.input_value_invalid['int']
    for item_str5 in element_list.input_value_invalid['str5']
    for item_str10 in element_list.input_value_invalid['str10']
    for item_boolean in element_list.input_value_invalid['boolean']
])
def test_update_invalid(item_int, item_int_1, item_str5, item_str10, item_boolean):
    driver.get(element_list.url)
    ui_click(element_list.ui['update']['category'])
    ui_input(element_list.ui['update']['idx'], element_list.input_value_invalid['int'][item_int])
    ui_input(element_list.ui['update']['input_1'], element_list.input_value_invalid['int'][item_int_1])
    ui_input(element_list.ui['update']['input_2'], element_list.input_value_invalid['str5'][item_str5])
    ui_input(element_list.ui['update']['input_3'], element_list.input_value_invalid['str10'][item_str10])
    ui_input(element_list.ui['update']['input_4'], element_list.input_value_invalid['boolean'][item_boolean])
    capture_in('update_invalid', item_int, item_int_1, item_str5, item_str10, item_boolean)
    ui_click(element_list.ui['update']['submit'])
    time.sleep(0.3)
    capture_out('update_invalid', item_int, item_int_1, item_str5, item_str10, item_boolean)
    assert ui_result(element_list.ui['result']) == '"update NG"', f'FAIL: {item_int}, {item_int_1}, {item_str5}, {item_str10}, {item_boolean}'


@pytest.mark.parametrize("item_int", [
    item_int for item_int in element_list.input_value_valid['delete_int']
])
def test_delete_valid(item_int):
    driver.get(element_list.url)
    ui_click(element_list.ui['delete']['category'])
    ui_input(element_list.ui['delete']['idx'], element_list.input_value_valid['delete_int'][item_int])
    capture_in('delete_valid', item_int)
    ui_click(element_list.ui['delete']['submit'])
    time.sleep(0.3)
    capture_out('delete_valid', item_int)
    assert ui_result(element_list.ui['result']) == '"PASS"', f'FAIL: {item_int}'


@pytest.mark.parametrize("item_int", [
    item_int for item_int in element_list.input_value_invalid['int']
])
def test_delete_invalid(item_int):
    driver.get(element_list.url)
    ui_click(element_list.ui['delete']['category'])
    ui_input(element_list.ui['delete']['idx'], element_list.input_value_invalid['int'][item_int])
    capture_in('delete_invalid', item_int)
    ui_click(element_list.ui['delete']['submit'])
    time.sleep(0.3)
    capture_out('delete_invalid', item_int)
    assert ui_result(element_list.ui['result']) == '"delete NG"', f'FAIL: {item_int}'


@pytest.mark.parametrize("item_int", [
    item_int for item_int in element_list.input_value_invalid['int']
])
def test_delete_invalid_null(item_int):
    driver.get(element_list.url)
    ui_click(element_list.ui['delete']['category'])
    ui_input(element_list.ui['delete']['idx'], element_list.input_value_invalid['int'][item_int])
    capture_in('delete_invalid_null', item_int)
    ui_click(element_list.ui['delete']['submit'])
    time.sleep(0.3)
    capture_out('delete_invalid_null', item_int)
    assert ui_result(element_list.ui['result']) == '"delete NG"', f'FAIL: {item_int}'