# 1. Import Flask
from flask import Flask

# 2. Create an app instance
app = Flask(__name__)

# 3. Define index route
@app.route('/')
def hello_world():
    return 'Hello world'

# 4. Define the about route


# 5. Define the contact route


# 6. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
