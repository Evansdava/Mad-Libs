def pluralize(string):
    str = string.lower()
    sec_last_let = len(str)-2

    # Check for adding "es"
    if (str.endswith("s") or str.endswith("sh")
            or str.endswith("x") or str.endswith("ch")):
        str = str + "es"

    # Check for consonant+y
    elif (str.endswith("y")) and (str[sec_last_let] != "a" and
                                  str[sec_last_let] != "e" and
                                  str[sec_last_let] != "i" and
                                  str[sec_last_let] != "o" and
                                  str[sec_last_let] != "u"):
        str = str[:len(str)-1] + "ies"

    # Default pluralization
    else:
        str = str + "s"

    return str


word_dict = {
    "NAME": "",
    "NOUN_1": "",
    "NOUN_2": "",
    "NOUN_3": "",
    "PL_NOUN_1": "",
    "PL_NOUN_2": "",
    "VERB_1": "",
    "VERB_2": "",
    "VERB_3": "",
    "FIELD OF STUDY": "",
    "ADJECTIVE_1": "",
    "ADVERB_1": "",
    }

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

story = """
    [NAME]'s "Three Laws of [FIELD OF STUDY]"

    1. A [NOUN_1] may not [VERB_1] a [NOUN_2] or, through inaction, allow a
       [NOUN_2] to [VERB_1].

    2. A [NOUN_1] must obey [PL_NOUN_1] given it by [NOUN_2] except where such
       [PL_NOUN_1] would conflict with the First Law.

    3. A [NOUN_1] must [VERB_2] its own [NOUN] as long as such [VERB_2] does
       not conflict with the First or Second Law.

    These laws ensure that a [NOUN_3] which relies [ADVERB_1] on [NOUN_1] does
    not [VERB_3] to [PL_NOUN_2] on a [ADJECTIVE_1] scale.
    """

# for key in word_dict:
#    word_dict[key] = input("Please input " + key + ": ")

# print(word_dict)

print(pluralize(input()))
