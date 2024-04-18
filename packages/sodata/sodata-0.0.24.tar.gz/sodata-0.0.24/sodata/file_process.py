# -*- coding: utf-8 -*-
# @File : file_process.py
# @Author : zh
# @Time : 2024/4/9 15:38
# @Desc : 数据处理过程中涉及到的文件操作
import json
import os


class FileProcessTool:

    # isFileProcessTool = "This is a tool for file process."
    def __init__(self) -> None:
        pass

    @staticmethod
    def count_lines(file_path: str) -> int:
        """
        计算文件行数
        Args:
            file_path: 文件路径
        Returns:
            lines_num: 行数
        """
        lines_num = 0
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(2 ** 20)
                if not data:
                    break
                lines_num += data.count(b'\n')
        return lines_num

    @staticmethod
    def process_txt_file(filepath: str,
                         encodings: list[str] = ['utf-8', 'gb18030', 'gbk', 'gb2312', 'latin-1', 'ascii']) -> str:
        """
        尝试使用不同的编码读取和转换文本文件。
        Args:
            filepath: 待处理的txt文件路径
            encodings: 尝试的编码列表
        Returns:
            content:返回处理后的文本数据
        """
        content = None
        for encoding in encodings:
            try:
                with open(filepath, 'r', encoding=encoding) as file:
                    content = file.read()
                # 成功读取后转换编码到utf-8（如果已经是utf-8则不需要转换）
                return content.encode('utf-8').decode('utf-8')
            except UnicodeDecodeError:
                continue
        raise UnicodeDecodeError(f"Failed to decode {filepath} with given encodings.")

    @staticmethod
    def save_to_jsonl(text_data: str, output_file: str) -> None:
        """
        将文本数据保存为JSON Lines格式。
        Args:
            text_data: 待保存的整本小说文本数据
            output_file: 输出文件路径
        Returns:
        """
        with open(output_file, 'a', encoding='utf-8') as file:
            file.write(json.dumps({"text": text_data}, ensure_ascii=False) + '\n')
        print(f"save to {output_file}!!!")

    @staticmethod
    def process_folder_and_save_to_jsonl(txt_folder_path: str, output_file: str) -> None:
        """
        递归遍历文件夹，处理每个txt文件，然后将数据保存为一整个JSONL格式。
        Args:
            txt_folder_path:  待转换的txt文本路径
            output_file:  输出文件路径
        Returns:
        """
        for root, dirs, files in os.walk(txt_folder_path):
            for file in files:
                if file.endswith('.txt'):
                    filepath = os.path.join(root, file)
                    try:
                        text_data = FileProcessTool.process_txt_file(filepath)
                        FileProcessTool.save_to_jsonl(text_data, output_file)
                        print(f"Processed and saved {file} successfully.")
                    except UnicodeDecodeError as e:
                        print(e)
        print("finished!!")
