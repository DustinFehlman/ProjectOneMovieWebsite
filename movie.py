import data_requester
# Movie class to create movie objects.Uses the data requester function to
# load movie properties from www.themoviedb.org.
class Movie():
    def __init__(self, movie_id, youtube_trailer):
        self.movie_id = movie_id
        movie_data = data_requester.get_movie_data(movie_id)
        self.title = movie_data['title']
        self.storyline = movie_data['overview'].encode('utf8')
        self.tagline = movie_data['tagline']
        self.poster_image_url = "https://image.tmdb.org/t/p/w300" + str(movie_data['poster_path'])
        self.trailer_youtube_url = youtube_trailer
        
        
        
        
        
