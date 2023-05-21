def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

import math 

A,B = MI()

def calculate_minimum_attacks(enemy_hp, attack_power):
    if enemy_hp <= 0:
        return 0
    else:
        return (enemy_hp + attack_power - 1) // attack_power

minimum_attacks = calculate_minimum_attacks(A, B)

print(minimum_attacks)
