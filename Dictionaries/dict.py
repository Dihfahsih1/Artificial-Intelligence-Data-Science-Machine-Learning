dict1={'a':1, 'b':2, 'c':3}
dict1['b']=4

dict1.update({'a':5,'e':10})
print(dict1)
del dict1['a']

get_dict=dict1.get('c')
print(dict1)


dict_keys=dict1.values()
print(dict_keys)


