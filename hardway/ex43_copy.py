from sys import exit
from random import randint
from textwrap import dedent # 把字符串开头的空白去掉

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")   # >>>>  ??????
        print("Subclass it and implement enter().")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map   # 声明一个变量 self.scene_map
        
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()


class Death(Scene):

    quips = ["You died. You kinda suck at this.",]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""The Gothons of Planet Percal #25 have invaded your ship and"""))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""Quick on the  draw you yank out your blaster and fire"""))
            return 'death'

        elif action == "dodge!":
            print(dedent("""Like a world class boxer you dodge, weave, ship and"""))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""Luckly for you they made you learn Gothon insults in"""))
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""You do a dive roll into the Weapon Armory, crouch and scan"""))

        # code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        code = f"10"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZEDDDD")
            guesses += 1
            guess = input("[keypad]> ")
            if guesses == 9:
                break    # 10 times break out while ,not 11 times in books bug 
        if guess == code:
            print(dedent("""The container clicks open and the seal breaks, letting""")) 
            return 'the_bridge'
        else:
            print(dedent("""The lock buzzes one last time and then you hear a"""))
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print(dedent("""You burst onto the Bridge with netron destruct bomb"""))
        
        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""In a panic you throw the bomb at the group of Gothons"""))
            return 'death'
        elif action == "slowly place the bomb":
            print(dedent("""You point your blaster at the bomb under your arm and"""))
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"


class EscapePod(Scene):

    def enter(self):
        print(dedent("""You rush through the ship desperately trying to make it to"""))

        good_pod = randint(1,5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent(f"""You jump into pod {guess} and hit the eject button."""))
            return 'death'
        else:
            print(dedent(f"""You jump into pod {guess} and hit the eject button."""))
            return 'finished'


class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name) #from Map() get the scene
        return val  # 返回房间函数变量

    def opening_scene(self):
        return self.next_scene(self.start_scene) # 返回


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
 
 # set a_game to an instance of Engine(a_map) 
 # make a class named Engine that is a_map
 # set a_map to an instance of Map()