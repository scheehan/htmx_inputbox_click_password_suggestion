from flask import Flask, render_template, request
from PySecretsGen import passwd

app = Flask(__file__)

# handle landing GET request and submit POST request 
@app.route("/", methods=['GET'])
@app.route("/submit", methods=['POST'])
def index():
    
    # handle POST request
    if request.method == 'POST':
        
        # capture form submitted value_key data
        subdata = request.form.get('value_key')
        
        # return result page
        return render_template('result.html', subdata=subdata)
    
    # return main landing page
    return render_template('index.html')

@app.route("/genpasswd")
def genpasswd():
    
    # generate a random alphanumeric string with special symbol characters without whitespace.  
    mypasswd = passwd(12)
    
    return render_template('input.html', value=mypasswd)



if __name__=="__main__":
    app.run()