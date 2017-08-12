# RecommendedSystems_movies
This is a Recommended Systems to recommend
  1. similar movies as per user views
  2. movies based on user previous rating
  3. Recommed Highest Rated movies based on the mean rating by all the users.



1 . For Finding out the similar Products , Run find_similar_products.py and get the list of 5 similar movies in realtive to one movie the user has watched . This is mostly used when a user is new and the system has no prior ratings for any movies from the user.

2. For recommending movies based on movie rating from user (movies/genre the user liked), run make_recommendations.py file . Give a particular userId in the console input between 1 - 100 and the system will recommed him similar movies which he has rated high in past.

3. For recommending movies based on movie's average' rating from all users), run find_highest_rated_movies.py file .  This is mostly used when a user is new and the system has no prior ratings for any movies from the user.




Extras:
Initially Run create_review_matrix.py and create_review_matrix_as_csv.py to see the movie reviews for every user for every movies in html or csv format.

References :
https://www.linkedin.com/learning/machine-learning-fundamentals-learning-to-make-recommendations/how-to-handle-first-time-users
