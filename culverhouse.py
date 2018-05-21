# -*- coding: utf-8 -*-
"""
Created on Mon May 21 06:32:53 2018

@author: Kennard


"""

import wikipedia

list_names_1 = ['Trevor Hebberd','Ian Crook','Frank Yallop','Craig Forrest',
              'John Filan','Steve Anthrobus','John_Chiedozie','Paul Goddard',
              'Youssef Chippo','John Bumstead','Glyn Hodges','Ian Ormondroyd',
              'Ian Butterworth','Mike Milligan','Ian Culverhouse']
              
list_names_2 = ['Carl Shutt','Chris Kiwomya','Eddie McGoldrick',
              'Jason Dozzell','Eric Young','Reuben Agboola',"Mich D'avray",
              'Richard Sholl','Mustapha Hadji','Ian Brightwell','Ian Snodin',
              'Ian Olney','Peter Hucker','Andy Ritchie']

def birthday(query):
    bday = ' '
    try:
        result = wikipedia.page(query +' (footballer)')
        string = result.html()
        bday = string.partition('bday')[2][:12]
        bday = bday.partition('>')[2][:10]
        name = result.title
    except wikipedia.exceptions.DisambiguationError as e:
        bday='?'
    except wikipedia.exceptions.PageError as e:
        bday='?'
    return(name, bday) 

def birth_place(query):
    bplace = ' '
    try:
        result = wikipedia.page(query + ' (footballer)')
        string = result.html()
        bplace = string.partition('birthplace')[2][:180]
        bplace = bplace.partition('title')[2][2:40]
        bplace = bplace.partition('"')[0][:]     
    except wikipedia.exceptions.DisambiguationError as e:
        bplace = '?'
    except wikipedia.exceptions.PageError as e:
        bplace = '?'
    return(bplace)     
print("Max:")
for name in list_names_1:
    query= name
    print(birthday(query),birth_place(query))
print("Barry:")
for name in list_names_2:
    query= name
    print(name,birthday(query),birth_place(query))
