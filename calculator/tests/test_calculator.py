from calculator import __version__
from calculator.calculator import Calculator


def test_version():
    assert __version__ == '0.1.2'

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

#d = Door.externalDoor()
#d1=Door(doortype='Internal Hollow', width=900, height=2100, thickness = 42, tag='D2')
#d2=Door(doortype='External Solid', width=925, height=2100, thickness = 50, tag ='D1')
