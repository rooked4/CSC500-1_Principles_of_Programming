# Charlie Goldstein
# CSC500-1
# Module 7: Critical Thinking Assignment

# Step 1: Data Specifications

# Dictionary for Room Number
room_num = {"CSC101": "3004", "CSC102":"4501", "CSC103":"6755", "NET110":"1244", "COM241":"1411"}

# Dictionary for Instructor
instructor_name = {"CSC101": "Haynes", "CSC102": "Alvarado", "CSC103": "Rich", "NET110": "Burke", "COM241": "Lee"}

# Dictionary for Meeting Time
meeting_time = {"CSC101": "8:30 AM", "CSC102": "9:30 AM", "CSC103": "10:30 AM", "NET110": "11:30 AM", "COM241": "1:00 PM"}


# Step 2: Program Logic

course_num = "dummy value"  # Initialize course_num as a default dummy value.
course_num = input("Enter a course number or 'q' to exit program: ")


while course_num not in room_num and course_num != 'q':
    course_num = input("Iam sorry, I cannot find this course number in our course catalogue. Let's try again. Please enter a course number or 'q' to exit program.")

if course_num == "q":
    print("Thank you for choosing the course catalogue. Have a great day!")

else:
    print("Course Number: " + course_num)
    print("Room Number: " + room_num[course_num])
    print("Instructor: " + instructor_name[course_num])
    print("Meeting Time: " + meeting_time[course_num])
    print()
    print("Thank you for choosing the course catalogue. Have a great day!")