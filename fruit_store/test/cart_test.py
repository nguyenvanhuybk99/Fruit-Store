import click
import requests

@click.group()
def cli():
    pass


@click.command('view_cart')
def view_cart():
    url = "http://0.0.0.0:8000/cart/cart"
    print(url)

    payload={
        'username': 'nguyenvanhuybk99',
        }

    response = requests.request("GET", url, data=payload)
    print(response.text)


@click.command('add_to_cart')
@click.option('-p', '--pk', default='1', help='primary key of product')
def add_to_cart(pk):
    url = "http://0.0.0.0:8000/cart/add_to_cart/" + str(pk)
    print(url)

    payload={
        'username': 'nguyenvanhuybk99',
        }

    response = requests.request("PUT", url, data=payload)
    print(response.text)


@click.command('update_cart')
@click.option('-p', '--pk', default='1', help='primary key of cart')
def update_cart(pk):
    url = "http://0.0.0.0:8000/cart/update_cart/" + str(pk)
    print(url)

    payload={
        'username': 'nguyenvanhuybk99',
        'fruits': '{"apple":2}'
        }

    response = requests.request("PUT", url, data=payload)
    print(response.text)

if __name__ == '__main__':
    cli.add_command(view_cart)
    cli.add_command(add_to_cart)
    cli.add_command(update_cart)
    cli()