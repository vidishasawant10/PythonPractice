import random

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

#loop 40 times and print the number of the loop times 2. ex 2,4,6,8

for number in range(40):
    print((number+1)*2)

cats = {"Jane": 14, "Cat": 5, "Tom": 8}

cats["Wilson"] = 1 # to add to the dict
print(cats)
del(cats["Tom"]) #to delete specific keyvalue pair

print (cats)
print(len(cats))

students = {1:True, 2: False}
val = random.randint(1,2)

if val == 1:
    print(students[1])
elif val ==2 :
    print(students[2])
