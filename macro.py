import random, calendar
from collections.abc import Iterable
from typing import Any



#####################
# Noneの処理(""との区別)
#####################

class _EmptyString(int):
    def __str__(self):
        return ""
EmptyString = _EmptyString()

# csv出力時の設定は「quoting=csv.QUOTE_NONNUMERIC」
def replace_none_with_emptystring(row: Iterable[Any]) -> Iterable[Any]:
    return [value if value is not None else EmptyString for value in row]



#####################
# {dd}の書換え処理
#####################

def add_day(yyyymmdd: str) -> str:
    year = int(yyyymmdd[:4])

    if('/' in yyyymmdd):
        month = int(yyyymmdd[5:7])
    else:
        month = int(yyyymmdd[4:6])
    # 指定された年月の最大日数を取得
    max_day = calendar.monthrange(year, month)[1]
    random_day = random.randint(1, max_day)
    yyyymmdd = yyyymmdd.replace('{dd}', f'{random_day:02d}')

    return yyyymmdd


def add_day_datetime(yyyymmddHHMMss: str) -> str:
    # 年月を抽出
    year = int(yyyymmddHHMMss[:4])
    month = int(yyyymmddHHMMss[4:6])

    # 指定された年月の最大日数を取得
    max_day = calendar.monthrange(year, month)[1]
    random_day = random.randint(1, max_day)
    yyyymmddHHMMss = yyyymmddHHMMss.replace('{dd}', f'{random_day:02d}')

    return yyyymmddHHMMss



#####################
# {seq}の書換え処理
#####################

def make_seq():
    seq = 1
    while True:
        yield seq
        seq += 1



# 使用例
if __name__ == '__main__':
    
    print(add_day("202403{dd}"))
    