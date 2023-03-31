
# from app1.models import Person

# obj = Person.objects.all()
# print(list(obj))
# print(obj)
# print(obj.query)

# for Person in obj:
    # print(Person)
    # print(Person.__dict__)


# to get 1st record

# first_record = Person.objects.first()
# print(first_record)


#to get record by id

# obj = Person.objects.get(id = 4)
# print(obj)



# if id not exist

# try:
#     obj = Person.objects.get(id = 10)
#     print(obj)

# except Person.DoesNotExist:
#     print("Record Not Exist...!")


# to get multiple records by using filename

# objs = Person.objects.filter(age = 32, address= "Pune")
# print(objs)
# print(objs.query)


# to modify the existing data

# p1 = Person.objects.get(id = 3)
# print(p1.__dict__)
# print(p1.mobile_num)
# p1.mobile_num = 8888556648
# print(p1.__dict__)
# p1.save()

# to delete data
# p1 = Person.objects.get(id = 5)
# p1.delete()

# to save the data
# 1st way:

# p1 = Person(name = "omy", age = 33, mobile_num = 7894564410 ,address = "Mumbai")
# p1.save()


# 2nd way:

# Person.objects.create(name = "ranjana", age = 50, mobile_num = 7898521235, address = "Nagpur")

# print(dir(Person.objects))


# 3rd way: bulk create

# s1 = Person(name = "Anwit",    age = 20, mobile_num = 7894564222 ,address = "Hydrabad")
# s2 = Person(name = "Shrinika", age = 22, mobile_num = 7894564333 ,address = "Bangluru")
# s3 = Person(name = "Anika",    age = 25, mobile_num = 7894564444 ,address = "Kerala")
# s4 = Person(name = "Jiyansh",  age = 29, mobile_num = 7894564555 ,address = "Shimla")

# Person.objects.bulk_create([s1, s2, s3, s4])


# to count records

# print(Person.objects.count())

# to delete all records
# Person.objects.all().delete()

#to delete multiple records
# Person.objects.filter(age = 25).delete()

# print(Person.objects.filter(name__startswith = "a"))

# print(Person.objects.filter(name__endswith = "A"))

# print(Person.objects.exclude(name__startswith = "a"))

# print(Person.objects.filter(id = 9).exists())

# print(Person.objects.all().order_by("name"))               # record in asscending order by id

# print(Person.objects.all().order_by("-id"))             #record in descending order

# Person.objects.get(id = 1).show_details()             # calling from models.py

# for i in Person.objects.all():                # details for all
#     i.show_details()


# print(Person.get_data_above_age())



# ==================================================================================================================

# from django.contrib.auth import get_user_model
# User = get_user_model()
# print(User.objects.all())



#exec(open(r'E:\SUMEDHA_Learnings\CLASS\B8\B8_DJANGO\first_project\app1\db_shell.py').read())

# print(Person.objects.filter(name__contains = "n"))

# data = Person.objects.all().values()
# # print(data)

# for i in data:
#     print(i, type(i))


# data = Person.objects.all().values("id", "name", "address")
# for i in data:
#     print(i)

# data = Person.objects.all().values()
# lst= []
# for i in data:
#     lst.append(i["name"])
# print(lst)


# to print the average age

# data = Person.objects.all().values("id", "name", "age")        # values gives list of dictionaries
# lst = list(map(lambda X: X['age'], list(data)))
# print(sum(lst)//len(lst))               # avg age of all persons



# data = Person.objects.all().values_list("address")        # values_list gives list of tuples
# print(data)

# ============================================================================================================

# FOR MYSQL DATABASE


from app1.models import *
from django.contrib.auth.models import User


# User.objects.create_user(username="Anika", password="anika@123")


# data = Person.objects.filter(id__in=[2,4]).update(is_active = False)        # soft delete of records
# print(data)

# print(Person.objects.all())         #gives all data but we want only is_active = true data

# print(Person.objects.filter(is_active = True))             #gives only true data i.e 1,3,5 id

# print(Person.get_active_data())

# print(Person.get_inactive_data())

# print(Person.actvprsns.all())

# print(Person.inactivep.all())

# ------------------------------------------------------------------------------------------------------
# exec(open(r'E:\SUMEDHA_Learnings\CLASS\B8\B8_DJANGO\first_project\app1\db_shell.py').read())
# clgs = College.objects.all()
# prnc = Principal.objects.all()
# depts = Department.objects.all()
# studs = Student.objects.all()
# subs = Subject.objects.all()


# print(clgs)
# print(prnc)
# print(depts)
# print(studs)
# print(subs)


# for i in depts:
#     # print(i)
#     print(i.__dict__)             # printed info in dictionary form


# clg = clgs[0]
# print(clg)
# print(clg.principal)                   # for one to one relationship


# sume_obj = Principal.objects.first()          # FROM PRINCIPAL FETCH COLLEGE
# print(sume_obj.college)


# clgs = College.objects.all()
# clg = clgs[0]
# # print(dir(clg))

# print(clg.department_set.all())                # one to many relation (fetching department from clg)


# dept = Department.objects.first()                     # many to one relation (fetching clg from department)
# print(dept.college)



# print(dept.student_set.all())                       # fetch student from department

# get all students department wise

# all_depts = Department.objects.all()                                # many to many relation
# for dept in all_depts:
#     print(f"DEPARTMENT = {dept.name}, STUDENT = {list(dept.student_set.all())}")


#   IN DICTIONARY FORMAT

# all_depts = Department.objects.all()
# d = {}
# for dept in all_depts:
#     d[dept.name]= list(dept.student_set.all())
# print(d)

# s1 = Student.objects.first()                     # fetch department from students
# print(s1.department)

# s1 = Student.objects.get(name = "Arin")
# print(s1.department)


# studs = Student.objects.all()
# stud_dict = {}
# for stud in studs:
#     stud_dict[stud.name] = stud.department

# print(stud_dict)


# clg = College.objects.get(id = 1)                   # after adding related_name in models.py
# print(clg.depts.all())

# dept = Department.objects.first()
# print(dept.studs.all())
  

# dept = Department.objects.get(id = 2)
# # print(dept)
# print(dept.subs.all())

# depts = Department.objects.all()
# for dept in depts:
#     print(dept.subs.all())


# print([list(dept.subs.all()) for dept in Department.objects.all()])                 #list comprehension

# clg = College.objects.get(id = 1)
# # print(clg)
# print(clg.depts.all()[1].studs.all())              # all students from IT... ie   arin, vedant, neha

# print(clg.depts.all()[1].studs.all()[2])


# clg = College.objects.get(id = 1)
# for i in clg.depts.all():
#     # print(i)     #department
#     print(i.studs.all())


# clg = College.objects.get(id= 1)
# std_lst = []
# for i in clg.depts.all():
#     std_lst.extend(i.studs.all())
# print(std_lst)


# s1 = Student.objects.get(id = 7)
# print(s1.department.college)
# print(s1.department.college.est_date)
# -------------------------------------------------------------------------------------------------------------------------------
# exec(open(r'E:\SUMEDHA_Learnings\CLASS\B8\B8_DJANGO\first_project\app1\db_shell.py').read())

# ADDITION
# create college......................

# College.objects.create(name = "NIT", adr = "Nagpur")       # created at mysql workbench

# add Principal........................1st way

# c1 = College.objects.get(id = 3)                              # by passing college instance/object
# p1 = Principal.objects.create(name = "Apurv", exp = 15, qua = "PHD", college = c1)
# p1.save()

# 2nd way

# By passing college Id

# p1 = Principal.objects.create(name = "Pragati", exp = 20, qua = "PHD", college_id = 2)
# p1.save()

# CREATE DEPARTMENT

# c1 = College.objects.get(id = 3)  
# Department.objects.create(name ="Chemical", dep_strn = 80, college = c1)                      

# CREATE STUDENTS

# Student.objects.create(name = "S", marks = 85, age = 17)
# Student.objects.create(name = "A", marks = 85, age = 18)
# Student.objects.create(name = "M", marks = 85, age = 19)


# FETCH THE STUDENTS
# s1, s2, s3 = Student.objects.filter(id__gt = 9)
# for i in s1, s2, s3:
#     print(i)
# print(s1, s2, s3)

# ADD DEPARTMENT ID IN STUDENT

# s1, s2, s3 = Student.objects.filter(id__gt = 9)
# Chem_dep = Department.objects.get(id = 3)
# Chem_dep.studs.add(s1,s2,s3)


# ADD SUBJECTS

# d1 = Department.objects.get(id = 3)
# Subject.objects.create(name = "Chemistry", is_practical = True, department = d1)

# -----------------------------------------------------------------------------------------------------------------------------------
#exec(open(r'E:\SUMEDHA_Learnings\CLASS\B8\B8_DJANGO\first_project\app1\db_shell.py').read())


# studs = Student.objects.all()
# print(studs)

# studs = Student.objects.all()[0]
# print(studs)


# studs = Student.objects.all()[0:7]
# print(studs)

##### select_related:

# studs = Student.objects.all()
# for i in studs:
#     print(i.department)


# studs = Student.objects.select_related("department")
# for i in studs:
#     print(i.department)


# MANY TO MANY RELATION:=============================================

# s1 = Subject.objects.get(name = "PYTHON")
# print(s1.student.all())
# s2 = Subject.objects.get(name = "OOPS")
# print(s2.student.all())

# s3 = Subject.objects.get(name = "DBMS")
# print(s3.student.all())


# st1 = Student.objects.get(name = "Arin")
# st2 = Student.objects.get(name = "Neha")
# st3 = Student.objects.get(name = "S")
# st4 = Student.objects.get(name = "A")
# st5 = Student.objects.get(name = "M")

# s2.student.add(st3, st4, st5)
# print(s2.student.all())

# s1.student.add(st2, st3, st4)
# print(s1.student.all())

# print(st4.subject_set.all())
# print(st3.subject_set.all())
# print(st2.subject_set.all())
# print(st1.subject_set.all())
# print(st5.subject_set.all())

# print(Subject.objects.filter(student__name__startswith= "Neha"))


# print(Student.objects.filter(subject__name__startswith= "P"))


# print(Student.objects.filter(department__name__startswith = "I"))                #fetch stud from depat

# print(Student.objects.filter(department__college__id = 1))                     # fetch stud from clg

# --------------------------------------------------------------------------------------------------------------

# exec(open(r'E:\SUMEDHA_Learnings\CLASS\B8\B8_DJANGO\first_project\app1\db_shell.py').read())
# RAW SQL QUERY: 1st way

# from django.db import connection
# cursor = connection.cursor()
# cursor.execute('''SELECT * FROM student''')   # hit sql query not orm query 
# # data = cursor.fetchall()
# data = cursor.fetchmany(3)                # printed 1st three records
# print(data)
# data = cursor.fetchmany(5)                # printed after 3rd record ie 4,5,6,7,8
# print(data)

# 2nd way:

# data = Student.objects.raw('SELECT * FROM student')
# for i in data:
#     print(i)

# MULTIPLE DATABASES OPERATIONS      # MySQL and SQLite3

# data = Student.objects.all()                   # uses default database
# print(data)

# Second_Database = "second_db"
# data = Student.objects.using(Second_Database).all()
# print(data)


# c1 = College.objects.using(Second_Database).create(name = "COEP",adr = "PUNE")
# d1 = Department.objects.using(Second_Database).create(name = "Civil",dep_strn = 50, college = c1)
# s1 = Student.objects.using(Second_Database).create(name = "Adhira",marks = 87, age = 24, department = d1)
# s2 = Student.objects.using(Second_Database).create(name = "Abhira",marks = 99, age = 25, department= d1)
# sub1 = Subject.objects.using(Second_Database).create(name = "physics", is_practical = True, department = d1)

# c1 = College.objects.using(Second_Database).get(id = 15)
# c1.delete()

# s1 = Student.objects.using(Second_Database).get(id = 6)
# s1.delete()
