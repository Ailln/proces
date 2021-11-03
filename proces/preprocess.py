import re
from typing import Union
from typing import Optional

from zhconv import convert


def delete_blank_character(text: str) -> str:
    """删除空白字符

    Attributes:
        text: input text
    """
    return re.sub(r"\s*", "", text)


def uppercase_to_lowercase(text: str) -> str:
    """大写转小写

    Attributes:
        text: input text
    """
    return text.lower()


def simplified_to_traditional(text: str) -> str:
    """繁体转简体

    Attributes:
        text: input text
    """
    return convert(text, "zh-cn")


def full_angle_to_half_angle(text: str) -> str:
    """全角转半角

    Attributes:
        text: input text
    """
    result = ""
    for uchar in text:
        inside_code = ord(uchar)
        if inside_code == 12288:  # 全角空格直接转换
            inside_code = 32
        elif 65281 <= inside_code <= 65374:  # 全角字符（除空格）根据关系转化
            inside_code -= 65248

        result += chr(inside_code)
    return result


def preprocess(data: Union[str, list], pipelines: Optional[list] = None):
    """文本预处理

    Attributes:
        data: input data.
        pipelines: default ["delete_blank_character", "uppercase_to_lowercase", "simplified_to_traditional", "full_angle_to_half_angle"]
    """
    all_pipelines = [
        "delete_blank_character",
        "uppercase_to_lowercase",
        "simplified_to_traditional",
        "full_angle_to_half_angle"
    ]
    if pipelines is None:
        pipelines = all_pipelines

    if type(data) == str:
        data_list = [data]
    else:
        data_list = data

    results = []
    for text in data_list:
        for func in pipelines:
            if func in all_pipelines:
                text = eval(f"{func}(text)")
            else:
                raise ValueError(f"pipeline: {func} not support!")
        results.append(text)

    if type(data) == str:
        return results[0]
    else:
        return results
