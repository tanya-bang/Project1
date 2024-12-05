"""
namesapce: 변수와 함수가 저장되는 공간
builtin : 파이썬의 기본내장함수 및 기본 예외가 저장되는 공간
global : 전역에 선언된 변수가 저장되는 공간
local : 함수 내부에 선언된 변수가 저장되는 공간

파이썬의 변수는 functional scope를 가진다.
함수 안에서 선언된 변수는 함수 안에서 사용이 가능하다.
"""

global_var = 'global_var'
var = '전역변수'

def study_builtin():
    print(dir(__builtins__))
# 그냥 이런게 있구나~ 하고 알고만 넘어가
# 프린트하면 뭐가 졸래 많이 나오는데 우리가 접근할 일 없음 ^^
# study_builtin()

# ==========여기서부터 본격 네임변수============

def study_namespace():

    global global_var
    global_var = '수정된 전역변수'

# local var

    outer_var = 'outer_var'

    def inner_fnc():
        inner_var = 'inner_var'

        # nonlocal : 
        # 지역 내부에서 한 뎁스 위에 있는
        # local namespace의 변수를 사용하겠다는 의미
        nonlocal outer_var
        outer_var = '수정된 outer_var'

    if(True):
        if_var = 'if_var'
    print(if_var)
    # 원래 이렇게 사용 못하는데, 함수 단위 스코프를 가지기 때문에
    # 이렇게 if문 바깥에서 print if_var해도 프린트 가넝한
    
    print(outer_var)
    inner_fnc()
    print(outer_var)

print(global_var)
study_namespace()
print(global_var)
    