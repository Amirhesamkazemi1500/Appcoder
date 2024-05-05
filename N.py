from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        domain = request.form['domain']
        return render_template('index.php', domain=domain)
    return render_template('index.php')

if __name__ == '__main__':
    app.run(debug=True)
