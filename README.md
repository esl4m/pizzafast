# PizzaFast
Python Django REST framework application for ordering pizza.


## To run the app:
- Create adn activate virtualenv: 
`virtualenv env`
`source env/bin/activate`

- Clone the repo to your local `git clone https://github.com/esl4m/pizzafast.git`

- cd into the application folder

- Create .env file , you can copy .env.example and rename your values

- Create Postgres Database and do not forget to add it to your .env file.

- Run the following commands to apply migrations for default Django Tables
`./manage.py makemigrations`
`./manage.py migrate`

- Create super user `./manage.py createsuperuser`

- Run `./manage.py runserver`

- To check the endpoints by url
List all pizza entries and create new `http://127.0.0.1:8000/pizza`
Update or Delete `http://127.0.0.1:8000/pizza/{{pizza_id}}`

List all orders and create new `http://127.0.0.1:8000/order`
Update or Delete `http://127.0.0.1:8000/order/{{order_id}}`

- Or by postman: Add the url and method

-- For Pizza --
```
GET http://127.0.0.1:8000/pizza : will list all pizza
POST: add in body "row json" like this
{
    "name": "margrita",
    "small_size_price": 10,
    "med_size_price": 30
}
PUT: http://127.0.0.1:8000/pizza/{{pizza_id}} --> to update any add the json in body
DELETE: http://127.0.0.1:8000/pizza/{{pizza_id}} --> to delete the pizza by id
```

-- For Pizza Orders --
```
GET http://127.0.0.1:8000/order : will list all orders
POST: add in body "row json" like this
{
    {
        "pizza": 2,
        "pizza_flavor": 1,
        "size": 30,
        "status": 2,
        "customer_name": "esl4m",
        "customer_address": "My current address",
        "price": 15
    }
}
PUT: http://127.0.0.1:8000/order/{{order_id}} --> to update any add the json in body
DELETE: http://127.0.0.1:8000/order/{{order_id}} --> to delete the pizza by id
```

-- To filter orders by customer name / order status --
```
http://127.0.0.1:8000/order/filter/status/{{customer_name}}
http://127.0.0.1:8000/order/filter/status/{{status_id}}

```

Enjoy :)
