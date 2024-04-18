# -*- coding: utf-8 -*- 
# @File : chunk_clean.py.py
# @Author : zh 
# @Time : 2024/4/15 上午11:38
# @Desc : 清除单个文本片段的无效数据
import regex 
import jionlp
from datasketch import MinHash, MinHashLSH
from sodata.clean_rule import rules


class ChunkCleanTool:
    """
    该类用于小说片段（chunk）的数据清洗
    注意是不能清洗整本小说，否则会有过度清洗的问题
    """
    rules = rules

    def __init__(self) -> None:
        pass

    @staticmethod
    def remove_duplicates_exact(paragraphs: list[str]):
        """
        精确匹配去重：对于段落列表中一模一样的段落进行去重
        args:
            paragraphs: 段落列表
        return:
            unique_paragraphs: 不含重复段落的段落列表
            repeated_text: 重复文本列表
        """
        unique_set = set()
        unique_paragraphs = []
        repeated_text = []
        for p in paragraphs:
            if p in unique_set:
                repeated_text.append(p)
                continue
            unique_set.add(p)
            unique_paragraphs.append(p)
        return unique_paragraphs, repeated_text

    @staticmethod
    def remove_duplicates_minhash(paragraphs: list[str], num_perm: int = 128):
        """
        MinHash去重：对于段落列表中相似性较大的段落进行去重
        args:
            paragraphs: 段落列表
            num_perm: 相似度参数，用于生成MinHash的排列数，较大的 num_perm 值会提高准确性，但也会增加计算成本
        return:
            unique_paragraphs: 不含重复段落的段落列表
            ordered_repeated:重复文本列表
        """
        lsh = MinHashLSH(threshold=0.5, num_perm=num_perm)
        minhashes = {}

        for i, p in enumerate(paragraphs):
            m = MinHash(num_perm=num_perm)
            for d in p:
                m.update(d.encode('utf8'))
            lsh.insert(f"p{i}", m)
            minhashes[f"p{i}"] = m

        unique_keys = set()
        ordered_unique_keys = []  # 用于保持原始顺序的唯一键列表
        ordered_repeated = []
        for i, p in enumerate(paragraphs):
            key = f"p{i}"
            if key in unique_keys:
                # x = []
                # x.append(paragraphs[key], paragraphs[i])
                ordered_repeated.append(paragraphs[i])
                continue
            duplicates = lsh.query(minhashes[key])
            unique_keys.update(duplicates)
            ordered_unique_keys.append(key)  # 仅当键是唯一的时候才添加

        # 使用有序的唯一键列表来生成最终的唯一段落列表
        unique_indices = [int(k[1:]) for k in ordered_unique_keys]
        unique_paragraphs = [paragraphs[i] for i in sorted(unique_indices)]  # 根据索引排序以保持原始顺序
        return unique_paragraphs, ordered_repeated
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
    
    @staticmethod
    def clean_text(chunk: str):
        """
        对于小说文本片段进行数据清洗
        args:
            chunk: 小说文本片段
        return:
            chunk: 清洗后的小说文本
            ordered_repeated:重复文本列表
        """
        raw_text = chunk
        # 应用替换规则
        for pattern, replacement in rules:
            # dirty_text_list.extend(re.findall(pattern, text))
            chunk = regex.sub(pattern, replacement, chunk)

            # 通用清洗
        chunk = jionlp.clean_text(chunk, remove_parentheses=False, delete_prefix=True)
        chunk, ordered_repeated = ChunkCleanTool.cascade_deduplication(chunk)
        # dirty_text_list.append(ordered_repeated)
        if "@" in chunk or "^" in chunk or "PS：" in chunk or "更新时间" in chunk or "回复时间" in chunk or "回复日期" in chunk or (
                "《" in chunk and "》" in chunk):
            return ''
        return chunk,ordered_repeated