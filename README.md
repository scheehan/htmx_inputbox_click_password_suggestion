# Strong Password Suggestion with HTMX hx-trigger click

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


## Flask + Jinja2

Demonstrate how user can interack with web interface

input box 

ctrl + click to 

## htmx

[htmx][1] gives you access to AJAX, CSS Transitions, WebSockets and Server Sent Events directly in HTML, using attributes, so you can build modern user interfaces with the simplicity and power of hypertext

```
form - hx-target="#value_key" hx-swap="outerHTML"

```

```
input - hx-get="/genpasswd" hx-trigger="click delay:1s" hx-swap="outerHTML"
```

## Put everyting together

![web UI](/images/web_UI_interface.png)

Objective were to 
User got the choice to use suggested password or input prefer password.

## Code review

backend password generate tool

```python
@app.route("/genpasswd")
def genpasswd():
    
    # generate a random alphanumeric string with special symbol characters without whitespace.  
    mypasswd = passwd(12)
    
    return render_template('input.html', value=mypasswd)
```

suggest a random combination of letters, numbers, and special characters. These suggestions are typically designed to meet security best practices, such as including a mix of uppercase and lowercase letters, numbers, and symbols.

web application provides users interface with input box 

Runs a Flask web server for prototyping (Flask is used only for development purposes, it is not meant here to create an API using Flask, but you can do it as well)

## How to finetune strong password based on your requirement

[pySecureTokenGenerator][4] offer 5 type of Cryptographically strong pseudo-random generator

This is a tool to generate cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.

- bytes: Generate a random byte string containing nbytes number of bytes.
- XKCD: Generate an XKCD-style passphrase based upon a simple american dict compressed file.
- hex: Generate a random text string, in hexadecimal.
- urlsafe: Generate a random URL-safe text string, containing nbytes random bytes. The text is Base64 encoded, so on average each byte results in approximately 1.3 characters.
- passwd: Generate a random alphanumeric string with special symbol characters without whitespace.

## Project structure:

static:js:htmx.min.js
templates:index.html
templates:input.html
templates:result.html
app.py
PySecretsGen.py

## How to install

```html
git clone https://github.com/scheehan/xxxx
cd xxx

python -m pip install -r requirements.txt

```



[1]: https://htmx.org/
[2]: https://flask.palletsprojects.com/en/3.0.x/
[3]: https://jinja.palletsprojects.com/en/3.1.x/
[4]: https://github.com/scheehan/pySecureTokenGenerator
