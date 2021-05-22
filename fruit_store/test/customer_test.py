import click
import requests

@click.group()
def cli():
    pass


@click.command('register')
def register():
    url = "http://0.0.0.0:8000/customer/register"
    print(url)

    payload={
        'username': 'nguyenvanhuybk99',
        'password': 'backend'
        }

    response = requests.request("POST", url, data=payload)
    print(response.text)


@click.command('place_order')
def place_order():
    url = "http://0.0.0.0:8000/customer/place_order"
    print(url)

    payload={
        'username': 'nguyenvanhuybk99',
        }

    response = requests.request("POST", url, data=payload)
    print(response.text)


@click.command('get_order_list')
def get_order_list():
    url = "http://0.0.0.0:8000/customer/order"
    print(url)

    payload={
        'username': 'nguyenvanhuybk99',
        }

    response = requests.request("GET", url, data=payload)
    print(response.text)


@click.command('get_order_detail')
@click.option('-p', '--pk', default='1', help='primary key of order')
def get_order_detail(pk):
    url = "http://0.0.0.0:8000/customer/order/" + str(pk)
    print(url)

    payload={
        'username': 'nguyenvanhuybk99',
        }

    response = requests.request("GET", url, data=payload)
    print(response.text)





if __name__ == '__main__':
    cli.add_command(register)
    cli.add_command(place_order)
    cli.add_command(get_order_detail)
    cli.add_command(get_order_list)
    cli()