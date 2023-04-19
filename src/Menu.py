from rich import print
#from src.Author import Author
from Evaluator import Evaluator
from Course import Course
from Jobs import Job
#from src.Feedback import Feedbacks
from Project import Projects
from Evalbyproject import EvalByProject
from dash import DASHBOARD

'''''''''
Classe de menus - display das telas que o usuario ira escolher entre elas. 
Classe menu são rotinas visuais. 
O que me usuario ira ver? 
Interações 
'''''''''
class Menu:
    #def __init__(self):
        
    def evaluator(self):
        print(" :star: [bold yellow]Welcome to our Exibition [/bold yellow].:star:")
        evalu = Evaluator()
        evalu.ask() 
        self.evaluation()
        print("Would you like to evaluate another project? Type 1 for YES or 2 for NO")
        answer = input()
        if answer == '1':
            self.evaluation()
        elif answer == '2':
            print("[bold yellow]Please, check the dashboard before leaving. It was a pleasure having you here. :heart: [/bold yellow]")
            dash = DASHBOARD()
            dash.queries()       
    


    def evaluation(self):
        print("[magenta] Now please evaluate the project [/magenta]")
        pevalu = EvalByProject()
        pevalu.main()










        # while True:
        #     print("Are you a student? Type 1 for YES or 2 for NO.")
        #     student = input()
        #     if student == "1":
        #         Course.courses()
        #         break
        #     elif student == "2":
        #         Job.jobs()
        #         break
        #     else: 
        #         print(":no_entry:", student, "is not recognized. [italic]Please type 1 for yes or 2 for no.[/italic]")
        # print("Please, provide us your age.")
        #Evaluator.age()




        # while True:
        #     print("[bold purple]Would you come again to future Exibitions?[/bold purple] :purple_heart: [italic purple]Type 1 for yes or 2 for no[/italic purple]")
        #     answer = input()
        #     if answer == '1':
        #         #Save the answer to the DATABASE
        #         EvalByProject.visitAgain()
        #         print(":red_heart: [yellow] Thank you! Looking foward to see you again![/yellow]")
        #         break
        #     elif answer == "2":
        #         EvalByProject.visitAgain()
        #         print(":crying_face:[red] We're sorry. We'll improve for the next time. [/red]")
        #         break
        #     else:
        #         print(":no_entry:", answer , "[red] Sorry, this answer is not recognized.[italic] Please type 1 or 2.[/italic][/red]")
        # while True:
        #     print("Would you like to provide a feedback? [italic] Type 1 for yes or 2 for no [/italic]")
        #     feedback = input()
        #     if feedback == "1":
        #         EvalByProject.feedback()
        #     elif feedback == "2": 
        #         print("[bold green]Alright! Thank you for being here. Please check our Dashboard before leaving.[/bold green] :red_heart:")
        #         exit()
        #     else:
        #         print(answer, "is not recognized. Please type [italic] YES or NO [/italic]")




