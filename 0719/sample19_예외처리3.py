'''
    예외처리( exception handling)

    1. 예외 ( exception) ?
      --> 일반적으로 '에러' 라고 부른다
      --> 실행중에 발생되는 '문제발생'
      --> 예외가 발생되면 프로그램이 '비정상종료' 된다.
        예> 화면이 멈추거나...

    2. 예외처리(exception handling)?
        --> 프로그램 실행중에 어쩔수 없이 발생된 예외를
            '비정상종료'하도록 두지 않고
            '정상종료' 하도록 유도하는 작업을 의미한다.

    3. 예외처리 방법
        가. 예외클래스 사용( 시스템에서 제공 )
            -> 예외클래스도 상속관계로 되어 있다.

            -SyntaxError: 문법오류
            -ZeroDivisionError: 0으로 나누었을 때 발생
            -IndexError: 인덱스 범위가 넘어갔을때
            -KeyError: dict에서 key값 없을 때
            -FileNotFoundError: 파일이 없을 때
            -XXXError
        나. try ~ except 문장
            try:
                문장1(실행하고자 하는 문장)
                문장2(실행하고자 하는 문장)
                ...
            except 예외클래스 as 별칭
                문장(예외가 발생했을 때 예외처리문장) --> 사용자가 실행하고자 했던 작업이 실패한 이유를 알려주는것이다.
        ==> except에 지정하는 아무 클래스 사용하지 못하고 예외처리를 담당할 수 있는 적합한 예외클래스로 지정해야 한다.
            단, 상속관계 구조로 봤을 때 부모 예외클래스는 사용할 수 있다.
        ==> Exception은 XXXError 예외클래스들의 최상위 예외클래스로 간주되어 처리된다.
            except Exception as e:  어떤경우든 처리 가능
                pass
        ==> e 변수에는 실행중에 발생된 예외정보를 가지고 있다.
            print(e)

    4. 다중 except문
        try:
            문장1 --> ZeroDivisionError 발생될 수 있는 코드
            문장2 --> KeyEror 발생될 수 있는 코드
            문장3 --> ?
        except ZeroDivisionError as e:
            문장
        except KeyError as e:
            문장
        except Exception as e:

    5. finally문
        --> 예외가 발생해도 실행되고
            발생하지 않아도 실행되는 문장
            따라서 무조건 실행해야 하는 문장을 사용할 때 지정한다.

        try:
            문장
        except Exception as e:
            문장
        finally:
            문장 ( 반드시 실행되는 문장 암시)
        주로 외부자원(파일, db, 네트워크) 연동시
        반드시 작업후에는 자원반납( close() ) 처리시 사용한다.

    6. 명시적으로 예외 발생(raise 예외클래스명)
     --> 시스템이 예외로 간주하지 않는다.
        사용자만 예외로 간주한다 --> 시스템이 예외발생 안시킨다. 따라서 사용자가 명시적으로 예외발생 시킨다.
       예> sql문에서 SELECT시 데이터가 없을 때

       sql = "select * from emp"
       count = con.execute(sql)
       if(count==0):
           raise Exception  # Exception 예외클래스로 명시적인 예외발생
'''
print("1")

try:
    x= {"name":"aaa"}
    print(x["age"]) #KeyError 발생
    num = 0
    result = 10 / num # ZeroDivisionError
    print("결과값: ",result)
except ZeroDivisionError as e:
    print("ZeroDivisionError",e)
except KeyError as e:
    print("KeyError",e)
except Exception as e:
    print("Exception",e)
finally:
    print("finally문 : 반드시 실행되는 문장")
print("end(정상종료)")

print(ZeroDivisionError.mro())
