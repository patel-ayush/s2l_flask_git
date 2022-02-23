from flask import Flask,session
import os
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from api_call import correct_sent_tc_api
from sign_language_crework import get_word,get_sent,save_uploadedfile

app=Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/',methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    else:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        if request.method == 'POST':
            return fun(filename)
            
            #print('upload_video filename: ' + filename)    
def fun(filename):
    if request.form.get('pred') == 'Predict':
        lab_list=get_word(filename)
        lab=" ".join(lab_list)
        return render_template("upload.html", filename=filename,pred=lab)

def clear(filename):
    if request.form.get('clear') == 'clear':
        #lab_list=get_word(filename)
        #lab=" ".join(lab_list)
        return render_template("upload.html", filename=" ",pred=" ")
    
            
@app.route('/display/<filename>')
def display_video(filename):
    #print('display_video filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename),code=301)

def predict(filename):
    return render_template('upload.html', pred=pred)


if __name__=="__main__":
    app.run(debug=True)
