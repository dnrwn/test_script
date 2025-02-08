API 테스트 TC 설계 과정 정리

설계 규칙은 특별한 이유가 없는 한 Unittest와 동일(필수, 선택 정보가 일부 상이함)
## 테스트 케이스 설계 규칙
- 페어와이즈 기법 (2-way)을 통해 동등 분할, 경계값 분석로 Case 추출
  - Mandatory일 경우 Null 값은 Invalid
  - Optional일 경우 Null 값은 Valid
- https://pairwise.yuuniworks.com/
1. 동등 분할
a. Int
  - Valid : 1
  - Invalid : 'a', Null
b. String
  - Valid = 'a', Null
  - Invalid = 1
c. Boolean
  - Valid = True, False, Null
  - Invlaid = 'a'
2. 경계값 분석
a. Int
  - valid : 1
b. String
  - Valid : ''(Min lengh), 'aaaaa'(Max lengh)
  - Invalid : 'aaaaab'(Max lengh + 1)
c. Boolean
  - Valid : 0, 1, 5

3. dict 형태로 전달하지 않은 Type Case (invalid)
  - list : [1, 'a', '3', 1]


Delete valid Case 수행  idx 값 처리 방안 검토 필요
- TC를 1회성으로 사용할 수 없으므로 idx 관리 프로세스를 가져갈 것인지, 아니면 idx를 추가하고 delete를 수행하는 절차를 가질 것인지 검토 필요
