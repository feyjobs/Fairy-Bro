# different between args & kw
# 非关键字参数 用于元组 关键字参数 用于字典
def foo(*args, **kw):
    print('args = ', args)
    print('kw = ', kw)
    print('--------------------')

if __name__ == '__main__':
    foo(1,2,3,4)
    foo(a=1,b=2,c=3)
    foo(1,2,3,4,a=1,b=2,c=3)
    foo('a',1,None,a=1,b='2',c=3)