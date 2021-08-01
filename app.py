from flask import Flask, render_template
#=========IMPORT===========#
Devil = Flask(__name__)
#=========NAME-APP=========#
@Devil.route('/')
def error():
    return render_template("error.html")
#=============#
if __name__ == '__main__':
    Devil.run(host='127.0.0.1', port=8080, debug=True)
