from rich.console import Console
from rich.table import Table
from rich import print
import sqlite3
sqliteConnection = sqlite3.connect(r"C:\Users\admin\Pessoal\Whitecliffe\codes\Natassjia\Presentation\DataBase.db")
cursor = sqliteConnection.cursor()


class Course: 
    
    def courses(self):
        table = Table(title="[bold]Courses[/bold]")
        table.add_column("ID", justify="right", style="cyan", no_wrap=True)
        table.add_column("Course name", justify="left", style="green")

        ssql = f"Select * from Course"
        cursor = sqliteConnection.cursor()
        cursor.execute(ssql)
        rows = cursor.fetchall()
        for row in rows:
            table.add_row(str(row[0]), row[1])
        console = Console()
        console.print(table)
        print(":pencil2: Select your course. Type the ID.")
        answer = input()
        return answer
    

        # addCourse= f"Insert into evaluator(CourseID, Jobs) values ('{answer}', '6')"
        # cursor = sqliteConnection.cursor()
        # cursor.execute(addCourse)
        # sqliteConnection.commit()