import functools

# log装饰
# 增加name输出
def log(f):
    @functools.wraps(f)
    def fn(x):
        print('call ' + f.__name__ + '()...')
        return f(x)
    return fn

# log_装饰 log_带参数
# 增加name输出 及 log参数
def log_(prefix):
    def pre_func(f):
        @functools.wraps(f)
        def func(*args , **kw ):
            print(prefix + ' call ' + f.__name__ + '()...')
            return f(*args, **kw)
        return func
    return pre_func

@log
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

@log_('prefix')
def factorial_(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result


print(factorial(10))
print(factorial_(10))

# 装饰后属性变化
# 通过 @functools.wraps(f) 保证属性一致
print(factorial.__name__)
print(factorial_.__name__)



