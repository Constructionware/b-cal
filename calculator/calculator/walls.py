from calculator.builderslib import library
from calculator.components import Door

class Wall(Door):    
    tag:str=None
    walltype:str = None
    form:str = 'solid'
    usage:str = None
    bearing:bool = False
    nonbearing:bool = True
    comments:str = None    
    _name:str = 'Building Wall'
    _length:float = None
    _height:float = None
    _thickness:float=None
    _unit:str = "m"
    _count:int = 1
    

    def __init__(self, walltype:str = None, height:float = None, length:float = None, thickness:float = None, usage:str = None, tag:str = None):
        self.walltype = walltype
        self.tag = tag
        self._height = height
        self._length = length
        self._thickness = thickness
        self.usage = usage
        self.update
        self.openings = []
        if tag:
            self.wall_tags.add(tag)
        

    @property
    def update(self):
        if self.usage and self.usage == 'structural':
            self.bearing = True
            self.nonbearing = False
        else:
            self.bearing = False
            self.nonbearing = True
            
    def wallname(self, name:str=None):
        ''' Get or set .'''
        if name:
            self._name = name
        else:
            pass
        return self._name

    def wallength( self , length:float=None, unit:str=None):
        """ Wall length  if you supply a unit Wall will asume that
                you want to explicitely reset the calculating unit on  the system
        """
        if length and unit:
            if unit == self._unit:
                self._length = length
                return f"{self._length} {self._unit}"
            self._unit = unit
            # Implement convert
            self._length = length
            return f"{self._length} {self._unit}"
        elif length and not unit:
            self._length = length
            return f"{self._length} {self._unit}"
        elif unit and not length:
            self._unit = unit
            # Implement convert 
            return f"{self._length} {self._unit}"           
        return f"{self._length} {self._unit}"

    def wallheight( self , height:float=None, unit:str=None):
        """ Wall height  if you supply a unit Wall will asume that
                you want to explicitely reset the calculating unit on  the system
        """
        if height and unit:
            if unit == self._unit:
                self._height = height
                return f"{self._height} {self._unit}"
            self._unit = unit
            # Implement convert
            self._height = height
            return f"{self._height} {self._unit}"
        elif height and not unit:
            self._height = height
            return f"{self._height} {self._unit}"
        elif unit and not height:
            self._unit = unit
            # Implement convert 
            return f"{self._height} {self._unit}"           
        return f"{self._height} {self._unit}"

    def wallthickness( self , thickness:float=None, unit:str=None):
        """ Wall Thickness  if you supply a unit Wall will asume that
                you want to explicitely reset the calculating unit on  the system
        """
        if thickness and unit:
            if unit == self._unit:
                self._thickness  = thickness
                return f"{self._thickness} {self._unit}"
            self._unit = unit
            # Implement convert
            self._thickness = thickness
            return f"{self._thickness} {self._unit}"
        elif thickness and not unit:
            self._thickness = thickness
            return f"{self._thickness} {self._unit}"
        elif unit and not thickness:
            self._unit = unit
            # Implement convert 
            return f"{self._thickness} {self._unit}"           
        return f"{self._thickness} {self._unit}"

    def process_wallopenings(self):
        #print(self.door_wall_log)
        #print(self.wall_tags)
        if self.tag and len(self.door_wall_log) > 1:
            
            for d in self.door_wall_log:
                if d['walltag'] == self.tag:
                    self.openings.append(d)
                    #print(d)        

    def setup(self, walltype:str=None, library:dict=None):
        if walltype and library:
            self.wallunit = library.get(walltype, 'Invalid walltype')
            self.walltype = self.wallunit['type']
            self.wallthickness(self.wallunit['thickness'] / 1000)
            
    def __repr__(self):        
        return f"{self._name} Type: {self.walltype} L:{self._length} H:{self._height}  T: {self._thickness} U:{self._unit}"

    @classmethod
    def cmu(cls, walltype:str=None, height:float = None, length:float = None, usage:str = None, tag:str = None):
        ''' Concrete Masonry Unit Wall '''
        wall = Wall()
        wall._name = "Concrete Masony Unit Wall"
        wall.tag = tag
        wall.usage = usage
        wall.wallheight(height)
        wall.wallength (length)
        wall.setup(walltype =walltype, library=library.cmulib)
        wall.update
        wall.openings = []
        if tag:
            wall.wall_tags.add(tag)        
        return wall

    @classmethod
    def drywall(cls, walltype:str='75', height:float = None, length:float = None, usage:str = 'Internal Partitioning', tag:str = None):
        ''' Dry Wall  Sheet Rock Wall '''        
        wall = Wall()
        wall._name = "Dry Wall"
        wall.tag = tag
        wall.usage = usage
        wall.wallheight(height)
        wall.wallength (length)
        wall.setup(walltype =walltype, library=library.sheetrocklib)
        wall.update
        wall.openings = []
        if tag:
            wall.wall_tags.add(tag)
        
        return wall
        
if __name__ == '__main__':
    wall = Wall.drywall('75', height=2.75, length=3.6, usage='Internal Partitioning',  tag='DW175')
    cm1 = Wall.cmu('150', height=2.75, length=3.6, usage='structural', tag='W10')
    cm2 = Wall.cmu('200',height=3.75, length=56, usage='structural', tag='W12')
    cm3 = Wall.cmu('250', height=2.75, length=3.6, usage='tructural', tag='W123')

    d2 = wall.externalDoor('Internal Hollow Core', width=800, tag='DI1', walltag='DW175')
    d1 = cm1.externalDoor(tag='DX12', walltag='W12')
    d3 = cm1.externalDoor('Hardwood V Jointed', tag='D2', walltag='W12')
    wall.process_wallopenings()
    cm1.process_wallopenings()
    cm2.process_wallopenings()
    cm3.process_wallopenings()
