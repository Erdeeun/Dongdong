import datetime

#주민번호 입력받기
joomin=input("주민번호를 입력하세요")
#940113-2111111
#입력된 주민번호로 생년월일을 구한다.
#1.년도 구하기
print(joomin[7])
print(type(joomin[7]))

if joomin[7] == "1" or joomin[7] =="2" :
    year="19"
elif joomin[7] == "3" or joomin[7] =="4" :
    year="20"
print (year + joomin[0:2])
year=year+joomin[0:2]
#yyyy-mm-dd 형식
month=joomin[2:4]
day=joomin[4:6]
print(f'{year}-{month}-{day}')
#print(year + '-' + month + '-' + day)자바식
#한국식 나이를 구한다 (현재 년도 - 태어난 년도 +1)

# 현재 날짜 구하기 = datetime 을 쓰면 된다
current_year = datetime.date.today().year

korean_year=current_year - int(year) + 1
print(korean_year)
#성별을 구한다.
if joomin[7] == '1' or joomin[7] == '3' : 
    sex="남성"
elif joomin[7] == '2' or joomin[7] == '4' :
    sex="여성"

print (f'당신의 성별은 {sex} 입니다.')