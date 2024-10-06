# Author : Eric Kemske Jr
# Class : ITN160
# Class Section : 602
# Date : 10/02/2024
# Assignment : Project 1 : Grade Calculation Program

# Supported by module 8, as well as a little bit of outside help from stackoverflow.com, geeksforgeeks.org, and w3schools.com,
# Either from conceptual ideas taken and molded in here or concepts themselves learned.

# Welcomes the teacher to the program
print("\nWelcome, to the amazing, awesome, super cool grade calculation program!!1!")

cont = True         # True variable stated to easily turn off while loop later
count_for_name = 1  # Used to both number and list names in a pleasing format
name = input("\nPlease enter the 1st student's name you wish to calculate the grade for: ") # Provides setup for while loop, and receives first student's name
name_list = []      # Creates list to append names into, allows for selection of individuals later
name_grade_average_list = []        # Separate list to assure assigning the correct average grade for each student

if name == "":   # Ensures no traceback error when no first name is entered
    print("\nNo input registered, please restart the program")
    exit()

name = name[0].upper() + name[1:]   # Ensures the capitalization of the first letter in each name
name_list.append(name)              # Inserts the first name entered into the list of names

# While loop created to enter subsequent names
while name != " ":
    name = input(f"Please enter student number {count_for_name + 1}'s name, or press enter to stop entering names: ")
    if name == "":      # Exit out of while loop when done entering names
        break
    count_for_name += 1     # Increases counter for each name entered, simply for the sake of numbering students within the prompt
    name = name[0].upper() + name[1:]   # Capitalizes the first letter of each name entered
    name_list.append(name)              # Inserts each name entered into the list created previously

# These while and nested while loops go through the process of retrieving the teacher's chosen student, entering grades for them,
# Calculating the average, and inserting the name and average grade pair into a two dimensional list.
while cont:
    count_for_name = 1      # This counting system is mainly used for the listing of the students that comes afterwards, reseting itself after each loop
    print()
    for i in name_list:     # For loop prints out the list of student's names entered by the teacher
        print(f"{count_for_name}: {i}")
        count_for_name += 1 # Counter goes up through each iteration, ensuring correct number for each student
    try:                    # Try-Except used to ensure the input given by the teacher is a number
        name_choice = int(input(f"\nPlease enter the number of the student you'd like to enter grades for (Whole Numbers Only 1 - {len(name_list)}): "))
    except:
        print("\nYou've entered something that was not a number, please try again.\n")
        continue            # Returns to the beginning of the while loop
    if name_choice > len(name_list) or name_choice < 1:    # Prevents an input outside the number choices given, looping back to the beginning of the while
        print("\nYou've entered a number outside the number of students, please try again.\n")
        continue
# Extra confirmation to make sure the teacher chose the correct student, just in case.
    name_confirmation = input(f"You've entered {name_choice} ({name_list[name_choice - 1]}), is this correct?(Y/N): ")
    if name_confirmation.upper() == "N":    # Loops back to the beginning of the while
        continue
# This is the beginning of entering in grades for the chosen student.
    elif name_confirmation.upper() == "Y":
        print(f"\nPlease enter the grades for {name_list[name_choice - 1]} between or equal to 0 and 100. When complete, enter a -1 as the last \"grade\".")
# Grade count used to calculate the average grade for the student and ocunt the number of grades when prompting the teacher. Grade list used to gather
# Grades to be summed up and averaged at the end. Could use len(list) for average as well, count used for better readability. List is basically for fun here
        grade_count = 0
        grade_list = []
        while True:     # Nested while loop used to gather and calculate average of indeterminate number of grades for the chosen student
            try:        # Try-Except used to ensure the teacher enters a number. Float used in case of decimal grades.
                grade = float(input(f"Grade #{grade_count + 1}: ")) # +1 for proper numbering while entering grades
            except:
                print("\nPlease enter a numerical value for the grade.\n")
                continue
            if grade != -1:     # First checks for anything other than -1 (exit command), then ensures the number entered is between 0 and 100. If not, returns
                                # To the beginning of the nested while loop, staying on the grade that needs to be entered next.
                if grade < 0 or grade > 100:
                    print("Please enter a grade between or equal to 0 and 100.\n")
                    continue
                grade_list.append(grade)    # Adds the grade to the list of grades
                grade_count += 1            # Increases the numebr of grades entered by 1
            elif grade == -1:   # Checks if grade entered is -1 (exit command), then calculates the average grade and enters the [name,average] pair into
                                # The two dimensional list mentioned before. Because this is the last grade, breaks out of the nested while loop as well.
                                # -1 is also not entered in and calculated with the rest of the grades.
                grade_average = sum(grade_list) / grade_count
                name_grade_average_list.append([name_list[name_choice - 1], grade_average])
                break
    # Checks if the length of the two dimensional list is as long as the name list. This is to tell the program when the last student's average grade
    # Is calculated and entered, with the cont = False preventing another loop from happening, ending the grade entering process.
        if len(name_grade_average_list) == len(name_list):
            print("\nThank you for entering all of the student's grades. You will be given a table showing their average performance.")
            cont = False
        else:   # Informs the teacher which student's grade was entered, how many student's grades have been entered, and how many are left to enter.
            print(f"\nStudent number {len(name_grade_average_list)} ({name_list[name_choice - 1]}) entered, "
                  f"{len(name_list) - len(name_grade_average_list)} student(s) left to enter, please continue")
            continue
    else:   # Restarts this iteration of the loop should an input other than y or n be entered for the confirmation.
        print("\nYou've entered something other than Y or N, please restart this entry\n\n")
        continue

# Just to be extra fancy, asks the teacher whether they would like to sort by name or by grade. "lambda" used for a temporary function
# to sort by the second index within the two dimensional list. Contained in a while loop to catch any entries outside of name or grade
# and not restart the entire program.
while True:
    sort_method = input("\nWould you like to sort this table by name or by grade?(Enter \"Name\" or \"Grade\"): ")
    if sort_method.upper() == "NAME":
        name_grade_average_list.sort()
        break
    elif sort_method.upper() == "GRADE":
        name_grade_average_list.sort(key = lambda x: x[1], reverse = True) # Key uses lambda function to sort by grade, reverse being True
        break                                                              # To ensure highest grade at the top of table
    else:   # Ensures no error when something other than name or grade is entered. Returns to beginning of this while loop.
        print("Please enter \"Name\" or \"Grade\"")
        continue

# This is the end result table of each student, average grade, and letter grade. Formatted to look (hopefully) nice.
# For loop ensures that every student entered will be listed, and the two dimensional list allows for the paired
# Average grade to come out assigned to the correct student.
print("\nName of Student\t\tAverage Grade\t\tLetter Grade")
for student in name_grade_average_list:
    if student[1] > 90:
        print(f"{student[0]:^15s}\t\t\t{student[1]:.2f}\t\t\tA - Excellent")
    elif 90 > student[1] >= 80:
        print(f"{student[0]:^15s}\t\t\t{student[1]:.2f}\t\t\tB - Good")
    elif 80 > student[1] >= 70:
        print(f"{student[0]:^15s}\t\t\t{student[1]:^.2f}\t\t\tC - Satisfactory")
    elif 70 > student[1] >= 65:
        print(f"{student[0]:^15s}\t\t\t{student[1]:^.2f}\t\t\tD - Passing, Needs Work")
    elif 65 > student[1]:
        print(f"{student[0]:^15s}\t\t\t{student[1]:^.2f}\t\t\tF - Failing")