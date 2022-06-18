# Image

Application is a Python project with a Django Rest Framework. 
The main function is posting image, and show list to url this image. 
In Project is three build account with diffrent possibilities: Basic, Premium, Enterprise.

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

## Run docker
docker-compose up

