# Neighbourhood Watch
This repository contains code for a neighbourhood watch app written using django framework.
## Authored by Machoka Daisy
## Description
This is  a web application that keeps users in the loop about what is happening in their neighbourhood. Users can view emergency contacts of their neighbourhood, view and upload posts about their neighbourhood and also, view, upload and search for businesses in their neighbourhood.
## Setup instructions
* Visit the live link to interact with the web app (https://neighwatch3000.herokuapp.com)
* Install python
* Git clone https://github.com/MachokaDaisy/py-go.git on your terminal. Find the neighbourhood folder and open it in your editor.
* Set up a virtual environment and install pip
* Set up a database named neighbourhood
* Migrate database by running python3 manage.py migrate
* Install dependencies by running pip install -r requirements.txt
* Run python3 manage.py runserver to run the app locally
* Run python3 manage.py test hood to run tests
## Technologies used
* HTML,
* CSS,
* Bootstrap,
* Python,
* Django,

## BDD
Open the webpage on your browser using the live link provided. 
* Sign up for an account by clicking on the signup tab in the navbar and filling the form. Once complete, you will be logged into your account and your name will be displayed on the navbar.
* Once logged in, fill in the profile form and also add where you live. When done, you will be redirected to a new local page showcasing all info about that page
* * ![Alt text](./static/images/local.png?raw=true "Optional Title")

* On the homepage, view the locations.
* To view information about an area, go to Your Hood tab on the navbar. If you haven't added a profile, you will be asked to add one
* To see the emergency contact of a location, press the contacts button
* * ![Alt text](./static/images/contacts.png?raw=true "Optional Title")

* To view the posts of a location, click the view area posts button on the mini navbar in the Your Hood page
* To add a post, click the add post button
* To view businesses, click the view all businesses button from resulting dropdown businesses tab on the navbar
* To search a business, click the search businesses tab on the navbar businesses dropdown
* * ![Alt text](./static/images/search.png?raw=true "Optional Title")
* To add a business, click the add business tab on the dropdown tab named businesses

* If you do not have a profile, click on the add profile link in the dropdown and fill the form to add your profile
* Click on view profile from the same dropdown to see your profile
* * ![Alt text](./static/images/profile.png?raw=true "Optional Title")
* Once done, click on the logout tab to logout
## Contacts
Feel free to contact me at machokadaisy25@gmail.com. For any contributions, please visit https://github.com/MachokaDaisy/py-go.git
## License
[![License:MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
Copyright (c) 2020 **Machoka Daisy**