import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
# 设置后端为TkAgg（支持图形化显示）
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
# --------------------------
# 任务1: 使用OpenCV读取一张测试图片
# --------------------------
img = cv2.imread('exp1/images/origin.jpg')

if img is None:
    raise FileNotFoundError("无法读取图片，请检查文件路径是否正确！")

# --------------------------
# 任务2: 输出图像基本信息
# --------------------------
height, width, channels = img.shape
dtype = img.dtype

print("===== 图像基本信息 =====")
print(f"图像尺寸 (宽×高): {width} × {height}")
print(f"通道数: {channels}")
print(f"像素数据类型: {dtype}")

# --------------------------
# 任务3: 显示原图（Matplotlib方式）
# --------------------------
# OpenCV读取的图像是BGR格式，Matplotlib显示需要转为RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(12, 6))  # 加宽窗口，避免图片挤压
plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title('Original Image (RGB)')
plt.axis('off')
# --------------------------
# 任务4: 转换为灰度图，并显示
# --------------------------
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.subplot(1, 2, 2)
plt.imshow(gray_img, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

plt.tight_layout()
plt.show()

# --------------------------
# 任务5: 保存处理结果，把灰度图保存为新文件
# --------------------------
cv2.imwrite('exp1/images/gray_test.jpg', gray_img)
print("灰度图已保存为: gray_test.jpg")

# --------------------------
# 任务6: 用NumPy做简单操作
# --------------------------
#  输出某个像素值 
if len(gray_img.shape) == 2:
    pixel_val = gray_img[100, 100]
    print(f"灰度图在 (100,100) 处的像素值: {pixel_val}")
else:
    pixel_val = img[100, 100]
    print(f"彩色图在 (100,100) 处的BGR像素值: {pixel_val}")

#  裁剪区域并保存
crop_img = img[640:940, 550:850]
cv2.imwrite('exp1/images/crop_test.jpg', crop_img)
print("裁剪区域已保存为: crop_test.jpg")