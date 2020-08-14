class Library:
    cmulib:dict = {
            "150": {
                "type": "cmu-150",
                "thickness": 150,
                "cmu": {
                "vol": 1,
                "unit": "mm",
                "length": 400,
                "height": 200,
                "breadth": 150,
                "kg": 0,
                 "lb": 0,
                "cores": 2,
                "corevolume":0,
                "mortar": 0
                },
                "volume":0
                
            },
            "200": {
                "type": "cmu-200",
                "vol": 1,
                "unit": "mm",
                "length": 400,
                "height": 200,
                "thickness": 200,
                "kg": 0,
                 "lb": 0,
                "volume":0
                },
            "250": {
                "type": "cmu-250",
                "vol": 1,
                "unit": "mm",
                "length": 400,
                "height": 200,
                "thickness": 250,
                "kg": 0,
                 "lb": 0,
                "volume":0
                },     
                "note": """General Cmu Notes"""         
        }
    sheetrocklib:dict = {
            "75": {
                "type": "drywall-75",
                "thickness": 75,
                "sheetrock": {
                "vol": 1,
                "unit": "mm",
                "length": 2400,
                "bredth": 1200,
                "thickness": 15,
                "kg": 0,
                 "lb": 0,
                "layers": 1,
                "compound": 1.2,
                "screws": 36,
                "tape": 7200                
                },
                "estimate":{}
                
            },
            "100": {
                "type": "drywall-100",
                "thickness": 100,
                "sheetrock": {
                "vol": 1,
                "unit": "mm",
                "length": 2400,
                "bredth": 1200,
                "thickness": 15,
                "kg": 0,
                 "lb": 0,
                "layers": 1,
                "compound": 1.2,
                "screws": 36,
                "tape": 7200                
                },
                "estimate":{}
                
            },
            "150": {
                "type": "drywall-150",
                "thickness": 150,
                "sheetrock": {
                "vol": 1,
                "unit": "mm",
                "length": 2400,
                "bredth": 1200,
                "thickness": 15,
                "kg": 0,
                 "lb": 0,
                "layers": 1,
                "compound": 1.2,
                "screws": 36,
                "tape": 7200                
                },
                "estimate":{}
                
            },
                "note": """General Sheet Rock  Notes"""         
        }

library = Library()


# Construction notes
class Notes:
    ''' A library of construction notations where keys are mapped to a
        costruction statement.
        Use: to word construction documents.
        '''
    def __init__(self):
        self.notes='Use: to word construction documents.'

    def connote(self):
        ''' returns a dictionary mapping abreviated keywords to a string
            representing a costruction statement.
        '''
        cnote={'excavation':{'exc':'to excavate for foundation','topsoil':'topsoil',
                             'soil':'solid earth','marl':'solid marl',
                             'stone':'solid stone','loosestone':'loose stone',
                             'softclay':'soft clay','sand':'loose sand',
                             'dispose':'cart away and dispose of excavated material',
                             'backfill':'To backfill with suitable fill and compact'
                             },
               
                             
        	'concrete':{'mix':'mix place and vibrate', 'conc':'concrete to',
                            'r121':'1:2:1', 'r122':'1:2:2', 'r123':'1:2:3',
                            'r124':'1:2:4','r131':'1:3:1', 'r132':'1:3:2',
                            'r133':'1:3:3','r134':'1:3:4','r135':'1:3:5','r136':'1:3:6'                            
                            },
               
               'rebar':{'cut':'cut bend and install','fab':'cut and fabticate',
                        'lnk':'links to', 'str':'stirrups', 'brs':'bars to','rbr':'re-bar',
                        'm5':'6mm', 'm10':'10mm', 'm12':'12mm','m16':'16mm', 'm20':'20mm',
                        'm25':'25mm',
                        '1/4':'1/4 inch','3/8':'1/2 inch','5/8':'5/8 inch',
                        '3/4':'3/4 inch','1':'1 inch'
                        },

               'structural':{'fdn':'foundation','stf':'stiffeners', 'clm':'columns',
                             'lnt':'lintels','bms':'beams','blt':'beltcourse',
                            'slb':'slab', 'wll':'block walls','blk':'block cores'},
               
               'Wall':{'erect':'to erect ', 'wll':'block wall ', 
                       'acore':'fill alternate cores ', 'core':'fill all cores',
                       'drw':'dry wall','cstone':'cut stone wall',
                       'dstone':'dressed stone wall','rstone':'rubble stone wall',
                       'ply':'plyboard wall','brd':'boarded wall'
                       
                       },

               'form':{'make':'make formwork','erect':'erect and remove formwork to',
                       'mprop':'install and remove metal shores to',
                       'wprop':'install and remove wooden shores to'
                       },

               'roof':{'install':'install roofing','erect':'erect roof',
                       'decra':'decra metal','metro':'metro romano',
                       'fiber':'fiber glass shingle','zinc':'zinc sheet',
                       'alsheet':'aluminum sheeting','stseam':'standing seam'
                       },

               'floor':{'install':'install flooring','lay':'level and lay',
                        'cer':'ceramic tiles','porc':'porcelain tiles',
                        'prk':'pakae tile','wood':'wooden flooring',
                        'thset':'thinset mortar',
                        'grt':'grouted in matching grout',
                        'plsh':'polish'
                        }
                 }
        return cnote