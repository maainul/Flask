from flask  import Flask
app=Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s'%name

@app.route('/post/<int:post_id>')
def show_post(post_id):
   return "post id %s" %post_id

if __name__ == '__main__':
    app.run(debug=True)
