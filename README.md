<h1 align="center">Xtreme Fitness Club<a name="#top"></a></h1>
<h1 align="center"><img src=""/></h1>

<a name="introduction"></a>
## Introduction
*Xtreme Fitness Club* they are fitness enthusiast who would love to share their love of health and fitness with others.
The website designed for business purpose offering personal trainning programs, group tranning programs, apparels and nutritional products.
What more perfect place to purchase these things than a trusted fitness center? The main goal is to make this business venture profitable and .

This is my final project of four Milestone Projects that make up the Full-Stack Web Development Diploma Training at [Code Institute](https://codeinstitute.net/). The goal of this project was to build a full-stack website with the use of HTML, CSS, JavaScript, Python, Django and a relational database; as well as the implementation of a checkout functionality, which has been achieved through the use of Stripe.

Xtreme Fitness is Python-Django web application, support by a PostgreSQL (and SQLite3) database, and deployed via the Heroku PaaS. This project uses the Stripe Checkout API (for educational purposes only: not currently taking real card payments) and is styled using the Bootstrap Grid System.

**NOTE:** If you would like to test the payment functionality of this project, NO NEED to create an account. Use the card number 4242 4242 4242 4242 with ANY address details, expiry date and CVC that you choose.


[Click here to view the project live.](https://xtreme-fitness.herokuapp.com/)


<div align="right"><a href="#top">🔝</a></div>



## Table of Contents

- [Introduction](#introduction)

- [User Experience](#ux)

      - [Wireframe](#wireframe)
      - [Color Palette](#color-palette)
      - [App Logo](#app-logo)

- [User Stories](#user-stories)

- [Database Structure](#database-structure)

<a name="ux"></a>

## User Experience (UX)

<a name="wireframe"></a>

### Wireframe
Link to the wireframe on []()

<a name="color-palette"></a>

### Color Palette

<img src="static/colorpallette.jpg" height="300px"/>

<a name="app-logo"></a>

### App Logo
*Xtreme Fitness Club Favicon*

 <img src="static/xfc-favicon.png" height="300px"/>


<div align="right"><a href="#top">🔝</a></div>


<a name="user-stories"></a>

## User Stories

<img src="static/user-stories-ms4.jpg"/>


Three main users were created:

1.	Superuser (admin) can add products, description of product, price and image.
2.	General browsing users who are potential customers who have browsed on to the website but did not register
3.	Authenticated users who are customer of the site by registering (adding their contact details and creating a user and password)


<div align="right"><a href="#top">🔝</a></div>

<a name="database-structure"></a>

## Database Structure 

Xtreme Fitness Club site is built on Django, and uses the SQLite3 database during all development stages. Through the deployment to Heroku, the database was changed to a PostgreSQL database as that is provided by Heroku as an add-on for production.

The Django’s default user model for authorization is also in use, which allows the project to meet one of the main requirements of separating features by anonymous users, users in session and superusers.

The structure of the apps are inspired by one of Code Institute's mini projects: _Boutique Ado_.

### Profiles App

#### UserProfile Model


| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 User | user | OneToOneField 'User' |  on_delete=models.CASCADE
 Phone number | default_phone_number | CharField | max_length=20, null=True, blank=True
 Address Line1 | default_street_address1 | CharField | max_length=80, null=True, blank=True
 Address Line2 | default_street_address2 | CharField | max_length=80, null=True, blank=True
 Postcode | default_postcode | CharField | max_length=20, null=True, blank=True
 Town/City | default_town_or_city | CharField | max_length=40, null=True, blank=True
 County | default_county | CharField | max_length=80, null=True, blank=True
 Country | default_country | CountryField | blank_label='Country', null=True, blank=True


### Products App

#### Product Model

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Category | category | ForeignKey 'Category' | null=True, blank=True, on_delete=models.SET_NULL
 Sku | sku | CharField | max_length=254, null=True, blank=True
 Name | name | CharField | max_length=254
 Description | description | TextField |max_length=700
 Sizes | has_sizes | BooleanField | default=False, null=True, blank=True
 Price | price | DecimalField | max_digits=6, decimal_places=2
 Rating | rating | DecimalField | max_digits=6, decimal_places=2, null=True, blank=True
 Image URL | image_url | URLField | max_length=300, null=True, blank=True
 Image | image | ImageField | null=True, blank=True

#### Category Model

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Name | name | CharField | max_length=254
Friendly Name | friendly_name | CharField | max_length=254, null=True, blank=True

<img src="static/products-app-data-schema.png"/>



### Blog App

#### Post Model

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Title | title | CharField | max_length=254
Slug | slug | SlugField | null=True, blank=True
Intro | intro | TextField |
Image_url |image_url | URLField | max_length=1024, null=True, blank=True
Image |image | ImageField | null=True, blank=True
Body |body| TextField | 
Body_sub_header |body_sub_header | TextField| null=True, blank=True
Body_text | body_text | TextField | null=True, blank=True
Date_added | date_added | DateTimeField | auto_now_add=True


#### Comment Model

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Post | post | ForeignKey Post, related_name='comments' | null=True, blank=True, on_delete=models.SET_NULL
Name |name | CharField | max_length=254
Email | email | EmailField
Body |body| TextField 
Date_added | date_added | DateTimeField | auto_now_add=True


### Subscribe App

#### Subscribe Model

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Email | email | EmailField | max_length=254, unique=True
Date_added | date_added | DateTimeField | auto_now_add=True