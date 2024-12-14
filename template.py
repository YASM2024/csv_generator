template = {

    # フォルダ名を記載
    'FOLDER1':{
        
        # テーブル名を記載
        'TABLE1': {

            # カラム名とデフォルト値を記載
            # 空白、None、文字列、数値など大体のものは入力可能
            # Noneは「,,,」のように囲い文字なし。""は「"","",""」のように囲われる。
            # configで指定されなかった場合、そのまま出力される。
            
            'COLUMN1': None,
            'COLUMN2': 'TEST-DATA',
            'COLUMN3': '',
            'COLUMN4': 0,
            'COLUMN5': "20250101",
            'COLUMN6': 0,
            'COLUMN7': 0,
            'COLUMN8': 0,
            'COLUMN9': 0,
            'COLUMN10': 0,
        },
        'TABLE2' : {
            'COLUMN1': None,
            'COLUMN102': 0,
            'COLUMN3': '99999999',
            'COLUMN104': 0,
            'COLUMN105': 0,
            'COLUMN106': 0,
            'COLUMN107': 0,
            'COLUMN108': 0,
            'COLUMN109': 0,
            'COLUMN110': 0,
        },
        'TABLE3' : {
            'COLUMN1': None,
            'COLUMN202': 0,
            'COLUMN203': 0,
            'COLUMN4': None,
            'COLUMN5': 0,
            'COLUMN6': 0,
            'COLUMN7': 0,
            'COLUMN208': 0,
            'COLUMN209': 0,
            'COLUMN210': 0,
        },
    },
    'FOLDER2':{
    },
    'FOLDER3':{
    },

}


if __name__ == '__main__':

    print("templateファイルに不正がないかチェックします...")

    print('文法エラーが無ければ問題なし。')