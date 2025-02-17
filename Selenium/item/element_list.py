########## General ##########
url = 'http://localhost:70/ui'  # url
driver_path = './util/edgedriver_win64/msedgedriver.exe' # selenium script 실행 위치 기준


########## UI ##########
ui = {
    'insert': {
        'category': '/html/body/div/ul/li[1]',
        'input_1': '//*[@id="tab-1"]/form/p[1]/input',
        'input_2': '//*[@id="tab-1"]/form/p[2]/input',
        'input_3': '//*[@id="tab-1"]/form/p[3]/input',
        'input_4': '//*[@id="tab-1"]/form/p[4]/input',
        'submit': '//*[@id="tab-1"]/form/p[5]/input'
    },
    'select': {
        'category': '/html/body/div/ul/li[2]',
        'idx': '//*[@id="tab-2"]/form/p[1]/input',
        'submit': '//*[@id="tab-2"]/form/p[2]/input'
    },
    'update': {
        'category': '/html/body/div/ul/li[3]',
        'idx': '//*[@id="tab-3"]/form/p[1]/input',
        'input_1': '//*[@id="tab-3"]/form/p[2]/input',
        'input_2': '//*[@id="tab-3"]/form/p[3]/input',
        'input_3': '//*[@id="tab-3"]/form/p[4]/input',
        'input_4': '//*[@id="tab-3"]/form/p[5]/input',
        'submit': '//*[@id="tab-3"]/form/p[6]/input'
    },
    'delete': {
        'category': '/html/body/div/ul/li[4]',
        'idx': '//*[@id="tab-4"]/form/p[1]/input',
        'submit': '//*[@id="tab-4"]/form/p[2]/input'
    },
    'result_old': '/html/body/div[3]/div[2]/div[2]/div[2]/span[2]',
    'result': '/html/body/pre'
}


########## input value ##########
input_value_valid = {
    'select_int': {
        0: 2
    },
    'delete_int': {
        1: 3
    },
    'int': {
        0: -2147483648,
        1: 2147483647
    },
    'str5': {
        0: 'a',
        1: 'ABCDE',
        2: ''
    },
    'str10': {
        0: 'a',
        1: 'ABCDEFGHIJ',
        2: ''
    },
    'boolean': {
        0: 1,
        1: 0
    }
}
input_value_invalid = {
    'int': {
        0: -2147483649,
        1: 2147483648,
        2: ''
    },
    'str5': {
        0: 'aaaaaa'
    },
    'str10': {
        0: 'aaaaaaaaaaa'
    },
    'boolean': {
        0: 2,
        1: 'aaaaaaa',
        2: ''
    }
}
