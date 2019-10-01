#modele
from sys import exit
from random import randint
from textwrap import dedent
from Leaderboard import *

#------------------------------
#class

class Engine(object):    #(map_object_with_classroom, player_object)
    def __init__(self,map_object,player_object):
        self.map_object = map_object
        self.player_object = player_object

    def play(self):
        print('\n')
        print(dedent('''
                        As a transfer student you decide to take over
                        the "The Master High" and exert your domanance
                        and show the mules how to be a leader.

                        For that you have to win the Student presidential
                        election. You start your campaign at you class room.

                        Answer all queries and add your view to increase
                        influence points, they will derminer your progress
                        and result.

                        Warning: Commiting to too much student request will
                        anger the principal. he will detain you from campaign.\n
                        '''))

        current_scene = self.map_object.begin()
        end_scene = self.map_object.Senario['finished']
        
        while current_scene != end_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.map_object.next_scene(next_scene_name)
        result = end_scene.enter()
        if result == 'lost':
            x = lose()
            x.enter()
        input('press enter to continue...\n>> ')



class lose(object):
    que = ['\nFailed to take control!\n',
           '\nYou Loser!\n',
           '\nMission Failed!\n']
    def enter(self):
        print(self.que[randint(0,len(self.que)-1)])
        print('\nYou are ingored by everyone and bullied to death\n')
        return None


class Player(object):
    def __init__(self,name):
        self.name = name
        self.student_influence = 30
        self.staff_influence = 30
        self.principal_influence = 30

    def get_stu_influ(self):    #get student influence
        x = self.student_influence
        if 0 < x <= 100 :
            return self.student_influence
        elif x <= 0:
            return 0
        else:
            return 100

    def get_staff_influ(self):    #get student influence
        x = self.staff_influence
        if 0 < x <= 100 :
            return x
        elif x <= 0:
            return 0
        else:
            return 100
    def get_principal_influ(self):    #get student influence
        x = self.principal_influence
        if 0 < x <= 100 :
            return x
        elif x <= 0:
            return 0
        else:
            return 100
    def get_avg_influ(self):
        return (self.get_stu_influ() + self.get_staff_influ() + self.get_principal_influ())/3


class Scene(object):
    def enter(self):
        print("Influence students in the premise to win election")
        pass


class ClassRoom(Scene):
    def enter(self):
        print(dedent('''
                        You've enter your class room and started your campaign
                        you ask studens for what they need in order to vote
                        for you... and students request
                        '''))
        print(dedent('''
                        Student_1: We want no homework!
                        '''))
        response = input('>> ').lower()
        if 'yes' in response or 'ok' in response:
            new_player.student_influence += 10
            new_player.staff_influence -= 10
        else:
            new_player.student_influence -= 10
            new_player.staff_influence += 10
        print(dedent('''
                        Student_2: We want a big event day to let off some steam.
                        '''))
        response = input('>> ').lower()
        if 'yes' in response or 'ok' in response:
            new_player.student_influence += 10
            new_player.staff_influence += 10
            new_player.principal_influence -= 10
            print('\n(You have been noted by the principal)')
        else:
            new_player.student_influence -= 10
            new_player.principal_influence += 10
        print(dedent('''
                        student_3: I want more special classes.
                        '''))
        response = input('>> ').lower()
        if 'yes' in response or 'ok' in response:
            new_player.student_influence -= 10
            new_player.staff_influence += 10
            new_player.principal_influence += 10
            print('\n(hahaha.... did you really do that!)')
        else:
            new_player.student_influence += 10
            new_player.staff_influence += 0
            new_player.principal_influence += 0

        print('\nsome students swear to vote for you and you move to next areana to conquer')

        return 'sportsclub'

class SportsClub(Scene):
    def enter(self):
        print(dedent('''

                        Now you enter the sports club to gain more influence of the school's
                        best club. it has the most number of members in the school so make sure
                        to get their attention.
                        You approach them and they start tell you what they want.'''))
        print(dedent('''
                        Student_1: Host an interschool Cricket tournament.
                        '''))
        response = input('>> ').lower()
        if 'yes' in response or 'ok' in response:
            new_player.student_influence += 10
            new_player.staff_influence += 10
            new_player.principal_influence += 10
            print('\n(The principal is delighted)')
        else:
            new_player.student_influence -= 10
            new_player.staff_influence += 0
            new_player.principal_influence += 0

        print(dedent('''
                        
                        Student_2: We want extra grade points to compensate
                        for extra practice hours.
                        '''))
        response = input('>> ').lower()
        if 'yes' in response or 'ok' in response:
            new_player.student_influence += 10
            new_player.staff_influence -= 10
            new_player.principal_influence -= 10
        else:
            new_player.student_influence -= 10
            new_player.staff_influence += 10
            new_player.principal_influence += 0

        print('\nsome students swear to vote for you and you move to next areana to conquer')

        return 'scienceclub'

class ScienceClub(Scene):
    def enter(self):
        print(dedent('''

                        The science club is the worst club in your school.
                        whith only 3 members. but you decide every vote counts and
                        decide to step in.
                        You step in and ask for any requirements they need...
                        '''))
        print(dedent('''
                        Student_1: We want after school experiment hours.
                        '''))
        response = input('>> ').lower()
        if 'yes' in response or 'ok' in response:
            new_player.student_influence += 10
            new_player.staff_influence -= 10
            new_player.principal_influence += 10
            print('\n(The Staff are annoyed they have to stay after hours.)')
            print('\n(The principal is delighted to see the charisma of students)')
        else:
            new_player.student_influence -= 10
            new_player.staff_influence += 10
            new_player.principal_influence += 0

        print(dedent('''
                        Student_2: We'll vote if you join Science club.
                        '''))
        response = input('>> ').lower()
        if 'yes' in response or 'ok' in response:
            new_player.student_influence += 10
            new_player.staff_influence += 10
            new_player.principal_influence += 0
        else:
            new_player.student_influence -= 10
            new_player.staff_influence += 0
            new_player.principal_influence += 0
        print(dedent('''
                        student_3: We want an organised science exhibition.
                        '''))
        response = input('>> ').lower()
        if 'yes' in response or 'ok' in response:
            new_player.student_influence += 10
            new_player.staff_influence += 10
            new_player.principal_influence -= 10
        else:
            new_player.student_influence -= 10
            new_player.staff_influence -= 10
            new_player.principal_influence += 10

        print('\nsome students swear to vote for you and you move to next areana to conquer')
        return 'canteen'

class Canteen(Scene):
    def enter(self):
        print(dedent('''

                        At lunch hour you enter the canten and students what must he do
                        inorder to win some votes...
                        '''))
        print(dedent('''
                        Student_1: We want pizza for lunch.
                        '''))
        response = input('>> ').lower()
        if 'yes' in response or 'ok' in response:
            new_player.student_influence += 10
            new_player.staff_influence += 10
            new_player.principal_influence -= 10
        else:
            new_player.student_influence -= 10
            new_player.staff_influence -= 10
            new_player.principal_influence += 10

        print(dedent('''
                        Student_2: Free food!!!(its gonna fome from your wallet.)
                        '''))
        response = input('>> ').lower()
        if 'yes' in response or 'ok' in response:
            new_player.student_influence += 10
            new_player.staff_influence += 10
            new_player.principal_influence -= 10
        else:
            new_player.student_influence -= 10
            new_player.staff_influence += 0
            new_player.principal_influence += 10
            print('\n(The pricipal is delighted to see a straight forward person)')

        print('\nsome students swear to vote for you and you move to next areana to conquer')
        return 'auditorium'

class Auditorium(Scene):
    def enter(self):
        print(dedent('''
                        The final campaign ground is the auditorium where the candidates are allowed
                        to speak for 10 minuted before the voting and result announcement.
                        you are called at the stage to give your speech...
                        '''))
        print(dedent('''

                        Do you want to talk about your achivemente?
                        '''))
        response = input('>> ').lower()
        if 'yes' in response or 'ok' in response:
            new_player.student_influence += 10
            new_player.staff_influence += 10
            new_player.principal_influence += 10
            print('\nmore achivements?')
            response = input('>> ').lower()
            if 'yes' in response or 'ok' in response:
                new_player.student_influence -= 10
                new_player.staff_influence -= 10
                new_player.principal_influence -= 10

        print(dedent('''

                        Do you want to talk about the corruption the school?
                        '''))
        response = input('>> ').lower()
        if 'yes' in response or 'ok' in response:
            new_player.student_influence += 10
            new_player.staff_influence += 10
            new_player.principal_influence -= 10

        print(dedent('''

                        Do you want to trash talk the competition?
                        '''))
        response = input('>> ').lower()
        if 'yes' in response or 'ok' in response:
            new_player.student_influence += 10
            new_player.staff_influence += 0
            new_player.principal_influence += 10

        if new_player.get_principal_influ() < 30:
            print('\nThe principal is angered by your campaigning and decide to reject')
            print('\nyour nomination')
            return 'lost'

        print('\nYour speech is over and you await for the competition to speak.')
        input()
        return 'finished'

class Finished(Scene):
    def enter(self):
        print('------------------------------------------------------')
        if new_player.get_staff_influ() < 30:
            print('\nstaff influence very low')
            print('The staff arrange a cue and decide to rig the results')
            print('you lost the elections')
            return 'lost'
        print('Judgement day arrives and they announce the results')
        if new_player.get_stu_influ() > 80:
            print('\nCongradulations!!!You have Won the election and have been elected as the school president! ')
            print('\nYou rule this school now, no one can talk over you.')
            new = LeaderBoard()
            new.write_to_table(new_player.name)
            new.show_table()
        else:
            print('\nyou lost the election due to less student influence')
            return 'lost'
        

class Map(object):
    Senario = {'lost':lose(), 'finished':Finished(), 'classroom':ClassRoom(),'sportsclub':SportsClub(), 'scienceclub':ScienceClub(), 'canteen':Canteen(), 'auditorium':Auditorium()}

    def __init__(self,start_scene):
        self.start_scene = start_scene

    def begin(self):
        return self.next_scene(self.start_scene)

    def next_scene(self,scene_name):
        nxt = self.Senario.get(scene_name)
        return nxt


#--------------------------------
#function


#main
def main():
    pass

if __name__ == '__main__':
    running = True
    while running:
        print(dedent("""
                       --Menu--
                       1. Start
                       2. Leaderboard
                       3. Exit
                       """))
        action = input('>>  ')
        if action == '1':
            player_name = None
            while not player_name :
                player_name = input('\nEnter name:')
                if not player_name:
                    print('please enter valid name!')
            map_object = Map('classroom')
            new_player = Player(player_name)
            start = Engine(map_object,new_player)
            start.play()
        elif action == '2':
            lb = LeaderBoard()
            lb.show_table()
            input("press enter to continue...")
        elif action == '3':
            runnig = False
            exit(1)
        else:
            print('\nInvalid option!')
            


