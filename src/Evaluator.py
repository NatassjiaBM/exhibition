from rich.console import Console
from rich.table import Table
from rich import print
import sqlite3
from Jobs import Job
from Course import Course
sqliteConnection = sqlite3.connect(r"C:\Users\admin\Pessoal\Whitecliffe\codes\Natassjia\Presentation\DataBase.db")
cursor = sqliteConnection.cursor()


class Evaluator:
    sName = '' 
    evaluatorID = 0
    gender = ''
    courseID = 0 
    JobID = 0 
    age = 0 

    def __init__(self):
        self.sName = '' 
        self.evaluatorID = 0
        self.gender = ''
        self.courseID = 0 
        self.JobID = 0 
        self.age = 0

    
    def ask(self): 
        if self.evaluatorID == 0:
            print("Please, type your first and last name.")
            self.sName = input().lower()
            ssql = f"SELECT EvaluatorID, Name, Age, CourseID, Jobs, Gender from evaluator where '{self.sName}' = lower(Name)"
            #print(ssql)
            cursor = sqliteConnection.cursor()
            cursor.execute(ssql)
            row = cursor.fetchone()
            if row is None:
                print("Type your age:")
                self.age = input()
                while True: 
                    print("Type your gender using M for Male, F for Female, O for others")
                    answer = input()
                    if answer.lower() not in ('f', 'm', 'o'):
                        print(answer, "is not valid. Please type M/F/O")
                    else: 
                        self.gender = answer
                        break
                course = Course()
                canswer = course.courses()
                self.courseID = canswer
                job = Job()
                janswer = job.jobs()
                self.JobID = janswer

                self.evaluatorID = self.save()
                # TID = self.getID()
                # if TID >= 0: 
                #     self.evaluatorID = TID
                    
            else:
                self.evaluatorID = row[0]
                self.sName = row[1]
                self.age = row[2]
                self.courseID = row[3]
                self.JobID = row[4]
                self.gender = row[5]
            #No código global a informação esteja disponivel, utilizar o ID em outros lugares
            Evaluator.id = self.evaluatorID
                

    def save(self):
        ssql = f"INSERT INTO evaluator (Age, CourseID, Jobs, Gender, Name) values ({self.age}, {self.courseID}, {self.JobID}, '{self.gender}', '{self.sName}')"
        cursor = sqliteConnection.cursor()
        cursor.execute(ssql)
        sqliteConnection.commit()
        return cursor.lastrowid  

    def getID(self):
        ssql = f"SELECT EvaluatorID, Name, Age, CourseID, Jobs, Gender from evaluator where '{self.sName}' = lower(Name)"
        cursor = sqliteConnection.cursor()
        cursor.execute(ssql)
        row = cursor.fetchone()
        if row is not None:
            return row[0] #se ele trouxe algum dado, retorna o evaluator ID
        else:
            return -1 

