import urllib

def locate_text():
    file_check = open("C:\Users\Arunkumaar\Desktop\Udacity\movie_quotes.txt")
    content = file_check.read()
    print(content)
    file_check.close()
    profanity_check(content)
    

def profanity_check(text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" +text)
    output = connection.read()
    #print(output)
    if "false" in output:
        print("You are good to go")
    elif "true" in output:
        print("Profanity Alert!!!")
    else:
        print("Error in reading file")
    connection.close()

locate_text()
