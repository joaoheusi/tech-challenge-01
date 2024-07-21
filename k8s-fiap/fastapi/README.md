# Tech Challenge - FIAP - Software Architecture
## Current phase: Phase 1

Self-service system developed for an expanding snack bar, aimed at solving issues of confusion and delays in orders.



In the first phase, the following functionalities were developed for the API:

* Customer Registration
* Customer Identification via CPF 
* Create, Edit, and Remove Products 
* Search Products by Category
* Fake Checkout, just send the selected products to the queue. The checkout is the order completion.
* List Orders

## General information

To create or fetch a customer use the routes in ```/v1/customers```.

To create, edit and remove products use the routes in ``` /v1/products``` *

To create an order, or to retrieve multiple orders use the routes in ``` /v1/orders ```.

*We didn't create a remove products route. We believe the best approach would be to deactivate a product if necessary. It can be done by passing out ``` isActive=false```in ```PATCH /v1/products/{productId}```



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
