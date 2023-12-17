import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0NjcwMmU1OWEyNDdlNGVmM2ExMTUyMTIzZTRjMGEzZCIsInN1YiI6IjY1NzgzMDAxYTFkMzMyMDBlMWI4NzMzOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.VwmTFMhumR--qpA2d-YcXBPFMk_pWoCHWGXWEpOO5_w"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0NjcwMmU1OWEyNDdlNGVmM2ExMTUyMTIzZTRjMGEzZCIsInN1YiI6IjY1NzgzMDAxYTFkMzMyMDBlMWI4NzMzOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.VwmTFMhumR--qpA2d-YcXBPFMk_pWoCHWGXWEpOO5_w"

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_backdrop_url(backdrop_path, size="w780"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{backdrop_path}"


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]

def get_movies_list(list_type='popular'):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    data = response.json()
    return data.get('results', []) 
