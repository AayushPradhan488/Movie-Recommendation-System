#func 1: create DB
#func 2: manage folders/directories
#func 3: insert data
#func 4: delete data
#func 5: return data
#func 6: fetch invoice number

import sqlite3
import pandas as pd
import csv

print('Start program...')

def con_cur():
    con=sqlite3.connect("db.sqlite3")
    cur=con.cursor()
    return con,cur

def MoviesDB():
    con,cur=con_cur()
    
    query='''CREATE TABLE website_movie (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      title VARCHAR(255),
      genre VARCHAR(255),
      director VARCHAR(255),
      year INT,
      rating DECIMAL(3,1),
      image VARCHAR(255)
    );'''
    cur.execute(query)
    con.commit()
    con.close()

def insert_values(title='NULL',genre='NULL',director='NULL',year='NULL',rating='NULL',image='NULL'):
    con,cur=con_cur()
    cur.execute("INSERT INTO website_movie VALUES (NULL,?,?,?,?,?,?)",(title,genre,director,year,rating,image))
    con.commit()
    con.close()

def delete_values(id):
    con,cur=con_cur()
    query="DELETE FROM website_movie WHERE ID="+str(id)
    cur.execute(query)
    con.commit()
    con.close()

def get_all_records():
    con,cur=con_cur()
    query="SELECT * FROM website_movie"
    cur.execute(query)
    rows=cur.fetchall()
    con.commit()
    con.close()
    return rows

def csv_to_DB():
    #df = pd.read_csv('imdb_top_1000.csv',header=0,usecols=['Series_Title','Genre','Director','Released_Year','IMDB_Rating'])
    #print(type(df))
    with open('imdb_top_1000.csv','r',encoding='utf-8',errors='ignore') as f:
        dataset = csv.reader(f)
        next(dataset)
        suc=0;fail=0
        for i in dataset:
            try:
                insert_values(i[1],i[5],i[9],i[2],i[6],'some_poster_image')
                suc+=1
            except sqlite3.IntegrityError:
                print('sqlite3.IntegrityError')
                print(i[1],i[5],i[9],i[2],i[6],sep='  |  ')
                fail+=1
            except sqlite3.OperationalError as e:
                print('sqlite3.OperationalError',e)
                print(i[1],i[5],i[9],i[2],i[6],sep='  |  ')
                fail+=1
            except sqlite3.ProgrammingError:
                print('sqlite3.ProgrammingError\nSyntax error in swl query')
                print(i[1],i[5],i[9],i[2],i[6],sep='  |  ')
                fail+=1
            except:
                print('Some other error')
                fail+=1
        print('\nLoop terminated...\n\nSuccess =',suc,'\nFail =',fail)

csv_to_DB()
#MoviesDB()
#insert_values(1,'The Shawshank Redemption', 'Drama', 'Frank Darabont', 1994, 9.3, 'shawshank_redemption.jpg')
#insert_values(2,'The Godfather', 'Crime', 'Francis Ford Coppola', 1972, 9.2, 'godfather.jpg')
#insert_values(3,'The Dark Knight', 'Action', 'Christopher Nolan', 2008, 9.0, 'dark_knight.jpg')
#insert_values(4,'3 Idiots', 'Crime, Drama', 'Amir Khan', 2008, 9.0, '3_idiots.jpg')
#delete_values(4)
#print(*get_all_records(),sep='\n')
#con,cur=con_cur()
#cur.execute("DROP TABLE movies")
#con.commit()
#con.close()

'''
CREATE TABLE movies (
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(255),
  genre VARCHAR(255),
  director VARCHAR(255),
  year INT,
  rating DECIMAL(3,1),
  image VARCHAR(255)
);

INSERT INTO movies (title, genre, director, year, rating, image) VALUES
('The Shawshank Redemption', 'Drama', 'Frank Darabont', 1994, 9.3, 'shawshank_redemption.jpg'),
('The Godfather', 'Crime', 'Francis Ford Coppola', 1972, 9.2, 'godfather.jpg'),
('The Dark Knight', 'Action', 'Christopher Nolan', 2008, 9.0, 'dark_knight.jpg'),
-- Add more movies here
;
'''

print('Success!')