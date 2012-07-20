from flask import Flask, request, render_template
import easyblog

app = Flask(__name__)

def calc_splits(tcxfile, split):
    return calc(tcxfile, float(split))

@app.route('/', methods=['GET'])
def blog():
    entries = easyblog.entries()
    return render_template('blog.html', entries=entries)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
