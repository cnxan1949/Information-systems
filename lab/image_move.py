import os
import shutil

# 源文件夹路径
source_dir = './face_images'
# 目标文件夹路径
a_dir = './face_images/train_set'
b_dir = './face_images/verify_set'

# 遍历源文件夹中的所有文件
for filename in os.listdir(source_dir):
    # 检查文件扩展名是否为.jpg
    if filename.endswith('.jpg'):
        # 尝试将文件名转换为整数
        try:
            file_number = int(os.path.splitext(filename)[0])
            # 根据文件名决定移动到a还是b文件夹
            if 0 <= file_number <= 23999:
                shutil.move(os.path.join(source_dir, filename), os.path.join(a_dir, filename))
            else:
                shutil.move(os.path.join(source_dir, filename), os.path.join(b_dir, filename))
        except ValueError:
            # 如果文件名不是数字，移动到b文件夹
            shutil.move(os.path.join(source_dir, filename), os.path.join(b_dir, filename))
