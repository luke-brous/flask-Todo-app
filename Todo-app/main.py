from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def homePage():




    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)
