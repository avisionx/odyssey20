from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    savemail = request.args.get('email', default = None)
    if(savemail != None):
        f = open("emails.txt", "a+")
        f.write(savemail + "\n")
        f.close()
    return render_template('index.html')

if(__name__ == "__main__"):
    app.run(host='0.0.0.0', port=8083)
