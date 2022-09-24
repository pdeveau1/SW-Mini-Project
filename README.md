# SW-Mini-Project

Work distribution:
------------

1. Front end: Shun (Flutter, firebase, login, etc)
2. Back end: Paige (Twiiter api, google cloud api, django api, etc)

Documentation:
-------------

#### UI Live Demo ####
https://user-images.githubusercontent.com/67556230/192120453-1316ac2e-bf8b-4e5c-9340-62026983d3ca.mov

#### Twitter API ####
To login use the endpoint '/api-auth/login/'.
This will bring up a login prompt and sign in so that all of the twitter accounts that user searches will be saved.
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/67556230/192120568-d8d33b59-ef1d-42b4-b100-5a2ae536f860.png">

To if you do not have an account and would like to register use the endpoint '/twitter/register/'.
This will bring up a registration prompt for the user to register using their username and password and a POST action.
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/67556230/192120611-7e72b5e3-0655-44b8-8630-bdf92ce61eda.png">

To add a user to the database use the endpoint 'twitter/user/'. Use a POST with the body containing the username in JSON format.
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/67556230/192120864-c3285675-c04f-4edc-9707-e5701aa8d19f.png">
This will return the username, if it is a bot or not, the sentiment, and the topics.
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/67556230/192120854-3927afc7-4e80-4fb9-b1a0-27b68c5ddf7b.png">
If you would like to update the information of the twitter user you can use the same enpoint, but perform a PUT instead of a POST with the username in JSON format.
