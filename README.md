# The application is under development. Not everything is complete.

# Image

Application is a Python project with a Django Rest Framework. 
The main function is posting images and showing a list of the URL of this image. 
In Project is four build accounts with different possibilities: Basic, Premium, Enterprise and Admin.

Different accounts tier has different possibilities:
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
    - ability to fetch a link to the (binary) image that expires after a number of seconds (user can specify any number between 300 and 30000)

## Admin Power
- may add custom user and choose tier
- may add image and assign a user to it
- may create a thumbnail image with any size

## URLS
http://localhost:8000/ - home (some frontend) <br/>
http://localhost:8000/admin - admin page <br/>
http://localhost:8000/api/ - Rest Framework Django (main APP) <br/>

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
docker-compose up   # run docker container
```
More commands in `commands.txt`


