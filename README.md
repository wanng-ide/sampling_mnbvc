# sampling_mnbvc

！！已弃用！！

因为pkl文件管理办法已经被废弃。

## 简介

`copy_pdfs.py`是一个Python脚本，用于从大型pickle文件中抽取特定的PDF文件，并将这些文件复制到一个新的目录中。

## 功能

- 从pickle文件中读取数据
- 找出File字段值以.pdf结尾的行
- 随机抽取指定数量的行
- 将对应的PDF文件复制到指定的目录中
- 可选择在第一个块中抽取到指定数量的行后就停止处理后续的块

## 使用方法

1. 确保你的Python环境中已经安装了`pandas`、`random`和`shutil`库。

```bash
pip install pandas
```

2. 针对pkl文件的格式为：

```txt
{'File': [], 'Size': [], 'SHA256': []}
```

3. 可以直接运行`copy_pdfs.py`脚本。

```bash
python copy_pdfs.py
```

!!! 参考下面进行修改copy_pdfs.py里面的内容。

4. (optional) 也可以在你的Python环境中运行以下命令：

```python
from copy_pdfs import copy_random_pdfs

pkl_file = '/path/to/your.pkl'  # pickle文件的路径
target_dir = '/path/to/target/dir'  # 目标文件夹路径
n = 100  # 需要复制的文件数量
# 是否在第一个块中抽取到n行后就停止处理后续的块，设置为False的话就是对整个pkl进行sampling
stop_after_first_chunk = False 

copy_random_pdfs(pkl_file, target_dir, n, stop_after_first_chunk)
```

请将上述代码中的`/path/to/your.pkl`和`/path/to/target/dir`替换为你的实际pickle文件路径和目标文件夹路径，将`n`替换为你想要复制的文件数量，将`stop_after_first_chunk`设置为你的实际需求。

## 注意事项

在运行这个脚本之前，请确保你有足够的磁盘空间来存储复制的文件。
