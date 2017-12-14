#! /usr/bin/env python3
import psycopg2
DBNAME = "news"


#passing queries in variables as list
query_one = ["""SELECT title,views FROM article_view LIMIT 3 """]
query_two = ["""SELECT name, sum(articles_by_view.views) AS views
            FROM articles_by_author, articles_by_view
            WHERE articles_by_author.title = articles_by_view.title
            GROUP BY name ORDER BY views """]
query_three = ["""   """]

#coverting queries into strings
query_1 = 'query_one'.join(query_one)
query_2 = 'query_two'.join(query_two)
query_3 = 'query_three'.join(query_three)

# query 1
db = psycopg2.connect(database = DBNAME)
conn = db.cursor()
conn.execute(query_1)
results = conn.fetchall()
conn.close()
results

print ("\n 1. What are the most popular three articles of all time? \n")
for result in results:
        print (str(result[0]) + " -> " + str(result[1]) + " views")

# query 2
db = psycopg2.connect(database = DBNAME)
conn = db.cursor()
conn.execute(query_2)
results = conn.fetchall()
conn.close()
results

print ('\n 2. Who are the most popular article authors of all time? \n')
for result in results:
        print ("* " + str(result[0]) + " -> " + str(result[1]) + " views")

# query 3
db = psycopg2.connect(database = DBNAME)
conn = db.cursor()
conn.execute(query_2)
results = conn.fetchall()
conn.close()
results

print ('\n 3. On which days did more than 1% of requests lead to errors? \n')
for result in results:
        print ("* " + str(result[0]) + " -> " + str(result[1]))

if __name__ == "__main__":
    print("This program is being run by it's self")
else:
    print("I am being imported into another module.")
