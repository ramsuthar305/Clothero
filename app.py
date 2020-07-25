from flask import Flask,request, render_template

app = Flask(__name__)
app.config.from_object("config.Config")

@app.errorhandler(404) 
def not_found(e): 
  return render_template("404.html") 

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as error:
        return error

if __name__ == '__main__':
    app.run(debug=True)
    

