from flask import Flask, request, url_for, redirect, render_template,send_file
from generator import Report1,Report2,Report3,Report4
import os

app=Flask(__name__)

@app.route("/", methods=['GET','POST'])
def layout():
    return render_template("layout.html")

@app.route("/r1", methods=['GET','POST'])
def r1():
    return render_template("r1.html")

@app.route("/r2", methods=['GET','POST'])
def r2():
    return render_template("r2.html")

@app.route("/r3", methods=['GET','POST'])
def r3():
    return render_template("r3.html")

@app.route("/r4", methods=['GET','POST'])
def r4():
    return render_template("r4.html")

@app.route("/data_r1", methods=['GET','POST'])
def data_r1():
    opts=Report1(request.args)
    filename1=opts.generate()
    if(filename1=='No Data'):
        return redirect(url_for('dataerror'))
    filepath=os.path.join('static','reports',filename1)
    return send_file(filepath,attachment_filename=filename1)
    return redirect(url_for('r1'))

@app.route("/data_r2", methods=['GET','POST'])
def data_r2():
    opts=Report2(request.args)
    filename1=opts.generate()
    if(filename1=='No Data'):
        return redirect(url_for('dataerror'))
    filepath=os.path.join('static','reports',filename1)
    return send_file(filepath,attachment_filename=filename1)
    return redirect(url_for('r2'))

@app.route("/data_r3", methods=['GET','POST'])
def data_r3():
    opts=Report3(request.args)
    filename1=opts.generate()
    if(filename1=='No Data'):
        return redirect(url_for('dataerror'))
    filepath=os.path.join('static','reports',filename1)
    return send_file(filepath,attachment_filename=filename1)
    return redirect(url_for('r3'))

@app.route("/data_r4", methods=['GET','POST'])
def data_r4():
    opts=Report4(request.args)
    filename1=opts.generate()
    if(filename1=='No Data'):
        return redirect(url_for('dataerror'))
    filepath=os.path.join('static','reports',filename1)
    return send_file(filepath,attachment_filename=filename1)
    return redirect(url_for('r4'))

@app.route("/dataerror", methods=['GET','POST'])
def dataerror():
    return render_template("dataerror.html")

if(__name__=="__main__"):
    app.run(host="0.0.0.0",debug=False)
