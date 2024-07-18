import difflib
 
def calculate_spelling_score(string):
    score = difflib.SequenceMatcher(None, string.lower(), string).ratio()
    return score


string1 = """out.Dr P redacted receives 25 honor points,
and 50 experience.Climbing 5850 spots
 
in the rookie standings D, your knight Dr

P redacted currently occupies the 3805th
position.Game tip. Your knights current
position on the ranking list will be told to
you automatically after each battle. You can
also say (ranking) at any time.Do you want to
fight against another knigh

my gold

He has 14 gold coins, and 20 serfs, who earn
20 gold coins per hour. Your serfs quarters
has enough space for 125 tenants.Game tip.
Gold is the main currency at Knight Manager.
With gold you can improve his sword, armor
and quarters at the blacksmith. He can

also buy powerful potions in the tavern for
gold, and of course he can win or lose gold
while playing cards. Gold is mainly obtained
through his servants, but can also be found
in many other activities.Would you like to
send Dr P redacted into battle against an
enemy knight? Or should he head for the
Blacksmith?

stop

ok.| wish you safe travels."""
string2 = """DrPredacted receives 25 NHhomor poimts,
amd So expericomce Climmbinmg SSso spots

im the rookie stamdimgs DMD, your kKkKmight Dr

P redacted curremtly occupies the SsSosth
Positiom Gare tip. Your kKkmigMts curremt
Positiom om the ramkKkimag List wvitt be totd to
yvwou autormaticatly after each battle. You cam
atso say CramkKkimg) at amy tirme Do you wanmt to
Fight agaimst amothier Kknmniqh

rmy gold

He has Tt Ggotd coims, amd 2O serfs, who ecearm
ZO gotd coims per Pmour Your serfs quarters
ras omough space For 125 temanmts. Gare tip.
Gotta is the rmmaim curremcy at Kmight Mamager.
vVvVVIthh Gotd you cam irmprowve Ihihis swvord, armor
amd quarters at the blacksmith. He cam

atso buy powverful potioms im the taverm for
gotd, amd of course Re cam wim or tose gold
wyinite playinmg cards. Gotltad is rmmaimly obtained
through hihis servanmts, Dut cam atso be Foumd
immoamy other activities VVvould you like to
semad DrP redacted imtoo battle agaimst am
eamermy Kkmigqght? Or should re Read For the
Btacksrmithh?

stop

oki wish you safe travels.

Ss ( Ask Alexa -"""

score1 = calculate_spelling_score(string1)
score2 = calculate_spelling_score(string2)

print(f"The spelling score for '{string1}' is {score1:.2f}")
print(f"The spelling score for '{string2}' is {score2:.2f}")
