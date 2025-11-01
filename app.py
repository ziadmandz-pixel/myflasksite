from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


messages = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        body = request.form.get('message')
        if name and body:
            messages.append({'name': name, 'body': body})
        return redirect(url_for('home'))
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
