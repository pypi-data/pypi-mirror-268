import json
import baseplate_KDS41_30_2022_calc

import matplotlib.pyplot as plt
input = { 
         'B' : 240, 'H' : 240, 'Fc' :24 , 'Fy' : 400, 
         'Ec' :25811.006260943130 , 'Es' : 210000, 
         'bolt' : [ 
           { 'X' : 90, 'Y' : 0, 'Area' : 314.15926535897933 }, 
           { 'X' : -90, 'Y' : 0, 'Area' : 314.15926535897933 } ], 
         'P' : -3349.9999999999964, 'Mx' : 0, 'My' : 51009999.999999985 
         }

JsonData = json.dumps(input)
result = baseplate_KDS41_30_2022_calc.calc_ground_pressure(JsonData)

with open('result.json', 'w') as json_file:
    json.dump(result, json_file, indent=4)