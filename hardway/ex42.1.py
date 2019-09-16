#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
class Person(object):
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age
 
class Student(Person):
    def __init__(self,name,gender,age,school,score):
        #super(Student,self).__init__(name,gender,age)
        self.name = name.upper()  # 例如这样，父类对name和gender的初始化只是简单的赋值，但子类要求字母全部大写。
        #self.gender = gender.upper()
        self.school = school
        self.score = score
 
s = Student('Alice','female',18,'Middle school',87)
print (s.school)
print (s.name)