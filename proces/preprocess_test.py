import unittest

from proces import delete_blank_character
from proces import uppercase_to_lowercase
from proces import traditional_to_simplified
from proces import full_angle_to_half_angle
from proces import preprocess


class TestPreprocess(unittest.TestCase):
    def setUp(self) -> None:
        self.dbc_data = {
            "删除 空白  字符": "删除空白字符",
            " 删除 空白 字符": "删除空白字符",
            " 删 除 空 白 字 符 ": "删除空白字符",
        }

        self.utl_data = {
            "UP": "up",
            "low": "low",
            "UPtoLOW": "uptolow",
        }

        self.tts_data = {
            "我幹什麼不干你事": "我干什么不干你事",
            "機械計算機的應用已經完全被電子計算機所取代": "机械计算机的应用已经完全被电子计算机所取代",
            "符號": "符号",
        }

        self.fth_data = {
            "（hi）": "(hi)",
            "你好：": "你好:",
            "！": "!",
        }

    def test_delete_blank_character(self) -> None:
        for key, value in self.dbc_data.items():
            self.assertEqual(delete_blank_character(key), value)

    def test_uppercase_to_lowercase(self) -> None:
        for key, value in self.utl_data.items():
            self.assertEqual(uppercase_to_lowercase(key), value)

    def test_traditional_to_simplified(self) -> None:
        for key, value in self.tts_data.items():
            self.assertEqual(traditional_to_simplified(key), value)

    def test_full_angle_to_half_angle(self) -> None:
        for key, value in self.fth_data.items():
            print(full_angle_to_half_angle(key))
            self.assertEqual(full_angle_to_half_angle(key), value)

    def test_preprocess(self) -> None:
        for key, value in self.dbc_data.items():
            self.assertEqual(preprocess(key), value)
        for key, value in self.utl_data.items():
            self.assertEqual(preprocess(key), value)
        for key, value in self.tts_data.items():
            self.assertEqual(preprocess(key), value)
        for key, value in self.fth_data.items():
            self.assertEqual(preprocess(key), value)


if __name__ == '__main__':
    unittest.main()
