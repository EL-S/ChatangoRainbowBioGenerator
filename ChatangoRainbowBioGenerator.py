import re, urllib.request,urllib.parse,math
username = "your chatango login" #this doesn't work, I don't know how to fix it
password = "your chatango password" #same as above
text = "I like rainbows" #the text to make rainbow
mode = "letters" #letters or words, use words if you hit the character limit!!!!!
change = 1 #how many words per colour!!! (use 1 if letters, just in case it is buggy)

 
def rainbow(word):
    count = len(word)
    group = []
    if mode == "letters":
        group = word
    elif mode == "words":
        words = word.split(" ")
        count = math.ceil(len(words))
        for i in range(0, count, change):
            wordss = ""
            try:
                for j in range(i, i+change):
                    if j == 0:
                        wordss += words[j]
                    else:
                        wordss += " " + words[j]
                    if j == (i+change-1):
                        group.append(wordss)
            except:
                group.append(wordss)
    count = len(group)
    #set rgb values
    r = 255 #rgb value set to red by default
    g = 0
    b = 0
    sub = int(765/count)
    counter = 0
    string = ""
    for x in range(0, count):
        letter = group[counter]
        s = "<f x12%02X%02X%02X='0'>%s" % (r, g, b, letter)
        string = string+s
        counter+=1
        if (r == 255) and (g >= 0) and (b == 0): #if all red
            g = g+sub
            if g > 255: g = 255
        if (r > 0) and (g == 255) and (b == 0): #if some red and all green
            r = r-sub #reduce red to fade from yellow to green
            if r<0: r = 0 #if red gets lower than 0, set it back to 0
        if (r == 0) and (g == 255) and (b >= 0):
            b = b+sub
            if b>255:
                b = 255
                trans = True
        if (r == 0) and (g > 0) and (b == 255):
            g = g-sub
            if g<0: g = 0
        if (r >= 0) and (g == 0) and (b == 255):
            r = r+sub
            if r>255: r = 255
    return str(string).replace("<f x12","<font color=\"#").replace("='0'","\"")
print(rainbow(text)) #print the converted rainbow string

#uncomment below section if you for some reason want to try login stuff anyway (it doesn't work lol)
"""
def authToken(u, p):
 token = urllib.request.urlopen("http://chatango.com/login", urllib.parse.urlencode({"user_id": username.lower(), "password": password, "storecookie": "on", "checkerrors": "yes" }).encode()).getheader("Set-Cookie")
 
 return re.search("auth.chatango.com=(.*?);", token).group(1)
print(authToken(username,password))
def edit_profile(u,p,edit):
     token = authToken(username, password)
     url = "http://%s.chatango.com/updateprofile?flash&d&s=%s" % (username.lower(), token)
     Data = urllib.parse.urlencode({"checkerrors": "yes", "full_profile": "", "uns":"1","line":rainbow(edit),"email": "Email Here", "location":"","gender":"M","age":"99"}).encode()
     headers = {"Cookie":"auth.chatango.com=%s" % token}
     req = urllib.request.Request(url, data=Data, headers=headers)
     urllib.request.urlopen(req)
     print("successful")
edit_profile(username,password,text)
"""
