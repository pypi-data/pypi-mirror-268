# -*- coding: utf-8 -*-
# @File :text_clean.py
# @Author : zh
# @Time : 2024/4/9 15:38
# @Desc : 清除整个小说文本中的无效数据


from sodata.chunk_clean import ChunkCleanTool


class TextCleanTool:


    def __init__(self) -> None:
        pass

    # 级联去重过程：输入为原始小说文本text
    @staticmethod
    def cascade_deduplication(text_dirty: str):
        """
        对于任意一段小说进行精确匹配去重和MinHash模糊去重
        args:
            text_dirty: 小说段落
        return:
            text_clean: 去重后的小说段落
           repeated_text: 重复文本列表
        """
        # 以一行为单位处理
        paragraphs = text_dirty.split('\n')
        # Step 1: 精确匹配去重
        unique_paragraphs, repeated_text = ChunkCleanTool.remove_duplicates_exact(paragraphs)
        # Step 2: MinHash去重
        unique_paragraphs, repeated_text = ChunkCleanTool.remove_duplicates_minhash(unique_paragraphs)

        text_clean = '\n'.join(unique_paragraphs)
        return text_clean, repeated_text