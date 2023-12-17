from flask import Flask, render_template,request
import tmdb_client

app = Flask(__name__)

AVAILABLE_LISTS = ['popular', 'top_rated', 'upcoming', 'now_playing']

@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', 'popular')
    if selected_list not in AVAILABLE_LISTS:
        selected_list = 'popular'
    movies = tmdb_client.get_movies_list(selected_list)[:8]
    return render_template("homepage.html", movies=movies, current_list=selected_list, available_lists=AVAILABLE_LISTS)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    backdrop_url = tmdb_client.get_backdrop_url(details['backdrop_path'])
    cast = tmdb_client.get_single_movie_cast(movie_id)
    return render_template("movie_details.html", movie=details, backdrop_url=backdrop_url,cast=cast)





if __name__ == '__main__':
    app.run(debug=True)  
    

