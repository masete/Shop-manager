"""The main method to start my application """
from APP.API.products import start_app

app = start_app()

if __name__ == '__main__':
    app.run(debug=True)
    