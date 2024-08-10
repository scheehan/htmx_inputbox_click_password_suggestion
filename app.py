from flask import Flask, render_template, render_template_string, request

from PySecretsGen import passwd

app = Flask(__file__)


@app.route("/", methods=['GET'])
@app.route("/submit", methods=['POST'])
def index():
    
    if request.method == 'POST':
        subdata = request.form.get('value_key')
        
        return render_template('result.html', subdata=subdata)
# return main landing page
    return render_template('index.html')



# def submit():
    

    

@app.route("/genpasswd")
def genpasswd():
    
    # generate a random alphanumeric string with special symbol characters without whitespace.  
    mypasswd = passwd(12)
    
    return render_template('input.html', value=mypasswd)
    
    # return render_template_string('''
    #                                 {% block myinput %}
    #                                 <input type="text" id="value_key" value="{{ value }}" hx-get="/genpasswd" hx-trigger="click delay:1s" hx-swap="outerHTML"/>
    #                                 {% endblock %}
    #                             ''', value=mypasswd)


if __name__=="__main__":
    app.run()