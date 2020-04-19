from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
@app.route('/register')
def home():
    return render_template('register.html')

@app.route('/result', methods=['GET','POST'])
def result():
    name = request.form.get("user_name")
    print(name)
    return render_template('result.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)
