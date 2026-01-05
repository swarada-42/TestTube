# import cv2
# import cv2.aruco as aruco

# # Select dictionary
# aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

# # Marker ID (0–49)
# marker_id = 5

# # Marker size (pixels)
# marker_size = 600

# # Generate marker
# marker_img = aruco.generateImageMarker(
#     aruco_dict,
#     marker_id,
#     marker_size
# )

# # Save marker
# cv2.imwrite("aruco_marker.png", marker_img)

# print("✅ ArUco marker saved as testtube.png")




import cv2
import cv2.aruco as aruco

# Select ArUco dictionary
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

# Marker size in pixels
marker_size = 600

# Marker IDs (must be different)
marker_ids = [5, 10]

for marker_id in marker_ids:
    # Generate marker image
    marker_img = aruco.generateImageMarker(
        aruco_dict,
        marker_id,
        marker_size
    )

    # Save marker
    filename = f"aruco_marker_{marker_id}.png"
    cv2.imwrite(filename, marker_img)

    print(f"✅ ArUco marker saved as {filename}")
