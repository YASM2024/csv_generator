# CSV GENERATOR
## 1. 概要
   このプログラムは、ひな形と設計図から、csvファイルとそれを含むフォルダ構成を自動生成します。  
   主に、csvファイルを扱うプログラムをテストするための、仮想データを作成することを想定しています。  
## 2. 使用方法
#### ひな形ファイル（template.py）作成
<ol>
   <li>空白、None、文字列、数値など、大体のものは入力可能です。日付型は文字列として入力してください。</li>
   <li>Noneは「,,,」のように囲い文字なし。""は「"","",""」のように囲われます。</li>
   <li>settingで指定されなかった場合、デフォルト値がそのまま出力されます。</li>
</ol>
<div class="snippet-clipboard-content notranslate overflow-auto">
<pre class="notranslate"><code>#template.py<br>
template = {<br>
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

#### 設計図ファイル（setting.json）を作成
<div class="snippet-clipboard-content notranslate overflow-auto">
<pre class="notranslate"><code>#setting.json<br>
{<br>
    "ISSUE1": { ・・・・作成件名<br>
        "FOLDER1": {・・・・フォルダ名<br>
            "TABLE1": [・・・・テーブル名<br>
                （例）カラム１の値を「0」、カラム２の値を「0」とした組み合わせを10行作成する<br>
                [{"COLUMN1": 0,"COLUMN2": 0},10],<br>
                [{"COLUMN1": 1,"COLUMN2": 0},10],<br>
                [{"COLUMN1": 0.0,"COLUMN2": 1.0},10],<br>
                [{"COLUMN1": 1,"COLUMN2": 1},10]<br>
            ],<br>
            "TABLE2": [・・・・テーブル名<br>
                （例）{dd}はランダムな日付を生成する<br>
                [{"COLUMN3": "202407{dd}"},10],<br>
                [{"COLUMN3": "202408{dd}"},10],<br>
                [{"COLUMN3": "202604{dd}"},10],<br>
                [{"COLUMN3": "202605{dd}"},10]<br>
            ],<br>
            "TABLE3": [・・・・テーブル名<br>
                （例）{seq}は連番を生成する<br>
                [{"COLUMN4": "YY-{seq}","COLUMN5": 1,"COLUMN6": 1.0,"COLUMN7": 1},10],<br>
                [{"COLUMN4": "AA-{seq}","COLUMN5": 1,"COLUMN6": 2.0,"COLUMN7": 1},10],<br>
                [{"COLUMN4": "AA-{seq}","COLUMN5": 1,"COLUMN6": 3,"COLUMN7": 1},10],<br>
                [{"COLUMN4": "AA-{seq}","COLUMN5": 1,"COLUMN6": 99,"COLUMN7": 1},10]<br>
            ]<br>
        },<br>
        "FOLDER2": {・・・・フォルダ名<br>
            <br>
        }<br>
    }<br>
}<br>
</code></pre>
               

#### 作成件名・出力フォルダパス・設計図ファイルパスを設定（config.ini）
<div class="snippet-clipboard-content notranslate overflow-auto">
<pre class="notranslate"><code>#config.ini
title = issue_title (作成件名)
output = C:\path\to\output (出力フォルダパス)
setting = C:\path\to\setting.json (設計図ファイルパス)
</code></pre>
