# Stock API Application
**Author**: Andrew Baik
**Version**: 1.0.0

## Overview
It's an AWS deployed backend web application with pyramid framework. Retrieves information from third-party API, saves into a database with POSTGRES.

## API
This application utilizes [IEX TRADING](https://iextrading.com/developer/docs/) API to retrieve public company stock information.


# Change Log
Aug 27, 2018
- [x] Created a Portfolio class with id, name, date_created, date_updated
- [x] Defined two class methods on your Portfolio class: one() and new()
- [x] In model/stock.py, created a Stock class with mirroring the data of 3rd party API
- [x] Define three class methods on your Stock class: one(), new(), and destroy()
- [x] Created Schema serializer
- [x] Created Portfolio, Stock, and Company View Controllers
- [x] Successfully interact with 3rd party API


Aug 23, 2018
- [x] Deployed the web application to AWS EC2
- [x] Added company and portfolio apis

Aug 22, 2018

- [x] Disable the unnecessary functionality of your scaffold, by commenting out the include() statements in your __init__.py:main() function.
- [x] Delete the templates/ directory
- [x] Remove the contents of default.py and notfound.py
- [x] GET / - the base API route
- [x] GET /api/v1/stock/ responds status code 200
- [x] POST /api/v1/stock/ responds status code 200
