from typing import Set, Pattern
from re import compile

from proces.util.conf import get_yaml


def get_all_cities() -> Set:
    stream_args = ["proces", "data/province_city.yaml"]
    cities = set()
    for province, p_value in get_yaml(stream_args).items():
        cities.add(province)
        for city in p_value:
            cities.add(f"{province}/{city}")
    return cities


def get_city_pattern() -> Pattern[str]:
    province_cache = {}

    def get_province_item_unit(province_data):
        if province_data not in province_cache.keys():
            if province_data[-5:] in ["特别行政区"]:
                item, unit = province_data[:-5], province_data[-5:]
            elif province_data[-3:] in ["自治区"]:
                if province_data[-4] == "族":
                    item, unit = province_data[:-5], province_data[-5:]
                else:
                    item, unit = province_data[:-3], province_data[-3:]
            elif province_data[-1] in ["省", "市"]:
                item, unit = province_data[:-1], province_data[-1]
            else:
                raise Exception(province_data)

            province_cache[province_data] = (item, unit)
        else:
            item, unit = province_cache[province_data]
        return item, unit

    city_cache = {}

    def get_city_item_unit(city_data):
        if city_data not in city_cache.keys():
            if city_data[-3:] in ["自治县", "自治州"]:
                item, unit = city_data[:-3], city_data[-3:]
            elif city_data[-2:] in ["林区", "地区"]:
                if city_data[-4] == "族":
                    item, unit = city_data[:-5], city_data[-5:]
                else:
                    item, unit = city_data[:-3], city_data[-3:]
            elif city_data[-1] in ["县", "市", "盟"]:
                item, unit = city_data[:-1], city_data[-1]
            else:
                raise Exception(city_data)
            city_cache[city_data] = (item, unit)
        else:
            item, unit = city_cache[city_data]

        return item, unit

    patterns = set()
    for line in get_all_cities():
        if "/" in line:
            province, city = line.split("/")
            p_item, p_unit = get_province_item_unit(province)
            c_item, c_unit = get_city_item_unit(city)
            patterns.add(f"{p_item}({p_unit})?{c_item}({c_unit})?")
            patterns.add(f"{c_item}({c_unit})?")
        else:
            province = line
            p_item, p_unit = get_province_item_unit(province)
            patterns.add(f"{p_item}({p_unit})?")

    patterns = sorted(patterns, key=lambda x: len(x), reverse=True)
    ptn_str = "|".join(patterns)
    return compile(f"({ptn_str})")
