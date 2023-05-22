reg_number = input("Enter Registration Number: ")
m1, m2, m3 = map(int, input("Enter Grades: ").split())
avg = (m1 + m2 + m3)/3
print("Registration Number: {} \nAverage Grades: {} ".format(reg_number, avg))
