# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 21:18:47 2022

@author: umita
"""
from datetime import date
today = date.today()

def menu():
    print("Menu \n1.Today to-do list \n2.Add to-do list of today \n3.History \n4.Quotation of the day \n5.Add daily \n0.Exit")
    
    try:
        decision = int(input("\nWhat do you want to do : "))
    except:
        print("Only Integer values!\n\n\n")
        menu()
        
    if isinstance(decision, int) == True:
    
        if decision == 1: today_to_do_list()
        elif decision == 2: add_to_do_list_of_today()
        elif decision == 3: history()
        elif decision == 4: quotation_of_the_day()
        elif decision == 5: add_daily()
        elif decision == 0: breakpoint;
        else: 
            print("There is no choice!\n\n\n")
            menu()
            
    else: 
        print("Not valid choice! \n\n")
        menu()
        
def today_to_do_list():
    
    file = open("to-dos.txt", 'r')
    lines = file.readlines()
    
    for i in lines:
        if str(today) in i:
            print(i)
    print("\n\n\n")
    menu()
    
def add_to_do_list_of_today():
    try:
        how_many_times = int(input("\nHow many things will you do today: "))
    except:
        print("Only Integer values!\n\n\n")
        today_to_do_list()
        
    to_do_s = []
    
    for i in range(0, how_many_times):
        input_text = str(i + 1) + ") "
        to_do_s.insert(0, input(input_text))
    to_do_s_dict = {
        str(today) : str(to_do_s)
        }
   
    read_file = open('to-dos.txt', 'r')
    
    if str(today) not in read_file.read():
        file = open('to-dos.txt', 'a')
        text = str(to_do_s_dict) + '\n'
        file.write(text)
        file.close()
        print("Your to-dos added. Loading main menu...\n\n\n")
        menu()
    else: 
        print("It has already written! loading main menu...\n\n\n")
        menu()
        
    read_file.close()
    
def history():
    
    file = open("to-dos.txt", 'r')
    lines = file.readlines()
    
    for i in lines:  
     print(i)
    print("\n\n\n")
    menu()
    
def quotation_of_the_day():
    from requests import get
    from json import loads

    response = get('http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')
    print('{quoteText} - {quoteAuthor}'.format(**loads(response.text)))
    print("\n\n\n")
    menu()
    
def add_daily():
 try:
    content1 = input(">> ")
    content = str(today)+" : " + content1 + '\n'
    file = open("daily.txt", "a")
    file.write(content)
    file.close()
 except:
     print("Eklenemedi!")
 menu()
menu()