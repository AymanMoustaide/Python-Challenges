
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


favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Apple Pie':
        print('Yes one of my favorite desserts is', dessert)
        break #! If this block become True , It's ignore else: 

    else:
        print('No sorry, not a dessert on my list')