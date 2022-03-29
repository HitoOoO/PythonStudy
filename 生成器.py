def simple_gen():
    yield 'hello'
    yield 'world'
gen = simple_gen()  #返回生成器对象
print(type(gen))
print(next(gen))
print(next(gen))