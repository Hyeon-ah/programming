# -*- coding: utf-8 -*-
"""210604.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_zYMNnP7isGrnvuLxq7GATkVU0KGA0Fy
"""

# 구글 시트를 활용하기 위한 라이브러리 import
import gspread

# 구글 시트에 접근할 수 있는 권한을 얻기 위한 코드
from google.colab import auth
auth.authenticate_user()

from oauth2client.client import GoogleCredentials

gc = gspread.authorize(GoogleCredentials.get_application_default())

# 원하는 시트 파일 열기
worksheet = gc.open('CDI  Data results(210604)')
# 원하는 탭 열기
worksheet = worksheet.worksheet('seg4_CDI')

#원하는 탭의 값을 모든 리스트로 불러오기
cell_list = worksheet.get_all_values()

#불러온 리스트 출력
print(cell_list)

# 임시 빈 리스트 생성
temp = []

#불러온 시트의 2번 행부터 9번 행까지 있는 데이터의 0번, 2번 데이터 불러오기
for i in range(len(cell_list)):
  if i > 1 and i < 10:
    temp.append([cell_list[i][0],cell_list[i][2]])

print(temp)

finding = gc.open('【영아용(8~17개월)】(Seg4) K M-B CDI 맥아더-베이츠 의사소통발달 평가의 (응답)').sheet1

test_sheet = finding.get_all_values()

for i in test_sheet:
  print(i)

answer = []

for i in range(len(test_sheet)):
  if i >2:
    for find in temp:
      if ((find[1].replace(' ','') == test_sheet[i][6].replace(' ','') and (find[0] in test_sheet[i])):
        answer.append(test_sheet[i])

for i in answer:
  print(i)

a = 3
b = 3
 # a 와 b는 같은가요?
# range(2) = [0,1]
for i in range(2):
  print(i)
  if a == b:
    print("a 와 b 는 같다")
    b = 4
  else:
    print("a 와 b 는 다르다")
# if a == b:
#    print("a 와 b 는 같다")
#    b = 5

# if a == b:
#   print("a 와 b 는 다르다")

a = b  # a의 값에 b를 넣어라
print(a)
