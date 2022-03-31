from flask import Flask, render_template

app = Flask('Josh')
# webcode = open('webcode.html').read() - not needed

@app.route('/')
def webprint():
    return render_template('webcode.html') 

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)
