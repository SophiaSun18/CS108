from guizero import App, Drawing, PushButton, Box, Text, TextBox, Window, ButtonGroup
from room_model import Room
from game_model import Game

class Room_Escape:
    
    def __init__(self, app):
        '''Initiate the game.'''
        
        self.game = Game()
        
        self.bag_list = []
        self.item_list = []
        
        self.fur_list = []
        for i in self.game.room.furs_info:
            if i[0] != 'entrance':
                self.fur_list.append(i[0])

        app.title = 'A Room'
        app.width = 600
        app.height = app.width + 100

        box_1 = Box(app, width=app.width, height=app.width, layout='grid', align='top')

        self.drawing = Drawing(box_1, width=app.width, height=app.width, grid=[0, 0])
        self.drawing.bg = 'black'

        self.text = Text(box_1, text="Welcome to the room!\n\nYou're trapped.\n\nFind out how to escape!",
                         grid=[0, 0], color='white', bg='black', size=35)
        
        box_2 = Box(app, width=app.width, height=50, layout='grid')

        self.start = PushButton(box_2, command=self.start_game, text='Start the game', grid=[0,0])
        self.load = PushButton(box_2, command=self.load, text='Load', grid=[1,0], enabled=False)
        self.yes = PushButton(box_2, command=self.get_information, text='Yes', grid=[2,0], enabled=False)
        self.no = PushButton(box_2, command=self.next_step, text='No', grid=[3,0], enabled=False)
        self.open_bag = PushButton(box_2, command=self.bag_open, text='Check my bag', grid=[4,0], enabled=False)
        self.use_item = PushButton(box_2, command=self.item_use_1, text='Use my item', grid=[5,0], enabled=False)
        self.save = PushButton(box_2, command=self.save, text='Save', grid=[6,0], enabled=False)
        PushButton(box_2, app.destroy, text='Quit', grid=[7,0])

        box_3 = Box(app, width=app.width, height=50, layout='grid')

        self.tips = TextBox(box_3, text='Your Goal: Escape from this room. Click on furnitures to get information.',
                            grid=[0,0], width=app.width)

    def start_game(self):
        '''Start the game after the start button is clicked and create a new room.'''

        self.text.visible = False
        self.start.enabled = False
        self.open_bag.enabled = True
        self.use_item.enabled = True
        self.load.enabled = True
        self.save.enabled = True
        
        for i in self.game.room.walls_info:
            self.drawing.line(i[1], i[2], i[3], i[4], color='white', width=4)
        for i in self.game.room.furs_info:
            self.drawing.rectangle(i[1], i[2], i[3], i[4], color=i[5])
        
        self.drawing.when_clicked = self.clicked_frame
        
    def clicked_frame(self, event):
        '''Give out the decision brunch when the user clicks on the furniture.'''

        if self.yes.enabled is False:
            self.fur_name = Game.get_fur_name(self.game, event.x, event.y)
            if self.fur_name != None:
                self.tips.value = 'This is a ' + self.fur_name + '. Do you want to search it?'
                self.yes.enabled = True
                self.no.enabled = True
                
    def get_information(self):
        '''If the user decides to search the furniture, then return the information and item.'''
        '''After adding new information and item into the bag, proceed into the next_step function.'''
        
        self.no.enabled = False
        
        inf = Game.get_info(self.game, self.fur_name)
        if inf not in self.bag_list:
            if 'You find a' not in inf:
                self.bag_list.append(inf)
            else:
                item = Game.get_item(self.game, self.fur_name)
                if item not in self.item_list and item != None:
                    self.item_list.append(item)
            
        self.tips.value = inf
        self.yes.when_clicked = self.next_step
    
    def next_step(self):
        '''If the user decides not to search the furniture, then end the decision brunch.'''
        
        self.tips.value = 'Click on other places to get more information.'
        self.yes.enabled = False
        self.no.enabled = False
        
        self.yes.when_clicked = self.get_information
    
    def save(self):
        '''Save the game progress into a separate file.'''
        
        self.game.save_game(self.bag_list, self.item_list)
        self.tips.value = 'Your game progress has been saved!'
    
    def load(self):
        '''Load the game progress into a separate file.'''
        
        self.bag_list, self.item_list = self.game.load_game()
        self.tips.value = 'Your game progress has been loaded!'

    def bag_open(self):
        '''Open the bag which inclued all information and items the user has collected.'''
            
        self.bag = Window(app, title='My bag', width=700, height=900)
        
        Text(self.bag, text='Your information.', size=20)
        if len(self.bag_list) == 0:
            TextBox(self.bag, text='No information yet.', width='fill')
        else:
            for i in self.bag_list:
                TextBox(self.bag, text=i, width='fill')
                
        Text(self.bag, text='Your items.', size=20)
        if len(self.item_list) == 0:
            TextBox(self.bag, text='No item yet.', width='fill')
        else:
            for i in self.item_list:
                TextBox(self.bag, text=i, width='fill')
                
    def item_use_1(self):
        '''Choose the item that the user wants to use.'''
        '''If the user hasn't got any item, then display the no-item message.'''
        '''If the user hasn't got any item, the item_use_2 fucntion can't be called.'''
            
        self.items_1 = Window(app, title='Choose item', width=400, height=400)
        self.use_1 = ButtonGroup(self.items_1, options=self.item_list)
        use = PushButton(self.items_1, text='Yes', command=self.item_use_2, enabled=False, align='bottom')
        if len(self.item_list) != 0:
            use.enabled = True
        else:
            Text(self.items_1, text='No item to use yet.', size=20)
        app.display()

    def item_use_2(self):
        '''Choose the object that the user wants to use the item on.'''
        
        self.items_1.destroy()
        self.items_2 = Window(app, title='Choose place', width=400, height=400)
        self.use_2 = ButtonGroup(self.items_2, options=self.fur_list + self.item_list)
        PushButton(self.items_2, text='Yes', command=self.item_interact, align='bottom')
        app.display()
    
    def item_interact(self):
        '''Decide if the chosen item and object can effectively interact.'''
        '''If can, return the new clue, remove the used item, add in the new item. '''
        '''If not, return the can't-use-it-here message.'''
        
        interact = Game.get_interaction(self.game, self.use_1.value, self.use_2.value)
        
        self.tips.value = interact[0]
        if interact[1] != ['']:
            for i in interact[1]:
                self.item_list.remove(i)
        if interact[2] != ['']:
            for i in interact[2]:
                self.item_list.append(i)
        self.items_2.destroy()
        
        if self.tips.value == 'You use the glass as the magnifying lens and you can read the paper now.':
            self.paper_read()
    
    def paper_read(self):
        '''Read the secret paper.'''
        
        paper_display = Window(app, title='The paper', width=900, height=400)
                
        paper = open('paper.txt')
        lines = paper.readlines()
        for i in lines:
            i = i[-(len(i)):-1]
            Text(paper_display, text=i, size=20)
        
        self.drawing.when_clicked = self.escape_begin

    def escape_begin(self, event):
        '''The interaction towards other furnitures is stopped.'''
        '''The only action is for the user to find the entrance based on the information on the paper.'''
        
        self.tips.value = 'You start to look for the entrance.'

        for i in self.game.room.furs_info:
            if i[0] == 'entrance':
                if int(i[1]) < event.x < int(i[3]) and int(i[2]) < event.y < int(i[4]):
                    self.game.count['entrance'] += 1
                    self.tips.value = Game.get_info(self.game, 'entrance')
                    
                    if self.tips.value == 'Just do it harder!':
                        self.game.count['entrance'] -= 1
                        self.drawing.when_double_clicked = self.escape
            else:
                self.tips.value = 'Keep looking for the entrance!'
    
    def escape(self):
        '''Successfully escape. Return to the original setting.'''
        
        entrance = Window(app, title='Escape Successful!',width=500,height=600)
        Text(entrance, text='A black hole appears\n\non the floor\n\nwith a ladder inside.\n\n\n\nCongratulations!\n\nYou successfully escape\n\nfrom the room!\n',
             width='fill', height='fill', color='yellow', bg='green', size=30)
        PushButton(entrance, text='close', command=entrance.destroy)
        
        self.drawing.clear()
        self.bag_list.clear()
        self.item_list.clear()
        
        self.text.visible = True
        self.start.enabled = True
        self.open_bag.enabled = False
        self.use_item.enabled = False
        self.load.enabled = False
        self.save.enabled = False
        
        self.tips.value = 'Your Goal: Escape from this room. Click on furnitures to get information.'
        self.drawing.when_clicked = None

app=App()
my_game=Room_Escape(app)
app.display()