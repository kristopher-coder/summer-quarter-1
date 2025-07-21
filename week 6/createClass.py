class Collection: 
    def __init__(self, movelists, gamelist): 
        self.movielist = [] 
        self.gamelist = []
        self.favgame = "" 
        self.faveMovie = "" 

        self.movielist = movelists 
        self.gamelist = gamelist

    def Addgame(self, name):
        if game in self.gamelist:
            print("Game is already in collection")
        else:
            self.gamelist.append(name) 



    def Addmovie(self, name): 
        if game in self.gamelist:
            print("Game is already in collection")
        else:
            self.movielist.append(name) 


    
    def Removegame(self, name): 
        if game in self.gamelist:
            self.gamelist.remove(name)
        else: 
            print("game not found")
    
    
    def Removemovie(self, name): 
        if game in self.gamelist:
            self.movielist.remove(name) 
        else:
            print("Game not found") 



    def DisplayGames(self): 
        for game in self.gamelist: 
            print(game)
    


    def DisplayMovie(self): 
        for movie in self.movielist: 
            print(movie) 



    def DisplayFavGame(self):  
        print(f'Fav Game: {self.favgame}')



    def DisplayFavMovie(self): 
        print(f'Fav movie:  {self.faveMovie}')  


    def DisplayCollection(Self): 
        Self.DisplayGames() 
        Self.DisplayFavGame()
        Self.DisplayMovie()
        Self.DisplayFavMovie() 


    def SetFavMovie(self, movie): 
        if movie not in self.movielist: 
            self.AddMovie(movie) 
        self.favgame = game