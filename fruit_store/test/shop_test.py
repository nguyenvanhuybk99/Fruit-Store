import click
import requests

@click.group()
def cli():
    pass


@click.command('get_all_product')
def get_all_product():
    url = "http://0.0.0.0:8000/shop/product"
    print(url)
    response = requests.request("GET", url)
    print(response.text)


@click.command('get_product')
@click.option('-p', '--pk', default='1', help='primary key of product')
def get_product(pk):
    url = "http://0.0.0.0:8000/shop/product/" + str(pk)
    print(url)
    response = requests.request("GET", url)
    print(response.text)


if __name__ == '__main__':
    cli.add_command(get_all_product)
    cli.add_command(get_product)
    cli()