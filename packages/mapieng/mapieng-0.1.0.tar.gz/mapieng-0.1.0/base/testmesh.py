import trimesh
import pyvista as pv
# 사각형의 네 개의 정점
vertices = [
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0]
]

# 한 개의 사각형을 만드는 인덱스
faces = [
    [0, 1, 2, 3]
]

# 메시 생성
mesh = trimesh.Trimesh(vertices=vertices, faces=faces, process=False)
pv_mesh = pv.wrap(mesh)

# 플롯터 생성
plotter = pv.Plotter()
plotter.add_mesh(pv_mesh, show_edges=True, line_width=1)  # 선의 두께를 10으로 설정
plotter.show()