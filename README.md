# CSV GENERATOR
1. 概要
   このプログラムは、設計図から、csvファイルとそれを含むフォルダ構成を自動生成します。  
1. 使用方法
<li>設計図ファイル（config.py）作成</li>
- 空白、None、文字列、数値など、大体のものは入力可能です。日付型は文字列として入力してください。
- Noneは「,,,」のように囲い文字なし。""は「"","",""」のように囲われます。
- configで指定されなかった場合、そのまま出力されます。
<div class="snippet-clipboard-content notranslate overflow-auto">
<pre class="notranslate"><code>template = {<br>
    # フォルダ名を記載<br>
    'FOLDER1':{<br>
        # テーブル名を記載<br>
        'TABLE1': {<br>
            # カラム名とデフォルト値を記載<br>
            'COLUMN1': None,<br>
            'COLUMN2': 'TEST-DATA',<br>
            'COLUMN3': '',<br>
            'COLUMN4': 0,<br>
            'COLUMN5': "20250101",<br>
             ...<br>
        },<br>
    },<br>
}`<br>
</code></pre>
<li>フォルダの出力先を設定</li>
<div class="snippet-clipboard-content notranslate overflow-auto">
<pre class="notranslate"><code>#generate.py 15行目付近
OUTPUT_DIR = r'C:\path\to\output'
</code></pre>
