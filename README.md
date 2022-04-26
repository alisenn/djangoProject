# Question 1 
## evreka1

`python manage.py makemigrations` -> create migration file from class

`python manage.py migrate` -> creates a table from migration file

I used postgresql database to implement this problem.
Function Returns the requested data in home.html
You need to enter dummy data to test
Jus run the following command

`python manage.py runserver`
When you open the app in browser it will give you the result in json format

# Optimization Suggestion
### Join Decomposition
Insteaad of a single query which django ORM does in default we can write multiple queries that returns the same data 
### Notes
I have implemented this question using MVT design pattern as you can see.

# Question 2
## evreka2




