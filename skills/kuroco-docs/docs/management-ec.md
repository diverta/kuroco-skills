# Kurocoドキュメント: 管理画面 / EC・決済

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- ECメインメニュー（`ec`）
- 商品規格編集（`ec-class-edit`）
- 商品規格SKU編集（`ec-combination-edit`）
- SKU一覧（`ec-combination-list`）
- 販売方法設定編集（`ec-delivery-edit`）
- 販売方法設定（`ec-delivery-list`）
- 注文情報編集（`ec-order-edit`）
- 注文一覧（`ec-order-list`）
- かご落ちリスト（`ec-order-list-abandoned`）
- 支払い方法編集（`ec-paymenttype-edit`）
- 支払方法設定（`ec-paymenttype-list`）
- ポイント編集（`ec-point-edit`）
- ポイント履歴（`ec-point-history`）
- ポイント一覧（`ec-point-list`）
- 有料会員プラン編集（`ec-premium-member-plan-edit`）
- 有料会員プラン一覧（`ec-premium-member-plan-list`）
- SKUデータダウンロード（`ec-product-download`）
- 商品設定（`ec-product-edit`）
- SKU設定一覧（`ec-product-group-list`）
- 商品一覧（`ec-product-list`）
- 定期購入者一覧（`ec-regular-member-list`）
- 配送処理（`ec-regular-product-delivery`）
- 定期購入管理（`ec-regular-product-edit`）
- 定期購入一覧（`ec-regular-product-list`）
- 売上ランキング（`ec-sale-ranking`）
- 売上集計（`ec-sale-total`）
- クーポンコード ダウンロード（`ec-serial-code-download`）
- クーポンコード設定編集（`ec-serial-code-group-edit`）
- クーポンコード設定（`ec-serial-code-group-list`）
- クーポンコード履歴（`ec-serial-code-history`）
- クーポンコード一覧（`ec-serial-code-list`）
- クーポンコード アップロード（`ec-serial-code-upload`）
- 売上/配送管理（`ec-shipping-data-search`）
- 店舗情報設定（`ec-shopmaster-edit`）
- SKU設定（`ec-sku-setting`）


---

# ECメインメニュー

> 元ページ: `management/ec` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec/

ECメインメニューでは、EC機能の確認と各設定ページへの遷移ができます。

## ECメインメニューの確認方法
[EC]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

## ECメインメニューの項目説明
ECのメニューは「商品」「注文」「レポート」「設定」にわかれており、それぞれの項目をクリックすると、各機能の画面に遷移します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/edae982bff1f82590805c91df11b4582.png)

## 商品
- SKU設定を追加

## 注文
- 注文一覧
- 売上/配送管理
- 定期購入管理
- かご落ちリスト

## レポート
- 売上集計
- 売上ランキング
- ポイント履歴
- 定期購入者数集計

## 設定
- 店舗情報設定
- 支払い方法設定
- 販売方法設定
- 有料会員設定
- ポイント設定
- クーポンコード設定

## 関連ドキュメント
- [店舗情報設定](/ja/docs/management/ec-shopmaster-edit/)
- [注文一覧](/ja/docs/management/ec-order-list/)
- [SKU設定](/ja/docs/management/ec-sku-setting/)
- [管理画面よりECの設定を行う](/ja/docs/tutorials/ec-management/)
- [ECサイト構築に必要なAPIの設定を行う](/ja/docs/tutorials/ec-api/)
- [ECサイトを作成する フロントエンドを作成する](/ja/docs/tutorials/ec-front-end/)


---

# 商品規格編集

> 元ページ: `management/ec-class-edit` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-class-edit/

商品規格編集では、対象のSKU設定の商品規格を編集できます。

## 商品規格編集の確認方法
[EC]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[SKU/規格]をクリックします。

:::tip
SKUが追加されていないと[SKU/規格]は表示されません。先にSKU設定を追加してください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b8a6beb614b12fbc87aac885d8f45a17.png)

SKU一覧のページから、編集をしたい規格の規格名をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/14e5ac4e859e9c064714ad22e8c4e540.png)

## 商品規格編集の項目説明

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ac78e39e9650da7497ca85e4fe9a5824.png)

|項目   |説明  |
| :--- | :--- |
|規格名|規格名を入力します。|
|コンテンツ定義|SKU設定で登録したコンテンツ定義が表示されます。|
|並び順|並び順を入力します。数値の大きい順に並びます。|
|分類|分類を作成します。[行を追加]をクリックすると、追加の行が表示され、分類を追加できます。|

## 各ボタンの説明
|項目   |説明  |
| :--- | :--- |
|更新する|コンテンツ定義の変更を反映します。|
|削除する|表示しているコンテンツ定義を削除します。|
|全てのSKUパターンを作成|クリックすると登録している分類それぞれでSKUを作成します。|

## 関連ドキュメント
- [SKU一覧](/ja/docs/management/ec-combination-list/)
- [SKU設定](/ja/docs/management/ec-sku-setting/)
- [商品規格SKU編集](/ja/docs/management/ec-combination-edit/)
- [商品設定](/ja/docs/management/ec-product-edit/)
- [管理画面よりECの設定を行う](/ja/docs/tutorials/ec-management/)


---

# 商品規格SKU編集

> 元ページ: `management/ec-combination-edit` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-combination-edit/

商品規格SKU編集では、SKUの商品規格の組み合わせを編集できます。

## 商品規格SKU編集の確認方法
[EC]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[SKU/規格]をクリックします。

:::tip
SKUが追加されていないと[SKU/規格]は表示されません。先にSKU設定を追加してください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b8a6beb614b12fbc87aac885d8f45a17.png)

SKU一覧のページから、編集をしたいSKUのSKU IDをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f6dca10e9be3a1bb9d7b2b3fc3162aee.png)

## 商品規格SKU編集の項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c4941dd07cac2795c6777694751b4b5c.png)

|項目   |説明  |
| :--- | :--- |
|コンテンツ定義|SKU設定で登録したコンテンツ定義が表示されます。|
|規格名|登録されている規格の一覧が表示されるので、それぞれの分類を選択します。

## 更新するボタン、削除するボタン
|項目   |説明  |
| :--- | :--- |
|更新する|SKUの変更を反映します。|
|削除する|表示しているSKUを削除します。<br/>この組み合わせを使用する商品がある場合は削除ができません。|

## 商品一覧
選択した商品規格SKUを使用する商品の一覧を表示します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bcc06214d353139671c9209a974c701f.png)

|項目   |説明  |
| :--- | :--- |
|商品ID|商品IDを表示します。|
|商品|商品名を表示します。|
|商品を削除|一覧の左端のチェックボックスにチェックを入れて、[商品を削除]をクリックすると、選択した商品を削除します。|

## 関連ドキュメント
- [SKU一覧](/ja/docs/management/ec-combination-list/)
- [商品規格編集](/ja/docs/management/ec-class-edit/)
- [SKU設定](/ja/docs/management/ec-sku-setting/)
- [商品設定](/ja/docs/management/ec-product-edit/)
- [管理画面よりECの設定を行う](/ja/docs/tutorials/ec-management/)


---

# SKU一覧

> 元ページ: `management/ec-combination-list` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-combination-list/

SKU一覧ではKurocoに登録しているSKUの一覧を確認できます。

## SKU一覧の確認方法
[EC]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)
ECメインメニューから[SKU/規格]をクリックします。

:::tip
SKUが追加されていないと[SKU/規格]は表示されません。先にSKU設定を追加してください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b8a6beb614b12fbc87aac885d8f45a17.png)

## SKU一覧の項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d0b188b8bc5b94e2d3f6ed56f3efe3a3.png)

|項目   |説明  |
| :--- | :--- |
|コンテンツ定義|SKU設定に登録されているコンテンツ定義を表示します。|
|CSVアップロード|CSVファイルでSKUのアップロードができます。|
|CSVダウンロード|CSVファイルでSKU一覧のダウンロードができます。|
|SKU:SKU ID|SKUのIDを表示します。|
|SKU:規格を追加|クリックすると商品規格編集のページに遷移し、SKUの規格を追加することができます。|

## 関連ドキュメント
- [SKU設定](/ja/docs/management/ec-sku-setting/)
- [商品規格編集](/ja/docs/management/ec-class-edit/)
- [商品規格SKU編集](/ja/docs/management/ec-combination-edit/)
- [SKUデータダウンロード](/ja/docs/management/ec-product-download/)
- [管理画面よりECの設定を行う](/ja/docs/tutorials/ec-management/)


---

# 販売方法設定編集

> 元ページ: `management/ec-delivery-edit` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-delivery-edit/

販売方法設定編集では販売方法の設定を編集できます。

## 販売方法設定編集の確認方法
[EC]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[販売方法設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/da8e6c5f93ca4b1d5a296b341e72072e.png)

販売方法設定のページから編集をしたい販売方法の[編集]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/15b27aeb45c88c670f973031293a7524.png)

## 販売方法設定編集の項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/cbe0f30b049d19269ab029dbd78b66c8.png)

|項目   |説明  |
| :--- | :--- |
|販売方法|販売方法の名前を入力します。|
|支払方法|利用できる支払方法を設定します。<br/>[編集]をクリックすると、支払方法編集のページを開きます。|
|商品種別|商品種別を選択します。<li>宅配:管理画面から売上/配送処理を行う実態のある商品</li><li>ダウンロード:マイページからDLを行うような電子商品</li><li>会員サービス/イベント:有料会員やイベント申し込みといったようなサービス商品</li>|
|サービス名／配送業者名|サービス名／配送業者名を入力します。|
|説明|販売方法に関する説明を入力します。|
|サービス利用料／配送料|本販売方法を選択した際のサービス利用料／配送料を入力します。|
|サービス利用料／配送料 (配送先別設定)|配送先別にサービス利用料／配送料を設定する場合は都道府県または郵便番号で設定をします。|
|送料無料の対象に含めない|送料無料の対象に含めない場合はチェックを入れます。|

## 更新するボタン

|項目   |説明  |
| :--- | :--- |
|更新する|クリックすると販売方法の編集内容を反映します。|

## 関連ドキュメント
- [販売方法設定](/ja/docs/management/ec-delivery-list/)
- [支払い方法編集](/ja/docs/management/ec-paymenttype-edit/)
- [支払方法設定](/ja/docs/management/ec-paymenttype-list/)
- [管理画面よりECの設定を行う](/ja/docs/tutorials/ec-management/)


---

# 販売方法設定

> 元ページ: `management/ec-delivery-list` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-delivery-list/

販売方法設定ではKurocoに登録している販売方法の確認ができます。

## 販売方法設定の確認方法
[EC]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[販売方法設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/da8e6c5f93ca4b1d5a296b341e72072e.png)

## 販売方法設定の項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0b4c4cb774ce0560a1ef4d4fda6da78a.png)

|項目   |説明  |
| :--- | :--- |
|販売ID|販売方法のIDが表示されます。IDは自動採番されます。|
|販売方法|販売方法編集で設定した販売方法の名前が表示されます。|
|支払い方法|利用できる支払方法を表示します。|
|商品種別|商品種別を表示します。|
|サービス利用料／配送料|サービス利用料／配送料を表示します。|
|編集|クリックすると販売方法編集のページに遷移します。|
|削除|クリックすると販売方法を削除します。|

## 関連ドキュメント
- [販売方法設定編集](/ja/docs/management/ec-delivery-edit/)
- [支払方法設定](/ja/docs/management/ec-paymenttype-list/)
- [ECメインメニュー](/ja/docs/management/ec/)
- [管理画面よりECの設定を行う](/ja/docs/tutorials/ec-management/)


---

# 注文情報編集

> 元ページ: `management/ec-order-edit` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-order-edit/

注文情報編集では注文の内容の変更やキャンセルができます。

## 注文情報編集の確認方法
[EC]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[注文一覧]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6cfd10804f270954959366a5852b09c0.png)

注文一覧のページから編集したい注文の[注文番号]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ffbeabc8ddaf768c5813cd377d924611.png)

## 注文情報編集の項目説明
### 注文情報
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/f63b26614542036fc87c7c2ca0e2357b.png)

|項目   |説明  |
| :--- | :--- |
|注文番号|注文番号を表示します。|
|決済番号|外部決済サービスから発行された決済番号を入力します。|
|承認番号（コンビニ取引番号）|外部決済サービスから発行された承認番号（またはコンビニ取引番号）を入力します。|
|支払種別|支払種別を選択します。|
|支払い方法|支払方法を表示します。|
|支払い備考|支払いに対する備考を入力します。|
|支払い状態|支払状態を選択します。|
|注文日時|注文日時を表示します。|
|入金日時|入金日時を表示します。|
|売上日時|売上日時を表示します。|
|キャンセル|表示している注文をキャンセルする場合はチェックを入れます。|
|備考|注文に対する備考を入力します。|

### 注文者情報
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a1d5fd8c68fab2d7f468a319485341a7.png)

|項目   |説明  |
| :--- | :--- |
|メンバーID|メンバーIDを入力します。|
|お名前|お名前を入力します。|
|メールアドレス|メールアドレスを入力します。|
|電話番号|電話番号を入力します。|
|住所|住所を入力します。|

### 受注商品情報
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/90a1aa86578da8334b61b9ab8d0f22b2.png)

|項目   |説明  |
| :--- | :--- |
|商品|商品のSKUを設定します。<br/>[コンテンツ定義] -> [コンテンツ] -> [商品] の順に選択します。 |
|商品を確認|クリックすると商品設定のページへ遷移します。|
|変更履歴を確認|クリックすると注文情報の更新履歴一覧ページへ遷移します。|
|配送状態|配送状態を表示します。|
|単価|単価を表示します。|
|数量|数量を表示します。|
|小計|小計を表示します。|
|送料|送料を入力します。|
|手数料|手数料を入力します。|
|合計|合計金額を入力します。|
|お支払金額|お支払金額を入力します。|
|使用ポイント|使用ポイントを入力します。|
|加算ポイント|加算ポイントを入力します。|

### クーポンコード情報

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d3f0a86d1bfe325cb9c5149ed470b4da.png)

|項目   |説明  |
| :--- | :--- |
|クーポンコード情報|注文時にクーポンの利用があった場合、クーポン情報へのリンクを表示します。<br/>利用していない場合は、「クーポンコード利用なし」を表示します。|
|商品|クーポンコードを利用した商品の情報を表示します。|

### お届け先情報
![Image from Gyazo](https://t.gyazo.com/teams/diverta/20c745bf063506892a8df35896983bf4.png)

|項目   |説明  |
| :--- | :--- |
|お名前|お名前を入力します。|
|電話番号|電話番号を入力します。|
|住所|住所を入力します。|
|配送希望|配送希望を入力します。|

### メモ
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/13eda61786611b002d828476bded6f6c.png)

|項目   |説明  |
| :--- | :--- |
|メモ1～メモ10|注文情報に関してメモを入力できます。|

### 更新するボタン、更新コメント
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c95f77ca994a380e645666855afdbcab.png)

|項目   |説明  |
| :--- | :--- |
|更新する|クリックすると注文情報の編集内容を反映します。|
|前回の更新コメント|前回の注文情報更新時のコメントを表示します。|
|更新コメント|注文情報を更新する際にコメントを残すことができます。|

## 関連ドキュメント
- [注文一覧](/ja/docs/management/ec-order-list/)
- [売上/配送管理](/ja/docs/management/ec-shipping-data-search/)
- [クーポンコード履歴](/ja/docs/management/ec-serial-code-history/)
- [管理画面よりECの設定を行う](/ja/docs/tutorials/ec-management/)


---

# 注文一覧

> 元ページ: `management/ec-order-list` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-order-list/

注文一覧では、商品への注文情報を確認できます。

## 注文一覧の確認方法
[EC]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[注文一覧]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b7cf0e77f26a7d4fb1656ca71da3d5aa.png)

## 注文一覧の項目説明
### 検索条件設定
![Image from Gyazo](https://t.gyazo.com/teams/diverta/54c44e957930ef57e217114bd0d1b908.png)

|項目   |説明  |
| :--- | :--- |
|注文番号|注文番号を入力します。|
|購入金額|購入金額の範囲を入力します。|
|支払い方法|支払方法を選択します。|
|支払い状態|支払状態を選択します。|
|お名前|注文者のお名前を入力します。|
|メンバーID|メンバーIDを入力します。|
|メールアドレス|メールアドレスを入力します。|
|都道府県|都道府県を選択します。|
|住所|住所を入力します。|
|電話番号|電話番号を入力します。|
|配送状態|配送状態を選択します。|
|メモ(件)|メモ項目の名前を選択します。(メモ1〜メモ10)|
|メモ(値)|メモ項目の値を入力します。[メモ(件)]で選択した項目が検索対象になります。|
|コンテンツ定義|注文された商品のコンテンツ定義を選択します。|
|対象商品|注文された商品のSKUを選択します。|
|商品名/商品ID|商品名/商品IDを入力します。|
|キャンセル|キャンセルの条件を選択します。|
|自動継続キャンセル|自動継続キャンセルの条件を選択します。|
|継続注文|継続注文の条件を選択します。|
|定期購入/自動継続|定期購入/自動継続の条件を選択します。|
|受注生産|受注生産の条件を選択します。|
|受注日|受注日を設定します。|
|入金日|入金日を設定します。|
|売上(発送)日|売上(発送)日を設定します。|
|会員・非会員|会員・非会員を選択します。|
|検索する|設定した条件で注文を検索します。|
|ダウンロードする|注文一覧のCSVファイルをダウンロードします。|
|検索条件をクリア|設定した検索条件をクリアします。|

### 並び順
![Image from Gyazo](https://t.gyazo.com/teams/diverta/69af401ae6dfe818cbe8dafd5b33da74.png)

|項目   |説明  |
| :--- | :--- |
|項目名|並び順に利用する項目を選択します。|
|並び順|降順か昇順かを選択します。|
|並び順を更新する|クリックすると注文一覧の並び順を更新します。|

### 注文データアップロード
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6b9e600e206aa71bad3b1735877cfdfa.png)

|項目   |説明  |
| :--- | :--- |
|csvファイル|[ファイルを選択]をクリックしてアップロードするCSVファイルを選択します。<br/>CSVファイルのサンプルは[ダウンロード]ボタンから取得できます。|
|値がない場合の動作|値が無い場合の動作を設定します。|
|アップロードする|クリックすると設定したcsvファイルをアップロードします。|

### 注文一覧
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a4c2666ab477ec875c120a521ece9c70.png)

|項目   |説明  |
| :--- | :--- |
|受注日|注文の受注日を表示します。|
|注文番号|注文番号を表示します。<br/>リンクをクリックすると注文情報編集のページへ遷移します。|
|お名前|注文者のお名前を表示します。|
|支払方法|支払方法を表示します。|
|入金日|入金日を表示します。|
|売上(発送)日|売上(発送)日を表示します。|
|キャンセル|注文のキャンセル状態に応じて、次の値のうちいずれか、または複数を表示します。<br/>「注文」<br/>「定期購入」<br/>「自動継続」|
|購入商品|購入した商品の情報を表示します。|
|購入金額|購入した商品の金額を表示します。|

### 一括処理
一覧の左端のチェックボックスにチェックを入れて、[削除する][キャンセルする]のいずれかをクリックすると、選択した注文に対して一括で処理を行います。

## 関連ドキュメント
- [注文情報編集](/ja/docs/management/ec-order-edit/)
- [売上/配送管理](/ja/docs/management/ec-shipping-data-search/)
- [かご落ちリスト](/ja/docs/management/ec-order-list-abandoned/)
- [売上集計](/ja/docs/management/ec-sale-total/)
- [管理画面よりECの設定を行う](/ja/docs/tutorials/ec-management/)


---

# かご落ちリスト

> 元ページ: `management/ec-order-list-abandoned` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-order-list-abandoned/

かご落ちリストではお客様が現在カートに入れている購入前の商品が確認できます。

## かご落ちリストの確認方法
[EC]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[かご落ちリスト]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/dfdfcceac2eaf00ee95d1b92f5d2a033.png)

## かご落ちリストの項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/bd74fa117a63e61c2d814574d9cf391d.png)

|項目   |説明  |
| :--- | :--- |
|カートID|対象のカートID|
|メンバー|会員の場合: 名前を表示<br/>非会員: Guest表示|
|商品名|カートに入れている商品名、及びその個数|
|最終更新日|カートの最終更新日|

## 一括処理
一覧の左端のチェックボックスにチェックを入れて、[削除する]をクリックすると、選択したかご落ちに対して一括で処理を行います。

## 関連ドキュメント
- [注文一覧](/ja/docs/management/ec-order-list/)
- [ECメインメニュー](/ja/docs/management/ec/)
- [管理画面よりECの設定を行う](/ja/docs/tutorials/ec-management/)


---

# 支払い方法編集

> 元ページ: `management/ec-paymenttype-edit` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-paymenttype-edit/

支払い方法編集では支払い方法の設定を編集できます。

## 支払い方法編集の確認方法
[EC]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[支払い方法設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/09e5da0135d4886849bc807b2fac38ff.png)

支払い方法設定のページから編集をしたい支払い方法の[編集]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b4e63f4bcda92f73749909ddd893e9e3.png)

## 支払い方法編集の項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9d3dcc12f578708c59288752c25b6c74.png)

|項目   |説明  |
| :--- | :--- |
|支払種別|支払い方法の名前を入力します。|
|支払い方法|支払い方法を設定します。<br/>Kurocoが対応している支払い方法は下記になります。<br/><br/>デフォルトで表示<li>支払い無し</li><li>代引き</li><li>現行振込</li><li>後払い</li><li>マニュアル決済</li><br/>Paygent連携後に表示<li>クレジットカード</li><li>コンビニ決済</li><li>月次クレジットカード</li><li>ネットバンキング</li><li>ATM決済(Pay-easy)</li>|
|手数料|手数料を設定します。|
|対象金額|支払い方法として利用できる対象の金額を設定します。|
|並び順|並び順を入力します。数値の大きい順に並びます。|

## 更新するボタン、削除するボタン

|項目   |説明  |
| :--- | :--- |
|更新する|クリックすると支払い方法の編集内容を反映します。|
|削除する|クリックすると表示している支払い方法を削除します。|

## 関連ドキュメント
- [支払方法設定](/ja/docs/management/ec-paymenttype-list/)
- [ECメインメニュー](/ja/docs/management/ec/)
- [管理画面よりECの設定を行う](/ja/docs/tutorials/ec-management/)
- [Paygentと連携するには](/ja/docs/tutorials/ec-paygent/)
- [EC決済方法別設定](/ja/docs/reference/ec-paymet-setting/)


---

# 支払方法設定

> 元ページ: `management/ec-paymenttype-list` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-paymenttype-list/

支払方法設定ではKurocoに登録している支払方法の確認ができます。

## 支払方法設定の確認方法
[EC]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[支払い方法設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/09e5da0135d4886849bc807b2fac38ff.png)

## 支払方法設定の項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/44c87e8f9adf016cfdeff223c6a2711b.png)

|項目   |説明  |
| :--- | :--- |
|ID|支払方法のIDが表示されます。IDは自動採番されます。|
|支払種別|支払方法編集で設定した支払の名前が表示されます。|
|支払い方法|支払い方法が表示されます。|
|手数料|手数料が表示されます。|
|対象金額(円)|支払方法として利用できる対象の金額が表示されます。|
|並び順|数の大きな順に並びます。一覧画面で入力して、画面下の[並び順を更新する]をクリックすると、一覧画面上で並び順だけ変更することができます。|
|編集|クリックすると支払方法編集のページに遷移します。|
|削除|クリックすると支払方法を削除します。|

## 関連ドキュメント
- [支払い方法編集](/ja/docs/management/ec-paymenttype-edit/)
- [ECメインメニュー](/ja/docs/management/ec/)
- [管理画面よりECの設定を行う](/ja/docs/tutorials/ec-management/)
- [Paygentと連携するには](/ja/docs/tutorials/ec-paygent/)
- [EC決済方法別設定](/ja/docs/reference/ec-paymet-setting/)


---

# ポイント編集

> 元ページ: `management/ec-point-edit` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-point-edit/

ポイント編集ではポイントを付与する条件を編集できます。

:::info
ポイント付与条件を設定していない場合、ポイントの自動付与（商品購入・ログイン・会員登録）は行われません。タイプ「商品購入」のポイントを付与するには、さらに[商品設定](/ja/docs/management/ec-product-edit/)の「ポイント率」で対象の商品にポイント設定を紐付ける必要があります。
:::

## ポイント編集の確認方法
[EC]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[ポイント設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b1c92935233e18db96ab87b242072d5c.png)

ポイント一覧のページから編集をしたいポイントの[タイトル]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/754743b207c85c9efad69f54f3038c28.png)

## ポイント編集の項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ba27cb6b5dc43301e8ed09242703321d.png)

|項目   |説明  |
| :--- | :--- |
|タイトル|ポイント付与条件のタイトルを入力します。|
|タイプ|ポイント付与対象のアクションを設定します。<br/><br/>商品購入: 商品の購入時にポイントを付与します。<br/>ログイン: ログイン時にポイントを付与します。<br/>会員登録: 会員登録の完了時にポイントを付与します。|
|ポイント数|付与するポイントを数値または%で入力します。<br/><br/>ポイント: 付与するポイントを数値で指定します。<br/>%: 購入金額に対して何パーセントのポイントを付与するかを指定します。タイプ「商品購入」を選択した場合のみ設定できます。|
|有効期間|ポイントの有効期間を入力します。<br/>年/月/週/日いずれかの単位で指定することができます。|
|仮期間|ポイントの仮期間を入力します。<br/>年/月/週/日いずれかの単位で指定することができます。<br/><br/>タイプ「商品購入」の場合、ポイントは仮ポイントとして付与されます。代引きの場合のみ仮期間が適用され、売上処理後、仮期間の経過後に確定します。代引き以外の支払い方法の場合、仮期間は適用されず、売上のタイミングでポイントが確定します。<br/>タイプ「ログイン」「会員登録」の場合、仮期間を設定すると仮ポイントとして付与され、仮期間の経過後に確定します。仮期間を設定しない場合は、即時に確定ポイントとして付与されます。<br/><br/>詳細は[仮ポイントが発生する操作と確定のタイミング](/ja/docs/reference/ec-point/#仮ポイントが発生する操作と確定のタイミング)を参照してください。|

## 更新するボタン、削除するボタン

|項目   |説明  |
| :--- | :--- |
|更新する|クリックすると、ポイント付与条件の編集内容を反映します。|
|削除する|クリックすると、表示しているポイント付与条件を削除します。|

## 関連ドキュメント
- [ポイント一覧](/ja/docs/management/ec-point-list/)
- [ポイント履歴](/ja/docs/management/ec-point-history/)
- [商品設定](/ja/docs/management/ec-product-edit/)
- [ECメインメニュー](/ja/docs/management/ec/)
- [管理画面よりECの設定を行う](/ja/docs/tutorials/ec-management/)


---

# ポイント履歴

> 元ページ: `management/ec-point-history` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-point-history/

ポイント履歴ではユーザーが獲得したポイントと使用したポイントを確認できます。

## ポイント履歴の確認方法
[EC]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[ポイント履歴]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0245404b215e65e3066de3ec38efe149.png)

## ポイント履歴の項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5de2af90c1476cf0b5c21e9a2dc2dd7f.png)

|項目   |説明  |
| :--- | :--- |
|対象月|ポイント履歴を確認する対象月を設定します。|
|ユーザー獲得ポイント累計|ユーザーが獲得したポイントの累計を表示します。|
|ユーザー使用ポイント累計|ユーザーが使用したポイントの累計を表示します。|
|更新する|クリックするとポイント履歴の表示を更新します。|

## 関連ドキュメント
- [ポイント一覧](/ja/docs/management/ec-point-list/)
- [ポイント編集](/ja/docs/management/ec-point-edit/)
- [売上/配送管理](/ja/docs/management/ec-shipping-data-search/)
- [ECメインメニュー](/ja/docs/management/ec/)


---

# ポイント一覧

> 元ページ: `management/ec-point-list` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-point-list/

ポイント一覧ではKurocoに登録しているポイント付与条件の一覧を確認できます。

## ポイント一覧の確認方法
[EC]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[ポイント設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b1c92935233e18db96ab87b242072d5c.png)

## ポイント一覧の項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c55740906fe54511e0a70a576e23c296.png)

|項目   |説明  |
| :--- | :--- |
|タイトル|ポイント付与条件のタイトルを入力します。|
|タイプ|ポイント付与対象のタイプを表示します。|
|ポイント数|獲得できるポイント数を表示します。|
|有効期間|ポイントの有効期間を表示します。|
|仮期間|ポイントの仮期間を表示します。|

各項目の詳細な説明については、[ポイント編集](/ja/docs/management/ec-point-edit/)を参照してください。

## 一括処理
一覧の左端のチェックボックスにチェックを入れて、[削除する]をクリックすると、選択したポイント付与条件に対して一括で処理を行います。

## 関連ドキュメント
- [ポイント編集](/ja/docs/management/ec-point-edit/)
- [ポイント履歴](/ja/docs/management/ec-point-history/)
- [ECメインメニュー](/ja/docs/management/ec/)
- [管理画面よりECの設定を行う](/ja/docs/tutorials/ec-management/)


---

# 有料会員プラン編集

> 元ページ: `management/ec-premium-member-plan-edit` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-premium-member-plan-edit/

有料会員プラン編集では有料会員プランの設定を編集できます。

## 有料会員プラン編集の確認方法
[EC]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[有料会員設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/74dfb568c43a6c97c1601f88ebfa5998.png)

有料会員プラン一覧のページから、編集をしたい有料会員プランの[編集]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5a77cb7d6d9f6160240dc083aee50000.png)

## 有料会員プラン編集の項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f21d803720d1be724c2fc47f159e502d.png)

|項目   |説明  |
| :--- | :--- |
|プラン名|プラン名を入力します。|
|有効期間|有効期間を設定します。|
|コンテンツ 【 商品 】|有料会員プランに所属するために購入する商品名が表示されます。|
|送料無料条件|有料会員の送料無料条件を設定します。|
|グループ|有料会員が所属するグループを設定します。|

## 更新するボタン、削除するボタン

|項目   |説明  |
| :--- | :--- |
|更新する|クリックすると有料会員プランの編集内容を反映します。|
|削除する|クリックすると表示している有料会員プランを削除します。|

## 関連ドキュメント
- [有料会員プラン一覧](/ja/docs/management/ec-premium-member-plan-list/)
- [商品設定](/ja/docs/management/ec-product-edit/)
- [グループ](/ja/docs/management/group/)
- [ECメインメニュー](/ja/docs/management/ec/)
- [Stripeと連携して有料会員の機能を実装する。](/ja/docs/tutorials/subscription-billing-with-stripe/)


---

# 有料会員プラン一覧

> 元ページ: `management/ec-premium-member-plan-list` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-premium-member-plan-list/

有料会員プラン一覧ではKurocoに登録している有料会員プランの一覧を確認できます。

## 有料会員プラン一覧の確認方法
[EC]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[有料会員設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/74dfb568c43a6c97c1601f88ebfa5998.png)

## 有料会員プラン一覧の項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/50411ad4a15f87cb1e500d9852a01023.png)

|項目   |説明  |
| :--- | :--- |
|No.|有料会員プランの番号が表示されます。番号は自動で採番されます。|
|プラン名|有料会員プランのプラン名を表示します。|
|購入すべき商品名[商品ID]|有料会員プランに所属するために購入する商品名を表示します。|
|付与される会員グループ名[グループID]|有料会員プランに付与されるグループ名を表示します。|
|編集|クリックすると有料会員プラン編集のページに遷移します。|

## 関連ドキュメント
- [有料会員プラン編集](/ja/docs/management/ec-premium-member-plan-edit/)
- [グループ](/ja/docs/management/group/)
- [ECメインメニュー](/ja/docs/management/ec/)
- [Stripeと連携して有料会員の機能を実装する。](/ja/docs/tutorials/subscription-billing-with-stripe/)


---

# SKUデータダウンロード

> 元ページ: `management/ec-product-download` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-product-download/

SKUデータダウンロードでは、対象のSKU設定に登録しているSKUの一覧をダウンロードできます。

## SKUデータダウンロードの確認方法
[EC]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)
ECメインメニューから[SKU/規格]をクリックします。

:::tip
SKUが追加されていないと[SKU/規格]は表示されません。先にSKU設定を追加してください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b8a6beb614b12fbc87aac885d8f45a17.png)

SKU一覧のページから[SKUデータダウンロード]のタブをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/deea3547dbbd68c6b06bae9fc59fa033.png)

## SKUデータダウンロードの項目説明

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d87c11814c04c1c13423238b09b7ef9e.png)

|項目   |説明  |
| :--- | :--- |
|カテゴリ|商品のカテゴリを設定します。|
|規格|ダウンロードする規格を設定します。|
|文字コード|ダウンロードする文字コードを指定します。|
|出力列設定|[出力する列を選択する。]をクリックすると、列名一覧が表示されます。出力したい列を選択します。|
|ダウンロードする|設定した条件でSKUデータをダウンロードします。|

## 関連ドキュメント
- [SKU一覧](/ja/docs/management/ec-combination-list/)
- [SKU設定](/ja/docs/management/ec-sku-setting/)
- [商品一覧](/ja/docs/management/ec-product-list/)
- [商品規格編集](/ja/docs/management/ec-class-edit/)


---

# 商品設定

> 元ページ: `management/ec-product-edit` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-product-edit/

商品設定では、販売価格や在庫数などの商品の設定を確認・編集できます。

## 商品設定の確認方法
[EC]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[EC]をクリックし、表示されたプルダウンから[SKU]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5d960774fc88c89459955a6c3c4a1bee.png)

商品一覧のページから、確認をしたい商品アイテムをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/75870c81531e637fabda2e7884d9ceae.png)

## 商品設定の項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6dc7dce7bc77f68bddb0da088221bcff.png)

|項目   |説明  |
| :--- | :--- |
|商品ID|商品IDを表示します。|
|コンテンツ定義|商品が所属するコンテンツ定義を表示します。|
|コンテンツ|商品が所属するコンテンツを表示します。|
|SKU|SKUを表示します。|
|並び順|並び順を入力します。数値の大きい順に並びます。|
|商品名|商品名を入力します。|
|販売価格|販売価格を入力します。<br/>「値引き額を使用する」にチェックを入れた場合実際の販売価格とは別に値引き前の金額を管理できます。<br/>「グループ別価格設定」を有効にした場合、購入者が所属しているグループに応じて販売価格を変更することが出来ます。|
|在庫数|在庫数を入力します。<br/>有料会員商品など特に在庫がない商品の場合は「無制限」にチェックを入れて下さい。|
|販売方法|販売方法を設定します。|
|ポイント率|ポイント率を選択します。|
|販売制限数|一度にカートに入れられる項目を制限します。<br/>（繰り返し購入することで複数購入は可能です）|
|発売日時|商品の発売日時です。<br/>同時に購入した商品も、この日付が異なると別注文に分割されます。<br/>ダウンロード商品の場合はこの日付以降にダウンロード可能になります。|
|在庫数の連動|購入・キャンセルのタイミングで指定商品も合わせて在庫数の増減を行います|
|セット商品（親商品）|編集中の商品が子商品だった場合に、親商品に指定されている商品です。|
|セット商品（子商品）|編集中の商品が親商品だった場合に、子商品に指定されている商品です。|
|定期購入回数|定期購入の対象商品の場合は「定期購入」にチェックを入れ回数を指定して下さい。|
|自動継続上限|自動継続課金を行う場合は自動継続にチェックを入れ回数を指定して下さい。特に回数の制限がない場合は十分に大きな数を指定して下さい。|
|受注生産|受注生産商品の場合にチェックを入れて下さい。<br/>受注生産商品は他の商品と同時に購入することは出来ません。また、売上配送管理画面などで受注生産商品の購入注文に対して絞り込みをかけることも可能になります。|
|拡張|[SKU設定](/ja/docs/management/ec-sku-setting/)で設定した拡張項目が表示されます。|

## 公開設定
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c653e826a5b7a19a18483d6a3412d967.png)

|項目   |説明  |
| :--- | :--- |
|公開にする|商品を公開します。|
|非公開にする|商品を非公開にします。|
|公開日指定|開始日付、終了日付を任意に指定して商品を公開します。|

## 更新するボタン、削除するボタン、更新コメント
![Image from Gyazo](https://t.gyazo.com/teams/diverta/cd77905de22dd6a9a3b6d82ec54bef5f.png)

|項目   |説明  |
| :--- | :--- |
|更新する|商品設定の変更を反映します。|
|削除する|表示している商品設定を削除します。|
|前回の更新コメント|前回の商品設定更新時のコメントを表示します。|
|更新コメント|商品設定を更新する際にコメントを残すことができます。|

## 関連ドキュメント
- [商品一覧](/ja/docs/management/ec-product-list/)
- [SKU設定](/ja/docs/management/ec-sku-setting/)
- [商品規格SKU編集](/ja/docs/management/ec-combination-edit/)
- [販売方法設定](/ja/docs/management/ec-delivery-list/)
- [管理画面よりECの設定を行う](/ja/docs/tutorials/ec-management/)


---

# SKU設定一覧

> 元ページ: `management/ec-product-group-list` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-product-group-list/

SKU設定一覧ではKurocoに登録しているSKU設定の一覧を確認できます。

## SKU設定一覧の確認方法
[EC]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[EC]をクリックし、表示されたプルダウンから[SKU設定一覧]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/24d3861b937f84b73fe7b5238d868fff.png)

## SKU設定一覧の項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ff2e6572e2753a2f19e3f4fd317d6206.png)

|項目   |説明  |
| :--- | :--- |
|公開|公開状態を確認できます。<br/>![fetched from Gyazo](https://t.gyazo.com/teams/diverta/04844a6327ba668f74880a0f10682489.png)：公開<br/>![fetched from Gyazo](https://t.gyazo.com/teams/diverta/f5923e63675ff30a82d61133019736d2.png)：閲覧制限有り<br/>![fetched from Gyazo](https://t.gyazo.com/teams/diverta/b483e6f928fc3319266dad8bc633f086.png)：非公開|
|SKU設定ID|SKU設定IDを表示します。IDは自動で採番されます。|
|SKU設定名|SKUの名前を表示します。|
|商品一覧|[商品一覧]をクリックすると商品一覧ページへ遷移し、対象のSKU設定の商品一覧が表示されます。|
|設定|[設定]をクリックするとSKU設定のページに遷移し、SKU設定の編集ができます。|
|最終更新日|SKU設定を最後に更新した日時を表示します。|

### 一括処理
一覧の左端のチェックボックスにチェックを入れて、[削除する]をクリックすると、選択したSKU設定に対して一括で処理を行います。

## 関連ドキュメント
- [SKU設定](/ja/docs/management/ec-sku-setting/)
- [商品一覧](/ja/docs/management/ec-product-list/)
- [SKU一覧](/ja/docs/management/ec-combination-list/)
- [ECメインメニュー](/ja/docs/management/ec/)


---

# 商品一覧

> 元ページ: `management/ec-product-list` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-product-list/

商品一覧ではKurocoに登録している商品の一覧を確認できます。

## 商品一覧の確認方法
[EC]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[EC]をクリックし、表示されたプルダウンから[SKU]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5d960774fc88c89459955a6c3c4a1bee.png)

## 商品一覧の項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/817c32c47dec2f9e5158f23a09148e1b.png)

|項目   |説明  |
| :--- | :--- |
|検索|条件を設定して商品の検索ができます。|
|商品名|商品名を表示します。<br/>クリックすると対象の商品コンテンツへ遷移します。|
|公開|公開状態を確認できます。<br/>![fetched from Gyazo](https://t.gyazo.com/teams/diverta/04844a6327ba668f74880a0f10682489.png)：公開<br/>![fetched from Gyazo](https://t.gyazo.com/teams/diverta/b483e6f928fc3319266dad8bc633f086.png)：非公開|
|商品ID|商品IDを表示します。IDは自動で採番されます。|
|商品アイテムを追加|クリックすると追加するSKUに設定する商品規格SKU設定ページへ遷移します。|
|商品アイテム|商品名を表示します。<br/>クリックするとSKU編集のページへ遷移します。|
|SKU|対象SKUの規格を表示します。|
|販売数|販売数を表示します。|
|在庫数|在庫数を表示します。|
|お気に入り|お気に入り登録されている数を表示します。|

## 一括処理
公開情報横のチェックボックスにチェックを入れて、[公開にする][非公開にする][削除する]のいずれかをクリックすると、選択した商品に対して一括で処理を行います。

## 関連ドキュメント
- [商品設定](/ja/docs/management/ec-product-edit/)
- [商品規格SKU編集](/ja/docs/management/ec-combination-edit/)
- [SKU設定](/ja/docs/management/ec-sku-setting/)
- [SKU設定一覧](/ja/docs/management/ec-product-group-list/)
- [管理画面よりECの設定を行う](/ja/docs/tutorials/ec-management/)


---

# 定期購入者一覧

> 元ページ: `management/ec-regular-member-list` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-regular-member-list/

定期購入者一覧では現在定期購入を行なっているユーザーとその購入状況が確認できます。

## 定期購入者一覧の確認方法
[EC]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[定期購読者数集計]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c236dfdc5d5ab4c94c5e415f9b4f3c0b.png)

定期購入者一覧ページが表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b8ccf4c98a6002f5aac1fe12a4936214.png)

## 定期購入者一覧の項目説明
### 検索条件設定

![Image from Gyazo](https://t.gyazo.com/teams/diverta/16f578e94199414a6a6ce9d63aa02ded.png)

|項目   |説明  |
| :--- | :--- |
|商品名/商品ID|商品名/商品IDを入力します。|
|商品種別|商品種別を選択します。|
|自動継続|自動継続の条件を選択します。|
|文字コード|文字コードを選択します。|
|検索する|設定した条件で定期購入者を検索します。|
|CSVダウンロードする|設定した条件で定期購入者の一覧をCSVダウンロードします。|


### 一覧

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5bf215c872ed1f0dd85a8531beb61f4b.png)

|項目   |説明  |
| :--- | :--- |
|コンテンツID|商品のコンテンツIDを表示します。|
|コンテンツ|商品のコンテンツ件名を表示します。|
|定期購読者|「一覧表示」をクリックすると[定期購入管理](/ja/docs/management/ec-regular-product-edit/)へ遷移します。|
|商品ID|商品IDが表示されます。|
|商品|商品名（SKU件名）が表示します。|
|商品種別|商品種別が表示します。|
|自動継続|この商品が自動継続かどうかを表示します。|
|定期購入者数|この商品を定期購入しているユーザーの人数を表示します。|

## 関連ドキュメント
- [定期購入管理](/ja/docs/management/ec-regular-product-edit/)
- [定期購入一覧](/ja/docs/management/ec-regular-product-list/)
- [配送処理](/ja/docs/management/ec-regular-product-delivery/)
- [商品設定](/ja/docs/management/ec-product-edit/)


---

# 配送処理

> 元ページ: `management/ec-regular-product-delivery` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-regular-product-delivery/

配送処理では現在、定期購入されている商品の配送処理ができます。

## 確認方法
[EC]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[定期購入管理]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/8931a6459e484f34ea5b0ff29b653686.png)

定期購入一覧のページから更新をしたいコンテンツの[配送処理]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/bc1e84f6eeea9a307a5c18c599491ab2.png)

## 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f73144cd75122d24b5ed9d159f046946.png)

### 配送対象注文一覧

|項目   |説明  |
| :--- | :--- |
|発送待ち件数|発送待ちの状態の注文件数を表示します。|
|発送準備中件数|発送準備中の状態の注文件数を表示します。|
|注文番号|注文番号を表示します。|
|商品名|商品のタイトルを表示します。|
|メンバーID|定期購入をしたメンバーのメンバーIDを表示します。|
|名前|定期購入をしたメンバーの名前を表示します。|
|ステータス|注文のステータスを表示します。|
|発送予定回数|発送予定の回数を表示します。|
|発送済回数|発送済の回数を表示します。|
|発送残回数|残りの発送回数を表示します。|

### 各ボタン

|項目   |説明  |
| :--- | :--- |
|発送準備|発送待ち状態の注文一覧を表示し、実行すると対象の注文を発送準備中にします。|
|発送完了|発送準備中状態の注文一覧を表示し、実行すると対象の注文を発送完了にします。|
|確認しました|状態の更新時、こちらにチェックが必要になります。|
|実行する|[発送準備]もしくは[発送完了]を選択し、[確認しました]にチェックを入れて[実行する]をクリックすると、注文の状態を更新します。|

### 履歴

|項目   |説明  |
| :--- | :--- |
|日付|操作を実行した日付を表示します。|
|操作|操作の内容(発送準備もしくは発送完了)を表示します。|
|操作者|操作を実行したメンバーを表示します。|
|対象人数|操作の対象となった人数を表示します。|
|CSVダウンロードする|[ダウンロード]をクリックすると操作の内容詳細をCSVでダウンロードします。|

## 関連ドキュメント
- [定期購入一覧](/ja/docs/management/ec-regular-product-list/)
- [定期購入管理](/ja/docs/management/ec-regular-product-edit/)
- [定期購入者一覧](/ja/docs/management/ec-regular-member-list/)
- [売上/配送管理](/ja/docs/management/ec-shipping-data-search/)


---

# 定期購入管理

> 元ページ: `management/ec-regular-product-edit` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-regular-product-edit/

定期購入管理では定期購入者の一覧表示と、定期購入されている商品の発送回数の編集ができます。

## 確認方法
[EC]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[定期購入管理]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8931a6459e484f34ea5b0ff29b653686.png)

定期購入一覧のページから更新をしたいコンテンツの[一覧に表示する]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/126111c2f41576ba5b6aa6cad2c0359a.png)

## 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5898810f252e1a06878278cbdd7b4e17.png)

### 定期購読情報詳細

|項目   |説明  |
| :--- | :--- |
|コンテンツID|定期購入商品のコンテンツIDを表示します。|
|コンテンツ|定期購入商品のタイトルを表示します。|
|注文者|商品の注文者を表示します。|
|注文番号|注文番号を表示します。|
|配送先|配送先を表示します。|
|商品ID|商品IDを表示します。|
|商品|商品のタイトルを表示します。|
|発送予定回数|発送予定回数を表示します。|
|発送回数|発送回数を表示します。|
|発送残回数|残りの発送回数を表示します。|
|配送状態|発送状態を表示します。<br/>[配送開始]もしくは[発送待ち解除]のボタンをクリックすると、配送状態を更新することができます。<br/>配送状態が配送待ちの商品は[配送処理](/ja/docs/management/ec-regular-product-delivery/)のページに表示されます。|

### 各ボタン

|項目   |説明  |
| :--- | :--- |
|更新|発送予定回数、発送済み回数に入力した内容を反映します。|
|CSVダウンロードする|定期購入の一覧をCSVでダウンロードします。<br/>「文字コード」より「Shitf-JIS」「UTF-8」が選択できます。|

## 関連ドキュメント
- [定期購入一覧](/ja/docs/management/ec-regular-product-list/)
- [配送処理](/ja/docs/management/ec-regular-product-delivery/)
- [定期購入者一覧](/ja/docs/management/ec-regular-member-list/)
- [商品設定](/ja/docs/management/ec-product-edit/)


---

# 定期購入一覧

> 元ページ: `management/ec-regular-product-list` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-regular-product-list/

定期購入一覧では現在、定期購入されている各商品の状態が確認できます。

## 定期購入一覧の確認方法
[EC]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)
ECメインメニューから[定期購入管理]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8931a6459e484f34ea5b0ff29b653686.png)

## 定期購入一覧の項目説明

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8f8c7bc041cfeddb062861349192a603.png)

|項目   |説明  |
| :--- | :--- |
|コンテンツID|定期購入商品のコンテンツID|
|コンテンツ|定期購入商品のタイトル|
|定期購入者数|現在商品を定期購入しているユーザーの数|
|定期購入者|定期購入者一覧へのリンク|
|配送処理|定期購入商品の配送処理を行う画面へのリンク|

## 関連ドキュメント
- [定期購入管理](/ja/docs/management/ec-regular-product-edit/)
- [配送処理](/ja/docs/management/ec-regular-product-delivery/)
- [定期購入者一覧](/ja/docs/management/ec-regular-member-list/)
- [商品設定](/ja/docs/management/ec-product-edit/)


---

# 売上ランキング

> 元ページ: `management/ec-sale-ranking` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-sale-ranking/

売上ランキングでは商品の売上ランキングを確認できます。

## 売上ランキングの確認方法
[EC]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[売上ランキング]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/36bb69f9060b56b43fa6f42a4d1626b4.png)

## 売上ランキングの項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/371db5b74bc3a4456e86d5ed788a9b03.png)

|項目   |説明  |
| :--- | :--- |
|集計期間|売上ランキングの集計を行う期間を設定します。|
|順位|順位を表示します。|
|商品名|商品名を表示します。|
|販売数|販売数を表示します。|

## 関連ドキュメント
- [売上集計](/ja/docs/management/ec-sale-total/)
- [売上/配送管理](/ja/docs/management/ec-shipping-data-search/)
- [注文一覧](/ja/docs/management/ec-order-list/)
- [ECメインメニュー](/ja/docs/management/ec/)


---

# 売上集計

> 元ページ: `management/ec-sale-total` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-sale-total/

売上集計では、[売上/配送管理](/ja/docs/management/ec-shipping-data-search/)画面で売上処理・配送処理を行った注文の一覧を確認できます。

## 売上集計の確認方法
[EC]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[売上集計]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/00058ab5f56648c32923251f524aea14.png)

## 売上集計の項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/53c8a2b09c9bfd3cc17d4c47009c07dc.png)

|項目   |説明  |
| :--- | :--- |
|期間|期間を設定します。|
|商品名/商品ID|「商品名」または「商品ID」を入力します。|
|集計種別|集計方法の種別を指定します。<br/>選択肢: 「売上集計」 (固定値)|
|定期購入/自動継続|「定期購入」または「自動継続」の条件を設定します。|
|キャンセル済みの注文を含める|キャンセル済みの注文を含める場合はチェックを入れます。|
|受注生産|[商品設定](/ja/docs/management/ec-product-edit/)画面で[受注生産]を設定した商品への注文を検索する場合にチェックを入れます。|
|検索|設定した条件で売上を検索します。|

## 売上一覧
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/fe22fa9db20fb84ce676110baf4b2293.png)

|項目   |説明  |
| :--- | :--- |
|注文番号|注文番号を表示します。|
|支払方法|注文の支払方法を表示します。|
|支払状態|注文の支払い状態を表示します。|
|キャンセル|キャンセル済みの注文の場合「○」を表示します。|
|注文日|注文日を表示します。|
|入金日|入金日を表示します。|
|売上(発送)日|売上日または商品の発送日を表示します。|
|商品ID|注文された商品のIDを表示します。|
|商品名|注文された商品の名称を表示します。|
|単価|注文された商品の単価を表示します。|
|数量|注文された商品の数量を表示します。|
|小計|注文情報の小計を表示します。|
|手数料|注文の手数料を表示します。|
|配送料|注文の配送料を表示します。|
|合計|注文の合計金額を表示します。|

## 関連ドキュメント
- [売上/配送管理](/ja/docs/management/ec-shipping-data-search/)
- [売上ランキング](/ja/docs/management/ec-sale-ranking/)
- [注文一覧](/ja/docs/management/ec-order-list/)
- [商品設定](/ja/docs/management/ec-product-edit/)


---

# クーポンコード ダウンロード

> 元ページ: `management/ec-serial-code-download` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-serial-code-download/

クーポンコード ダウンロードではクーポンコードの情報やクーポンコードの使用履歴をダウンロードできます。

## クーポンコード ダウンロードの確認方法
[EC]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[クーポンコード設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a0addcce8c0c6d7eee23f9e66bd8dc59.png)

クーポンコード設定のページから[クーポンコード ダウンロード]のタブをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/211bb4c943dcc1dbac0fc60056b81c48.png)

## クーポンコード ダウンロードの項目説明
### クーポンコード情報
抽出条件の[クーポンコード]のタブから、クーポンコード情報をダウンロードできます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f42e8080ca905549baf324b1c0af3152.png)

|項目   |説明  |
| :--- | :--- |
|有効期限|有効期限の範囲を指定します。|
|利用区分|利用区分を選択します|
|クーポンコード定義|クーポンコード定義を選択します。|
|対象商品|対象商品を選択します。|
|文字コード|ダウンロードする文字コードを指定します。|
|ダウンロードする|クリックすると指定した条件でクーポンコードをダウンロードします。|

### 使用履歴
抽出条件の[使用履歴]のタブから、クーポンコードの使用履歴をダウンロードできます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1b6e9d368d4db206f10f3550c0084341.png)

|項目   |説明  |
| :--- | :--- |
|有効期限|有効期限の範囲を指定します。|
|使用日|クーポンコード使用日の範囲を指定します。|
|クーポンコードグループ|クーポンコードグループを選択します。|
|対象商品|対象商品を選択します。|
|文字コード|ダウンロードする文字コードを指定します。|
|ダウンロードする|クリックすると指定した条件でクーポンコードの使用履歴をダウンロードします。|

## 関連ドキュメント
- [クーポンコード設定](/ja/docs/management/ec-serial-code-group-list/)
- [クーポンコード アップロード](/ja/docs/management/ec-serial-code-upload/)
- [クーポンコード一覧](/ja/docs/management/ec-serial-code-list/)
- [クーポンコード履歴](/ja/docs/management/ec-serial-code-history/)


---

# クーポンコード設定編集

> 元ページ: `management/ec-serial-code-group-edit` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-serial-code-group-edit/

クーポンコード設定編集ではクーポンコードの設定を編集できます。

## クーポンコード設定編集の確認方法
[EC]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[クーポンコード設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a0addcce8c0c6d7eee23f9e66bd8dc59.png)

クーポンコード設定のページから編集をしたいクーポンコードの[タイトル]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/40517b3a16cf4c7a020ef47e86fab046.png)

## クーポンコード設定編集の項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/899a280b5aeee542fa683c8b35e70e30.png)

|項目   |説明  |
| :--- | :--- |
|クーポンコード定義ID|クーポンコードのIDになります。クーポンコード設定追加時に自動で採番されます。|
|タイトル|クーポンコードのタイトルを入力します。|
|タイプ|クーポンコードのタイプを選択します。|
|値|クーポンのタイプがコードの場合、値引き額や値引き率を設定します。|
|有効期間|クーポンコードの有効期間を表示します。|
|無料期間|無料期間を表示します。|
|購入可能数|クーポンコードの利用できる回数を設定します。|
|対象商品|クーポンの対象となる商品を設定します。|
|会員登録時に利用する|会員登録時に利用する場合はチェックを入れます。|

## 更新するボタン、削除するボタン

|項目   |説明  |
| :--- | :--- |
|更新する|クリックするとクーポンコードの編集内容を反映します。|
|削除する|クリックすると表示しているクーポンコードを削除します。|

## 関連ドキュメント
- [クーポンコード設定](/ja/docs/management/ec-serial-code-group-list/)
- [クーポンコード一覧](/ja/docs/management/ec-serial-code-list/)
- [クーポンコード ダウンロード](/ja/docs/management/ec-serial-code-download/)
- [クーポンコード アップロード](/ja/docs/management/ec-serial-code-upload/)


---

# クーポンコード設定

> 元ページ: `management/ec-serial-code-group-list` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-serial-code-group-list/

クーポンコード設定ではKurocoに登録しているクーポンコード設定の一覧を確認できます。

## クーポンコード設定の確認方法
[EC]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[クーポンコード設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a0addcce8c0c6d7eee23f9e66bd8dc59.png)

## クーポンコード設定の項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f351c8f4246642f48f3b28996e311c60.png)

|項目   |説明  |
| :--- | :--- |
|タイトル|クーポンコードのタイトルを表示します。|
|タイプ|クーポンコードのタイプを表示します。|
|購入可能数|クーポンコードの利用できる回数を表示します。|
|有効期間|クーポンコードの有効期間を表示します。|
|対象ID|`対象商品`を設定した際にその商品ID、およびその商品へのリンクが表示されます。|
|会員登録|`会員登録時に利用する`にチェックを入れた場合に「有効」と表示されます。|
|発行数|発行済みのクーポンコード数（使用済みも含んだ累計）|
|クーポンコード一覧|クリックするとクーポンコードの発行や、発行済みのクーポンコード一覧を確認できるページ変遷移します。|

## 一括処理
一覧の左端のチェックボックスにチェックを入れて、[削除する]をクリックすると、選択したクーポンコード設定に対して一括で処理を行います。

## 関連ドキュメント
- [クーポンコード設定編集](/ja/docs/management/ec-serial-code-group-edit/)
- [クーポンコード一覧](/ja/docs/management/ec-serial-code-list/)
- [クーポンコード ダウンロード](/ja/docs/management/ec-serial-code-download/)
- [クーポンコード アップロード](/ja/docs/management/ec-serial-code-upload/)
- [クーポンコード履歴](/ja/docs/management/ec-serial-code-history/)


---

# クーポンコード履歴

> 元ページ: `management/ec-serial-code-history` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-serial-code-history/

クーポンコード履歴ではクーポンコードを利用した履歴の一覧を確認できます。

## クーポンコード履歴の確認方法
[EC]をクリックします。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d6d15d578a35db35c0f6d2f49fe75b6a.png?witdh=600)

ECメインメニューから[クーポンコード設定]をクリックします。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/2380ce77f812ff657d345858a2772cb1.png?witdh=600)

クーポンコード設定のページから確認をしたいクーポンコードの[クーポンコード一覧]をクリックします。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/c7430277d87848efbf0125cff007c036.png?witdh=600)

クーポンコード一覧のページから確認をしたいクーポンコードの[クーポンコード]をクリックします。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/f939d5aac3546af7c5ce6b140fe86a3c.png?witdh=600)

## クーポンコード履歴の項目説明
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/60b6a4ca2eae021b4c5854dc280593a6.png?witdh=600)

|項目   |説明  |
| :--- | :--- |
|商品ID|クーポンを利用して購入した商品のID|
|注文番号|クーポンを利用して購入した注文のID|
|数量|クーポンを利用して購入された商品の個数|
|処理日|クポーポンコード履歴に追加された日（購入日）|

## 一括処理
一覧の左端のチェックボックスにチェックを入れて、[削除する]をクリックすると、選択したクーポンコード履歴に対して一括で処理を行います。

## 関連ドキュメント
- [クーポンコード一覧](/ja/docs/management/ec-serial-code-list/)
- [クーポンコード設定](/ja/docs/management/ec-serial-code-group-list/)
- [クーポンコード ダウンロード](/ja/docs/management/ec-serial-code-download/)


---

# クーポンコード一覧

> 元ページ: `management/ec-serial-code-list` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-serial-code-list/

クーポンコード一覧ではクーポンコードの発行や、クーポンコードの一覧を確認できます。

## クーポンコード一覧の確認方法
[EC]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[クーポンコード設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a0addcce8c0c6d7eee23f9e66bd8dc59.png)

クーポンコード設定のページから編集をしたいクーポンコードの[クーポンコード一覧]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/047d7226e8195b93521bf87bafa1485f.png)

## クーポンコード作成
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3516d8594fb1969812a08863c1b38f73.png)

|項目   |説明  |
| :--- | :--- |
|発行数|クーポンコードを発行する数を入力します。|
|クーポンコードを発行|クリックするとクーポンコードを発行します。|

## クーポンコード一覧
### 検索
![Image from Gyazo](https://t.gyazo.com/teams/diverta/600941c64453c919d1417fe3b3bdde30.png)

|項目   |説明  |
| :--- | :--- |
|クーポンコード|クーポンコードを入力します。<br/>部分一致での検索になります。|
|メンバーID|メンバーIDを入力します。|
|利用区分|利用区分を選択します。|
|有効期限|有効期限の範囲を設定します。|
|使用済対象商品|対象商品を選択します。|
|検索|クリックすると設定した条件でクーポンコードを検索します。|

### クーポンコード一覧
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a295635099162579281b1f3a6af11afd.png)

|項目   |説明  |
| :--- | :--- |
|クーポンコード|クーポンコードを表示します。|
|利用区分|クーポンの利用状態を表示します。|
|有効期限|有効期限を表示します。|
|発行日|発行日を表示します。|

### 一括処理
一覧の左端のチェックボックスにチェックを入れて、[削除する]をクリックすると、選択したクーポンコードに対して一括で処理を行います。

## 関連ドキュメント
- [クーポンコード設定](/ja/docs/management/ec-serial-code-group-list/)
- [クーポンコード設定編集](/ja/docs/management/ec-serial-code-group-edit/)
- [クーポンコード履歴](/ja/docs/management/ec-serial-code-history/)
- [クーポンコード ダウンロード](/ja/docs/management/ec-serial-code-download/)
- [クーポンコード アップロード](/ja/docs/management/ec-serial-code-upload/)


---

# クーポンコード アップロード

> 元ページ: `management/ec-serial-code-upload` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-serial-code-upload/

クーポンコード アップロードではクーポンコードをCSVで一括アップロードできます。

## クーポンコード アップロードの確認方法
[EC]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[クーポンコード設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a0addcce8c0c6d7eee23f9e66bd8dc59.png)

クーポンコード設定のページから[クーポンコード アップロード]のタブをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/fe1d608781f9e687f459c1ea1a524c8a.png)

## クーポンコード アップロードの項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/21f64396a9e883200815cbfe868e6668.png)

|項目   |説明  |
| :--- | :--- |
|csvファイル|アップロードするCSVファイルを登録します。CSVファイルの雛形はクーポンコード ダウンロードからダウンロードできます。|
|クーポンコード重複時の動作|クーポンコードが重複した場合の動作を選択します。<li>全ての取り込みを停止</li><li>重複したものを無視</li><li>上書き保存</li>|
|アップロードする|クリックすると選択したCSVの情報でクーポンコードをアップロードします。|

## CSVについて
**※CSVのフォーマットは「クーポンコードダウンロード」から取得してください**  
**※「対象商品」、「数量」、「有効期限」、「最終更新日」の各項目はアップロード時には無視されます。**

|項目   |説明  |
| :--- | :--- |
|クーポンコード|対象クーポンコードです、新規登録時には既に発行されているものと重複しない文字列を指定してください。<br/>既に発行済みのコードと重複した場合は`クーポンコード重複時の動作`の選択に従って処理が行われます。<br/>尚、クーポンコードの長さはデフォルト設定では16文字です。|
|クーポンコード定義ID|対象クーポンコードの「クーポンコード定義ID」を指定してください。![Image from Gyazo](https://t.gyazo.com/teams/diverta/7502dec92b459f00b9a695700019be34.jpg?witdh=600)|
|発行日|クーポンコードを登録日付です。|

## 関連ドキュメント
- [クーポンコード ダウンロード](/ja/docs/management/ec-serial-code-download/)
- [クーポンコード設定](/ja/docs/management/ec-serial-code-group-list/)
- [クーポンコード一覧](/ja/docs/management/ec-serial-code-list/)
- [クーポンコード設定編集](/ja/docs/management/ec-serial-code-group-edit/)


---

# 売上/配送管理

> 元ページ: `management/ec-shipping-data-search` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-shipping-data-search/

売上/配送管理では入金済みの注文の確認と、売上処理、発送処理ができます。

## 売上/配送管理の確認方法
[EC]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[売上/配送管理]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e83db2966acc7830a22a0b931e6f4e9a.png)

## 売上/配送管理の項目説明
### 検索条件設定

売上/配送処理を行う対象の注文情報を検索できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b4c31a8e34ea794498d1c3cc79ca97fa.png)

|項目   |説明  |
| :--- | :--- |
|発送予定日|発送予定日を設定します。|
|商品名/商品ID|商品名/商品IDを入力します。|
|定期購入/自動継続|定期購入/自動継続の条件を設定します。|
|キャンセル済みの注文を含める|キャンセル済みの注文を含める場合はチェックを入れます。|
|受注生産|[商品設定](/ja/docs/management/ec-product-edit/)画面で[受注生産]を設定した商品への注文を検索する場合にチェックを入れます。|
|文字コード|文字コードの条件を設定します。|
|検索する|設定した条件で売上/配送を検索します。|
|CSVダウンロードする|設定した検索条件で売上/配送一覧をCSVダウンロードします。|

### 売上/配送一覧

売上/配送処理を行う対象の注文一覧を表示します。  
[注文情報編集](/ja/docs/management/ec-order-edit/)画面で、支払い状態が「決済完了」に設定されている注文が表示の対象となります。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/407154c98d07c2476f8620f7c1ef4c86.png)

|項目   |説明  |
| :--- | :--- |
|売上|チェックを入れて[売上のみ]をクリックすると売上処理をします。|
|注文番号|注文番号を表示します。<br/>クリックすると注文情報編集のページへ遷移します。|
|注文日|注文日を表示します。|
|売上日|売上日を表示します。|
|支払種別|支払種別を表示します。|
|配送先|配送先を表示します。|
|配送希望|配送希望を表示します。|
|発送|チェックを入れて[発送のみ]をクリックすると発送処理をします。|
|配送番号|配送番号を表示します。番号は自動で採番されます。|
|配送状態|配送状態を表示します。|
|発送予定日|発送予定日を入力します。|
|商品番号|商品番号を表示します。<br/>クリックすると商品設定のページ変遷移します。|
|商品名|商品名を表示します。|
|個数|個数を表示します。|

### 各ボタンの説明

|項目   |説明  |
| :--- | :--- |
|売上+発送|クリックするとチェックを入れた注文に対して、売上処理と発送処理をします。|
|売上のみ|クリックするとチェックを入れた注文に対して、売上処理をします。|
|発送のみ|クリックするとチェックを入れた注文に対して、発送処理をします。|
|更新する|クリックすると発送予定日の情報を更新します。|

## 関連ドキュメント
- [注文一覧](/ja/docs/management/ec-order-list/)
- [注文情報編集](/ja/docs/management/ec-order-edit/)
- [商品設定](/ja/docs/management/ec-product-edit/)
- [ECメインメニュー](/ja/docs/management/ec/)
- [管理画面よりECの設定を行う](/ja/docs/tutorials/ec-management/)


---

# 店舗情報設定

> 元ページ: `management/ec-shopmaster-edit` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-shopmaster-edit/

店舗情報設定では店舗情報、EC関連メールアドレス、購入時のルール、決済サービスなどの設定ができます。

## 店舗情報設定の確認方法
[EC]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[店舗情報設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/097a83d40812f8bd4945031879349597.png)

## 店舗情報設定の項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9af1171fd7eb12d6ca4784486fb851a6.png)

|項目   |説明  |
| :--- | :--- |
|会社名|会社名を入力します。|
|商品注文受付（管理者宛）Eメールアドレス|注文があった際に管理者宛に送信されるメールアドレスを設定します。|
|通貨|通貨を設定します。|
|おまとめ配送|おまとめ配送を利用するか設定します。<br/>おまとめ配送を利用すると通常配送商品を購入した際に販売方法が異なる商品でも同一注文になります。|
|送料無料条件|送料無料の条件を設定します。|
|送料計算方法|送料の計算方法を選択します。|

## 決済代行サービス設定
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/af10f0a279016390c7ab059773c40188.png)

|項目   |説明  |
| :--- | :--- |
|決済代行サービス情報|決済代行を行うサービスを選択します。<br/>利用できるサービスと決済方法は[決済代行サービスについて](#決済代行サービスについて)をご確認ください。|

## 更新するボタン
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/62afaf16a1066f0daf10874d7e098ded.png)

|項目   |説明  |
| :--- | :--- |
|更新する|クリックすると店舗情報の更新内容を反映します。|

## 決済代行サービスについて
### 決済代行サービス未使用
決済代行サービスを利用せずに銀行振込などのみで入金処理を行う場合はこちらを選択します。

#### 利用可能な決済サービス

- 支払い無し
- 銀行振込
- 後払い
- 代引き
- マニュアル決済

### Paygent
[Paygent](https://www.paygent.co.jp/)を利用して決済代行を行う場合はこちらを選択します。  
『Paygent（開発用）』を選択すると[試験環境接続キット]で提供されている試験環境への接続となります。本番サイト・検証サイトが異なる場合に検証サイトの設定をこちらにすることでテストが行なえます。

#### 利用可能な決済サービス

- 支払い無し
- クレジットカード
- コンビニ決済
- 月次クレジットカード
- 銀行振込
- 後払い
- 代引き
- マニュアル決済

#### Paygent設定例
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/3fe4559ffe1b09b464be10c2c45f6f9e.png)

|項目   |説明  |
| :--- | :--- |
|マーチャントID|PaygentのマーチャントIDを入力します。|
|マーチャント名|任意のマーチャント名を入力します。（全角）|
|ファイル決済通知ハッシュ値生成キー|※ファイル決済を利用する場合のみ設定が必要<br/>Paygentのファイル決済通知ハッシュ値生成キーを入力します。|
|差分通知ハッシュ値生成キー|Paygentの差分通知ハッシュ値生成キーを入力します。|
|トークン生成鍵|Paygentのトークン生成鍵を入力します。|
|トークン受取ハッシュ鍵|必要に応じてクレジットカードトークン生成時の改ざんチェックに利用します、詳細はPaygentマニュアルの<br/>02_PG外部インターフェース仕様説明書（トークン決済）.pdf<br/>を参照してください。|
|接続ID|Paygentの接続IDを入力します。|
|接続IDパスワード|Paygentの接続IDパスワードを入力します。|
|クライアント証明書|Paygentの「本番環境接続キット」もしくは「試験環境接続キット」内のサーバー用クライアント証明書に入っているpemファイルをアップロードします。|

## 関連ドキュメント
- [支払方法設定](/ja/docs/management/ec-paymenttype-list/)
- [販売方法設定](/ja/docs/management/ec-delivery-list/)
- [ECメインメニュー](/ja/docs/management/ec/)
- [管理画面よりECの設定を行う](/ja/docs/tutorials/ec-management/)
- [Paygentと連携するには](/ja/docs/tutorials/ec-paygent/)
- [EC決済方法別設定](/ja/docs/reference/ec-paymet-setting/)


---

# SKU設定

> 元ページ: `management/ec-sku-setting` ｜ 公式ページ: https://kuroco.app/ja/docs/management/ec-sku-setting/

SKU設定では、SKUの雛形となる情報を設定できます。

Kurocoではコンテンツを商品として扱い、SKUをコンテンツに紐付けて管理します。
SKU設定とSKUの関係は、コンテンツ定義とコンテンツの関係に似ています。
コンテンツ定義で各コンテンツの拡張項目を設定するのと同様に、SKU設定では各SKUの拡張項目などを設定します。
SKU設定は必ず1つのコンテンツ定義に関連付けられます。


データ概念は以下のようになります。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/ff140004c5800f74139488f4719e4c14.png)

## SKU設定の確認方法
### まだSKU設定が追加されてい無い場合
[EC]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[SKU設定を追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e7ccf54f111dab9924e5e8a28f5ddf05.png)

### 既にSKU設定が追加されている場合
[EC]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1858974bdfd209b0717e16ed7a5d4e3d.png)

ECメインメニューから[EC]をクリックし、表示されたプルダウンから[SKU設定一覧]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/24d3861b937f84b73fe7b5238d868fff.png)

SKU設定一覧のページから右上の[＋追加]をクリックするか、編集したいSKU設定の[設定]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/51926c3975ee1fa1358207d036f15e39.png)

## SKU設定の項目説明

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0a6157443bdd9883202ac7a685d6aaeb.png)

|項目   |説明  |
| :--- | :--- |
|SKU設定名|SKU設定の名前を入力します。|
|コンテンツ定義|紐づけるコンテンツ定義を選択します。|
|有料会員グループ|有料会員サイトにおける会員プランなどの商品を定義する場合はチェックを入れます。|

## SKU 拡張項目

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/c135ada3cb62965ecfe59fda4dcbec4b.png)

|項目   |説明  |
| :--- | :--- |
|ID|拡張項目のIDです。自動採番されます。|
|親項目|作成した項目に親項目を指定する場合はこちらを利用します。|
|項目名、注釈|項目の名称と注釈を入力できます。注釈には、項目についてのメモや注意書きなどを記入できます。|
|設定項目|設定項目を選択します|
|並び順(大きい方が上)|拡張項目の並び順を指定します。数が大きいものが上に表示されます。|

## 詳細設定

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/71a94df59e79d240aa169712cc01f5ad.png)

|項目   |説明  |
| :--- | :--- |
|閲覧制限|作られたSKU設定を見ることができるグループを選択します。<br/>閲覧を「許可する」設定です。|
|編集制限|SKU設定を編集できるグループを選択します。<br/>編集を「許可する」設定です。|

## 公開設定

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4b10970a648e1ffa92cb5a89c4000f89.png)

|項目   |説明  |
| :--- | :--- |
|公開にする|SKU設定を公開します。|
|非公開にする|SKU設定を非公開にします。|
|公開日指定|開始日付、終了日付を任意に指定してSKU設定を公開します。|

## 追加するボタン、更新コメント

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ff476b3fac0633f5c7fdf10413fca2cd.png)

|項目   |説明  |
| :--- | :--- |
|追加する|SKU設定の変更を反映します。|
|更新コメント|SKU設定を更新する際にコメントを残すことができます。|

## 関連ドキュメント
- [SKU設定一覧](/ja/docs/management/ec-product-group-list/)
- [SKU一覧](/ja/docs/management/ec-combination-list/)
- [商品設定](/ja/docs/management/ec-product-edit/)
- [コンテンツ定義](/ja/docs/management/content-structure-topics-group/)
- [管理画面よりECの設定を行う](/ja/docs/tutorials/ec-management/)
