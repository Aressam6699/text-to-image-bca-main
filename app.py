from flask import Flask, request, jsonify, render_template, flash, url_for, redirect, send_file
import os
from werkzeug.utils import secure_filename
from PIL import Image, ImageDraw
import pandas as pd
import uuid
import zipfile
import shutil
# from os import listdir
# from os.path import isfile, join
import glob
# UPLOAD_FOLDER = 
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app = Flask(__name__) #Initialize the flask App

def handler(func, path, exc_info): 
    print("Inside handler") 
    print(exc_info) 

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/convert', methods=['GET', 'POST'])
def convert():
    unique_filename = str(uuid.uuid4())
    path = r'downloads_' + unique_filename
    if request.method == "POST":
        if request.files:
            file = request.files['file1'] #remove secure filename later
            print(file)
            xls = pd.ExcelFile(file)
            print(xls)

            sheetX = xls.parse(0) #2 is the sheet number+1 thus if the file has only 1 sheet write 0 in paranthesis

            var1 = sheetX['Question']
            var2 = sheetX['option A']
            var3 = sheetX['option B']
            var4 = sheetX['option C']
            var5 = sheetX['option D']

            #print(len(var1)) #1 is the row number.
            #print(var1,"\t",var2,"\t",var3,"\t",var4,"\t",var5)
            W, H = (400,300)
            if not os.path.exists(path):
                os.makedirs(path)
            # print("\n===============\n\n")
            # print(path)
            # print("\n\n===============\n")

            for i in range(len(var1)):        
                msg = str(var1[i])
                im = Image.new("RGBA",(W,H),"white")
                draw = ImageDraw.Draw(im)
                w, h = draw.textsize(msg)
                draw.text(((W-w)/2,(H-h)/2), msg, fill="black")
                #im.save(str(i+1)+"Question."+str(i+1)+") "+str(var1[i])+".png", "PNG")
                im.save(path+"/"+str(i+1)+"_0Question.png","PNG")    
                msg = str(var2[i])
                im = Image.new("RGBA",(W,H),"white")
                draw = ImageDraw.Draw(im)
                w, h = draw.textsize(msg)
                draw.text(((W-w)/2,(H-h)/2), msg, fill="black")
                im.save(path+"/"+str(i+1)+"_1OptionA.png","PNG")
                #im.save(str(i+1)+"Question"+str(i+1)+" Answers/OptionA.png", "PNG")
                msg = str(var3[i])
                im = Image.new("RGBA",(W,H),"white")
                draw = ImageDraw.Draw(im)
                w, h = draw.textsize(msg)
                draw.text(((W-w)/2,(H-h)/2), msg, fill="black")
                im.save(path+"/"+str(i+1)+"_2OptionB.png","PNG")
                #im.save(str(i+1)+"Question"+str(i+1)+" Answers/OptionA.png", "PNG")
                msg = str(var4[i])
                im = Image.new("RGBA",(W,H),"white")
                draw = ImageDraw.Draw(im)
                w, h = draw.textsize(msg)
                draw.text(((W-w)/2,(H-h)/2), msg, fill="black")
                im.save(path+"/"+str(i+1)+"_3OptionC.png","PNG")
                #im.save(str(i+1)+"Question"+str(i+1)+" Answers/OptionA.png", "PNG")
                msg = str(var2[i])
                im = Image.new("RGBA",(W,H),"white")
                draw = ImageDraw.Draw(im)
                w, h = draw.textsize(msg)
                draw.text(((W-w)/2,(H-h)/2), msg, fill="black")
                im.save(path+"/"+str(i+1)+"_4OptionD.png","PNG")
                #im.save(str(i+1)+"Question"+str(i+1)+" Answers/OptionA.png", "PNG")

    return render_template('index.html', path=path)


@app.route('/download', methods=["GET","POST"])
def download_file():
    path = str(request.form['download'])
    onlyfiles = glob.glob(path+"/*.png")
    #onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    with zipfile.ZipFile(path+".zip",'w',compression=zipfile.ZIP_DEFLATED) as my_zip:
        for i in onlyfiles[::-1]:
            my_zip.write(i)
    #return path
    #path = "sample.txt"
    res = send_file(path+".zip", as_attachment=True)
    shutil.rmtree(path, onerror = handler)
    os.remove(path+".zip")
    return res
# xls = pd.ExcelFile("samplequestion.xls")




#return render_template('index.html', **locals())

if __name__ == "__main__":
    app.run(debug=True)