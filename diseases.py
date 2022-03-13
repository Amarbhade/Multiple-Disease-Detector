from flask import Flask,render_template,request,url_for
import pandas as pd
from numpy import asarray
import numpy as np

import pickle

model1=pickle.load(open("kidneydiseas","rb"))
model2=pickle.load(open("cancer.pkl","rb"))
model3=pickle.load(open("thyroid.pkl","rb"))

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("multiple Disease.html")

@app.route("/predict1",methods=["POST","GET"])
def predict1():
    A = float(request.form.get("age"))
    al=float( request.form.get("albu"))
    sugar = request.form.get("sugar")
    puscell=request.form.get("puscell")
    if puscell=="normal":
        PC=1.0
    else:
        PC=0.0
    bac=request.form.get("bac")
    if bac=="NotPresent":
        BC=0
    else:
        BC=1
    blood=float(request.form.get("blood"))
    serus=float(request.form.get("serus"))
    NA=float(request.form.get("NA"))
    K=float(request.form.get("K"))
    HB=float(request.form.get("hb"))
    wbc=float(request.form.get("wbc"))
    rbc=float(request.form.get("rbc"))
    dm=request.form.get("dm")
    if dm=="yes":
        DM=1
    else:
        DM=0

    d1=[A,al,sugar,PC,BC,blood,serus,NA,K,HB,wbc,rbc,DM]
    data1=asarray([d1])

    result=model1.predict(data1)
    if result == 1:
         result="Patient has kidney diseases"
    else:
        result="Patient has not kidney diseases"

    return render_template("kidneycd.html",result=result)

@app.route("/predict2",methods=["POST","GET"])
def breastcancer():
    CT=float(request.form.get("clump_thickness"))
    UC=float(request.form.get("uniform_cell_size"))
    UCS=float(request.form.get("uniform_cell_shape"))
    MA=float(request.form.get("marginal_adhesion"))
    SE=float(request.form.get("single_epithelial_size"))
    BN=float(request.form.get("bare_nuclei"))
    BC=float(request.form.get("bland_chromatin"))
    NN=float(request.form.get("normal_nucleoli"))
    MS=float(request.form.get("mitoses"))

    data2=[CT,UC,UCS,MA,SE,BN,BC,NN,MS]

    d2=asarray([data2])

    result=model2.predict(d2)

    if result==2:
        result="Patient not suffer from breast cancer"
    else:
        result="Patient is suffer from breast cancer"

    return render_template("cancer.html",result=result)

@app.route("/predict3",methods=["POST","GET"])
def thyroid():
    age=float(request.form.get("age"))
    sex=request.form.get("sex")
    if sex=="Female":
        sex=0
    else:
        sex=1
    OT=request.form.get("OT")
    if OT=="False":
        OT=0
    else:
        OT=1
    OA=request.form.get("OA")
    if OA=="False":
        OA=0
    else:
        OA=1
    TS=request.form.get("TS")
    if TS=="False":
        TS=0
    else:
        TS=1
    G=request.form.get("G")
    if G=="False":
        G=0
    else:
        G=0
    T = request.form.get("T")
    if T == "False":
        T = 0
    else:
        T = 0
    H=request.form.get("H")
    if H=="False":
        H=0
    else:
        H=0
    TSH=float(request.form.get("TSH"))
    TT4=float(request.form.get("TT4"))
    T4U=float(request.form.get("T4U"))
    FTI=float(request.form.get("FTI"))

    data=[age,sex,OT,OA,TS,G,T,H,TSH,TT4,T4U,FTI]
    new_data=asarray([data])

    result=model3.predict(new_data)

    if result==1:
        result="Patient Is Not Suffer From Thyroid Disease"
    elif result==0:
        result="Patient Has compensated_hypothyroid"
    elif result==2:
        result="Patient Has primary_hypothyroid"
    else:
        result="secondary_hypothyroid"

    return render_template("thyroidD.html",result=result)



@app.route("/breast")
def cancerpage():
    if request.method=="POST":
        return request(url_for("multiple Disease.html"))
    return render_template("cancer.html")

@app.route("/thyroid")
def thyroidpage():
    if request.method=="POST":
        return request(url_for("multiple Disease.html"))
    return render_template("thyroidD.html")


@app.route("/kidney",methods=["POST","GET"])
def kidneypage():
    if request.method=="POST":
        return request(url_for("multiple Disease.html"))
    return render_template("kidneycd.html")



if __name__=="__main__":
    app.run(debug=True)