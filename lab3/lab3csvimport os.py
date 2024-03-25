import os
import csv
from PIL import Image

# 定义函数来获取图像文件的信息
def get_image_info(image_path):
    try:
        with Image.open(image_path) as img:
            # 获取图像大小
            width, height = img.size
            # 获取图像模式
            mode = img.mode
            # 返回图像信息
            return os.path.basename(image_path), os.path.dirname(image_path), width, height, mode
    except Exception as e:
        # 如果出现任何错误，打印错误信息并返回 None
        print(f"Error processing {image_path}: {e}")
        return None

# 定义函数来将图像信息写入CSV文件
def write_image_info_to_csv(image_folder, output_csv):
    # 创建CSV文件并写入列标题
    with open(output_csv, mode='w', newline='', encoding='gbk') as file:
        writer = csv.writer(file)
        writer.writerow(['FileName', 'FolderPath', 'Width', 'Height', 'Mode'])

        # 遍历图像文件夹中的每个图像文件，并将其信息写入CSV文件
        for root, dirs, files in os.walk(image_folder):
            for file in files:
                if file.endswith('bmp'):
                    image_path = os.path.join(root, file)
                    image_info = get_image_info(image_path)
                    if image_info:
                        writer.writerow(image_info)

# 指定图像文件夹路径（注意：此处需要用原始字符串前缀 r 来表示路径，避免转义）
image_folder = r'C:\Users\韩韩\Desktop\毕业设计\数据\casia-facev5\CASIA-FaceV5'
# 指定输出CSV文件路径（同样需要使用原始字符串前缀 r）
output_csv = r'C:\Users\韩韩\Desktop\毕业设计\代码\image_info.csv'

# 调用函数来写入图像信息到CSV文件
write_image_info_to_csv(image_folder, output_csv)
