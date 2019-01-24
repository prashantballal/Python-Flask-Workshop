from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def index():
          result={'math':80,'c':70,'java':90}
          
          return render_template('table.html', result=result)

if __name__=='__main__':
          app.run(debug=True)
