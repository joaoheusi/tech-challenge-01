# Tech Challenge - FIAP - Software Architecture
## Current phase: Phase 2

Self-service system developed for an expanding snack bar, aimed at solving issues of confusion and delays in orders.



In the first phase, the following functionalities were developed for the API:

* Customer Registration
* Customer Identification via CPF 
* Create, Edit, and Remove Products 
* Search Products by Category
* Checkout, send the selected products to the queue.
* Webhook route to receive payment confirmation, changes the order status to preparing.
* Route to change the order status to ready.
* Route to change the order status to completed
* List Orders
* List ongoing orders, sorted by status and age.

## General information

To create or fetch a customer use the routes in ```/v1/customers```.

To create, edit and remove products use the routes in ``` /v1/products``` *

To create an order, or to retrieve multiple orders use the routes in ``` /v1/orders ```.

*We didn't create a remove products route. We believe the best approach would be to deactivate a product if necessary. It can be done by passing out ``` isActive=false```in ```PATCH /v1/products/{productId}```

## Suggested use

1) Create products using POST /v1/products

2) Create one or multiple orders using POST /v1/orders

3) Get the ```payment externalId``` with GET /v1/orders/{order_id}/payment

4) Send a POST /v1/notifications with {"action":"payment.updated", data: {"id": ```payment externalId```}}

5) Send to one of the orders POST /v1/orders/{order_id}/ready

6) List ongoing orders with GET /v1/orders/ongoing

7) Send a POST /v1/orders/{order_id}/complete

### If you want to use the real mercadopago payment gateway it will be necessary to provide a valid key in .env. As well as make a real payment to the qr code and later send a notification with the real mercadopago payment id in POST /v1/notificiations. For ease of use, the default payment provider is a fake one. To change it go to src/config/injector/modules and find the class PaymentsProviderModule where more information is provided.


## To run the code using docker(recommended):

First you need to install  ```docker``` and ```docker compose```.

Run:
```
docker compose up
```

## To access the Swagger

To access the swagger you first need to run the applicatio and navigate to:

http://0.0.0.0:80/docs

or 

http://localhost:80/docs

There is also a ```.rest``` file in the root directory to help you test out the API.


### If you have any doubts or trouble trying to deploy, our FIAP information is as follows:


6SOAT
Group 53

RM 353469 João Marcelo Heméritas Heusi

RM 354274 Luciano Marcos Farias Junior

RM 353599 Sabrina Reis Hablocher
