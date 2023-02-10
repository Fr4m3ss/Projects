# PythonDB-Project
Movie Database for COP4521
Members: 
- Greg Garman
- Ben Zech
- Katterin Soto
- Frankie Messina
- Chistopher Alvarez


## Description:
Our website is a full stack application that allows users to view a list of movies, see reviews other users have left for each movie, and leave a review of their own. The process involves first creating an account. There are two different type of accounts/roles in the application, which is the regular user and the admin. The regular users can leave reviews for movies while the admin users cannot, but admins are able to make modifications to the database. The utility behind a deployed website, like ours, is that anybody from anywhere in the world could contribute by leaving a movie review and it helps users get an idea of which movies might be worth seeing. It is also a fun way for people to give their opinions about movies. The application was written in Django using Python, HTML, and CSS.


## User Interface:
The application is straight forward, as the user enters in information into fields that have labels for what they should be. 

## Libraries:
- Django, django-crispy-forms,Pillow  

## Other resources:
The application is deployed on Microsoft Azure and the URL that our group used for presenting the project is here:
https://cop4521finalproject.azurewebsites.net/
The app is also containerized using Docker. The process for deploying the application involved first building an image from a virtual machine, and pushing to Docker Hub (account fsugreg123) and then linking the image to Azure where it was downloaded and deployed.

## Sources used in project:
- For installing Docker, this official tutorial was used:
  - https://docs.docker.com/engine/install/ubuntu/

- The main resource our group used to learn Django and obtain a feel for how a Django app is structured is this YouTube series which consists of walkthrough videos for how to build a blog app in Django. Though the foundation of our app is structured similarly to that of this blog app, the code in our application was written by us.
https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p

- The movie information and images are retrieved from this source:
  - https://www.themoviedb.org/?language=en-US

- The CSS referenced the following links:
  - https://www.w3schools.com/html/html_css.asp
  - https://developer.mozilla.org/en-US/docs/Web/CSS/color

## Separation of Work:
Gregory Garman:
- Containerizing and deploying to Azure
- Creating forms users enter information into and the corresponding models that are stored in the DB.
- Security features such as adding function decorators and class mixins, as well as CSRF tokens.
- Helped implement leaving reviews for movies

Benjamin Zech:
- Information management of movies, specifically with titles, images, and description
- Write README.md

Katterin Soto:
- Implemented user creation, login and logout system
- Created Profile Management for users to access username, password, and email
- User access to setting a profile image

Frankie Messina:
- Implemented CSS to make website more appealing in shape and color
- Embedded hyperlink to movie information in the movie image
- Added back button to home from reviews tab

Chistopher Alvarez:
- Information management of reviews
- Delete reviews for user and super user


