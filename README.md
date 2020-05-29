# What to do with your bits&pieces at home?

- Domain: http://134.209.248.77/

# About the Website

"What to do with your bits and pieces at home" is a website which provides you with creative inspirations how to use the stuff you don't need at home. Instead of throwing it away you can Upcycle creative usefull peaces!

# Technologies

HTML, CSS, Python, Flask

# Deployment

- Server: digital ocean
- Handiling requests: NGNIX & Gunicorn

# Get it running locally

Required:

- Python 3.6 
- pip
- requirements from requirements.txt with pip.
- The file run.py is created for running on a server. To get it run on a local machine, make sure to adapt run.py:

```from flaskM import create_app

app = create_app()

if __name__ == "__main__":
    try:
        app.run(port=3000, debug=True)
    except OSError:
        print("OS Error")```

Inside repository execute run.py with python.