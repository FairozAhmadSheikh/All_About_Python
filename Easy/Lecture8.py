# Logical Opeartor and or and Not 
# Function to check pass/fail status

exam_score = float(input("Enter your exam score (0-100): "))
attendance_percentage = float(input("Enter your attendance percentage (0-100): "))

# Using logical operators to check if the student has passed
if exam_score >= 50 and attendance_percentage >= 75:
    print("Congratulations! You have passed.")
elif exam_score < 50 and attendance_percentage < 75:
    print("You have failed. Both exam score and attendance are below passing criteria.")
else:
    if exam_score < 50:
        print("You have failed due to low exam score.")
    else:
        print("You have failed due to low attendance.")



