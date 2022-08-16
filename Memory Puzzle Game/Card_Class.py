from graphics2 import *

class Card:
    
    ''' Card class creates the shape, color, and label of the card'''
    
    def __init__(self, center, shape, color, labelText):
        '''create the card using dictionary assigning each shape of string to actually creating the shape
            and has the label aligned in the center of the shapes and color'''
        self.center = center
        self.shape = shape
        self.color = color
        self.label = Text(center, labelText)
        self.label.setSize(20)
        
        triP1 = Point(self.center.getX(), self.center.getY()-50)
        triP2 = Point(self.center.getX()+50, self.center.getY()+50)
        triP3 = Point(self.center.getX()-50, self.center.getY()+50)
        shapesDict = {'Triangle': Polygon(triP1, triP2, triP3),
                      'Square':Rectangle(Point(self.center.getX()-50, self.center.getY()-50), Point(self.center.getX()+50, self.center.getY()+50)),
                      'Circle':Circle(self.center, 60)} 
        self.shapeObj = shapesDict[self.shape]
        self.shapeObj.setFill(self.color)
        
    # accessor methods (get)
    def getCenter(self):
        '''returns the center point of the card'''
        return self.getCenter
    
    def getShape(self):
        '''returns the shape string of this card'''
        return self.shape
        
    def getColor(self):
        '''returns the color string of this card'''
        return self.color
        
    def getLabel(self):
        '''returns label string of this card'''
        return self.label
    
    # mutator methods (set)    
    def draw(self, window):
        '''draws the shape containing color and the label on the window'''
        self.shapeObj.draw(window)
        self.label.draw(window)
        
    def undraw(self):
        '''undraws just the shape containing the color'''
        self.shapeObj.undraw()
     
    def __str__(self):
        '''converts the card to strings of text'''
        return f"<A Card for {self.getShape()} with {self.getColor()} color has label {self.getLabel()}>"