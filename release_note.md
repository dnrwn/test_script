예정
- 이슈 : 젠킨스 파이프라인에서 selenium 실행하면 아래 error가 발행해서 진행 안됨
  - local에서 직접 하면 잘 됨
- selenium.common.exceptions.SessionNotCreatedException: Message: session not created: Microsoft Edge failed to start: crashed.
  (session not created: DevToolsActivePort file doesn't exist) 
- driver 경로 문제인가 싶어서 여러번 테스트 했으나, 다른 문제인 것 같음
- google에서 사례가 종종 보였지만 해결되지 않음

- excel read 로는 젠킨스 파이프라인에서 트리거로 사용하기 어려움 
-> pytest를 이용한 api 테스트용 case 추가 검토, postman으로 트리거 가능할지 검토

- event.py 파일 실행 경로에 상관 없이 동작하도록 경로 부분을 절대 경로로 모두 수정
- file_read.py : file_read, sheet_read 함수 정리할 필요가 있을지 검토
- event.py : function_name, method, url 정보 관리 위치 검토 필요
- postman, selenium, excel_read 통합 관리
  - readme 파일 정리 필요 (재작성 등)
- Selenium_script.py 파일 분리
  - 기본 Script (파라미터로 단일 Case를 처리하는 Script)와 실제 Test를 구동하는 Script 분리)

2025-02-17 업데이트
1. Selenium Test Case 수정
- parametrize를 사용하여 각 Case가 독립적으로 수행되도록 ㅜㅅ정
- Selenium 하위 run.py 파일로 수행하도록 수정
- result 경로 수정
- edge webdriver 변경 (131 -> 133)

2. jenkins 파이프라인 수정
- excel_read, pytest, selenium이 병렬로 수행되도록 수정

2025-02-10 업데이트
- API Test용 TC 업데이트 완료
  - pytest.ini 인식 이슈가 있어서 ini 파일을 지정해서 테스트 수행해야 함
    - pytest -c pytest.ini test_apitest_tc.py
  - Case 추출 기준 : excel_read 경로에 있는 TC 문서

2025-01-28 업데이트
file_read.py
1. TC 파일 경로 수정
- test_script 경로에서 실행하는 조건에 맞게 수정
2. TC result 생성 경로 수정
- test_script 경로에서 실행하는 조건에 맞게 수정
3. log 경로 수정
- test_script 경로에서 실행하는 조건에 맞게 수정

version : 0.6, date : 2025-01-21
- console log 추가 code 작성

version : 0.6, date : 2025-01-21
- file_write 함수 작성 완료 (file_read.py)
- TC 문서에 test_data 항목 추가 예정 (file_read)
  - test date 정보는 file 명으로 관리 하기로 결정 (적용 X)

version : 0.5, date : 2025-01-20
- 주요 변경 사항 
  - actual_result, record를 cell 값이 아닌 cell 위치로 저장
  - write 함수 초기 설계 완료
    - excel write, save 부분 추가 후 완료 예정
  - excel read 값을 json type으로 변환하도록 수정
  - case_run 함수 최적화 (event.py)
  - 기능을 dict 형태 data로 저장하고 for문을 통해 간략화

- 주요 변경 사항
  - 기존 : 각 Cell 의 값을 동적 변수에 삽입하는 부분에서 중단
  - 변경 : 각 Cell 의 값을 동적 변수에 삽입하고 dict 변수에 추가
- event.py 추가
  - 역할 : file_read.py 에서 dict 변수에 추가된 각 Cell 의 Value 를 이용해서 API 에 접근

version : 0.3, date : 2024-03-30
- main -> file_read 파일명 변경
- event -> GET, POST in/out Event 생성 (Postman 대응)
- 주요 변경 사항
  - 기존 : globals 함수를 통해 python script 로 테스트 결과 생성
  - 변경 : Excel 의 각 cell 값을 GET, POST 형태로 전달 (func_connect() 함수 수정)
- input 을 통해 if 문으로 tkinker 사용 시 탐색기 시작되지 않고 프리징 현상 발생하여 File 수동 선택하도록 작성


version : 0.2.1, date : 2023-09-07
- python tc, function 부분 분리 (미완)
- main script 보완

개요 : 엑셀 문서로 작성된 TC와 Python Script로 작성된 TC를 통해 API 기능 실행 결과를 기록하는 로직 작성

1. 구성
- TC.xlsx : TC 예시 문서
- file_read.py : TC 문서 data를 동적 변수에 삽입, 삽입된 변수를 py_tc.py 의 함수에 전달, py_tc.py의 return 값을 TC 문서에 기록
- event.py : Test 실행 부분

2. Test Case (TC.xlsx) : 엑셀 파일의 행을 기준으로 아래의 Test item 작성
- Function name
- No
- description

[comment]: <> (- valid, Invalid, 해당 값으로 인해 영향을 주는 로직 없음)
- type
- Parameter
- Expected Result

3. Main 로직 (file_read.py) : TC.xlsx의 Item 을 읽고 동적 변수에 삽입
- Function Name : py_tc.py의 함수명을 호출하기 위해 삽입
- Parameter : py_tc.py의 인자로 삽입하기 위해 삽입

4. Test Case 로직 (event.py) : 

[comment]: <> (- 동적 변수를 통해 얻은 valid, invalid 값으로 result 를 분개한다. &#40;if 문, try 문&#41;)
- 동적 변수를 통해 얻은 parameter 를 func.py에 전달(다중 인자 활용 업데이트 필요)
- func.py의 return 결과를 main.py로 전달

5. Test Case 수행 결과 (TC.xlsx)
- 엑셀 파일의 result 열에 수행 결과 입력 후 새로운 파일로 저장한다.

※ file_read.py와 etc_main.py 차이 : 파일 선택, 읽기, 쓰기 등 각 기능 모듈화 계획이 file_read, 초기 계획이 etc_main 

================
5. 2차 계획
- main.py : parameter cell의 data가 쉼표(,) 로 구분될 경우 parameter 분리 code 추가
  -> 복수의 parameter 입력 대응
