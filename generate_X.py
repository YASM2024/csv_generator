import os, csv, random
from template import template
from config import Config
from macro import add_day, make_seq, replace_none_with_emptystring


from pprint import pprint

conf = Config()

TITLE = 'ISSUE_X'
CONFIG = conf.config[TITLE]
TEMPLATE = template

OUTPUT_DIR = r'C:\path\to\output'

def mk_csv(folder, table):
    try:
        output_folder = TITLE + '\\' + folder
        FILENAME = f'{table}.csv'

        ######################## データ生成・出力方法を定義 #######################

        def generate(folder, table):
            # configからbluepaintを生成する
            cols = conf.get_cols(TITLE, folder, table)
            
            # bluepaint に、プレースホルダを作成する。
            bluepaint = { 'SUBJID': [] }
            for col in cols: bluepaint[col] = []

            # Configをループして設定書を作成する。
            records_count = 0

            for item in CONFIG[folder][table]:
                values, count = item
                seq_gens = {col: make_seq() for col in cols}  # 各カラムごとにジェネレータを作成

                # values（dict型）のキーが、TEMPLATE[folder][table]の当該テーブルのキーに含まれなかったら、エラーを出す。
                # ここにエラー処理を書く想定・・・
                records_count += count
                for _ in range(count):
                    for col in cols:
                        tmp_val = values[col]
                        # tmp_val に処理が必要な場合には、ここに記載する。
                        if isinstance(tmp_val, str) and '{dd}' in tmp_val: tmp_val = add_day(tmp_val)
                        if isinstance(tmp_val, str) and '{seq}' in tmp_val: 
                            seq_val = next(seq_gens[col]); tmp_val = tmp_val.replace('{seq}', str(seq_val))
                        bluepaint[col].append(tmp_val)
            
            bluepaint['SUBJID'] = list(range(1, records_count + 1))

            # 設定書を検査する。
            rows = len(next(iter(bluepaint.values())))
            if not all(isinstance(value, list) and len(value) == rows for value in bluepaint.values()):
                raise Exception(f"Folder[{folder}] Table[{table}]：bluepaintの各項目がリストであり、かつ要素数が一致している必要があります。プログラムを終了します。")

            # 設定書から各行のデータを生成する。
            for i in range(rows):
                data = TEMPLATE[folder][table].copy()
                # 生成ルールを記載
                data['SUBJID'] = bluepaint["SUBJID"][i]
                for col in cols: data[col] = bluepaint[col][i]

                yield data


    except Exception:
        raise Exception(f"Folder[{folder}] Table[{table}]：メソッド generate で予期せぬエラーが発生しました。")

    #################### csvファイルを出力する ###################

    # フォルダを作成
    outdir = os.path.join(OUTPUT_DIR, output_folder)
    if not os.path.exists(outdir): os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, FILENAME)

    # ファイルを作成
    with open(outpath, 'w', newline='', encoding="utf_8_sig") as f:
        writer = csv.writer(f, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        try:
            header = list(TEMPLATE[folder][table].keys())
            writer.writerow(header)
            # テンプレートとConfigから、各行のレコードを書出す。
            data_rows = generate(folder, table)
            for data in data_rows:
                writer.writerow(replace_none_with_emptystring(data.values()))

        except Exception:
            raise Exception(f"Folder[{folder}] Table[{table}]：テンプレートまたは Config に誤りがある可能性があります。")

    print(f'{TITLE}: {FILENAME} データの作成が完了しました')


# 使いかた
mk_csv( folder = "FOLDER1", table = "TABLE1" )
