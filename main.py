import random
import requests
import webbrowser
#importing needed modules

#prints a title
print("Find working prnt.sc links!")

abc = ["a","b","c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
# just lists with charcters prob a more efficiant way to do it but yeah
countermax = int(input('How links would you like to generate? ')) # asks user how many it should have
openinbrowser = int(input('Would you like to open working links in default browser? [1. Yes/2. No] ')) # if user wants to open in a browser

counter = 0 # Counts succussful links
fail = 0 # counts connection errors
tries = 0 # counts how many tries it has done
while countermax > counter:
    url = "https://prnt.sc/" + abc[random.randint(0, len(abc)-1)] + abc[random.randint(0, len(abc)-1)] + abc[random.randint(0, len(abc)-1)] + abc[random.randint(0, len(abc)-1)] + abc[random.randint(0, len(abc)-1)]
    #generates urls
    try:
        req = requests.get(url, headers={'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"}) 
        # Custom User Agent specified because cloudflare/lightshot blocks python user agent for Firefox 108.0 on Linux x64 but this can be changed to whatever
        if req.text.find("i.imgur.com") >= 0 or req.text.find("https://image.prntscr.com/image/") >= 0:
            print(url)
            if openinbrowser == 1: #opens url if user wants this option
                webbrowser.open(url)
            counter+=1
    except requests.exceptions.ConnectionError:
        fail+=1 # if no internet or server goes down
    tries+=1
print(f"Found ({counter}/{countermax})") 
print(f"Tried ({counter}/{tries})")
