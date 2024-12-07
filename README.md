# CSV GENERATOR
## 1. 概要
   このプログラムは、設計図から、csvファイルとそれを含むフォルダ構成を自動生成します。  
## 2. 使用方法
#### 設計図ファイル（template.py）作成
<ol>
   <li>空白、None、文字列、数値など、大体のものは入力可能です。日付型は文字列として入力してください。</li>
   <li>Noneは「,,,」のように囲い文字なし。""は「"","",""」のように囲われます。</li>
   <li>configで指定されなかった場合、そのまま出力されます。</li>
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

#### フォルダの出力先を設定
<div class="snippet-clipboard-content notranslate overflow-auto">
<pre class="notranslate"><code>#generate.py 15行目付近
OUTPUT_DIR = r'C:\path\to\output'
</code></pre>
