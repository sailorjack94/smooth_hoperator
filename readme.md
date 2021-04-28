#Smooth Hoperator

**Smooth Hoperator** is an ultra-light browser based app to track products and suppliers. Specifically designed for beer products and managing detail on individual suppliers/brewers. The app has a variety of additional functionality including Stock Level tracking with warnings for Low/Out of Stock products, form based product/supplier management to allow editing and addition/removal of items, stock value and standing profit calculation, individual markup calculations and a variety of useful filters, sortings and groupings.

----------------------------------------------------------------

##Installation

Smooth Hoperator is a full-stack application written in Python (Flask + Psycopg), a database running PostgreSQL and a reactive front-end in HTML with CSS styling.

The following python packages are required to use Smooth Hoperator and should be installed as below:

```
pip install flask

pip install psycopg
```

Once the dependendcies have been resolved, clone and setup the files as below:
NB - SSH must be setup and enabled.

```
git clone git@github.com:sailorjack94/smooth_hoperator.git
```

Setup the database by running the following commands in your terminal:

```
createdb smooth_hoperator

psql -d smooth_hoperator -f smooth_hoperator/db/smooth_hoperator.sql

python3 console.py

flask run
```

Once the above commands have been executed, open a browser window to 127.0.0.1:5000 and you should see Smooth Hoperator running. Instructions are on the Home Page, and contained within individual pages.


###Home Page


###Beer Listing


###Beer Management/Detail


###Brewer Management/Detail