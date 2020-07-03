import click


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