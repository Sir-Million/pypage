from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/contacto')
def contato():
    return render_template('contacto.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)