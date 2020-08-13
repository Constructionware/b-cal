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
