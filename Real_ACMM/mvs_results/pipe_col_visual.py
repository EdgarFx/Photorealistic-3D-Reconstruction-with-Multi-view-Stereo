import numpy as np
import pylab as plt
import matplotlib.cm as cm

def read_array(path):
    with open(path, "rb") as fid:
        width, height, channels = np.genfromtxt(
            fid, delimiter="&", max_rows=1, usecols=(0, 1, 2), dtype=int
        )
        fid.seek(0)
        num_delimiter = 0
        byte = fid.read(1)
        while True:
            if byte == b"&":
                num_delimiter += 1
                if num_delimiter >= 3:
                    break
            byte = fid.read(1)
        array = np.fromfile(fid, np.float32)
    array = array.reshape((width, height, channels), order="F")
    return np.transpose(array, (1, 0, 2)).squeeze()

depth = read_array('DSC_0636.JPG.geometric.bin')

# depth_map[depth_map == 0] = np.nan

min_bound, max_bound = np.percentile(
    depth, [58.3, 99]
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