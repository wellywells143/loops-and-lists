# Last week, you created your own list & dictionary. 
# This week, we will continue to work on these--this time, running loops on them!
# Using a loop enables you to take the same action or set of actions with every item in a list. This helps you work efficiently! 
# There are two types of loop structures for loops, which we will talk about today and while loops, which we will not talk about today but to push the dial
print("This is my exit ticket!")

# Part I. Loop through lists
# First, we'll learn how to loop through lists!
# Let's go back to our Spotify playlist, but this time it contains the tracklist for Beyonce's new album, Renaissance. 
playlist = [
  "I'm That Girl",
  "Alien Superstar",
  "Cuff It",
  "Energy",
  "Break My Soul",
  "Church Girl",
  "Plastic Off the Sofa",
  "Virgo's Groove",
  "Move",
  "Heated",
  "Thique",
  "All Up in Your Mind",
  "America Has a Problem",
  "Pure/Honey" ,
  "Summer Renaissance"
  ]

# Print the playlist in the line below:
print(playlist)

# How can we print out each song on this playlist individually? Retrieving each song can take forever (imagine if there were 100 songs!). We can do this efficiently by using a loop. Here's how to do that:
# Step 1: Define the list--we did this already!
# Step 2: Define the loop. We will use a FOR loop. This loop will tell Python to pull a song from the tracklist & associate with the variable jam. 
# Step 3: Print the song that's been assigned to jam
for song in playlist:
  print(song)

# You can customize a message for each element in your list using f-strings
for jam in playlist:
  print(f"{jam} is sooo fiiire!")

# Indented lines after "for jam in playlist" are INSIDE the loop. Each indented line is executed once for each value on the list.
# Here's an example of adding another indented line inside our loop. Note that \n prints a message in a new coding line.
for jam in playlist:
  print(f" {jam} is sooo fiiire!")
  print(f" How many streams do you think will {jam} have this summer? \n")

# # Now it's your turn to create your own list!
# # Think of at least 3 of your favorite shows right now and store the show titles in a list in the next line:
faveshows = [
  "Naruto",
  "Spy x Family",
  "Bob's Burgeers"
 ]
print(faveshows)
# # Now that you've defined your list, create a FOR loop that prints an f-string of a message that includes each show in your list, modeling your code after lines 38-39. An example output could be: "{show} is the best show ever!" Write this modified loop in the next 2 lines:
for show in faveshows:
  print(show)
  print(f" {show} is a great show!")
  print(f" {show} is one of the best shows!")
# # Now modify your FOR loop similar to lines 43-45. Write your FOR loop again but this time add this statement in a new code line (use \n): "How many streams do you think {show}" will have this year?" Write your modified FOR loop in the next few lines:
for fav in faveshows:
  print(fav)
  print(f" {fav} is so heart warming. \n")
  print(f" {fav} makes me so happy.")
  



# # We can also loop through a portion of a list or a slice. Accessing a slice uses the same indexing method that we've been using to retrieve elements of a list.
# # # For example, Beyonce's tracklist has 15 songs with "I'm That Girl" as the first song, which means that its index number would be 0. 
# # # To generate a subset, if you want the 2nd, 3rd, & 4th item in the list, you would start the slice at index 1 and end at index 4:
print(faveshows[0:2])
# # # In the next line, write down what songs showed up in the output:
# # #

# # # In the indexing you just did (playlist[1:4]), if you remove the first index (1), what songs do you think will be in the output? When you omit the first index like that, Python automatically starts your list at the beginning of the list:
print(playlist[:0])

# # # Similarly, if you remove the second index (4), what songs do you think will be in the output? When you omit the second index, Python automatically starts counting from the first index and includes the rest of the list. So, if your first index is 2, that means that your output will start at the element at location 2 (3rd element) and then print out the rest of the list from that location:
print(playlist[1:])

# # # How about if your index has a negative number? That just means that you are counting from the back of the list. That means if you put -3, the last three songs from the list will be printed in the output:
print(playlist[-1:])

# # # Now let's loop through a slice!
# # # Instead of looping through the entire list, you can loop through just a slice or subset of the whole list. 
# # # Why should we care about being able to create a subset and running a loop through it? It allows you to use slices to process data in chunks of a size that you can specify. 
# # # Here's an example of how to loop through a slice:
print("These are the first 3 songs in Beyonce's new album:")
for jam in playlist[:3]:
  print(jam)

# # # Now create a slice or subset of your list of favorite shows, then run a loop through your slice:
print("These are the first 2 shows of my showlist")
for show in faveshows[:2]:
  print(show)