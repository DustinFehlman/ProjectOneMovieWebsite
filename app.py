import movie
import fresh_tomatoes
# Main app file. Creates movies to be shown on webpage. Movies are loaded into
# a list and passed to fresh_tomatoes fucntion. 
fight_club = movie.Movie(550, "https://www.youtube.com/watch?v=SUXWAEX2jlg")
star_wars = movie.Movie(11, "https://www.youtube.com/watch?v=nywPf1p-BBY")
casino = movie.Movie(524, "https://www.youtube.com/watch?v=EJXDMwGWhoA")
forest_gump = movie.Movie(13, "https://www.youtube.com/watch?v=bLvqoHBptjg")
kill_bill = movie.Movie(24, "https://www.youtube.com/watch?v=7kSuas6mRpk")
gattaca = movie.Movie(782, "https://www.youtube.com/watch?v=hWjlUj7Czlk")
movie_list = [fight_club, star_wars, casino, forest_gump, kill_bill, gattaca]
fresh_tomatoes.open_movies_page(movie_list)
