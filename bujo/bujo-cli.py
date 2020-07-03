import click
import colored
from colored import stylize

print(stylize("This is the BUJO CLI", colored.fg("aquamarine_1b")))

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
if __name__ == "__main__":
    main()