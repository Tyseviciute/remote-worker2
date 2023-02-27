my_list = [a for a in range(7)]
new_list = [a for a in range(10) if a in my_list and a%2==0]
print(new_list)

my_list = list()
my_list.append([4, [3, 2], 1])
my_list.extend([9, 10, 11])
print(my_list[0][1][1] + my_list[2])

my_list = [11, 22, 32, 17, 7]
print(my_list.pop(-3)),
my_list.remove(my_list[0]),
print(my_list)
my_tuple = (2e-04, True, False, 18, 1.7, True)
val = 0
for a in my_tuple:
  val += int(a)
print(val)

my_dict = dict()
for i in range (3):
  for j in range(2):
    my_dict[i] = j
print(my_dict)