# -*- coding: utf-8 -*-
"""Base_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1803JRGW_rRXiWAipBBw1tVsbGLwj9kvm
"""

!pip install goto-statement

# import igraph as ig
import json
import urllib.request
import numpy as np
import scipy.stats
import operator
from random import randint
from goto import with_goto
alpha = 0.2
NOQ = 0
Questions_asked = []
Answers_given = []
no_of_questions_asked = 0

def Layer1(eras_dict,birth_date):
  global NOQ
  global no_of_questions_asked

  years = list(map(int, eras_dict.keys())) 
  era_min = min(years)-(min(years)%10)
  era_max = max(years)-(max(years)%10)

  # birth_year = int(birth_date[0:])
  # probability_scores_eras = []

  eras = []
  i = era_min

  era_wise_movies = []
  final_movies = set()
  
  while i < era_max+10:
    # temp_score = 0
    # count_movies = 0
    limit = i + 10
    eras.append(i)
    movies_set = set()
    
    while i < limit :
      # temp_score += scipy.stats.norm(birth_year+20,10).pdf(i)
      if i in years :
        movies = list(eras_dict[str(i)])
        movies_set.update(movies)
        final_movies.update(movies)
        # count_movies+= len(movies)
      i+=1
    
    era_wise_movies.append(movies_set)


  for i in range(no_of_questions_asked):
    index = randint(0,len(eras)-1)
    question = "Is the movie from " + str(eras[index]) + "s era ? Y/N/M :"
    if question not in Questions_asked:  
      Questions_asked.append(question)
      NOQ+=1
      choice = input(question)
      Answers_given.append(choice.lower())
      if choice.lower() == 'n':
        final_movies = final_movies.difference(era_wise_movies[index])

      elif choice.lower() == 'y':
        final_movies = era_wise_movies[index]
        break
      elif choice.lower() == 'm':
        continue
      else:
        print("Incorrect Code")
        exit()
      
  return list(final_movies)

def Layer2(file,movies,file3):
  global NOQ
  global no_of_questions_asked
  
  genre_list = []
  for i in movies:
    genre_list.extend(file3[str(i)]["genre_new"])

  genre_list = list(set(genre_list))

  for i in range(min(no_of_questions_asked,len(genre_list))):

    index = randint(0,len(genre_list)-1)
    question = "Is "+str(genre_list[index])+" the genre of your movie ?\n Yes/No/Maybe : "
    if question not in Questions_asked:  
      Questions_asked.append(question)
      NOQ+=1
      choice = input(question)
      Answers_given.append(choice.lower())     
      if choice.lower() == 'y':
        new_movie = list((set(file["genre_new"][str(genre_list[index])])).intersection(set(movies)))
        return new_movie
      
      elif choice.lower() == 'n':
        movies = list((set(movies).difference(set(file["genre_new"][str(genre_list[index])]))))
        genre_list = []
        for i in movies:
          genre_list.extend(file3[str(i)]["genre_new"])
        genre_list = list(set(genre_list))
        
      elif choice.lower() == 'm':
        continue        
      else:
        break

  return movies

def Layer3(file,movies,file3):
  global NOQ
  global no_of_questions_asked
  
  genre_list = []
  for i in movies:
    genre_list.extend(file3[str(i)]["subject_new"])

  genre_list = list(set(genre_list))

  for i in range(min(no_of_questions_asked,len(genre_list))):

    index = randint(0,len(genre_list)-1)
    question = "Is "+str(genre_list[index])+" the subject of your movie ?\n Yes/No/Maybe : "
    if question not in Questions_asked:  
      Questions_asked.append(question)
      NOQ+=1
      choice = input(question)
      Answers_given.append(choice.lower())
      if choice.lower() == 'y':
        new_movie = list((set(file["subject_new"][str(genre_list[index])])).intersection(set(movies)))
        return new_movie
      
      elif choice.lower() == 'n':
        movies = list((set(movies).difference(set(file["subject_new"][str(genre_list[index])]))))
        genre_list = []
        for i in movies:
          genre_list.extend(file3[str(i)]["subject_new"])
        genre_list = list(set(genre_list))
        
      elif choice.lower() == 'm':
        continue        
      else:
        break

  return movies

def Layer4(file,movies,file3):
  global NOQ
  global no_of_questions_asked
  
  genre_list = []
  
  for i in movies:
    genre_list.extend(file3[str(i)]["starring"])

  genre_list = list(set(genre_list))

  for i in range(min(no_of_questions_asked,len(genre_list))):

    index = randint(0,len(genre_list)-1)
    question = "Is "+str(genre_list[index])+" an actor of your movie ?\n Yes/No/Maybe : "
    if question not in Questions_asked:  
      Questions_asked.append(question)
      NOQ+=1
      choice = input(question)
      Answers_given.append(choice.lower())
      if choice.lower() == 'y':
        new_movie = list((set(file["starring"][str(genre_list[index])])).intersection(set(movies)))
        return new_movie
      
      elif choice.lower() == 'n':
        movies = list((set(movies).difference(set(file["starring"][str(genre_list[index])]))))
        genre_list = []
        for i in movies:
          genre_list.extend(file3[str(i)]["starring"])
        genre_list = list(set(genre_list))
        
      elif choice.lower() == 'm':
        continue        
      else:
        break

  return movies

def Layer5(file,movies,file3):
  global NOQ
  global no_of_questions_asked
  
  genre_list = []
  for i in movies:
    genre_list.extend(file3[str(i)]["director"])

  genre_list = list(set(genre_list))

  for i in range(min(no_of_questions_asked,len(genre_list))):

    index = randint(0,len(genre_list)-1)
    question = "Is "+str(genre_list[index])+" the director of your movie ?\n Yes/No/Maybe : "
    if question not in Questions_asked:  
      Questions_asked.append(question)
      NOQ+=1
      choice = input(question)
      Answers_given.append(choice.lower())
      if choice.lower() == 'y':
        new_movie = list((set(file["director"][str(genre_list[index])])).intersection(set(movies)))
        return new_movie
      
      elif choice.lower() == 'n':
        movies = list((set(movies).difference(set(file["director"][str(genre_list[index])]))))
        genre_list = []
        for i in movies:
          genre_list.extend(file3[str(i)]["director"])
        genre_list = list(set(genre_list))
        
      elif choice.lower() == 'm':
        continue        
      else:
        break

  return movies

def Layer6(file,movies,file3):
  
  global NOQ
  global no_of_questions_asked

  genre_list = []
  for i in movies:
    genre_list.extend(file3[str(i)]["musicComposer"])

  genre_list = list(set(genre_list))

  for i in range(min(no_of_questions_asked,len(genre_list))):

    index = randint(0,len(genre_list)-1)
    question = "Is "+str(genre_list[index])+" the music composer of your movie ?\n Yes/No/Maybe : "
    if question not in Questions_asked:  
      Questions_asked.append(question)
      NOQ+=1
      choice = input(question)
      Answers_given.append(choice.lower())
      if choice.lower() == 'y':
        new_movie = list((set(file["musicComposer"][str(genre_list[index])])).intersection(set(movies)))
        return new_movie
      
      elif choice.lower() == 'n':
        movies = list((set(movies).difference(set(file["musicComposer"][str(genre_list[index])]))))
        genre_list = []
        for i in movies:
          genre_list.extend(file3[str(i)]["musicComposer"])
        genre_list = list(set(genre_list))
        
      elif choice.lower() == 'm':
        continue        
      else:
        break

  return movies

def random_questioning(movies,file,file3):
  global no_of_questions_asked
  options = {2 : Layer2,
             3 : Layer3,
             4 : Layer4,
             5 : Layer5,
             6 : Layer6}
  used = []
  for i in range(0,3):
    key=randint(2, 6)
    while key in used :
      key=randint(2, 6)
    no_of_questions_asked=1
    movies = options[key](file,movies,file3)
    
  return movies

def trace(movie_val,file3):
#   print(len(Questions_asked),len(Answers_given))
  print("Trace of your responses :")
  print("Questions asked                                  Responses Given")
  print("----------------------------------------------------------------")
  for i in range(len(Questions_asked)):
    print(Questions_asked[i]+"                         "+Answers_given[i])
    
  print("Correct Answers are:")
  print("Era :",file3[movie_val]['release_year'])
  print("Genre :",file3[movie_val]['genre_new'])
  print("Subject :",file3[movie_val]['subject_new'])
  print("Actor :",file3[movie_val]['starring'])
  print("Director :",file3[movie_val]['director'])
  print("Music Director :",file3[movie_val]['musicComposer'])

@with_goto
def main():
  
  global no_of_questions_asked
  global NOQ
  
  while(True):

    choice = input("Do you want to play 20Q-Game ? Y/N :")
    if choice.lower() == 'y':
      Questions_asked.clear()
      Answers_given.clear()
      NOQ = 0
    
      birth_date = input("Please enter your Birthyear in YYYY format :")
    
      with open('filtered_data_to_movie.json','r') as json_file:  
        file2 = json.load(json_file)
      with open('filtered_movie_to_data.json','r') as json_file:  
        file3 = json.load(json_file)

      primary_keys = list(file2.keys())

      eras = file2['release_year']
      no_of_questions_asked = 1
      movies = Layer1(eras,birth_date)

      if len(movies)>5:
        no_of_questions_asked = 1
        movies = Layer2(file2,movies,file3)
        # print(len(movies))
      if len(movies)>5:
        no_of_questions_asked = 1
        movies = Layer3(file2,movies,file3)
        # print(len(movies))
      if len(movies)>5:
        no_of_questions_asked = 2
        movies = Layer4(file2,movies,file3)
        # print(len(movies))
      if len(movies)>5:
        no_of_questions_asked = 1
        movies = Layer5(file2,movies,file3)
        # print(len(movies))
      if len(movies)>5:
        no_of_questions_asked = 1
        movies = Layer6(file2,movies,file3)
        # print(len(movies))

      label .jump

      if 0 < len(movies) <= 5 :

        print("Most Probable guess for the movies are :")
        print(len(Questions_asked))
        for i in movies:
          print(file3[i]["label"])

        Next_choice = input("Is your movie in the given list ? Y/N :")

        if Next_choice.lower() == 'y':
          print("Thanks for playing")          
        else:
          print("You entered an incorrect choice somewhere !!!")
          
          movie_val = int(input("Enter the index of the correct movie :"))
          movie_val = str(movie_val - 1)
                     
          trace(movie_val,file3)
          
      elif len(movies) > 5:

        print("Most Probable guess for the movies are :")

        for i in movies[0:5]:
          print(file3[str(i)]["label"])

        Next_choice = input("Is your movie in the given list ? Y/N :")

        if Next_choice.lower() == 'y':
          print("Thanks for playing")
        else:
          movies = set(movies).difference(set(movies[0:5]))
          movies = list(movies)
          
          if NOQ<20:
            movies = random_questioning(movies,file2,file3)
            goto .jump

          else:
            print("We give up !!!!")
            print(len(Questions_asked))
            movie_val = int(input("Enter the index of the correct movie :"))
            movie_val = str(movie_val - 1)
                 
      else:
        print("Does this movie really exist !!, I Don't know any such movie")
    else:
      break

main()

# def count():
#   c_dict={}
#   c_dict['count'] = 0
#   with open('count.json', 'w') as fp:                    #write_in_layer2
#      json.dump(c_dict, fp, sort_keys=True, indent=4)
# count()

# def all_Layer_prob_dump(file):
#   all_layer = ['release_year','genre_new','subject_new','starring','director','musicComposer']
#   json_filename = ['layer1_prob','layer2_prob','layer3_prob','layer4_prob','layer5_prob','layer6_prob'] 
  
#   for a in range(len(all_layer)):
#     genre_list = list(file[all_layer[a]])
#     layer_prob={}
#     for i in genre_list:
#       current_keys = list(layer_prob.keys())
#       if i not in current_keys: 
#         layer_prob[str(i)]=0.0

#     json_name=json_filename[a]+".json"
#     with open(json_name, 'w') as fp:                
#         json.dump(layer_prob, fp, sort_keys=True, indent=4)