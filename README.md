# SW-Mini-Project #

## Work distribution: ##


1. Front end: Shun (Flutter, firebase, login, etc)
2. Back end: Paige (Twiiter api, google cloud api, django api, etc)

## Documentation: ##

### UI Live Demo ###
https://user-images.githubusercontent.com/67556230/192120453-1316ac2e-bf8b-4e5c-9340-62026983d3ca.mov

### Twitter API ###
#### Login ####
To login use the endpoint '/api-auth/login/'.
This will bring up a login prompt and sign in so that all of the twitter accounts that user searches will be saved.
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/67556230/192120568-d8d33b59-ef1d-42b4-b100-5a2ae536f860.png">

#### Register ####
To if you do not have an account and would like to register use the endpoint '/twitter/register/'.
This will bring up a registration prompt for the user to register using their username and password and a POST action.
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/67556230/192120611-7e72b5e3-0655-44b8-8630-bdf92ce61eda.png">

#### Add Twitter user ####
To add a user to the database use the endpoint 'twitter/user/'. Use a POST with the body containing the username in JSON format.
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/67556230/192120864-c3285675-c04f-4edc-9707-e5701aa8d19f.png">
This will return the username, if it is a bot or not, the sentiment, and the topics.
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/67556230/192120854-3927afc7-4e80-4fb9-b1a0-27b68c5ddf7b.png">
If you would like to update the information of the twitter user you can use the same enpoint, but perform a PUT instead of a POST with the username in JSON format.

#### Check Twitter user ####
To get the information about a specific twitter user that have already addded to the database use the endpoint 'twitter/user/<username>' and perform a GET.
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/67556230/192120990-6d71987e-1846-4d85-82bb-f4e483675a05.png">

 #### Check details of Twitter user ####
 To get the specific details of the twitter user perform a GET with the endpoints 'twitter/isbot/<username>','twitter/sentiment/<username>',or 'twitter/topics/<username>'.
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/67556230/192121020-69a26c7c-46fe-4960-af42-df656343021b.png">
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/67556230/192121031-6551e09c-959f-47d3-bcc6-269a84276052.png">
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/67556230/192121037-d6c641e3-cf38-4442-a4d2-91ca69d8d71d.png">

* Front end:
--------------

1. Front end app: We originally want to do a IOS app so we choose the Xcode as our SDK. This SDK is easy on UI design since it has graphical edditing but very inconvinient in calling and using outside resources, like APIs. So we choose to use Flutter as our SDK. This one is relatively harder on UI design but easier on code development. 

2. Login section: 
