
#_ FOR LOOP 


# cars = ['Audi', 'Rolls Royce', 'Nissan GTR']

# #! assinge a variable to each item in cars
# for a in cars:
#     print(a)

#_ CODE EXERCISE
#*WRITE A PROGRAM THAT CALCULATES THE AVERAGE STUDENT HEIGHT FROM A LIST OF HEIGHTS.

# 156 178 165 171 187
# #!DON'T CHANGE THE CODE BELOW

# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# # print(student_heights)


# #!DON'T CHANGE THE CODE ABOVE 

# total_height = 0 #! EMPTY VARIABLE THAT WILL UPDATE LATER
# for height in student_heights:
#     total_height += height
# print(total_height)
    
# total_student = 0 #! EMPTY VARIABLE THAT WILL UPDATE LATER
# for student in student_heights:
#     total_student += 1
# print(total_student)

# average_height = total_height / total_student
# round_average = round(average_height) #! TO DISPLAY NUMBERS WITHOUT NUMBERS AFTER COMA

# print(f'There are a total of {total_student} student and the average is {round_average}')

# #!WRITE YOUR CODE BELOW THIS ROW 



#_ CODE EXERCISE TWO (HOW MUCH THIS COMPANY WORTH)

# available_cars = ['AUDI', 'NISSAN', 'ROLLS ROYCE', 'MERCEDES','FERRARI']
# each_car_price = ['100000', '80000', '250000', '90000', '120000']

# cars_price = [available_cars, each_car_price]

# mapping = dict(zip(available_cars, each_car_price)) #! Assinge values in one list to another list using (dict(zip))

# mapping_list = list(mapping.items()) #Convert the dictionary to a list of tuples

# print(mapping_list[0])

# for av in available_cars:
#     print(av)


#_ CODE EXERCISE FIZZ BUZZ GAME 

#! Your program should print each number from 1 to 100 in turn.


# for i in range(1, 101):
#     print (i)
#     if i % 5 == 0:
#         i = 'Buzz'
#         print(i)
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# I
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".
# And if the number is divisible by both 3 and 5 e.g.
# 15 then instead of the number it should print "FizzBuzz"



#_________________
# n = int(input())

# if n % 2 == 1:
#     print('Weird')
# elif 2 <= n <= 5 and n % 2 == 0:
#     print("Not Weird")
# elif 6 <= n <= 20 and n % 2 == 0:
#     print("Weird")
# elif n > 20 and n % 2 == 0:
#     print("Not Weird") 

#//                  

# a=int(input())
# b=int(input())
# print(a//b)

#! SQUARE
# n = int(input())
# for x in range(n):
#     print(x ** 2)


#! 
# n = int(input("Enter a number: ").strip())

# for x in range(1, n + 1):
#     print(x, end='')

# count = 1 
# while count < 5:
#     count += 1
#     print(count)


# We'll print the number of read or unread notifications that a user received.
# 1. If  u⁠n⁠r⁠e⁠a⁠d⁠  is not  0⁠ , print  Y⁠o⁠u⁠ h⁠a⁠v⁠e⁠ {⁠u⁠n⁠r⁠e⁠a⁠d⁠}⁠ u⁠n⁠r⁠e⁠a⁠d⁠ m⁠e⁠s⁠s⁠a⁠g⁠e⁠s⁠ . Use f-string to display the value of  u⁠n⁠r⁠e⁠a⁠d⁠  inside the string.
# 2. Else print  N⁠o⁠ u⁠n⁠r⁠e⁠a⁠d⁠ m⁠e⁠s⁠s⁠a⁠g⁠e⁠s⁠.⁠ C⁠h⁠e⁠c⁠k⁠ y⁠o⁠u⁠r⁠ {⁠r⁠e⁠a⁠d⁠}⁠ r⁠e⁠a⁠d⁠ m⁠e⁠s⁠s⁠a⁠g⁠e⁠s⁠ . Use f-string to display the value of  r⁠e⁠a⁠d⁠  inside the string.

reminder_count = 0
while reminder_count < 3:
    reminder_count += 1
    
    print("Reminder: Stop the bot!")
    
