##Overview
The application allows all users to  read posts written by registered users. The registered users can create , update and delete their posts. They can update their profile which includes their username,email and a display picture. They can also comment on other users’ posts. The application as expected also has a login and SignUp form for users who wish to register and login to the website. Also it has a search feature that allows users to search posts by their title or author.
##Components
manage.py : Django's command-line utility for administrative tasks.
Main project directory- learndjango :
settings.py: This file stores all the configurations of the application’s django installations. 
urls.py: This file stores the root urls or paths of the web application.So, it is referred to locate templates in the app directory for the given path.
blog: This directory handles all the views, models, forms , templates etc. related to Posts and Comments.
models.py: It contains the model for Post and Comment .eg of model for Comments:

views.py:  It contains function-based and class based views related to the above models. Eg. view for post creation form:
		
admin.py: This file is for register the models created on admin site.
Templates: This directory contains the django templates(html files) for rendering to the web pages.
##Users: Similarly, this directory  has the models.py ,views.py ,forms.py files and templates directory which handle the models, views ,forms, templates etc. related to the User model.
media : It has the static media files required for the project which include display pictures of the registered users.
posts.json: this file has some sample posts which have been entered into the database.
##Database 
The django application uses sqlite3 database to store information of User, Post,Comment, and Profile model.
For every new model created run the following commands in the given order to prepare a table for that model in the database:
1.python manage.py makemigrations
2.python manage.py migrate
##Requirements
Find in https://github.com/kopal960/Blog/blob/master/requirements.txt
##Deployment
Github and Heroku used
https://blog-project-django.herokuapp.com
