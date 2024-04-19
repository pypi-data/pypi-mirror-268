<div align="center">

   <h1> Async Firebase REST API </h1>

   <p>A simple python wrapper for <a href="https://firebase.google.com">Google's Firebase REST API's</a>.</p>
   <p>This package is an async fork of <a href="https://github.com/AsifArmanRahman/firebase-rest-api">AsifArmanRahman/firebase-rest-api</a>.</p>
   <br>

</div>

<div align="center">
   <a href="https://pepy.tech/project/async-firebase-rest-api"> 
      <img alt="Total Downloads" src="https://static.pepy.tech/personalized-badge/async-firebase-rest-api?period=total&units=international_system&left_color=blue&right_color=grey&left_text=Downloads">
   </a>
</div>

<div align="center">

   <a href="https://github.com/matiaskotlik/async-firebase-rest-api/actions/workflows/tests.yml">
      <img alt="GitHub Workflow Status" src="https://img.shields.io/github/actions/workflow/status/matiaskotlik/async-firebase-rest-api/tests.yml?label=tests&logo=Pytest">
   </a>

   <a href="https://async-firebase-rest-api.readthedocs.io/en/latest/">

      <img alt="Read the Docs" src="https://img.shields.io/readthedocs/async-firebase-rest-api?logo=Read%20the%20Docs&logoColor=white">

   </a>
   <a href="https://codecov.io/gh/matiaskotlik/async-firebase-rest-api"> 
      <img alt="CodeCov" src="https://codecov.io/gh/matiaskotlik/async-firebase-rest-api/branch/main/graph/badge.svg?token=N7TE1WVZ7W"> 
   </a>

</div>

<div align="center">
   <a href="https://pypi.org/project/async-firebase-rest-api/"> 
      <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/async-firebase-rest-api?logo=python">
   </a>
   <a href="https://pypi.org/project/async-firebase-rest-api/"> 
      <img alt="PyPI" src="https://img.shields.io/pypi/v/async-firebase-rest-api?logo=PyPI&logoColor=white">
   </a>
</div>



## Installation

```shell
pip install async-firebase-rest-api
```


## Quick Start

In order to use this library, you first need to go through the following steps:

1. Select or create a Firebase project from [Firebase](https://console.firebase.google.com) Console.

2. Register an Web App.


### Example Usage

```python
# Import Async Firebase REST API library
import firebase

# Firebase configuration
config = {
   "apiKey": "apiKey",
   "authDomain": "projectId.firebaseapp.com",
   "databaseURL": "https://databaseName.firebaseio.com",
   "projectId": "projectId",
   "storageBucket": "projectId.appspot.com",
   "messagingSenderId": "messagingSenderId",
   "appId": "appId"
}

# Instantiates a Firebase app
app = firebase.initialize_app(config)


# Firebase Authentication
auth = app.auth()

# Create new user and sign in
await auth.create_user_with_email_and_password(email, password)
user = await auth.sign_in_with_email_and_password(email, password)


# Firebase Realtime Database
db = app.database()

# Data to save in database
data = {
   "name": "Robert Downey Jr.",
   "email": user.get('email')
}

# Store data to Firebase Database
await db.child("users").push(data, user.get('idToken'))


# Firebase Storage
storage = app.storage()

# File to store in storage
file_path = 'static/img/example.png'

# Store file to Firebase Storage
await storage.child(user.get('localId')).child('uploaded-picture.png').put(file_path, user.get('idToken'))
```
