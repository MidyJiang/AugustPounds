import csv
import random

# 生成随机数
random_numbers = [random.randint(1, 100) for _ in range(10)]  # 生成10个范围在1到100之间的随机数

# 写入 CSV 文件
file_path = r'data_boc/send.csv'  # 定义要保存的文件路径和名称
with open(file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Random Number'])  # 写入表头
    writer.writerows([[num] for num in random_numbers])  # 逐行写入数据

print(f"随机数已写入 {file_path} 文件。")
