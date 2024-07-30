import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def read_depth_dmb(file_path):
    try:
        with open(file_path, 'rb') as inimage:
            # 读取数据
            type_info = np.fromfile(inimage, dtype=np.int32, count=1)[0]
            h = np.fromfile(inimage, dtype=np.int32, count=1)[0]
            w = np.fromfile(inimage, dtype=np.int32, count=1)[0]
            nb = np.fromfile(inimage, dtype=np.int32, count=1)[0]

            # 检查数据类型
            if type_info != 1:
                return None

            # 读取深度图数据
            data_size = h * w * nb
            depth_data = np.fromfile(inimage, dtype=np.float32, count=data_size)
            
            # 将深度图数据转换为矩阵
            depth = np.reshape(depth_data, (h, w))
            
            return depth
    except IOError:
        print("Error opening file", file_path)
        return None


# def visualize_depth_map(depth_map):
#     plt.imshow(depth_map)
#     # plt.colorbar()  # 添加颜色条
#     plt.title('Depth Map')
#     plt.xlabel('Width')
#     plt.ylabel('Height')
#     plt.show()



# depth = read_depth_dmb("ACMM_pipe/2333_00000002/depths.dmb")
# min_bound, max_bound = np.percentile(
#     depth, [0.55, 98]
# )

# depth = read_depth_dmb("ACMH_pipe/2333_00000002/depths.dmb")
# min_bound, max_bound = np.percentile(
#     depth, [1.7, 93]
# )

# depth = read_depth_dmb("ACMH_s3/2333_00000002/depths.dmb")
# min_bound, max_bound = np.percentile(
#     depth, [0.6, 98]
# )

depth = read_depth_dmb("ACMM_s3/2333_00000002/depths.dmb")
min_bound, max_bound = np.percentile(
    depth, [0.1, 99]
)

depth[depth < min_bound] = min_bound
depth[depth > max_bound] = max_bound


# max_bound = np.max(depth)
# min_bound = np.min(depth)

normalized_depth = (depth - min_bound) / (max_bound - min_bound)
colors = cm.jet(normalized_depth)
height, width = depth.shape
depth_rgb = np.zeros((height, width, 3), dtype=np.uint8)

for y in range(height):
    for x in range(width):
        if normalized_depth[y,x] != 0:
            depth_rgb[y, x] = (int(colors[y, x, 0] * 255), int(colors[y, x, 1] * 255), int(colors[y, x, 2] * 255))


print(depth)
print(max_bound)
print(min_bound)
plt.imshow(depth_rgb)
plt.xticks([])
plt.yticks([])
plt.axis('off')
plt.show()