from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the Flask application if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True, port=8081)
