# Task 1: Create a Dictionary of Student Marks

# create a dictionary with student name as keys and marks as value

student_mark = {"Alice":85, "Bob":90, "Carol":75, "Diana":75, "Eva":85, "Fanny":93}

# Ask to user to input a student's name

student_name = input("Please enter your name:  ")

# Display corresponding marks and if student's name not found display appropriate message

if student_name in student_mark:
    print(f"{student_name}'s mark:{student_mark[student_name]}")
else:
    print("Sorry, your name is not available.")
