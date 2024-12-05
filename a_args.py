# 여기는 외워라
# 함수가 인자를 전달받는 다섯가지 방법

def study_arg1(a:int, b:int):
    """
    타입힌트 : 사용자에게 인자의 타입에 대한 힌트를 제공
        - 다른 언어는 이런식으로 a:int, b:int라고 명시해주면
          자동으로 int만 넣게 강제가 되는데 파이썬에서는 강제하는 기능이 없음.
          print(study_arg1(10,10))이 내가 기대한건데
          print(study_arg1(a,b)) 이런 식으로 넣음 ㅋㅋ
    """
    return a + b

def study_arg2(age:int, user:str = 'anonymous'):
    """
    default-arg
    매개변수에 인자가 전달되지 않을 경우 사용할 기본값을 지정
    """
    print(f'사용자 {user}의 나이는 {age}살 입니다.')

# study_arg2(100)

def study_arg3(age:int, *args, user:str = 'anonymous'):
    """
    가변매개변수
    매개변수의 개수를 지정할 수 없을 때 사용한다.
    사용자가 전달한 복수의 인자는 tuple안에 담겨 전달된다.
    일반 매개변수 뒤에 작성되어야 한다.
    """

    print(type(args))
    print(args)
    sum = 0
    for i in args:
        sum += i
    print(f'가변인자의 합: {sum}')

# 인자를 매개변수로 전달할 때
# 어떤 매개변수에 들어가야하는 지를
# 위치로 나타내는 방식을 위치인자 ex) 100
# 매개변수 명으로 나타내는 방식을 키워드인자 ex) user='azi'
# 키워드인자가 위치인자보다 뒤에 위치해야 한다.

study_arg3(100, 1, 2, 3, 4, 5, user='tanya_')
# 제일 앞에 있는 100은 age에 들어가고 나머지 1~5가 가변매개변수인 args에 들어감

def study_arg4(age:int, user:str = 'anonymous', *args, **kwargs):
    """
    키워드 가변 매개변수 (kwargs로 줄여서 씀)
    인자를 넘길 때, 매개변수명을 지정해서 복수의 인자를 전달하면
    매개변수명을 key, 인자값을 value로 가지는 dict에 담아서
    kwargs에 전달해준다.
    """
    print('타입: ', type(kwargs))
    print('키워드아규먼트: ', kwargs)
    # dict니까 for in 문 사용 가능
    for item in kwargs.items():
        print(item)

#study_arg4(100, 'tanya', 1, 2, 3, 4, 5, unserstanding='zero', sleep='100%')

def study_arg5(age:int, height:int):
    print(f'{age}살의 평균 키는 {height}입니다.')

# 인자를 넘길 때 튜플로 넘겨볼 겁니다.
args = (10, 25)
study_arg5(*args)