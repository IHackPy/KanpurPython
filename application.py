from flask import Flask,render_template,request,redirect

app = Flask(__name__)
mail = []
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/learn")
def learn():
    return render_template("learn.html")

@app.route("/join",methods=['POST','GET'])
def join():
    if request.method == 'POST':
        a = request.form.get('mail')
        if a:
            mail.append(a)
            return redirect("/success")
        else:
            return ("Please enter a valid email address")
    else:
        return render_template("join.html")

@app.route("/success")
def clear():
    return render_template("success.html",mails = mail)

if __name__=='__main__':
    app.run(debug=True)
