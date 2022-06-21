from app import app;
@app.route("/")
def index():
    return "Hello World"

    #register routes
    app.register_blueprint(home)
    return app