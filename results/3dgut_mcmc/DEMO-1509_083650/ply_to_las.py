import open3d as o3d
import numpy as np
import laspy

pcd = o3d.io.read_point_cloud("export_last.ply")

pts = np.asarray(pcd.points)

las = laspy.create()

las.x = pts[:,0]
las.y = pts[:,1]
las.z = pts[:,2]

las.write("converted_format/export_last.las")

print("Saved converted_format/export_last.las")
