# functions.py
from pprint import pprint 
import math 

    
class Trigonometry: 

    def __init__(self, name:str=None, *args, **kwargs):

        ''' 
        Trigonometry is a branch of mathematics that studies relationships 
        between the sides and angles of triangles.
        '''
        if name:
            self.trig_name = name

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

    def radian(self, degree:float=None):
        '''
            Return the Aangular radians given a degrees.  
        '''
        if degree and degree < 361:
            return math.radians(degree)
        return 'You have exceded the maximimum circular degree of a true circle' 

        
    def degree(self, radian:float=None):
        '''
            Return the Aangular degrees radians given a radian.  
        '''
        if radian and radian < self.radian(360):
            return math.degrees(radian)
        return 'You have exceded the maximimum radei of a true circle'

    
    def hypothenuse(self, rise:float=None, run:float=None):
        '''
            Return the length the hypothenuse of a triangle given its rise and run distance.  
        '''
        if rise and run:           
            return self.sqrt( self.sqr(rise) + self.sqr(run) )
        return 

    
class Geometry(
     # Plugins 
     Trigonometry
     ):       
    def __init__(self, name:str=None, *args, **kwargs):
        ''' 
        Geometry is a branch of mathematics that studies the size, 
        shapes, angles, positions  and dimensions of things.
        '''
        if name:
            self.geo_name = name
    # Calculator Functions Here   

    def rcircle(self, radius:float=None):
        '''
            Return the Area of a circle given its radius.            
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
        if radius:
            return self.sqr(radius) * self.pi
        pprint(self.rcircle.__doc__, depth=1, width=60)
        return 

    def dcircle(self, diameter:float=None):
        '''
            Return the Area of a circle given its diameter.  
        '''
        if diameter:
            return (self.rcircle(diameter / 2))
        return   

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
        return 

    def trapezoid(self, toplength:float=None, baselength:float=None, height:float=None):
        '''
            Return the area of a Trapezium or Quadrilateral given the length of
            its two paralell sides and the distance between them.  
        '''
        if toplength and baselength and height:                      
            return ((toplength +  baselength) / 2) * height
        return 

    def quadrilateral(self, toplength:float=None, baselength:float=None, height:float=None):
        return self.trapezoid(toplength, baselength, height)


    
       