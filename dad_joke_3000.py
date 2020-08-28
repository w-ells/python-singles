   ____    _    ____        _  ___  _  _______   _____  ___   ___   ___
# |  _ \  / \  |  _ \      | |/ _ \| |/ / ____| |___ / / _ \ / _ \ / _ \
# | | | |/ _ \ | | | |  _  | | | | | ' /|  _|     |_ \| | | | | | | | | |
# | |_| / ___ \| |_| | | |_| | |_| | . \| |___   ___) | |_| | |_| | |_| |
# |____/_/   \_\____/   \___/ \___/|_|\_\_____| |____/ \___/ \___/ \___/
# This program was a challenge on the Udemy Python 3 Boot Camp course, taught
# by Colt Steel. I completed this program without assistance after watching the
# tutorial on python requests and queries. 28 Aug 2020



# Import Section
import requests
from pyfiglet import figlet_format
from termcolor import colored
from random import choice

# Definitions
url = "https://icanhazdadjoke.com/search"
logo_name = "DAD JOKE 3000"
color = "red"

def dad_joke(url="https://icanhazdadjoke.com/search", term=""):

	# Query URL for term. And convert response to python-readable from the json
	response = requests.get(url, headers={"Accept": "application/json"}, params={"term": term})
	data = response.json()

	# Figure out how many jokes and pages there are
	num_jokes = data["total_jokes"]
	num_pages = data["total_pages"]

	# Respond based on query results:
	if num_jokes == 0 or term== "":
		# Get a new random joke
		url = "https://icanhazdadjoke.com"
		response = requests.get(url, headers={"Accept":"application/json"})
		data = response.json()
		joke = data["joke"]
		return print(f"\nThere weren't any jokes about your input, so here is a random one: \n\n{joke}")

	elif num_jokes == 1:
		# Extract joke from data: dict, then list, then dict:
		joke = data["results"][0]["joke"]
		return print (f"\nI've one joke about your request, {term}. Here it is: \n\n{joke}")

	else:
		# make a request for one joke per page. randomly choose one page out of num_jokes
			joke_index= choice(range(num_jokes))+1
			response = requests.get(url,headers ={"Accept":"application/json"}, params={"term":term, "limit": 1, "page":joke_index})
			data = response.json()
			joke = data["results"][0]["joke"]
			print (f"\nJoke {joke_index} out of {num_jokes} randomly chosen about \"{term}\":\n")
			return print(joke)



# Header - Logo in ASCII art and in a color defined by "color"
big_letters = figlet_format(logo_name)
colored_big_letters = colored (big_letters, color)
print (colored_big_letters)

# User Input: Enter a term
term = input("Hello, we're going to tell you a joke. What should it be about? ")
dad_joke(url,term)
