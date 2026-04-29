from app import create_app

app = create_app()

# Debug can be turned to True in development but False in Production
# For the sake of the project we can keep it True
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)
