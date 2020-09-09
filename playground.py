from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play/')
def play():
    return render_template('playground.html', num=int(3))
@app.route('/play/<num>')
def repeatbox(num):
    return render_template('playground.html', num=int(num))
@app.route('/play/<num>/<color>')
def colorandrepeat(num, color):
    return render_template('playground.html', num=int(num), color=str(color))
if __name__ == "__main__":
    app.run(debug=True)