class Config:

    config = {

        # 作成件名
        'ISSUE_X':{

            # フォルダ名
            'FOLDER1':{
                
                # テーブル名
                'TABLE1': [

                    # カラム１の値を「0」、カラム２の値を「0」とした組み合わせを10行作成する
                    # 例：[{'カラム１': 0, 'カラム２': 0}, 10]

                    [{'COLUMN1': 0, 'COLUMN2': 0}, 10],
                    [{'COLUMN1': 1, 'COLUMN2': 0}, 10],
                    [{'COLUMN1': 0, 'COLUMN2': 1}, 10],
                    [{'COLUMN1': 1, 'COLUMN2': 1}, 10],
                ],
                
                'TABLE2': [

                    # {dd}は日付を生成する

                    [{'COLUMN3': '202407{dd}'}, 10],
                    [{'COLUMN3': '202408{dd}'}, 10],
                    [{'COLUMN3': '202604{dd}'}, 10],
                    [{'COLUMN3': '202605{dd}'}, 10],            
                ],

                'TABLE3': [

                    # {seq}は連番を生成する

                    [{'COLUMN4': 'YY-{seq}', 'COLUMN5': 1,'COLUMN6': 1,'COLUMN7': 1}, 10],
                    [{'COLUMN4': 'AA-{seq}', 'COLUMN5': 1,'COLUMN6': 2,'COLUMN7': 1}, 10],
                    [{'COLUMN4': 'AA-{seq}', 'COLUMN5': 1,'COLUMN6': 3,'COLUMN7': 1}, 10],
                    [{'COLUMN4': 'AA-{seq}', 'COLUMN5': 1,'COLUMN6': 99,'COLUMN7': 1}, 10],

                ],
            },
            'FOLDER2':{

            },
        }

    }

    def get_cols(self, title: str, folder: str, table: str) -> list:
        tmp_set = set()
        for rule in self.config[title][folder][table]:
            tmp_set |= set(rule[0].keys())
        return list(tmp_set)



if __name__ == '__main__':

    print('configファイルをテストします...')
    from template import template

    conf = Config()

    for title, folders in conf.config.items():

        for folder, item in folders.items():
            
            for table, rules in item.items():
                
                all_cols = list(template[folder][table].keys())
                
                for rule in rules:
                    tested = list(rule[0].keys())

                    # tested が、all_colsに含まれるか
                    if(all(element in all_cols for element in tested)):
                        # 含まれるならOK
                        pass
                    else:
                        # 含まれないならNG
                        raise Exception(f"{title}.{table}の設定に、テンプレートファイルに含まれないカラムがあります。")


    print('configファイルは正常です。')

