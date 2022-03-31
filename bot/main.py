from flask import Flask, render_template

app = Flask('main')

@app.route('/')
def webprint():
    return render_template('main.html') 

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)
