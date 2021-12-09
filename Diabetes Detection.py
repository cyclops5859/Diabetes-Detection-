# Created by Cyclops!
import time

print ("Welcome, here You can check your Diabetes Level.")
time.sleep(1)
print ("")

print ("What unit would you like to use?")

print ("\n1.0. mg/dL")
print ("2.0. mmol/L")

print ("")

op = eval(input("What Unit would you like to choose : "))

print ("")

if op == 1.0:
    print (">>> mg/dL Unit <<<")

    print ("")

    print ("Please choose an option.")

    print ("\n1. After meal")

    print ("2. 2 - 3 Hours after meal")

    print ("3. Fassting")

    print ("4. Enter anything to Exit")
    print (" ")
    x = eval(input("Please enter an option: "))

    if x == 1:
        d = eval(input("What is your Blood Glucose Level?: "))
        if d >= 170 and d <= 189:
            print ('Your Normal !')
        elif d <=169:
            print ("It's too low! have some thing sweet.")
        elif d > 190 and d <= 219:
            print ("You are prediabetic / Borderline diabetic !' Please take care.")
        elif d > 220 and d <= 300:
            print ("You are Diabetic !' Please take care.")
        elif d > 300:
            print ("You are highly Diabetic Immediate Insulin prescribed!")
#-----------------------------------------------------------------------------------------------------
    if x == 2:
        d = eval(input("What is your Blood Glucose Level?: "))
        if d >= 120 and d <= 140:
            print ('Your Normal !')
        elif d <=119:
            print ("It's too low! have some thing sweet.")
        elif d > 141 and d <= 199:
            print ("You are prediabetic / Borderline diabetic !' Please take care.")
        elif d == 200:
            print ("You are Diabetic !' Please take care.")
        elif d > 201:
            print ("You are highly Diabetic Immediate Insulin prescribed!")
#-----------------------------------------------------------------------------------------------------
    if x == 3:
        d = eval(input("What is your Blood Glucose Level?: "))
        if d >= 80 and d <= 100:
            print ('Your Normal !')
        elif d <=79:
            print ("It's too low! have some thing sweet.")
        elif d > 101 and d <= 125:
            print ("You are prediabetic / Borderline diabetic !' Please take care.")
        elif d == 126:
            print ("You are Diabetic !' Please take care.")
        elif d > 127:
            print ("You are highly Diabetic Immediate Insulin prescribed!")
#-----------------------------------------------------------------------------------------------------        
#-----------------------------------------------------------------------------------------------------
if op == 2.0:
    print (">>> mmol/L Unit <<<")

    print ("")

    print ("Please choose an option.")

    print ("\n1. After meal")

    print ("2. 2 - 3 Hours after meal")

    print ("3. Fassting")

    print ("4. Enter anything to Exit")
    print (" ")
    x = eval(input("Please enter an option: "))

    if x == 1:
        d = eval(input("What is your Blood Glucose Level?: "))
        if d >= 9.4 and d <= 10.5:
            print ('Your Normal !')
        elif d <=9.3:
            print ("It's too low! have some thing sweet.")
        elif d > 10.6 and d <= 12.2:
            print ("You are prediabetic / Borderline diabetic !' Please take care.")
        elif d > 12.3 and d <= 16.7:
            print ("You are Diabetic !' Please take care.")
        elif d > 16.7:
            print ("You are highly Diabetic Immediate Insulin prescribed!")
#-----------------------------------------------------------------------------------------------------
    if x == 2:
        d = eval(input("What is your Blood Glucose Level?: "))
        if d >= 6.7 and d <= 7.8:
            print ('Your Normal !')
        elif d <= 6.6:
            print ("It's too low! have some thing sweet.")
        elif d > 7.8 and d <= 11.1:
            print ("You are prediabetic / Borderline diabetic !' Please take care.")
        elif d == 11.1:
            print ("You are Diabetic !' Please take care.")
        elif d > 11.2:
            print ("You are highly Diabetic Immediate Insulin prescribed!")
#-----------------------------------------------------------------------------------------------------
    if x == 3:
        d = eval(input("What is your Blood Glucose Level?: "))
        if d >= 4.4 and d <= 5.6:
            print ('Your Normal !')
        elif d <=4.4:
            print ("It's too low! have some thing sweet.")
        elif d > 5.6 and d <= 6.9:
            print ("You are prediabetic / Borderline diabetic !' Please take care.")
        elif d == 7.0:
            print ("You are Diabetic !' Please take care.")
        elif d > 7.1:
            print ("You are highly Diabetic Immediate Insulin prescribed!")

