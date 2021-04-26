from src import create_app


def init_app():
    print("Martial Art Manager started!")
    return create_app()


app = init_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

