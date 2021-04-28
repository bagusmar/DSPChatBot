import csv
import random
import datetime
from tkinter import *

##Try to import a google search function into the system
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

##Make a basic grahpical user interface
root = Tk()
root.title("Python Chatting Apps")

##Arrays needed to make sure that only valid letters are present
alphabet = []
sentence = []
alphabetList = []

##Arrays needed for the greetings that the system will recognised
greeting = []
greetingList = []

##Arrays needed for the French greetings that the system will recognised
greetingFR = []
greetingFRList = []

##Arrays needed for the Spanish greetings that the system will recognised
greetingSpa = []
greetingSpaList = []

##Arrays needed for the goodbyes that the system will recognised
goodbye = []
goodbyeList = []

##Arrays needed for the positive adjectives that the system will recognised
modPost = []
modPostList = []

##An array that will be used to store definitions of an inputted phrase
definitionList = []

##An array that will be used to store definitions of a response
responseList = []

##Make a 2D Array from a CSV file
with open('alphabet.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        alphabet.append(row)

##Make a 1D Array from the previous 2D Array
for i in range(len(alphabet)):
    alphabetList.append(alphabet[i][0])

##Greetings
##Make a 2D Array from a CSV file
with open('greetings.csv', 'r') as file2:
    reader2 = csv.reader(file2)
    for row in reader2:
        greeting.append(row)

##Make a 1D Array from the previous 2D Array
for i in range(len(greeting)):
    greetingList.append(greeting[i][0])

##Greetings French
##Make a 2D Array from a CSV file
with open('greetingsFR.csv', 'r') as file6:
    reader6 = csv.reader(file6)
    for row in reader6:
        greetingFR.append(row)

##Make a 1D Array from the previous 2D Array
for i in range(len(greetingFR)):
    greetingFRList.append(greetingFR[i][0])

##Greetings Spanish
##Make a 2D Array from a CSV file
with open('greetingsSpa.csv', 'r') as file7:
    reader7 = csv.reader(file7)
    for row in reader7:
        greetingSpa.append(row)

##Make a 1D Array from the previous 2D Array
for i in range(len(greetingFR)):
    greetingSpaList.append(greetingSpa[i][0])

    
##Words modifier positive
##Make a 2D Array from a CSV file
with open('modifierGood.csv', 'r') as file3:
    reader3 = csv.reader(file3)
    for row in reader3:
        modPost.append(row)

##Make a 1D Array from the previous 2D Array
for i in range(len(modPost)):
    modPostList.append(modPost[i][0])

##Words goodbye
##Make a 2D Array from a CSV file
with open('goodbye.csv', 'r') as file4:
    reader4 = csv.reader(file4)
    for row in reader4:
        goodbye.append(row)

##Make a 1D Array from the previous 2D Array
for i in range(len(goodbye)):
    goodbyeList.append(goodbye[i][0])


##Make an input box
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

##Make an output box
o = Entry(root, width=35, borderwidth = 5)
o.grid(row=3,column=0,columnspan=3,padx=10,pady=10)
b = Entry(root, width=35, borderwidth = 5)
b.grid(row=4,column=0,columnspan=3,padx=10,pady=10)

##A method that will be used if a date is asked for
def dateGetter():
    o.insert(0,"Current Time =" + datetime.datetime.now().strftime("%d/%m/%y"))

##A method that will be used if a time is asked for
def timeGetter():
    o.insert(0,"Current Time =" + datetime.datetime.now().strftime("%H:%M:%S"))

##A method that will be used if a query has been asked 
def whatChecker(sentence, i):
    ##Set the query so that it has yet been answered
    answerAlready = False
    ##Check if the query meet several criteria, including premade responses
    for a in range(i,len(sentence)):
        ##Check if query asks for time and has not been answered yet
        if sentence[a] == "time" and answerAlready == False:
            timeGetter()
            answerAlready = True
            
        ##Check if query asks for the date and has not been answered yet
        elif sentence[a] == "date" and answerAlready == False:
            dateGetter()
            answerAlready = True
            
    ##If the question has not been answered, then google search it
    if answerAlready == False:
        try:
            ##Retrieve the entire query
            query = e.get()
            ##Search the query from the internet
            newSearch = search(query, tld = "com", num = 1, stop = 1)            
            ##Take the first link produced by google
            for i in search(query,tld = "com",num=1,stop=1,pause=2):
                newSearch = i                
            ##Output the link
            b.insert(0,newSearch)
        ##If the search fails, then write an error message
        except:
            newLabel = Label(root, text = "I'm sorry, I cannot answer that currently, do you have an internet connection?")
            newLabel.grid(row=6,column=0)
        answerAlready = True

##Section handles the inputs and create responses
def getDef(sentence):
    ##Delete all outputs
    o.delete(0,END)
    b.delete(0,END)

    ##Set error checker
    counter = 0

    ##Check the contents of the system
    for i in range(len(sentence)):
        print(sentence[i])
        ##Check if there is no responses yet
        if counter == 0:
            ##Check if the input is a greeting in English
            if sentence[i] in greetingList:
                ##Randomly select a greeting
                o.insert(0,greetingList[random.randint(0,len(greetingList)-1)])
                ##Ask "how are you?"
                convo = "How are you?"
                ##Output the results
                b.insert(0, convo)
                ##Stop the program from responding again
                counter += 1

            ##Check if the input is a greeting in French
            elif sentence[i] in greetingFRList:
                ##Randomly select a greeting
                o.insert(0,greetingFRList[random.randint(0,len(greetingFRList)-1)])
                ##Ask "how are you?"
                convo = "Comment allez-vous?"
                ##Output the results
                b.insert(0, convo)
                ##Stop the program from responding again
                counter += 1

            ##Check if the input is a greeting in Spanish
            elif sentence[i] in greetingSpaList:
                ##Randomly select a greeting
                o.insert(0,greetingSpaList[random.randint(0,len(greetingSpaList)-1)])
                ##Ask "how are you?"
                convo = "¿Cómo estás?"
                ##Output the results
                b.insert(0, convo)
                ##Stop the program from responding again
                counter += 1

            elif sentence[i] == "how":
                ##Check if the input is "How are you?"
                if sentence[i+1] == "are":
                    if sentence [i+2] == "you":
                        ##Randomly select a positive response
                        o.insert(0,"I am " + modPostList[random.randint(0,len(modPostList)-1)])

                ##Check if the input is asking for some sort of review
                elif sentence[i+1] == "is":
                    ##Retrieve the entire query
                    query = e.get()
                    ##Search the query from the internet
                    newSearch = search(query, tld = "com", num = 1, stop = 1)
                    ##Take the first link produced by google
                    for i in search(query,tld = "com",num=1,stop=1,pause=2):
                        newSearch = i
                    ##Output the link
                    b.insert(0,newSearch)
                ##Stop the program from responding again
                counter += 1
            ##Check if the input is a query 
            elif sentence[i] == "what":
                whatChecker(sentence,i)
                ##Stop the program from responding again
                counter += 1
            ##Check if the input is a farewell
            elif sentence[i] in goodbyeList:
                ##Randomly chose a farewell
                o.insert(0,goodbyeList[random.randint(0, len(goodbyeList))])
                ##Stop the program from responding again
                counter += 1
    ##Check if the input is unanswered
    if counter ==0:
        o.insert(0, "Warning, something went wrong!")

##Method if the system receives an input
def buttonClick():
    ##reset the letters
    letters = []
    ##reset the sentence array
    sentence = []
    ##get new sentence
    newSentence = e.get()
    ##make the sentence lower case
    newSentence = newSentence.lower()
    ##split the sentences and turn it into arrays
    for i in range(len(newSentence)):
        if newSentence[i] in alphabetList:
            letters.append(newSentence[i])
        else:
            words = ''.join(letters)
            sentence.append(words)
            letters = []
            words = ''
    words = ''.join(letters)
    if words != '':
        sentence.append(words)
    ##send the sentences into the method to make sense of it
    getDef(sentence)

##initialise the GUI            
enterButton = Button(root, text= "Enter", padx=100, pady=10,command=buttonClick)
enterButton.grid(row=1, column=0)

##Root the GUI
root.mainloop()
