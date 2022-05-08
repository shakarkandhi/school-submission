from flask import Flask, request, url_for, redirect, render_template,send_file
from generator import Report1
import os

app=Flask(__name__)

@app.route("/", methods=['GET','POST'])
def r1():
    return render_template("r1.html")

@app.route("/data_r1", methods=['GET','POST'])
def data_r1():
    opts=Report1(request.args)
    filename1=opts.generate()
    filepath=os.path.join('static','reports',filename1)
    return send_file(filepath,attachment_filename=filename1)
    return redirect(url_for('r1'))


if(__name__=="__main__"):
    app.run(host="0.0.0.0",debug=False)

