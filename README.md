# Test Script 간략 설명

요구사항 문서 경로
- https://github.com/dnrwn/restapi_song > doc 하위 md 파일

TC 기준 문서 경로
- API : doc/APITest_TC_20250209.xlsx
- UI : 작성 예정

타겟 Server 경로
- https://github.com/dnrwn/restapi_song
- Flask, mysql을 이용한 Insert, Select, Update, Delete 기능 수행
- 간략한 UI 구성

## Unittest (일부 완료)
- 젠킨스 활용을 위해 레포지토리 분리
- 경로 : https://github.com/dnrwn/unittest_song
- pytest를 이용한 단위 테스트 수행
- pytest-cov로 coverage 측정
- pytest-html-report로 수행 결과 기록

## Excel Read (완료)
- Excel 문서에 작성한 Test Case를 통해 API Test 수행
- Requests 모듈 이용
- 결과 비교는 단순히 PASS, NG로 판단하게 되어 있으나 추후 업데이트 예정
- 새로운 Excel 문서를 생성하고 수행 결과 기입

## Pytest (완료)
- Pytest를 통해 API Test 수행
- Requests 모듈 이용
- Assert 문으로 Expected Result, Actual Result를 비교하게 되어 있으나 추후 업데이트 예정
- html-report를 통해 수행 결과 기록

## Postman (완료)
- Postman을 통해 API Test 수행
- Postman import를 위한 json 파일 작성 완료
- Request Code로 결과를 판단하도록 되어 있으나 추후 업데이트 예정

## Selenium (업데이트 필요)
- Selenium을 이용한 UI 테스트 수행
- assert 문으로 Expected Result, Actual Result를 비교하게 되어 있으나 추후 업데이트 예정
- screen capture로 수행 과정 기록
- log로 수행 과정 기록
- pytest-html-report로 수행 결과 기록
