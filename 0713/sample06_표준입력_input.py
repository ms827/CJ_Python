'''
표준입력
1.키보드로 입력
2.input() 함수 사용
3.특정 함수의 사용 방법 알아보기
    help(함수명)
4. 입력받은 모든 데이터는 문자열(str)로 처리된가.
    따라서 숫자로 변경해야 하는 경우 int()로 변경하고 처리한다
'''
help(input)

name = input("이름입력:")
age = input("나이입력:") #입력값 문자로 저장 연산불가
print("입력값:", name, int(age)+1, type(age))
