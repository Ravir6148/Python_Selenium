#
# def hello_decorator(func):
#     def inner1():
#         print("Hello, this is before function execution")
#         func()
#         print("This is after function execution")
#     return inner1
#
# def function_to_be_used():
#     print("This is inside the function !!")
#
# function_to_be_used = hello_decorator(function_to_be_used)
# function_to_be_used()

def deco_Func(func):
    def inner1():
        print("Before executing the wrapped func")
        func()
        print("Before executing the wrapped func")
    return inner1

def func_going_to_wrap():
    print("This is going to wrap")

func_going_to_wrap = deco_Func(func_going_to_wrap)
func_going_to_wrap()
