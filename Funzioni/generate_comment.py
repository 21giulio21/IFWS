import itertools
import random

comment_list=[["Questa","La tua","La"],
                  ["foto", "fotografia"],
                  ["è veramente", "è proprio", "è davvero"],
                  ["pazzesca", "unica", "sensazionale", "bellissima", "magnifica", "indimenticabile",
                   "meravigliosa", "straordinaria", "eccezionale", "magica",
                   "emozionante"],
                  [" "," "," "," "," "," ","❤"," "],
                  [".", "..", "...", "!", "!!", "!!!"]]

def generate_comment(comment_list):
    #genera un commento a caso usando le parole di comment_list
        c_list = list(itertools.product(*comment_list))

        repl = [("  ", " "), (" .", "."), (" !", "!")]
        res = " ".join(random.choice(c_list))
        for s, r in repl:
            res = res.replace(s, r)
        return res.capitalize()

print(generate_comment(comment_list))