# Scrieti un program care sa organizeze o baza de date in 4 echipe.
#   Baza de date poate sa fie o lista, un dictionar sau mai multe elemente singular
#   Se va returna un dictionar de forma {nume_echipa:[]}
#   Fiecare membru de echipa, odata sortat in echipa, va avea numele si prenumele scris cu majuscule, restul literelor vor fi mici

# "nume prenume": "fav_hobby"
dictionary_of_ppl = {
    "Dan I.": "gaming",
    "Adi B.": "workout",
    "Ady": "gaming",
    "Aidan": "fotbal",

    "Alex T.": "gym",
    "Anamaria Sarbu": "workout",
    "Andreea Balan": "cooking",
    "Diana S.": "pictura",

    "Elena": "snowboarding",
    "George": "poker",
    "Marius": "gaming",
    "Iulian Iosif": "Diablo",

    "Iulian F.": "traveling",
    "Marina M.": "socializarea",
    "Vlad M.": "anime",
    "Cristi P.": "swimming"
}

alpha_team = []
beta_team = []
gama_team = []
delta_team = []

# 1. Inspect input - dictionary: decide how to parse the iterable
#       Identify keys
#       Create the teams: predefine 4 teams as empty lists
# 2. Get number of players
#       Define how many players will go in a team
# 3. Fill the roasters

def get_list_of_keys_from_dict(dictionary_of_players):
    """
    Return a list of all players from the dictionary
    :param dictionary_of_players: db used for our list
    :return: list with names of players
    """
    return list(dictionary_of_players.keys())

def get_number_of_players(list_of_names):
    return len(list_of_names)

def define_players_in_each_team(list_of_names):
    global alpha_team
    global beta_team
    global gama_team
    global delta_team

    len(list_of_names)/4
    if len(list_of_names)%4 == 0:
        # each team will have 4 players

        alpha_team  = list_of_names[0:4]
        beta_team   = list_of_names[4:8]
        gama_team   = list_of_names[8:12]
        delta_team  = list_of_names[12:16]
    else:
        # 3 teams will have 4 players and one will have less than 4
        pass


if __name__ == "__main__":
    list_of_names = get_list_of_keys_from_dict(dictionary_of_ppl)
    define_players_in_each_team(list_of_names)
    print(alpha_team)
    print(beta_team)
    print(gama_team)
    print(delta_team)
