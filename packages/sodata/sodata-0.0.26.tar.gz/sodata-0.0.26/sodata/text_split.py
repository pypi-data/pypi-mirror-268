# -*- coding: utf-8 -*- 
# @File : text_split.py
# @Author : zh 
# @Time : 2024/4/9 15:38 
# @Desc : 将小说文本切分成段落

import random
import re
import copy

from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain_core.documents import BaseDocumentTransformer, Document
from abc import ABC, abstractmethod

from sodata.clean_rule import split_pattern
from sodata.chunk_clean import ChunkCleanTool
from typing import (
    Callable,
    Iterable,
    List,
    Dict,
    Optional,
    Any
)


class TextSplitter(BaseDocumentTransformer, ABC):
    """文本切分接口，用于将文本切分成块。"""
    def __init__(
            self,
            chunk_size: int = 4000, #返回块的最大大小
            chunk_overlap: int = 200, #块之间的字符重叠
            length_function: Callable[[str], int] = len, #用于测量给定块长度的函数
            keep_separator: bool = False, #是否在块中保留分隔符
            add_start_index: bool = False, #如果为`True`，则在元数据中包含块的开始索引
            strip_whitespace: bool = True, #如果为`True`，则从每个文档的开始和结束去除空白字符
    ) -> None:
        if chunk_overlap > chunk_size:
            raise ValueError(
                f"chunk_overlap ({chunk_overlap}) 不应大于 chunk_size ({chunk_size})。"
            )
        self._chunk_size = chunk_size
        self._chunk_overlap = chunk_overlap
        self._length_function = length_function
        self._keep_separator = keep_separator
        self._add_start_index = add_start_index
        self._strip_whitespace = strip_whitespace

    @abstractmethod
    def split_text(self, text: str) -> List[str]:
        """将文本切分成多个部分。"""
        pass

    def create_documents(
        self, texts: List[str], metadatas: Optional[List[dict]] = None
    ) -> List[Document]:
        """
        从文本列表创建文档
        Args:
            texts: 文本列表
            metadatas:
        Returns:
            documents: 文档列表
        """
        _metadatas = metadatas or [{}] * len(texts)
        documents = []
        for i, text in enumerate(texts):
            index = -1
            for chunk in self.split_text(text):
                metadata = copy.deepcopy(_metadatas[i])
                if self._add_start_index:
                    index = text.find(chunk, index + 1)
                    metadata["start_index"] = index
                new_doc = Document(page_content=chunk, metadata=metadata)
                documents.append(new_doc)
        return documents

    def split_documents(self, documents: Iterable[Document]) -> List[Document]:
        """
            切分文档
        Args:
            documents: 文档列表
        Returns:
            documents: 切分后的文档列表
        """
        texts, metadatas = [], []
        for doc in documents:
            texts.append(doc.page_content)
            metadatas.append(doc.metadata)
        return self.create_documents(texts, metadatas=metadatas)

class ChineseRecursiveTextSplitter(RecursiveCharacterTextSplitter):
    """
    该类继承于RecursiveCharacterTextSplitter
    用于中文文本的递归切分
    """

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

    @staticmethod
    def _split_text_with_regex_from_end(text: str, separator: str, keep_separator: bool) -> List[str]:
        """
        根据给定的分隔符（separator）将文本（text）分割成多个部分
        Args:
            text: 待分割的文本
            separator: 分割符列表
            keep_separator: 是否保留分割符
        Returns:
             recombine_list:返回分割后，除去所有空字符串的列表
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
        recombine_list = [s for s in splits if s != ""]  # 重组非空白字符
        return recombine_list

    def _split_text(self, text: str, separators: List[str]) -> List[str]:
        """
        分割文本并返回分割后的文本块。
        Args:
            text:整本书的文本
            separators: 用于分割文本的分隔符列表
        Returns:
            chunks_list： 分割处理后，再删去多余的空白字符和换行符的文本块列表
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
        splits = self._split_text_with_regex_from_end(text, _separator, self._keep_separator)
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
        chunks_list = [re.sub(r"\n{2,}", "\n", chunk.strip()) for chunk in final_chunks if chunk.strip() != ""]
        return chunks_list


class BookSplitTool:
    """
    该类用于切分小说
    1. 将text切成chunk
    2. 将chunk切成segments
    3. 将text切成segments
    """
    # 定义静态变量
    seg1: int = 200
    seg2: int = 1000
    seg3: int = 2000
    seg4: int = 4000
    p1: float = 0.25
    p2: float = 0.25
    p3: float = 0.50

    def __init__(self, seg1: int = None, seg2: int = None, seg3: int = None, seg4: int = None,
                 p1: float = None, p2: float = None, p3: float = None) -> None:
        self.cleaner = ChunkCleanTool()
        if seg1 is not None:
            BookSplitTool.seg1 = seg1
        if seg2 is not None:
            BookSplitTool.seg2 = seg2
        if seg3 is not None:
            BookSplitTool.seg3 = seg3
        if seg4 is not None:
            BookSplitTool.seg4 = seg4
        if p1 is not None:
            BookSplitTool.p1 = p1
        if p2 is not None:
            BookSplitTool.p2 = p2
        if p3 is not None:
            BookSplitTool.p3 = p3

    @staticmethod
    def split_text_into_head_tail(chunk: str, tail_length: int = 200) -> tuple:
        """
        将一个文本块按照tail_length分割成head和tail
        Args:
            chunk:单个文本片段
            tail_length:tail片段的最小长度
        Returns:
            head_text: 前一段文本
            tail_text: 后一段文本
        """
        if not isinstance(chunk, (str, bytes)):
            raise ValueError("The 'text' argument must be a string or bytes-like object, got: {}".format(type(chunk)))
    # 现在可以安全地使用 re.split()
        # 使用正则表达式匹配中文句子结束符，以此来分割文本成句子
        sentences = re.split(split_pattern, chunk)
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

    @staticmethod
    def custom_sampling(seg1: int, seg2: int, seg3: int, seg4: int, p1: float, p2: float, p3: float):
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
            sample: 抽样结果(chunk_size)
        """
        ranges = [(seg1, seg2, p1), (seg2, seg3, p2), (seg3, seg4, p3)]
        # 基于定义的概率随机选择ranges
        selected_range = random.choices(ranges, weights=[r[2] for r in ranges], k=1)[0]
        # 生成一个在选定范围内的随机样本, k:选取次数
        sample = random.randint(selected_range[0], selected_range[1])
        return sample

    @staticmethod
    def convert_book_to_chunks(text: str, len_min: int = 2048) -> tuple:
        """
        将小说切成随机长度的chunk
        Args:
            text:  整本小说的文本内容
            len_min: 小说最小长度，如果小于该值将被过滤
        Returns:
            chunk_list: chunk列表
            chunk_size: chunk的最大长度
        """
        # 进行数据预处理
        if len(text) < len_min:
            print('filter the book and length is ', len(text))
            return None, None
        text = text
        # 将text文本切割为chunk_list
        chunk_size = BookSplitTool.custom_sampling(BookSplitTool.seg1, BookSplitTool.seg2, BookSplitTool.seg3,
                                                   BookSplitTool.seg4,
                                                   BookSplitTool.p1, BookSplitTool.p2, BookSplitTool.p3)
        print('the max length of chunk is {}'.format(chunk_size))
        cs = ChineseRecursiveTextSplitter(chunk_size=chunk_size)
        chunk_list = cs.split_text(text)
        return chunk_list, chunk_size

    @staticmethod
    def convert_chunk_into_head_tail_seg(chunk: str, min_idx: int, max_idx: int, chunk_size: int) -> tuple:
        """
        将chunk切分成两段，切分的位置在min_idx与max_idx之间
         Args：
            chunk:单个文本片段
            min_idx: 最小切分位置
            max_idx: 最大切分位置
            chunk_size: chunk的长度
        Return：
            head_text: 前一段文本
            tail_text: 后一段文本
        """
        assert min_idx > 0 and max_idx > 0 and min_idx < max_idx
        assert abs(max_idx - min_idx) > 3
        # ---切片---
        idx_split_rand = random.randint(min_idx + 1, min(chunk_size, max_idx - 1))
        head_text, tail_text = BookSplitTool.split_text_into_head_tail(chunk, idx_split_rand)
        return head_text, tail_text

    @staticmethod
    def convert_chunk_into_segments(chunk: str, len_seg: int = 512) -> list:
        """
        将一个chunk切分成若干segments
        Args:
            chunk: 小说文本片段
            len_seg: 段落最大长度，seg以分隔符结尾，不会突然结束
        Returns:
            segments: 该chunk切分后的segment列表
        """
        segments = []
        current_segment = ''
        sentences = re.split(split_pattern, chunk)
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

    @staticmethod
    def convert_book_to_segment(text: str, book_len_min: int = 2048, len_seg: int = 512,
                                chunk_sample: bool = True) -> list:
        """
        将一整本书切分成若干segment
        Args:
            text: 整个小说文本
            book_len_min: 小说最小长度，如果小于该值将被过滤
            len_seg: 段落最大长度，seg以分隔符结尾，不会突然结束
            chunk_sample: 只选择这本书的任意一个chunk，为了加快速度
        Returns:
            segments_list: 这整本书切分出的segment列表
        """
        try:
            chunk_list, chunk_size= BookSplitTool.convert_book_to_chunks(text, book_len_min)
            if len(chunk_list) == 0:
                print("chunk_list is empty!")
                return [[]]
            segments_list = []
            for chunk in chunk_list:
                if chunk_sample:
                    chunk = random.choice(chunk_list)
                chunk = ChunkCleanTool.clean_text(chunk)
                if len(chunk) == 0:
                    segments_list.append([])
                segments_per_chunk = BookSplitTool.convert_chunk_into_segments(chunk, len_seg)
                segments_list.append(segments_per_chunk)
                if chunk_sample:
                    break
        except Exception as e:
            print(f"Error processing {text}: {e}")
            return [[]]
        return segments_list
