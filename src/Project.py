from rich.console import Console
from rich.table import Table
from rich import print
import sqlite3
sqliteConnection = sqlite3.connect(r"C:\Users\admin\Pessoal\Whitecliffe\codes\Natassjia\Presentation\DataBase.db")
cursor = sqliteConnection.cursor()

class Projects:
    def project(self):
        #Ir no banco, fazer um FOR. Abre um cursor, para cada linha retornda pelo cursor (FOR EACH ROW)
        table = Table(title="[bold]Projects[/bold]")
        table.add_column("ID", justify="right", style="cyan", no_wrap=True)
        table.add_column("Title", style="magenta")
        table.add_column("Author", justify="right", style="green")

#Fazer for aqui. colocar atributo
        ssql = f"Select * from Projects"
        cursor = sqliteConnection.cursor()
        cursor.execute(ssql)
        rows = cursor.fetchall()
        for row in rows: #Iteraction- algo que vai se repetir
             table.add_row(str(row[0]), row[1], row[2])


        console = Console()
        console.print(table)
        print(":pencil: Select one ID to Evaluate the project:")
        answer = input()
        return answer







#This was a previous test to interact with the user. 
# Now it's not used anymore because I can have the data direct from the database
        # table.add_row("01", "Random Triangles", "Fiona Li")
        # table.add_row("02", "Spider man", "Jeffrey")
        # table.add_row("03", "Philosophy", "Taylor")
        #table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")



        # project= f"Insert into evaluator(ProjectID) values ('{answer}')"
        # cursor = sqliteConnection.cursor()
        # cursor.execute(project)
        # sqliteConnection.commit() 
