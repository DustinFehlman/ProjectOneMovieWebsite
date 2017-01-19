import json, urllib
# Function that opens an api url to import movie data.
# Takes one argument, which is the ID of a movie from www.themoviedb.org.
# Upon opening url, function will load and return a json object.
def get_movie_data(movie_id):
    url = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "?api_key=66886a46bb1b1cfc593a89b28e79f26c"
    url_response = urllib.urlopen(url)
    movie_data = json.loads(url_response.read())
    return movie_data
