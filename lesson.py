# 1
fitus = ('appel','banana', 'cherry', 'orenge','kiwi')
print (fitus[1])
print(fitus[-1])
print(fitus[3])
# 2
nambers = (1,2,3,4,2,5,6,2)
soni = nambers.count(2)
print(soni)
print (nambers[5])
# 3
color = ["red", "green", "blue"]
color.append ("yellow")
print(color)
# 4
letters = ['a', 'b', 'c', 'd', 'e']
letters.reverse()
print(letters)
# 5 tusgunmadim
nested_tuple = (1, 2, (3, 4, 5), 6, 7)
print(nested_tuple[2])
# 6
my_tuple = [10, 20, 30, 40, 50]
my_tuple.append(60)
my_tuple = tuple(my_tuple)
my_tuple = list(my_tuple)
print(my_tuple)
# 7
tuple1 = [1, 2, 3]
tuple2 = [4, 5, 6]
tuple1.extend(tuple2)
print(tuple1)