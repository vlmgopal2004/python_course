# ===*=== Hyderabad Metro Employee Details ===*===
emp_id = int(input("Enter Employee ID: "))
emp_name = input("Enter Employee Name: ")
emp_con_no = int(input("Enter Employee Contact No: "))
emp_skills = input("Enter Employee Skills: ").split(',')
emp_salary = float(input("Enter Employee Salary: "))
no_of_work_days = int(input("Enter No of Working Days(per month): "))
no_of_weekoff = int(input("Enter No of WeekOffs(per month): "))
work_schedule = (no_of_work_days, no_of_weekoff)
yearly_hike = float(input("Enter Yearly Hike Percentage: "))
employement_categories = set(input("Enter Different Departments in Hyderabad Metro: ").split(','))
emp_department = input("Enter Employee Working Department: ")
emp_work_loc = input("Enter Employee Work Location: ")
emp_type = input("Enter Employee Type(Full-Time/Part-Time/Intern): ")
position_info = {
    'department' : emp_department,
    'work_loc' : emp_work_loc,
    'emp_type' : emp_type
}

#output section
print('\nOutput:\n')
#Using Comma Separation (sep=',')
print("Employee ID, Employee Name, Salary: "+ str(emp_id), emp_name, emp_salary, sep=',')
#Using Percentage Formatting (% operator)
print("Yearly Hike Percentage: %.2f%%" % yearly_hike)
#Using f-strings (f"")
print(f"Employee Name: {emp_name} \nEmployee Contact No: {emp_con_no} \nEmployee Salary: ₹{emp_salary} \nYearly Hike Persentage: {yearly_hike}%")
#Using .format() method
print("Position Info: Employee Department - {}, Employee Work Location - {}, Employee Type - {}".format(position_info["department"], position_info["work_loc"], position_info["emp_type"]))

