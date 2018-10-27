# Shop-manager

## This is the backend/Endpoints for the store-manager-UI

## Badges

[![Build Status](https://travis-ci.org/masete/Shop-manager.svg?branch=ft-single-sales-record-161439633)](https://travis-ci.org/masete/Shop-manager)
[![Maintainability](https://api.codeclimate.com/v1/badges/15ffa1f06d31e2d884ae/maintainability)](https://codeclimate.com/github/masete/Shop-manager/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/masete/Shop-manager/badge.svg?branch=ft-single-sales-record-161439633)](https://coveralls.io/github/masete/Shop-manager?branch=ft-single-sales-record-161439633)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d74df6128d854c51be20be9b9e775544)](https://www.codacy.com/app/masete/Shop-manager?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=masete/Shop-manager&amp;utm_campaign=Badge_Grade)


## Features 

- Admin can add a product
- Admin or store attendant can get all products
- Admin or store attendant can get a specific product.
- Store attendant can add a sale order.
- Admin can get all sale order details.

## API Endpoints

| REQUEST | ROUTE | FUNCTIONALITY |
| ------- | ----- | ------------- |
| GET | /api/v1/products | Fetches all products|
| GET | api/v1/products/&lt;product_id&gt; | Fetches a single product |
| GET | api/v1/sales | Fetches all sales records |
| GET | api/v1/sales/&lt;sales_id&gt; | Fetches a single sales record |
| POST | api/v1/products | Creates a product |
| POST | api/v1/sales | Creates a sales order |

**Getting started with the app**

**Modules and tools used to build the endpoints**

* [Python 3.6](https://docs.python.org/3/)

* [Flask](http://flask.pocoo.org/)


## Installation

Create a new directory and initialize git in it. Clone this repository by running
```sh
$ git clone URL   which in this case is https://github.com/masete/Shop-manager.git
```
Create a virtual environment. For example, with virtualenv, create a virtual environment named venv using
```sh
$ virtualenv venv
```
Activate the virtual environment
```sh
$ cd venv/scripts/activate
```
Install the dependencies in the requirements.txt file using pip
```sh

$ pip install -r requirements.txt
```
Populate the requirements.txt using

$ pip freeze  >  requirements.txt
```sh
Start the application by running
```
$ python run.py
```sh
Test your setup using [postman](www.getpostman.com) REST-client
You can checkout my postman collections from :
https://documenter.getpostman.com/view/5131975/RWgxvFbt
 
The APP is hosted on heroku, checkout this Link: https://store-manager-vii.herokuapp.com/


Hope you had a nice ride