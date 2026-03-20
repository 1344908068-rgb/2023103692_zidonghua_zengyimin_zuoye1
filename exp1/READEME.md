# 实验一：Python视觉开发环境搭建与图像基本读写

## 实验内容
1. 搭建 WSL + VS Code + Python 虚拟环境
2. 使用 OpenCV 读取、显示、保存图片
3. 实现图像灰度转换、区域裁剪等基本操作
4. 输出图像尺寸、通道数、像素类型等信息

## 运行环境
- Python 3.12
- OpenCV 4.10.0
- NumPy 2.0.0
- Matplotlib 3.9.0

## 文件说明
- `main.py`：核心代码
- `images/zy.jpg`：原始测试图片
- `original_zy.jpg`：保存的原图
- `gray_zy.jpg`：灰度转换结果
- `crop_zy.jpg`：裁剪结果图片

## 运行方式
```bash
cd ~/cv-course
source .venv/bin/activate
python exp1/main.py