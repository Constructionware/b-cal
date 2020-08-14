# b-cal: Easy Estimating
A Construction Estimator and Building Parts calculator

## Introduction

The Building Calculator provides a suite of geometric and trigonomic functions essential to estimating construction and industry related jobs.

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
its rise and run 

    [4] cal.rafter(rise=2400, run=3600)

Calculate the area and hip length of a Roof Hip Section

    [4] cal.hip(rise=2400, run=3600, span=6000)
    





       




    



