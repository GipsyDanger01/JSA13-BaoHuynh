def find_value(numbers, number_to_find):
   low = 0
   high = len(numbers - 1)

   while low <= high:
       middle = low + (high - low) // 2

       if numbers[middle] == number_to_find:
           return middle
       elif numbers[middle] < number_to_find:
           low = middle + 1
       else:
           high = middle - 1
   return -1

# test data
numbers = [7, 9, 14, 22, 34]
number_to_find = 22

final = find_value(numbers, number_to_find)

if final == -1:
   print("This item was not found in the list.")
else:
   print("The number " + str(number_to_find) + " was found at index position " + str(final) + ".")

