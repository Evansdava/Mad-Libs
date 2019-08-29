import random
import inflect

# Inflect is used for pluralization functionality. Credit goes to Jazzband.
# https://pypi.org/project/inflect/
p = inflect.engine()

# Check the part of speech of words
def get_type(key):
    type = key.lower()
    type = type.split("_")[0]
    
    return type


# Cycle through dictionary, get user inputs in a random order
def get_words(dict):
    keys = list(dict.keys())
    random.shuffle(keys)

    for key in keys:
       while word_dict[key] == "":
         word_dict[key] = input("Please input a " + get_type(key) + ": ")
         if word_dict[key] == "":
            print("I didn't get that. Please try again")


# List of keys that will be used for replacement
word_dict = {
    "NAME": "",
    "NOUN_1": "",
    "NOUN_2": "",
    "NOUN_3": "",
    "PLURAL NOUN_1": "",
    "PLURAL NOUN_2": "",
    "VERB_1": "",
    "VERB_2": "",
    "VERB_3": "",
    "FIELD OF STUDY": "",
    "ADJECTIVE_1": "",
    "ADVERB_1": "",
    }

# Template for story
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

# Story ready to be libbed
story = """
    [NAME]'s "Three Laws of [FIELD OF STUDY]"

    1. A [NOUN_1] may not [VERB_1] a [NOUN_2] or, through inaction, allow a
       [NOUN_2] to [VERB_1].

    2. A [NOUN_1] must obey [PLURAL NOUN_1] given it by [NOUN_2] except where
       such [PLURAL NOUN_1] would conflict with the First Law.

    3. A [NOUN_1] must [VERB_2] its own [NOUN] as long as such [VERB_2] does
       not conflict with the First or Second Law.

    These laws ensure that a [NOUN_3] which relies [ADVERB_1] on [NOUN_1] does
    not [VERB_3] to [PLURAL NOUN_2] on a [ADJECTIVE_1] scale.
    """

get_words(word_dict)
print(word_dict)

print(p.plural(input()))
