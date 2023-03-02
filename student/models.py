from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=500)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = 'student'


# {
# "student_name" : "blah",
# "age" : 12,
# "gender" : "Male",
# "email" : "blah@gmail.com",
# "phone" : 12345678,
# "user_name" : "blah",
# "password" : "123456"
# }
