#可变类型作为参数
def flist(l):
    l.append(0)
    print(l)

ll=[]
flist(ll)
flist(ll)

#不可变类型作为参数
def fstr(s):
    s+='a'
    print(s)

ss = 'bbb'
fstr(ss)
fstr(ss)



#例题

def clear_list(l):
    l=[]

ll=[1,2,3]
clear_list(ll)
print(ll)

#可变参数作为默认参数  默认参数只计算一次
def flist(l=[1]):
    l.append(1)
    print(l)
flist()
flist()


#什么是可变参数
def print_multiple_args(*args):
    print(type(args),args)
    for idx,val in enumerate(args):
        print(idx,val)
print_multiple_args('a','b','c')

#关键子参数
def print_multiple_args(**kwargs):
    print(type(kwargs),kwargs)
    for k,v in kwargs.items():
        print('{}:{}'.format(k,v))
print_multiple_args(a=1,b=2)

#test
def print_all(a,*args,**kwargs):
    print(a)
    if args:
        print(args)
    if kwargs:
        print(kwargs)
print_all('hsdad','aa','bbbbb','vvvvv',c='ccc')