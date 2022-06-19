# The application is under development. Not everything is complete.

# Image

Application is a Python project with a Django Rest Framework. 
The main function is posting images and showing a list of the URL of this image. 
In Project is three build accounts with different possibilities: Basic, Premium, and Enterprise.

TO DO:
Different accounts have different possibilities, because now everyone can see orginall, and thubnail 200px and 400px.

PLAN:
- Basic after uploading an image get:
    -  a link to a thumbnail that's 200px in height

- Premium after uploading an image get:
    - a link to a thumbnail that's 200px in height
    - a link to a thumbnail that's 400px in height
    - a link to the originally uploaded image

- Enterprise after uploading an image get:
    - a link to a thumbnail that's 200px in height
    - a link to a thumbnail that's 400px in height
    - a link to the originally uploaded image

## URLS
http://localhost:8000/ - home
http://localhost:8000/admin - admin page
http://localhost:8000/api/ - Rest Framework Django

## Users
If you want to log in as previously prepared users, use the username and password below.
| Username  | Password |
| :---: | :---: |
| admin  | admin  |
| basic  | basic  |
| premium  | premium  |
| enterprise  | enterprise  |

## Run docker
In terminal write:
```
docker build --tag python-django .  # build container
docker-compose up   # run docker container
```


