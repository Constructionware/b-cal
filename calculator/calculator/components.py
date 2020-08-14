import uuid
from time import time, ctime


class Door:
    dlog:list = []
    door_areas :list = []
    door_wall_log:list = []
    wall_tags:set = set ()
    
    def __init__(self, doortype:str=None, width:float=None, height:float=None, thickness:float = None, tag:str=None, walltag:str=None):
        self._id = uuid.uuid4().hex
        self.dtag = tag
        self.dtype = doortype
        self.dwidth = width
        self.dheight = height
        self.dthickness = thickness
        self.dlog.append({"id": self._id, "tag": self.dtag, "logged": self.currentime()})
        self.door_areas.append(self.doorarea())
        if walltag:
            data = self.__dict__
            data['walltag'] = walltag
            self.door_wall_log.append(data)
            self.wall_tags.add(walltag)

    
    def doorarea(self):
        if self.dwidth and self.dheight and self.dwidth > 300:
            self.dunit = 'm2'
            self.drarea = round((self.dwidth / 1000) * (self.dheight / 1000),2)
            return round(self.drarea,2), self.dunit
        else:
            return None
        return 'You need to supply a width and a length in metric units'

    def __repr__(self):
        return f"{self.dtype} Door, {self.dtag} Width: {self.dwidth} Height: {self.dheight}"

    @property
    def total_door_areas(self):
        self.total_doorareas = sum([a[0] for a in self.door_areas])
        return  round(self.total_doorareas,2)

    @property
    def door_areas_list(self):
        self.door_areaslist = [a[0] for a in self.door_areas]
        return  self.door_areaslist 
        
    @staticmethod
    def timestamp():
        ''' Time Time Stamp '''
        return int(time() * 1000 )

    @staticmethod
    def currentime():
        ''' Now '''
        return ctime()

    @classmethod
    def externalDoor(cls, doortype:str="External HardWood Door", width:float=950, height:float=2100, thickness:float = 50, tag:str='Dh1', walltag:str=None):
        door = Door(doortype=doortype, width=width, height=height, thickness=thickness, tag=tag,  walltag=walltag)
        return door
        

class Roof(
    # Plugins
    Geometry
):
    def __init__(self, name:str=None, *args, **kwargs):
        if name:
            self.roofname = name
        self.roofname = "Building Roof"

    def rafter(self, rise:float=None, run:float=None):
        '''
            Return the length the rafter given its rise and run distance.  
        '''
        if rise and run:
            rafter = {'length': self.hypothenuse(rise, run)}
            rafter['cut_length'] = rafter['length'] * 1.05
            return rafter
        return self.rafter.__doc__
    
    
    def hip(self, rise:float=None, run:float=None, span:float=None):
        '''
           Roof: Returns the area and hip length of a hipped section of roof 
            given the rise run and width across its fascia or main span.  
        '''
        if rise and span and run and rise < span:
            hypothenuse = self.hypothenuse(rise=rise, run=run)
            rise_2 = hypothenuse
            run_2 = span / 2
            hip = self.hypothenuse(rise=rise_2, run=run_2)
            return {
                "area": hypothenuse * (span / 2), # formula for area of triangle
                "run": run,
                "hip": hip,
                "fascia": span
            }           
        return self.hip.__doc__
    
    def __repr__(self):
        return f" Roof: {self.roofname}"


class Wall(
    # Plugins 
    Geometry,
    Door
    ): 
    
    tag:str = None
    _unit:str = "m"
    _count:int = 1  
    _height:float = None
    _length:float = None
    _thickness:float = None       

    def __init__(
        self, 
        walltype:str = None,
        height:float = None, 
        length:float = None, 
        thickness:float = None, 
        usage:str = None, 
        tag:str = None
        ):
        self.bearing:bool = False
        self.comments:str = None
        self.form:str = 'hard-solid'
        self.nonbearing:bool = True
        self.openings = []
        self.tag = tag 
        self.usage = usage
        self.wall_name = 'Building Wall'
        self.walltype = walltype       
        self._height = height
        self._length = length
        self._thickness = thickness       
        self.update  
        if tag:            
            self.wall_tags.add(tag)        

    @property
    def update(self):
        self.process_wallopenings
        if self.usage and self.usage == 'structural':
            self.bearing = True
            self.nonbearing = False
        else:
            self.bearing = False
            self.nonbearing = True
            
    def wallname(self, name:str=None):
        ''' Get or set .'''
        if name:
            self.wall_name = name
        else:
            pass
        return self.wall_name

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
                return f"{self.__thickness} {self._unit}"
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
    
    @property
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
        return f"{self.wall_name} Type: {self.walltype} L:{self._length} H:{self._height}  T: {self._thickness} U:{self._unit}"

    @classmethod
    def cmu(cls, walltype:str=None, height:float = None, length:float = None, usage:str = None, tag:str = None):
        ''' Concrete Masonry Unit Wall '''
        wall = Wall()
        wall.wall_name = "Concrete Masony Unit Wall"
        wall.tag = tag
        wall.usage = usage
        wall.wallheight(height)
        wall.wallength (length)
        wall.openings = [] 
        wall.setup(walltype =walltype, library=library.cmulib)
        wall.update        
        if tag:
            wall.wall_tags.add(tag)        
        return wall

    @classmethod
    def drywall(cls, walltype:str='75', height:float = None, length:float = None, usage:str = 'Internal Partitioning', tag:str = None):
        ''' Dry Wall  Sheet Rock Wall '''        
        wall = Wall()
        wall.wall_name = "Dry Wall"
        wall.tag = tag
        wall.usage = usage
        wall.wallheight(height)
        wall.wallength (length)
        wall.openings = [] 
        wall.setup(walltype =walltype, library=library.sheetrocklib)
        wall.update
        if tag:
            wall.wall_tags.add(tag)
        
        return wall
        

#d = Door.externalDoor()
#d1=Door(doortype='Internal Hollow', width=900, height=2100, thickness = 42, tag='D2')
#d2=Door(doortype='External Solid', width=925, height=2100, thickness = 50, tag ='D1')
