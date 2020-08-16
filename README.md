# Simple template for a Python Flask POST API

<img src = "https://cdn.pixabay.com/photo/2018/04/11/19/48/cloud-3311588_960_720.png" height="100">

This is a template for making a Flask post API in Python.
<br>
For non-backend developers, this is a starting point to start developing APIs in Python's Flask framework.

<h3>How to install Flask?</h3>

```
pip install Flask
```

<h3>How to use this file?</h3>

1. Clone this repo
  
2. Open command line or Terminal on your computer
  
3. Go to the folder where this repo is downloaded

<h3>Choosing between development and production environment to run</h3>
  
i. Enter this if you are working in <b>dev environment or on your local computer:</b>

```
python index.py
```

  ii. Flask is designed to run in debug environment only that that handle request of only one User.<br>
  &nbsp; &nbsp; &nbsp; &nbsp;To make it run in production, we need a dependency called as <b>waitress</b>. <br>
  &nbsp; &nbsp; &nbsp; &nbsp;For <b>production environment</b> enter this:


```
pip install waitress
python index_prod.py 
```

<h3>How to use this API?</h3>

```
Fire this API Request any from front end:

URL - 127.0.0.1:5000/json-example  
Raw JSON Request - {"language":"hindi", "framework":"flask"}
```

Response woule be:

```
{"framework": "flask is robust", "language": "hindi is nice"} 
```

<br>
<i>Use this <b>template file</b> to make any modifiction to the API or to add new APIs</i>
