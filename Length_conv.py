from flask import Flask,render_template,request

app = Flask(__name__)




@app.route("/", methods=["POST","GET"])
def Lenth_calculator():
    val=0.00;
    old_val=0.00
    
    
    if(request.method=="POST"):
        old_val = float(request.form["fromValue"])
        if(request.form["fromUnit"]=="meters"):
            
            if(request.form["toUnit"]=="meters"):
                val=float(request.form["fromValue"])
                
            elif (request.form["toUnit"]=="kilometers"):
                val = float((request.form["fromValue"]))/1000
                
            elif(request.form["toUnit"]=="miles"):
                val = float((request.form["fromValue"]))*0.000621371
               
            elif(request.form["toUnit"]=="feet"):
                val =float((request.form["fromValue"]))*3.28084
               
               # old_val = float(request.form["fromValue"])
            
            
                
        elif(request.form["fromUnit"]=="kilometers"):
            
            if(request.form["toUnit"]=="meters"):
                val=float(request.form["fromValue"])*1000
                
            elif (request.form["toUnit"]=="kilometers"):
                val = float((request.form["fromValue"]))
               
            elif(request.form["toUnit"]=="miles"):
                val = float((request.form["fromValue"]))*0.621371
                
            elif(request.form["toUnit"]=="feet"):
                val =float((request.form["fromValue"]))*3280.84
                
                
        elif(request.form["fromUnit"]=="miles"):
            
            if(request.form["toUnit"]=="meters"):
                val=float(request.form["fromValue"])*1609.34
                
            elif (request.form["toUnit"]=="kilometers"):
                val = float((request.form["fromValue"]))*1.60934
                
            elif(request.form["toUnit"]=="miles"):
                val = float((request.form["fromValue"]))
                
            elif(request.form["toUnit"]=="feet"):
                val =float((request.form["fromValue"]))*5280
                
                
        elif(request.form["fromUnit"]=="feet"):
            
            if(request.form["toUnit"]=="meters"):
                val=float(request.form["fromValue"])*0.3048
                
            elif (request.form["toUnit"]=="kilometers"):
                val = float((request.form["fromValue"]))*0.0003048
                
            elif(request.form["toUnit"]=="miles"):
                val = float((request.form["fromValue"]))/5280
                
            elif(request.form["toUnit"]=="feet"):
                val =float((request.form["fromValue"]))
                
        else:
            pass
    
    return render_template("index.html",content=val,num_enter=old_val)

if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 80, debug = True)
