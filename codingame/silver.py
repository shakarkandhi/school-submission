import sys
import math
from scipy import spatial

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# base_x: The corner of the map representing your base
base_x, base_y = [int(i) for i in input().split()]
if(base_x == 0):
    enemy_x,enemy_y=17630,9000
else:
    enemy_x,enemy_y=0,0
heroes_per_player = int(input())  # Always 3
# game loop
while True:
    mon=[]
    monvc=[]
    monid=[]
    mon_threat=[]
    hero=[]
    for i in range(2):
        # health: Each player's base health
        # mana: Ignore in the first league; Spend ten mana to cast a spell
        health, mana = [int(j) for j in input().split()]
    entity_count = int(input())  # Amount of heros and monsters you can see
    for i in range(entity_count):
        # _id: Unique identifier
        # _type: 0=monster, 1=your hero, 2=opponent hero
        # x: Position of this entity
        # shield_life: Ignore for this league; Count down until shield spell fades
        # is_controlled: Ignore for this league; Equals 1 when this entity is under a control spell
        # health: Remaining health of this monster
        # vx: Trajectory of this monster
        # near_base: 0=monster with no target yet, 1=monster targeting a base
        # threat_for: Given this monster's trajectory, is it a threat to 1=your base, 2=your opponent's base, 0=neither
        _id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for = [int(j) for j in input().split()]
        if(_type == 1):
            hero.append([x,y])
        if(_type == 0):
            mon.append([x,y])
            monvc.append([vx,vy])
            monid.append(_id)
            mon_threat.append(threat_for)
    if(len(mon) != 0):
        tree=spatial.KDTree(mon)
        for i in range(heroes_per_player):   
            idx=tree.query([base_x,base_y])[1]
            nearest=mon[idx]
            nearest_vc=monvc[idx]
            entity_id=monid[idx]
            threat_for=mon_threat[idx]
            if(threat_for != 0):          
                if(math.sqrt((nearest[0]-hero[i][0])**2 + (nearest[1]-hero[i][1])**2) < 10000):
                    if((math.sqrt((nearest[0]-hero[i][0])**2 + (nearest[1]-hero[i][1])**2) < 1280) and (math.sqrt((nearest[0]-base_x)**2 + (nearest[1]-base_y)**2) < 1000)):
                        print("SPELL WIND",nearest[0]-5*nearest_vc[0],nearest[1]-5*nearest_vc[1])
                    else:    
                        print("MOVE",nearest[0],nearest[1])
                else:
                    print("MOVE 5000 4000")
            else:
                print("SPELL CONTROL",entity_id,enemy_x,enemy_y)
                
            # Write an action using print
            # To debug: print("Debug messages...", file=sys.stderr, flush=True)


            # In the first league: MOVE <x> <y> | WAIT; In later leagues: | SPELL <spellParams>;
    else:
        if(base_x==0):
            print("MOVE 9000 4500")
            print("MOVE 4500 4000")
            print("MOVE 5500 600")
        else:
            print("MOVE 9000 4500")
            print("MOVE 13750 5500")
            print("MOVE 17500 3800")
