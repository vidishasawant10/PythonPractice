fav_movies =["Sandlot", "The Lego Movie","Dune"]
print(len(fav_movies))

fav_movies.append("IronMan") # add at end
print(len(fav_movies))

fav_movies.insert(1,"Batman") #add at a specific place

print(fav_movies)
del (fav_movies[2])#delete at a specific place
print(fav_movies)

while len(fav_movies) > 1:
    del (fav_movies[-1])
print(fav_movies)