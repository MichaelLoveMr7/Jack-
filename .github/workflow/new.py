# part of the code is changed from youtube video:https://www.youtube.com/watch?v=igvwOW4uf54&t=31s
# The data.csv contains 670, 000 or more passwords.
import sys, math, re

def check_password_length(password):
    length = len(str(password))
    
    global password_length_good
    if type(password) == float:
        pass
    
    if length > 8:                          #long password is better than smaller one
       
        password_length_good = False
    
    else:
        
        password_length_good = True
    

def check_password_uppercase(password):
    global UpperLength
    
    UpperLength = len(re.findall(r'[A-Z]',str (password)))# problem here
    
  
def check_password_numbers(password):
    global digits
    digits = len(re.findall(r'[0-9]', str(password)))
    
   
        
def check_common_passwords(password):
    global matchedPass 
    matchedPass = False
    #Most common linked passwords as of 2012 from statista
    commonPasswords = ['password','linkedin','sunshine','qwerty','123456','123456789'
                       '12345678','111111','1234567','654321']
    for commonPass in commonPasswords:
        if commonPass == password:
            matchedPass = True


def password_eval(password, password_length_good, UpperLength, digits, matchedPass):
    print('\n[*] Password Evaluation: ')
    judge = 0
    
    if matchedPass == True:
        judge = 9
        print('careless and lazy customers')
    elif password_length_good == True and UpperLength >= 3 and digits >=3 and matchedPass == False:
        judge = 1
        print('careful customers')
    
    elif password_length_good == True and UpperLength <= 3 and digits >= 3 and matchedPass == False:
        judge = 2
        print('digit-liked customers')
        
    elif password_length_good == True and UpperLength >= 3 and digits <= 3 and matchedPass == False:
        judge = 3
        print('Upper-case obese customers')
        
    elif password_length_good == True and UpperLength <= 3 and digits <= 3 and matchedPass == False:
        judge = 4
        print('abnormal and long-liked customers')
        
    elif password_length_good == False and UpperLength >= 3 and digits >= 3 and matchedPass == False:
        judge = 5
        print('condensed and short-like customers')
        
    elif password_length_good == False and UpperLength <= 3 and digits >= 3 and matchedPass == False:
        judge = 6
        print('digit-liked and short customers')
        
    elif password_length_good == False and UpperLength >= 3 and digits <= 3 and matchedPass == False:
        judge = 7
        print('Uppercase-liked and short customers')
    
    elif password_length_good == False and UpperLength <= 3 and digits <=3 and matchedPass == False:
        judge = 8
        print('Abnormal and short  customers')
        
    print(judge)
    return judge

def file_len(fname):             #94-98 stackflow
    with open(fname) as f:
        for i,l in enumerate(f):
            pass
    return i + 1


import numpy as np
import pandas as pd
import random
import re
import os
from numpy import genfromtxt
count = file_len("data.csv")
pswd_data = pd.read_table("data.csv", error_bad_lines = False)#error_bad_lines = False,
pswd_data.dropna(inplace = True)
with open("data.csv", 'r') as f:
    lines = f.read().splitlines()
    last_line = lines[-1]
    print (last_line)

sequence = 0
customer1 = 0
customer2 = 0
customer3 = 0
customer4 = 0
customer5 = 0
customer6 = 0
customer7 = 0
customer8 = 0
customer9 = 0
array = []
while sequence != count-1:
    password = pswd_data.iloc[sequence, 0]
    check_password_length(password)
    check_password_uppercase(password)
    check_password_numbers(password)
    check_common_passwords(password)
    i=password_eval(password, password_length_good, UpperLength, digits, matchedPass)
    
    if i == 1:
        customer1 = customer1 + 1
    elif i == 2:
        customer2 = customer2 + 1
    elif i == 3:
        customer3 = customer3 + 1
    elif i == 4:
        customer4 = customer4 + 1
    elif i == 5:
        customer5 = customer5 + 1
    elif i == 6:
        customer6 = customer6 + 1
    elif i == 7:
        customer7 = customer7 + 1
    elif i == 8:
        customer8 = customer8 + 1
    elif i == 9:
        customer9 = customer9 + 1
        
    sequence = sequence + 1
'''
#These data for conveniently further testing the diagram generated below
a = pswd_data.iloc[669878,0]
print(a)

customer1 = 490
customer2 = 27092
customer3 = 284
customer4 = 12173
customer5 = 60056
customer6 = 461597
customer7 = 13218
customer8 = 94969
customer9 = 0
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from astropy.visualization import hist

customer = [customer1,customer2, customer3, customer4,customer5,customer6, customer7, customer8,customer9]

def makeArrays(customer):
    arrays = []
    arrays.append(("percentage", "kind"))
    a = 0
    for i in customer:
        a = a + 1
        arrays.append((i, a))
        
    return arrays


array = makeArrays(customer)
array = pd.DataFrame(array)

y = array.iloc[1: ,0] #good plt
x = array.iloc[1: ,1]

import matplotlib.pyplot as plt #for conveniently run the cell from line 156 to the last line, import here

plt.plot(x, y, label='1 to 9 Cusomters')
plt.xlabel('kind')
plt.ylabel('people number')
plt.title('classifier users by passwords ')
plt.legend()
plt.axis([1,10,0,700000])
plt.show()
print("customer1: careful customers, ",customer1)
print("customer2: digit-liked customers, ",customer2)
print("customer3: Upper-case obese customers, ",customer3)
print("customer4: abnormal and long-liked customers, ",customer4)
print("customer5: condensed and short-like customers, ",customer5)
print("customer6: digit-liked and short customers, ",customer6)
print("customer7: Uppercase-liked and short customers, ",customer7)
print("customer8: Abnormal and short  customers, ",customer8)
print("customer9: careless and lazy customers, ",customer9)


y1 = array.iloc[1: 6,0].tolist()
x1 = array.iloc[1: 6,1].tolist()
plt.bar(x1, y1, label = '1,2,3,4,5 customers')
plt.xlabel('kind')
plt.ylabel('people number')
plt.title('classifier users by passwords ')
plt.legend()
plt.axis([1,6,0,700000])
plt.show()           
print("customer1: careful customers, ",customer1)
print("customer2: digit-liked customers, ",customer2)
print("customer3: Upper-case obese customers, ",customer3)
print("customer4: abnormal and long-liked customers, ",customer4)
print("customer5: condensed and short-like customers, ",customer5)

y2 = array.iloc[6: 10, 0].tolist()
x2 = array.iloc[6: 10, 1].tolist()

plt.bar(x2, y2, label = '6,7,8,9 customers')

plt.xlabel('kind')
plt.ylabel('people number')
plt.title('classifier users by passwords ')
plt.legend()
plt.axis([6,11,0,700000])
plt.show() 

print("customer6: digit-liked and short customers, ",customer6)
print("customer7: Uppercase-liked and short customers, ",customer7)
print("customer8: Abnormal and short  customers, ",customer8)
print("customer9: careless and lazy customers, ",customer9)
