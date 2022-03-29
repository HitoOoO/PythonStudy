List_Comprehension = [i for i in range(10) if i%2==0]     #列表推导式
List_Comprehension2 = (i for i in range(10) if i%2==0)  #返回生成器


a = ['a','b','c']
b = [1,2,3]
Dict = {k:v for k,v in zip(a,b)}    #字典推导式
#print(List_Comprehension)
#print(List_Comprehension2)
#print(Dict)
print(type(List_Comprehension),(type(List_Comprehension2)))