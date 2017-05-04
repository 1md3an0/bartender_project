def choose_your_palette():
    """
    This function requests the type of tastes the users would like in their drink
    """

    global taste_answers
    global valid_response
    global valid_response_yes
    global valid_response_no

    taste_answers = {
        }

    valid_response = {
        "Y": True,
        "y": True,
        "Yes": True,
        "yes": True,
        "YES": True,
        "N": False,
        "n": False,
        "No": False,
        "no": False,
        "NO": False,
        }

    valid_response_yes = {
        "Y": True,
        "y": True,
        "Yes": True,
        "yes": True,
        "YES": True,
        }
    
    valid_response_no = {
        "N": False,
        "n": False,
        "No": False,
        "no": False,
        "NO": False,
        }
        
    questions = {
        "strong": "Do ye like yer drinks strong?",
        "salty": "Do ye like it with a salty tang?",
        "bitter": "Are ye a lubber who likes it bitter?",
        "sweet": "Would ye like a bit of sweetness with yer poison?",
        "fruity": "Are ye one for a fruity finish?",
        }
    
    # Ask questions
    for key in questions:
        taste_reply = str(key) + "_input"
        taste_reply = input(questions[key]+" Y/N: ")
        taste_name = str(key)
        
    #Make sure responses are in the right format
        while (str(taste_reply) not in valid_response):
            print("      Arrrrrgh, that not be a proper arrrrrgghnswer.")
            print("      Try again!")
            taste_reply = input(questions[key]+" Y/N: ")

    # If correct format then proceed to make a new dictionary stating True
    # and False values next to "taste" Keys, e.g. " 'strong':False "
        taste_answers[taste_name] = valid_response[taste_reply]

def add_the_ingredients():
    """
    This function returns random ingredients respective to the user's requested tastes
    """
    import random

    # Ingredients dictionary
    ingredients = {
        "strong": ["glug of rum", "slug of whisky", "splash of gin"],
        "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
        "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
        "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
        "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
        }

    # For ease of reading for the user
    print("")

    # Extract pairs from taste_answers with True values 
    tastes_to_include = {k:v for k, v in taste_answers.items() if v }

    # If all answers are False then query
    if all(v == 0 for v in tastes_to_include.values()):
        no_taste_provided()
        
    print("Try mixing these in your next drink:")
    
    # Return corresponding ingredients for requested tastes
    for k in tastes_to_include:
        the_drink = random.choice(ingredients.get(k)) #ingredients.get(k)
        print(the_drink)

def no_taste_provided():
    """
    This function is called if the user has replied no to all the tastes queried 
    """
    # Allows the user to exit the entire script if they wish 
    import sys
    
    no_taste = input("Ye haven't picked a type of taste! Arrrr, can't I make you something? Y/N: ")

    while str(no_taste) not in valid_response:
        print("      Arrrrrgh, that not be a proper arrrrrgghnswer.")
        print("      Try again!")
        no_taste_provided()
        
    if str(no_taste) in valid_response_yes:
        make_a_drink()

    if str(no_taste) in valid_response_no:
        print("Bye then!")
        sys.exit()
    
def name_the_drink():
    """
    This function names the drink by randomly assigning an adjective with an animals name
    """
    # This allows me to apply the random function to create the drink name
    import random
    adjectives = ['Brave', 'Agreeable', 'Calm', 'Delightful',
                  'Eager', 'Faithful', 'Gentle', 'Happy', 'Jolly',
                  'Kind', 'Lively', 'Nice', 'Obedient', 'Proud',
                  'Relieved', 'Silly', 'Thankful', 'Victorious',
                  'Witty', 'Zealous', 'Angry', 'Bewildered', 'Clumsy',
                  'Defeated', 'Embarrassed', 'Fierce', 'Grumpy',
                  'Helpless', 'Itchy', 'Jealous', 'Lazy', 'Mysterious',
                  'Nervous', 'Obnoxious', 'Panicky', 'Repulsive',
                  'Scary', 'Thoughtless', 'Uptight', 'Worried'
                  ]
    
    animals = ['Bali Cattle', 'Alpaca', 'Cat', 'Cattle', 'Chicken',
               'Dog', 'Bactrian Camel', 'Canary', 'Dirty Camel', 'Duck',
               'Goat', 'Goose', 'Guineafowl', 'Hedgehog', 'Pig', 'Pigeon',
               'Rabbit', 'Silkmoth', 'Silver Fox', 'Turkey', 'Donkey',
               'Fancy Mouse', 'Lab Rat', 'Ferret', 'Gayal', 'Goldfish'
               ]
    
    drink_name = "Yaaarr, its name be {} {}! Drink up!".format(str(random.choice(adjectives)),str(random.choice(animals)))
    print("")
    print(drink_name)
    print("")

def make_a_drink():
    """
    This is the main function which calls the previous functions
    and asks the user if they would like another drink once one has been made
    """
    import sys

    choose_your_palette()
    add_the_ingredients()
    name_the_drink()

    make_another_drink = input("Would you like another drink? Y/N: ")

    #Make sure responses are in the right format
    while str(make_another_drink) not in valid_response:
        print("      Arrrrrgh, that not be a proper arrrrrgghnswer.")
        print("      Try again!")
        make_another_drink = input("Would you like another drink? Y/N: ")

    if str(make_another_drink) in valid_response_yes:
        print("")
        make_a_drink()

    if str(make_another_drink) in valid_response_no:
        print("Bye then!")
        sys.exit()


## -------------------------------------------------

if __name__ == '__main__':    
    make_a_drink()


def stock_counter():
    """
    Incomplete: this is part of the extension exercises which I
    will ask questions about
    
    Task: add a stock count for each ingredient which decreases whenever
    the bartender makes a drink.

    Question: I'm not sure whether I am understanding the task correctly -
    can values be stored between the script running or does it mean during
    one instance of the program running?
    
    """
        stock_of_ingredients = {
        "glug of rum":10,
        "slug of whisky":10,
        "splash of gin":10,
        "olive on a stick":20,
        "salt-dusted rim":20,
        "rasher of bacon":20,
        "shake of bitters":30,
        "splash of tonic":40,
        "twist of lemon peel":50,
        "sugar cube":100,
        "spoonful of honey":150,
        "spash of cola":60,
        "slice of orange":90,
        "dash of cassis":100,
        "cherry on top":40
        }
    
def multiple_customers():
    """

    Incomplete: this is part of the extension exercises which I
    will ask questions about

    Task: Multiple customers: The bartender could ask for the customer's name
    before they are served. They could then remember the customer's
    preferences for when the same customer asks for another drink.

    Question: I'm not sure whether I am understanding the task correctly -
    can names be stored between the script running?

    """
