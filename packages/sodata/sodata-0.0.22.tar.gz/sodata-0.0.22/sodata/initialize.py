# -*- coding: utf-8 -*- 
# @File : initialize.py
# @Author : zh 
# @Time : 2024/4/17 上午10:18
# @Desc : 初始化配置文件
import yaml

config = None  # 声明config为全局变量

def init():
    # 读取系统配置
    global config  # 使用global关键字指明config是全局变量
    with open('conf/config.yaml', 'r', encoding='utf-8') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config
