# Proces

[![Pypi](https://img.shields.io/pypi/v/proces.svg)](https://pypi.org/project/proces/)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/Ailln/proces/blob/master/LICENSE)
[![stars](https://img.shields.io/github/stars/Ailln/proces.svg)](https://github.com/Ailln/proces/stargazers)

🐨 文本预处理。

## 1 安装

> ⚠️ 注意：
> 1. 本地安装仅支持 Python 的 3.6 以上版本；
> 2. 尽可能使用 `proces` 的最新版本。

### 使用 pip 安装

```shell
pip install proces -U
```

### 从代码库安装

```shell
git clone https://github.com/Ailln/proces.git

cd proces && python setup.py install
```

## 2 使用

```python
from proces import preprocess

# 默认会按照顺序执行，处理空白字符、大写转小写、繁体转简体、全角转半角
result = preprocess("Today, 你 幹 什 麼 ！")
# result: today,你干什么!

# 配置 pipeline，比如只去除空白字符
result = preprocess("Today, 你 幹 什 麼 ！", pipelines=["handle_blank_character"])
# result: Today,你幹什麼！

# 单独使用子方法
from proces import handle_blank_character
from proces import uppercase_to_lowercase
from proces import traditional_to_simplified
from proces import full_angle_to_half_angle
from proces import handle_substitute

# 处理空白字符
result = handle_blank_character("空 白 字 符")
# result: 空白字符
result = handle_blank_character("空 白 字 符", ",")
# result: 空,白,字,符

# 大写转小写
result = uppercase_to_lowercase("UP to low")
# result: up to low

# 繁体转简体
result = traditional_to_simplified("我幹什麼不干你事")
# result: 我干什么不干你事

# 全角转半角
result = full_angle_to_half_angle("你好！")
# result: 你好!

# 替换一些字符
result = handle_substitute("你好！/:-", r"/:-", "表情")
# result: 你好！表情
```

## 3 TODO

- [x] add get all methods of preprocess
- [ ] 装饰器

## 4 许可

[![](https://award.dovolopor.com?lt=License&rt=MIT&rbc=green)](./LICENSE)
