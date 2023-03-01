from flask import Flask , render_template
from data import Posts
app = Flask (__name__)
Posts = Posts()
@app.route('/')
def home():
    return render_template ('home.html')


@app.route('/about')
def about():
    return render_template ('about.html')

@app.route('/blogger')
def blogger():
    return render_template ('blogger.html', posts=Posts)



if __name__=='__main__':

    app.run(debug=True)
