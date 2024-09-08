# Strong Password Suggestion with HTMX hx-trigger

---

![intro](/images/htmx_password_generator.png)

## Introduction

Users registration often require user to be creative in order to fullfill password requirement on-the-fly. 

This simple web app were to demostrate prove-of-concept (PoC) with Flask as web framework, python function to generate cryptographically strong pseudo-random, and htmx access AJAX in HTML. 

Helps users having difficulty to come up with effective and strong password create strong, unique passwords while try to register their online accounts. Address challeges for users to come up with password during account creation.

Strong password suggestion is to generte passwords that are enhances the security of your online accounts. in turn, helps prevent common security issues like using weak passwords or reusing the same password across multiple sites. This reduces the risk of your accounts being compromised and increase difficulty for hackers to guess or crack.

## Features

- htmx trigger 
- password generator

## How it works

The problem try to address were randomise cryptographic token whenever a request triggered. Typical users account creation often from web sites. Thus, Demonstration uses web framework Flask to rander web input box html elements for password input, after password string submitted, received password will be display within a div tag html element.

[Flask][2] is a Web application framework allow to develop web applications easily with python code. Coupled together with web template engine [jinja2][3] to render a dynamix web page. 

Randomise cryptographic token needs to be dynamically generated and replace html element data. Thus, uses htmx and Jinja2 to dynamically trigger action and replace html element data.

[htmx][1] gives you access to AJAX, CSS Transitions, WebSockets and Server Sent Events directly in HTML, using attributes, so you can build modern user interfaces with the simplicity and power of hypertext

In short, user needs to hold down Ctrl key and left mouse click to trigger password request.

### Simple Web application

Objective were to allow users to trigger strong password request whenever needed with a simple ctrl + left mouse click. User got the choice to use suggested password or input prefer password.

![web UI](/images/web_UI_interface.png)

## Code Walkthrough

```python
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <script src="{{ url_for('static', filename='js/htmx.min.js') }}"></script>

    <title>Click to generate strong password</title>
</head>
```

[pySecureTokenGenerator][4] python function serve as backend strong password generator

generate a random alphanumeric string with special symbol characters without whitespace. 
at least one lowercase character, at least one uppercase character, at least one special symbol character and at least three digits

```python
from PySecretsGen import passwd

@app.route("/genpasswd")
def genpasswd():
    
    mypasswd = passwd(12)
    
    return render_template('input.html', value=mypasswd)
```

HTMX library access AJAX features directly from HTML

```python
<form action="/submit" hx-target="#value_key" hx-swap="outerHTML" autocomplete="off" method="post" >

```

```python
<input type="text" name="value_key" id="value_key" value="{{ value }}" hx-get="/genpasswd" hx-trigger="click[ctrlKey] delay:1s" hx-swap="outerHTML" hx-params="not value_key"/>

```



suggest a random combination of letters, numbers, and special characters. These suggestions are typically designed to meet security best practices, such as including a mix of uppercase and lowercase letters, numbers, and symbols.

web application provides users interface with input box 

Runs a Flask web server for prototyping (Flask is used only for development purposes, it is not meant here to create an API using Flask, but you can do it as well)

## Under your control - finetune cryptographic token based on your requirement

[pySecureTokenGenerator][4] offer 5 type of Cryptographically strong pseudo-random generator

This is a tool to generate cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.

- bytes: Generate a random byte string containing nbytes number of bytes.
- XKCD: Generate an XKCD-style passphrase based upon a simple american dict compressed file.
- hex: Generate a random text string, in hexadecimal.
- urlsafe: Generate a random URL-safe text string, containing nbytes random bytes. The text is Base64 encoded, so on average each byte results in approximately 1.3 characters.
- passwd: Generate a random alphanumeric string with special symbol characters without whitespace.

## Activate virtual environment

```
python -m venv .venv

Windows:
.\.venv\Scripts\activate

Linux & Unix:
source .venv/bin/activate

pip install -r requirements.txt

```
## Clone repository
```python
git clone https://github.com/scheehan/htmx_inputbox_click_password_suggestion
cd htmx_inputbox_click_password_suggestion

flask run --debug
```

[1]: https://htmx.org/
[2]: https://flask.palletsprojects.com/en/3.0.x/
[3]: https://jinja.palletsprojects.com/en/3.1.x/
[4]: https://github.com/scheehan/pySecureTokenGenerator

https://github.com/presprog/contao-password-suggestion
https://github.com/Mohasin-Haque/PasswordSuggestion
https://pythonbasics.org/what-is-flask-python/