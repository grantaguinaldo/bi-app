from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/is_alive')
def hello_world():
    return 'Yes, I am alive!!!'

@app.route('/upper')
def mapUpper():
    return render_template('upper75.html')

@app.route('/lower')
def mapLower():
    return render_template('lower50.html')

if __name__ == "__main__":
    app.run(debug=True)