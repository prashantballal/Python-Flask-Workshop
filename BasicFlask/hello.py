from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def index():
          name="prashant"
          list=[1,2,4]
          return render_template('tmp.html', name=name, list=list)

if __name__=='__main__':
          app.run(debug=True)
