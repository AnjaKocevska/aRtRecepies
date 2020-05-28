from flaskM import create_app

app = create_app()

if __name__ == "__main__":
    try:
        app.run(port=3000, debug=True)
    except OSError:
        print("OS Error")