#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 19:03:05 2018

@author: slytherin
"""

import pandas as pd

data=pd.read_csv("dataset.csv")
attrition=pd.get_dummies(data.Attrition)
attrition=attrition.drop('Yes',axis=1)
data=data.drop('Attrition',axis=1)
data=data.join(attrition)
travel=pd.get_dummies(data.BusinessTravel)
travel=travel.drop('Travel_Rarely',axis=1)
data=data.drop('BusinessTravel',axis=1)
data=data.join(travel)
department=pd.get_dummies(data.Department)
department=department.drop('Sales',axis=1)
data=data.drop('Department',axis=1)
data=data.join(department)
edu=pd.get_dummies(data.EducationField)
edu=edu.drop('Human Resources',axis=1)
data=data.drop('EducationField',axis=1)
data=data.join(edu)
gender=pd.get_dummies(data.Gender)
gender=gender.drop('Female',axis=1)
data=data.drop('Gender',axis=1)
data=data.join(gender)
data.Age=data.Age.astype('category')
data.Age=data.Age.cat.reorder_categories(['junior','senior'])
#data.Age=data.Age.cat.codes
print(data.head())