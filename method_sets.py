# Adding values to an empty set
b=set()
print(type(b))
b.add(10)
b.add(4)
# b.add([10,40,67])can not be added in the sets
# tuble can be added in the sets but list can not be added in the sets 
b.add((30,40,50,90,1000))
# Adding a value repeatedly does  not  change a set
b.add((4,5,6))
print(b)
# prints the length of the b
print(len(b))
print(b)
# remove()
# pop()
# union()
# clear()
# intersection()

