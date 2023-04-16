import rich 
from rich import print
from rich.table import Table
from rich.console import Console
import sqlite3
sqliteConnection = sqlite3.connect(r"C:\Users\admin\Pessoal\Whitecliffe\codes\Natassjia\Presentation\DataBase.db")
cursor = sqliteConnection.cursor()

aspecttable = Table(title ="[bold magenta]Favourite Aspects[/bold magenta]")          


class FavourtiteAspects:
    def aspects(self):
            aspecttable.add_column("ID", justify="right", style="cyan", no_wrap=True)
            aspecttable.add_column("Fav. Aspect", justify="right", style="green")

            ssql = f"Select * from FavAspect"
            cursor = sqliteConnection.cursor()
            cursor.execute(ssql)
            rows = cursor.fetchall()
            for row in rows:
                aspecttable.add_row(str(row[0]), row[1])
            console = Console()
            console.print(aspecttable)
            print("Select your favorite aspects of the presentation")
            answer = input() 
            return answer