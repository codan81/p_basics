# We've declared this list for you
from sympy import appellf1


num_list = [2, 65, 3, 7, 39, 22, 11, 94, 299, 9, 20, 21, 51, 37]

# # Iterate through the provided `num_list` and print out every number in the list
# print("All of the numbers in the list are:")
# for each_ele in num_list:
#   print(each_ele)

# # Iterate through the provided `num_list` and create an if statement to print every number greater than 50
# print("Numbers greater than 50:")
# for each_ele in num_list:
#   if each_ele > 50:
#     print(each_ele)

# # Iterate through the provided `num_list` to print the index of the first occurrence of the number 11.
# print("Index of first occurrence of the number 11:")
# index = 0
# for each_ele in num_list:
#   if each_ele == 11:
    # print(num_list.index(each_ele))

# Iterate through the provided `num_list` and print the sum of all the numbers.
# print("Sum of all numbers:")
# sum = 0
# for number in num_list:
#     sum += number
# print(sum)


fruits = [
  "Apple", "Orange", "Banana", "Pomelo", "Apple", "Kiwi", "Peach", "Banana", "Grape", "Tomato",
  "Kiwi", "Apple", "Watermelon", "Lemon", "Pomelo", "Apple", "Banana", "Peach", "Apricot", "Grape"]

# Iterate through the provided `fruits` list and print the number of times "Apple" appears in the list.
print("Number of times 'Apple' appears in the list:")
count = 0 
for fruit in fruits:
    if fruit == "Apple":
        count += 1
print (count)

