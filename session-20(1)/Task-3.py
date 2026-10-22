# Create a Movie class with a private attribute _rating (float between 0 and 10). Write getter and setter methods for _rating. The setter should only allow values between 0 and 10; if an invalid value is given, print an error message.Do not allow direct access to _rating outside the class.

class Movie:
    def __init__(self, name, rating):
        self._name = name
        self._rating = rating
    
    def get_rating(self):
        return self._rating
    
    def set_rating(self, rating):
        if 0 <= rating <= 10:
            self._rating = rating
        else:
            print("Invalid rating")

my_movie = Movie("Movie 1", 10)
print(my_movie.get_rating())
my_movie.set_rating(20) # This will print "Invalid rating"
print(my_movie.get_rating())
