# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "subscribe to ______ "
youtuber = "Samuwhy" # some string variable

# a few ways to do this
#print ("subscribe to " + youtuber)
#print ("subscribe to {}".format (youtuber))
#print (f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input ("Verb: ")
verb2 = input ("Verb: ")
Super_Hero = input ("Super Hero: ")

madlib = f"Going to the gym makes me feel {adj}! I love going because \
         I love to {verb1} Get {verb2} like I am {Super_Hero}!"

print(madlib)