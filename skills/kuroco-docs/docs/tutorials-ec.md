# Kurocoドキュメント: チュートリアル / EC・決済

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- ECサイト構築に必要なAPIの設定を行う（`ec-api`）
- ECサイトを作成する フロントエンドを作成する（`ec-front-end`）
- 管理画面よりECの設定を行う（`ec-management`）
- Paygentと連携するには（`ec-paygent`）
- Paygentで3Dセキュアを使用する（`ec-using-3d-secure-with-paygent`）
- EC機能 API設定とSwagger UIを利用した動作確認の方法（`how-to-use-purchase-by-swagger`）
- Stripeと連携して有料会員の機能を実装する。（`subscription-billing-with-stripe`）


---

# ECサイト構築に必要なAPIの設定を行う

> 元ページ: `tutorials/ec-api` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/ec-api/

Kurocoを利用してECサイトを作成する方法を、具体的な手順で説明します。
サイト構築には大きく3つの作業・設定が必要です。

1. [管理画面よりECの設定を行う](/ja/docs/tutorials/ec-management/)
2. ECサイト構築に必要なAPIを設定する（本ページ）
3. [フロントエンドを作成する](/ja/docs/tutorials/ec-front-end/)

本チュートリアルでは、ECサイト構築の際に必要であるAPI設定の方法を説明します。

## 前提
ECの購入は、ログイン後に行う前提です。
そのため、ページではECのAPI設定と合わせて関連するログイン・プロファイル情報取得用のAPI設定も記載します。
ログイン実装の説明については本チュートリアルでは省略しますので、[KurocoとNuxt.jsで、ログイン画面を構築する](/ja/docs/tutorials/integrate-login/)にてご確認ください。

## エンドポイント一覧

今回作成するエンドポイントは下記です。

|項目|エンドポイント パス|サンプルVueファイル|
|---|---|---|
|ログイン|login|-|
|注文者情報取得|profile|product_list.vue<br/>purchase.vue|
|商品一覧取得|product-list|product_list.vue|
|カートに追加|add-cart|product_list.vue|
|カートの内容を取得|`cart-items/{ec_cart_id}`|product_list.vue <br/> purchase.vue|
|商品を購入|purchase|purchase.vue|

:::tip
サンプルVueファイルはこの後の[フロントエンドを作成する](/ja/docs/tutorials/ec-front-end/)で作成するページのVueファイル名になります。
:::

## APIの作成
まずはAPIを作成します。今回は、「EC」というAPIを作成します。
API画面より[新しいAPIを作成する]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/e4450d463c64c0ff496d7be38eaa1822.png)

下記入力し、[追加する]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/5c6b69e08a69dde857ac287ceebf21a1.png)

|項目   |内容  |
| :--- | :--- |
|タイトル|EC|
|版|1|
|ディスクリプション|EC用のAPI|

## エンドポイントの作成
次にエンドポイントを作成します。
先ほど作成したECのAPI画面より、[Configure Endpoint]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/c59fc36923f9c764e164f4826971a2a1.png)
エンドポイント作成画面が表示されます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/31e6a117688a65e08caddf16b7729949.png)
こちらから、下記エンドポイントを作成します。


### ログイン  

ログイン処理を行います。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/95769a2feb37b52769abcdafeeca79c1.png)

|項目   |内容  |
| :--- | :--- |
|パス|login |
|カテゴリー|認証 |
|モデル|Login|
|オペレーション|login_challenge|

#### サンプルリクエスト
```
{
  "email": "test@example.co.jp",
  "password": "test_password",
  "login_save": 0
}
```
|キー|説明|
|---|---|
|email|ログインするメンバーのメールアドレス|
|password|ログインするメンバーのパスワード|
|login_save|ログイン状態を保持するか否か（保持する場合は1を指定）|

#### サンプルレスポンス
```
{
  "grant_token": "(省略)",
  "status": 0,
  "member_id": 123,
  "info": {
    "validUntil": 1633945168
  },
  "messages": [],
  "errors": []
}
```

### 注文者情報取得 

ログイン後にカートIDやメンバー情報を取得します。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/f611eed2ee4e9708843616fc5554ee01.png)

|項目   |内容  |
| :--- | :--- |
|パス|profile |
|カテゴリー|認証 |
|モデル|Login|
|オペレーション|profile|
|Parameters：basic_info|name1<br/>name2<br/>zip_code<br/>tdfk_cd<br/>address1<br/>address2<br/>address3<br/>tel<br/>email|

#### サンプルレスポンス
```
{
  "name1": "テスト",
  "name2": "太郎",
  "zip_code": "1234567",
  "tdfk_cd": "03",
  "address1": "住所(市区町村)",
  "address2": "丁目番地",
  "address3": "建物名",
  "tel": "09022223333",
  "email": "test@example.co.jp",
  "member_id": 123,
  "group_ids": {
    "102": "Login User"
  },
  "shash": "(省略)",
  "expiresAt": 1633945233,
  "ec_cart_id": 1000,
  "ec_point": 1,
  "ec_temp_point": 150
}
```

### 商品一覧取得　

本APIで商品のコンテンツデータ、商品アイテムデータが取得できます。
filter機能を利用した検索にも対応しています。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/7783df5529134a764ca40b1a5741e984.png)

|項目   |内容  |
| :--- | :--- |
|パス|product-list |
|カテゴリー|EC |
|モデル|ECProduct|
|オペレーション|list|
|Parameters：topics_group_id|（対象のコンテンツ定義のグループIDを指定）|

:::tip
コンテンツ定義のグループIDは、Kuroco管理画面の[コンテンツ定義](/ja/docs/management/content-structure-topics-group/)より確認できます。
:::

#### サンプルレスポンス
```
  "list": [
    {
      "product_id": 41205,
      "ymd": "1970-01-01",
      "subject": "PHP Development\t- Paperback",
      "link_url": "",
      "open_flg": 1,
      "inst_ymdhi": "2020-06-19 17:42:18.033674+09",
      "update_ymdhi": "2020-11-04 20:48:26.468659+09",
      "product_group_id": 11,
      "ext_col_01": "",
      "topics_id": 7,
      "combination_id": 235,
      "stock": 3978,
      "stock_unlimited": 0,
      "sale_limit": 0,
      "sale_unlimited": 1,
      "price_01": "0",
      "price_02": "2500",
      "set_product_ids": "",
      "release_ymdhi": null,
      "delivery_type": 255,
      〜略〜
      "product_data": {
        "topics_id": 7,
        "season": 2016,
        "ymd": 0,
        "contents_type": 6,
        "contents": "<img class=\"img-responsive\" src=\"/files/user/201512070955_1.jpg\"><br/>\r\n<br/>\r\n画面サイズを小さくするとレイアウトが変わります。",
        "subject": "PHP Development",
        "topics_flg": 1,
        "open_flg": 1,
        "regular_flg": 0,
        "inst_ymdhi": "2016-06-09T12:28:31+09:00",
        "update_ymdhi": "2020-06-19T17:09:39+09:00",
        "topics_group_id": 5,
        "ext_col_01": "",
        〜略〜
      },
      "combination_name": "Paperback",
      "class_options": {
        "16": {
          "ec_class_id": 16,
          "ec_class_option_id": 44,
          "label_nm": "Paperback"
        }
      },
      "order_list": []
```


### カートに追加

カートIDを指定して商品をカートに追加します。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/6107181456e5c4e2ebccb273e7944cba.png)

|項目   |内容  |
| :--- | :--- |
|パス|add-cart |
|カテゴリー|EC |
|モデル|ECCart|
|オペレーション|add|

#### サンプルリクエスト
```
{
  "ec_cart_id": 1000,
  "item": {
    "product_id": 41205,
    "quantity": 1
  }
}
```
|キー|説明|
|---|---|
|ec_cart_id|カートID|
|item.product_id|商品アイテムID|
|item.quantity|個数|

#### サンプルレスポンス
```
{
  "messages": [
    "新規追加しました。"
  ],
  "errors": []
}
```

### カートの内容を取得

現在のカートの内容を取得します。  

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/68f693f7ce0206f7dd8f76dc5b6bde02.png)

|項目   |内容  |
| :--- | :--- |
|パス|`cart-items/{ec_cart_id}` |
|カテゴリー|EC |
|モデル|ECCart|
|オペレーション|details|

#### サンプルレスポンス
```
{
  "messages": [],
  "errors": [],
  "details": {
    "ec_cart_id": 1000,
    "items": [
      {
        "product_id": 41205,
        "quantity": 1
      }
    ],
    "subtotal": 2500,
    "deliv_fee": 200,
    "total": 2700,
    "total_quantity": 1
  },
  "payment_list": {
    "59": {
      "payment_type": "Bank transfer",
      "payment_method": 4,
      "use_link_type": false,
      "use_token": false
    }
  }
}
```

:::tip
payment_list にはカートに入っている商品アイテムで共通に利用出来る支払方法の情報が格納されています。
:::

### 商品を購入

カートに入れた商品を購入するためのAPIです。
各決済方法別にリクエストサンプルと注意事項を記載します。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/c75c362f3efd067be9c3bbf9edddbcb7.png)

|項目   |内容  |
| :--- | :--- |
|パス|purchase |
|カテゴリー|EC |
|モデル|ECOrder|
|オペレーション|purchase|

#### サンプルリクエスト

```
{
  "ec_cart_id": 0,
  "order_products": {},
  "product_id": 0,
  "quantity": 0,
  "ec_payment_id": 1,
  "discount": {
    "point": 0,
    "serial_code": "string"
  },
  "shipping_address": {
    "name1": "",
    "name2": "",
    "zip_code": "000",
    "tdfk_cd": "",
    "address1": "",
    "address2": "",
    "address3": "",
    "tel": ""
  },
  "sp_career_info": {
    "sp_career": 1,
    "open_id": "string",
    "return_url": "string",
    "cancel_url": "string",
    "other_url": "string",
    "outline": "string"
  },
  "orderer": {
    "name1": "string",
    "name2": "string",
    "zip_code": "000",
    "tdfk_cd": "01",
    "address1": "string",
    "address2": "string",
    "address3": "string",
    "tel": "string",
    "email": "email@example.com"
  },
  "card_token": "string",
  "order_note": "string",
  "validate_only": false
}
```

|キー名|説明|
|---|---|
|ec_cart_id|カートID<br/>ログイン済みの場合はprofile APIから取得可能<br/>未ログインの場合は0を指定|
|order_products|カートを利用せず、APIリクエスト時に購入商品を直接指定する場合に利用する(※)|
|product_id|カートを利用せず、APIリクエスト時に購入商品を直接指定する場合に利用する(※)|
|quantity|カートを利用せず、APIリクエスト時に購入商品を直接指定する場合に利用する(※)|
|ec_payment_id|`支払い方法ID`を設定してください<br/>一般的には、商品に紐付く「販売方法」を取得後、その中から選択された対象の支払い方法に対応するIDを指定することになります|
|shipping_address|配送先情報<br/>ログイン済みで未入力の場合はログイン社の情報が設定されます|
|orderer|注文者情報<br/>ログイン済みで未入力の場合はログイン社の情報が設定されます|
|order_note|注文時メモ|
|validate_only|入力チェックのみを行い、実際の決済・購入処理は行いたくない場合はtrueを設定してください|

以上でAPIの作成完了です。

:::tip
エンドポイント項目の詳細な説明は、[エンドポイント 設定項目一覧](/ja/docs/reference/endpoint-settings/)を参照ください。
:::

次に、フロントエンドを設定します。[フロントエンドを作成する](/ja/docs/tutorials/ec-front-end/)をご確認ください。

## 関連ドキュメント
- [管理画面よりECの設定を行う](/ja/docs/tutorials/ec-management/)
- [ECサイトを作成する フロントエンドを作成する](/ja/docs/tutorials/ec-front-end/)
- [ログイン画面を構築する](/ja/docs/tutorials/integrate-login/)
- [EC機能 API設定とSwagger UIを利用した動作確認の方法](/ja/docs/tutorials/how-to-use-purchase-by-swagger/)
- [エンドポイント 設定項目一覧](/ja/docs/reference/endpoint-settings/)
- [ECのAPIでカード決済を行うには？](/ja/docs/faq/how-can-i-get-card-token/)


---

# ECサイトを作成する フロントエンドを作成する

> 元ページ: `tutorials/ec-front-end` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/ec-front-end/

Kurocoを利用してECサイトを作成する方法を、具体的な手順で説明します。
サイト構築には大きく3つの作業・設定が必要です。

1. [管理画面よりECの設定を行う](/ja/docs/tutorials/ec-management/)
2. [ECサイト構築に必要なAPIの設定を行う](/ja/docs/tutorials/ec-api/)
3. フロントエンドを作成する（本ページ）


## 作成するフロントページ一覧

今回作成するファイルは下記です。

|項目|ファイル名|内容|
|---|---|---|
|商品一覧ページ|product_list.vue|商品一覧の表示<br/>カート内容表示<br/>カートへの商品追加|
|商品購入ページ|purchase.vue|カート内容表示<br/>注文者情報入力<br/>支払い方法選択<br/>購入|


:::info
今回は商品一覧〜購入までのページのサンプルになりますが、実際にサイトを構築する際にはログインページ・会員登録ページなどが必要になります。
ログイン実装の説明については本チュートリアルでは省略しますので、[KurocoとNuxt.jsで、ログイン画面を構築する](/ja/docs/tutorials/integrate-login/)にてご確認ください。
:::

## フロントエンド実装
Nuxtインストールディレクトリに、下記構造にてファイル作成します。  
今回はpagesディレクトリ内にecディレクトリを作成し、その下に「product_list.vue」と「purchase.vue」ファイルを作成しました。

```
pages
 - ec
   - product_list.vue
   - purchase.vue
```

### 商品一覧ページの作成
まずは商品一覧ページを作成します。下記のように記載します。

```markup [product_list.vue]
<template>
    <div>
        <div>
        <h2 class="title">Cart items</h2>
        <div v-if="cartItems" class="box">
            <ul>
                <h3>購入商品</h3>
                <li class="cart-item" v-for="item in cartItems.items" :key="item.product_id">
                    <div class="product_id">ID: {{ item.product_id }}</div>
                    <div class="quantity">購入数: {{ item.quantity }}</div>
                </li>
            </ul>
            <ul>
                <h3>注文内容</h3>
                <li>
                    <div>配送料: {{ cartItems.deliv_fee }}</div>
                    <div>商品の小計: {{ cartItems.subtotal }}</div>
                    <div>合計: {{ cartItems.total }}</div>
                </li>
            </ul>
            <div>
                <NuxtLink to="/ec/purchase" class="btn">カートに進む</NuxtLink>
            </div>
        </div>
        <div v-else>まだカートにアイテムはありません。</div>
        </div>
        <div class="box">
            <h2 class="title">Product list</h2>
            <ul v-if="productList" class="ul">
                <li class="list-item" v-for="item in productList" :key="item.product_id">
                    <div class="title">商品名：{{ item.subject }}</div>
                    <div class="title">商品名：{{ item.subject }}</div>
                    <div class="price">価格：{{ item.price_02 }} 円</div>
                    <div class="cart btn" @click="addCart(item.product_id)">購入する</div>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    auth: false,
    async asyncData ({ $axios, params }) {
        try {
            const profile = await $axios.$get(process.env.BASE_URL + '/rcms-api/1/profile')
            let cartItems = {
                details: null
            }
            if (profile.ec_cart_id) {
                cartItems = await $axios.$get(process.env.BASE_URL + '/rcms-api/1/cart-items/' + profile.ec_cart_id)
            }
            const productList = await $axios.$get(process.env.BASE_URL + '/rcms-api/1/product-list')

            return {
                'cartItems': cartItems.details,
                'productList': productList.list
            }
        }catch (e) {
            console.log(e.message)
        }
    },
    data() {
        return {
            paymentId: {}
        }
    },
    methods: {
        async addCart(product_id) {
            const profile = await this.$axios.$get(process.env.BASE_URL + '/rcms-api/1/profile')
            const addItem = {
                ec_cart_id: profile.ec_cart_id,
                item: {
                    product_id: product_id,
                    quantity: 1
                }
            }
            const addCartResp = await this.$axios.$post(process.env.BASE_URL + '/rcms-api/1/add-cart', addItem)
            if (addCartResp.errors.length == 0) {
                alert('Success add cart')
                const cartListResp = await this.$axios.$get(process.env.BASE_URL + '/rcms-api/1/cart-items/' + profile.ec_cart_id)
                this.cartItems = cartListResp.details
            } else {
                alert(addCartResp.errors[0].message)
            }
        }
    }
}
</script>
<style scoped>
div.box{
border: solid 1px #ddd;
border-radius :8px;
padding: 10px;
margin:10px;
}

li {
  border-radius :8px;
  box-shadow :0px 0px 5px silver;
  padding: 0.5em 0.5em 0.5em 2em;
  margin: 20px;
}

.btn,
a.btn {
  color: #fff;
  background-color: #fd9535;
}
.btn:hover,
a.btn:hover {
  color: #fff;
  background: #fd9535;
}

a.btn--radius {
   border-radius: 100vh;
}
</style>
```

:::caution
上記サンプルコード内、「/rcms-api/1/…」の「1」にはご自身のAPIのIDをご記入ください。
:::

### 商品購入ページ
次に商品購入ページを作成します。下記のように記載します。

```markup [purchase.vue]
<template>
    <div>
        <div class="box">
            <h2 class="title">注文内容</h2>
            <ul v-if="cartItems">
                <div>配送料: {{ cartItems.deliv_fee }}</div>
                <div>商品の小計: {{ cartItems.subtotal }}</div>
                <div>合計: {{ cartItems.total }}</div>
                
                <li class="cart-item" v-for="item in cartItems.items" :key="item.product_id">
                    <div class="product_id">ID: {{ item.product_id }}</div>
                    <div class="quantity">購入数: {{ item.quantity }}</div>
                </li>
            </ul>
        </div>
        <div class="box">
            <h2 class="title">購入者情報</h2>
            <label for="cheese">お名前</label>
            <input name="name1" v-model="orderer.name1" /> <input name="name2" v-model="orderer.name2" /><br/>
            <label for="cheese">郵便番号</label>
            <input name="zip_code" v-model="orderer.zip_code" maxlength="7" minlength="7" /><br/>
            <label for="cheese">住所</label>
            <select name="tdfk_cd" v-model="orderer.tdfk_cd">
            <option value="">-- No selected --</option>
            <option value="01">北海道</option>
            <!-- 省略 -->
            <option value="13">東京都</option>
            <!-- 省略 -->
            <option value="47">沖縄県</option>
            </select><br/>
            <input name="address1" v-model="orderer.address1" /><br/>
            <input name="address2" v-model="orderer.address2" /><br/>
            <input name="address3" v-model="orderer.address3" /><br/>
            <label for="cheese">電話番号</label>
            <input name="tel" v-model="orderer.tel" /><br/>
            <label for="cheese">メールアドレス</label>
            <input name="email" v-model="orderer.email" /><br/>
        </div>
        <div class="box">
            <h2 class="title">支払い方法</h2>
            <div class="payment" >
                <span>お支払い方法を選択する >> </span>
                <select v-model="paymentId">
                    <option value="0">-- 選択する --</option>
                    <option v-for="(paymment_info, payment_id) in paymentList" :key="payment_id"
                        :value="payment_id"
                    >{{ paymment_info.payment_type }}
                    </option>
                </select>
            </div>
            <!-- Add credit card information entry forms, etc. as needed. -->
            <!-- 必要に応じてクレジットカード情報入力フォームなどを追加 -->
            <div @click="normalBuy()" class="cart btn">
                注文を確定する
            </div>
        </div>
    </div>
</template>

<script>
export default {
    auth: false,
    async asyncData ({ $axios, params }) {
        try {
            const profile = await $axios.$get(process.env.BASE_URL + '/rcms-api/1/profile')
            
            /*const profile = await $axios.$get('/profile')*/
            let cartItems = {
                details: null
            }
            let orderer = {}
            if (profile.ec_cart_id) {
                cartItems = await $axios.$get(process.env.BASE_URL + '/rcms-api/1/cart-items/' + profile.ec_cart_id)
                
                orderer.name1 = profile.name1
                orderer.name1 = profile.name2
                orderer.zip_code = profile.zip_code
                orderer.tdfk_cd = profile.tdfk_cd
                orderer.address1 = profile.address1
                orderer.address2 = profile.address2
                orderer.address3 = profile.address3
                orderer.tel = profile.tel
                orderer.email = profile.email
            }
            return {
                'cartItems': cartItems.details,
                'paymentList': cartItems.payment_list,
                'orderer': orderer
            }
        }catch (e) {
            console.log(e.message)
        }
    },
    data() {
        return {
            paymentId: 0
        }
    },
    methods: {
        async normalBuy() {
            if (!this.paymentId) {
                alert('Please select payment')
                return
            }
            const profile = await this.$axios.$get(process.env.BASE_URL + '/rcms-api/1/profile')
            if (!profile.ec_cart_id) {
                alert('No loggedin')
                return
            }
            const order = {
                ec_cart_id: profile.ec_cart_id,
                ec_payment_id: parseInt(this.paymentId),
                orderer: this.orderer
            }
            this.$axios.$post(process.env.BASE_URL + '/rcms-api/1/purchase ', order)
            .then((response) => {
                if (response.errors.length === 0) {
                    alert('Success purchase')
                    this.cartItems = null
                }
            })
            .catch((error) => {
                alert(error.response.data.errors[0].message)
            })
        }
    },
}
</script>
<style scoped>
```

:::caution
上記サンプルコード内、「/rcms-api/1/…」の「1」にはご自身のAPIのIDをご記入ください。
:::

## 画面確認
ファイルを保存し、`ec/product_list`へアクセスすると下記のような画面が表示されます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/0c592678561984b3b673fa749b6b8918.png)

[購入する]をクリックすると、カートにアイテムが保存されます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/10758cd5f9dfa4f6d25dd80a27ef906e.png)

[カートに進む]をクリックすると、注文内容の確認と購入者情報、支払い方法の登録画面が表示されます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/76c3cc69e0a9103fc8219b0c73050cda.png)

[注文を確定する]をクリックして購入完了となります。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/02658ab467d6620803a6b57a8e77e3ab.png)

以上で、商品の表示から購入まで対応可能となります。
今回はECの全体的な構造の説明のため、詳細な説明は省略していますが、クレジットカード決済や定期購入等も可能となります。

## 参考情報

### カートを利用せずに商品を購入する場合
今回のチュートリアルでは、銀行振込による決済、および商品の発送を伴う運用を想定していますのでカートに商品を追加し、購入というフローとなっていますが、有料会員の購入などカートを利用せずに商品を指定して購入処理を行いたい場合は『[カートを利用せずに直接商品を指定して購入するには？](/ja/docs/faq/how-can-i-purchase-without-cart/)』を参照してください

## 関連ドキュメント
- [管理画面よりECの設定を行う](/ja/docs/tutorials/ec-management/)
- [ECサイト構築に必要なAPIの設定を行う](/ja/docs/tutorials/ec-api/)
- [ログイン画面を構築する](/ja/docs/tutorials/integrate-login/)
- [EC機能 API設定とSwagger UIを利用した動作確認の方法](/ja/docs/tutorials/how-to-use-purchase-by-swagger/)
- [カートを利用せずに直接商品を指定して購入するには？](/ja/docs/faq/how-can-i-purchase-without-cart/)


---

# 管理画面よりECの設定を行う

> 元ページ: `tutorials/ec-management` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/ec-management/

Kurocoを利用してECサイトを作成する方法を説明します。
KurocoでECサイトを構築するには大きく3つの作業が必要です。

1. 管理画面よりECを設定する（本ページ）
2. [ECサイト構築に必要なAPIの設定を行う](/ja/docs/tutorials/ec-api/)
3. [フロントエンドを作成する](/ja/docs/tutorials/ec-front-end/)

本チュートリアルでは、Kuroco管理画面のECメニューより、店舗情報の設定方法と商品の追加方法を説明します。

## 店舗情報の設定
ECサイト構築にあたり、最初に下記情報を設定します。

|項目   |説明  |
| :--- | :--- |
|店舗情報|店舗の運営者情報を設定します。|
|支払い方法|購入時の支払い方法を設定します。|
|販売方法|商品の販売方法を設定します。|

### 店舗情報を設定する
[EC] -> [店舗情報設定]をクリックし、店舗情報設定ページに遷移します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7447683f223f35a68f9360b678b2bb66.png)

店舗情報設定のページで配送時の無料条件や決済サービス（Paygent）との連携設定を行います。  
今回は例として下記のように登録します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c2a5e520beb2932330f82124f0ef4cf0.png)

|項目   |内容  |
| :--- | :--- |
|会社名|株式会社Kuroco EC|
|商品注文受付（管理者宛）<br/>メールアドレス|`no-reply@example.com`|
|通貨|円|
|おまとめ配送|利用しない|
|送料無料条件|1000|
|送料計算方法|カート単位で計算|
|決済代行サービス情報|決済代行サービス未使用|

:::tip
店舗情報設定の詳細は[管理画面マニュアル -> 店舗情報設定](/ja/docs/management/ec-shopmaster-edit/)をご確認ください。  
:::

### 支払方法を設定する
[EC] -> [支払い方法設定]をクリックし、支払い方法設定一覧ページに遷移します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/dcb14a6fc1c1521916c647d1c62eb0f5.png)

[支払い方法設定一覧](/ja/docs/management/ec-paymenttype-list/)のページから[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/457c02934446973533e3046b64d60ffe.png)
  
ここでは下記のように銀行振込を設定し[追加する]をクリックします。  

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/af67cb8a46e88384670117a071779a15.png)

|項目   |内容  |
| :--- | :--- |
|支払種別|銀行振込|
|支払い方法|銀行振込|
|手数料|0|
|対象金額|0 〜 999999|
|並び順|未入力|

:::tip
支払方法設定の詳細は[管理画面マニュアル -> 支払方法編集](/ja/docs/management/ec-paymenttype-edit/)をご確認ください。  
:::

:::tip
今回のチュートリアルでは銀行振込による決済を利用するため、外部の決済サービスは使用しませんが、Kurocoではデフォルトの決済サービスとしてPaygentを利用出来ます。
Paygent設定の詳細は [Paygentと連携するには](/ja/docs/tutorials/ec-paygent/) をご確認ください。  
:::

### 販売方法を設定する
[EC] -> [販売方法設定]をクリックし、販売方法設定一覧ページに遷移します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5b56c6d6e23db01963bdfd87c53302cf.png)

販売方法設定一覧のページから[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/329fe7724d41580f6bdf6e29881b3746.png)
  
下記のように設定し[追加する]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/c5f2c1e100bb677826f801aaa3abd689.png)

|項目   |内容  |
| :--- | :--- |
|販売方法|一般商品|
|支払い方法|銀行振込|
|商品種別|宅配|
|サービス名／配送業者名|未入力|
|説明|未入力|
|サービス利用料／配送料|220|
|サービス利用料／配送料 (配送先別設定)|未入力|
|送料無料の対象に含めない|未入力|

:::tip
支払方法設定の詳細は[管理画面マニュアル -> 販売方法編集](/ja/docs/management/ec-delivery-edit/)をご確認ください。  
:::

以上で、店舗情報の設定が完了です。

## 商品の追加
ここからは販売商品の登録方法を説明します。
今回は「衣料品」と「靴」というSKUを設定し、それぞれ商品を追加する方法を説明します。

### コンテンツ定義・SKU設定を設定する
まずはSKUの設定をします。  
Kurocoでは商品はコンテンツ定義で設定し、値段や配送方法、在庫数の設定を商品設定で管理します。そのため、先にコンテンツ定義を設定します。  

:::tip
コンテンツ定義とSKU設定は1対1で紐付きます。
:::

コンテンツ定義のページから[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e5ca05b33f98348925bb0f3db12d55da.png)

「衣料品」のコンテンツ定義を追加します。今回は下記設定で追加し、[追加する]をクリックします。  

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/10e48029159c616fe13dae5c19d6813a.png)

|項目   |内容  |
| :--- | :--- |
|グループ名|衣料品|
|並び順| 1000|

:::tip
コンテンツ定義の詳細は[管理画面マニュアル -> コンテンツ定義編集](/ja/docs/management/content-structure-topics-group/)をご確認ください。  
:::

同様に「靴」のコンテンツ定義も追加します。  

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/2680df1b96c1e55d6beadfb4f9bba87f.png)

|項目   |内容  |
| :--- | :--- |
|グループ名|靴|
|並び順| 900|

以上で「衣料品」と「靴」のコンテンツ定義の追加ができました。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/dc2dbd89d5e7b5ddb6946b914dbfae44.png)

次に、SKUを設定します。  
[EC] -> [SKU設定を追加]をクリックし、SKU設定を追加ページに遷移します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2d2094ae8b44e04d9f54c6f65a062779.png)

今回は、先ほど作成したコンテンツ定義「衣料品」と紐付けてSKU設定を追加します。
今回は下記設定で追加し、[追加する]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/6cbd5238b397035e5c32c5eecaf34618.png)

|項目   |内容  |
| :--- | :--- |
|SKU設定名|衣料品|
|コンテンツ定義|衣料品|

:::tip
SKU設定の詳細は[管理画面マニュアル -> SKU設定](/ja/docs/management/ec-sku-setting/)をご確認ください。 
:::

以上で「衣料品」SKU設定完了です。  

同様に「靴」のSKU設定も追加し、SKU設定の追加は完了です。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/96bdd77f5492b8d91b61d557f358625c.png)

### SKUを追加する
次に商品アイテムを特定するSKUを追加します。  
今回のSKUは商品規格(色（赤、黒..）、サイズ（S、M、L...）)の組み合わせとします。 

[ECメインメニュー]より[EC]プルダウンをクリックし、[SKU設定一覧]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/96fb886235402559c3abe9b41bb2fe7d.png)

SKU設定一覧のページより「衣料品」の[設定]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c46c15c9a0392ce1004a1564df057d1c.png)

[SKU/規格]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b4b24e39ee6de96b1c3b310a7ccec0b9.png)

[規格を追加]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/9382b165384c14c80beb8e39f79ce22e.png)
商品規格編集ページが表示されるので、サイズに関する規格を追加します。  
今回は下記のように設定し、[追加する]をクリックします。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/62ff7215a0e358964affc0e482d0691c.png)

|項目   |内容  |
| :--- | :--- |
|規格名|サイズ|
|分類| Sサイズ<br/>Mサイズ<br/>Lサイズ|

同様にカラーに関する規格を追加します。今回は下記のように設定します。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/1800c7d6524339299867cd4196bc9bff.png)

|項目   |内容  |
| :--- | :--- |
|規格名|カラー|
|分類| ブラック<br/>ホワイト<br/>レッド|

規格が追加されたことを確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d53ebfe6ba94bef944a4d863f1774084.png)

:::tip
商品規格編集の詳細は[管理画面マニュアル -> 商品規格編集](/ja/docs/management/ec-class-edit/)をご確認ください。
::: 

次にSKUを追加します。[SKU追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2e2c1b8b3fc48d94c630ca5c0c04ef6a.png)

商品規格SKU編集ページが表示されるので、下記のように規格の組み合わせを設定し、[追加する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0f7e99874e5be2c8b8745906de61c37c.png)

|項目   |内容  |
| :--- | :--- |
|サイズ|Sサイズ|
|カラー|レッド|

同様に、必要なパターンだけSKUを追加します。  
SKUを追加すると[SKU一覧]にて下記のように確認ができます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a6c596b4e8b3d04d5e8c34c3326d33be.jpg)

:::tip
[商品企画編集](/ja/docs/management/ec-class-edit/)のページの[全てのSKUパターンを作成]のボタンや、[SKU一覧](/ja/docs/management/ec-combination-list/)のページの[CSVアップロード]もご活用ください。 
:::

「靴」に対しても同様の流れで規格とSKUを追加します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/451e8fc57847cdc360ffc59ca1a89c1e.png)

### 商品を追加する 
次に商品を追加します。Kurocoでは、1つのコンテンツに対して各SKUの商品を作ることができます。
商品設定では価格、配送方法、在庫数、DL商品の場合は電子データなどを設定します。

今回は下記のイメージにて商品を追加します。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/0812e7516e2704a31be7a1572f53352b.png)

コンテンツから[衣料品]をクリックし、右上の[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cf66c26857fd677a502d16524cec2572.png)

今回は下記のように記載し、[追加する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9122df3757ed50fa709792944ff0bfeb.png)

|項目   |内容  |
| :--- | :--- |
|タイトル|ジャケットA|

同様に「ジャケットB」「コートC」「コートD」を追加すると下記のように衣料品一覧が確認できます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ef1de3c4fca2631812a3151a85e4ed34.png)

次に商品(SKU)を追加します。
衣料品一覧でタイトルをクリックして、衣料品編集ページに遷移します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/98ff5667c0c7f1bc7d42b4e967c1b64e.png)

商品(SKU)の[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6693134f9d5d5a93198c2bbcb82ea4ea.png)

商品規格SKU編集のページに遷移します。規格(サイズ・カラー/)の組み合わせを設定して[追加する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/61d9411fb7ab5497043ea79e86ad145c.png)

商品設定編集のページに遷移します。今回は下記のように記載し、[追加する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/838cac26f4c38d363b2a56dcfbfe1bfe.jpg)

|項目   |内容  |
| :--- | :--- |
|商品名|ジャケットA_S_R|
|販売価格|10000|
|在庫数| 10|
|販売方法|一般商品|

同様に必要な商品を追加していきます。追加した商品は[商品一覧](/ja/docs/management/ec-product-list/)のページで確認ができます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/cf11839c102b53cbf29f638817f4cfcc.png)
「靴」も同様の流れで商品を追加します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ce6d59c37cf84cf2f68c5b49fca7b452.png)

以上で商品の登録が完了です。  

:::tip
商品設定の詳細は[管理画面マニュアル -> 商品設定](/ja/docs/management/ec-product-edit/)をご確認ください。 
:::

## メールの設定を行う
商品購入時、入金確認時、および商品発送時に購入者に対してメール通知を行いますので、そのメールの文面を設定します。  
[オペレーション] > [メッセージひな形]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/be3fdd5c65007a98fd554828930f3384.png)

### 購入完了メール（銀行振込）
注文申し込みが行われた際にお客様へ送信するメールの内容を変更します。

「購入完了メール（銀行振込）」のテンプレート名をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c0fab555b2109c42d5c45bc5241055ed.png)

編集画面が表示されます。
今回は銀行振込を利用するので、振込先の口座番号の記載や、振込記述等必要情報を追記してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bae46597c36b919c97f95099754ed7ef.jpg)

### 決済完了メール（銀行振込）
入金を確認した後お客様に送るメールの内容を変更します。

「決済完了メール（銀行振込）」のテンプレート名をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/17cd2ae0813f9f5ee7a7263d221a77bc.png)

編集画面が表示されますので文言などを変更して下さい。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/20d3afdb39c4a66340da30d4efdbc6a4.jpg)

お客様からの入金確認後、注文情報の`入金日時`部分にある「入金済みにする」にチェックを入れ、更新することで入金確認（決済完了）のメールを送ることが出来ます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/0da54661e780e176a8a2e52361b2139e.png)

### 商品発送メール(会員購入) 
商品を発送した際にお客様へ送るメールの内容を変更します。

「商品発送メール(会員購入)」のテンプレート名をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/463bf3f63926b49118b233511479034e.png)

編集画面が表示されますので文言などを変更して下さい。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d94d7ac266d79ec9b6bc9ed4bb92b5bd.png)

:::caution
今回会員制ECサイトを想定しているので「商品発送メール(会員購入) 」の変更となりますが、非会員による購入が可能な場合は「商品発送メール（ゲスト購入）」メールも合わせて変更して下さい。
:::

### メール送信方法について
メールの送信は「売上/配送管理」画面より対応します。
[EC] -> [売上/配送管理]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0eeaddd5b4eb9a767c290d95098bffaa.png)

「売上/配送管理」画面から「発送メールを送信する」を選択して配送処理を行うことで商品発送メールを送ることが出来ます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/32a3fdf08622a19e6328e09f0b3d8fbd.png)

以上で管理画面での設定が完了です。

次に、APIを設定します。[ECサイト構築に必要なAPIの設定を行う](/ja/docs/tutorials/ec-api/)をご確認ください。

## 関連ドキュメント
- [ECメインメニュー](/ja/docs/management/ec/)
- [店舗情報設定](/ja/docs/management/ec-shopmaster-edit/)
- [商品設定](/ja/docs/management/ec-product-edit/)
- [SKU設定](/ja/docs/management/ec-sku-setting/)
- [ECサイト構築に必要なAPIの設定を行う](/ja/docs/tutorials/ec-api/)
- [ECサイトを作成する フロントエンドを作成する](/ja/docs/tutorials/ec-front-end/)
- [Paygentと連携するには](/ja/docs/tutorials/ec-paygent/)


---

# Paygentと連携するには

> 元ページ: `tutorials/ec-paygent` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/ec-paygent/
> 概要: EC機能を利用した際に外部の決済サービスであるPaygentと連携する方法を説明します。

## 概要
EC機能を利用した際に外部の決済サービスであるPaygentと連携する方法を説明します。

## Paygent設定について  
クレジットカード決済など決済サービス（Paygent）を利用する場合は[Paygentの資料請求のページ](https://sandbox.paygent.co.jp/cgi-bin/contact_a3.cgi)から申し込みを行ってください。  
注) 銀行振込やマニュアル決済など決済サービスを利用しない決済方法のみの利用であればこちらの申し込みは不要です。

申込時の注意点は下記になります。  

|項目   |内容  |
| :--- | :--- |
|ご利用（予定）のシステム|「Kuroco」と記入をお願いします。|
|検討中の決済手段|Kurocoが対応している決済手段を選択してください。Kurocoが対応している決済手段は[店舗情報設定 利用可能な決済サービス](/ja/docs/management/ec-shopmaster-edit/#利用可能な決済サービス)を参照ください。|
|オプション申込について|「決済情報差分照会」、「決済情報差分通知」のオプション申し込みが必要になります。<br/>その際、「決済情報差分通知URL」には`(管理画面URL)/direct/ec/paygent_recv/`を指定し、「接続モジュール言語」には「PHP」を指定してください。<br/>また、「決済通知ステータス」には全てチェックを入れていただけますようお願いします。<br/>オプション申込の手続き方法はPaygentにお問い合わせください。|
|月次クレジットカード決済（継続課金）の利用|月次クレジットカード決済（継続課金）を利用の場合は、「カード情報お預かり機能」、「ファイル処理機能」、「カード情報更新機能(洗替_マニュアル)」 のオプションも合わせて必要です。<br/>また、「ファイル処理機能」の「クレジットカード決済」で「オーソリ」、「売上」、「カード情報更新（洗替）」を**利用する**に設定するようにしてください。|

お申込みが完了したら[Paygent管理画面](https://portal.paygent.co.jp/n/manage-m/login.html)の情報をKurocoの店舗情報設定画面に入力することでPaygentとの連携が行えます。  
詳細は[店舗情報設定のPaygent設定例](/ja/docs/management/ec-shopmaster-edit/#paygent設定例)をご参照ください。

## 関連ドキュメント
- [店舗情報設定](/ja/docs/management/ec-shopmaster-edit/)
- [Paygentで3Dセキュアを使用する](/ja/docs/tutorials/ec-using-3d-secure-with-paygent/)
- [管理画面よりECの設定を行う](/ja/docs/tutorials/ec-management/)
- [EC決済方法別設定](/ja/docs/reference/ec-paymet-setting/)


---

# Paygentで3Dセキュアを使用する

> 元ページ: `tutorials/ec-using-3d-secure-with-paygent` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/ec-using-3d-secure-with-paygent/
> 概要: EC機能を利用した際に外部の決済サービスであるPaygentとで3Dセキュアを利用する方法を説明します。

## 概要
Paygentと連携した決済で3Dセキュアを利用する方法を説明します。

## Paygent側の設定

### 3Dセキュア（EMV 3Dセキュア）に申し込む
まずは、3Dセキュア（EMV 3Dセキュア）に申し込んでください。
※3Dセキュア1.0には未対応です

### 「3Dセキュア結果受付ハッシュ鍵」を発行する
つぎに、申し込み設定完了メールに記との手順に従って「3Dセキュア結果受付ハッシュ鍵」を発行します。

> ▼リンクタイプでEMV 3Dセキュア（3Dセキュア 2.0）をご利用の場合
 システムタイプをリンクまたはリンク+モジュールでご利用頂いている加盟店様が
 EMV 3Dセキュア（3Dセキュア 2.0）をご利用される場合、
 ペイジェントオンラインから『３Dセキュア結果受付ハッシュ鍵』の生成が必要となります。
 （※ハッシュ鍵の生成がされていないと決済エラーが発生します。）
> 
> ３Dセキュア結果受付ハッシュ鍵の生成の方法については、下記となります。
 1. ペイジェントオンラインに管理ユーザにてログイン
 2. メンテナンス＞システム管理情報
 3. 3Dセキュア結果受付ハッシュ鍵　「鍵を作る」をクリック
 4. 3Dセキュア結果受付ハッシュ鍵が表示されます。
> 
> ※詳細はペイジェントオンラインマニュアル（P.218）５－ｃ．３Ｄセキュア結果受付ハッシュ鍵をご確認ください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b24fa2b8d680481959e042575466a0c5.jpg)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/012a90ef642c3bb4edd3a5c0916d73ff.png)

:::info
発行はPaygentオンラインから行えます。
詳しくは[加盟店サポートサイト](https://support.paygent.co.jp/faq/show/276?category_id=99&site_domain=default)をご確認ください。
::: 

## Kuroco側の設定
### 3Dセキュアの設定をする
ECの店舗情報設定に「3Dセキュア結果受付ハッシュ鍵」を設定します。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b732db5c3537a8ab88a2b45ad8f74302.png)


支払い方法設定からクレジットカード決済のオプションで3Dセキュアを利用するに設定します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d08a54f9743936faadb08cfbae8dac0f.png)


### APIにリクエストを送る
SKU等を作成し、`ECOrder::purchase`のエンドポイントに以下のリクエストします。

**JSON**
```json
{
  "product_id": 41201,
  "quantity": 1,
  "ec_payment_id": 58,
  "card_token": "tok_CY9YQzCwS8Efm1ngz6jM7cKr4a",
  "card_options": {
    "card_3dsec_return_url": "/order/3dsec/"
  }
}
```

**Curl**
```curl
curl -X 'POST' \
  'https://shibazaki-kuroco-dev.g.kuroco.app/rcms-api/1/ec/ordre' \
  -H 'accept: */*' \
  -H 'X-RCMS-API-ACCESS-TOKEN: d97aaaad1c068d596bd8d3dd37a75343d5d135827c89a434ac5b9c704a9305ab' \
  -H 'Content-Type: application/json' \
  -d '{
  "product_id": 41201,
  "quantity": 1,
  "ec_payment_id": 58,
  "card_token": "tok_CY9YQzCwS8Efm1ngz6jM7cKr4a",
  "card_options": {
    "card_3dsec_return_url": "/order/3dsec/"
  }
}'
```

:::info
card_3dsec_return_url には3Dセキュア認証後にリダイレクトさせたいフロントのURLを指定してください
:::

**レスポンス例**

```json
{
  "errors": [],
  "messages": [
    "注文が完了しました。"
  ],
  "ids": [
    1
  ],
  "ext_data": {
    "credit_card_3dsec_resp": {
      "out_acs_html": "<form name=\"submitForm\" action=\"https://・・・
    }
  }
}
```

:::caution
システム上、注文が分かれるような下記の組み合わせでの購入を行うとエラーとなります
個別に購入するようなフロント実装で対応をお願いします
- 通常商品とDL商品
- 発売済み商品と予約商品
- クーポン利用とクーポン利用ではない購入


```
{
  "errors": [
    {
      "code": "unprocessable_entity",
      "message": "3Dセキュアを利用している場合は配送・DLを1つにまとめる必要があります、予約商品や配送・DL商品が混ざっている場合は個別に注文してください。"
    }
  ],
  "x-rcms-request-id": "a32b81da-a923-410b-af1e-f1853343aca8"
}
```
:::

レスポンスの`out_acs_html`で、必要なHTMLが得られますので、こちらをフロント側で表示させてください。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fc63ce1ed65968e05e0563e39c4008a6.png)

:::tip
こちらはフロント側の処理で自動でsubmitさせるようにしても問題ありません
:::

:::caution
Paygentの仕様変更によりHTMLが変わる可能性があります。  
その場合はKuroco側の対応も必要になる可能性があります。  
:::

### ステータスの確認をする
このタイミングでは、Kuroco側の注文情報は便宜上決済失敗として扱っております管理画面から確認する際には「決済失敗を除く」のチェックを外して検索して下ださい。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/69221072f3689a8b454825779cb63c29.png)

「OK」を押して3Cセキュア認証画面で行う認証が問題無ければ注文情報は決済完了ステータスになります。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5d507172b84a5e938ac698f78112df03.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/16a20862b06c04f153598191552c16cb.png)

また、Paygentの管理画面からも認証状態が確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2b4ffadcc5d3e5796d12189558a0a773.png)

### 売上処理を行う
商品の発送などと同時に「売上/配送」画面から売り上げ処理を行います。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f9263530348f39a83841126c7c60752c.png)

:::info
配送を伴わない商品はこちらから売上処理を行わないパターンもあります。  
3Dセキュアの処理とは関係なくECサービスの共通処理なので詳細は割愛します。
:::

Paygentの管理画面から「消込済」になっていることを確認します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/23990e3ec0f627bf98c569a3a2eebbe5.png)

### エラー時の対応

- 3Dセキュア承認エラー、承認画面でのタイムアウト
  - 注文情報、もしくはPaygent管理画面からエラー内容が確認出来ます。
  - フロントページの戻りURLに「dsec_error=1」のクエリパラメータを付与してリダイレクトします。
  - 3Dセキュア認証が通った後にクレジットカードのオーソリに失敗した場合は管理者宛にメール送信するようにしています。（フロント実装によっては個別に対応をお願いします）
  
## 関連ドキュメント
- [Paygentと連携するには](/ja/docs/tutorials/ec-paygent/)


---

# EC機能 API設定とSwagger UIを利用した動作確認の方法

> 元ページ: `tutorials/how-to-use-purchase-by-swagger` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-use-purchase-by-swagger/

本チュートリアルでは、ECサイト構築の際、必要になるAPIの設定とSwagger UIを使った注文手順の確認方法を記載します。  
本手順では[EC機能 店舗情報の設定と商品登録の方法](/ja/docs/tutorials/ec-management/)のチュートリアルの設定が既に行われている前提となります。

## APIの作成
まずはEC用のAPIを作成します。  
APIのページから[新しいAPIを作成する]をクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/e065a41adaca8667b3c4da0adc6b0d58.png?witdh=600)
Title, Version, Descriptionを入力して[ADD]をクリックします。
今回は下記のように設定しました。

| 設定項目 | 設定           |  
| :------- | :------------- | 
| Title | EC API | 
| Version | 1 |
| Description | EC |

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/8512ce0dc495ae5f44a8136c00ce804b.png?witdh=600)
次にセキュリティの設定します。  
先ほど作成したAPIのページから[セキュリティ]をクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/b93b4383041ef8ead2dd91ee38bf97cc.png?witdh=600)
セキュリティをDynamic TokenもしくはCookieに設定します。  
今回はCookieに設定して進めて行くので、Cookieを選択し[Save]をクリックします。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/fd7b127d056d80b5ead4a98823ea9f52.png?witdh=600)
参考：セキュリティ設定については[API Security](/ja/docs/management/api-security/)を参照ください。


次にCORSの設定します。 
先ほど作成したAPIのページから[CORSを設定する]をクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/2f099b06209178f56c780379beb04775.png?witdh=600)
下記のように設定し、[Save]をクリックします。

|設定項目 |設定 |
| :--- | :---- |
|CORS_ALLOW_ORIGINS|<li>管理画面URL</li><li>フロントエンド ドメイン</li><li>ローカルドメイン(例：http://localhost:3000)</li>|
|CORS_ALLOW_METHODS|<li>GET</li><li>POST</li>|

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/887cfcda7645b14882b3ef0b691196d0.png?witdh=600)
## エンドポイントの作成
次にエンドポイントを作成します。
APIのページから[Configure Endpoint]をクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/a70c4b90a07e9a0bfdf7d5b269339f2c.png?witdh=600)
注文に必要なエンドポイントは下記になりますのでそれぞれ作成してください。

**ログイン用エンドポイント**  

| 設定項目 | 設定           |             |
| :------- | :------------- | :---------- |
| パス | login |             |
|  | 有効/無効 | 有効 |
| モデル | カテゴリー | 認証 |
|  | モデル | Login |
|  | オペレーション | Login_challenge |

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/56405d93e2a5199164b547d36eb9009c.png?witdh=600)
**プロフィール情報取得用エンドポイント**  

| 設定項目 | 設定           |             |
| :------- | :------------- | :---------- |
| パス | user/profile |             |
|  | 有効/無効 | 有効 |
| モデル | カテゴリー | 認証 |
|  | モデル | Login |
|  | オペレーション | profile |

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/6c5b0a76f3e9534a0a1a02dddb98f551.png?witdh=600)
**カートへの商品追加用エンドポイント**  

| 設定項目 | 設定           |             |
| :------- | :------------- | :---------- |
| パス | ec/cart/add |             |
|  | 有効/無効 | 有効 |
| モデル | カテゴリー | EC |
|  | モデル | ECCart |
|  | オペレーション | add |

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/224597823d1ad675121c6eef140d14ca.png?witdh=600)
**商品処理用エンドポイント**  

| 設定項目 | 設定           |             |
| :------- | :------------- | :---------- |
| パス | ec/order/purchase |             |
|  | 有効/無効 | 有効 |
| モデル | カテゴリー | EC |
|  | モデル | ECOrder |
|  | オペレーション | purchase |

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/89f8cc81101109929e41a9b69f16b814.png?witdh=600)
以上でエンドポイントの作成完了です。今回は下記４つのエンドポイントを作成しました。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/da7ad5e21950c19ac00cf08f0a4eceb6.png?witdh=600)
## APIの動作確認
エンドポイントの設定ができたら、対象のエンドポイントをSwaggerUIで動作させ、商品の購入ができることを確認していきます。  

### ログイン
今回のケースでは会員として登録済みのメンバーにログインをさせた状態での購入を想定していますので、SwaggerUI画面からログイン処理を行う必要があります。

:::info
注文時に利用する為、[メンバー編集](/ja/docs/management/member/#メンバーの編集)の[プロフィール情報]ページでログインに使用するメンバーの住所登録は事前に行っておいてください。  
:::

APIのページから[Swagger UI]をクリックしてSwagger UIのページに遷移します。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/45f20eeae4a5be402fadd2d9c432c2e7.png?witdh=600)
`login`のエンドポイントをクリックします。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/4dd71a57c6b306edba4519fd8c367d7e.png?witdh=600)
[Try it out]をクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/e0a9516a0cded35ec92621846dfd7901.png)
Request bodyフィールドが表示されますので、下記のようにログイン情報を記載して、[Execute]をクリックします。
```json title="Request body"
{
  "email": "YOUR_MAIL_ADDRESS@example.com",
  "password": "PASSWORD",
  "login_save": 0
}
```

:::caution
`YOUR_MAIL_ADDRESS@example.com` と `PASSWORD` にはご自身のメールアドレスとパスワードを入力ください。
:::

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/1933be946296c9907ec0edd502612bf5.png?witdh=600)
ログインに成功すると、レスポンスコード:200でデータがレスポンスされます。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/3f30f3640a1786036fb7d3961a739da0.png)
補足)APIのセキュリティ設定をDynamic Tokenで利用する場合  
リクエストヘッダにトークンを付与する必要があるので、[Swagger UIを利用して、APIのセキュリティを確認する](/ja/docs/tutorials/how-to-use-swagger-ui/)で説明しているログインの方法を参照してください。

### カートIDの取得
ログイン処理が完了したらカートIDを取得します。  
カートIDはログインユーザーの情報に紐づけされているため、profileのエンドポントから取得します。  
`user/profile`のエンドポイントをクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/501b5bce1639f66e729ca61fc21379f7.png?witdh=600)
[Try it out]をクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/50033fae47251e04d824a78a491c901a.png?witdh=600)
[Execute]をクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/d9fe6a7b62cff772bd04f01ff61fb92f.png?witdh=600)
レスポンスコード:200でデータがレスポンスされますので、`ec_cart_id`の値をメモしておきます。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/e294dcbab9e9df6d007a8186d3f1ac23.png?witdh=600)
このケースでは`1306`がカートIDとなります。

### カートに商品を追加する
購入したい商品の商品IDを確認し、そのIDを指定して商品をカートに追加します。  
まずは[商品設定](/ja/docs/management/ec-product-edit/)のページを参考に購入したい商品のIDを確認します。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/84f52803418c5b38182c8dbc51fddc67.png?witdh=600)
このケースでは`41211`が商品IDとなります。

Swagger UIのページに戻り、`/ec/cart/add`のエンドポイントをクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/e837ec77b5c9042038eb6bb9f96c3662.png?witdh=600)
[Try it out]をクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/03d58c403ff909ca6ff7981f443821c4.png?witdh=600)
Request bodyフィールドが表示されますので、下記のようにカートIDと、商品の情報を記載して、[Execute]をクリックします。

設定が必要なパラメータは下記の通りです。

- ec_cart_id: 事前に確認したカートID
- product_id: 購入する商品ID
- quantity: 購入個数

今回は下記のように設定しました。

| 設定項目 | 設定           |  
| :------- | :------------- | 
| ec_cart_id | 1306 | 
| product_id | 41211 |
| quantity | 1 |

```json title="Request body"
{
  "ec_cart_id": 1306,
  "item": {
    "product_id": 41211,
    "quantity": 1
  }
}
```

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/2b9281dbdd95d495506cb53e0a18fa11.png?witdh=600)
商品の追加が完了すると、レスポンスコード:200でデータがレスポンスされ、`messages`に`"新規追加しました。"`の表示がされます。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/a1dc94f8fd675429a0b986dc6e162a02.png?witdh=600)
### カートの商品を購入する
商品の購入時、支払方法を指定する必要があるので、[支払方法設定](/ja/docs/management/ec-paymenttype-list/)のページで、支払い方法のIDを確認します。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/9780524c1949625a55477bf66d37b3f9.png?witdh=600)今回は銀行振込のID`58`で購入します。

Swagger UIのページに戻り、`/ec/order/purchase`のエンドポイントをクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/cde401f6ecfe3d6872ea6c5730808ab1.png?witdh=600)
[Try it out]をクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/71ede3dba7b6c1866cf9ed31a983fa3f.png?witdh=600)
Request bodyフィールドが表示されますので、下記のようにカートIDと支払方法のIDを記載して、[Execute]をクリックします。

設定が必要なパラメータは下記の通りです。

:::caution
今回は必須パラメータのみで進めます。他のパラメータは状況に応じて変更をしてください。  
ec_cart_id: 事前に確認したカートID  
ec_payment_id: 決済する支払い方法のID  
:::

今回は下記のように設定しました。

| 設定項目 | 設定           |  
| :------- | :------------- | 
| ec_cart_id | 1306 | 
| ec_payment_id | 58 |

```json title="Request body"
{
  "ec_cart_id": 1306,
  "ec_payment_id": 58
}
```
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/e68931e1a2f4d83de242ce0a1f2956c4.png?witdh=600)
商品の購入が完了すると、レスポンスコード:200でデータがレスポンスされ、`messages`に`"注文が完了しました。"`、`ids`に注文IDが返却されます。  
また、購入者のメールアドレス宛に「ご購入完了のお知らせ」のメールが届きます。  
注文はカートの状態により配送単位で複数に分かれることもあります。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/ccd634ca3331d41476fd6cb6ca805819.png?witdh=600)
## 注文情報の確認
先ほどSwagger UIを利用して購入した注文は[注文一覧](/ja/docs/management/ec-order-list/)から確認できます。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/fba6f8eeba5c77c0d11f855365ef2ce6.png?witdh=600)
以上でECサイト構築の際、必要になるAPIの設定とSwagger UIを使った注文手順の確認方法の説明を終了します。

## 関連ドキュメント
- [管理画面よりECの設定を行う](/ja/docs/tutorials/ec-management/)
- [ECサイト構築に必要なAPIの設定を行う](/ja/docs/tutorials/ec-api/)
- [ECサイトを作成する フロントエンドを作成する](/ja/docs/tutorials/ec-front-end/)
- [Swagger UIを利用して、APIのセキュリティを確認する](/ja/docs/tutorials/how-to-use-swagger-ui/)
- [API セキュリティ](/ja/docs/management/api-security/)
- [ECのAPIでカード決済を行うには？](/ja/docs/faq/how-can-i-get-card-token/)


---

# Stripeと連携して有料会員の機能を実装する。

> 元ページ: `tutorials/subscription-billing-with-stripe` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/subscription-billing-with-stripe/
> 概要: KurocoとStripeを連携すると、Stripeのサブスクリプション支払い実行後、対象のユーザーを自動で特定のグループに追加できます。こちらを利用して、有料会員とその支払い機能を実装できます。

## 概要
KurocoとStripeを連携すると、Stripeのサブスクリプション支払い実行後、対象のユーザーを自動で特定のグループに追加できます。
こちらを利用して、有料会員とその支払い機能を実装できます。

## 学べること

以下の手順でKurocoとStripeの連携からサブスクリプション購読・解除までの動作を確認します。

* [KurocoとStripeの連携](#kurocoとstripeの連携)
  - [StripeでAPIキーを取得](#stripeでapiキーを取得)
  - [StripeでWebhookを作成](#stripeでwebhookを作成)
  - [KurocoでStripeとのAPI連携を設定](#kurocoでstripeとのapi連携を設定)

* [サブスクリプション商品の追加](#サブスクリプション商品の追加)
  - [Stripeで商品の追加](#stripeで商品の追加)
  - [KurocoのグループとStripeの商品を紐づけ](#kurocoのグループとstripeの商品を紐づけ)

* [APIの設定](#apiの設定)
  - [エンドポイントの設定](#エンドポイントの設定)
  - [支払処理の確認](#支払処理の確認)
  - [キャンセル処理の確認](#キャンセル処理の確認)

## KurocoとStripeの連携

まずKurocoと連携するためのAPIキーをStripeから取得します。

### StripeでAPIキーを取得

ブラウザで[Stripeのダッシュボード](https://dashboard.stripe.com/)にアクセスし、右上の[Developers]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/998a7d7b6e72a9ff73336acfc1fa202f.png)

次に、左サイドバーメニューの[API keys]をクリックすると、[Publishable key]と[Secret key]が表示されます。  
後で使用するのでコピーしてください。

:::caution
Stripeにはテストモードと本番モードの2種類があります。
モードによってAPIキーが異なりますので切り替えの際はKuroco側の設定も更新する必要があります。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1463f45913a90348113701014db4208d.png)

### StripeでWebhookを作成

次に、サイドメニューの[Webhooks]をクリックし、[Add an endpoint]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3c8abbd3fc861a4a343b3ca590460d7f.png)

Webhookの設定ページに移動したら、Stripeの決済が成功したかどうかをKurocoが判断するためのWebhookを追加します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/94aa9e09dd6d2d44b2a63a57b92cdc06.png)

以下のように設定します。  

| 項目 | 設定 |
| :---  | :---  |
| Endpoint URL | [外部システム連携] -> [[Stripe](/ja/docs/management/stripe/)]で表示されるエンドポイントURLを入力します。|
| Description  | webhookの説明を入力します。(任意) |
| Listen to    | [Events on your account] を選択します。|
| Version      | 最新のバージョンを選択します。|
| Events       | [+ Select events]をクリックして、ドロップダウンから以下のイベント選択します。<ul><li>`customer.subscription.created`</li><li>`customer.subscription.deleted`</li><li>`customer.subscription.updated`</li></ul>選択ができたら[Add events] をクリックしてイベントを追加します。 |

完了したら、[Add endpoint]をクリックします。

エンドポイントのページに遷移するので、Signing secretの[Reveal]をクリックして、Webhookの秘密鍵を表示します。  
後で使用するのでコピーしてください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d0a520b9294b90323506c9f610630910.png)

### KurocoでStripeとのAPI連携を設定

Kurocoの管理画面から[外部システム連携]->[Stripe]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bed3aa3ffa8cabc2e0838f271b0cb93f.png)

Stripeの外部システム連携ページが表示されたら、Stripeで取得したPublishable key(公開可能キー)、Secret key(シークレットキー)、Signing secret(ウェブフックシークレット)を入力します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/108ab6a54e6603d27edea180e6cb6884.png)

| 項目 | 設定 |
| :--- | :---  |
| Status | [有効にする]にチェックを入れます。|
| 公開可能キー | Stripeで取得した[Publishable key]を入力します。 |
| シークレットキー | Stripeで取得した[Secret key]を入力します。 |
| ウェブフックシークレット | Stripeで取得した[Signing secret]を入力します。 |

入力が完了したら[更新する]をクリックして設定を反映します。

## サブスクリプション商品の追加

次に、Stripe及びKurocoで利用するサブスクリプションの設定をします。

### Stripeで商品の追加

Stripeの管理画面のメニューバーから[Products]をクリックし、左サイドバーから[All products]をクリックします。
   
Productsページに遷移するので、[+ Add a product]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2a97ee06c256958b8ea76a502bee77d0.png)

商品の追加ページに遷移するので、以下のように、商品の詳細を記入します。  
詳しくは、Stripeのドキュメント[商品および価格を管理する](https://stripe.com/docs/products-prices/manage-prices)を参照してください。

| 項目 | 設定 |
| :--- | :--- |
| Name | 商品の名前を入力します。 |
| Description | 商品の説明を入力します。 |
| Pricing | 商品の価格を入力します。 |
| Recurring  | 定期支払にするため[Recurring]を選択します。 |
| Billing period | 支払い周期を選択します。 |

設定が完了したら[Save product]をクリックして商品を追加します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d25df95fe43ed69f9fa8eaa6d7111fb2.png)

商品の詳細ページに遷移するので、`price_`から始まるAPI IDをコピーしておきます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5f018cec74aa98e71cdf383dc2a574d5.png)

他の商品を追加する場合は、同様のステップを繰り返します。

### KurocoのグループとStripeの商品を紐づけ

次にStripeの支払が完了した際に追加されるKurocoのグループを設定します。  
Stripeの商品とKurocoのグループは1対1で紐づくので、複数の商品を利用する場合は商品ごとにグループを作成します。  
新しいグループの作成方法については、[グループを作成する](/ja/docs/tutorials/how-to-make-new-group/)を参照してください。

グループ一覧ページから対象のグループ名をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/32cd62723ff8d7c5330b62088ffb9ea8.png)

グループ編集の画面「StripeプライスID」の項目に、Stripeから取得したAPI IDを入力します。

:::tip
「StripeプライスID」の項目はStripeとKurocoの連携後に表示されます。表示されない場合は、上記の[KurocoとStripeの連携](#kurocoとstripeの連携)に戻り、入力・設定が正しいか確認してください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/25cd5fcb3c06de1a142030e3ff56a7f5.png)

Stripeの決済ページから正常に支払いが完了すると、支払いをしたメンバーがこのグループに自動的に追加されます。

## APIの設定

最後に、支払い処理に必要なエンドポイントを追加して動作の確認をします。  
支払い用のエンドポイントと、キャンセル用のエンドポイントの2つを準備します。

### エンドポイントの設定

:::caution
決済機能を利用するためには、APIのセキュリティ設定をCookieまたは動的トークンに設定してください。
:::

Kurocoの左サイドバーメニューから、[API]をクリックし、エンドポイントを追加するAPIを選択します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/477300a8e16803900febf4469215a58b.png)

エンドポイント一覧画面で、[新しいエンドポイントの追加]をクリックし、以下2つのエンドポイントを追加します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1af3b17d5e6c1bdd530cdb39aa7a4168.png)

#### チェックアウトエンドポイント
支払い用のURLを生成するためのエンドポイントです。  

| 項目 | 設定 |
| :--- | :--- |
| カテゴリー | Payments |
| モデル | Stripe, v1 |
| オペレーション | checkout |
| products_list | `price_`から始まるStripeプライスIDを入力します。<ul><li>複数のStripeプライスIDを設定できます。</li><li>StripeプライスIDをフロントエンドから変更することはできません。</li></ul>|
| return_url | 支払いが成功した場合にリダイレクトされるフロントエンドのURLを設定します。 |
| return_err_url |  支払いが失敗した場合にリダイレクトされるフロントエンドのURLを設定します。 |
| trial_end |  トライアル期間の終了日を指定できます。 |
| trial_period_days |  トライアル期間の日数を指定できます。 |

設定が完了したら[追加する]をクリックしてエンドポイントを追加します。

ここでは以下のように設定しました。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a34f702656c4c922e5d7440910f8d0cc.png)

#### キャンセルエンドポイント
サブスクリプションをキャンセルするためのエンドポイントです。  

| 項目 | 設定 |
| :--- | :--- |
| カテゴリー | Payments |
| モデル | Stripe, v1 |
| オペレーション | cancel_order |

設定が完了したら[追加する]をクリックしてエンドポイントを追加します。

ここでは以下のように設定しました。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2184f4326c67b695e22e57fbeae4f8c1.png)

### 支払処理の確認
Swagger UIを利用して、支払い及び、連携したグループへの追加が期待通りに動作しているか確認します。

エンドポイント一覧画面で、[Swagger UI]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/410a1c3570453fa969d76aeacdfeabb8.png)

支払いを行いたいメンバーでログインをして、チェックアウトエンドポイントの[Try it out]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/11f34df1503e6fded0c0b7d4005eab05.png)

[Execute]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/503401472b2d923c12d215df04bd1df9.png)

支払い用のURLが発行されるのでブラウザからアクセスします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5d8f120814340bb9459cb8d2e6d595f6.png)

支払いページに遷移するので、カード情報を入力し、[申し込む]をクリックします。

:::tip
テストモードの場合はStripeの[テストカード](https://stripe.com/docs/testing#international-cards)を利用して、支払処理後の動作確認が可能です。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/44c6b1ab3e4b22284ce3bb56a7b5e51e.png)

支払いが完了すると、エンドポイントで設定したフロントエンドのURLに遷移します。  
return_urlが空欄の場合はフロントエンドURLのトップページに遷移します。

以下3点を確認し、動作が正常に完了したことを確認してください。  

- 支払いをしたメンバー情報のID情報タブで、所属グループにStripeと連携したグループが追加されている。  
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/1b7f39bd891d0a063a4e451402e376c0.png)

- 支払いをしたメンバー情報のプロフィール情報タブで「StripeカスタマーID」と「StripeサブスクリプションID」が追加されている。  
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/453161e509029b43516a49bc015f153b.png)

- Stripe管理画面の[Billing]->[Subscription]で支払いをしたメンバーが追加されており、StripeサブスクリプションIDがKuroco管理画面と一致している。  
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/a4ab2faee0f781df82f33ac7c4a58ebe.png)  
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/144255e4f4b6d43e03646fd984099043.png)

### キャンセル処理の確認

続いてキャンセル処理の確認をします。  
サブスクリプションのキャンセルを行いたいメンバーでログインをして、キャンセルエンドポイントの[Try it out]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9456bf51a59b865b258076a62a637a71.png)

[Execute]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b6ffcfffd1029f38661dd098564c9904.png)

okのステータスが表示されたらキャンセル処理は完了です。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fdbfac0405ee10a2b6e1d2c51128c1aa.png)

以下3点を確認し、動作が正常に完了したことを確認してください。

- 支払いをしたメンバー情報のID情報タブで、所属グループからStripeと連携したグループが削除されている。  
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/bbc80b0f85c8807b526e087dc0e4789f.png)

- 支払いをしたメンバー情報のプロフィール情報タブで「StripeサブスクリプションID」が削除されている。  
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/3bc158d86690dc006c773ab75c66ff23.png)

- Stripe管理画面の[Billing]->[Subscription]の[Current]タブから対象のメンバーが削除され、[Canceled]タブに追加されている。  
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/2c1d15d69eb4d12eb6bf798be3c12954.png)

:::caution
サブスクリプションのキャンセル処理は、確認ページにリダイレクトされることなく、即座に行われます。  
また、キャンセル時の返金はありません。
:::

## その他
### 制限事項

現在、KurocoはStripeの以下の支払いタイプに対応していません。
- ゲストチェックアウト（非ログインユーザーの支払）
- One time設定の商品購入
- メンバーへの複数のサブスクリプションIDの発行

### Stripe CLI
Strileの開発者ツールである[Stripe CLI](https://stripe.com/docs/stripe-cli) を使用すると、コマンドラインから直接、Stripe の組み込みを構築、テスト、管理できます。

これを行うには、以下に示すフラグを指定して `stripe listen` というコマンドを実行します。ウェブフックシークレットを受け取るので、それをローカル環境に追加して情報を復号化します。

| Flag | Description |
| :--- | :--- |
| `--forward-to`  | Webhookの呼び出しの転送先となるローカルホストのURLを入力します。 |
| `--events` | リッスンしたいイベントのリストをカンマ区切りで入力します。 |
| `--skip-verify` | ローカルSSL証明書がない、または無効な場合に、このフラグを使用して認証をスキップします。|

Stripe CLIの詳細については以下を参照してください。
- [Stripe CLI を使ってみる](https://stripe.com/docs/stripe-cli)
- [Stripe CLI でイベントをリッスンする](https://stripe.com/docs/stripe-cli/about-events)

## 関連ドキュメント
- [Stripe](/ja/docs/management/stripe/)
- [有料会員プラン一覧](/ja/docs/management/ec-premium-member-plan-list/)
- [グループ](/ja/docs/management/group/)
- [社内ネットワークからアクセスした場合のみスーパーユーザーとなるグループを作成する](/ja/docs/tutorials/how-to-make-new-group/)
