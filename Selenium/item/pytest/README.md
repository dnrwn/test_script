버그
1. script 실행 시 assert 문에서 error 발생
   - result 요소 값이 변경됨
     - 기존의 경우 json data에서 각 line 별로 요소를 추출할 수 있었으나? (불확실) 현재는 통 data 로 들어옴
     - find 함수를 써서 data 분해 필요