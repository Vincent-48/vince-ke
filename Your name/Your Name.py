# Type your name

import random

def border(name, e, emo, emoji):
    name=input("-Your name with design- \nRun it several times for random design."
               "\n\n").upper()
    if name=="":
        return "Hmmm...Forgot to type your name!😋"
    e=["*","~","#","="]
    emo=["😉","😆","😍","😘,","😎"]
    emoji=["💥","👄","🌹","🍎","🍇"]
    first= random.choice(e) * (len(name)+6)
    second= random.choice(emo) + " " + name + ""
    + random.choice(emoji)
    return first + "\n" + second + "\n" + first
print(border(input, "","",""))