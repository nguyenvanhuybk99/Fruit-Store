# Fruit Store

Develop basic Fruit-Store by Django Rest Framework with Mongodb

### Database bao gồm các collections: 
1. shop_product,
2. cart_cart, cart_cartitem
3. customer_customer, customer_order, customer_orderitem

Đối với những request yêu cầu thông tin người dùng, thông tin người dùng sẽ được request gửi thông qua form json, {"username":"nguyenvanhuybk99"}

Đối với các request: Thêm vào giỏ, chỉnh sửa giỏ hàng, đặt hàng, hệ thống sẽ kiểm tra số lượng trong kho, nếu thỏa mãn yêu cầu thì tiến hàng xử lý request, nếu ko sẽ trả về 'out of stock'. Giỏ hàng sẽ được lưu tại database


### Cửa hàng gồm có những chức năng cơ bản sau:

 Phía khách hàng:

1. Đăng ký tài khoản
2. Xem danh sách sản phẩm (GET), xem thông tin chi tiết sản phẩm (GET)
3. Thêm vào giỏ (PUT), xem thông tin giỏ hàng (GET), chỉnh sửa giỏ hàng (PUT)
4. Đặt hàng (POST), xem lịch sử đơn hàng (GET), xem chi tiết đơn hàng (GET)

Phía quản lý cửa hàng:
1. Xem danh sách sản phẩm (GET), xem thông tin chi tiết sản phẩm (GET)
2. Chỉnh sửa thông tin sản phẩm (PUT), tạo mới sản phẩm (POST), xóa sản phẩm (DELETE)
3. Xem danh sách khách hàng (GET)
4. Xem danh sách đơn hàng (GET), xem chi tiết đơn hàng (GET)


# Tutorial

> cd fruit_store

## create image from taz file (images: django_mongo:latest) or from Dockerfile

> docker load --input backend_test.tar

or

> docker build -t django_mongo:latest .

## create and start docker container 

> docker run -itd -p 8000:8000 --name fruit_store django_mongo:latest

## exec container and run server && test (use 2 terminal)

> docker exec -it fruit_store bash

> python manage.py runserver 0.0.0.0:8000

open other terminal to test:

> docker exec -it fruit_store bash

> cd test

Test phía khách hàng:

1. Đăng ký tài khoản theo request.data
> python customer_test.py register

2. Xem danh sách sản phẩm
> python shop_test.py get_all_product

3. Xem chi tiêt sản phẩm theo id
> python shop_test.py get_product --pk 1

4. Thêm vào giỏ theo id sản phẩm
> python cart_test.py add_to_cart --pk 1

5. Xem thông tin giỏ hàng 
> python cart_test.py view_cart

6. Chỉnh sửa giỏ hàng theo id của giỏ và request.data
> python cart_test.py update_cart --pk 1

7. Đặt hàng
> python customer_test.py place_order

8. Xem lịch sử đơn hang
> python customer_test.py get_order_list

9. Xem chi tiết đơn hàng theo id
> python customer_test.py get_order_detail --pk 1

Test phía chủ cửa hàng:

1. Xem danh sách sản phẩm:
> python manager_test.py manager_get_all_product

2. Xem chi tiết sản phẩm
> python manager_test.py manager_get_product_by_pk --pk 1

3. Thêm sản phẩm theo request.data
> python manager_test.py manager_post_product

4. Chỉnh sửa sản phẩm theo id sản phẩm và request.data
> python manager_test.py manager_put_product --pk 1

5. Xóa sản phẩm theo id sản phẩm
> python manager_test.py manager_delete_product --pk 3

6. Xem danh sách khách hàng
> python manager_test.py manager_get_all_customer

7. Xem lịch sử đơn hàng
> python manager_test.py manager_get_all_order

9. Xem chi tiết đơn hàng theo id đơn hàng
> python manager_test.py manage_get_order_by_ok --pk 1
