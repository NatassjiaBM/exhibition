import rich 
from rich import print
from rich.table import Table
from rich.console import Console
import sqlite3
from favAspects import FavourtiteAspects
from Project import Projects
from Evaluator import Evaluator

sqliteConnection = sqlite3.connect(r"C:\Users\admin\Pessoal\Whitecliffe\codes\Natassjia\Presentation\DataBase.db")
cursor = sqliteConnection.cursor()

aspecttable = Table(title ="[bold magenta]Favourite Aspects[/bold magenta]")

class EvalByProject:

    evaluatorID = 0 
    projectID = 0
    evalprojectID = 0
    favAspectID = 0 
    visitAgain = 0
    feedBack = ""

    def __init__(self): 
        self.evaluatorID = 0 
        self.projectID = 0
        self.evalprojectID = 0
        self.favAspectID = 0 
        self.visitAgain = 0
        self.feedBack = ""


    def main(self):
        project = Projects()
        panswer = project.project()
        self.projectID = panswer

        favaspect = FavourtiteAspects()
        fanswer = favaspect.aspects()
        self.favAspectID = fanswer
        while True: 
            print("Would you come to future exibitions? Type 1 for YES or 2 for NO.")
            visitAnswer = input()
            if visitAnswer not in ("1", "2"):
                print(visitAnswer, "is not valid. Please type 1 or 2")
            else: 
                self.visitAgain = visitAnswer
                break
        while True:
            print("Would you like to give us a feedback? Type 1 for YES or 2 for NO")
            answer = input()
            if answer == '1':
                self.feedback()
                break
            elif answer == '2':
                print("Thank you for coming. Please check the dashboard before leaving")
                break
            else: 
                print(answer, "is not recognized. Please type 1 or 2.")
        # row = cursor.fetchone() #Não esta encontrando nada
        # print(row)

        self.save()
        #como interligar o id da pessoa com o daqui?
        # self.evaluatorID = row[0]
        # self.projectID = row[1]
        # self.evalprojectID = row[2]
        # self.favAspectID = row[3]
        # self.visitAgain = row[4]
        # self.feedBack = row[5]

    def save(self):
        ssql = f"INSERT INTO EvalbyProject(EvaluatorID, ProjectID, FavAspectID, VisitAgain, Feedback) values({Evaluator.id}, {self.projectID}, {self.favAspectID}, {self.visitAgain}, '{self.feedBack}')"
        cursor = sqliteConnection.cursor()
        cursor.execute(ssql)
        sqliteConnection.commit()


    def feedback(self):
        print("Please type your feedback.")
        answer = input()
        self.feedBack = answer

            






        # def fav_aspects(self): 
        #     aspecttable.add_column("ID", justify="right", style="cyan", no_wrap=True)
        #     aspecttable.add_column("Fav. Aspect", justify="right", style="green")

        #     ssql = f"Select * from FavAspect"
        #     cursor = sqliteConnection.cursor()
        #     cursor.execute(ssql)
        #     rows = cursor.fetchall()
        #     for row in rows:
        #         aspecttable.add_row(str(row[0]), row[1])
        #     console = Console()
        #     console.print(aspecttable)

        #     print("Select your favorite aspects of the presentation")
        #     self.favAspectID = input() 
        #     while True: 
        #         print("Would you come to future exibitions? Type 1 for YES or 2 for NO.")
        #         visitAnswer = input()
        #         if visitAnswer() not in ('1', '2'):
        #             print(visitAnswer, "is not valid. Please type 1 or 2")
        #         else: 
        #             self.visitAgain = visitAnswer
        #             break
        #     print("")
                      
            # favAspects = f"Insert into EvalbyProject(FavAspectID) values ('{answer}')"
            # where '{evaluatorID}' = evaluatorID)"
            # cursor = sqliteConnection.cursor()
            # cursor.execute(favAspects)
            # sqliteConnection.commit() 

    # def visitAgain():
    #     answer = input()
    #     visitagain = f"Insert into EvalbyProject(VisitAgain) values ('{answer}')"
    #     cursor = sqliteConnection.cursor()
    #     cursor.execute(visitagain)
    #     sqliteConnection.commit()  


    # def feedback():
    #     feedback = input()
    #     ssql = f"Insert into EvalbyProject(Feedback) values ('{feedback}')"
    #     cursor = sqliteConnection.cursor()
    #     cursor.execute(ssql)
    #     sqliteConnection.commit()  
    #     print("[bold green]Alright! Thank you for being here. Please check our Dashboard before leaving.[/bold green] :red_heart:")
    #     exit()