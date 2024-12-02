# Part 2: Alarm clock calculation
current_time = int(input("Enter the current time (0-23): "))
wait_hours = int(input("Enter the number of hours to wait for the alarm: "))

# Calculate alarm time
alarm_time = (current_time + wait_hours) % 24

# Display the result
print("\nThe alarm will go off at: {}:00 (24-hour format)".format(alarm_time))
