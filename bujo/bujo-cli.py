import click
import colored
from colored import stylize
from utilcli import showLoader

print(stylize("This is the BUJO CLI", colored.fg("aquamarine_1b")))

@click.group()
def bujo():
    pass

@bujo.command(help="displays cool ascii art greeting message")
def hey():
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

@bujo.command(help="shows a loader")
def load():
    showLoader()

if __name__ == "__main__":
    bujo()