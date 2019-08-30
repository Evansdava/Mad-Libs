import random
from pattern.text.en import pluralize, conjugate

# Check the part of speech of words
def get_type(key):
    type = key.lower()
    type = type.split("_")[0]
    
    return type


# Cycle through dictionary, get user inputs in a random order
def get_words(dict):
    keys = list(dict.keys())
    random.shuffle(keys)

    # Loop inspired by Austin Marshall on Stack Overflow 
    # https://stackoverflow.com/questions/7785672/how-to-iterate-through-dict-in-random-order-in-python
    for key in keys:
       while dict[key] == "" and key != "NOUN_2P":
            if key.startswith("A"):
                dict[key] = input("Please input an " + get_type(key) + ": ")
            else:
                dict[key] = input("Please input a " + get_type(key) + ": ")

            if dict[key] == "":
                print("I didn't get that. Please try again")

    dict["NOUN_2P"] = pluralize(dict["NOUN_2"])
    dict["VERB_1P"] = conjugate(dict["VERB_1"], "inf")


# Replace all words in the story
def replace_words(story, dict):
    new_story = story
    for key in dict:
        new_story = new_story.replace("["+key+"]", dict[key])

    return new_story

# List of keys that will be used for replacement
word_dict = {
    "NAME": "",
    "NOUN_1": "",
    "NOUN_2": "",
    "NOUN_2P": "",
    "NOUN_3": "",
    "NOUN_4": "",
    "PLURAL NOUN_1": "",
    "PLURAL NOUN_2": "",
    "VERB_1P": "",
    "VERB_1": "",
    "VERB_2": "",
    "VERB_3": "",
    "FIELD OF STUDY": "",
    "ADJECTIVE_1": "",
    "ADVERB_1": "",
    }

# Original version of story
og_story = """
    Isaac Asimov's "Three Laws of Robotics"

    1. A robot may not injure a human being or, through inaction, allow a human
       being to come to harm.

    2. A robot must obey orders given it by human beings except where such
       orders would conflict with the First Law.

    3. A robot must protect its own existence as long as such protection does
       not conflict with the First or Second Law.

    These laws ensure that a society which relies heavily on robots does not
    fall victim to accidents on a horrific scale.
    """

# Story template ready to be libbed
template = """
    [NAME]'s "Three Laws of [FIELD OF STUDY]"

    1. A [NOUN_1] may not [VERB_1] a [NOUN_2] or, through inaction, allow a
       [NOUN_2] to be [VERB_1P].

    2. A [NOUN_1] must obey [PLURAL NOUN_1] given it by [NOUN_2P] except where
       such [PLURAL NOUN_1] would conflict with the First Law.

    3. A [NOUN_1] must [VERB_2] its own [NOUN_4] as long as such [VERB_2] does
       not conflict with the First or Second Law.

    These laws ensure that a [NOUN_3] which relies [ADVERB_1] on [NOUN_1] does
    not [VERB_3] to [PLURAL NOUN_2] on a [ADJECTIVE_1] scale.
    """

get_words(word_dict)
print(replace_words(template, word_dict))
