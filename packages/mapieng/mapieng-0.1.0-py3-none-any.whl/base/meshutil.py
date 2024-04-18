import matplotlib.pyplot as plt
from calculator_asd import *

util = CDgnASDEngine()
util.create_section(240, 240)
util.initialize(24, 400, 25811.006260943130, 210000.00000000000)
util.add_rebar(90, 0, 314.15926535897933)
util.add_rebar(-90, 0, 314.15926535897933)
util.set_comp_bar_mode(False)

# 결과 출력
util.calc_centroid()
util.calc_rotation_angle(-3349.9999999999964, 0, 51009999.999999985)

data = util.m_arCon
x_coords = [arc['dX'] for arc in data]
y_coords = [arc['dY'] for arc in data]
pn_values = [arc['dPn'] for arc in data]
# 그래프를 생성합니다.
plt.figure(figsize=(8, 6))
scatter = plt.scatter(x_coords, y_coords, c=pn_values, cmap='viridis', s=100)  # 색상을 Pn 값에 따라 지정

# 컬러바를 추가합니다.
plt.colorbar(scatter, label='Pn value')

plt.xlabel('X coordinate')
plt.ylabel('Y coordinate')
plt.title('Plot of Pn values at X, Y coordinates using color')
plt.grid(True)
plt.show()