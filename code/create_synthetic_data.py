import math, random
from pathlib import Path

random.seed(17)
centers = [
    (-8.0, -8.0, 0.0),
    ( 8.0, -8.0, 0.0),
    (-8.0,  8.0, 0.0),
    ( 8.0,  8.0, 0.0),
    ( 0.0,  0.0, 8.0),
]
points = []
num_points_per_object = 30
for cx, cy, cz in centers:
    for _ in range(num_points_per_object): 
        x = cx + random.uniform(-0.35, 0.35)
        y = cy + random.uniform(-0.35, 0.35)
        z = cz + random.uniform(-0.35, 0.35)
        intensity = random.randint(10, 100)
        points.append((x, y, z, intensity))

out = Path(r"C:\Users\danag\Documents\LIDAR\data\synthetic.pcd")

with out.open("w") as f:
    f.write("# .PCD v.7 - Point Cloud Data file format\n")
    f.write("VERSION .7\n")
    f.write("FIELDS x y z intensity\n")
    f.write("SIZE 4 4 4 4\n")
    f.write("TYPE F F F F\n")
    f.write("COUNT 1 1 1 1\n")
    f.write(f"WIDTH {len(points)}\n")
    f.write("HEIGHT 1\n")
    f.write("VIEWPOINT 0 0 0 1 0 0 0\n")
    f.write(f"POINTS {len(points)}\n")
    f.write("DATA ascii\n")
    for x, y, z, intensity in points:
        f.write(f"{x:.6f}, {y:.6f}, {z:.6f}, {intensity}\n")

print(f"Created {out} with {len(points)} points in 5 clearly separated clusters.")
