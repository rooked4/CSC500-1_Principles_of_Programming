# Charlie Goldstein
# CSC500-1
# Module 7: Pseudocode


Pseudocode:

# Step 1: Data Specifications

# Dictionary for Room Number
room_num = {"CSC101": "3004", "CSC102": "4501", "CSC103": "6755", "NET110": "1244", "COM241": "1411"}

# Dictionary for Instructor
instructor_name = {"CSC101": "Haynes", "CSC102": "Alvarado", "CSC103": "Rich", "NET110": "Burke", "COM241": "Lee"}

# Dictionary for Meeting Time
meeting_time = {"CSC101": "8:30 AM", "CSC102": "9:30 AM",
	"CSC103": "10:30 AM", "NET110": "11:30 AM", "COM241": "1:00 PM"}

# Step 2: Program Logic

# Input course number
INITIALIZE course_num = "dummy value"
PRINT "Welcome to Charlie’s course catalogue program. Please enter a course number or "q" to exit program:"
INPUT course_num

# Request valid course input or sentinel value to allow user to exit.
WHILE course_num NOT IN room_num AND course_num NOT EQUAL "q"
	PRINT "I am sorry, I cannot find this course in our course catalogue. Let's try again. Please enter a course number or "q" to exit program"
	INPUT course_num
END WHILE

IF course_num == "q" THEN
	PRINT "Thank you for choosing the online course catalogue. Have a great day!"
ELSE

	# Retrieve and display the Room number, Instructor and Meeting Time.
	PRINT "Course information"
	PRINT "Course number: " + course_num
	PRINT "Room number: " + room_num[course_num]
	PRINT "Instructor: " + instructor_name[course_num]
	PRINT "Meeting Time: " + meeting_time[course_num]
	PRINT
	PRINT "Thank you for choosing the Charlie’s course catalogue. Have a great day!"
END IF
