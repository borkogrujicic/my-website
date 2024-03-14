from flask import Flask, render_template


app = Flask(__name__)

posts = [
    {
        'author': 'Borisav Grujicic',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'February 29, 2024'
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 5, 2024'  
    }
]

@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")    
def about():
    return render_template('about.html')



if __name__ == '__main__':
    app.run(debug=True)