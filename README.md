# SW-Mini-Project # 
by Paige, Shun

## Work distribution: ##


1. Front end: Shun (Flutter, firebase, login, etc)
2. Back end: Paige (Twiiter api, google cloud api, django api, etc)

## Documentation: ##

### UI Live Demo ###
https://user-images.githubusercontent.com/67556230/192120453-1316ac2e-bf8b-4e5c-9340-62026983d3ca.mov

### UI explaination ###
<img width="1440" alt="image" src="https://github.com/pdeveau1/SW-Mini-Project/blob/main/UI_design.png">

Section explain: 
1. You can enter you usename or the username you want to search here as input parameters and use the functions related to this input. 

2. This is a function where it will list all the follows of the one you want to search and list them in section 4

3. These are functions that provide Bot check, topic find and see mood functions for the user you want to search and will show them in the corresbonding area with test messages showing now 

4. This section shows all the follows and can also do individual searching for every user and keep them in textfield near those buttons. 

5. This is a module that provide the user with google login with google API used. 

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

2. Login section: We tried to use the twitter login which twitter provided for flutter, however we find out that the one they provide only capable for IOS and Android platform and since we are doing a web application, we then switch to a [google login](https://pub.dev/packages/google_sign_in_web), the login module looks like this:

<img width="1440" alt="image" src="https://github.com/pdeveau1/SW-Mini-Project/blob/main/Google_login.png">

3. List followers: We use a lot of Twitter APIs in our project as discussed in previous sections. We also use some directly in front end with API calls from [Postman](https://restless-satellite-11181.postman.co/workspace/My-Workspace~ac80e874-9a82-49bb-8b33-cbb2291d6465/request/23335950-950d4e68-6b0f-46ec-9e6a-3dfcbb9f74cd?ctx=code), We find a username's id and then use the id to find his/her follows. Of course, this need a [elevated access of twitter developer portal](https://developer.twitter.com/en/portal/projects/1568384337850023941/apps/25404206/settings). Postman is also useful when developing with flutter since it has functions of creating API calling codes based on the SDK we use, here, dart. 

4. Upload on Github: We had faced some problems on uploading the flutter app onto Github since the file is too large, that's why Shun doesn't have a lot of commits on this repository early in the development when he was doing UI and front end stuffs locally. However he did keep all files backups on google drive and update with his teammates. We finally figure it up with VScode commit with linking to github. 
 
5. Firebase linking: Our app also connected to the [firebase](https://console.firebase.google.com/u/1/project/shun-mini/authentication/providers) when we create it and we enable the google and twitter authoritation on it. 

6. HTTP protocal error: This is an interesting and major problem we face during development. Since flutter has a default safe-control setting, and it stops us to make API calls from other server, we tried a whole lot of ways and finally figure it out with an answer [here](https://stackoverflow.com/questions/71157863/dart-flutter-http-request-raises-xmlhttprequest-error)
 
