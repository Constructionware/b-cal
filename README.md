# b-cal: Easy Estimating
A Construction Estimator and Building Parts calculator

## Introduction

B-cal provides a suite of geometric and trigonomic functions essential to estimating construction and industry related jobs.

## Installation
    $ pip install b_cal

## Usage
    [1] from b_cal.calculator import Calculator
    [2] cal = Calculator()

Find the hypothenuse of A triangle given its 
rise and base length.
![alt triangle](hypothen.png) 

    [3] cal.hypothenuse(rise=8, run=14)

 
Calculate the length of a rafter given 
its rise and run <br>

![alt roof section](roofsect.png)


    [4] cal.rafter(rise=1460, run=2901)


Calculate the area and hip length of a Roof Hip Section

![alt roof plan](roofplan.jpg) ![alt roof](sect-a.jpg)


    [5] cal.hip(rise=1469, run=2922, span=5843)

b-cal returns a JSON object with key mapping to computed values.

Calculate Area of Roof segment given the length of ridge and fascia, run and rise 

![alt roof plan](roofplan-2.jpg)









       




    



