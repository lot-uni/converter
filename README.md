# converterとは
フォルダ階層から開発中の防災アプリのシステム内で使用する独自のclass?(以下「ライトニング配列」という)を生成するライブラリです。
このライブラリを使う事で、フォルダとmarkdownファイルだけでライトニング配列を作成する事ができます。
ライトニング配列はAnserとQuestionの二つのファイルで構成されており、Anserの配列はmarkdownファイルの内容を用いて生成しています。

# converterの利用例
以下の例では **：脊椎を持っている動物ですか？** というフォルダ構造からclassを生成してみます。
## 注意
outputというフォルダがなければ本ライブラリは正常に動作できません！
## デモの環境
フォルダ構造
```
.
├── main.py
├── output
└── ：脊椎を持っている動物ですか？
    ├── 持っていない：この無脊椎動物はどのグループに属しますか？
    │   ├── それ以外
    │   │   └── another.md
    │   ├── 軟体動物
    │   │   └── nantai.md
    │   └── 節足動物：この中から選んで
    │       ├── 昆虫類
    │       │   └── kontixyuu.md
    │       ├── 甲殻類
    │       │   └── koukaku.md
    │       ├── 蜘蛛類
    │       │   └── spider.md
    │       ├── ムカデ類
    │       │   └── mukade.md
    │       └── ヤスデ類
    │           └── yasude.md
    └── 持っている：この脊椎動物はどのグループに属していますか？
        ├── 魚類
        │   └── fish.md
        ├── 鳥類
        │   └── bird.md
        ├── 両生類
        │   └── amphibian.md
        ├── 哺乳類
        │   └── mammalian.md
        └── 爬虫類
            └── reptiles.md
```
main.py
``` 
import converter as cvt
```

## 結果

フォルダ構造
```
.
├── main.py
├── output
│   ├── Anser
│   └── Question
└── ：脊椎を持っている動物ですか？
    ├── 持っていない：この無脊椎動物はどのグループに属しますか？
    │   ├── それ以外
    │   │   └── another.md
    │   ├── 軟体動物
    │   │   └── nantai.md
    │   └── 節足動物：この中から選んで
    │       ├── 昆虫類
    │       │   └── kontixyuu.md
    │       ├── 甲殻類
    │       │   └── koukaku.md
    │       ├── 蜘蛛類
    │       │   └── spider.md
    │       ├── ムカデ類
    │       │   └── mukade.md
    │       └── ヤスデ類
    │           └── yasude.md
    └── 持っている：この脊椎動物はどのグループに属していますか？
        ├── 魚類
        │   └── fish.md
        ├── 鳥類
        │   └── bird.md
        ├── 両生類
        │   └── amphibian.md
        ├── 哺乳類
        │   └── mammalian.md
        └── 爬虫類
            └── reptiles.md
```

Question
```
[
    Question(
        message: "脊椎を持っている動物ですか？",
        choices: [
            Choice(text: "持っている", next:1, finish:false),
            Choice(text: "持っていない", next:2, finish:false),
        ]
    ),
    Question(
        message: "この脊椎動物はどのグループに属していますか？",
        choices: [
            Choice(text: "鳥類", next:0, finish:true),
            Choice(text: "爬虫類", next:1, finish:true),
            Choice(text: "魚類", next:2, finish:true),
            Choice(text: "両生類", next:3, finish:true),
            Choice(text: "哺乳類", next:4, finish:true),
        ]
    ),
    Question(
        message: "この無脊椎動物はどのグループに属しますか？",
        choices: [
            Choice(text: "節足動物", next:3, finish:false),
            Choice(text: "それ以外", next:5, finish:true),
            Choice(text: "軟体動物", next:6, finish:true),
        ]
    ),
    Question(
        message: "この中から選んで",
        choices: [
            Choice(text: "昆虫類", next:7, finish:true),
            Choice(text: "ヤスデ類", next:8, finish:true),
            Choice(text: "甲殻類", next:9, finish:true),
            Choice(text: "ムカデ類", next:10, finish:true),
            Choice(text: "蜘蛛類", next:11, finish:true),
        ]
    ),
]
```

Anser
```
[
    Anser(
        title: "bird",
        detail: ""
    ),
    Anser(
        title: "reptiles",
        detail: ""
    ),
    Anser(
        title: "fish",
        detail: ""
    ),
    Anser(
        title: "amphibian",
        detail: ""
    ),
    Anser(
        title: "mammalian",
        detail: ""
    ),
    Anser(
        title: "kontixyuu",
        detail: ""
    ),
    Anser(
        title: "yasude",
        detail: ""
    ),
    Anser(
        title: "koukaku",
        detail: ""
    ),
    Anser(
        title: "mukade",
        detail: ""
    ),
    Anser(
        title: "spider",
        detail: ""
    ),
    Anser(
        title: "another",
        detail: ""
    ),
    Anser(
        title: "nantai",
        detail: ""
    ),
]
```
# 最後に
これから公開予定のplaygroundsのプロジェクトも公開できたらこのライブラリが皆様の役に立つかも知れません
(役に立つとは言っていない)


