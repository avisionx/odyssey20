from flask import Flask, render_template, request, jsonify, abort
from data import eventsData

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

@app.route("/api/<path:path>")
def dataApi(path):
    return jsonify(eventsData[path])

@app.route("/<path:categ>/<int:idE>")
def event(categ, idE):
    for i in range(len(eventsData[categ])):
        if(idE == eventsData[categ][i]['id']):
            return render_template('event.html', eventTypeLink=str(categ), event=eventsData[categ][i])
    abort(404)

@app.route("/privacy-policy/")
def policy():
    return render_template('policy.html')

# @app.route("/sponsors/")
# def sponsors():
#     return render_template('sponsors.html')

# @app.route("/team/")
# def team():
#     return render_template('team.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if(__name__ == "__main__"):
    app.run(host='0.0.0.0', port=8083)
