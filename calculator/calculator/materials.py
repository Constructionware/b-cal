
class Water:
    watername:str = 'H2O'   
    water_property:dict = {
         "form": 'fluid',
        "vol": 1,
        "unit": "gal",
        "ppg": 8.34,
        "kgpg": 3.785,
        "ltr": 3.785,
        "temp": {
            "unit": "deg",
             "boil": {
                 "F": 212,
                 "C": 100
                },
             "freeze": {
                 "F": 32,
                 "C": 0
                 }
            },
        "unit_convention": """
                ppg:pound per gallon, 
                kgpg: kilograms per gallon,
                ltr: liter,
                tmp: room temperature
                """  ,
         "generalnnote": """Cold water is more dense than ice 
        or than warm water or liquid just above freezing. 
        This is an unusual property of the substance, 
        resulting from hydrogen bonding.
         So, a gallon of warm water would weigh slightly less 
         than a gallon of cold water.
        """
    
     
    } 
    
    def water(self, name:str=None):
        ''' H2O  A Clear Fluid Substance  composting of Hydrogen and Oxygen.'''
        if name:
            self.watername = name
        return self.watername

    def waterppg( self , gals:float=None):
        """ Pound per gallon returns the weight in pounds of 1 usgallon of water"""
        if gals:
            return f"{gals * self.water_property['ppg']} lbs"
        return f"{self.water_property['ppg']} lb"

    def waterkpg( self , kilos:float=None):
        """ Kilograms  per gallon returns the weight in kilograms of 1 usgallon of water"""
        if kilos:
            return f"{kilos * self.water_property['kgpg']} Kg"
        return f"{self.water_property['kgpg']} Kg"

    def waterlpg( self , liters:float=None):
        """ Liters  per gallon returns the Metric Volume in liters of 1 usgallon of water"""
        if liters:
            return f"{liters * self.water_property['ltr']} liters"
        return f"{self.water_property['ltr']} liter"

    
    
