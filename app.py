import click
from data_loader import load_data
from top_products import top_n_products
from user_recommend import user_recommendations

@click.group()
def cli():
    pass

@click.command()
@click.option('--n', default=10, help='Number of top products')
@click.option('--start', default=None, help='Start date YYYY-MM-DD')
@click.option('--end', default=None, help='End date YYYY-MM-DD')
def top_products(n, start, end):
    df = load_data()
    top = top_n_products(df, n, start, end)
    click.echo(top)

@click.command()
@click.option('--user', required=True, type=int, help='User ID for recommendations')
@click.option('--n', default=5, help='Number of recommendations')
def recommend(user, n):
    df = load_data()
    recs = user_recommendations(df, user, n)
    click.echo(recs)

cli.add_command(top_products)
cli.add_command(recommend)

if __name__ == "__main__":
    cli()