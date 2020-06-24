# Plivo-SMSWebApp

Hi! This is a SMS web application using Flask, a web development framework written in Python. This web app uses a Plivo phone number and the Plivo API
to send and receive SMS messages. The web app also has the ability to show and filter your message history. 

## To build and deploy this web app:

### 1. Create a local directory
$ mkdir 'directory name'

$ sudo apt-get install -y python python-pip python-virtualenv

### 2. Setup a virtual env and install the requirements 
$ virtualenv env

You will also need to install all the dependencies in the requirements file

### 3. Clone this repo

### 4. Configure the variables 
There are a few variables that you can change to turn this into your own webapp.

The most important ones are in messenger.py. 
You will need to put in your own Plivo Auth ID, Auth Token, and phone number.

There are also some html changes you can make to change the name of the website, the about me section, etc.

### 5. Deploy the app
$ python messenger.py
Your webapp is now running! You can visit http://localhost:5000 to view your website

### 6. Expose your application to the internet 
I used Ngrok to expose the web server to the internet. It is a free tunneling software. 

### 7. Send your first message!
