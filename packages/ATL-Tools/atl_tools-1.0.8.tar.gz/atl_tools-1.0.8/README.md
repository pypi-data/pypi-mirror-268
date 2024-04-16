# ATL_Tools 使用指南
## 1. 简介
ATL_Tools 是一个由[AI-Tianlong](https://github.com/AI-Tianlong)开发的工具集合，包含一些便利的小工具，发布的目的是为了方便自己使用。
## 2. 使用方法

### mkdir_or_exist(filename: str)
有以下两个主要的功能：
- 创建文件夹：
    ```python
    mkdir_or_exist(xxxx) # 创建文件夹, 存在则不创建
    ```
- 寻找所有符合后缀文件夹名称(绝对路径):
    ```python
    find_data_list(img_root_path: str, suffix: str ='.jpg') # 返回所有后缀为.jpg的文件绝对路径
    ```
- 使用方法：
    ```python
    from ATL_Tools import mkdir_or_exist, find_data_list
    #创建文件夹
    mkdir_or_exist('新文件夹名称')
    #获取文件夹内所有后缀为.jpg的文件绝对路径
    img_lists = find_data_list(img_root_path='数据集文件夹路径', suffix ='.jpg')
    ```
## 3. 版本更新日志
- 2023-12-06 v1.0.2 修复README中显示问题。
- 2023-12-06 v1.0.3 修改项目名称为ATL_Tools。
- 2024-04-03 v1.0.6 增加ATL_gdal模块，用于处理遥感影像。
- 2024-04-09 v1.0.7 修复ATL_gdal模块中对于ATL_path的引用，`__init__.py` 注释掉`from ATL_gdal import *`, 可不安装gdal使用ATL_Tools
- 2024-04-16 v1.0.8 修复 `ValueError: cannot convert float NaN to integer` in ATL_gdal Line 371