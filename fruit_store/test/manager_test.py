import click
import requests

@click.group()
def cli():
    pass


@click.command('manager_get_all_product')
def manager_get_all_product():
    url = "http://0.0.0.0:8000/manager/product"
    print(url)
    response = requests.request("GET", url)
    print(response.text)


@click.command('manager_get_product_by_pk')
@click.option('-p', '--pk', default='1', help='primary key of product')
def manager_get_product_by_pk(pk):
    url = "http://0.0.0.0:8000/manager/product/" + str(pk)
    print(url)
    response = requests.request("GET", url)
    print(response.text)


@click.command('manager_post_product')
def manager_post_product():
    url = "http://0.0.0.0:8000/manager/product"
    print(url)

    payload={
        'name': 'watermelon',
        'price': '30',
        'quantity': '2'
        }

    response = requests.request("POST", url, data=payload)
    print(response.text)


@click.command('manager_put_product')
@click.option('-p', '--pk', default='1', help='primary key of product')
def manager_put_product(pk):
    url = "http://0.0.0.0:8000/manager/product/" + str(pk)
    print(url)
    
    payload={
        'name': 'orange',
        'price': '15',
        'quantity_in_stock': '30'
        }

    response = requests.request("PUT", url, data=payload)
    print(response.text)


@click.command('manager_delete_product')
@click.option('-p', '--pk', default='1', help='primary key of product')
def manager_delete_product(pk):
    url = "http://0.0.0.0:8000/manager/product/" + str(pk)
    print(url)
    response = requests.request("DELETE", url)
    print(response.text)


@click.command('manager_get_all_customer')
def manager_get_all_customer():
    url = "http://0.0.0.0:8000/manager/customer"
    print(url)
    response = requests.request("GET", url)
    print(response.text)


@click.command('manager_get_all_order')
def manager_get_all_order():
    url = "http://0.0.0.0:8000/manager/order"
    print(url)
    response = requests.request("GET", url)
    print(response.text)

@click.command('manager_get_order_by_pk')
@click.option('-p', '--pk', default='1', help='primary key of order')
def manager_get_order_by_pk(pk):
    url = "http://0.0.0.0:8000/manager/order/" + str(pk)
    print(url)
    response = requests.request("GET", url)
    print(response.text)


if __name__ == '__main__':
    cli.add_command(manager_get_all_product)
    cli.add_command(manager_get_product_by_pk)
    cli.add_command(manager_post_product)
    cli.add_command(manager_put_product)
    cli.add_command(manager_delete_product)
    cli.add_command(manager_get_all_customer)
    cli.add_command(manager_get_all_order)
    cli.add_command(manager_get_order_by_pk)
    cli()

