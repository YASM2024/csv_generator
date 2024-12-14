class SettingHandler():

    def __init__(self, file_path):
        self.__setting = {}
        with open(file_path, 'r', encoding='utf-8') as file:
            code = file.read()
            exec(code, globals(), locals())
        self.__setting = locals()['setting']


    def get_cols(self, title: str, folder: str, table: str) -> list:
        tmp_set = set()
        for rule in self.__setting[title][folder][table]:
            tmp_set |= set(rule[0].keys())
        return list(tmp_set)

    @property
    def setting(self):
        return self.__setting

    @setting.setter
    def setting(self, value):
        self.__setting = value


if __name__ == '__main__':

    print('settingファイルをテストします...')
    try:
        from template import template

        sh = SettingHandler(r'C:\Users\Public\Documents\git\csv_generator\setting.txt')
        setting = sh.setting

        for title, folders in setting.items():
        
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
                    
        
        
        print('settingファイルは正常です。')
    
    except Exception as e:
        print(f"エラー発生。settingファイルが異常です。{e}")

