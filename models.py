from django.db import models

# Create your models here.
# SQL :
# CREATE TABLE Person (
#     id int,
#     name varchar(50),
#     age int NOT NULL,
#     gender varchar(10)
# );

class Person(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return '{name} {age} {gender}'.format(name = self.name, age = self.age, gender = self.gender)