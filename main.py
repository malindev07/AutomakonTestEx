import math
from math import sqrt

import yaml

radius_wheel  = 0.125 # В метрах
wheel_base = 1.29 # В метрах

output_data = []

with open('input_lite.yaml') as file:
    data = yaml.load_all(file, Loader = yaml.FullLoader)
    
    i = 0
    for item in data :
        current_output_data = {'linear':{'x':0.0, 'y':0.0, 'z':0.0}, 'angular':{'x':0.0, 'y':0.0, 'z':0.0}}
        
        radius = 0
        if item['twist']['angular']['z']:
            radius = abs(item['twist']['linear']['x'] /  item['twist']['angular']['z'])
        
        omega_machine = item['twist']['angular']['z']
        # Расчет скорости вращения колеса
        omega_wheel = omega_machine * radius/ radius_wheel
        
        ugol_wheel = 0
        # Расчет угла поворота
        if radius:
            r2 = sqrt((radius**2 - wheel_base**2))

            ugol_A = math.degrees(math.atan(r2 / wheel_base))
            ugol_wheel = 180 - 90 - ugol_A
            
        else:
            ugol_wheel = float(ugol_wheel)
            # print(ugol_wheel)
        
        current_output_data['linear']['x'] = omega_wheel
        current_output_data['angular']['z'] = ugol_wheel
        
        output_data.append(current_output_data)
        

print(output_data)
with open('output_lite.yaml', 'w') as output_file:
    yaml.dump_all(output_data, output_file,default_flow_style=False,sort_keys=False)