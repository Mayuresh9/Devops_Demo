from flask import Flask,render_template,request

app = Flask(__name__)




def conversion(from_Unit,to_Unit,value):
    if(from_Unit=="meters"):
    
        if(to_Unit=="meters"):
            val=value
                
        elif (to_Unit=="kilometers"):
            val = value/1000
                
        elif(to_Unit=="miles"):
            val = value*0.000621371
               
        elif(to_Unit=="feet"):
            val = value*3.28084
            
                
    elif(from_Unit=="kilometers"):
            
        if(to_Unit=="meters"):
            val=value*1000
                
        elif (to_Unit=="kilometers"):
            val = value
               
        elif(to_Unit=="miles"):
            val = value*0.621371
                
        elif(to_Unit=="feet"):
            val =value*3280.84
                
                
    elif(from_Unit=="miles"):
            
        if(to_Unit=="meters"):
            val=value*1609.34
                
        elif (to_Unit=="kilometers"):
            val = value*1.60934
                
        elif(to_Unit=="miles"):
            val = value
                
        elif(to_Unit=="feet"):
            val =value*5280
                
                
    elif(from_Unit=="feet"):
            
        if(to_Unit=="meters"):
            val=value*0.3048
                
        elif (to_Unit=="kilometers"):
            val = value*0.0003048
                
        elif(to_Unit=="miles"):
            val = value/5280
                
        elif(to_Unit=="feet"):
            val = value
                
    else:
        pass
    
    return val

def check_valid_input(value):
    if(value < 0):
        return True
    else:
        return False
    


@app.route("/", methods=["POST","GET"])
def Lenth_calculator():
    val=0.00;
    old_val=0.00

    if(request.method=="POST"):
        old_val = float(request.form["fromValue"])
        if(check_valid_input(float(request.form["fromValue"]))):
            return render_template("index.html",content="Invalid_Input",num_enter=old_val)
        else:
            val=conversion(request.form["fromUnit"],request.form["toUnit"],float(request.form["fromValue"]))
            val = round(val,4)
    
    return render_template("index.html",content=val,num_enter=old_val)

if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 80, debug = True)
