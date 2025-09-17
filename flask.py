from flask import Flask

# Ek Flask application instance banate hain
app = Flask(__name__)

# Ek route define karte hain jo homepage par chalega
@app.route('/')
def hello():
    return '<h1>Hello World! Jenkins ne deploy kar diya!</h1>'

# Application ko run karne ke liye
if __name__ == '__main__':
    # host='0.0.0.0' zaroori hai taaki server bahar se accessible ho
    app.run(host='0.0.0.0', port=5000)
