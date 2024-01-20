basic = float(input("Enter Ayush basic salary: "))
hra = basic * 0.12
da = basic * 0.4
pf = (basic + da) * 0.1
net_salary = basic + hra + da - 2 * pf
