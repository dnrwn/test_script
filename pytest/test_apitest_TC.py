import requests, logging, pytest, json
from datetime import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
date = datetime.now().strftime('%y-%m-%d %H:%M:%S')

@pytest.mark.parametrize("url, params, expected_result",
                         [('http://localhost:70/func_1', {'idx':5}, 'PASS')])
def test_case_1(url, params, expected_result):
    actual_result = requests.get(url=url, params=params).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, params, expected_result",
                         [('http://localhost:70/func_1', {'idx':'a'}, 'NG')])
def test_case_2(url, params, expected_result):
    actual_result = requests.get(url=url, params=params).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, params, expected_result",
                         [('http://localhost:70/func_1', {'idx':None}, 'NG')])
def test_case_3(url, params, expected_result):
    actual_result = requests.get(url=url, params=params).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_3',
                              {'input_1': 1, 'input_4': False}, 'PASS'),
                         ])
def test_case_4(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_3',
                              {'input_1': 1, 'input_2': 'a', 'input_3': 'a', 'input_4': True}, 'PASS'),
                         ])
def test_case_5(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_3',
                              {'input_1': 1, 'input_2': 'a', 'input_4': True}, 'PASS'),
                         ])
def test_case_6(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_3',
                              {'input_1': 1, 'input_2': 'a', 'input_3': 'a'}, 'PASS'),
                         ])
def test_case_7(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_3',
                              {'input_1': 1, 'input_3': 'a', 'input_4': True}, 'PASS'),
                         ])
def test_case_8(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_3',
                              {'input_1': 1}, 'PASS'),
                         ])
def test_case_9(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_3',
                              {'input_1': 1, 'input_2': 'a', 'input_3': 'a', 'input_4': False}, 'PASS'),
                         ])
def test_case_10(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_3', {'input_1': 'a', 'input_2': 'a', 'input_3': 'a', 'input_4': True}, 'NG'),
                         ])
def test_case_11(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_3', {'input_2': 'a', 'input_3': 'a', 'input_4': True}, 'NG'),
                         ])
def test_case_12(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_3', {'input_1': 1, 'input_2': 1, 'input_3': 'a', 'input_4': True}, 'NG'),
                         ])
def test_case_13(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_3', {'input_1': 1, 'input_2': 'a', 'input_3': 1, 'input_4': True}, 'NG'),
                         ])
def test_case_14(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_3', {'input_1': 1, 'input_2': 'a', 'input_3': 1, 'input_4': 'a'}, 'NG'),
                         ])
def test_case_15(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_2', {'idx': 5, 'input_1': 1, 'input_4': False}, 'PASS'),
                         ])
def test_case_16(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_2', {'idx': 5, 'input_1': 1, 'input_2': 'a', 'input_3': 'a', 'input_4': True}, 'PASS'),
                         ])
def test_case_17(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_2', {'idx': 5, 'input_1': 1, 'input_2': 'a', 'input_4': True}, 'PASS'),
                         ])
def test_case_18(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_2', {'idx': 5, 'input_1': 1, 'input_3': 'a', 'input_4': True}, 'PASS'),
                         ])
def test_case_19(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_2', {'idx': 5, 'input_1': 1, 'input_2': 'a', 'input_3': 'a'}, 'PASS'),
                         ])
def test_case_20(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_2', {'idx': 5, 'input_1': 1}, 'PASS'),
                         ])
def test_case_21(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_2', {'idx': 5, 'input_1': 1, 'input_2': 'a', 'input_3': 'a', 'input_4': False}, 'PASS'),
                         ])
def test_case_22(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']


@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_2', {'input_1': 'a', 'input_2': 1, 'input_3': 'a', 'input_4': 'a'}, 'NG'),
                         ])
def test_case_23(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_2', {'input_1': 1, 'input_2': 'a', 'input_3': 'a', 'input_4': True}, 'NG'),
                         ])
def test_case_24(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_2', {'input_1': 5, 'input_2': 'a', 'input_3': 'a', 'input_4': 'a'}, 'NG'),
                         ])
def test_case_25(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_2', {'input_1': 5, 'input_3': 'a', 'input_4': True}, 'NG'),
                         ])
def test_case_26(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_2', {'input_1': 5, 'input_2': 1, 'input_3': 1, 'input_4': 'a'}, 'NG'),
                         ])
def test_case_27(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_2', {'input_1': 5, 'input_2': 1, 'input_3': 'a', 'input_4': 1}, 'NG'),
                         ])
def test_case_28(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_2', {'input_1': 5, 'input_2': 1, 'input_3': 'a', 'input_4': 'a'}, 'NG'),
                         ])
def test_case_29(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_4', {'idx': 5}, 'PASS')
                         ])
def test_case_30(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_4', {'idx': 'a'}, 'NG')
                         ])
def test_case_31(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_4', {}, 'NG'),
                         ])
def test_case_32(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_1', {'idx': 2147483647}, 'NG')
                         ])
def test_case_33(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.get(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_1', {'idx': -2147483648}, 'NG')
                         ])
def test_case_34(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.get(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_1', {'idx': 2147483648}, 'NG'),
                         ])
def test_case_35(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.get(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_1', {'idx': -2147483649}, 'NG'),
                         ])
def test_case_36(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.get(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_3', {'input_1': 1, 'input_2': 'aaaaa', 'input_3': '', 'input_4': 0}, 'PASS'),
                         ])
def test_case_37(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_3', {'input_1': 1, 'input_2': '', 'input_3': 'aaaaabbbbb', 'input_4': 1}, 'PASS'),
                         ])
def test_case_38(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_3', {'input_1': 1, 'input_2': '', 'input_3': '', 'input_4': 1}, 'PASS'),
                         ])
def test_case_39(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_3', {'input_1': 1, 'input_2': '', 'input_3': 'aaaaabbbbb', 'input_4': 0}, 'PASS'),
                         ])
def test_case_40(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_3', {'input_1': 1, 'input_2': 'aaaaa', 'input_3': 'aaaaabbbbb', 'input_4': 1}, 'PASS'),
                         ])
def test_case_41(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_3', {'input_1': 1, 'input_2': 'aaaaab', 'input_3': 'aaaaabbbbb', 'input_4': 1}, 'NG'),
                         ])
def test_case_42(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_3', {'input_1': 1, 'input_2': 'aaaaa', 'input_3': 'aaaaabbbbbc', 'input_4': 1}, 'NG'),
                         ])
def test_case_43(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_3', {'input_1': 1, 'input_2': 'aaaaa', 'input_3': 'aaaaabbbbb', 'input_4': 5}, 'PASS'),
                         ])
def test_case_44(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']


@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_2', {'idx': 5, 'input_1': 1, 'input_2': 'aaaaa', 'input_3': '', 'input_4': 0}, 'PASS'),
                         ])
def test_case_45(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_2', {'idx': 5, 'input_1': 1, 'input_2': '', 'input_3': 'aaaaabbbbb', 'input_4': 1}, 'PASS'),
                         ])
def test_case_46(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_2', {'idx': 5, 'input_1': 1, 'input_2': '', 'input_3': '', 'input_4': 1}, 'PASS'),
                         ])
def test_case_47(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_2', {'idx': 5, 'input_1': 1, 'input_2': 'aaaaa', 'input_3': 'aaaaabbbbb', 'input_4': 1}, 'PASS'),
                         ])
def test_case_48(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_2', {'idx': 5, 'input_1': 1, 'input_2': '', 'input_3': 'aaaaabbbbb', 'input_4': 0}, 'PASS'),
                         ])
def test_case_49(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_2', {'idx': 5, 'input_1': 1, 'input_2': 'aaaaab', 'input_3': 'aaaaabbbbb', 'input_4': 1}, 'NG'),
                         ])
def test_case_50(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_2', {'idx': 5, 'input_1': 1, 'input_2': 'aaaaa', 'input_3': 'aaaaabbbbbc', 'input_4': 1}, 'NG'),
                         ])
def test_case_51(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_2', {'idx': 5, 'input_1': 1, 'input_2': 'aaaaa', 'input_3': 'aaaaabbbbb', 'input_4': 5}, 'PASS'),
                         ])
def test_case_52(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_4', {'idx': 2147483647}, 'NG'),
                         ])
def test_case_53(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_4', {'idx': -2147483648}, 'NG'),
                         ])
def test_case_54(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_4', {'idx': 2147483648}, 'NG'),
                         ])
def test_case_55(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']

@pytest.mark.parametrize("url, data, expected_result",
                         [
                             ('http://localhost:70/func_4', {'idx': -2147483649}, 'NG'),
                         ])
def test_case_56(url, data, expected_result):
    data_c = json.dumps(data)
    data = json.loads(data_c)
    actual_result = requests.post(url=url, json=data).json()
    logger.info(actual_result)
    assert expected_result in actual_result['Result']
