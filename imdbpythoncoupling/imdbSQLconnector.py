import time
import mysql.connector
from mysql.connector import errorcode
import tkinter
import csv
from random import randint
title = ("INSERT INTO titles "
             "(title_id, type, primary_title, original_title, is_adult, premiered, ended, runtime_minutes, genres) "
             "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
             )
people = ("INSERT INTO people "
              "(person_id, name, born, died) "
              "VALUES (%s,%s,%s,%s)"
              )
episode = ("INSERT INTO episodes "
               "(episode_title_id, show_title_id, season_number, episode_number) "
               "VALUES (%s,%s,%s,%s)"
               )
akas = ("INSERT INTO akas "
            "(title_id, title, region, language, types, attributes, is_original_title) "
            "VALUES (%s,%s,%s,%s,%s,%s,%s)"
            )
rating = ("INSERT INTO ratings "
              "(title_id, rating, votes) "
              "VALUES (%s,%s,%s)"
              )
crew = ("INSERT INTO crew "
            "(title_id, person_id, category, job) "
            "VALUES (%s,%s,%s,%s)"
            )
r = 0
e1 = 0
e2 = 0
e3 = 0
e4 = 0
q = 0
v = 0
qu = 0
vu = 0
u = 0
uu = 0
uq = 0
uv = 0
ww = 0
k1 = 0
k2 = 0
k3 = 0
k4 = 0
k5 = 0
k6 = 0
d1 = 0
d2 = 0
d3 = 0
d4 = 0
d5 = 0
d6 = 0
u1 = 0
u11 = 0
u2 = 0
u22 = 0
u3 = 0
u33 = 0
u4 = 0
u44 = 0
q1 = 0
q11 = 0
q2 = 0
q22 = 0
q3 = 0
q4 = 0
q5 = 0
q6 = 0
qn = 0
qt = 0
p = 0
t = 0
cursor = 0
main = 0
confirm = 0
limit = 0
connection = 0
s1 = ''
s2 = ''
def qPRange():
    global q11
    global q
    global v
    global cursor
    global main
    global limit
    qq = q.get()
    vv = v.get()
    q11.destroy()
    main.title('IMDB Interface - People')
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='name').grid(row=0, column=0)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='born').grid(row=0, column=1)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='died').grid(row=0, column=2)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='me').grid(row=0, column=3)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=4)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=5)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=6)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=7)
    x = 1
    if vv is not '' or qq is not '':
        if vv is not '' and qq is not '':
            cursor.execute("SELECT * FROM people where born >= " + qq +" and died <= " + vv + " LIMIT 30")
        elif qq is not '':
            cursor.execute("SELECT * FROM people where born >= " + qq + " order by born asc LIMIT 30")
        elif vv is not '':
            cursor.execute("SELECT * FROM people where died <= " + vv + " order by died desc LIMIT 30")
    for (person_id, name, born, died, me) in cursor:
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=name).grid(row=x, column=0)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=born).grid(row=x, column=1)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=died).grid(row=x, column=2)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=me).grid(row=x, column=3)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=4)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=5)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=6)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=7)
        x = x + 1
    limit = x
    while x < 31:
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=0)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=1)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=2)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=3)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=4)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=5)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=6)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=7)
        x = x + 1
    main.update()

def qTRange():
    global q22
    global q
    global v
    global cursor
    global main
    global limit
    main.title('IMDB Interface - Titles')
    qq = q.get()
    vv = v.get()
    q22.destroy()
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='primary_title').grid(row=0, column=0)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='original_title').grid(row=0, column=1)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='type').grid(row=0, column=2)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='is_adult').grid(row=0, column=3)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='premiered').grid(row=0, column=4)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='ended').grid(row=0, column=5)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='runtime_minutes').grid(row=0, column=6)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='genres').grid(row=0, column=7)
    x = 1
    if vv is not '' or qq is not '':
        if vv is not '' and qq is not '':
            cursor.execute("SELECT * FROM titles where premiered >= " + qq + " and ended <= " + vv + " LIMIT 30")
        elif qq is not '':
            cursor.execute("SELECT * FROM titles where premiered >= " + qq + " group by premiered asc LIMIT 30")
        elif vv is not '':
            cursor.execute("SELECT * FROM titles where ended <= " + vv + " group by ended desc LIMIT 30")
    for (title_id, type, primary_title, original_title, is_adult, premiered, ended, runtime_minutes, genres) in cursor:
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=primary_title).grid(row=x, column=0)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=original_title).grid(row=x, column=1)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=type).grid(row=x, column=2)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=is_adult).grid(row=x, column=3)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=premiered).grid(row=x, column=4)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=ended).grid(row=x, column=5)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=runtime_minutes).grid(row=x, column=6)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=genres).grid(row=x, column=7)
        x = x + 1
    limit = x
    while x < 31:
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=0)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=1)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=2)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=3)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=4)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=5)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=6)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=7)
        x = x + 1
    main.update()

def qPeople():
    global cursor
    global main
    global limit
    main.title('IMDB Interface - People')
    cursor.execute("SELECT * FROM people LIMIT 30")
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='name').grid(row=0, column=0)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='born').grid(row=0, column=1)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='died').grid(row=0, column=2)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='me').grid(row=0, column=3)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=4)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=5)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=6)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=7)
    x = 1
    for (person_id, name, born, died, me) in cursor:
         tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=name).grid(row=x, column=0)
         tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=born).grid(row=x, column=1)
         tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=died).grid(row=x, column=2)
         tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=me).grid(row=x, column=3)
         tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=4)
         tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=5)
         tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=6)
         tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=7)
         x = x + 1
    limit = x
    main.update()
def qPeople2():
    global cursor
    global main
    global limit
    main.title('IMDB Interface - People')
    cursor.execute("SELECT * FROM people order by name asc LIMIT 30")
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='name').grid(row=0, column=0)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='born').grid(row=0, column=1)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='died').grid(row=0, column=2)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='me').grid(row=0, column=3)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=4)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=5)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=6)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=7)
    x = 1
    for (person_id, name, born, died, me) in cursor:
         tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=name).grid(row=x, column=0)
         tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=born).grid(row=x, column=1)
         tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=died).grid(row=x, column=2)
         tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=me).grid(row=x, column=3)
         tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=4)
         tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=5)
         tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=6)
         tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=7)
         x = x + 1
    limit = x
    main.update()
def qPeople3():
    global cursor
    global main
    global limit
    main.title('IMDB Interface - People')
    cursor.execute("SELECT * FROM people order by name desc LIMIT 30")
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='name').grid(row=0, column=0)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='born').grid(row=0, column=1)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='died').grid(row=0, column=2)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='me').grid(row=0, column=3)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=4)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=5)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=6)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=7)
    x = 1
    for (person_id, name, born, died, me) in cursor:
         tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=name).grid(row=x, column=0)
         tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=born).grid(row=x, column=1)
         tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=died).grid(row=x, column=2)
         tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=me).grid(row=x, column=3)
         tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=4)
         tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=5)
         tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=6)
         tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=7)
         x = x + 1
    limit = x
    main.update()
def qTitles():
    global cursor
    global main
    global limit
    main.title('IMDB Interface - Titles')
    cursor.execute("SELECT * FROM titles LIMIT 30")
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='primary_title').grid(row=0, column=0)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='original_title').grid(row=0, column=1)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='type').grid(row=0, column=2)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='is_adult').grid(row=0, column=3)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='premiered').grid(row=0, column=4)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='ended').grid(row=0, column=5)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='runtime_minutes').grid(row=0, column=6)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='genres').grid(row=0, column=7)
    x = 1
    for (title_id, type, primary_title, original_title, is_adult, premiered, ended, runtime_minutes, genres) in cursor:
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=primary_title).grid(row=x, column=0)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=original_title).grid(row=x, column=1)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=type).grid(row=x, column=2)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=is_adult).grid(row=x, column=3)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=premiered).grid(row=x, column=4)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=ended).grid(row=x, column=5)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=runtime_minutes).grid(row=x, column=6)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=genres).grid(row=x, column=7)
        x = x + 1
    limit = x
    main.update()
def qTitles2():
    global cursor
    global main
    global limit
    main.title('IMDB Interface - Titles')
    cursor.execute("SELECT * FROM titles order by primary_title asc LIMIT 30")
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='primary_title').grid(row=0, column=0)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='original_title').grid(row=0, column=1)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='type').grid(row=0, column=2)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='is_adult').grid(row=0, column=3)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='premiered').grid(row=0, column=4)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='ended').grid(row=0, column=5)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='runtime_minutes').grid(row=0, column=6)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='genres').grid(row=0, column=7)
    x = 1
    for (title_id, type, primary_title, original_title, is_adult, premiered, ended, runtime_minutes, genres) in cursor:
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=primary_title).grid(row=x, column=0)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=original_title).grid(row=x, column=1)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=type).grid(row=x, column=2)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=is_adult).grid(row=x, column=3)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=premiered).grid(row=x, column=4)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=ended).grid(row=x, column=5)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=runtime_minutes).grid(row=x, column=6)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=genres).grid(row=x, column=7)
        x = x + 1
    limit = x
    main.update()
def qTitles3():
    global cursor
    global main
    global limit
    main.title('IMDB Interface - Titles')
    cursor.execute("SELECT * FROM titles order by primary_title desc LIMIT 30")
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='primary_title').grid(row=0, column=0)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='original_title').grid(row=0, column=1)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='type').grid(row=0, column=2)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='is_adult').grid(row=0, column=3)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='premiered').grid(row=0, column=4)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='ended').grid(row=0, column=5)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='runtime_minutes').grid(row=0, column=6)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='genres').grid(row=0, column=7)
    x = 1
    for (title_id, type, primary_title, original_title, is_adult, premiered, ended, runtime_minutes, genres) in cursor:
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=primary_title).grid(row=x, column=0)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=original_title).grid(row=x, column=1)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=type).grid(row=x, column=2)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=is_adult).grid(row=x, column=3)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=premiered).grid(row=x, column=4)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=ended).grid(row=x, column=5)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=runtime_minutes).grid(row=x, column=6)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=genres).grid(row=x, column=7)
        x = x + 1
    limit = x
    main.update()
def qTitles4():
    global cursor
    global main
    global limit
    main.title('IMDB Interface - Titles')
    cursor.execute("SELECT * FROM titles where ended >= 0 LIMIT 30")
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='primary_title').grid(row=0, column=0)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='original_title').grid(row=0, column=1)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='type').grid(row=0, column=2)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='is_adult').grid(row=0, column=3)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='premiered').grid(row=0, column=4)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='ended').grid(row=0, column=5)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='runtime_minutes').grid(row=0, column=6)
    tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='genres').grid(row=0, column=7)
    x = 1
    for (title_id, type, primary_title, original_title, is_adult, premiered, ended, runtime_minutes, genres) in cursor:
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=primary_title).grid(row=x, column=0)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=original_title).grid(row=x, column=1)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=type).grid(row=x, column=2)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=is_adult).grid(row=x, column=3)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=premiered).grid(row=x, column=4)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=ended).grid(row=x, column=5)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=runtime_minutes).grid(row=x, column=6)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=genres).grid(row=x, column=7)
        x = x + 1
    limit = x
    main.update()
def qPerson():
    global q
    global q1
    global limit
    main.title('IMDB Interface - People')
    try:
        cursor.execute("SELECT * FROM people WHERE name = \'" + q.get() + "\' limit 30")
        q1.destroy()
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='name').grid(row=0, column=0)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='born').grid(row=0, column=1)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='died').grid(row=0, column=2)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='me').grid(row=0, column=3)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=4)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=5)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=6)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=7)
        x = 1
        for (person_id, name, born, died, me) in cursor:
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=name).grid(row=x, column=0)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=born).grid(row=x, column=1)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=died).grid(row=x, column=2)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=me).grid(row=x, column=3)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=4)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=5)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=6)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=7)
            x = x + 1
        limit = x
        while x < 31:
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=0)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=1)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=2)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=3)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=4)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=5)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=6)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=7)
            x = x + 1
    except mysql.connector.Error as err:
        e = tkinter.Tk()
        e.minsize(260, 40)
        e.title('Error')
        tkinter.Label(e, text=err).pack()
        button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
        button.pack()
    main.update()
def qTitle():
    global q
    global q2
    global cursor
    global main
    global limit
    main.title('IMDB Interface - Title')
    try:
        cursor.execute("SELECT * FROM titles WHERE primary_title = \'" + q.get() + "\' LIMIT 30")
        q2.destroy()
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='primary_title').grid(row=0, column=0)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='original_title').grid(row=0, column=1)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='type').grid(row=0, column=2)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='is_adult').grid(row=0, column=3)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='premiered').grid(row=0, column=4)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='ended').grid(row=0, column=5)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='runtime_minutes').grid(row=0, column=6)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='genres').grid(row=0, column=7)
        x = 1
        for (title_id, type, primary_title, original_title, is_adult, premiered, ended, runtime_minutes, genres) in cursor:
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=primary_title).grid(row=x, column=0)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=original_title).grid(row=x, column=1)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=type).grid(row=x, column=2)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=is_adult).grid(row=x, column=3)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=premiered).grid(row=x, column=4)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=ended).grid(row=x, column=5)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=runtime_minutes).grid(row=x, column=6)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=genres).grid(row=x, column=7)
            x = x + 1
        limit = x
        while x < 31:
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=0)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=1)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=2)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=3)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=4)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=5)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=6)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=7)
            x = x + 1
    except mysql.connector.Error as err:
        e = tkinter.Tk()
        e.minsize(260, 40)
        e.title('Error')
        tkinter.Label(e, text=err).pack()
        button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
        button.pack()
    main.update()
def qEpisode():
    global q
    global q3
    global cursor
    global main
    global limit
    main.title('IMDB Interface - Episodes')
    try:
        cursor.execute("SELECT title_id, primary_title FROM titles WHERE primary_title = \'" + q.get() + "\'")
        q3.destroy()
        id = 'N/A'
        show = 'N/A'
        for (title_id, primary_title) in cursor:
            id = title_id
            show = primary_title
        cursor.execute("SELECT * FROM episodes WHERE show_title_id = \'" + id + "\' LIMIT 30")
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='Show').grid(row=0, column=0)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='episode_id').grid(row=0, column=1)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='season_number').grid(row=0, column=2)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='episode_number').grid(row=0, column=3)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=4)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=5)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=6)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=7)
        x = 1
        for (episode_id, tid, season, episode) in cursor:
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=show).grid(row=x, column=0)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=episode_id).grid(row=x, column=1)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=season).grid(row=x, column=2)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=episode).grid(row=x, column=3)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=4)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=5)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=6)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=7)
            x = x + 1
        limit = x
        while x < 31:
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=0)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=1)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=2)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=3)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=4)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=5)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=6)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=7)
            x = x + 1
    except mysql.connector.Error as err:
        e = tkinter.Tk()
        e.minsize(260, 40)
        e.title('Error')
        tkinter.Label(e, text=err).pack()
        button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
        button.pack()
    main.update()
def qRating():
    global q
    global q4
    global cursor
    global main
    global limit
    main.title('IMDB Interface - Ratings')
    try:
        cursor.execute("SELECT title_id, primary_title FROM titles WHERE primary_title = \'" + q.get() + "\'")
        q4.destroy()
        id = 'N/A'
        show = 'N/A'
        for (title_id, primary_title) in cursor:
            id = title_id
            show = primary_title
        cursor.execute("SELECT * FROM ratings WHERE title_id = \'" + id + "\' LIMIT 30")
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='title').grid(row=0, column=0)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='rating').grid(row=0, column=1)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='vote').grid(row=0, column=2)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=3)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=4)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=5)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=6)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=7)
        x = 1
        for (tid, rating, votes) in cursor:
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=show).grid(row=x, column=0)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=rating).grid(row=x, column=1)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=votes).grid(row=x, column=2)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=3)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=4)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=5)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=6)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=7)
            x = x + 1
        limit = x
        while x < 31:
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=0)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=1)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=2)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=3)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=4)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=5)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=6)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=7)
            x = x + 1
    except mysql.connector.Error as err:
        e = tkinter.Tk()
        e.minsize(260, 40)
        e.title('Error')
        tkinter.Label(e, text=err).pack()
        button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
        button.pack()
    main.update()
def qAkas():
    global q
    global q6
    global cursor
    global main
    global limit
    main.title('IMDB Interface - Akas')
    try:
        cursor.execute("SELECT title_id, primary_title FROM titles WHERE primary_title = \'" + q.get() + "\'")
        q6.destroy()
        id = 'N/A'
        for (title_id, primary_title) in cursor:
            id = title_id
        cursor.execute("SELECT * FROM akas WHERE title_id = \'" + id + "\' LIMIT 30")
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='title').grid(row=0, column=0)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='region').grid(row=0, column=1)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='language').grid(row=0, column=2)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='types').grid(row=0, column=3)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='attributes').grid(row=0, column=4)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='is_original_title').grid(row=0, column=5)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=6)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=7)
        x = 1
        for (tid, title, region, language, types, attributes, is_original_title) in cursor:
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=title).grid(row=x, column=0)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=region).grid(row=x, column=1)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=language).grid(row=x, column=2)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=types).grid(row=x, column=3)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=attributes).grid(row=x, column=4)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=is_original_title).grid(row=x, column=5)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=6)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=7)
            x = x + 1
        limit = x
        while x < 31:
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=0)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=1)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=2)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=3)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=4)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=5)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=6)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=7)
            x = x + 1
    except mysql.connector.Error as err:
        e = tkinter.Tk()
        e.minsize(260, 40)
        e.title('Error')
        tkinter.Label(e, text=err).pack()
        button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
        button.pack()
    main.update()
def qCrewN():
    global q
    global qn
    global cursor
    global main
    global limit
    main.title('IMDB Interface - Crew')
    try:
        cursor.execute("SELECT person_id, name FROM people WHERE name = \'" + q.get() + "\'")
        qn.destroy()
        id = 'N/A'
        name = 'N/A'
        for (person_id, called) in cursor:
            id = person_id
            name = called
        cursor.execute("SELECT * FROM crew WHERE person_id = \'" + id + "\' LIMIT 30")
        titles = []
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='title').grid(row=0, column=0)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='name').grid(row=0, column=1)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='person_id').grid(row=0, column=2)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='category').grid(row=0, column=3)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='job').grid(row=0, column=4)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=5)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=6)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=7)
        x = 1
        for (tid, person, cat, job) in cursor:
            titles.append(tid)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=name).grid(row=x, column=1)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=person).grid(row=x, column=2)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=cat).grid(row=x, column=3)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=job).grid(row=x, column=4)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=4)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=5)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=6)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=7)
            x = x + 1
        x = 1
        for title in titles:
            cursor.execute("SELECT title_id, primary_title FROM titles WHERE title_id = \'" + title + "\'")
            for (title_id, show) in cursor:
                tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=show).grid(row=x, column=0)
                x = x + 1
        limit = x
        while x < 31:
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=0)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=1)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=2)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=3)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=4)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=5)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=6)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=7)
            x = x + 1
    except mysql.connector.Error as err:
        e = tkinter.Tk()
        e.minsize(260, 40)
        e.title('Error')
        tkinter.Label(e, text=err).pack()
        button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
        button.pack()
    main.update()
def qCrewT():
    global q
    global qt
    global cursor
    global main
    global limit
    main.title('IMDB Interface - Crew')
    try:
        cursor.execute("SELECT title_id, primary_title FROM titles WHERE primary_title = \'" + q.get() + "\'")
        qt.destroy()
        id = 'N/A'
        show = 'N/A'
        for (title_id, primary_title) in cursor:
            id = title_id
            show = primary_title
        cursor.execute("SELECT * FROM crew WHERE title_id = \'" + id + "\' LIMIT 30")
        names = []
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='title').grid(row=0, column=0)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='name').grid(row=0, column=1)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='person_id').grid(row=0, column=2)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='category').grid(row=0, column=3)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE, text='job').grid(row=0, column=4)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=5)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=6)
        tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=0, column=7)
        x = 1
        for (tid, person, cat, job) in cursor:
            names.append(person)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=show).grid(row=x, column=0)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=cat).grid(row=x, column=3)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=job).grid(row=x, column=4)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=4)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=5)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=6)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=7)
            x = x + 1
        x = 1
        for name in names:
            cursor.execute("SELECT person_id, name FROM people WHERE person_id = \'" + name + "\'")
            for (person_id, called) in cursor:
                tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=called).grid(row=x, column=1)
                tkinter.Label(main, width=20, relief=tkinter.RIDGE, text=name).grid(row=x, column=2)
                x = x + 1
        limit = x
        while x < 31:
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=0)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=1)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=2)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=3)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=4)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=5)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=6)
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=7)
            x = x + 1
    except mysql.connector.Error as err:
        e = tkinter.Tk()
        e.minsize(260, 40)
        e.title('Error')
        tkinter.Label(e, text=err).pack()
        button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
        button.pack()
    main.update()
def qP1():
    global q
    global q1
    global p
    p.destroy()
    q1 = tkinter.Tk()
    q1.title('Find Person')
    q1.minsize(300, 50)
    tkinter.Label(q1, text='Name').grid(row=0, column=0)
    q = tkinter.Entry(q1)
    q.grid(row=0, column=1)
    tkinter.Button(q1, text='Search', width=10, command=qPerson).grid(row=1, column=1)
    q1.update()
def qP2():
    global q
    global q11
    global p
    global v
    p.destroy()
    q11 = tkinter.Tk()
    q11.title('Find People')
    q11.minsize(300, 50)
    tkinter.Label(q11, text='Born').grid(row=0, column=0)
    q = tkinter.Entry(q11)
    q.grid(row=0, column=1)
    tkinter.Label(q11, text='Died').grid(row=1, column=0)
    v = tkinter.Entry(q11)
    v.grid(row=1, column=1)
    tkinter.Button(q11, text='Search', width=10, command=qPRange).grid(row=2, column=1)
    q11.update()
def queryPerson():
    global p
    p = tkinter.Tk()
    p.title('Find People')
    p.minsize(300, 50)
    tkinter.Button(p, text='Find by Name', width=25, command=qP1).grid(row=1, column=0)
    tkinter.Button(p, text='Find by Range', width=25, command=qP2).grid(row=1, column=1)
    p.update()
def queryTitle1():
    global q
    global q2
    global t
    t.destroy()
    q2 = tkinter.Tk()
    q2.title('Find Title')
    q2.minsize(300, 50)
    tkinter.Label(q2, text='Title').grid(row=0, column=0)
    q = tkinter.Entry(q2)
    q.grid(row=0, column=1)
    tkinter.Button(q2, text='Search', width=10, command=qTitle).grid(row=1, column=1)
    q2.update()
def queryTitle2():
    global q
    global q22
    global t
    global v
    t.destroy()
    q22 = tkinter.Tk()
    q22.title('Find Titles')
    q22.minsize(300, 50)
    tkinter.Label(q22, text='Premier').grid(row=0, column=0)
    q = tkinter.Entry(q22)
    q.grid(row=0, column=1)
    tkinter.Label(q22, text='Ended').grid(row=1, column=0)
    v = tkinter.Entry(q22)
    v.grid(row=1, column=1)
    tkinter.Button(q22, text='Search', width=10, command=qTRange).grid(row=2, column=1)
    q22.update()
def queryTitle():
    global t
    t = tkinter.Tk()
    t.title('Find Titles')
    t.minsize(300, 50)
    tkinter.Button(t, text='Find by Name', width=25, command=queryTitle1).grid(row=1, column=0)
    tkinter.Button(t, text='Find by Range', width=25, command=queryTitle2).grid(row=1, column=1)
    t.update()
def queryEpisode():
    global q
    global q3
    q3 = tkinter.Tk()
    q3.title('Find Episodes')
    q3.minsize(300, 50)
    tkinter.Label(q3, text='Title').grid(row=0, column=0)
    q = tkinter.Entry(q3)
    q.grid(row=0, column=1)
    tkinter.Button(q3, text='Search', width=10, command=qEpisode).grid(row=1, column=1)
    q3.update()
def queryRating():
    global q
    global q4
    q4 = tkinter.Tk()
    q4.title('Find Rating')
    q4.minsize(300, 50)
    tkinter.Label(q4, text='Title').grid(row=0, column=0)
    q = tkinter.Entry(q4)
    q.grid(row=0, column=1)
    tkinter.Button(q4, text='Search', width=10, command=qRating).grid(row=1, column=1)
    q4.update()
def queryByName():
    global q
    global qn
    global q5
    q5.destroy()
    qn = tkinter.Tk()
    qn.title('Find Crew')
    qn.minsize(300, 50)
    tkinter.Label(qn, text='Name').grid(row=0, column=0)
    q = tkinter.Entry(qn)
    q.grid(row=0, column=1)
    tkinter.Button(qn, text='Search', width=10, command=qCrewN).grid(row=1, column=1)
    qn.update()
def queryByTitle():
    global q
    global qt
    global q5
    q5.destroy()
    qt = tkinter.Tk()
    qt.title('Find Crew')
    qt.minsize(300, 50)
    tkinter.Label(qt, text='Title').grid(row=0, column=0)
    q = tkinter.Entry(qt)
    q.grid(row=0, column=1)
    tkinter.Button(qt, text='Search', width=10, command=qCrewT).grid(row=1, column=1)
    qt.update()
def queryCrew():
    global q5
    q5 = tkinter.Tk()
    q5.title('Find Crew')
    q5.minsize(300, 50)
    tkinter.Button(q5, text='Find by Name', width=25, command=queryByName).grid(row=1, column=0)
    tkinter.Button(q5, text='Find by Title', width=25, command=queryByTitle).grid(row=1, column=1)
    q5.update()
def queryAkas():
    global q
    global q6
    q6 = tkinter.Tk()
    q6.title('Find Akas')
    q6.minsize(300, 50)
    tkinter.Label(q6, text='Title').grid(row=0, column=0)
    q = tkinter.Entry(q6)
    q.grid(row=0, column=1)
    tkinter.Button(q6, text='Search', width=10, command=qAkas).grid(row=1, column=1)
    q6.update()

def cPerson():
    global k1
    global q
    global v
    global qu
    global qv
    global cursor
    global connection
    value1 = q.get()
    if value1 is '':
        value1 = None
    value2 = v.get()
    if value2 is '':
        value2 = None
    value3 = qu.get()
    if value3 is '':
        value3 = None
    value4 = qv.get()
    if value4 is '':
        value4 = None
    k1.destroy()
    check = True
    if value3 is not None and value4 is not None:
        if value3 > value4:
            check = False
    if check:
        try:
            cursor.execute(people, (value1, value2, value3, value4))
        except mysql.connector.Error as err:
            e = tkinter.Tk()
            e.minsize(260, 40)
            e.title('Error')
            tkinter.Label(e, text=err).pack()
            button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
            button.pack()
        else:
            e = tkinter.Tk()
            e.minsize(260, 40)
            e.title('Created Person')
            tkinter.Label(e, text='Person has successfully been created!').pack()
            button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
            button.pack()
            connection.commit()
    else:
        e = tkinter.Tk()
        e.minsize(260, 40)
        e.title('Error')
        tkinter.Label(e, text='Birth happens after death').pack()
        button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
        button.pack()
def createPerson():
    global k1
    global q
    global v
    global qu
    global qv
    k1 = tkinter.Tk()
    k1.title('New Person')
    k1.minsize(300, 50)
    tkinter.Label(k1, text='Person_id').grid(row=0, column=0)
    q = tkinter.Entry(k1)
    q.grid(row=0, column=1)
    tkinter.Label(k1, text='Name').grid(row=1, column=0)
    v = tkinter.Entry(k1)
    v.grid(row=1, column=1)
    tkinter.Label(k1, text='Born').grid(row=2, column=0)
    qu = tkinter.Entry(k1)
    qu.grid(row=2, column=1)
    tkinter.Label(k1, text='Died').grid(row=3, column=0)
    qv = tkinter.Entry(k1)
    qv.grid(row=3, column=1)
    tkinter.Button(k1, text='Create', width=10, command=cPerson).grid(row=4, column=1)
    k1.update()
def cTitle():
    global k2
    global q
    global v
    global qu
    global qv
    global u
    global uu
    global uq
    global uv
    global ww
    global cursor
    global connection
    value1 = q.get()
    if value1 is '':
        value1 = None
    value2 = v.get()
    if value2 is '':
        value2 = None
    value3 = qu.get()
    if value3 is '':
        value3 = None
    value4 = qv.get()
    if value4 is '':
        value4 = None
    value5 = u.get()
    if value5 is '':
        value5 = None
    value6 = uu.get()
    if value6 is '':
        value6 = None
    value7 = uq.get()
    if value7 is '':
        value7 = None
    value8 = uv.get()
    if value8 is '':
        value8 = None
    value9 = ww.get()
    if value9 is '':
        value9 = None
    k2.destroy()
    check = True
    if value6 is not None and value7 is not None or value6 is None:
        if value6 > value7:
            check = False
    if check:
        try:
            cursor.execute(title, (value1, value2, value3, value4, value5, value6, value7, value8, value9))
        except mysql.connector.Error as err:
            e = tkinter.Tk()
            e.minsize(260, 40)
            e.title('Error')
            tkinter.Label(e, text=err).pack()
            button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
            button.pack()
        else:
            e = tkinter.Tk()
            e.minsize(260, 40)
            e.title('Created Title')
            tkinter.Label(e, text='Title has successfully been created!').pack()
            button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
            button.pack()
            connection.commit()
    else:
        e = tkinter.Tk()
        e.minsize(260, 40)
        e.title('Error')
        tkinter.Label(e, text='Premiered date is after end date').pack()
        button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
        button.pack()
def createTitle():
    global k2
    global q
    global v
    global qu
    global qv
    global u
    global uu
    global uq
    global uv
    global ww
    k2 = tkinter.Tk()
    k2.title('New Title')
    k2.minsize(300, 50)
    tkinter.Label(k2, text='Title_id').grid(row=0, column=0)
    q = tkinter.Entry(k2)
    q.grid(row=0, column=1)
    tkinter.Label(k2, text='Type').grid(row=1, column=0)
    v = tkinter.Entry(k2)
    v.grid(row=1, column=1)
    tkinter.Label(k2, text='Primary Title').grid(row=2, column=0)
    qu = tkinter.Entry(k2)
    qu.grid(row=2, column=1)
    tkinter.Label(k2, text='Original Title').grid(row=3, column=0)
    qv = tkinter.Entry(k2)
    qv.grid(row=3, column=1)
    tkinter.Label(k2, text='is_Adult').grid(row=4, column=0)
    u = tkinter.Entry(k2)
    u.grid(row=4, column=1)
    tkinter.Label(k2, text='Premiered').grid(row=5, column=0)
    uu = tkinter.Entry(k2)
    uu.grid(row=5, column=1)
    tkinter.Label(k2, text='Ended').grid(row=6, column=0)
    uq = tkinter.Entry(k2)
    uq.grid(row=6, column=1)
    tkinter.Label(k2, text='Runtime Minutes').grid(row=7, column=0)
    uv = tkinter.Entry(k2)
    uv.grid(row=7, column=1)
    tkinter.Label(k2, text='Genres').grid(row=8, column=0)
    ww = tkinter.Entry(k2)
    ww.grid(row=8, column=1)
    tkinter.Button(k2, text='Create', width=10, command=cTitle).grid(row=9, column=1)
    k2.update()
def cEpisode():
    global k3
    global q
    global v
    global qu
    global qv
    global cursor
    global connection
    value1 = q.get()
    if value1 is '':
        k3.destroy()
        e = tkinter.Tk()
        e.minsize(260, 40)
        e.title('Error')
        tkinter.Label(e, text='No title to reference to titles').pack()
        button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
        button.pack()
    else:
        value2 = v.get()
        if value2 is '':
            value2 = None
        value3 = qu.get()
        if value3 is '':
            value3 = None
        value4 = qv.get()
        if value4 is '':
            value4 = None
        k3.destroy()
        cursor.execute("SELECT title_id, primary_title FROM titles WHERE primary_title = \'" + value1 + "\'")
        id = ''
        show = ''
        for (title_id, primary_title) in cursor:
            id = title_id
            show = primary_title
        if show is '':
            e = tkinter.Tk()
            e.minsize(260, 40)
            e.title('Error')
            tkinter.Label(e, text='Title does not exist in titles').pack()
            button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
            button.pack()
        else:
            try:
                cursor.execute(episode, (value2, id, value3, value4))
            except mysql.connector.Error as err:
                e = tkinter.Tk()
                e.minsize(260, 40)
                e.title('Error')
                tkinter.Label(e, text=err).pack()
                button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                button.pack()
            else:
                e = tkinter.Tk()
                e.minsize(260, 40)
                e.title('Created Episode')
                tkinter.Label(e, text='Episode has successfully been created!').pack()
                button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                button.pack()
                connection.commit()
def createEpisode():
    global k3
    global q
    global v
    global qu
    global qv
    k3 = tkinter.Tk()
    k3.title('New Episode')
    k3.minsize(300, 50)
    tkinter.Label(k3, text='Title Name(Ref)').grid(row=0, column=0)
    q = tkinter.Entry(k3)
    q.grid(row=0, column=1)
    tkinter.Label(k3, text='Episode Id').grid(row=1, column=0)
    v = tkinter.Entry(k3)
    v.grid(row=1, column=1)
    tkinter.Label(k3, text='Season Number').grid(row=2, column=0)
    qu = tkinter.Entry(k3)
    qu.grid(row=2, column=1)
    tkinter.Label(k3, text='Episode Number').grid(row=3, column=0)
    qv = tkinter.Entry(k3)
    qv.grid(row=3, column=1)
    tkinter.Button(k3, text='Create', width=10, command=cEpisode).grid(row=4, column=1)
    k3.update()
def cRating():
    global k4
    global q
    global v
    global qu
    global qv
    global cursor
    global connection
    value1 = q.get()
    if value1 is '':
        k4.destroy()
        e = tkinter.Tk()
        e.minsize(260, 40)
        e.title('Error')
        tkinter.Label(e, text='No title to reference to titles').pack()
        button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
        button.pack()
    else:
        value2 = v.get()
        if value2 is '':
            value2 = None
        value3 = qu.get()
        if value3 is '':
            value3 = None
        k4.destroy()
        cursor.execute("SELECT title_id, primary_title FROM titles WHERE primary_title = \'" + value1 + "\'")
        id = ''
        show = ''
        for (title_id, primary_title) in cursor:
            id = title_id
            show = primary_title
        if show is '':
            e = tkinter.Tk()
            e.minsize(260, 40)
            e.title('Error')
            tkinter.Label(e, text='Title does not exist in titles').pack()
            button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
            button.pack()
        else:
            try:
                cursor.execute(rating, (id, value2, value3))
            except mysql.connector.Error as err:
                e = tkinter.Tk()
                e.minsize(260, 40)
                e.title('Error')
                tkinter.Label(e, text=err).pack()
                button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                button.pack()
            else:
                e = tkinter.Tk()
                e.minsize(260, 40)
                e.title('Created Rating')
                tkinter.Label(e, text='Rating has successfully been created!').pack()
                button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                button.pack()
                connection.commit()
def createRating():
    global k4
    global q
    global v
    global qu
    k4 = tkinter.Tk()
    k4.title('New Rating')
    k4.minsize(300, 50)
    tkinter.Label(k4, text='Title Name(Ref)').grid(row=0, column=0)
    q = tkinter.Entry(k4)
    q.grid(row=0, column=1)
    tkinter.Label(k4, text='Rating').grid(row=1, column=0)
    v = tkinter.Entry(k4)
    v.grid(row=1, column=1)
    tkinter.Label(k4, text='Votes').grid(row=2, column=0)
    qu = tkinter.Entry(k4)
    qu.grid(row=2, column=1)
    tkinter.Button(k4, text='Create', width=10, command=cRating).grid(row=3, column=1)
    k4.update()
def cCrew():
    global k5
    global q
    global v
    global qu
    global qv
    global cursor
    global connection
    value1 = q.get()
    if value1 is '':
        k5.destroy()
        e = tkinter.Tk()
        e.minsize(260, 40)
        e.title('Error')
        tkinter.Label(e, text='No title to reference to titles').pack()
        button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
        button.pack()
    else:
        value2 = v.get()
        if value2 is '':
            k5.destroy()
            e = tkinter.Tk()
            e.minsize(260, 40)
            e.title('Error')
            tkinter.Label(e, text='No person to reference to people').pack()
            button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
            button.pack()
        else:
            value3 = qu.get()
            if value3 is '':
                value3 = None
            value4 = qv.get()
            if value4 is '':
                value4 = None
            k5.destroy()
            cursor.execute("SELECT title_id, primary_title FROM titles WHERE primary_title = \'" + value1 + "\'")
            id1 = ''
            show = ''
            for (title_id, primary_title) in cursor:
                id1 = title_id
                show = primary_title
            if show is '':
                e = tkinter.Tk()
                e.minsize(260, 40)
                e.title('Error')
                tkinter.Label(e, text='Title does not exist in titles').pack()
                button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                button.pack()
            else:
                cursor.execute("SELECT person_id, name FROM people WHERE name = \'" + value2 + "\'")
                id2 = ''
                name = ''
                for (pid, n) in cursor:
                    id2 = pid
                    name = n
                if name is '':
                    e = tkinter.Tk()
                    e.minsize(260, 40)
                    e.title('Error')
                    tkinter.Label(e, text='Person does not exist in people').pack()
                    button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                    button.pack()
                else:
                    try:
                        cursor.execute(crew, (id1, id2, value3, value4))
                    except mysql.connector.Error as err:
                        e = tkinter.Tk()
                        e.minsize(260, 40)
                        e.title('Error')
                        tkinter.Label(e, text=err).pack()
                        button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                        button.pack()
                    else:
                        e = tkinter.Tk()
                        e.minsize(260, 40)
                        e.title('Created Crew')
                        tkinter.Label(e, text='Crew has successfully been created!').pack()
                        button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                        button.pack()
                        connection.commit()
def createCrew():
    global k5
    global q
    global v
    global qu
    global qv
    k5 = tkinter.Tk()
    k5.title('New Crew')
    k5.minsize(300, 50)
    tkinter.Label(k5, text='Title Name(Ref)').grid(row=0, column=0)
    q = tkinter.Entry(k5)
    q.grid(row=0, column=1)
    tkinter.Label(k5, text='Person Name(Ref)').grid(row=1, column=0)
    v = tkinter.Entry(k5)
    v.grid(row=1, column=1)
    tkinter.Label(k5, text='Category').grid(row=2, column=0)
    qu = tkinter.Entry(k5)
    qu.grid(row=2, column=1)
    tkinter.Label(k5, text='Job').grid(row=3, column=0)
    qv = tkinter.Entry(k5)
    qv.grid(row=3, column=1)
    tkinter.Button(k5, text='Create', width=10, command=cCrew).grid(row=4, column=1)
    k5.update()
def cAkas():
    global k6
    global q
    global v
    global qu
    global qv
    global u
    global uu
    global uq
    global cursor
    global connection
    value1 = q.get()
    if value1 is '':
        k6.destroy()
        e = tkinter.Tk()
        e.minsize(260, 40)
        e.title('Error')
        tkinter.Label(e, text='No title to reference to titles').pack()
        button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
        button.pack()
    else:
        value2 = v.get()
        if value2 is '':
            value2 = None
        value3 = qu.get()
        if value3 is '':
            value3 = None
        value4 = qv.get()
        if value4 is '':
            value4 = None
        value5 = u.get()
        if value5 is '':
            value5 = None
        value6 = uu.get()
        if value6 is '':
            value6 = None
        value7 = uq.get()
        if value7 is '':
            value7 = None
        k6.destroy()
        cursor.execute("SELECT title_id, primary_title FROM titles WHERE primary_title = \'" + value1 + "\'")
        id = ''
        show = ''
        for (title_id, primary_title) in cursor:
            id = title_id
            show = primary_title
        if show is '':
            e = tkinter.Tk()
            e.minsize(260, 40)
            e.title('Error')
            tkinter.Label(e, text='Title does not exist in titles').pack()
            button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
            button.pack()
        else:
            try:
                cursor.execute(akas, (id, value2, value3, value4, value5, value6, value7))
            except mysql.connector.Error as err:
                e = tkinter.Tk()
                e.minsize(260, 40)
                e.title('Error')
                tkinter.Label(e, text=err).pack()
                button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                button.pack()
            else:
                e = tkinter.Tk()
                e.minsize(260, 40)
                e.title('Created Akas')
                tkinter.Label(e, text='Akas has successfully been created!').pack()
                button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                button.pack()
                connection.commit()
def createAkas():
    global k6
    global q
    global v
    global qu
    global qv
    global u
    global uu
    global uq
    k6 = tkinter.Tk()
    k6.title('New Akas')
    k6.minsize(300,50)
    tkinter.Label(k6, text='Title Name(Ref)').grid(row=0, column=0)
    q = tkinter.Entry(k6)
    q.grid(row=0, column=1)
    tkinter.Label(k6, text='Alternate Title').grid(row=1, column=0)
    v = tkinter.Entry(k6)
    v.grid(row=1, column=1)
    tkinter.Label(k6, text='Region').grid(row=2, column=0)
    qu = tkinter.Entry(k6)
    qu.grid(row=2, column=1)
    tkinter.Label(k6, text='Language').grid(row=3, column=0)
    qv = tkinter.Entry(k6)
    qv.grid(row=3, column=1)
    tkinter.Label(k6, text='Types').grid(row=4, column=0)
    u = tkinter.Entry(k6)
    u.grid(row=4, column=1)
    tkinter.Label(k6, text='Attributes').grid(row=5, column=0)
    uu = tkinter.Entry(k6)
    uu.grid(row=5, column=1)
    tkinter.Label(k6, text='Is Original?').grid(row=6, column=0)
    uq = tkinter.Entry(k6)
    uq.grid(row=6, column=1)
    tkinter.Button(k6, text='Create', width=10, command=cAkas).grid(row=7, column=1)
    k6.update()

def delete():
    global cursor
    global main
    global confirm
    cursor.execute("DROP DATABASE IF EXISTS imdb")
    main.destroy()
    confirm.destroy()
    start()

def confirmDeletion():
    global confirm
    confirm = tkinter.Tk()
    confirm.title('Delete IMDB')
    tkinter.Label(confirm, text='ARE you sure you want to delete the Database?').grid(row=0)
    tkinter.Button(confirm, text='Yes', width=25, command=delete).grid(row=1, column=0)
    tkinter.Button(confirm, text='No', width=25, command=confirm.destroy).grid(row=1, column=1)
    confirm.update()
def dPerson():
    global d1
    global q
    global cursor
    global connection
    try:
        value1 = q.get()
        d1.destroy()
        if value1 is '':
            e = tkinter.Tk()
            e.minsize(260, 40)
            e.title('Error')
            tkinter.Label(e, text='No person to reference to people').pack()
            button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
            button.pack()
        else:
            cname = 'NUL'
            name = 'NULL'
            while cname is not name:
                cursor.execute("SELECT person_id, name FROM people WHERE name = \'" + value1 + "\'")
                id = 'NULL'
                cname = name
                for (pid, n) in cursor:
                    id = pid
                    name = n
                cursor.execute("SET foreign_key_checks = 0")
                cursor.execute("DELETE FROM crew WHERE person_id = \'" + id + "\'")
                cursor.execute("DELETE FROM people WHERE name = \'" + value1 + "\'")
                cursor.execute("SET foreign_key_checks = 1")
            e = tkinter.Tk()
            e.minsize(260, 40)
            e.title('Deleted Person')
            tkinter.Label(e, text='All instances of person has been deleted if they existed!').pack()
            button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
            button.pack()
            connection.commit()
    except mysql.connector.Error as err:
        e = tkinter.Tk()
        e.minsize(260, 40)
        e.title('Error')
        tkinter.Label(e, text=err).pack()
        button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
        button.pack()
def deletePerson():
    global d1
    global q
    d1 = tkinter.Tk()
    d1.title('Delete Person')
    d1.minsize(300, 50)
    tkinter.Label(d1, text='Notice: Deleting a person will delete').grid(row=0)
    tkinter.Label(d1, text='every instance of person in every other table').grid(row=1)
    tkinter.Label(d1, text='                                            Name').grid(row=2, column=0)
    q = tkinter.Entry(d1)
    q.grid(row=2, column=1)
    tkinter.Button(d1, text='DELETE', width=10, command=dPerson).grid(row=3, column=1)
    d1.update()
def dTitle():
    global d2
    global q
    global cursor
    global connection
    try:
        value1 = q.get()
        d2.destroy()
        if value1 is '':
            e = tkinter.Tk()
            e.minsize(260, 40)
            e.title('Error')
            tkinter.Label(e, text='No title to reference to titles').pack()
            button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
            button.pack()
        else:
            pshow = 'NUL'
            show = 'NULL'
            while pshow is not show:
                cursor.execute("SELECT title_id, primary_title FROM titles WHERE primary_title = \'" + value1 + "\'")
                id = 'NULL'
                pshow = show
                for (tid, s) in cursor:
                    id = tid
                    show = s
                cursor.execute("SET foreign_key_checks = 0")
                cursor.execute("DELETE FROM episodes WHERE show_title_id = \'" + id + "\'")
                cursor.execute("DELETE FROM ratings WHERE title_id = \'" + id + "\'")
                cursor.execute("DELETE FROM akas WHERE title_id = \'" + id + "\'")
                cursor.execute("DELETE FROM crew WHERE title_id = \'" + id + "\'")
                cursor.execute("DELETE FROM titles WHERE primary_title = \'" + value1 + "\'")
                cursor.execute("SET foreign_key_checks = 1")
            e = tkinter.Tk()
            e.minsize(260, 40)
            e.title('Deleted Title')
            tkinter.Label(e, text='All instances of title has been deleted if they existed!').pack()
            button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
            button.pack()
            connection.commit()
    except mysql.connector.Error as err:
        e = tkinter.Tk()
        e.minsize(260, 40)
        e.title('Error')
        tkinter.Label(e, text=err).pack()
        button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
        button.pack()
def deleteTitle():
    global d2
    global q
    d2 = tkinter.Tk()
    d2.title('Delete Title')
    d2.minsize(300, 50)
    tkinter.Label(d2, text='Notice: Deleting a title will delete').grid(row=0)
    tkinter.Label(d2, text='every instance of title in every other table').grid(row=1)
    tkinter.Label(d2, text='                                           Title').grid(row=2, column=0)
    q = tkinter.Entry(d2)
    q.grid(row=2, column=1)
    tkinter.Button(d2, text='DELETE', width=10, command=dTitle).grid(row=3, column=1)
    d2.update()
def dRating():
    global d3
    global q
    global cursor
    global connection
    try:
        value1 = q.get()
        d3.destroy()
        if value1 is '':
            e = tkinter.Tk()
            e.minsize(260, 40)
            e.title('Error')
            tkinter.Label(e, text='No title to reference to titles').pack()
            button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
            button.pack()
        else:
            cursor.execute("SELECT title_id, primary_title FROM titles WHERE primary_title = \'" + value1 + "\'")
            id = 'NULL'
            show = 'NULL'
            for (tid, s) in cursor:
                id = tid
                show = s
            cursor.execute("SET foreign_key_checks = 0")
            cursor.execute("DELETE FROM ratings WHERE title_id = \'" + id + "\'")
            cursor.execute("SET foreign_key_checks = 1")
            e = tkinter.Tk()
            e.minsize(260, 40)
            e.title('Deleted Rating')
            tkinter.Label(e, text='Rating has been deleted if they existed!').pack()
            button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
            button.pack()
            connection.commit()
    except mysql.connector.Error as err:
        e = tkinter.Tk()
        e.minsize(260, 40)
        e.title('Error')
        tkinter.Label(e, text=err).pack()
        button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
        button.pack()

def deleteRating():
    global d3
    global q
    d3 = tkinter.Tk()
    d3.title('Delete Rating')
    d3.minsize(300, 50)
    tkinter.Label(d3, text='Title').grid(row=0, column=0)
    q = tkinter.Entry(d3)
    q.grid(row=0, column=1)
    tkinter.Button(d3, text='DELETE', width=10, command=dRating).grid(row=1, column=1)
    d3.update()
def dEpisode():
    global d4
    global q
    global v
    global u
    global cursor
    global connection
    try:
        value1 = q.get()
        value2 = v.get()
        value3 = u.get()
        d4.destroy()
        if value1 is not '' or value2 is not '' or value3 is not '':
            if value1 is not '' and value2 is not '' and value3 is not '':
                cursor.execute("SELECT title_id, primary_title FROM titles WHERE primary_title = \'" + value1 + "\'")
                id = 'NULL'
                show = 'NULL'
                for (tid, s) in cursor:
                    id = tid
                    show = s
                cursor.execute("SET foreign_key_checks = 0")
                cursor.execute("DELETE FROM episodes WHERE show_title_id = \'" + id + "\' and season_number = " + value2 + " and episode_number = " + value3)
                cursor.execute("SET foreign_key_checks = 1")
                e = tkinter.Tk()
                e.minsize(260, 40)
                e.title('Deleted Episodes')
                tkinter.Label(e, text='All episodes has been deleted for that title if they existed!').pack()
                button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                button.pack()
                connection.commit()
            elif value1 is not '' and value2 is not '':
                cursor.execute("SELECT title_id, primary_title FROM titles WHERE primary_title = \'" + value1 + "\'")
                id = 'NULL'
                show = 'NULL'
                for (tid, s) in cursor:
                    id = tid
                    show = s
                cursor.execute("SET foreign_key_checks = 0")
                cursor.execute("DELETE FROM episodes WHERE show_title_id = \'" + id + "\' and season_number = " + value2)
                cursor.execute("SET foreign_key_checks = 1")
                e = tkinter.Tk()
                e.minsize(260, 40)
                e.title('Deleted Episodes')
                tkinter.Label(e, text='All episodes has been deleted for that title if they existed!').pack()
                button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                button.pack()
                connection.commit()
            elif value1 is not '' and value3 is not '':
                e = tkinter.Tk()
                e.minsize(260, 40)
                e.title('Error')
                tkinter.Label(e, text='You cannot delete an episode with a title and episode number alone').pack()
                button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                button.pack()
            elif value1 is not '':
                cursor.execute("SELECT title_id, primary_title FROM titles WHERE primary_title = \'" + value1 + "\'")
                id = 'NULL'
                show = 'NULL'
                for (tid, s) in cursor:
                    id = tid
                    show = s
                cursor.execute("SET foreign_key_checks = 0")
                cursor.execute("DELETE FROM episodes WHERE show_title_id = \'" + id + "\'")
                cursor.execute("SET foreign_key_checks = 1")
                e = tkinter.Tk()
                e.minsize(260, 40)
                e.title('Deleted Episodes')
                tkinter.Label(e, text='All episodes has been deleted for that title if they existed!').pack()
                button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                button.pack()
                connection.commit()
            else:
                e = tkinter.Tk()
                e.minsize(260, 40)
                e.title('Error')
                tkinter.Label(e, text='No title to reference to titles').pack()
                button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                button.pack()
    except mysql.connector.Error as err:
        e = tkinter.Tk()
        e.minsize(260, 40)
        e.title('Error')
        tkinter.Label(e, text=err).pack()
        button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
        button.pack()
def deleteEpisode():
    global d4
    global q
    global v
    global u
    d4 = tkinter.Tk()
    d4.title('Delete Episode')
    d4.minsize(300, 50)
    tkinter.Label(d4, text='Specifying only title will delete all episodes').grid(row=0)
    tkinter.Label(d4, text='Specifying title with season will delete all episodes in season').grid(row=1)
    tkinter.Label(d4, text='Specifying title, season and episode will delete one episode').grid(row=2)
    tkinter.Label(d4, text='                                                          Title').grid(row=3, column=0)
    q = tkinter.Entry(d4)
    q.grid(row=3, column=1)
    tkinter.Label(d4, text='                                                  Season Number').grid(row=4, column=0)
    v = tkinter.Entry(d4)
    v.grid(row=4, column=1)
    tkinter.Label(d4, text='                                                 Episode Number').grid(row=5, column=0)
    u = tkinter.Entry(d4)
    u.grid(row=5, column=1)
    tkinter.Button(d4, text='DELETE', width=10, command=dEpisode).grid(row=6, column=1)
    d4.update()
def dCrew():
    global d5
    global q
    global v
    global cursor
    global connection
    try:
        value1 = q.get()
        value2 = v.get()
        d5.destroy()
        if value1 is not '' or value2 is not '':
            cursor.execute("SET foreign_key_checks = 0")
            if value1 is not '' and value2 is not '':
                cursor.execute("SELECT title_id, primary_title FROM titles WHERE primary_title = \'" + value1 + "\'")
                id1 = 'NULL'
                show = 'NULL'
                for (tid, s) in cursor:
                    id1 = tid
                    show = s
                cursor.execute("SELECT person_id, name FROM people WHERE name = \'" + value2 + "\'")
                id2 = 'NULL'
                name = 'NULL'
                for (pid, n) in cursor:
                    id2 = pid
                    name = n
                cursor.execute("DELETE FROM crew WHERE title_id = \'" + id1 + "\' and person_id = \'" + id2 + "\'")
                e = tkinter.Tk()
                e.minsize(260, 40)
                e.title('Deleted Crew')
                tkinter.Label(e, text='Crew has been deleted by title and person if they existed!').pack()
                button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                button.pack()
                connection.commit
            elif value1 is not '':
                cursor.execute("SELECT title_id, primary_title FROM titles WHERE primary_title = \'" + value1 + "\'")
                id1 = 'NULL'
                show = 'NULL'
                for (tid, s) in cursor:
                    id1 = tid
                    show = s
                cursor.execute("DELETE FROM crew WHERE title_id = \'" + id1 + "\'")
                e = tkinter.Tk()
                e.minsize(260, 40)
                e.title('Deleted Crew')
                tkinter.Label(e, text='Crew has been deleted by title if it existed!').pack()
                button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                button.pack()
                connection.commit()
            elif value2 is not '':
                cursor.execute("SELECT person_id, name FROM people WHERE name = \'" + value2 + "\'")
                id2 = 'NULL'
                name = 'NULL'
                for (pid, n) in cursor:
                    id2 = pid
                    name = n
                cursor.execute("DELETE FROM crew WHERE person_id = \'" + id2 + "\'")
                e = tkinter.Tk()
                e.minsize(260, 40)
                e.title('Deleted Crew')
                tkinter.Label(e, text='Crew has been deleted by person if they existed!').pack()
                button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                button.pack()
                connection.commit()
            cursor.execute("SET foreign_key_checks = 1")
        else:
            e = tkinter.Tk()
            e.minsize(260, 40)
            e.title('Error')
            tkinter.Label(e, text='No fields were filled').pack()
            button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
            button.pack()
    except mysql.connector.Error as err:
        e = tkinter.Tk()
        e.minsize(260, 40)
        e.title('Error')
        tkinter.Label(e, text=err).pack()
        button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
        button.pack()

def deleteCrew():
    global d5
    global q
    global v
    d5 = tkinter.Tk()
    d5.title('Delete Crew')
    d5.minsize(300, 50)
    tkinter.Label(d5, text='Specifying only title will delete all Crew for that title').grid(row=0)
    tkinter.Label(d5, text='Specifying only name will delete all Crew for that person').grid(row=1)
    tkinter.Label(d5, text='Specifying name and title will delete one Crew').grid(row=2)
    tkinter.Label(d5, text='                                                    Title').grid(row=3, column=0)
    q = tkinter.Entry(d5)
    q.grid(row=3, column=1)
    tkinter.Label(d5, text='                                                     Name').grid(row=4, column=0)
    v = tkinter.Entry(d5)
    v.grid(row=4, column=1)
    tkinter.Button(d5, text='DELETE', width=10, command=dCrew).grid(row=5, column=1)
    d5.update()
def dAkas():
    global d6
    global q
    global v
    global cursor
    global connection
    try:
        value1 = q.get()
        value2 = v.get()
        d6.destroy()
        if value1 is not '' or value2 is not '':
            cursor.execute("SET foreign_key_checks = 0")
            if value1 is not '' and value2 is not '':
                cursor.execute("SELECT title_id, primary_title FROM titles WHERE primary_title = \'" + value1 + "\'")
                id1 = 'NULL'
                show = 'NULL'
                for (tid, s) in cursor:
                    id1 = tid
                    show = s
                cursor.execute("SELECT title, title_id FROM akas WHERE title = \'" + value2 + "\'")
                id2 = 'NULL'
                name = 'NULL'
                for (pid, n) in cursor:
                    id2 = pid
                    name = n
                cursor.execute("DELETE FROM akas WHERE title_id = \'" + id1 + "\' and title = \'" + id2 + "\'")
                e = tkinter.Tk()
                e.minsize(260, 40)
                e.title('Deleted Akas')
                tkinter.Label(e, text='Akas has been deleted by title and akas if they existed!').pack()
                button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                button.pack()
                connection.commit()
            elif value1 is not '':
                cursor.execute("SELECT title_id, primary_title FROM titles WHERE primary_title = \'" + value1 + "\'")
                id1 = 'NULL'
                show = 'NULL'
                for (tid, s) in cursor:
                    id1 = tid
                    show = s
                cursor.execute("DELETE FROM akas WHERE title_id = \'" + id1 + "\'")
                e = tkinter.Tk()
                e.minsize(260, 40)
                e.title('Deleted Akas')
                tkinter.Label(e, text='Akas has been deleted by english or original title if they existed!').pack()
                button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                button.pack()
                connection.commit()
            elif value2 is not '':
                cursor.execute("SELECT title, title_id FROM akas WHERE title = \'" + value2 + "\'")
                id2 = 'NULL'
                name = 'NULL'
                for (pid, n) in cursor:
                    id2 = pid
                    name = n
                cursor.execute("DELETE FROM akas WHERE title = \'" + id2 + "\'")
                e = tkinter.Tk()
                e.minsize(260, 40)
                e.title('Deleted Akas')
                tkinter.Label(e, text='Akas has been deleted by alternate title if they existed!').pack()
                button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                button.pack()
                connection.commit()
            cursor.execute("SET foreign_key_checks = 1")
        else:
            e = tkinter.Tk()
            e.minsize(260, 40)
            e.title('Error')
            tkinter.Label(e, text='No fields were filled').pack()
            button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
            button.pack()
    except mysql.connector.Error as err:
        e = tkinter.Tk()
        e.minsize(260, 40)
        e.title('Error')
        tkinter.Label(e, text=err).pack()
        button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
        button.pack()
def deleteAkas():
    global d6
    global q
    global v
    d6 = tkinter.Tk()
    d6.title('Delete Akas')
    d6.minsize(300, 50)
    tkinter.Label(d6, text='Specifying only title will delete all Akas for that title').grid(row=0)
    tkinter.Label(d6, text='Specifying only Akas will delete all Akas for with that name').grid(row=1)
    tkinter.Label(d6, text='Specifying Akas and title will delete that specific Akas').grid(row=2)
    tkinter.Label(d6, text='                                                    Title').grid(row=3, column=0)
    q = tkinter.Entry(d6)
    q.grid(row=3, column=1)
    tkinter.Label(d6, text='                                          Alternate Title').grid(row=4, column=0)
    v = tkinter.Entry(d6)
    v.grid(row=4, column=1)
    tkinter.Button(d6, text='DELETE', width=10, command=dAkas).grid(row=5, column=1)
    d6.update()
def uPerson():
    global u1
    global q
    global v
    global cursor
    global connection
    value1 = q.get()
    v2 = v.get()
    u1.destroy()
    try:
        if value1 is not '' and v2 is not '':
            value2 = int(v2)
            cursor.execute("SELECT person_id, born, died FROM people WHERE name = \'" + value1 + "\'")
            show = 'NULL'
            b = 0
            ended = 0
            for (tid, s, end) in cursor:
                show = tid
                b = s
                ended = end
            if b is None:
                b = -99999
            if show is not 'NULL':
                if b <= value2 and ended is None:
                    cursor.execute("UPDATE people SET died = " + str(value2) + " where person_id = \'" + show + "\'")
                    connection.commit()
                    e = tkinter.Tk()
                    e.minsize(260, 40)
                    e.title('Person Updated')
                    tkinter.Label(e, text='Person has been given a death').pack()
                    button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                    button.pack()
                else:
                    e = tkinter.Tk()
                    e.minsize(260, 40)
                    e.title('Error')
                    tkinter.Label(e, text='Person not found').pack()
                    button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                    button.pack()
            else:
                e = tkinter.Tk()
                e.minsize(260, 40)
                e.title('Error')
                tkinter.Label(e, text='Person expiry is before birth or death was already logged').pack()
                button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                button.pack()
        else:
            e = tkinter.Tk()
            e.minsize(260, 40)
            e.title('Error')
            tkinter.Label(e, text='Not all fields were filled').pack()
            button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
            button.pack()
    except mysql.connector.Error as err:
        e = tkinter.Tk()
        e.minsize(260, 40)
        e.title('Error')
        tkinter.Label(e, text=err).pack()
        button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
        button.pack()
def updatePerson():
    global u1
    global q
    global v
    u1 = tkinter.Tk()
    u1.title('Update Person')
    u1.minsize(300, 50)
    tkinter.Label(u1, text='Refer to a person and give an expiration date').grid(row=0)
    tkinter.Label(u1, text='Name').grid(row=1, column=0)
    q = tkinter.Entry(u1)
    q.grid(row=1, column=1)
    tkinter.Label(u1, text='Died').grid(row=2, column=0)
    v = tkinter.Entry(u1)
    v.grid(row=2, column=1)
    tkinter.Button(u1, text='UPDATE', width=10, command=uPerson).grid(row=3, column=1)
    u1.update()
def uTitle():
    global u2
    global q
    global v
    global cursor
    global connection
    value1 = q.get()
    v2 = v.get()
    u2.destroy()
    try:
        if value1 is not '' and v2 is not '':
            value2 = int(v2)
            cursor.execute("SELECT title_id, premiered, ended FROM titles WHERE primary_title = \'" + value1 + "\'")
            show = 'NULL'
            b = 0
            ended = 0
            for (tid, s, end) in cursor:
                show = tid
                b = s
                ended = end
            if show is not 'NULL':
                if b <= value2 and ended is None:
                    cursor.execute("UPDATE titles SET ended = " + str(value2) + " where title_id = \'" + show + "\'")
                    connection.commit()
                    e = tkinter.Tk()
                    e.minsize(260, 40)
                    e.title('Title Updated')
                    tkinter.Label(e, text='Title has been given an end year').pack()
                    button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                    button.pack()
                else:
                    e = tkinter.Tk()
                    e.minsize(260, 40)
                    e.title('Error')
                    tkinter.Label(e, text='Title not found').pack()
                    button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                    button.pack()
            else:
                e = tkinter.Tk()
                e.minsize(260, 40)
                e.title('Error')
                tkinter.Label(e, text='Title end date is before premier date or end date already exists').pack()
                button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                button.pack()
        else:
            e = tkinter.Tk()
            e.minsize(260, 40)
            e.title('Error')
            tkinter.Label(e, text='Not all fields were filled').pack()
            button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
            button.pack()
    except mysql.connector.Error as err:
            e = tkinter.Tk()
            e.minsize(260, 40)
            e.title('Error')
            tkinter.Label(e, text=err).pack()
            button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
            button.pack()
def updateTitle():
    global u2
    global q
    global v
    u2 = tkinter.Tk()
    u2.title('Update Title')
    u2.minsize(300, 50)
    tkinter.Label(u2, text='Refer to the title and give a cancellation year').grid(row=0)
    tkinter.Label(u2, text='Title').grid(row=1, column=0)
    q = tkinter.Entry(u2)
    q.grid(row=1, column=1)
    tkinter.Label(u2, text='Ended').grid(row=2, column=0)
    v = tkinter.Entry(u2)
    v.grid(row=2, column=1)
    tkinter.Button(u2, text='UPDATE', width=10, command=uTitle).grid(row=3, column=1)
    u2.update()
def uRatings():
    global u33
    global s1
    global v
    global u
    global cursor
    global connection
    value1 = v.get()
    value2 = u.get()
    u33.destroy()
    if value1 is not '' and value2 is not '':
        v1 = int(value1)
        v2 = int(value2)
        cursor.execute("SELECT rating, votes FROM ratings where title_id = \'" + s1 + "\'")
        rate = 0
        vote = 0
        for (ra, vo) in cursor:
            rate = ra
            vote = vo
        rate = (v1 * (v2/(v2+vote))) + (rate *(vote/(v2+vote)))
        vote = vote + v2
        cursor.execute("UPDATE ratings SET rating = \'" + str(rate) + "\' where title_id = \'" + s1 + "\'")
        connection.commit()
        cursor.execute("UPDATE ratings SET votes = \'" + str(vote) + "\' where title_id = \'" + s1 + "\'")
        connection.commit()
        e = tkinter.Tk()
        e.minsize(260, 40)
        e.title('Updated Rating')
        tkinter.Label(e, text='Rating Entry has been updated').pack()
        button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
        button.pack()
    else:
        e = tkinter.Tk()
        e.minsize(260, 40)
        e.title('Error')
        tkinter.Label(e, text='Not all fields were filled').pack()
        button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
        button.pack()
def updateRatings2():
    global u33
    global u3
    global q
    global s1
    global v
    global u
    global cursor
    s1 = q.get()
    u3.destroy()
    try:
        if s1 is not '':
            cursor.execute("SELECT title_id, primary_title FROM titles WHERE primary_title = \'" + s1 + "\'")
            s1 = 'NULL'
            show = 'NULL'
            for (tid, s) in cursor:
                s1 = tid
                show = s
            cursor.execute("SELECT title_id, rating FROM ratings where title_id = \'" + s1 + "\'")
            rating = 'NULL'
            for (tid, n) in cursor:
                rating = tid
            if rating is 'NULL':
                e = tkinter.Tk()
                e.minsize(260, 40)
                e.title('Error')
                tkinter.Label(e, text='No rating exists for title').pack()
                button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                button.pack()
            else:
                u33 = tkinter.Tk()
                u33.title('Update Rating')
                u33.minsize(300, 50)
                tkinter.Label(u33, text='Update Values based on voter weight').grid(row=0)
                tkinter.Label(u33, text='Add Rating').grid(row=1, column=0)
                v = tkinter.Entry(u33)
                v.grid(row=1, column=1)
                tkinter.Label(u33, text='Add Voters').grid(row=2, column=0)
                u = tkinter.Entry(u33)
                u.grid(row=2, column=1)
                tkinter.Button(u33, text='UPDATE', width=10, command=uRatings).grid(row=3, column=1)
        else:
            e = tkinter.Tk()
            e.minsize(260, 40)
            e.title('Error')
            tkinter.Label(e, text='Not all fields were filled').pack()
            button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
            button.pack()
    except mysql.connector.Error as err:
        e = tkinter.Tk()
        e.minsize(260, 40)
        e.title('Error')
        tkinter.Label(e, text=err).pack()
        button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
        button.pack()
def updateRatings():
    global u3
    global q
    u3 = tkinter.Tk()
    u3.title('Update Rating')
    u3.minsize(300, 50)
    tkinter.Label(u3, text='Select the Entry to Modify').grid(row=0)
    tkinter.Label(u3, text='Title').grid(row=1, column=0)
    q = tkinter.Entry(u3)
    q.grid(row=1, column=1)
    tkinter.Button(u3, text='Submit', width=10, command=updateRatings2).grid(row=3, column=1)
def uCrew():
    global u44
    global s1
    global s2
    global u
    global uu
    global cursor
    global connection
    value1 = u.get()
    value2 = uu.get()
    u44.destroy()
    if value1 is not '' or value2 is not '':
        if value1 is not '':
            cursor.execute("UPDATE crew SET category = \'" + value1 + "\' where title_id = \'" + s1 + "\' and person_id = \'" + s2 + "\'")
            connection.commit()
        if value2 is not '':
            cursor.execute("UPDATE crew SET job = \'" + value2 + "\' where title_id = \'" + s1 + "\' and person_id = \'" + s2 + "\'")
            connection.commit()
        e = tkinter.Tk()
        e.minsize(260, 40)
        e.title('Updated Crew')
        tkinter.Label(e, text='Crew Entry has been updated').pack()
        button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
        button.pack()
    else:
        e = tkinter.Tk()
        e.minsize(260, 40)
        e.title('Error')
        tkinter.Label(e, text='No fields were filled').pack()
        button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
        button.pack()
def updateCrew2():
    global u4
    global u44
    global q
    global v
    global u
    global uu
    global s1
    global s2
    global cursor
    s1 = q.get()
    s2 = v.get()
    u4.destroy()
    try:
        if s1 is not '' and s2 is not '':
            cursor.execute("SELECT title_id, primary_title FROM titles WHERE primary_title = \'" + s1 + "\'")
            s1 = 'NULL'
            show = 'NULL'
            for (tid, s) in cursor:
                s1 = tid
                show = s
            cursor.execute("SELECT person_id, name FROM people WHERE name = \'" + s2 + "\'")
            s2 = 'NULL'
            name = 'NULL'
            for (pid, n) in cursor:
                s2 = pid
                name = n
            cursor.execute("SELECT title_id, person_id FROM crew where title_id = \'" + s1 + "\' and person_id = \'" + s2 + "\'")
            crew = 'NULL'
            for (pid, n) in cursor:
                crew = pid + n
            if crew is 'NULL':
                e = tkinter.Tk()
                e.minsize(260, 40)
                e.title('Error')
                tkinter.Label(e, text='No crew exists').pack()
                button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
                button.pack()
            else:
                u44 = tkinter.Tk()
                u44.title('Update Crew')
                u44.minsize(300, 50)
                tkinter.Label(u44, text='Update Values').grid(row=0)
                tkinter.Label(u44, text='Category').grid(row=1, column=0)
                u = tkinter.Entry(u44)
                u.grid(row=1, column=1)
                tkinter.Label(u44, text='Job').grid(row=2, column=0)
                uu = tkinter.Entry(u44)
                uu.grid(row=2, column=1)
                tkinter.Button(u44, text='UPDATE', width=10, command=uCrew).grid(row=3, column=1)
        else:
            e = tkinter.Tk()
            e.minsize(260, 40)
            e.title('Error')
            tkinter.Label(e, text='Not all fields were filled').pack()
            button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
            button.pack()
    except mysql.connector.Error as err:
        e = tkinter.Tk()
        e.minsize(260, 40)
        e.title('Error')
        tkinter.Label(e, text=err).pack()
        button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
        button.pack()
def updateCrew():
    global u4
    global q
    global v
    u4 = tkinter.Tk()
    u4.title('Update Crew')
    u4.minsize(300, 50)
    tkinter.Label(u4, text='Select the Entry to Modify').grid(row=0)
    tkinter.Label(u4, text='Title').grid(row=1, column=0)
    q = tkinter.Entry(u4)
    q.grid(row=1, column=1)
    tkinter.Label(u4, text='Name').grid(row=2, column=0)
    v = tkinter.Entry(u4)
    v.grid(row=2, column=1)
    tkinter.Button(u4, text='Submit', width=10, command=updateCrew2).grid(row=3, column=1)
def gSauce():
    global cursor
    random = randint(0, 10000)
    cursor.execute("select primary_title, premiered, ended, rating, votes, name, born, died, category "
                    "from titles inner join ratings on titles.title_id = ratings.title_id "
                    "inner join crew on crew.title_id = titles.title_id inner join people on "
                    "people.person_id = crew.person_id limit 10000")
    current = 0
    suggestion = ''
    suggestion2 = ''
    for (one, two, three, four, five, six, seven, eight, nine) in cursor:
        if current == random:
            suggestion = ("We recommend " + one + " which showed on " + str(two))
            if three is not None:
                suggestion = suggestion + " and ended on " + str(three)
            suggestion = suggestion + ". "
            if four is not None:
                suggestion = suggestion + "It has a rating of " + str(four)
            if five is not None:
                suggestion = suggestion + " under a group of " + str(five) + " voters"
            if six is not None:
                suggestion2 = "It has " + six
            if seven is not None:
                suggestion2 = suggestion2 + " who was born on " + str(seven)
            if eight is not None:
                suggestion2 = suggestion2 + " and died on " + str(eight)
            suggestion2 = suggestion2 + ". "
            if nine is not None:
                suggestion2 = suggestion2 + " their role was " + nine + "."
        current = current + 1
    sauce = tkinter.Tk()
    sauce.title('Media Suggestion')
    sauce.minsize(600,50)
    tkinter.Label(sauce, text=suggestion).pack()
    tkinter.Label(sauce, text=suggestion2).pack()
    tkinter.Button(sauce, text='Awesome!', command=sauce.destroy).pack()
def madlad():
    global cursor
    cursor.execute("SELECT title_id, primary_title from titles limit 5000")
    random = randint(0, 5000)
    value1 = ''
    count = 0
    for(one, two) in cursor:
        if count == random:
            value1 = two
        count = count + 1
    cursor.execute("SELECT premiered, ended from titles limit 5000")
    random = randint(0, 5000)
    value2 = ''
    value3 = ''
    count = 0
    for (one, two) in cursor:
        if count == random:
            if one is not None:
                value2 = str(one)
            if two is not None:
                value3 = str(two)
        count = count + 1
    cursor.execute("SELECT person_id, name from people limit 5000")
    random = randint(0, 5000)
    value4 = ''
    count = 0
    for (one, two) in cursor:
        if count == random:
            value4 = two
        count = count + 1
    random = randint(0, 5000)
    value5 = ''
    value6 = ''
    count = 0
    cursor.execute("SELECT born, died from people limit 5000")
    for (one, two) in cursor:
        if count == random:
            if one is not None:
                value5 = str(one)
            if two is not None:
                value6 = str(two)
        count = count + 1
    random = randint(0, 5000)
    value7 = ''
    count = 0
    cursor.execute("SELECT title_id, category from crew limit 5000")
    for (one, two) in cursor:
        if count == random:
            value7 = two
        count = count + 1
    suggestion = "Wassup mate! Oh snap I just remembered, have you heard about "
    suggestion2 = "It might be strange but I think that the piece "
    suggestion3 = "I know for certain that this person "
    if value7 is not '':
        suggestion = suggestion + value7 + " "
    if value4 is not '':
        suggestion = suggestion + value4 + ". "
    suggestion = suggestion + "Who was kinda in that one bit in " + value1 + ". "
    if value2 is not '':
        suggestion2 = suggestion2 + "aired on " + value2
    if value3 is not '':
        suggestion2 = suggestion2 + " and the show finally died because of that once incident on " + value3
    suggestion2 = suggestion2 + "."
    if value5 is not '':
        suggestion3 = suggestion3 + "came into this world on " + value5
    if value6 is not '':
        suggestion3 = suggestion3 + " and they bit the dust on " + value6
    suggestion3 = suggestion3 + ", was chill."
    sauce = tkinter.Tk()
    sauce.title('Cool Radical Dude on the Beach')
    sauce.minsize(600, 50)
    tkinter.Label(sauce, text=suggestion).pack()
    tkinter.Label(sauce, text=suggestion2).pack()
    tkinter.Label(sauce, text=suggestion3).pack()
    tkinter.Button(sauce, text='Huh?', command=sauce.destroy).pack()
def initalize(money, firstTimeStart):
    global e1
    global e2
    global e3
    global e4
    global r
    global connection
    connection = money
    r.destroy()
    if firstTimeStart == '0':
        m = tkinter.Tk()
        m.title('Creating Tables')
        m.minsize(260, 100)
        tkinter.Label(m, text='First time runtime; Setting up database tables.').grid(row=0)
        tkinter.Label(m, text='Please Wait!').grid(row=1)
        tkinter.Label(m, text='          ***          ').grid(row=2)
        tkinter.Label(m, text='          Creating titles table          ').grid(row=3)
        m.update()
        cash = money.cursor()
        cash.execute(
            "CREATE TABLE `titles` ("
            "`title_id` varchar(10) CHARACTER SET latin1 NOT NULL PRIMARY KEY,"
            "`type` varchar(15) CHARACTER SET latin1 DEFAULT NULL,"
            "`primary_title` varchar(400) CHARACTER SET latin1 DEFAULT NULL,"
            "`original_title` varchar(400) CHARACTER SET latin1 DEFAULT NULL,"
            "`is_adult` int(11) DEFAULT NULL,"
            "`premiered` int(11) DEFAULT NULL,"
            "`ended` int(11) DEFAULT NULL,"
            "`runtime_minutes` int(11) DEFAULT NULL,"
            "`genres` varchar(32) CHARACTER SET latin1 DEFAULT NULL"
            ") ENGINE=innodb;"
        )
        tkinter.Label(m, text='          ******          ').grid(row=2)
        tkinter.Label(m, text='          Creating person table          ').grid(row=3)
        m.update()
        cash.execute(
            "CREATE TABLE `person` ("
            "`my_id` int primary key,"
            "`my_name` char(14) unique"
            ")ENGINE=innodb;"
        )
        tkinter.Label(m, text='          Adding Charles          ').grid(row=3)
        m.update()
        cash.execute("INSERT INTO person (my_id, my_name) VALUES(%s,%s)", ('0', 'Charles Pelton'))
        tkinter.Label(m, text='          *********          ').grid(row=2)
        tkinter.Label(m, text='          Creating people table          ').grid(row=3)
        m.update()
        cash.execute(
            "CREATE TABLE `people` ("
            "`person_id` varchar(10) CHARACTER SET latin1 NOT NULL PRIMARY KEY,"
            "`name` varchar(105) CHARACTER SET latin1 DEFAULT NULL,"
            "`born` int(11) DEFAULT NULL,"
            "`died` int(11) DEFAULT NULL,"
            "`me` char(14) DEFAULT 'Charles Pelton',"
            "FOREIGN KEY (me) REFERENCES person(my_name)"
            ") ENGINE=innodb;"
        )
        tkinter.Label(m, text='          ************          ').grid(row=2)
        tkinter.Label(m, text='          Creating episodes table          ').grid(row=3)
        m.update()
        cash.execute(
            "CREATE TABLE `episodes` ("
            "`episode_title_id` varchar(10) CHARACTER SET latin1 DEFAULT NULL,"
            "`show_title_id` varchar(10) CHARACTER SET latin1 DEFAULT NULL,"
            "`season_number` int(11) DEFAULT NULL,"
            "`episode_number` int(11) DEFAULT NULL,"
            " FOREIGN KEY (show_title_id) REFERENCES titles(title_id)"
            ") ENGINE=innodb;"
        )
        tkinter.Label(m, text='          ***************          ').grid(row=2)
        tkinter.Label(m, text='          Creating ratings table          ').grid(row=3)
        m.update()
        cash.execute(
            "CREATE TABLE `ratings` ("
            "`title_id` varchar(10) CHARACTER SET latin1 DEFAULT NULL,"
            "`rating` float DEFAULT NULL,"
            "`votes` int(11) DEFAULT NULL,"
            "FOREIGN KEY (`title_id`) REFERENCES titles(title_id)"
            ") ENGINE=innodb;"
        )
        tkinter.Label(m, text='          ***************          ').grid(row=2)
        tkinter.Label(m, text='          Creating akas table          ').grid(row=3)
        m.update()
        cash.execute(
            "CREATE TABLE `akas` ("
            "`title_id` varchar(10) CHARACTER SET latin1 DEFAULT NULL,"
            "`title` varchar(553) CHARACTER SET latin1 DEFAULT NULL,"
            "`region` varchar(4) CHARACTER SET latin1 DEFAULT NULL,"
            "`language` varchar(3) CHARACTER SET latin1 DEFAULT NULL,"
            "`types` varchar(16) CHARACTER SET latin1 DEFAULT NULL,"
            "`attributes` varchar(62) CHARACTER SET latin1 DEFAULT NULL,"
            "`is_original_title` int(11) DEFAULT NULL,"
            "FOREIGN KEY (`title_id`) REFERENCES titles(title_id)"
            ") ENGINE=innodb;"
        )
        tkinter.Label(m, text='          ******************          ').grid(row=2)
        tkinter.Label(m, text='          Creating crew table          ').grid(row=3)
        m.update()
        cash.execute(
            "CREATE TABLE `crew` ("
            "`title_id` varchar(10) CHARACTER SET latin1,"
            "`person_id` varchar(10) CHARACTER SET latin1,"
            "`category` varchar(20) CHARACTER SET latin1 DEFAULT NULL,"
            "`job` varchar(286) CHARACTER SET latin1 DEFAULT NULL,"
            "PRIMARY KEY (title_id,  person_id),"
            "FOREIGN KEY (title_id) REFERENCES titles(title_id),"
            "FOREIGN KEY (person_id) REFERENCES people(person_id)"
            ") ENGINE=innodb;"
        )
        money.commit()
        m.title('Inserting Data')
        tkinter.Label(m, text='First time runtime; Setting up database entries.').grid(row=0)
        tkinter.Label(m, text='                    ***                    ').grid(row=2)
        tkinter.Label(m, text='          Adding titles          ').grid(row=3)
        m.update()
        cash_data = csv.reader(open('titles_5000.csv', encoding='utf-8'))
        i = 0
        x = 0
        for rows in cash_data:
            if i == 1:
                for item in rows:
                    if (item == ''):
                        rows[x] = None
                    x = x + 1
                cash.execute(title, rows)
                x = 0
            else:
                i = 1
        money.commit()
        tkinter.Label(m, text='          ******          ').grid(row=2)
        tkinter.Label(m, text='          Adding people          ').grid(row=3)
        m.update()
        cash_data = csv.reader(open('people_5000.csv', encoding='utf-8'))
        i = 0
        x = 0
        for rows in cash_data:
            if i == 1:
                for item in rows:
                    if (item == ''):
                        rows[x] = None
                    x = x + 1
                cash.execute(people, rows)
                x = 0
            else:
                i = 1
        money.commit()
        tkinter.Label(m, text='          *********          ').grid(row=2)
        tkinter.Label(m, text='          Adding episodes          ').grid(row=3)
        m.update()
        cash_data = csv.reader(open('episodes_5000.csv', encoding='utf-8'))
        i = 0
        x = 0
        for rows in cash_data:
            if i == 1:
                for item in rows:
                    if (item == ''):
                        rows[x] = None
                    x = x + 1
                cash.execute(episode, rows)
                x = 0
            else:
                i = 1
        money.commit()
        tkinter.Label(m, text='          ************          ').grid(row=2)
        tkinter.Label(m, text='          Adding akas          ').grid(row=3)
        m.update()
        cash_data = csv.reader(open('akas_5000.csv', encoding='utf-8'))
        i = 0
        x = 0
        for rows in cash_data:
            if i == 1:
                for item in rows:
                    if (item == ''):
                        rows[x] = None
                    x = x + 1
                try:
                    cash.execute(akas, rows)
                except mysql.connector.Error as err:
                    x = 0
                x = 0
            else:
                i = 1
        money.commit()
        tkinter.Label(m, text='          ***************          ').grid(row=2)
        tkinter.Label(m, text='          Adding ratings          ').grid(row=3)
        m.update()
        cash_data = csv.reader(open('ratings_5000.csv', encoding='utf-8'))
        i = 0
        x = 0
        for rows in cash_data:
            if i == 1:
                for item in rows:
                    if (item == ''):
                        rows[x] = None
                    x = x + 1
                cash.execute(rating, rows)
                x = 0
            else:
                i = 1
        money.commit()
        tkinter.Label(m, text='          ******************          ').grid(row=2)
        tkinter.Label(m, text='          Adding crew          ').grid(row=3)
        m.update()
        cash_data = csv.reader(open('crew_5000.csv', encoding='utf-8'))
        i = 0
        x = 0
        for rows in cash_data:
            if i == 1:
                for item in rows:
                    if (item == ''):
                        rows[x] = None
                    x = x + 1
                cash.execute(crew, rows)
                x = 0
            else:
                i = 1
        money.commit()
        m.destroy()
    global cursor
    global main
    cursor = money.cursor()
    main = tkinter.Tk()
    main.title('IMDB Interface')
    main.minsize(680, 300)
    menu = tkinter.Menu(main)
    main.config(menu=menu)
    createmenu = tkinter.Menu(menu)
    menu.add_cascade(label='Create', menu=createmenu)
    createmenu.add_command(label='Person', command=createPerson)
    createmenu.add_command(label='Title', command=createTitle)
    createmenu.add_command(label='Rating', command=createRating)
    createmenu.add_command(label='Episodes', command=createEpisode)
    createmenu.add_command(label='Crew', command=createCrew)
    createmenu.add_command(label='Akas', command=createAkas)
    querymenu = tkinter.Menu(menu)
    menu.add_cascade(label='Query', menu=querymenu)
    querymenu.add_command(label='Person', command=queryPerson)
    querymenu.add_command(label='Title', command=queryTitle)
    querymenu.add_command(label='Rating', command=queryRating)
    querymenu.add_command(label='Episodes', command=queryEpisode)
    querymenu.add_command(label='Crew', command=queryCrew)
    querymenu.add_command(label='Akas', command=queryAkas)
    umenu = tkinter.Menu(menu)
    menu.add_cascade(label='Update', menu=umenu)
    umenu.add_command(label='Person', command=updatePerson)
    umenu.add_command(label='Title', command=updateTitle)
    umenu.add_command(label='Rating', command=updateRatings)
    umenu.add_command(label='Crew', command=updateCrew)
    dmenu = tkinter.Menu(menu)
    menu.add_cascade(label='Delete', menu=dmenu)
    dmenu.add_command(label='Person', command=deletePerson)
    dmenu.add_command(label='Title', command=deleteTitle)
    dmenu.add_command(label='Rating', command=deleteRating)
    dmenu.add_command(label='Episodes', command=deleteEpisode)
    dmenu.add_command(label='Crew', command=deleteCrew)
    dmenu.add_command(label='Akas', command=deleteAkas)
    exitmenu = tkinter.Menu(menu)
    menu.add_cascade(label='Options', menu=exitmenu)
    exitmenu.add_command(label='Delete Database', command=confirmDeletion)
    exitmenu.add_command(label='Exit', command=main.destroy)
    special = tkinter.Menu(menu)
    menu.add_cascade(label='Special Features', menu=special)
    special.add_command(label='Generate Sauce', command=gSauce)
    special.add_command(label='Madlibs', command=madlad)
    x = 0
    y = 0
    while x < 31:
        while y < 8:
            tkinter.Label(main, width=20, relief=tkinter.RIDGE).grid(row=x, column=y)
            y = y + 1
        x = x + 1
        y = 0
    tkinter.Label(main, width=20, text='General Queries:').grid(row=31, column=0)
    tkinter.Button(main,  width=15, text='People', command=qPeople).grid(row=31, column=1)
    tkinter.Button(main, width=15, text='People Ordered A...Z', command=qPeople2).grid(row=31, column=2)
    tkinter.Button(main, width=15, text='People Ordered Z...A', command=qPeople3).grid(row=31, column=3)
    tkinter.Button(main,  width=15, text='Titles', command=qTitles).grid(row=31, column=4)
    tkinter.Button(main, width=15, text='Titles Ordered A...Z', command=qTitles2).grid(row=31, column=5)
    tkinter.Button(main, width=15, text='Titles Ordered Z...A', command=qTitles3).grid(row=31, column=6)
    tkinter.Button(main, width=15, text='Titles with End Dates', command=qTitles4).grid(row=31, column=7)
    main.mainloop()

def login():
    global e1
    global e2
    global e3
    global e4
    global r
    try:
        money = mysql.connector.connect(
        host=e1.get(),
        user=e3.get(),
        password=e4.get(),
        database='imdb',
        auth_plugin='mysql_native_password')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            e = tkinter.Tk()
            e.minsize(260, 40)
            e.title('Error')
            tkinter.Label(e, text='user name or password is incorrect').pack()
            button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
            button.pack()
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            money = mysql.connector.connect(
            host=e1.get(),
            user=e3.get(),
            password=e4.get(),
            auth_plugin='mysql_native_password')
            cash = money.cursor()
            cash.execute("CREATE DATABASE imdb")
            time.sleep(3)
            money = mysql.connector.connect(
                host=e1.get(),
                user=e3.get(),
                password=e4.get(),
                database='imdb',
                auth_plugin='mysql_native_password')
            initalize(money, '0')
        else:
            e = tkinter.Tk()
            e.minsize(260, 40)
            e.title('Error')
            tkinter.Label(e, text=err).pack()
            button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
            button.pack()
    else:
        initalize(money, '1')


def start():
    global r
    r = tkinter.Tk()
    r.title('Database Login')
    r.minsize(260, 100)
    tkinter.Label(r, text='host').grid(row=0)
    tkinter.Label(r, text='user').grid(row=1)
    tkinter.Label(r, text='password').grid(row=2)
    global e1
    global e3
    global e4
    e1 = tkinter.Entry(r)
    e3 = tkinter.Entry(r)
    e4 = tkinter.Entry(r)
    e1.grid(row=0, column=1)
    e3.grid(row=1, column=1)
    e4.grid(row=2, column=1)
    tkinter.Button(r, text='Login', command=login).grid(row=3, column=1)
    r.mainloop()

start()