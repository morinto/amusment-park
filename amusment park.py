# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
BOLD = '\033[1m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'

age=int(input(f"{BOLD}{BLUE}please input your Age: "  ))
bill=0
if age > 5 and age < 50:
    if age < 10:
        bill = 1000
        print (f"{BOLD}{BLUE}your bill is {bill} naira")
    elif age < 25:
        bill = 2000
        print (f"{BOLD}{BLUE}your bill is {bill} naira")
    else:
        bill = 2500
        print (f"{BOLD}{BLUE}your bill is {bill} naira")
    bills=input(f"{BOLD}{BLUE}do u love want to snap pic yes/no:  "   )
    if bills == "yes":
        print(f"{BOLD}{YELLOW}16 picture is 800 naira")
        print(f"{BOLD}{YELLOW}8 picure is 600 naira")
        print(f"{BOLD}{YELLOW}4 picture is 400 naira")
        print(f"{BOLD}{YELLOW}2 picture is 300 naira")
        a=input("select either 16,8,4 or 2 picture ")
        while a !="16" and a !="8" and a !="4" and a!="2":
            print(f"{BOLD}{YELLOW}please  select eiher 16,8,4 and 2")
            a=input()
        if a=="16":
            bill +=800
            print(f"{BOLD}{BLUE}your total bill is {bill} naira")
          
        elif a=="8":
           bill +=600
           print(f"{BOLD}{BLUE}your total bill is {bill} naira")
        elif a=="4":
           bill+=400
           print(f"{BOLD}{BLUE}your total bill is {bill} naira")
        elif a=="2":
          bill+=300
          print(f"{BOLD}{BLUE}your total bill is {bill} naira")
        else:
           print("unrecongnise selection")
    else:
        print(f"{BOLD}{BLUE}your total bill is {bill} naira")
    print (f"{BOLD}{GREEN}select payment plan")
    print(f"{BOLD}{GREEN}cash"  " " "Or"     " card")
    p=input()
    if p=="card":
        print(f"{BOLD}{YELLOW}slot in your card")
        z=input(f"{BOLD}{YELLOW}type either yes or no to continue the transaction  ")
        if z== "yes":
              print(f"{BOLD}{RED}transaction process")
              print(f"{BOLD}{BLUE}enjoy your ride at our amusement park")
        else:
             print("transaction aborted")
    else:
        print(f"{BOLD}{BLUE}please pay your cash to the cashier at the park")
        
        
else:
    print(f"{BOLD}{RED}you are not qualify")
        
    
    
    

        