
#_ GRADING PROGRAM

#* INSTRUCTIONS



student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99, 
    "Draco": 74,
    "Neville": 62,
}

# 🚨 Don't change the code above 👆

#! TODO1: CREATE AN EMPTY DICTIONARY CALLED STUDENT_GRADES.

student_grades = {}

#!TODO2: WRITE YOUR CODE BELOW TO ADD THE GRADES TO STUDENT_GRADES.👇


for x in student_scores:

    if student_scores[x] >= 91:
        student_scores[x] = 'Outstanding'
        
        student_grades = x, student_scores[x]
    
    elif student_scores[x] >= 81 and student_scores[x] <= 90:
        student_scores[x] = 'Exceeds Expectations'
        student_grades = x, student_scores[x]


    elif student_scores[x] >= 71 and student_scores[x] <= 80:
        student_scores[x] = 'Acceptable'
        student_grades = x, student_scores[x]

        
    elif student_scores[x] <= 70:
        student_scores[x] = 'Fail'
        student_grades = x, student_scores[x]


    print(student_grades)
    
        
        

# print(student_grades)