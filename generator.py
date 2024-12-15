class Generator:
    
    def __init__(self, config_file):
        import configparser
        
        # configファイルからディレクトリ設定を取得する
        self.__config = configparser.ConfigParser()
        self.__config.read(config_file)

    def mk_csv(self, folder, table):

        import os, csv, random
        from template import template
        from pprint import pprint
        from setting_handler import SettingHandler
        from macro import add_day, make_seq, replace_none_with_emptystring

        try:

            TITLE = self.__config.get('config', 'title')
            OUTPUT_DIR = self.__config.get('config', 'output')
            SETTING_DIR = self.__config.get('config', 'setting')
            
            sh = SettingHandler(SETTING_DIR)
            output_folder = fr'{TITLE}\{folder}'
            filename = f'{table}.csv'

            ######################## データ生成・出力方法を定義 #######################

            def generate(folder, table):
                # settingからblueprintを生成する
                cols = sh.get_cols(TITLE, folder, table)
                
                # blueprint に、プレースホルダを作成する。
                blueprint = { 'COLUMN1': [] }
                for col in cols: blueprint[col] = []

                # settingをループして設定書を作成する。
                records_count = 0

                for item in sh.setting[TITLE][folder][table]:
                    values, count = item
                    seq_gens = {col: make_seq() for col in cols}  # 各カラムごとにジェネレータを作成

                    # values（dict型）のキーが、 template[folder][table]の当該テーブルのキーに含まれなかったら、エラーを出す。
                    # ここにエラー処理を書く想定・・・
                    records_count += count
                    for _ in range(count):
                        for col in cols:
                            tmp_val = values[col]
                            # tmp_val に処理が必要な場合には、ここに記載する。
                            if isinstance(tmp_val, str) and '{dd}' in tmp_val: tmp_val = add_day(tmp_val)
                            if isinstance(tmp_val, str) and '{seq}' in tmp_val: 
                                seq_val = next(seq_gens[col]); tmp_val = tmp_val.replace('{seq}', str(seq_val))
                            blueprint[col].append(tmp_val)
                
                # COLUMN1に値が入っていない場合には、連番で埋める。
                if len(blueprint['COLUMN1']) == 0:
                    blueprint['COLUMN1'] = list(range(1, records_count + 1))

                # 設定書を検査する。
                rows = len(next(iter(blueprint.values())))
                if not all(isinstance(value, list) and len(value) == rows for value in blueprint.values()):
                    raise Exception(f"Folder[{folder}] Table[{table}]：blueprintの各項目がリストであり、かつ要素数が一致している必要があります。プログラムを終了します。")

                # 設定書から各行のデータを生成する。
                for i in range(rows):
                    data = template[folder][table].copy()
                    # 生成ルールを記載
                    data['COLUMN1'] = blueprint["COLUMN1"][i]
                    for col in cols: data[col] = blueprint[col][i]

                    yield data


        except Exception:
            raise Exception(f"Folder[{folder}] Table[{table}]：メソッド generate で予期せぬエラーが発生しました。")

        #################### csvファイルを出力する ###################

        # フォルダを作成
        outdir = os.path.join(OUTPUT_DIR, output_folder)
        if not os.path.exists(outdir): os.makedirs(outdir, exist_ok=True)
        outpath = os.path.join(outdir, filename)

        # ファイルを作成
        with open(outpath, 'w', newline='', encoding="utf_8_sig") as f:
            writer = csv.writer(f, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            try:
                header = list(template[folder][table].keys())
                writer.writerow(header)
                # テンプレートとConfigから、各行のレコードを書出す。
                data_rows = generate(folder, table)
                for data in data_rows:
                    writer.writerow(replace_none_with_emptystring(data.values()))

            except Exception:
                raise Exception(f"Folder[{folder}] Table[{table}]：テンプレートまたは Config に誤りがある可能性があります。")

        print(f'{TITLE}: {filename} データの作成が完了しました')


# 使いかた
generator = Generator(config_file = "./config.ini")
generator.mk_csv(folder = "FOLDER1", table = "TABLE1")
generator.mk_csv(folder = "FOLDER1", table = "TABLE2")
generator.mk_csv(folder = "FOLDER1", table = "TABLE3")
