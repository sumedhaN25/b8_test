# E:\SUMEDHA_Learnings\CLASS\B8\b8_env\Scripts\activate.bat                #activate env

from django.db import models

# Create your models here.


class ActivePersons(models.Manager):          #custom model manager
    def get_queryset(self):
        return super().get_queryset().filter(is_active = True)


class InactivePerson(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active = False)


class Person(models.Model):   #table
    name = models.CharField(max_length= 200)
    age = models.IntegerField()
    mobile_num = models.IntegerField()
    address = models.CharField(max_length= 100)
    email = models.EmailField(null=True)
    date_joined = models.DateTimeField(auto_now= True, null= True)
    date_updated = models.DateTimeField(auto_now_add= True, null= True)
    is_active = models.BooleanField(default=True)
    actvprsns = ActivePersons()
    inactivep = InactivePerson()

    class Meta:
        db_table = "person"

    def __str__(self):
        # return self.name
        return f"{self.name} -- {self.address}" 


    def show_details(self):
        print(f"""Person Name = {self.name}
Person Age = {self.age}
Person Mobile = {self.mobile_num}
Person Address = {self.address}""")


    @classmethod
    def get_data_above_age(cls):
        return cls.objects.filter(age__gte = 25)              #gte = greater than equal to



    @classmethod
    def get_avg_age(cls):
        ''' average age of all persons'''
        data = cls.objects.all().values("id", "name", "age")
        lst = list(map(lambda x: x['age'], list(data)))
        return sum(lst)//len(lst)


    @classmethod
    def get_active_data(cls):
        return cls.objects.filter(is_active= True)  

    @classmethod
    def get_inactive_data(cls):
        return cls.objects.filter(is_active = False)

# ---------------------------------------------------------------------------------------------------------------

# RELATIONSHIP

class CommonClass(models.Model):
    name = models.CharField(max_length= 100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class College(CommonClass):
    adr = models.CharField(max_length=100)
    est_date = models.DateField(auto_now= True)

    class Meta:
        db_table = "college"


class Principal(CommonClass):
    exp = models.FloatField()
    qua = models.CharField(max_length= 100)
    college = models.OneToOneField(College, on_delete=models.CASCADE, related_name= "princi")

    class Meta:
        db_table = "principal"
    


class Department(CommonClass):
    dep_strn = models.IntegerField()
    college = models.ForeignKey(College, on_delete= models.CASCADE, related_name= "depts", null= True)

    class Meta:
        db_table = "department"



class Student(CommonClass):
    marks = models.IntegerField()
    age = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name= "studs", null = True)

    class Meta:
        db_table = "student"
    


class Subject(CommonClass):
    is_practical = models.BooleanField(default= False)
    student = models.ManyToManyField(Student, related_name= "subs" )
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name= "subs")


    class Meta:
        db_table = "sub"
    
#   ERD = > ENTITY RELATIONSHIP DIAGRAM
# --------------------------------------------------------------------------------------------------------




