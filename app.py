# 1
my_list = ['olma', 'banan', 'gilos', 'shaftoli']
user_element = input("Element kiriting: ")
print(my_list.index(user_element))


# 2
numbers = [45, 12, 78, 3, 56, 9]
min_index = numbers.index(min(numbers))
print(min_index)


# 3
letters = ['B', 'C', 'A', 'D', 'A', 'E']
print(letters.index('A'))


# 4
my_list = ['python', 'java', 'c++', 'go']
user_element = input("Element kiriting: ")
if user_element in my_list:
    print("Mavjud, indeksi:", my_list.index(user_element))
else:
    print("Mavjud emas")


# 5
letters = ['a', 'b', 'c', 'd', 'e']
user_letter = input("Harf kiriting: ")
if user_letter in letters:
    letters.remove(user_letter)
print(letters)
