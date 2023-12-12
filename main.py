from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    # Przykładowa lista filmów
    movies = [
        {"title": "Film 1", "image_url": "http://placehold.it/300x500"},
        {"title": "Film 2", "image_url": "http://placehold.it/300x500"},
        {"title": "Film 3", "image_url": "http://placehold.it/300x500"},
        {"title": "Film 4", "image_url": "http://placehold.it/300x500"}
    ]
    
    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
