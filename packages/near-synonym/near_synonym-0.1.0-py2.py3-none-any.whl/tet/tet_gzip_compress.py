# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2024/4/11 10:27
# @author  : Mo
# @function:


from io import BytesIO  # 从 io 模块导入 BytesIO 类
import base64  # 导入 base64 模块
import gzip  # 导入 gzip 模块
import json  # 导入 json 模块
import re
import os

from tqdm import tqdm

# 定义一个函数，将字符串压缩为 gzip 格式，并进行 base64 编码后返回结果
def gzip_str(to_gzip: str) -> str:
    out = BytesIO()  # 创建一个 BytesIO 对象
    with gzip.GzipFile(fileobj=out, mode='w') as f:  # 使用 gzip 对象进行数据压缩
        f.write(to_gzip.encode())  # 将待压缩的字符串写入 gzip 对象中
    return base64.b64encode(out.getvalue()).decode()  # 对压缩后的数据使用 base64 编码并返回结果


# 定义一个函数，输入参数为经过压缩和 base64 编码后的字符串，输出参数为解压缩并解码后的字符串
def ungzip_str(to_ungzip: str) -> str:
    compressed = base64.b64decode(to_ungzip)  # 先对输入字符串进行 base64 解码，再将已压缩的数据转换为 bytes 格式
    with gzip.GzipFile(fileobj=BytesIO(compressed)) as f:  # 使用 GzipFile 对象读取已编码的二进制对象，并解压缩该对象
        return f.read().decode()  # 返回解压缩后的数据，要注意先用 decode 将 bytes 对象转换为字符串格式


def load_json(path, parse_int=None):
    """
        加载json
    Args:
        path_file[String]:, path of file of save, eg. "corpus/xuexiqiangguo.lib"
        parse_int[Boolean]: equivalent to int(num_str), eg. True or False
    Returns:
        data[Any]
    """
    with open(path, mode="r", encoding="utf-8") as fj:
        model_json = json.load(fj, parse_int=parse_int)
    return model_json

def compress_json(json_data):
    # 使用re模块的sub函数移除JSON字符串中的空格和换行符
    return re.sub(r'\s+', '', json_data)

def tetFunc1():
    # 创建一个字典
    dataDict = load_json("ci_atmnonym_synonym.json")

    # 将字典转换为JSON字符串
    jsonStr = json.dumps(dataDict)
    # 打印JSON字符串
    print("原始json字符串：", jsonStr)
    print("原始json字符串长度：", len(jsonStr))
    jsonStr = compress_json(jsonStr)
    zipStr = gzip_str(jsonStr)
    print("压缩编码后的json字符串：", zipStr)
    print("压缩编码后的json字符串长度：", len(zipStr))
    unzipStr = ungzip_str(zipStr)
    print("解压缩后的json字符串：", unzipStr)
    print("解压缩后的json字符串长度：", len(unzipStr))
    if jsonStr == unzipStr:
        print("源字符串和解压后的字符串相同")
    else:
        print("源字符串和解压后的字符串不同")


# # 示例JSON数据
# json_data = '{\n    "name": "John",\n    "age": 30,\n    "city": "New York"\n}'
# # 压缩JSON数据
# compressed_json = compress_json(json_data)
# print(compressed_json)  # 输出压缩后的JSON数据


def gzip_compress_json(path_json="ci_atmnonym_synonym.json"):
    """   gzip压缩文件   """
    import json
    import gzip

    # 读取JSON文件
    with open(path_json, "r", encoding="utf-8") as file:
        data = json.load(file)
        file.close()
    # 将数据转换为JSON字符串
    json_str = json.dumps(data)
    # 将JSON字符串压缩并写入文件
    with gzip.open(path_json+".gz", "wt") as gz_file:
        gz_file.write(json_str)
        gz_file.close()
    print("gzip compress json file ok!")


def gzip_compress_file(path_in="word2vec.ann", path_out=None):
    """   gzip压缩文件   """
    import json
    import gzip

    with open(path_in, "rb") as file:
        file_string = file.read()
        file.close()
    if not path_out:
        path_out = path_in + ".gz"
    with gzip.open(path_out, "wb") as gz_file:
        gz_file.write(file_string)
        gz_file.close()
    print(f"gzip {path_in} to {path_out} ok!")


def gzip_load_file(path_in, path_out=None):
    """   gzip解压缩文件   """
    with gzip.open(path_in, "rt") as gz_file:
        file_string = gz_file.read()
        gz_file.close()

    if not path_out:
        path_out = path_in.strip(".gz")
    with open(path_out, "wt") as txt_file:
        txt_file.write(file_string)
        txt_file.close()
    print(f"gzip {path_in} to {path_out} ok!")
    print(path_in, path_out)


def dfs_file(path_dir):
    """
        递归获取某个目录下的所有文件(所有层, 包括子目录)
    Args:
        path_dir[String]:, path of dir, eg. "/home/data"
    Returns:
        data[List]: data of input, eg. ["2020_01_08.txt"]
    """
    path_files = []
    for root, dirs, files in os.walk(path_dir):  # 分别代表根目录、文件夹、文件
        for file in files:  # 遍历文件
            file_path = os.path.join(root, file)  # 获取文件绝对路径
            path_files.append(file_path)  # 将文件路径添加进列表
    files = list(set(path_files))
    files.sort()  # the same list
    return files



if __name__ == '__main__':
    myz = 0
    # tetFunc1()

    # gzip_compress_json()
    # gzip_compress_file()
    # gzip_load_file("word2vec.ann.gz")

    path_dir = "D:\\workspace\\pythonMyCode\\django_project\\near-synonym\\near_synonym\\data"
    files = dfs_file(path_dir)
    for file in tqdm(files, desc="gzip-file"):
        if ".gz" not in file:
            gzip_compress_file(path_in=file, path_out=file.replace("\\data", "\\data_gzip")+".gzip")

