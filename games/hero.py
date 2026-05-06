# Rpg game 
# one hero , one villan , random(10,20), attacking, HP,
import random as r

def hero_attack(villan_hp, hero_punch):

    villan_hp = villan_hp - hero_punch
    if villan_hp < 0:
        return 0
    else:
        return villan_hp

def villan_attack(hero_hp, villan_punch):
    hero_hp = hero_hp - villan_punch
    if hero_hp < 0:
        return 0
    else:
        return hero_hp

hero_hp = 100
villan_hp = 100

while True:
    n = r.randint(1, 2)

    if n == 1:
        hero_punch = r.randint(10, 20)
        villan_hp = hero_attack(villan_hp, hero_punch)
        print(f"Hero attacks! Damage: {hero_punch}, Villan HP: {villan_hp}")
    else:
        villan_punch = r.randint(10, 20)
        hero_hp = villan_attack(hero_hp, villan_punch)
        print(f"Villan attacks! Damage: {villan_punch}, Hero HP: {hero_hp}")

    if hero_hp <= 0:
        print("Villan Win")
        break
    elif villan_hp <= 0:
        print("Hero Win")
        break