# Kurocoドキュメント: リファレンス / コンテンツ管理（1/3）

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- グループ化・繰り返しを行ったコンテンツ項目の制御（`control-of-grouped-and-repeated-content-items`）
- フォーム定義で利用できるフォーム項目一覧（`form-field-list`）
- Kurocoで利用される共通Object型定義（`general-object-type`）
- JSON Schemaパターンサンプル（`json-column-schema`）
- Kurocoのキーワード検索の種類（`keyword-search-types`）


---

# グループ化・繰り返しを行ったコンテンツ項目の制御

> 元ページ: `reference/control-of-grouped-and-repeated-content-items` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/control-of-grouped-and-repeated-content-items/
> 概要: Kurocoでは、コンテンツ定義においてグループ化や繰り返しの設定を行うことで、柔軟なコンテンツ管理が可能です。本ドキュメントでは、グループ化や繰り返しを用いたコンテンツをAPIで扱う際に、レスポンスがどのように変化するのか、また更新時にどのような形式でリクエストを送信すればよいのかについて解説します。

Kurocoでは、コンテンツ定義においてグループ化や繰り返しの設定を行うことで、柔軟なコンテンツ管理が可能です。  
本ドキュメントでは、グループ化や繰り返しを用いたコンテンツをAPIで扱う際に、レスポンスがどのように変化するのか、また更新時にどのような形式でリクエストを送信すればよいのかについて解説します。

## APIレスポンス構造

`Topics::list` や `Topics::details` のエンドポイントでデータを取得する場合のレスポンス構造を説明します。

### 繰り返し
項目に繰り返しを設定すると設定した値が配列でレスポンスされます。  
繰り返しの途中のデータを削除した場合は配列の前方に詰められ、空のデータは含まれません。

```json
    "repeat_texts": [
      "text1",
      "text2",
      "text3"
    ],
```

### グループ化
項目をグループ化した場合、`ext_group`のパラメータを有効にしているか否かでレスポンスの形式が異なります。

**ext_group=trueの場合**  
グループ化された項目が1つのオブジェクトにまとまります。  
オブジェクトの項目名に対して管理画面でslugの設定が可能です。  

```json
   "groups": {
      "choice": {
        "key": "key1",
        "label": "value1"
      },
      "image": {
        "id": "2740_ext_04_0",
        "url": "https://xxxxxx.g.kuroco-img.app/v=1747392576/files/topics/2740_ext_4_0.png",
        "desc": "",
        "url_org": "https://xxxxxx.g.kuroco-img.app/files/topics/2740_ext_4_0.png"
      },
      "text": "text"
    },
```

**ext_group=falseの場合**  
それぞれのAPIのレスポンスとなり、レスポンス上はグループ化しない場合と変わりません。

```json
    "choice": {
      "key": "key1",
      "label": "value1"
    },
    "image": {
      "id": "2740_ext_04_0",
      "url": "https://xxxxxx.g.kuroco-img.app/v=1747392576/files/topics/2740_ext_4_0.png",
      "desc": "",
      "url_org": "https://xxxxxx.g.kuroco-img.app/files/topics/2740_ext_4_0.png"
    },
    "text": "text",
```

### 繰り返し+グループ化

**ext_group=trueの場合**  
グループ化されたオブジェクトが配列でレスポンスされます。

```json
    "groups": [
      {
        "choice": {
          "key": "key1",
          "label": "value1"
        },
        "image": {
          "id": "2740_ext_07_0",
          "url": "https://xxxxxx.g.kuroco-img.app/v=1747392576/files/topics/2740_ext_7_0.png",
          "desc": "",
          "url_org": "https://xxxxxx.g.kuroco-img.app/files/topics/2740_ext_7_0.png"
        },
        "text": "text1"
      },
      {
        "choice": {
          "key": "key2",
          "label": "value2"
        },
        "image": {
          "id": "2740_ext_07_1",
          "url": "https://xxxxxx.g.kuroco-img.app/v=1747392576/files/topics/2740_ext_7_1.png",
          "desc": "",
          "url_org": "https://xxxxxx.g.kuroco-img.app/files/topics/2740_ext_7_1.png"
        },
        "text": "text2"
      }
    ],
```

**ext_group=falseの場合**  
それぞれのAPIのレスポンスが配列で返ります。  
グループ化の一部に空のデータがある場合は`""`や`{}`が配列に含まれ、配列のデータ数はグループ化された各項目で同じになります。

```json
    "choice": [
      {
        "key": "key1",
        "label": "value1"
      },
      {
        "key": "key2",
        "label": "value2"
      }
    ],
    "image": [
      {
        "id": "2740_ext_07_0",
        "url": "https://xxxxxx.g.kuroco-img.app/v=1747392576/files/topics/2740_ext_7_0.png",
        "desc": "",
        "url_org": "https://xxxxxx.g.kuroco-img.app/files/topics/2740_ext_7_0.png"
      },
      {
        "id": "2740_ext_07_1",
        "url": "https://xxxxxx.g.kuroco-img.app/v=1747392576/files/topics/2740_ext_7_1.png",
        "desc": "",
        "url_org": "https://xxxxxx.g.kuroco-img.app/files/topics/2740_ext_7_1.png"
      }
    ],
    "text": [
      "",
      "text2"
    ],
```

## APIによる更新

`Topics::update` や `Topics::bulk_upsert` のエンドポイントでデータを更新する場合、基本的には`Topics::details`で取得したレスポンスと同じ構造でリクエストをしますが、グループ化や繰り返しの設定がされた項目を更新する場合には以下の注意点があります。

- グループ化された項目群は全ての項目をPOSTする必要があります。
- 変更しない項目は変更前と同じ値をPOSTしてください。
- 画像の項目は`id`と`desc`の項目のみPOSTします。(`desc`は省略可)

以下にグループ化+繰り返しをした項目を更新する場合の事例を紹介しますので参考にしてください。  
ext_group=trueを設定した`Topoics::update`のエンドポイントを利用する想定で書かれています。

### 一部のデータを差し替える

一部のデータを差し替える場合は`Topics::details`で取得したレスポンスを元に変更したい項目を書き換えてPOSTします。

```json
{
  "text_group": [
    {
      "text_1": "text1-1",      //既存のデータと同一の値をPOST
      "text_2": "New text"      //任意の値をPOST
    },
    {
      "text_1": "text2-1",      //既存のデータと同一の値をPOST
      "text_2": "text2-2"       //既存のデータと同一の値をPOST
    }
  ]
}
```

#### NG例
グループ化された項目群は全項目POSTする必要があります。
以下のように一部の項目を除外し項目数に差が出る場合、データの並び順が不正になることがありますのでご注意ください。

```json
{
  "text_group": [
    {
      "text_1": "text1-1",      //既存のデータと同一の値をPOST
                                //text_2を含めない
    },
    {
      "text_1": "text2-1",      //既存のデータと同一の値をPOST
      "text_2": "text2-2"       //既存のデータと同一の値をPOST
    }
  ]
}
```

### 一部の画像を差し替える

画像の差替えを行いたい場合は、アップロードしたいファイルを `Files::upload` のエンドポイントでKurocoの一時領域にアップロードし、取得した`file_id`をリクエストボディに追加します。

```json
{
  "groups": [
    {
      "choice": {
        "key": "key1",
        "label": "value1"
      },
      "image": {
        "id": "2740_ext_07_0",
        "desc": "test image1"
      },
      "text": "text1"
    },
    {
      "choice": {
        "key": "key2",
        "label": "value2"
      },
      "image": {
        "id": "2740_ext_07_1",
        "file_id": "files/temp/6217dfe10e096f03dce0dc2a60df8240785d5b13880d72477f18c0ff71597070.png",  //差し替えるファイル
        "desc": "test image2"
      },
      "text": "text2"
    }
  ]
}
```

<!--以下はPOSTに含まれない画像"id": "2740_ext_07_0",が消え、データが壊れるので利用不可-->
<!--
画像に対して振られたidを指定して更新する方法

```json
{
  "repeat_groups": [
    {
      "r_image": {
        "id": "2740_ext_07_1",
        "file_id": "files/temp/985a12e67d73c9fc91be443ebf87ea0287f64f2708a70bb46ca56efe57dd0453.png",
        "desc": "test image2"
      }
    }
  ]
}
```
-->

### 並び順を変える

並び順を変える場合は `Topics::details`で取得したレスポンスを元にグループ単位で順番を変えてPOSTします。

```json
{
  "repeat_groups": [
    {
      "r_choice": {
        "key": "key2",
        "label": "value2"
      },
      "r_image": {
        "id": "2740_ext_07_1",
        "desc": "test image2"
      },
      "r_text": "text2"
    },
    {
      "r_choice": {
        "key": "key1",
        "label": "value1"
      },
      "r_image": {
        "id": "2740_ext_07_0",
        "desc": "test image1"
      },
      "r_text": "text1"
    }
  ]
}
```
#### NG例
グループに複数の画像が含まれる場合、一部だけ入れ替える事はできません。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2f7c5b8939111f8b5ad1e5094cd09ebf.png)

`Topics::update`へのリクエストボディの例で言うと以下の例などです。  

```json
{
  "repeat_multi_image": [
    {
      "image1": {
        "id": "2740_ext_09_1"
      },
      "image2": {
        "id": "2740_ext_10_0"
      }
    },
    {
      "image1": {
        "id": "2740_ext_09_0"
      },
      "image2": {
        "id": "2740_ext_10_1"
      }
    }
  ]
}
```

グループ内で複数のindex番号(_X)が混在することはできませんので、一部の画像を別のグループと入れ替えたい場合は、画像の差し替えをしてください。

### 繰り返しの一部を削除する

繰り返しの一部を削除するには、以下の2通りの方法があります。  

#### 全項目を明示的に空でPOSTする

以下のように、グループ内のすべての項目を空値（`""` や `{}`）でPOSTすることで、グループの削除が可能です。  
項目名は省略せず、すべて含めてPOSTしてください。

```json
{
  "groups": [
    {
      "choice": {},
      "image": {},
      "text": ""
    },
    {
      "choice": {
        "key": "key2",
        "label": "value2"
      },
      "image": {
        "id": "2740_ext_07_0",
        "desc": "test image2"
      },
      "text": "text2"
    }
  ]
}
```

:::caution
グループに真偽値が含まれる場合、真偽値は`""`や`null`での更新を受け付けないため本方法は使用できません。
:::

#### 必要な繰り返し項目のみPOSTする

削除対象となるグループ（オブジェクト）を含めず、登録対象のグループのみをリクエストに含めるようにPOSTしてください。

```json
{
  "groups": [
    {
      "choice": {
        "key": "key2",
        "label": "value2"
      },
      "image": {
        "id": "2740_ext_07_0",
        "desc": "test image2"
      },
      "text": "text2"
    }
  ]
}
```

## 関連ドキュメント
- [コンテンツ定義](/ja/docs/management/content-structure-topics-group/)
- [コンテンツ定義で利用できる項目設定一覧](/ja/docs/reference/list-of-extra-column-available-on-content/)
- [APIを使ったファイルのアップロードについて](/ja/docs/reference/uploading-files-using-the-api/)
- [コンテンツ定義編集で項目設定をグループ化したのですが、APIから返却される json はグループ化されません。どうすればいいですか？](/ja/docs/faq/how-to-group-json-response-for-grouped-content-definition-items/)
- [コンテンツのbulk_upsert APIで画像・ファイル項目の更新はできますか？](/ja/docs/faq/can-i-update-topics-files-using-bulk_upsert-api/)


---

# フォーム定義で利用できるフォーム項目一覧

> 元ページ: `reference/form-field-list` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/form-field-list/

フォーム定義は、デフォルトで下記4つのフィールド項目を所有しています。

- name
- email
- カテゴリ
- message

![Image from Gyazo](https://t.gyazo.com/teams/diverta/94a42f04397d36191dfe66ced5fa4e31.jpg)

[フォーム項目設定](/ja/docs/management/form-field-settings/)で拡張項目を設定することで、フォームの所有する項目を追加できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fbe4457a79e955d09fe1fb9feb02f036.jpg)

また、各項目は[設定]をクリックして設定画面を開くと、入力制限や表示させる内容を設定できます。  
設定できる内容は項目により異なりますので下記参照ください。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/9fbafca3dd9958d581ac5d83b23ae23e.png)

## 共通設定
それぞれの項目は共通の設定が存在します。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/2f9b57eccf4b40f9da1410422dc240d5.png)

|項目 |説明 |
| :--- | :--- |
|任意/必須|任意/必須を選択できます。|
|選択項目の設定|項目設定を文字列で表現します。|
|設定|その項目の設定を変更できます。|
|注釈|注釈を記載します。|

「選択項目の設定」は、手動で入力する他に、項目の「設定」を変更した際に自動で入力される場合があります。  
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/b0e9331b8789ab6d9468070812df4652.gif)

## 拡張項目一覧
[改行なし短文（テキストボックス）](#改行なし短文テキストボックス)  
[改行ありの長文（テキストエリア）](#改行ありの長文テキストエリア)  
[単一選択(ラジオボタン)](#単一選択ラジオボタン)  
[単一選択(セレクトボックス)](#単一選択セレクトボックス)  
[複数選択(チェックボックス)](#複数選択チェックボックス)  
[日付フォーマット](#日付フォーマット)  
[真偽値](#真偽値)  
[ファイル(KurocoFiles)](#ファイルkurocofiles)  
[GCS上のファイル](#gcs上のファイル)  
[ファイル(S3)](#ファイルs3)  
[マトリクス](#マトリクス)  

## テキスト関連
### 改行なし短文（テキストボックス）
#### 項目設定
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/8c8a4c8a00ebc58d98e4de86fed49d85.png)

|項目 | |説明 |
| :--- | :--- | :--- |
|入力関連|入力制限|入力できる文字列を制限することができます。|
| |正規表現|入力制限で[正規表現]を選択した場合は正規表現を記入します。|
|文字数制限|min|最小文字数を入力します。|
| |max|最大の文字数を入力します。|
|Placeholder| |プレースホルダを入力します。|
|親項目||入力した内容がレスポンスに含まれるようになります。|

#### JSONレスポンス
下記画像の設定の場合におけるレスポンス例  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/7431c7fa4621279739e4a1623bbde877.png)

```json
"cols": {
    ...
    "ext_01": {
        "msg": "",
        "type": 1,
        "title": "text",
        "options": [],
        "order_no": 0,
        "required": 1,
        "validate": {
            "min_length": "10",
            "type": "regex",
            "regex": "^\\d+$",
            "max_length": "20",
            "parent_elm": "name",
            "placeholder": "数字"
        },
        "option_default": [],
        "option_group": [],
        "attribute": {
            "parent_elm": "name",
            "min_length": "10",
            "type": "regex",
            "regex": "^\\d+$",
            "max_length": "20",
            "placeholder": "数字",
            "limit_type": ""
        }
    },
    ...
}
```


### 改行ありの長文（テキストエリア）
#### 項目設定
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a8bcf1271e98d93d5185eff5c5ab372f.png)

|項目 | |説明 |
| :--- | :--- | :--- |
|文字数制限|min|最小文字数を入力します。|
| |max|最大の文字数を入力します。|
|親項目||入力した内容がレスポンスに含まれるようになります。|

#### JSONレスポンス
下記画像の設定の場合におけるレスポンス例  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/2175451f56c3cc789ef036458ae016ee.png)

```json
"cols": {
    ...
    "ext_02": {
        "msg": "",
        "type": 2,
        "title": "sentence",
        "options": [],
        "order_no": 0,
        "required": 1,
        "validate": {
            "type": "email",
            "placeholder": "メール",
            "parent_elm": "ext_01"
        },
        "option_default": [],
        "option_group": [],
        "attribute": {
            "parent_elm": "ext_01",
            "type": "email",
            "placeholder": "メール",
            "limit_type": "",
            "min_length": "",
            "max_length": ""
        }
    },
    ...
}
```

## セレクション関連
### 単一選択(ラジオボタン)
#### 項目設定
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/b0bd2d057ba2fa5ebecc2e2247026f39.png)

|項目 | |説明 |
| :--- | :--- | :--- |
|入力関連|親項目|入力した内容がレスポンスに含まれるようになります。|
||選択項目の表示をランダムにする|チェックを入れるとattribute内のrandomキーを`1`でレスポンスします。<br/>注：レスポンスデータの項目順は変更されません。並び順はrandomキー`1`を利用し、フロントエンドで変更をお願い致します。|
|選択項目|番号|選択項目のKeyを記入します。|
| |項目|選択項目のValueを記入します。|
| |group|グループ化したい場合に、グループのIDを記入します。|
| |初期値|デフォルト選択の指定を設定します。|
| |追加|選択項目を追加します。|
| |削除|選択項目を削除します。|

#### JSONレスポンス
下記画像の設定の場合におけるレスポンス例  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/ee8decbab061db7fdc29c7250108569c.png)

#### 「選択項目の設定」内容
```
1::value1::attribute::group::group1
2::value2::attribute::group::group1
3::default::value3::attribute::group::group3
```

```json
"cols": {
    ...
    "ext_03": {
        "msg": "",
        "type": 3,
        "title": "single radio",
        "options": {
            "1": "value1",
            "2": "value2",
            "3": "value3"
        },
        "order_no": 0,
        "required": 1,
        "validate": [],
        "option_default": [
            "3"
        ],
        "option_group": {
            "1": "group1",
            "2": "group1",
            "3": "group3"
        },
        "contents": [
            {
            "key": 1,
            "value": "value1",
            "default": false,
            "attribute": {
                "group": "group1"
            }
            },
            {
            "key": 2,
            "value": "value2",
            "default": false,
            "attribute": {
                "group": "group1"
            }
            },
            {
            "key": 3,
            "value": "value3",
            "default": true,
            "attribute": {
                "group": "group3"
            }
            }
        ],
        "attribute": {
            "parent_elm": ""
        }
    },
    ...
}
```

### 単一選択(セレクトボックス)
#### 項目設定
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/e5441972fda28600c24539c7ac80950c.png)

|項目 | |説明 |
| :--- | :--- | :--- |
|入力関連|親項目|入力した内容がレスポンスに含まれるようになります。|
||選択項目の表示をランダムにする|チェックを入れるとattribute内のrandomキーを`1`でレスポンスします。<br/>注：レスポンスデータの項目順は変更されません。並び順はrandomキー`1`を利用し、フロントエンドで変更をお願い致します。|
|選択項目|番号|選択項目のKeyを記入します。|
| |項目|選択項目のValueを記入します。|
| |group|グループ化したい場合に、グループのIDを記入します。|
| |初期値|デフォルト選択の指定を設定します。|
| |追加|選択項目を追加します。|
| |削除|選択項目を削除します。|

#### JSONレスポンス
下記画像の設定の場合におけるレスポンス例  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/1b3f138874d0c59295f1e7c82b6f984d.png)

#### 「選択項目の設定」内容
```
1::default::value1
2::value2
```

```json
"cols": {
    ...
    "ext_04": {
        "msg": "",
        "type": 4,
        "title": "single selectbox",
        "options": {
            "1": "value1",
            "2": "value2"
        },
        "order_no": 0,
        "required": 1,
        "validate": {
            "random": "1"
        },
        "option_default": [
            "1"
        ],
        "option_group": [],
        "contents": [
            {
            "key": 1,
            "value": "value1",
            "default": true,
            "attribute": {}
            },
            {
            "key": 2,
            "value": "value2",
            "default": false,
            "attribute": {}
            }
        ],
        "attribute": {
            "parent_elm": "",
            "random": "1"
        }
    },
    ...
}
```

### 複数選択(チェックボックス)
#### 項目設定
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/3ce37f6213bb0c956e317a8f4fab9c90.png)

|項目 | |説明 |
| :--- | :--- | :--- |
|入力関連|親項目|入力した内容がレスポンスに含まれるようになります。|
||選択項目の表示をランダムにする|チェックを入れるとattribute内のrandomキーを`1`でレスポンスします。<br/>注：レスポンスデータの項目順は変更されません。並び順はrandomキー`1`を利用し、フロントエンドで変更をお願い致します。|
|選択項目|番号|選択項目のKeyを記入します。|
| |項目|選択項目のValueを記入します。|
| |group|グループ化したい場合に、グループのIDを記入します。|
| |初期値|デフォルト選択の指定を設定します。|
| |追加|選択項目を追加します。|
| |削除|選択項目を削除します。|

#### JSONレスポンス
下記画像の設定の場合におけるレスポンス例  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/385d6869b13f88ba53b567498a389141.png)

#### 「選択項目の設定」内容
```
1::default::value1
2::value2
```

```json
"cols": {
    ...
    "ext_05": {
        "msg": "",
        "type": 5,
        "title": "multiple checkbox",
        "options": {
            "1": "value1",
            "2": "value2"
        },
        "order_no": 0,
        "required": 1,
        "validate": [],
        "option_default": [
            "1"
        ],
        "option_group": [],
        "contents": [
            {
            "key": 1,
            "value": "value1",
            "default": true,
            "attribute": {}
            },
            {
            "key": 2,
            "value": "value2",
            "default": false,
            "attribute": {}
            }
        ],
        "attribute": {
            "parent_elm": ""
        }
    },
    ...
}
```

### 日付フォーマット
#### 項目設定
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/ce0628d43b0bcd7e492549d453ca3fbe.png)

|項目 | |説明 |
| :--- | :--- | :--- |
|入力関連|親項目|入力した内容がレスポンスに含まれるようになります。|
|選択項目の設定|時間も設定する|チェックを入れると時間の設定ができるようになります。|
| |年(下限)|項目の最低年を入力します。|
| |年(上限)|項目の最高年を入力します。|
| |昇順(年)|年を昇順で並び替えます。|
|入力関連|期間制限の基準日|期間を制限したい場合の、基準となる日を入力します。(※)|
| |開始までの期間|期間を制限したい場合の、開始までの期間を入力します。(※)|
| |終了までの期間|期間を制限したい場合の、終了までの期間を入力します。(※)|

(※) [PHPのstrtotime()の形式](https://www.php.net/manual/en/function.strtotime.php#refsect1-function.strtotime-examples)で指定します。

#### JSONレスポンス
下記画像の設定の場合におけるレスポンス例  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d65fe3e1271b160475ac7bc75d3e6af2.png)

#### 「選択項目の設定」内容
```
add_time::1
minYear::2022
maxYear::2020
originStrDate::2021-10-10
minPeriod::+30 day
maxPeriod::-1 week 2 days 4 hours 2 seconds
```

```json
"cols": {
    ...
    "ext_06": {
        "msg": "",
        "type": 6,
        "title": "date",
        "options": {
            "add_time": "1",
            "minYear": "2022",
            "maxYear": "2020",
            "originStrDate": "2021-10-10",
            "minPeriod": "+30 day",
            "maxPeriod": "-1 week 2 days 4 hours 2 seconds",
            "arrYear": {
            "2020": 2020,
            "2021": 2021,
            "2022": 2022
            }
        },
        "order_no": 0,
        "required": 1,
        "validate": [],
        "option_default": [],
        "option_group": [],
        "attribute": {
            "parent_elm": "",
            "add_time": "1",
            "minYear": "2022",
            "maxYear": "2020",
            "originStrDate": "2021-10-10",
            "minPeriod": "+30 day",
            "maxPeriod": "-1 week 2 days 4 hours 2 seconds",
            "arrYear": {
            "2020": 2020,
            "2021": 2021,
            "2022": 2022
            }
        }
    },
    ...
}
```

### 真偽値
#### 項目設定
![Image from Gyazo](https://t.gyazo.com/teams/diverta/89c63a3cb95743eae713fd959edaafce.png)

|項目 |説明 |
| :--- | :--- |
|デフォルト|チェックを入れるとoptions項目に`{"key": "default","value": "****"}`のレスポンスが追加されます。|

#### JSONレスポンス
下記画像の設定の場合におけるレスポンス例  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6a4724e8169e03a70925abba4b2fa2f1.png)

#### 「選択項目の設定」内容
```
default::true
```

```json
"cols": {
    ...
    "ext_09": {
        "key": "ext_09",
        "msg": "",
        "type": 13,
        "title": "Bool",
        "options": [
          {
            "key": "default",
            "value": "true"
          }
        ],
        "order_no": 0,
        "required": 1,
        "validate": [],
        "option_default": [],
        "option_group": [],
        "attribute": {
          "parent_elm": ""
        }
    },
    ...
}
```

## ファイル関連
### ファイル(KurocoFiles)
#### 項目設定
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/f67db25c2634667d0f1b377a8ef1aa78.png)

|項目 | |説明 |
| :--- | :--- | :--- |
|入力関連|親項目|入力した内容がレスポンスに含まれるようになります。|
|選択項目の設定|拡張子|アップロードを許可するファイルの拡張子を指定します。<br/>指定が無い場合は次の拡張子が許可されます。`jpg`,`jpeg`,`gif`,`png`,`pdf`|
| |追加|アップロードを許可するファイルの拡張子を追加します。|
| |削除|アップロードを許可するファイルの拡張子を削除します。|

#### JSONレスポンス
下記画像の設定の場合におけるレスポンス例  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d114006b38824428e46c478c864561f6.png)

#### 「選択項目の設定」内容
```
png
jpg
```

```json
"cols": {
    ...
    "ext_07": {
        "msg": "",
        "type": 7,
        "title": "file",
        "options": [
            "png\r",
            "jpg"
        ],
        "order_no": 0,
        "required": 1,
        "validate": [],
        "option_default": [],
        "option_group": [],
        "extensions": [
            "png\r",
            "jpg"
        ],
        "attribute": {
            "parent_elm": ""
        }
    },
    ...
}
```

### GCS上のファイル
GCS上のファイルははFirebaseとの連携後に利用可能です。

#### 項目設定
![Image from Gyazo](https://t.gyazo.com/teams/diverta/fc89651d750e2c97b1abdc79e34f4466.png)

|項目 | |説明 |
| :--- | :--- | :--- |
|入力関連|親項目|入力した内容がレスポンスに含まれるようになります。|
|選択項目の設定|拡張子|アップロードを許可するファイルの拡張子を指定します。<br/>指定が無い場合は次の拡張子が許可されます。`jpg`,`jpeg`,`gif`,`png`,`pdf`|
| |追加|アップロードを許可するファイルの拡張子を追加します。|
| |削除|アップロードを許可するファイルの拡張子を削除します。|

#### JSONレスポンス
下記画像の設定の場合におけるレスポンス例  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/125a6e6b961b2a7df6cb77a7a9d38fe5.png)

#### 「拡張子の設定」内容
```
png
jpg
```

```json
"cols": {
    ...
    "ext_04": {
        "msg": "",
        "type": 11,
        "title": "file_gcs",
        "options": [
          "png",
          "jpg"
        ],
        "order_no": 0,
        "required": 1,
        "validate": [],
        "option_default": [],
        "option_group": [],
        "extensions": [
          "png",
          "jpg"
        ],
        "attribute": {
          "parent_elm": ""
        }
    },
    ...
}
```

### ファイル(S3)
ファイル(S3)はAmazon S3との連携後に利用可能です。

#### 項目設定
![Image from Gyazo](https://t.gyazo.com/teams/diverta/30ae1260efeee5b7d3c23cf7d358be37.png)

|項目 | |説明 |
| :--- | :--- | :--- |
|入力関連|親項目|入力した内容がレスポンスに含まれるようになります。|
|選択項目の設定|拡張子|アップロードを許可するファイルの拡張子を指定します。<br/>指定が無い場合は次の拡張子が許可されます。`jpg`,`jpeg`,`gif`,`png`,`pdf`|
| |追加|アップロードを許可するファイルの拡張子を追加します。|
| |削除|アップロードを許可するファイルの拡張子を削除します。|

#### JSONレスポンス
下記画像の設定の場合におけるレスポンス例  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f86811ba624012071e5708dc9f331fe9.png)


#### 「拡張子の設定」内容
```
png
jpg
```

```json
"cols": {
    ...
    "ext_04": {
        "msg": "",
        "type": 12,
        "title": "file_s3",
        "options": [
          "png",
          "jpg"
        ],
        "order_no": 0,
        "required": 1,
        "validate": [],
        "option_default": [],
        "option_group": [],
        "extensions": [
          "png",
          "jpg"
        ],
        "attribute": {
          "parent_elm": ""
        }
    },
    ...
}
```

## その他

### マトリクス
#### 項目設定
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/c6e6c1c8adc7f01ddd2187fa52282602.png)

|項目 | |説明 |
| :--- | :--- | :--- |
|入力関連|タイプ|単一選択/複数選択を指定します。|
||親項目|入力した内容がレスポンスに含まれるようになります。|
| |選択項目の表示をランダムにする|チェックを入れるとattribute内のrandomキーを`1`でレスポンスします。<br/>注：レスポンスデータの項目順は変更されません。並び順はrandomキー`1`を利用し、フロントエンドで変更をお願い致します。|
|選択項目-列|番号|列のKeyを記入します。|
| |項目|列のValueを記入します。|
| |追加|列を追加します。|
| |削除|列を削除します。|
|選択項目-行|番号|行のKeyを記入します。|
| |項目|行のValueを記入します。|
| |追加|行を追加します。|
| |削除|行を削除します。|

#### JSONレスポンス
下記画像の設定の場合におけるレスポンス例  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/e74805c00e95438137c01ba7a0a660b5.png)

#### 「選択項目の設定」内容
```
COL::1::column1
COL::2::column2
ROW::1::row1
ROW::2::row2
```

```json
"cols": {
    ...
    "ext_09": {
        "msg": "",
        "type": 10,
        "title": "matrix",
        "options": {
            "COL": {
            "1": "column1",
            "2": "column2"
            },
            "ROW": {
            "1": "row1",
            "2": "row2"
            }
        },
        "order_no": 0,
        "required": 1,
        "validate": {
            "selection_type": "multiple",
            "random": "1"
        },
        "option_default": [],
        "option_group": [],
        "contents": [
            {
            "key": 1,
            "value": "row1",
            "attribute": {
                "matrix_type": "ROW"
            }
            },
            {
            "key": 2,
            "value": "row2",
            "attribute": {
                "matrix_type": "ROW"
            }
            },
            {
            "key": 1,
            "value": "column1",
            "attribute": {
                "matrix_type": "COL"
            }
            },
            {
            "key": 2,
            "value": "column2",
            "attribute": {
                "matrix_type": "COL"
            }
            }
        ],
        "attribute": {
            "parent_elm": "",
            "selection_type": "multiple",
            "random": "1"
        }
    },
    ...
}
```

## 関連ドキュメント
- [フォーム項目設定](/ja/docs/management/form-field-settings/)
- [フォーム基本設定](/ja/docs/management/inquiry-basic-settings/)
- [フォーム画面を構築する](/ja/docs/tutorials/setting-up-inquiry-forms/)
- [フォームの項目に初期値やプレースホルダーを設定できますか？](/ja/docs/faq/can-i-set-initial-value-or-placeholder-fof-form-items/)
- [フォーム項目設定の並び順がAPIに反映しません](/ja/docs/faq/the-ordering-of-form-fields-is-not-reflected-in-the-api/)


---

# Kurocoで利用される共通Object型定義

> 元ページ: `reference/general-object-type` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/general-object-type/

カスタム処理、バッチテンプレート、メールテンプレートなどで利用出来るSmarty変数の中で  
共通の型定義を持つObjectの一覧を記載します。

## ext_config オブジェクト型
コンテンツ定義の設定です。

### よく利用する項目の説明
| 変数名 | 型 | 説明 |
| :--- | :--- | :--- |
| no | String |拡張番号 |
| ext_col_nm | String | 拡張キー名 |
| ext_index | Int | 拡張番号の数値 |
| title<br/>ext_title| String | 項目名 |
| type | String | 拡張種別（0: テキスト、2: 単一選択などの選択形式） |
| options | Object | 拡張項目の設定<br/>「単一選択」、「複数選択可」、「マスタ形式」の場合は選択肢の一覧となります |
| limits |  Object |入力制限<br/>必須項目の場合は`"required":"1"` |
| ext_group_loop | Int | 繰り返し回数 |
| ext_slug | String | 識別子 |
| ext_help_msg | String | 注釈 |

### サンプル
```json
[
    {
        "no":"01",
        "ext_col_nm":"ext_1",
        "ext_index":1,
        "title":"text input",
        "type":"0",
        "options":[],
        "limits":{
            "required":"1"
        },
        "ext_title":"text input",
        "ext_type":"0",
        "ext_option":"",
        "ext_group_id":null,
        "ext_group_parent_ext_col":"",
        "ext_group_loop":1,
        "ext_order_no":0,
        "ext_limit_item":"required=1",
        "ext_parent_col_nm":"",
        "topics_group_ext_id":138,
        "ext_slug":"text_col",
        "ext_help_msg":"",
        "ext_template":"",
        "separator":null,
        "ext_option_parent_id":null,
        "default_selection":"",
        "default_value":""
    },
    {
        "no":"02",
        "ext_col_nm":"ext_2",
        "ext_index":2,
        "title":"select input",
        "type":"2",
        "options":{
            "1":"value1",
            "2":"value2"
        },
        "limits":[],
        "ext_title":"select input",
        "ext_type":"2",
        "ext_option":"1::value1\\r\\n2::value2",
        "ext_group_id":null,
        "ext_group_parent_ext_col":"",
        "ext_group_loop":1,
        "ext_order_no":0,
        "ext_limit_item":"",
        "ext_parent_col_nm":"",
        "topics_group_ext_id":139,
        "ext_slug":"select_col",
        "ext_help_msg":"",
        "ext_template":"",
        "separator":null,
        "ext_option_parent_id":null,
        "default_selection":"",
        "default_value":""
    }
]
```

## 関連ドキュメント
- [カスタム処理](/ja/docs/management/function/)
- [バッチテンプレート](/ja/docs/management/batch-template/)
- [カスタム処理に利用できるトリガと変数の一覧](/ja/docs/reference/trigger-variables/)
- [KurocoのSmarty基本構文](/ja/docs/reference/basic-syntax-kuroco-smarty/)
- [メッセージひな形に利用できる変数一覧](/ja/docs/reference/mail-variables/)


---

# JSON Schemaパターンサンプル

> 元ページ: `reference/json-column-schema` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/json-column-schema/
> 概要: Kurocoのコンテンツ定義では、JSON型の拡張項目を使って柔軟なフォームUIを構築できます。このページでは、実際に使えるJSON Schemaのパターンを紹介します。

## JSON拡張項目の設定方法

Kurocoのコンテンツ定義では、JSON型の拡張項目を使って柔軟なフォームUIを構築できます。
このページでは、実際に使えるJSON Schemaのパターンを紹介します。

:::info
Kurocoで使用するJSONスキーマの構文は、https://json-schema.org/understanding-json-schema/basics がベースです。
基本的な構文については`JSON Schema`のドキュメントを参照してください。
:::

## 基本的なフィールドタイプ

### セレクトボックス(文字列の選択)

```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "title": "ステータス",
      "description": "コンテンツの公開状態を選択してください",
      "enum": ["draft", "published", "archived"],
      "default": "draft"
    }
  }
}
```

**表示**: セレクトボックス
![Image from Gyazo](https://t.gyazo.com/teams/diverta/97c61c1713e36382ea546acdfe6a4c8e.png)

**注意**: `default`が設定されている場合はその値が初期選択されます。

---

### セレクトボックス(表示ラベルのカスタマイズ)

```json
{
  "type": "object",
  "properties": {
    "priority": {
      "type": "string",
      "title": "優先度",
      "enum": ["low", "medium", "high", "urgent"],
      "enumNames": ["低", "中", "高", "緊急"],
      "default": "medium"
    }
  }
}
```

**表示**: セレクトボックス(日本語ラベル)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5a27ef67fa57fc8f5bc9f5b3144eb083.png)

**注意**: `enumNames`を使用することで、内部的な値(`low`など)とは異なる表示ラベル(`低`など)を設定できます。

---

### セレクトボックス(数値の選択)

```json
{
  "type": "object",
  "properties": {
    "rating": {
      "type": "integer",
      "title": "評価",
      "enum": [1, 2, 3, 4, 5],
      "enumNames": ["★", "★★", "★★★", "★★★★", "★★★★★"]
    }
  }
}
```

**表示**: セレクトボックス(数値)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/20c91a1bc9f2b32c70cc4ec216e5dc09.png)

**注意**: Number/Integer型のenumの場合、`default`未設定時は最初の値が自動選択されます。

---

### 複数選択セレクトボックス

```json
{
  "type": "object",
  "properties": {
    "tags": {
      "type": "array",
      "title": "タグ",
      "description": "複数選択可能です(Ctrl/Cmd + クリック)",
      "items": {
        "type": "string",
        "enum": ["技術", "ビジネス", "デザイン", "マーケティング", "その他"]
      }
    }
  }
}
```

**表示**: 複数選択セレクトボックス
![Image from Gyazo](https://t.gyazo.com/teams/diverta/68288d57fbf109423a6ca28f04a08354.png)

---

## 実用的な入力フォーム

### ファイルマネージャー(画像・ファイル選択)

```json
{
  "type": "object",
  "title": "メディア設定",
  "properties": {
    "thumbnailImage": {
      "type": "string",
      "title": "サムネイル画像",
      "description": "一覧表示用のサムネイル画像を選択してください",
      "format": "file-manager"
    },
    "headerImage": {
      "type": "string",
      "title": "ヘッダー画像",
      "description": "ページ上部に表示する画像",
      "format": "file-manager"
    },
    "pdfDocument": {
      "type": "string",
      "title": "PDFドキュメント",
      "description": "ダウンロード用PDFファイル",
      "format": "file-manager"
    },
    "videoFile": {
      "type": "string",
      "title": "動画ファイル",
      "format": "file-manager"
    }
  }
}
```

**表示**:
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5ed04369d51e03be185f4928e692d767.png)

**特徴**:
- CKFinderとの完全統合
- ファイルパスを文字列として保存
- ファイル選択後にプレビューリンク表示

---

### WYSIWYGエディタ(HTMLエディタ)

```json
{
  "type": "object",
  "title": "記事コンテンツ",
  "properties": {
    "title": {
      "type": "string",
      "title": "タイトル",
      "minLength": 1,
      "maxLength": 100
    },
    "summary": {
      "type": "string",
      "title": "要約",
      "description": "記事の簡単な説明(プレーンテキスト)",
      "format": "textarea",
      "rows": 3
    },
    "content": {
      "type": "string",
      "title": "本文",
      "description": "記事の本文をHTML形式で入力してください",
      "format": "html"
    },
    "sidebarContent": {
      "type": "string",
      "title": "サイドバーコンテンツ",
      "description": "サイドバーに表示する内容",
      "format": "html",
      "format_options": { "height": "300px" }
    }
  }
}
```

**表示**:
![Image from Gyazo](https://t.gyazo.com/teams/diverta/bfc0321c949722ac382fdc0dc232c5c2.png)

**特徴**:
- `format: "html"` でCKEditorを自動表示
- `format_options` でエディタのオプションを指定
- CKFinderとの完全統合(画像アップロード・管理)

---

### 日付・日時の入力

```json
{
  "type": "object",
  "title": "日付・日時設定",
  "properties": {
    "publishDate": {
      "type": "string",
      "title": "公開日",
      "description": "記事を公開する日付を選択してください",
      "format": "date",
      "nullable": false
    },
    "publishDateTime": {
      "type": "string",
      "title": "公開日時",
      "description": "記事を公開する日時を選択してください",
      "format": "date-time",
      "minuteInterval": 15,
      "nullable": false
    },
    "eventStartDate": {
      "type": ["string", "null"],
      "title": "イベント開始日(必須)",
      "description": "イベントの開始日を選択してください",
      "format": "date"
    },
    "eventEndDateTime": {
      "type": ["string", "null"],
      "title": "イベント終了日時(任意)",
      "description": "イベントの終了日時を選択してください",
      "format": "date-time"
    }
  }
}
```

**表示例**:
![Image from Gyazo](https://t.gyazo.com/teams/diverta/bb4ebac3e2685440a7454edbca4c6f89.png)

**特徴**:
- `format: "date"`: 日付のみ(年月日)を入力
- `format: "date-time"`: 日付と時刻(年月日 時分秒)を入力
- `nullable: false`: 必須項目の表示を設定可能
- `minuteInterval`: 分の選択肢の間隔を設定（設定可能な値: 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30）
- DatePickerコンポーネントで直感的に選択

---

## 応用的な設定例

### 繰り返し項目(配列フォーム)

```json
{
  "type": "object",
  "properties": {
    "news": {
      "type": "array",
      "title": "ニュース一覧",
      "description": "最新のニュースを最大10件まで登録できます",
      "minItems": 1,
      "maxItems": 10,
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "title": "タイトル",
            "description": "ニュースのタイトルを入力してください",
            "maxLength": 100
          },
          "link": {
            "type": "string",
            "title": "リンク",
            "description": "ニュース記事のURLを入力してください"
          },
          "publishDate": {
            "type": ["string", "null"],
            "title": "公開日",
            "format": "date"
          },
          "category": {
            "type": "string",
            "title": "カテゴリー",
            "enum": ["press", "blog", "event", "update"],
            "enumNames": ["プレスリリース", "ブログ", "イベント", "アップデート"]
          }
        },
        "required": ["title", "link"]
      }
    }
  }
}
```

**表示**: 繰り返し可能なカードUI
![Image from Gyazo](https://t.gyazo.com/teams/diverta/50336412cde1af120e01b402a5e26aa9.png)

**特徴**:
- 各アイテムがカード形式で表示
- ↑↓ボタンで順番を入れ替え可能
- 各カードの下に「追加」ボタンを配置
- `minItems`: 最低限必要なアイテム数(削除時に制限、アラート表示)
- `maxItems`: 最大登録可能数(追加時に制限、アラート表示)
- JSON プレビューボタンで確認可能(モーダル表示、読み取り専用)
- descriptionは各フィールドの下部に小さな文字で表示

---

### ブログ記事の設定フォーム例

```json
{
  "type": "object",
  "title": "ブログ記事設定",
  "properties": {
    "title": {
      "type": "string",
      "title": "記事タイトル",
      "minLength": 1,
      "maxLength": 100
    },
    "category": {
      "type": "string",
      "title": "カテゴリー",
      "enum": ["news", "tutorial", "blog", "announcement"],
      "enumNames": ["ニュース", "チュートリアル", "ブログ", "お知らせ"]
    },
    "status": {
      "type": "string",
      "title": "公開状態",
      "enum": ["draft", "review", "published", "archived"],
      "enumNames": ["下書き", "レビュー待ち", "公開済み", "アーカイブ"],
      "default": "draft"
    },
    "featured": {
      "type": "boolean",
      "title": "注目記事"
    },
    "tags": {
      "type": "array",
      "title": "タグ",
      "items": {
        "type": "string",
        "enum": ["Vue.js", "React", "Angular", "JavaScript", "TypeScript", "CSS", "HTML"]
      }
    },
    "visibility": {
      "type": "string",
      "title": "閲覧権限",
      "enum": ["public", "members", "premium", "private"],
      "enumNames": ["公開", "会員限定", "プレミアム会員限定", "非公開"],
      "default": "public"
    },
    "publishDate": {
      "type": ["string", "null"],
      "title": "公開日",
      "description": "記事を公開する日付を選択してください",
      "format": "date"
    },
    "publishDateTime": {
      "type": ["string", "null"],
      "title": "公開日時",
      "description": "記事を公開する日時を選択してください",
      "format": "date-time"
    }
  },
  "required": ["title", "category", "status"]
}
```

**表示例**:
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c0d3b12391dea5d185523505db0c09ed.jpg)

---

### ECサイト商品設定例

```json
{
  "type": "object",
  "title": "商品設定",
  "properties": {
    "productName": {
      "type": "string",
      "title": "商品名",
      "minLength": 1
    },
    "size": {
      "type": "string",
      "title": "サイズ",
      "enum": ["XS", "S", "M", "L", "XL", "XXL"]
    },
    "color": {
      "type": "string",
      "title": "カラー",
      "enum": ["red", "blue", "green", "black", "white", "yellow"],
      "enumNames": ["レッド", "ブルー", "グリーン", "ブラック", "ホワイト", "イエロー"]
    },
    "availability": {
      "type": "string",
      "title": "在庫状況",
      "enum": ["in_stock", "low_stock", "out_of_stock", "pre_order"],
      "enumNames": ["在庫あり", "残りわずか", "在庫切れ", "予約受付中"],
      "default": "in_stock"
    },
    "shippingOptions": {
      "type": "array",
      "title": "配送方法",
      "items": {
        "type": "string",
        "enum": ["standard", "express", "overnight", "pickup"],
        "enumNames": ["通常配送", "速達", "翌日配送", "店舗受取"]
      }
    },
    "price": {
      "type": "number",
      "title": "価格",
      "minimum": 0
    },
    "onSale": {
      "type": "boolean",
      "title": "セール対象"
    }
  },
  "required": ["productName", "price", "availability"]
}
```

**表示例**:
![Image from Gyazo](https://t.gyazo.com/teams/diverta/be0b2e13412b6b80dbd110ea1ba3d399.png)

---

### より複雑な配列例(商品バリエーション with WYSIWYG)

```json
{
  "type": "object",
  "properties": {
    "productVariants": {
      "type": "array",
      "title": "商品バリエーション",
      "description": "サイズ・カラー別の商品情報を登録",
      "minItems": 1,
      "items": {
        "type": "object",
        "properties": {
          "sku": {
            "type": "string",
            "title": "SKU",
            "description": "商品コード"
          },
          "size": {
            "type": "string",
            "title": "サイズ",
            "enum": ["XS", "S", "M", "L", "XL", "XXL"]
          },
          "color": {
            "type": "string",
            "title": "カラー",
            "enum": ["red", "blue", "green", "black", "white"],
            "enumNames": ["レッド", "ブルー", "グリーン", "ブラック", "ホワイト"]
          },
          "description": {
            "type": "string",
            "title": "商品説明",
            "description": "このバリエーションの詳細説明",
            "format": "html",
            "format_options": { "height": "300px" }
          },
          "stock": {
            "type": "integer",
            "title": "在庫数",
            "minimum": 0,
            "default": 0
          },
          "price": {
            "type": "number",
            "title": "価格",
            "minimum": 0
          },
          "image": {
            "type": "string",
            "title": "商品画像",
            "format": "file-manager"
          },
          "available": {
            "type": "boolean",
            "title": "販売中",
            "default": true
          }
        },
        "required": ["sku", "size", "color", "price"]
      }
    }
  }
}
```

**表示例**:
![Image from Gyazo](https://t.gyazo.com/teams/diverta/26bb96f163b26aaf7198730ce22e36ce.jpg)

**特徴**:
- 配列オブジェクト内で`format: "html"`を使用してWYSIWYGエディタを配置可能
- 各アイテムごとに独立したCKEditorインスタンスが生成される
- ファイルマネージャーとWYSIWYGを同時に使用可能
- `format_options`でエディタの高さを個別に調整可能

## 設定リファレンス

### 表示モード
- `JSONデータ定義からUIを構成する`が有効 → JSON Schemaに基づいた**フォームUI**を表示
- `JSONデータ定義からUIを構成する`が無効 → **JSONエディタ**のみ表示

### フィールドタイプの自動判定
- `string` - テキスト入力
- `string` + `enum` - セレクトボックス
- `string` + `format: "date"` - DatePicker(日付のみ)
- `string` + `format: "date-time"` - DatePicker(日時)
- `string` + `format: "file-manager"` - ファイルマネージャー(CKFinder統合)
- `string` + `format: "html"` - WYSIWYGエディタ(CKEditor)
- `string` + `format: "textarea"` - テキストエリア
- `number` / `integer` - 数値入力
- `number` / `integer` + `enum` - 数値セレクトボックス
- `boolean` - チェックボックス
- `array` + `items.type: "string"` - カンマ区切りテキストエリア
- `array` + `items.enum` - 複数選択セレクトボックス
- `array` + `items.type: "object"` - 繰り返しカードUI
- `object` - JSON形式テキストエリア

### WYSIWYGエディタオプション (format_options)

`format: "html"`を使用する場合、`format_options`でCKEditorの動作をカスタマイズできます。以下のオプションが利用可能です：

| オプション | 説明 | 例 |
|-----------|------|-----|
| `height` | エディタの高さ | `"height": "300px"` |
| `width` | エディタの幅 | `"width": "800px"` |
| `toolbar` | ツールバーのプリセット。`"basic"`を指定すると簡易ツールバー（太字、斜体、リスト、リンクのみ）になります | `"toolbar": "basic"` |
| `use_markdown` | `"1"`を指定するとMarkdownモードになります | `"use_markdown": "1"` |
| `subscript` | 下付き・上付き文字ボタンを追加 | `"subscript": true` |
| `strikethrough` | 取り消し線ボタンをツールバーに追加 | `"strikethrough": true` |
| `removePlugins` | 削除するプラグイン（カンマ区切り） | `"removePlugins": "insertImage,mediaEmbed"` |
| `use_font_size_px` | フォントサイズをピクセル単位で選択可能にする | `"use_font_size_px": true` |
| `largeColorPalette` | `"true"`を指定すると拡張カラーパレットを使用 | `"largeColorPalette": "true"` |
| `customColors` | カスタムカラー（カンマ区切りの16進数値） | `"customColors": "#ff0000,#00ff00,#0000ff"` |
| `use_magicline` | MagicLine機能を有効化（要素間に挿入ポイントを表示） | `"use_magicline": true` |
| `custom_css` | カスタムCSSファイルのパス | `"custom_css": "/path/to/custom.css"` |
| `resource` | ファイルアップロード先のリソースパス | `"resource": "/files/user/"` |

#### 例: カスタムオプション付きWYSIWYG

```json
{
  "type": "object",
  "properties": {
    "content": {
      "type": "string",
      "title": "記事本文",
      "format": "html",
      "format_options": {
        "height": 400,
        "customColors": "#2c7be5,#00d97e,#e63757",
        "use_magicline": true
      }
    },
    "sidebar": {
      "type": "string",
      "title": "サイドバーコンテンツ",
      "description": "サイドバー用の簡易エディタ",
      "format": "html",
      "format_options": {
        "height": 200,
        "toolbar": "basic"
      }
    }
  }
}
```

---

### デフォルト値の決定
1. `default`が設定されている → その値を使用
2. `default`が未設定の場合:
   - `enum`に`null`が含まれる → `null`を初期値とする
   - `enum`に`null`が含まれない → `enum[0]`(最初の値)を初期値とする

### バリデーション
- `required` - 必須項目(Array/Objectタイプ用)
- `nullable` - null許可(false時に必須マーク表示、Enum/Date/Number/Integer用)
- `minLength` / `maxLength` - 文字数制限(String用、minLength: 1で必須マーク表示)
- `minimum` / `maximum` - 数値範囲
- `minItems` / `maxItems` - 配列要素数制限
- `pattern` - 正規表現パターン

### 必須項目の設定方法

フィールドを必須項目にする方法は、フィールドタイプによって異なります。

#### Enum、Date、Date-time、Number、Integerの場合
```json
{
  "type": "string",  // または "integer", "number"、nullを許可しない
  "format": "date",  // または "enum": ["1", "2"],
  "nullable": false  // ← これがfalseの場合に必須マーク表示
}
```

**ルール**: `nullable: false` を設定すると必須マーク(*)が表示されます。typeでnullを許可しないことで入力必須にします。

#### String(テキスト入力)の場合
```json
{
  "type": "string",
  "minLength": 1  // ← これが1以上の場合に必須マーク表示
}
```

**ルール**: `minLength: 1` 以上を設定すると必須項目になり、必須マーク(*)が表示されます。

#### Array(配列)、Object(オブジェクト)の場合
```json
{
  "type": "object",
  "properties": {
    "tags": {
      "type": "array",
      "minItems": 1,  // ← 1つ以上選択必須
      "items": {
        "type": "string",
        "enum": ["1", "2", "3"]
      }
    }
  },
  "required": ["tags"]  // ← required配列に含まれる場合に必須マーク表示
}
```

**ルール**: スキーマのトップレベルにある`required`配列にフィールド名を含めると必須表示になります。

#### 実践例: 複数タイプの必須項目を含むスキーマ

```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",  // ← "null"を許可しない
      "enum": [null, "draft", "published"],
      "nullable": false  // ← 必須マーク表示
    },
    "name": {
      "type": "string",
      "minLength": 1  // ← 必須マーク表示
    },
    "publishDate": {
      "type": "string",  // ← "null"を許可しない
      "format": "date",
      "nullable": false  // ← 必須マーク表示
    },
    "tags": {
      "type": "array",
      "minItems": 1,  // ← 1つ以上選択必須
      "items": {
        "type": "string",
        "enum": ["1", "2", "3"]
      }
    }
  },
  "required": ["tags"]  // ← Array/Object以外は各プロパティの設定で必須判定される
}
```

### 配列オブジェクトUIの動作
- アイテム追加時に `maxItems` チェック(上限に達している場合はアラート表示)
- アイテム削除時に `minItems` チェック(最小数を下回る場合はアラート表示)
- 各カード下部に「追加」ボタンを配置
- アイテムがゼロの場合は最初の「追加」ボタンのみ表示

### その他の機能
- `enumNames`で表示ラベルをカスタマイズ可能
- `type: ["string", "null"]`のようなUnion Type(nullable)に対応
- `description`はフィールド下部にヘルプテキストとして表示
- JSON プレビューボタンで現在の値を確認可能(モーダル表示)

### ネスト構造の対応状況と制限

#### サポートされているネスト構造

システムは以下のネスト構造に対応しています：

##### Object (単一オブジェクト)
```json
{
  "type": "object",
  "properties": {
    "name": {"type": "string"},
    "email": {"type": "string"}
  }
}
```

##### Array → Object (オブジェクトの配列)
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "title": {"type": "string"},
      "link": {"type": "string"}
    }
  }
}
```

##### Object → Array → Object (オブジェクト内の配列内のオブジェクト)
```json
{
  "type": "object",
  "properties": {
    "news": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "title": {"type": "string"},
          "category": {"type": "string", "enum": ["blog", "news"]}
        }
      }
    }
  }
}
```

##### Array → Object → Array → Object (オブジェクトの配列の中にオブジェクトの配列)
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "label": {"type": "string", "title": "ラベル"},
      "title": {"type": "string", "title": "タイトル"},
      "text": {"type": "string", "title": "テキスト"},
      "images": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "image": {"type": "string", "format": "file-manager"},
            "alt": {"type": "string", "title": "代替テキスト"}
          },
          "required": ["image"]
        }
      }
    }
  }
}
```

**解説**: これらのパターンは完全にサポートされており、UIで直接編集可能です。

---

#### 制限事項: 5階層以上のネスト

**5階層以上のネスト構造は、現在UIでの直接編集に対応していません。**

##### 推奨される回避策: 構造を分割する

深いネスト構造が必要な場合は、**複数の拡張項目に分割**することで対応できます。

##### 解決例: 2つの拡張項目に分割

###### 拡張項目1: `departments_data` (部署と社員情報)
```json
{
  "type": "object",
  "properties": {
    "departmentId": {
      "type": "string",
      "title": "部署ID",
      "description": "一意の部署識別子"
    },
    "departmentName": {
      "type": "string",
      "title": "部署名"
    },
    "employees": {
      "type": "array",
      "title": "社員一覧",
      "items": {
        "type": "object",
        "properties": {
          "employeeId": {
            "type": "string",
            "title": "社員ID"
          },
          "employeeName": {
            "type": "string",
            "title": "社員名"
          },
          "position": {
            "type": "string",
            "title": "役職",
            "enum": ["manager","staff","intern"],
            "enumNames": ["マネージャー","スタッフ","インターン"
            ]
          }
        }
      }
    }
  }
}
```

###### 拡張項目2: `employee_skills_data` (社員のスキル情報)
```json
{
  "type": "object",
  "properties": {
    "employeeId": {
      "type": "string",
      "title": "社員ID",
      "description": "departments_dataの社員IDと対応"
    },
    "employeeName": {
      "type": "string",
      "title": "社員名(参照用)"
    },
    "employeeSkills": {
      "type": "array",
      "title": "社員スキル一覧",
      "items": {
        "type": "object",
        "properties": {
          "skillName": {
            "type": "string",
            "title": "スキル名"
          },
          "level": {
            "type": "string",
            "title": "習熟度",
            "enum": ["beginner","intermediate","advanced","expert"],
            "enumNames": ["初級","中級","上級","エキスパート"]
          },
          "yearsOfExperience": {
            "type": "integer",
            "title": "経験年数",
            "minimum": 0
          }
        }
      }
    }
  }
}
```

**メリット**:
- ✅ 各拡張項目が4階層以内(Array → Object → Array → Object)に収まる
- ✅ UIで完全に編集可能
- ✅ `employeeId`をキーとしてデータを関連付け
- ✅ それぞれのデータを独立して管理できる

**データの関連付け**:
- `departments_data`で社員の基本情報を管理
- `employee_skills_data`で社員のスキル情報を管理
- 両者を`employeeId`で紐付け

---

#### ネスト構造の対応表

| 構造パターン | 階層数 | UI対応 | 例 |
|------------|--------|--------|-----|
| Object | 1階層 | ✅ | `{type: "object"}` |
| Array → Object | 2階層 | ✅ | ニュース一覧、商品バリエーション |
| Object → Array → Object | 3階層 | ✅ | ユーザー情報 → 注文履歴 |
| Array → Object → Array → Object | 4階層 | ✅ | セクション → 画像一覧 |
| それ以上の深いネスト | 5階層以上 | ❌ | - |

## 関連ドキュメント
- [サブ項目(JSON)を使用して複雑な構造を持つコンテンツ項目を設定する](/ja/docs/tutorials/setting-up-json-field/)
- [コンテンツ定義](/ja/docs/management/content-structure-topics-group/)
- [コンテンツ定義で利用できる項目設定一覧](/ja/docs/reference/list-of-extra-column-available-on-content/)


---

# Kurocoのキーワード検索の種類

> 元ページ: `reference/keyword-search-types` ｜ 公式ページ: https://kuroco.app/ja/docs/reference/keyword-search-types/
> 概要: このドキュメントでは、Kurocoで利用可能な3種類のキーワード検索（topics_keyword、full_text_search、Filter検索）について、その特徴、仕様、利用パターンを説明します。

# Kurocoのキーワード検索の種類

Kurocoには3つの異なるタイプのキーワード検索機能があり、それぞれに特徴とユースケースがあります。このリファレンスでは、各タイプの特性、仕様、使用パターンについて説明します。

## 検索タイプの概要

| 検索タイプ | 説明 | ユースケース |
|:------------|:------------|:--------------|
| [topics_keyword](#topics_keyword) | 特別な設定不要で各項目を自動的に検索 | 基本的なキーワード検索の迅速な実装 |
| [full_text_search](#full_text_search) | テンプレートから生成された文字列を高パフォーマンスで検索 | カスタム検索コンテンツによる複数カラム検索 |
| [Filter検索](#filter検索) | 複雑な条件を持つフィルタークエリを使用 | 複数の条件と演算子を使用した高度な検索 |

## topics_keyword

`topics_keyword`検索は、コンテンツ内の各項目を自動的に検索します。

:::caution
この機能は一部のサイトではすでに使えなくなっているため、[Filter検索](#filter検索)のご利用をお勧めいたします。
:::

### 特徴

- コンテンツ内の各項目を自動的に検索
- スペースで区切られたキーワードはデフォルトでAND検索を実行
- パラメータでAND検索をOR検索に変更可能
- 英数字の大文字小文字は区別しない
- 検索するカラムを指定可能
- 最小限の設定で簡単に実装可能

### 検索可能な項目タイプ

`topics_keyword`は以下の項目タイプを自動的に検索します：

**標準フィールド：**
- `subject` - コンテンツのタイトル/件名フィールド
- `contents` - メインコンテンツのテキストフィールド
- `topics_id` - コンテンツID（キーワードが数字の場合）
- `slug` - コンテンツのSlug
- `contents_type` - コンテンツタイプ/カテゴリ(カテゴリ名で検索します。)

**拡張フィールド：**
- テキスト
- テキスト(オートコンプリート)
- テキストエリア
- WYSIWYG
- HTML
- 単一選択：key, label の両方を検索
- 複数選択可：key, label の両方を検索
- 日付フォーマット
- マスタ形式：key, label の両方を検索
- マスタ(チェックボックス)：key, label の両方を検索
- 関連情報選択：module_id, module_type を使用して検索
- 真偽値フィールド：true/false を文字列として検索
- 画像（KurocoFilesにアップロード）：desc を使用して検索
- ファイル（KurocoFilesにアップロード）：desc を使用して検索
- ファイル（ファイルマネージャーから）: ファイルパスを検索
- APIフィールド
- カウンター: 文字列として検索
- リンク:url, tilte の両方を検索
- 数値: 文字列として検索
- 表組(テーブル)
- 地図

:::tip
`target_col_for_keyword`パラメータを使用して、特定のフィールドに検索を制限してご利用ください。
:::

### パラメータ

| パラメータ | 型 | 説明 | デフォルト |
|:----------|:-----|:------------|:--------|
| topics_keyword | string | 検索するキーワード | - |
| topics_keyword_cond | string | 複数キーワードの条件："AND"または"OR" | "AND" |
| target_col_for_keyword | string/array | 検索対象のカラム（例："subject"、"contents", "ext_1"）| すべての検索可能なカラム |
| use_target_col_for_keyword_from_request | boolean | クエリでtarget_col_for_keywordの指定を許可 | false |

### 多言語サポート

- 副言語で検索するには、`_lang`パラメータを使用（例：`?_lang=en`）
- 検索は指定された言語で自動的に機能します

### 使用例

```
/rcms-api/1/content?topics_keyword=例&topics_keyword_cond=OR
```

### 注意点

- 実装は簡単ですが、複雑な条件はサポートしていません
- より高度な検索には、[Filter検索](#filter検索)の使用を検討してください

## full_text_search

`full_text_search`は、テンプレートを使用して検索可能なテキスト文字列を生成し、複数のカラムにわたる高性能な検索を提供します。

### 特徴

- テンプレートで生成された文字列を検索
- 複数カラム検索に対する高パフォーマンス
- スペースで区切られたキーワードはデフォルトでAND検索を実行
- パラメータでAND検索をOR検索に変更可能
- コンテンツ定義でのキーワードテンプレート設定が必要
- 関連コンテンツやメンバー情報を検索テキストに含めることが可能

### パラメータ

| パラメータ | 型 | 説明 | デフォルト |
|:----------|:-----|:------------|:--------|
| full_text_search | string | 検索するキーワード | - |
| full_text_search_cond | string | 複数キーワードの条件："AND"または"OR" | "AND" |

### 多言語サポート

- 副言語で検索するには、`_lang`パラメータを使用（例：`?_lang=en`）
- 検索は指定された言語で自動的に機能します

### テンプレート設定

full_text_searchを使用するには以下の設定が必要です。  

1. コンテンツ定義設定で「キーワード検索にテンプレートを利用する」を有効にする
2. Smarty構文を使用してテンプレートを設定する


### 使用例

```
/rcms-api/1/content?full_text_search=例&full_text_search_cond=AND
```

### 注意点

- 検索可能な文字列はコンテンツごとに100MBに制限されています
- 検索可能な文字列内の半角英字は自動的に小文字に変換されます
- 実装の詳細については、[キーワード検索用文字列を用意する](/ja/docs/tutorials/how-to-implement-cutom-body-search/)を参照してください

## Filter検索

Filter検索は、フィルタークエリ機能を使用して、様々な条件と演算子による複雑な検索を実行します。

### 特徴

- フィルタークエリで`contains`のオペレータを使用すると指定の項目に対して部分一致で検索が可能(キーワード検索)
- フィルタークエリで`search_keyword`パラメータを使用すると複数の項目に対する検索が可能
- 複数の演算子による複雑な検索条件をサポート
- AND/ORを使用して他のフィルター条件と組み合わせ可能
- 大文字小文字を区別する検索と区別しない検索オプションを提供
- 特定のカラムにわたって検索可能

### containsで検索可能なフィールド

Filter検索の`contains`, `icontains`, `ncontains`, `nicontains`で文字列の部分一致を元に検索可能なカラムには以下があります：

**標準フィールド：**
- `subject` - コンテンツのタイトル/件名フィールド
- `slug` - コンテンツのSlug
- `contents` - メインコンテンツのテキストフィールド

<!--
topics_id は動作しない
contents_type_nm は動作しない
contents_type_ext_col_XX も動作しない
contents_type_list は文字列の部分一致ではなく、指定のIDが配列に含まれるか否かなので除外
-->

**拡張フィールド：**
- テキスト
- テキスト(オートコンプリート)
- テキストエリア
- WYSIWYG
- HTML
- 単一選択：keyに対する検索
- 複数選択可：keyに対する検索
- 日付フォーマット
- マスタ形式：keyに対する検索
- マスタ(チェックボックス)：keyに対する検索
- 真偽値フィールド：true/false を文字列として検索
- 画像（KurocoFilesにアップロード）：desc を使用して検索
- ファイル（KurocoFilesにアップロード）：desc を使用して検索
- ファイル（ファイルマネージャーから）: ファイルパスを検索
- APIフィールド
- リンク:url, tilte の両方を検索
- 表組(テーブル)

<!--
以下は検索できない
- 関連情報選択
- カウンター
- 数値
- 地図はgmap_x, gmap_y, gmap_type, gmap_zoom を検索(gmap_place_idは未確認)するが、:D()の検索が想定されるので除外
-->

:::info
Filter検索の対象とする項目はエンドポイントの`filter_request_allow_list`パラメータで許可されている必要があります。
:::

### search_keywordによる複数項目検索

`search_keyword contains "KEYWORD"`の形式で指定すると、事前に指定した複数のコンテンツに対して contains による絞込みができます。  
項目は`filter_request_allow_list`に`search_keyword:[subject,ext_1]`のように指定します。

### 多言語サポート

- 副言語で検索するには、`filter_lang`パラメータを使用（例：`?filter_lang=en`）
- フィルター検索では、検索対象とする言語(`filter_lang`)とレスポンスの言語(`_lang`)を別に設定できます

### 使用例

特定の項目に対するキーワード検索：
```
?filter=ext_1 contains "例"
```

複数の項目を指定したキーワード検索：
```
?filter=ext_1 contains "例" OR ext_2 contains "例2"
```

大文字小文字を区別しない検索：
```
?filter=ext_1 icontains "例"
```

Not検索：
```
?filter=ext_1 ncontains "除外ワード"
```

他の条件との組み合わせ：
```
?filter=ext_1 contains "例" AND inst_ymdhi > "2023-01-01"
```

search_keywordによる複数項目検索
```
// 事前にエンドポイントに filter_request_allow_list keyword:[subject,ext_1] を設定
?filter=search_keyword contains "例"
```

### 注意点

- 繰り返しフィールドの場合、検索は項目全体に適用されます
- 一部のサイトでは`search_keyword`ではなく`keyword`での検索となります。
- Filter検索はキーワード以外の検索にも利用可能です。詳細は以下を参照してください。
  - [検索機能を実装する](/ja/docs/tutorials/implement-a-search-function/)
  - [Filter検索のパラメータ](/ja/docs/reference/filter-query/)
  - [関連しているデータを条件にしたfilter機能](/ja/docs/reference/r-filter/)

## 関連ドキュメント

- [検索機能を実装する](/ja/docs/tutorials/implement-a-search-function/)
- [Filter検索のパラメータ](/ja/docs/reference/filter-query/)
- [関連しているデータを条件にしたfilter機能](/ja/docs/reference/r-filter/)
- [キーワード検索用文字列を用意する](/ja/docs/tutorials/how-to-implement-cutom-body-search/)
- [Kuroco管理画面の検索機能について](/ja/docs/reference/search-function-on-kuroco-admin-panel/)
