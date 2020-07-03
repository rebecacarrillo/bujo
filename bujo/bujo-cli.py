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

click.echo('Start? [y/n] ' , nl=False)
c = click.getchar()
click.echo()
if c == 'y':
    click.echo('Yay!')
elif c == 'n':
    click.echo('Okay bye')
else:
    click.echo('No manches, invalid input')


if __name__ == "__main__":
    main()