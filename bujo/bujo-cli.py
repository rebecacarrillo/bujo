import click
import colored
from colored import stylize
from utilcli import showLoader

print(stylize("This is the BUJO CLI", colored.fg("aquamarine_1b")))

@click.group()
def bujo():
    pass

@click.command()
def main():
    click.echo("""
    Welcome to the
    
        .-.                    .----.        
  (_) )-.    _     .-.      /.--.    .- 
     / __)  '     (        //    )`-'   
    /    `.  /     )..-.   //    /       
   /'      )(     / `.   /(    /        
(_/  `----'  `._.'    `-'  `-.'         

    CLI
    """)



@bujo.command()
def load():
    showLoader([1,1,1,1,1,1])

if __name__ == "__main__":
    bujo()