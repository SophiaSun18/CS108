from guizero import App, Drawing

class Room:
    '''This is the model of a room.'''
    
    def __init__(self):
        self.walls_info = []
        walls = open('wall.txt')
        lines = walls.readlines()
        for l in lines:
            info = l.split(',')
            info[-1] = info[-1][-(len(info[-1])):-1]
            info[1], info[2], info[3], info[4] = int(info[1]), int(info[2]), int(info[3]), int(info[4])
            self.walls_info.append(info)
    
        self.furs_info = []
        furnitures = open('furniture.txt')
        lines = furnitures.readlines()
        for l in lines:
            info = l.split(',')
            info[-1] = info[-1][-(len(info[-1])):-1]
            info[1], info[2], info[3], info[4] = int(info[1]), int(info[2]), int(info[3]), int(info[4])
            self.furs_info.append(info)