import pickle
import datetime

now = datetime.datetime.now()

#Leader_board
class LeaderBoard(object):
    def __init__(self):
        pass

    def show_table(self):

        # load the previous score if it exists
        try:
            with open('score.dat', 'rb') as file:
                score_chart_list = pickle.load(file)
            #print(score_chart_list)
            
            if score_chart_list:
                print('\n___________Hall of Fame___________\n')
                countN = 1
                for player in score_chart_list:
                    print('{}th President: {:10} year: {}'.format(countN,player[0],player[1]))
                    countN += 1
                    
        except:
            print('LeaderBoard Empty')
        print('\n')
        
        

    def write_to_table(self,name):
        try:
            with open('score.dat', 'rb') as file:
                score_chart_list = pickle.load(file)
            #pickle.dump(score, file)
        except:
            score_chart_list = []
        with open('score.dat','wb') as file:
            score_chart_list.append([name,now.year])
            pickle.dump(score_chart_list,file)
        

