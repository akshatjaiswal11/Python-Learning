r=["Roll no.", "Enrollment no.", "Name", "Course", "Semester"]

s=[[  1,  "E001",   "John Doe",  "Computer Science", 1],
[  2,  "E002",   "Jane Smith",  "Electrical Engineering", 1],
[  3,  "E003",   "Alice Johnson",  "Mechanical Engineering", 2],]

import csv

f=open("11.csv","w",newline="\n")
w=csv.writer(f,delimiter=",")

w.writerow(r)
w.writerows(s)
f.close()