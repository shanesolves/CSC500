# Dictionaries containing course information
room_numbers = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

meeting_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# User input
course_number = input("Enter the course number (e.g., CSC500): ")

# Check if the course exists
if course_number in room_numbers:
    # Retrieve and display the details
    print("Course Details:")
    print("Room Number:", room_numbers[course_number])
    print("Instructor:", instructors[course_number])
    print("Meeting Time:", meeting_times[course_number])
else:
    # Error message
    print("Error: Course not found. Please check the course number and try again.")
