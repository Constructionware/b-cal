# calculator.py
from pprint import pprint 
import math 
from calculator.walls import Wall
from calculator.water import Water    
    
class Calculator(
    # Plugins   
    Wall,
    Water,
    ):
    _name:str = 'CentryPlan Building Calculator'
   
    def __init__(self, name:str=None, *args, **kwargs):
        if name:
            self._name = name
            
    # Calculator Functions Here
    @property
    def pi(self):
        return math.pi
    
    def sqr(self, num:float=None):
        if num:
            return num * num
        return 

    def sqrt(self, num:float=None):
        """ Does not accept negative numbers"""
        if num and num > 0 :
            return math.sqrt(num)
        return 

    def area_r(self, num:float=None):
        '''
            Return the Area given a radius.            
            In geometry, the area enclosed by a circle of radius r is π r².
             Here the Greek letter π represents a constant, approximately equal to 3.14159, which is equal to 
             the ratio of the circumference of any circle to its diameter. Source: wikipedia.com.
             A = \pi r^2
                A	=	area
                r	=	radius
            Usage:
                In [3]: cal.area_r(2)                                                                                                              
                Out[3]: 12.566370614359172

        '''
        if num:
            return self.sqr(num) * self.pi
        pprint(self.area_r.__doc__, depth=1, width=60)
        return 

    def area_d(self, num:float=None):
        '''
            Return the Area given a diameter.  
        '''
        if num:
            return (self.area_r(num / 2))
        return 
    
    def angle_d(self, num:float=None):
        '''
            Return the Aangular radians given a degrees.  
        '''
        if num and num < 361:
            return math.radians(num)
        return 'You have exceded the maximimum circular degree of a true circle'
    

    def angle_r(self, num:float=None):
        '''
            Return the Aangular degrees radians given a radian.  
        '''
        if num and num < self.angle_d(360):
            return math.degrees(num)
        return 'You have exceded the maximimum radei of a true circle'

    def rectangle(self, length:float=None, width:float=None):
        '''
            Identifies and Return the Area and perimeter of a rectangle or square.  
        '''
        if length and width:
            objectr = {
                "area": length * width,
                "perimeter": (2 * length) + (2 * length)
            }
            if  length == width:
                objectr['figure'] = 'Square'
            else:
                objectr['figure'] = 'Rectangle'           
            return objectr
        return 

    def triangle(self, base:float=None, height:float=None):
        '''
            Identifies and Return the Area and perimeter of a rectangle or square.  
        '''
        if base and height:                      
            return (base / 2) * height
        return self.triangle.__dict__

    def trapezium(self, toplength:float=None, baselength:float=None, height:float=None):
        '''
            Return the area of a Trapezium or Quadrilateral given the length of
            its two paralell sides and the distance between them.  
        '''
        if toplength and baselength and height:                      
            return ((toplength +  baselength) / 2) * height
        return self.trapezium.__doc__

    def rafter_length(self, rise:float=None, run:float=None):
        '''
            Return the length of a rafter given its rise and run distance.  
        '''
        if rise and run:
            rafter = {'length': self.sqrt( self.sqr(rise) + self.sqr(run) )}
            rafter['cut_length'] = rafter['length'] * 1.05
            return rafter
        return self.rafter_length.__doc__

    
    
    def roof_hip(self, rise:float=None, run:float=None, span:float=None):
        '''
            .  
        '''
        if rise and span and run and rise < span:
            hypothenuse = self.rafter_length(rise=rise, run=run)
            rise_2 = hypothenuse['length']
            run_2 = span / 2
            hip = self.rafter_length(rise=rise_2, run=run_2)
            return {
                "area": hypothenuse['length'] * (span / 2), # formula for area of triangle
                "fascia_to_ridge": run,
                "hip": hip['length'],
                "fascia": span
            }           
        return self.rafter_length.__doc__
    
    
    
    def __repr__(self):
        return f" Calculator => {self._name}"
    
cal = Calculator()
if __name__ == '__main__': # Launch Calculator
    cal = Calculator()
