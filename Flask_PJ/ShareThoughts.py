from flask import Flask, render_template
app = Flask(__name__)


thoughts = [
    {
        'author': 'Oliver',
        'title': 'Thought1',
        'date': '2019-02-18',
        'content': "Hello World"
    },
    {
        'author': 'Mike',
        'title': 'Thought2',
        'date': '2019-02-19',
        'content': "Cool Place!"
    }
]


@app.route("/")
def hello():
    return render_template('home.html', thoughts=thoughts)


if __name__ == '__main__':
    app.run(debug=True)
