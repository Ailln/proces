import re
from typing import Union
from typing import Optional

from zhconv import convert


def handle_blank_character(text: str, repl: Optional[str] = None) -> str:
    """处理空白字符，默认替换成空字符

    Attributes:
        text: input text
        repl: replace text
    """
    if repl is None:
        repl = ""
    return re.sub(r"\s+", repl, text)


def uppercase_to_lowercase(text: str) -> str:
    """大写转小写

    Attributes:
        text: input text
    """
    return text.lower()


def traditional_to_simplified(text: str) -> str:
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


def handle_substitute(text: str, ptn: str, repl: str) -> str:
    """替换一些字符

    Attributes:
        text: input text
        ptn: re pattern
        repl: replace text
    """
    return re.sub(ptn, repl, text)


def preprocess(data: Union[str, list], pipelines: Optional[list] = None, params: Optional[dict] = None) \
        -> Union[str, list]:
    """文本预处理

    Attributes:
        data: input data.
        pipelines: default is
            ["handle_blank_character",
            "uppercase_to_lowercase",
            "traditional_to_simplified",
            "full_angle_to_half_angle"]
        params: function parameters
    """
    all_pipelines = [
        "handle_blank_character",
        "uppercase_to_lowercase",
        "traditional_to_simplified",
        "full_angle_to_half_angle",
        "handle_substitute"
    ]

    default_pipelines = [
        "handle_blank_character",
        "uppercase_to_lowercase",
        "traditional_to_simplified",
        "full_angle_to_half_angle"
    ]
    if pipelines is None:
        pipelines = default_pipelines

    if type(data) == str:
        data_list = [data]
    else:
        data_list = data

    results = []
    for text in data_list:
        for func in pipelines:
            if func in all_pipelines:
                if params is not None and func in params.keys():
                    text = eval(f"{func}(text, *{params[func]})")
                else:
                    text = eval(f"{func}(text)")
            else:
                raise ValueError(f"pipeline: {func} not support!")
        results.append(text)

    if type(data) == str:
        return results[0]
    else:
        return results
