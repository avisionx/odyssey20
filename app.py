from flask import Flask, render_template, request

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def index():
    savemail = request.args.get('email', default = None)
    if(savemail != None):
        f = open("emails.txt", "a+")
        f.write(savemail + "\n")
        f.close()
    return render_template('index.html')

@app.route("/privacy-policy/")
def policy():
    return render_template('policy.html')

if(__name__ == "__main__"):
    app.run(host='0.0.0.0', port=8083)
