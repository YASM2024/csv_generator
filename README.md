# CSV GENERATOR
## 1. 概要
   このプログラムは、ひな形と設計図から、csvファイルとそれを含むフォルダ構成を自動生成します。  
## 2. 使用方法
#### ひな形ファイル（template.py）作成
<ol>
   <li>空白、None、文字列、数値など、大体のものは入力可能です。日付型は文字列として入力してください。</li>
   <li>Noneは「,,,」のように囲い文字なし。""は「"","",""」のように囲われます。</li>
   <li>configで指定されなかった場合、デフォルト値がそのまま出力されます。</li>
</ol>
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
}<br>
</code></pre>

#### 設計図ファイル（config.py）を作成
<div class="snippet-clipboard-content notranslate overflow-auto">
<pre class="notranslate"><code>class Config:<br>
    config = {<br>
        # 作成件名<br>
        'ISSUE_X':{<br>
            # フォルダ名<br>
            'FOLDER1':{<br>
                # テーブル名<br>
                'TABLE1': [<br>
                    # カラム１の値を「0」、カラム２の値を「0」とした組み合わせを10行作成する<br>
                    # 例：[{'カラム１': 0, 'カラム２': 0}, 10]<br>
                    [{'COLUMN1': 0, 'COLUMN2': 0}, 10],<br>
                    [{'COLUMN1': 1, 'COLUMN2': 0}, 10],<br>
                ],<br>
                'TABLE2': [<br>
                    # {dd}は日付を生成する<br>
                    [{'COLUMN3': '202407{dd}'}, 10],<br>
                ],<br>
                'TABLE3': [<br>
                    # {seq}は連番を生成する<br>
                    [{'COLUMN4': 'YY-{seq}', 'COLUMN5': 1,'COLUMN6': 1,'COLUMN7': 1}, 10],<br>
                ],<br>
            }<br>
         }<br>
      }<br>
</code></pre>
               

#### フォルダの出力先を設定
<div class="snippet-clipboard-content notranslate overflow-auto">
<pre class="notranslate"><code>#generate.py 15行目付近
OUTPUT_DIR = r'C:\path\to\output'
</code></pre>
