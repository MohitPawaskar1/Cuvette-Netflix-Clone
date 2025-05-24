from flask import Flask, render_template

app = Flask(__name__)

# Sample movie data
movies = [
    {
        'title': 'Inception',
        'image': 'inception.jpg',
        'trailer': 'https://www.youtube.com/watch?v=YoHD9XEInc0'
    },
    {
        'title': 'Interstellar',
        'image': 'interstellar.jpg',
        'trailer': 'https://www.youtube.com/watch?v=zSWdZVtXT7E'
    },
    {
        'title': 'The Dark Knight',
        'image': 'dark_knight.jpg',
        'trailer': 'https://www.youtube.com/watch?v=EXeTwQWrcwY'
    }
]

@app.route("/")
def home():
    return render_template("index.html", movies=movies)

if __name__ == "__main__":
    app.run(debug=True)
