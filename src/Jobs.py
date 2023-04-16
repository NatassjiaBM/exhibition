from rich.console import Console
from rich.table import Table
from rich import print
import sqlite3
sqliteConnection = sqlite3.connect(r"C:\Users\admin\Pessoal\Whitecliffe\codes\Natassjia\Presentation\DataBase.db")
cursor = sqliteConnection.cursor()


table = Table(title="[bold]Jobs[/bold]")
 
class Job:
    def jobs(self):
        table.add_column("ID", justify="right", style="cyan", no_wrap=True)
        table.add_column("Job", justify="left", style="white")

        ssql = f"Select * from Jobs"
        cursor = sqliteConnection.cursor()
        cursor.execute(ssql)
        rows = cursor.fetchall()
        for row in rows:
            table.add_row(str(row[0]), row[1])
        console = Console()
        console.print(table)
        print(":woman_mechanic: Select your Job. Type the Job ID.")
        answer = input()
        return answer
        # Could I automatically select that its a student ? 
        # addJob= f"Insert into evaluator(Jobs, CourseID) values ('{answer}', '20' )"
        # cursor = sqliteConnection.cursor()
        # cursor.execute(addJob)
        # sqliteConnection.commit()

