import tkinter as tk
from tkinter import messagebox
import random




class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


    def attack(self):
        return self.damage




class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword", damage=10)


class Axe(Weapon):
    def __init__(self):
        super().__init__(name="Axe", damage=15)


class Bow(Weapon):
    def __init__(self):
        super().__init__(name="Bow", damage=8)


class Character:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.weapon = None


    def choose_weapon(self, weapon):
        self.weapon = weapon


    def attack(self, opponent):
        if self.weapon:
            damage = self.weapon.attack()
            opponent.health -= damage
            return damage
        else:
            return 0




def attack_opponent():
    if not player.weapon:
        messagebox.showwarning("No Weapon", "Please choose a weapon first!")
        return


    damage = player.attack(opponent)
    attack_info.set(f"Player attacked with {player.weapon.name} dealing {damage} damage!")
    opponent_health.set(f"Opponent Health: {opponent.health}")


   
    if opponent.health > 0:
        opp_damage = random.choice(weapons).attack()
        player.health -= opp_damage
        attack_info.set(f"Opponent attacked back dealing {opp_damage} damage!")
        player_health.set(f"Player Health: {player.health}")
   
   
    check_game_over()




def choose_weapon(weapon_name):
    weapon_dict = {"Sword": Sword, "Axe": Axe, "Bow": Bow}
    player.choose_weapon(weapon_dict[weapon_name]())
    current_weapon.set(f"Current Weapon: {weapon_name}")




def check_game_over():
    if player.health <= 0:
        messagebox.showinfo("Game Over", "You have been defeated!")
        root.quit()
    elif opponent.health <= 0:
        messagebox.showinfo("Victory!", "You have defeated the opponent!")
        root.quit()




player = Character(name="Player")
opponent = Character(name="Opponent")
weapons = [Sword(), Axe(), Bow()]




root = tk.Tk()
root.title("Text-Based Fighting Game")


current_weapon = tk.StringVar(value="Current Weapon: None")
player_health = tk.StringVar(value=f"Player Health: {player.health}")
opponent_health = tk.StringVar(value=f"Opponent Health: {opponent.health}")
attack_info = tk.StringVar(value="Choose a weapon and attack!")


tk.Label(root, textvariable=current_weapon).pack()
tk.Label(root, textvariable=player_health).pack()
tk.Label(root, textvariable=opponent_health).pack()
tk.Label(root, textvariable=attack_info).pack()


tk.Button(root, text="Choose Sword", command=lambda: choose_weapon("Sword")).pack()
tk.Button(root, text="Choose Axe", command=lambda: choose_weapon("Axe")).pack()
tk.Button(root, text="Choose Bow", command=lambda: choose_weapon("Bow")).pack()
tk.Button(root, text="Attack!", command=attack_opponent).pack()


root.mainloop()


