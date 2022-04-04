import requests

class TheMovieDb:
    def __init__(self):
        self.api_url="https://api.themoviedb.org/3"
        self.api_key="e8a9d5f82d78ca210c8076d648685cl2"

    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

movieApi= TheMovieDb()

while True:
    secim = input("1-Popular Moviews\n2-Exit\nSeçim: ")

    if secim == "2":
        break
    else:
        if secim =="1":
            movies = movieApi.getPopulars()
            for movie in movies['results']:
                print(movies['title'])
