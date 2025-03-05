from flask import Flask, render_template, url_for
app = Flask(__name__)
post = [
    {
        'author' : 'Jon',
        'title': 'Vlog Post1',
        'Content': 'First Post Content',
        'date_added' :'26_8_20030'
    },
    {
        'author' : 'Vicky',
        'title' : 'Vlog Post2',
        'Content' : 'Second Post Content',
        'date_added' : '29_5_2007'
    }
    ]
@app.route('/')
def hello_world():
    return render_template('primary.html',post = post)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')

if __name__ == "__main__":
    app.run(debug=True)