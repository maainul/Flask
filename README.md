# Flask
### Configure Environment
```
   1.pip install virtualenv
   2.sudo apt-get install virtualenv
Create Folder :
   3.mkdir newproj
   4.cd newproj
   5.virtualenv venv
   6. source venv/bin/activate or . venv/bin/activate
```











```.py
#Importing flask module in the project is mandatory
from flask import Flask
app = Flask(__name__)#name is as arguments

@app.route('/')
#which tells the application which URL should call the associated function.
#app.route(rule,options)
#Rule parameter represent the url binding
#Options is list of parameter to be forwared to the underlying Rule object.
def hello_world():
   return  'hello world'
if __name__ == '__main__':
   app.run()#Run method of Flask class runs the applications on the local development server
```
