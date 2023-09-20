'''
The definintion for tutorial class
'''
#import statements
import random

class Tutorials():
    """
    Definition for the Tutorial class.
    attributes
    - tutorial_title 
    - tutorial_content
    """

    def __init__(self, 
                 tutorial_title, 
                 tutorial_content,
                 ):
        self.tutorial_title = tutorial_title
        self.tutorial_content = tutorial_content
        
    #accessor methods
    def get_tutorial_title(self):
        return self.tutorial_title

    def get_tutorial_content(self):
        return self.tutorial_content
    
    #setter methods
    def set_tutorial_title(self, new_tutorial_title):
        self.tutorial_title = new_tutorial_title

    def set_tutorial_content(self, new_tutorial_content):
        self.tutorial_content = new_tutorial_content
    
    #function for displaying motivational messages
    def disp_motivational_message(self):
        messages_list = ["Keep up the good work!", "You can do it!", "Keep going!"]
        message = random.choice(messages_list)
        print(message)



if __name__ == "__main__":
    tutorial1 = Tutorials("New Tutorial", "Random content")
    tutorial1.disp_motivational_message()