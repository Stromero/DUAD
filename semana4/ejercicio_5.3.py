number_of_grades = int(input('Enter the number of grades: '))

print('Number of grades:', number_of_grades)

counter = 0
approved_count = 0
failed_count = 0
total_sum = 0
approved_sum = 0
failed_sum = 0

while counter < number_of_grades:
    student_grade = int(input('Enter the student grade: '))
    
    if student_grade >= 70:
        approved_count = approved_count + 1
        approved_sum = approved_sum + student_grade
    else:
        failed_count = failed_count + 1
        failed_sum = failed_sum + student_grade

    counter = counter + 1
    total_sum = total_sum + student_grade

# General average
final_average = total_sum / number_of_grades

# Approved average (avoid division by zero)
if approved_count > 0:
    approved_average = approved_sum / approved_count
else:
    approved_average = 0

# Failed average (avoid division by zero)
if failed_count > 0:
    failed_average = failed_sum / failed_count
else:
    failed_average = 0

print("Number of grades entered:", number_of_grades, "\n",
      "Number of approved grades:", approved_count, "\n",
      "Number of failed grades:", failed_count, "\n",
      "Overall average:", final_average, "\n",
      "Approved grades average:", "%.2f" % approved_average, "\n",
      "Failed grades average:", "%.2f" % failed_average
      )