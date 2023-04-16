import typer
from Menu import Menu

#Apenas o inicio do programa usando Typer. 
#Apartir daqui estou usando2 typer como meu framework
def main():
    mn = Menu()
    mn.evaluator()

if __name__ == "__main__":
    typer.run(main)