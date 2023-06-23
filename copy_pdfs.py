import os
import pandas as pd
import random
import shutil

def copy_random_pdfs(pkl_file, target_dir, n, stop_after_first_chunk=False):
    # 创建目标目录（如果它还不存在的话）
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # 用于存储选中的文件的列表
    selected_files = []

    # 分块读取pickle文件
    chunksize = 10 ** 6  # 可以根据你的内存大小调整这个值
    for chunk in pd.read_pickle(pkl_file, chunksize=chunksize):
        # 找出File字段值以.pdf结尾的行
        pdfs = chunk[chunk['File'].str.endswith('.pdf')]

        # 如果pdfs的行数少于n，那么所有的行都会被选中
        if len(pdfs) < n:
            selected_pdfs = pdfs
        else:
            # 随机抽取n行
            selected_pdfs = pdfs.sample(n)

        # 将选中的文件添加到列表中
        selected_files.extend(selected_pdfs['File'].tolist())

        # 如果选中的文件数量已经达到n，并且stop_after_first_chunk为True，那么停止处理后续的块
        if len(selected_files) >= n and stop_after_first_chunk:
            break

    # 如果selected_files的长度大于n，那么随机选择n个文件
    if len(selected_files) > n:
        selected_files = random.sample(selected_files, n)

    # 复制选中的文件
    for src_file in selected_files:
        dst_file = os.path.join(target_dir, os.path.basename(src_file))
        shutil.copy2(src_file, dst_file)

# 使用
pkl_file = '/path/to/your.pkl'  # pickle文件的路径
target_dir = '/path/to/target/dir'  # 目标文件夹路径
n = 100  # 需要复制的文件数量
# 是否在第一个块中抽取到n行后就停止处理后续的块，设置为False的话就是对整个pkl进行sampling
stop_after_first_chunk = False 

copy_random_pdfs(pkl_file, target_dir, n, stop_after_first_chunk)
