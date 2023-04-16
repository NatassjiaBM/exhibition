#Importing the DataBase

import pyodbc
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\admin\Pessoal\Whitecliffe\codes\Natassjia\Presentation\WhitecliffePresentation.accdb;')
import matplotlib.pyplot as plt  #Importing the Dash functions 
# import numpy as np
import typer 
from rich import print

class Person():
#Defing the menu for the author 
    def author():
        print('Please, type or name')
        authorname = input()
        ssql = f"Select * from Author where '{authorname}' = AuthorName"
        cursor = conn.cursor()
        cursor.execute(ssql)
        row = cursor.fetchone()
        if row is None:
            print("We were unable to find your profile.")
            return 0 #False
        else:
            #Row = dessa linha pegue essa .coluna
            authorname = row.AuthorName
            return 1 #True

 #Defining the menu for the evaluator    
    def evaluator():
        print('Welcome to our Tech presentation. Please provide some information to our report.')
        print('Please select your gender')
        Gender = input()
        FindGender = f"Update Person set Gender = '{Gender}'"
        cursor = conn.cursor()
        cursor.execute(FindGender)
        conn.commit()
        print('Please type your age.')
        Age = input()
        AddAge = f"Update Person set Age = '{Age}'"
        cursor = conn.cursor()
        cursor.execute(AddAge)
        conn.commit()
        #print('Select your course')

def menu():
    print("Welcome to the Tech Presentation. Are you a Evaluator or a Project Author? Type 1 for Evaluator or 2 for Project Author.")
    answer = input()
    if answer == "1":
        Person(evaluator)
        #evaluator()
    elif answer.lower == '2':
        author()
    else:
        print("I don't recognize this answer. Please type 1 or 2")
        menu()



def __main__():
    menu()
    typer.run()

__main__()