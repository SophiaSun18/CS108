from room_model import Room
from guizero import Drawing, App

class Game:
    '''This is the model of the room-escaping game.'''
    
    def __init__(self):
        '''Initiate the game.'''
        '''Create a list of the furnitures in the room.'''
        self.room = Room()
        self.count = {}
        for i in self.room.furs_info:
            self.count[i[0]] = 0
        
    def get_fur_name(self, x, y):
        '''Get a coordinate and return the name of the furniture on the position
        while also keeping track of how many times the furniture has been clicked.'''
        for i in self.room.furs_info:
            if i[0] != 'entrance' and i[1] < x < i[3] and i[2] < y < i[4]:
                self.count[i[0]] += 1
                return i[0]
    
    def get_info(self, fur_name):
        '''Get information based on the furniture name and how many times its clicked.'''
        info_list = []
        infos = open('info.txt')
        lines = infos.readlines()
        for l in lines:
            info = l.split('/')
            info[-1] = info[-1][-(len(info[-1])):-1]
            info_list.append(info)
        
        for i in info_list:
            if i[0] == fur_name:
                if self.count[fur_name] < len(i):
                    return i[self.count[fur_name]]
                else:
                    return random.choice(i[1:(len(i))])                    
    
    def get_item(self, fur_name):
        '''Get item based on the name of the clicked furniture.'''
        item_list = []
        items = open('item.txt')
        lines = items.readlines()
        for l in lines:
            item = l.split('/')
            item[-1] = item[-1][-(len(item[-1])):-1]
            item_list.append(item)
        
        for i in item_list:
            if i[0] == fur_name:
                return i[1]

    def get_interaction(self, ob_1, ob_2):
        '''Determine whether the chosen items can interact and return the result the user will get.'''
        message = 'You can not use this item here now.'
        lose = []
        get = []
        
        info = []
        f = open('interaction.txt')
        lines = f.readlines()
        for l in lines:
            list = l.split('/')
            list[-1] = list[-1][-(len(list[-1])):-1]
            info.append(list)
        
        for l in info:
            if [ob_1,ob_2] == l[0].split(','):
                message = l[1]
                lose = l[2].split(',')
                get = l[3].split(',')
        
        return message, lose, get
    
    def save_game(self, bag_list=[], item_list=[]):
        '''Save the bag and item information into a separate file.'''
        f = open('save.txt', 'w')
        for i in bag_list:
            f.write(i)
            f.write('/')
        f.write('\n')
        for i in item_list:
            f.write(i)
            f.write('/')
        f.close()
    
    def load_game(self):
        '''Load the bag and item information from a separate file.'''
        f = open('save.txt')
        line = f.readline()
        bag_list = line.split('/')
        bag_list.remove('\n')
        line = f.readline()
        item_list = line.split('/')
        item_list.remove('')
        
        return bag_list, item_list