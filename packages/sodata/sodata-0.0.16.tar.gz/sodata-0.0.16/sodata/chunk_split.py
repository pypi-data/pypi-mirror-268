# -*- coding: utf-8 -*- 
# @File : chunk_split.py 
# @Author : zh 
# @Time : 2024/4/9 15:38 
# @Desc : 将小说文本切分成段落

import random
import re
from langchain.text_splitter import RecursiveCharacterTextSplitter
import jieba
from .clean_rule import *
from .chunk_clean import DataCleaner
from typing import (
    List,
    Dict,
    Optional,
    Any
)

def split_text_into_head_tail(text, tail_length=200):
    """
    将一个文本块按照tail_length分割成head和tail
    Args:
        text:单个文本片段
        tail_length:tail片段的最小长度
    Returns:
        head_text: 前一段文本
        tail_text: 后一段文本
    """
    # 使用正则表达式匹配中文句子结束符，以此来分割文本成句子
    sentences = re.split(split_pattern, text)
    # 保证句子后的标点符号不丢失
    sentences = [sentences[i] + (sentences[i + 1] if i + 1 < len(sentences) else '') for i in
                 range(0, len(sentences) - 1, 2)]

    tail_text = ""  # 初始化后面一段文本
    accumulated_length = 0  # 累计字数

    # 从后向前遍历句子，累计长度直到满足指定的后段字数
    while sentences and accumulated_length < tail_length:
        sentence = sentences.pop()  # 取出最后一个句子
        accumulated_length += len(sentence)
        tail_text = sentence + tail_text  # 将句子添加到后段文本的开头

    # 剩余的句子组成前一段文本
    head_text = ''.join(sentences)
    return head_text, tail_text


def split_text_into_segments(text, len_seg=512):
    """
    将文本切分成若干段,添加句号分隔每个sentence,每段长度不超过len_seg
    Args:
        text:
        len_seg:最大段落长度
    Returns:
        segments: 段落列表
    """
    segments = []
    current_segment = ''
    sentences = re.split(split_pattern, text)
    for sentence in sentences:
        if len(current_segment) + len(sentence) + 1 <= len_seg:  # 加上句号
            if current_segment:
                current_segment += '。'  # 添加句号分隔句子
            current_segment += sentence
        else:
            segments.append(current_segment)
            current_segment = sentence
    if current_segment:  # 处理最后一个 segment
        segments.append(current_segment + '。')
    return segments


def split_text_into_fixed_length_segments(text, segment_length=512):
    """
    将文本切分成固定长度(segment_length)的段
    Args:
        text:
        segment_length: 段落长度
    Returns:
        segments: 段落列表
    """
    # 检查输入是否为字符串
    if not isinstance(text, str):
        raise ValueError("输入必须是一个字符串。")
    # 检查段长度是否合理
    if segment_length <= 0:
        raise ValueError("段长度必须大于0。")
    # 使用列表推导式来生成段
    segments = [text[i:i + segment_length] for i in range(0, len(text), segment_length)]
    return segments


def custom_sampling(seg1, seg2, seg3, seg4, p1, p2, p3):
    """
       从三个区间中随机抽样
    Args:
        seg1: 1区间左端点
        seg2: 1间区右端点，2区间左端点
        seg3: 2区间右端点，3区间左端点
        seg4: 3区间右端点
        p1: 1区间的概率
        p2: 2区间的概率
        p3: 3区间的概率
    Returns:
        sample: 抽样结果
    """
    ranges = [(seg1, seg2, p1), (seg2, seg3, p2), (seg3, seg4, p3)]
    # 基于定义的概率随机选择ranges
    selected_range = random.choices(ranges, weights=[r[2] for r in ranges], k=1)[0]
    # 生成一个在选定范围内的随机样本, k:选取次数
    sample = random.randint(selected_range[0], selected_range[1])
    return sample


def _split_text_with_regex_from_end(
        text: str, separator: str, keep_separator: bool) -> List[str]:
    """
    一段文本text根据分隔符separator从文本的末尾分割文本。
    Args:
        text: 待分割的文本
        separator: 分割符列表
        keep_separator: 是否保留分割符
    Returns:
        返回分割后，除去所有空字符串的列表
    """
    if separator:
        if keep_separator:
            # 模式中的括号将分隔符保留在结果中。
            _splits = re.split(f"({separator})", text)
            splits = ["".join(i) for i in zip(_splits[0::2], _splits[1::2])]
            if len(_splits) % 2 == 1:
                splits += _splits[-1:]
            # splits = [_splits[0]] + splits
        else:
            splits = re.split(separator, text)
    else:
        splits = list(text)
    return [s for s in splits if s != ""]  # 重组非空白字符


class ChineseRecursiveTextSplitter(RecursiveCharacterTextSplitter):
    def __init__(
            self,
            separators: Optional[List[str]] = None,  # 用于分割文本的分隔符列表,默认为None。
            keep_separator: bool = True,  # 是否保留分割符在分割后的文本中,默认为True。
            is_separator_regex: bool = True,  # 分隔符是否为正则表达式。默认为True。
            chunk_size: int = 512,  # 每个文本块的最大长度。默认为512。
            chunk_overlap: int = 0,  # 相邻文本块的重叠长度。默认为0,表示没有重叠。
            **kwargs: Any,
    ) -> None:

        super().__init__(chunk_size=chunk_size, chunk_overlap=chunk_overlap, keep_separator=keep_separator, **kwargs)
        self._separators = separators or [
            "\n\n",
            "\n",
            "。|！|？",
            "\.\s|\!\s|\?\s",
            "；|;\s",
            "，|,\s"
        ]
        self._is_separator_regex = is_separator_regex

    def _split_text(self, text: str, separators: List[str]) -> List[str]:
        """
        分割文本并返回分割后的文本块。
        Args:
            text:整本书的文本
            separators: 用于分割文本的分隔符列表
        Returns:
            分割处理后，再删去多余的空白字符和换行符的文本块列表
        """
        final_chunks = []
        # 从最后一个分隔符开始遍历
        separator = separators[-1]
        new_separators = []
        for i, _s in enumerate(separators):
            # 如果分隔符是正则表达式则直接使用，否则进行转义，当成普通字符串使用
            _separator = _s if self._is_separator_regex else re.escape(_s)
            if _s == "":
                separator = _s  # \s表示空白字符
                break
            if re.search(_separator, text):
                separator = _s
                new_separators = separators[i + 1:]
                break

        _separator = separator if self._is_separator_regex else re.escape(separator)
        # 使用正则表达式按separator拆分文本
        splits = _split_text_with_regex_from_end(text, _separator, self._keep_separator)
        # 开始合并，递归拆分更长的文本。
        _good_splits = []
        # _separator = "" if self._keep_separator else separator
        _separator = separator if self._keep_separator else ""
        for s in splits:
            if self._length_function(s) < self._chunk_size:
                _good_splits.append(s)
            else:
                if _good_splits:
                    merged_text = self._merge_splits(_good_splits, _separator)
                    final_chunks.extend(merged_text)
                    _good_splits = []
                if not new_separators:
                    final_chunks.append(s)
                else:
                    # 新的分隔符存在，递归拆分
                    other_info = self._split_text(s, new_separators)
                    final_chunks.extend(other_info)
        if _good_splits:
            merged_text = self._merge_splits(_good_splits, _separator)
            final_chunks.extend(merged_text)
        # "\n{2,}"匹配两个或更多连续的换行符。
        return [re.sub(r"\n{2,}", "\n", chunk.strip()) for chunk in final_chunks if chunk.strip() != ""]


class BookSplit:
    """
    该类用于切分小说
    1. 将小说切成chunk
    2. 将chunk切成segment
    3. 将小说切成segment
    """

    def __init__(self) -> None:
        self.cleaner = DataCleaner()

    def convert_book_to_chunks(self, text_book, len_min=2048):
        """将小说切成随机长度的chunk
         args：
            text_book: 小说文本
            len_min: 小说最小长度，如果小于该值将被过滤
        return
            chunk_list: chunk列表
            chunk_size: chunk的最大长度
        """
        # 进行数据预处理
        if len(text_book) < len_min:
            print('filter the book and length is ', len(text_book))
            return []
        text = text_book
        # 将text文本切割为chunk_list
        chunk_size = custom_sampling(seg1=200, seg2=1000, seg3=2000, seg4=4000, p1=0.25, p2=0.25, p3=0.5)
        print('the max length of chunk is {}'.format(chunk_size))
        cs = ChineseRecursiveTextSplitter(chunk_size=chunk_size)
        chunk_list = cs.split_text(text)
        return chunk_list, chunk_size

    def convert_chunk_into_seg_head_tail(self, text, min_idx, max_idx, chunk_size):
        """将chunk切分成两段，切分的位置在min_idx与max_idx之间
         args：
            text: 小说文本
            min_idx: 最小切分位置
            max_idx: 最大切分位置
            chunk_size: chunk的长度
        return
            head_text: 前一段文本
            tail_text: 后一段文本
        """
        assert min_idx > 0 and max_idx > 0 and min_idx < max_idx
        assert abs(max_idx - min_idx) > 3
        # ---切片---
        idx_split_rand = random.randint(min_idx + 1, min(chunk_size, max_idx - 1))
        head_text, tail_text = split_text_into_head_tail(text, idx_split_rand)
        return head_text, tail_text

    def convert_chunk_into_segments(self, text, len_seg=512):
        """将chunk切分成若干段
            args：
                text: 小说文本
                len_seg: 段落最大长度，seg以分隔符结尾，不会突然结束
            return
                segments: 这个chunk的segment列表
        """
        return split_text_into_segments(text, len_seg)

    def convert_book_to_seg(self, text_book, book_len_min=2048, len_seg=512, chunk_sample=True):
        """将book切分成segment
            args：
                text_book: 小说文本
                blen_seg: 段落最大长度，seg以分隔符结尾，不会突然结束
                book_len_min: 小说最小长度，如果小于该值将被过滤
                chunk_sample: 只选择这本书的任意一个chunk，为了加快速度
            return
                segments_list: 这本书的segment列表
        """
        try:
            chunk_list = self.convert_book_to_chunks(text_book, book_len_min)
            if len(chunk_list) == 0:
                return [[]]
            segments_list = []
            for chunk in chunk_list:
                if chunk_sample:
                    chunk = random.choice(chunk_list)
                chunk = self.cleaner.clean_text(chunk)
                if len(chunk) == 0:
                    segments_list.append([])
                segments_per_chunk = self.convert_chunk_into_segments(chunk, len_seg)
                segments_list.append(segments_per_chunk)
                if chunk_sample:
                    break
        except Exception as e:
            print(f"Error processing {text_book}: {e}")
            return [[]]
        return segments_list
