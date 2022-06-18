# Image

Application is a Python project with a Django Rest Framework. 
The main function is posting images and showing a list of the URL of this image. 
In Project is three build accounts with different possibilities: Basic, Premium, and Enterprise.

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

## Run docker
In terminal write:
```
docker build --tag python-django .  # build container
docker-compose up   # run docker container
```


