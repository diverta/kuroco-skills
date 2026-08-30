# Kurocoドキュメント: チュートリアル / API・カスタム処理（2/2）

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- 静的アクセストークンによるAPIアクセス制限の方法（`restricting-api-access-with-statictoken`）
- カスタム処理を利用して、APIエンドポイントに独自のスタブを設定する（`setting-up-stubs-on-api-endpoints-using-custom-functions`）
- Swagger UIを利用して、コンテンツのデータ構造を確認する（`using-swagger-to-check-the-structure-of-data`）


---

# 静的アクセストークンによるAPIアクセス制限の方法

> 元ページ: `tutorials/restricting-api-access-with-statictoken` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/restricting-api-access-with-statictoken/

## KurocoのAPIセキュリティについて
KurocoのAPIセキュリティは下記５つから選択できます。
- 無し
- 静的アクセストークン
- 動的アクセストークン
- Cookie
- 特権付き静的トークン

一時的な開発用APIを作成してテストをする場合や、完全にオープンなデータを利用する場合は「無し」を設定できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6f01c6328767339b23838b18a0940dbd.png)

しかしながら、APIのセキュリティ設定を「無し」にしてしまうと誰でもAPIが利用できるようになり、外部から無差別にAPIリクエストを受け付けることが可能になります。  

この状態が想定通りではない場合、静的アクセストークン機能を利用することである程度の制限をかけることができます。  
今回は静的アクセストークンを利用してアクセス制限をかける方法を説明します。

:::caution
静的アクセストークンの文字列は公開サイトのネットワーク通信やJSファイル内の記述を参照することで外部からも閲覧可能な情報となります。その為、セキュアな情報に対する制限をかけたい場合は静的アクセストークンではなく動的アクセストークン・Cookie制限によるログイン認証やAPIに閲覧グループによる制限をかける形で対応をしてください。
:::

## 静的アクセストークンによるAPIアクセス制限方法
静的アクセストークンによるAPIアクセス制限の方法を説明します。

### 1. KurocoのAPIのセキュリティを設定する
任意のAPI一覧ページから[セキュリティ]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d4def3cf4d3594707701c3052ef09d2b.png)

「セキュリティ」を静的アクセストークンに変更し、[保存する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2bcf006b2a9598350d7a2993419ae44d.png)

### 2.静的アクセストークンを発行する
API一覧ページから[Swagger UI]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e5b6af39026c75af192d5a329d647591.png)

Swagger画面の上部にある 「静的アクセストークン」 の「有効期限」より有効期限を設定し、[生成する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7115b681f876864bce2fb483e6b27046.png)

トークンが発行されます。後ほど利用するのでコピーしておいてください。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/06518b76d5caa7a90a1a2809e56ee0d2.png)

以上でKuroco管理画面での操作は完了です。  

### 3. APIアクセスの設定

一例としてNuxt3とNext.jsのコードを記載しています。  

:::info
本チュートリアルでは以下のバージョンでコードを書いています。
- Nuxt3: v3.14.0
- Next.js: v15.0.3 (Using App Router)
:::

まず、チュートリアルで必要なパッケージをインストールします：

**Nuxt3:**

Nuxt 3では追加のパッケージのインストールは不要です。

**Next.js:**

```bash title="terminal"
npm install axios
```


### 4. 環境変数の設定

**Nuxt3:**

```plaintext title=".env"
NUXT_STATIC_TOKEN=YOUR_STATIC_TOKEN_HERE
NUXT_PUBLIC_API_BASE_URL=https://your-api-endpoint.com
```

**Next.js:**

```plaintext title=".env"
STATIC_TOKEN=YOUR_STATIC_TOKEN_HERE
NEXT_PUBLIC_API_URL=https://your-api-endpoint.com
```


:::caution 注意
`NUXT_PUBLIC_`/`NEXT_PUBLIC_`プレフィックスがつく環境変数は、クライアントサイドで参照可能になります。詳細は下記のリンクをご確認ください。
- [Nuxt 3 Documents - runtime-config](https://nuxt.com/docs/guide/going-further/runtime-config)
- [Next.js Documents - environment-variables](https://nextjs.org/docs/app/building-your-application/configuring/environment-variables)
:::


### 5. 設定ファイルの更新

**Nuxt3:**

```ts title="nuxt.config.ts"
export default defineNuxtConfig({
  runtimeConfig: {
    public: {
      staticToken: process.env.NUXT_STATIC_TOKEN,
      publicApiBaseUrl: process.env.NUXT_PUBLIC_API_BASE_URL
    }
  }
})
```

**Next.js:**

```ts title="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  env: {
    STATIC_TOKEN: process.env.STATIC_TOKEN
  }
}

module.exports = nextConfig
```


### 6. APIのリクエストヘッダーに静的アクセストークンを設定する

**Nuxt3:**

```ts title="/plugins/fetch.ts"
export default defineNuxtPlugin(() => {
  const config = useRuntimeConfig()

  return {
    provide: {
      customFetch: (url: string, options = {}) => {
        return useFetch(url, {
          baseURL: config.public.apiBase as string,
          headers: {
            'x-rcms-api-access-token': config.public.staticToken as string
          },
          ...options
        })
      }
    }
  }
})
```

:::info
Kurocoビギナーズガイドでは `plugins` の利用方法はカバーしていませんが、この機会に公式ドキュメントでぜひ触れてみてください。
- [Nuxt 3 Documents - plugins](https://nuxt.com/docs/guide/directory-structure/plugins)
:::

**Next.js:**

```ts title="/lib/axios.ts"
import axios from 'axios'

export const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL,
  headers: {
    'x-rcms-api-access-token': process.env.STATIC_TOKEN
  }
})
```


### 7. APIの使用例

**Nuxt3:**

```markup title="/pages/example.vue"
<script setup>
// 基本的な使用例
const { $customFetch } = useNuxtApp()
const { data: response } = await $customFetch('/api/endpoint');

// 個別にヘッダーを上書きする例
const { $customFetch } = useNuxtApp()
const { data: customData } = await $customFetch('/api/endpoint', {
  headers: {
    'x-rcms-api-access-token': 'different-token'
  }
}
</script>
<template>
  <div>
    <div v-if="pending">Loading...</div>
    <div v-else>
      <pre>{{ data }}</pre>
    </div>
  </div>
</template>
```

**Next.js:**

```tsx title="/app/example.tsx"
// APIクライアントを使用する場合
import { api } from '@/lib/axios'

export default function Page() {
  const [data, setData] = useState(null)

  useEffect(() => {
    const fetchData = async () => {
      const response = await api.get('/api/endpoint')
      setData(response.data)
    }
    fetchData()
  }, [])

  return <div>{/* データの表示 */}</div>
}

// または組み込みfetchを使用する場合
async function getData() {
  const res = await fetch('https://api-endpoint.com/api/endpoint', {
    headers: {
      'x-rcms-api-access-token': process.env.STATIC_TOKEN
    }
  })
  return res.json()
}

// App RouterのServer Componentで使用する場合
export default async function Page() {
  const data = await getData()
  return <div>{/* データの表示 */}</div>
}
```

:::info
- Nuxt 3: `useFetch`/`$fetch`を使用し、自動的にヘッダーに静的トークンが付与される例を紹介しました。
- Next.js: `fetch`または`axios`を使用し、リクエストヘッダーに静的トークンを設定する例を紹介しました。
:::

:::tip
- リクエストヘッダーに、`X-RCMS-API-ACCESS-TOKEN` をキーとして静的アクセストークンを設定し、リクエストを送信することでデータ取得が可能です。
:::

:::caution
・プロジェクトにあわせて、実際には `.env` や `.env.local` など別ファイルに記述することをお勧めします。  環境変数のファイルは必ず`.gitignore`に追加し、機密情報をリポジトリにコミットしないようにしてください。
:::

以上で静的アクセストークンによるAPIアクセス制限の設定が完了です。

## 特権付き静的トークンによるAPIアクセス制限方法

特権付き静的トークンは、静的アクセストークンと同様のトークン認証ですが、トークン生成時に特定のメンバーを指定します。  
指定したメンバーの権限でリクエストが実行されるため、ログインや動的トークン生成のフローを経ることなく、メンバーの権限に基づいたAPIリクエスト制限のあるエンドポイントにアクセスできます。  
サーバー間通信で、特定のメンバーの権限でAPIにアクセスする必要がある場合などに利用します。

リクエストヘッダーへのトークンの設定方法やフロントエンドからの利用方法は静的アクセストークンと同じです。ここでは、静的アクセストークンと異なる管理画面での操作を説明します。

### 1. セキュリティを特権付き静的トークンに設定する
API画面より、セキュリティの[設定]をクリックし、「セキュリティ」を[特権付き静的トークン]に変更して[更新する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/994681867a09d0c4e40b3d9cc07ea1c7.png)

### 2. 特権付き静的トークンを発行する
API情報画面の[特権付き静的トークン]の[生成する]をクリックし、表示されたダイアログで以下の項目を指定します。
- **有効期限**: トークンの有効期限を指定します。
- **メモ**: 任意のメモを入力できます。
- **メンバーID**: トークンに紐付けるメンバーのIDを指定します。このメンバーの権限でAPIリクエストが実行されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c4bab79743ba750a3dbe2006283426fd.png)

値を入力したら[生成する]をクリックします。トークンが発行されるので、後ほど利用するのでコピーしておいてください。

### 3. APIアクセスの設定
リクエストヘッダーへの特権付き静的トークンの設定方法は、静的アクセストークンと同じです。  
上記「3. APIアクセスの設定」〜「7. APIの使用例」のコードで、環境変数に設定するトークンの値を特権付き静的トークンの値に置き換えることで、そのまま利用できます。  
リクエストヘッダーには、静的アクセストークンと同様に `X-RCMS-API-ACCESS-TOKEN` をキーとしてトークンを設定します。

:::caution
特権付き静的トークンは、指定したメンバーの権限でリクエストを実行します。そのため、適切な権限を持つメンバーを指定してトークンを生成してください。  
また、静的アクセストークンと同様にトークンの文字列が流出するリスクがあるため、トークンの更新を想定したシステム構成にし、機密情報をリポジトリにコミットしないようにしてください。
:::

以上で特権付き静的トークンによるAPIアクセス制限の設定が完了です。

## 参考
- [API Security](/ja/docs/management/api-security/)
- [Swagger UIを利用して、APIのセキュリティを確認する](/ja/docs/tutorials/how-to-use-swagger-ui/)

## 関連ドキュメント
- [API セキュリティ](/ja/docs/management/api-security/)
- [Swagger UIを利用して、APIのセキュリティを確認する](/ja/docs/tutorials/how-to-use-swagger-ui/)
- [ログイン画面を構築する](/ja/docs/tutorials/integrate-login/)
- [エンドポイント設定後の注意点](/ja/docs/tutorials/points-to-note-after-endpoint-configuration/)
- [静的アクセストークンの有効期限が切れる前に通知は届きますか？](/ja/docs/faq/notification-before-static-access-token-expires/)


---

# カスタム処理を利用して、APIエンドポイントに独自のスタブを設定する

> 元ページ: `tutorials/setting-up-stubs-on-api-endpoints-using-custom-functions` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/setting-up-stubs-on-api-endpoints-using-custom-functions/
> 概要: カスタム処理を使用して、APIエンドポイントに独自のスタブを設定する方法を解説します。この機能を利用すると、実際のカスタム処理を作成する前に、フロントエンド側からの動作確認が可能になります。

カスタム処理を使用して、APIエンドポイントに独自のスタブを設定する方法を解説します。  
スタブを設定すると、実際のカスタム処理を作成する前に、フロントエンド側からの動作確認が可能になります。

## スタブを利用する理由

下記のような場合、スタブを設定することで開発をスムーズに進めることができます。
- Kurocoにまだ十分にデータを入れていない
- 複雑なカスタム処理の実装が必要だが、まだ未実装である

本来であれば、バックエンドの実装完了後にフロントエンドの実装をする流れになります。
そのため、バックエンドの実装が完了するまでフロントエンド側はダミーのデータを準備してテストしなくてはいけませんでした。
また、バックエンド実装後にダミーデータの内容を修正する必要もあります。

しかしながら、スタブを利用することで想定のエンドポイントへリクエストをすることが可能となります。
ダミーデータの準備や、バックエンド実装後の修正が不要になり、開発効率が上がります。

## 事前準備

今回は[カスタム処理と紐づいたAPIエンドポイントを作成する](/ja/docs/tutorials/creating-a-custom-function-endpoint/)で作成した、下記カスタム処理とエンドポイントを利用します。

| 項目 | 内容 |
| :--- | :--- | 
|カスタム処理 | PlainCustomFunction |
|エンドポイント | /rcms-api/1/plain-custom-endpoint |

このチュートリアルのカスタム処理は、`data`変数にassignした値を`{"data": ...}`形式でレスポンスする書き方のため、エンドポイントの`show_contents`パラメータは無効（デフォルト）のまま利用してください。  
テンプレートが何も出力せず`data`変数にassignするだけの書き方では、`show_contents`を有効にするとテンプレートの出力が空になり、レスポンスは`[]`になります。詳細は[エンベロープなしのJSONを返す（show_contents）](/ja/docs/tutorials/creating-a-custom-function-endpoint/#エンベロープなしのjsonを返すshow_contents)を参照してください。

それでは、以下パターンにてカスタム処理にスタブを設定する方法を説明します。カスタム処理をそれぞれのパターンで修正して確認します。

- [シンプルな文字列を返すカスタム処理を実装する](#シンプルな文字列を返すカスタム処理を実装する)
- [JSONを返すカスタム処理を実装する](#jsonを返すカスタム処理を実装する)
- [条件付きでJSONを返すカスタム処理を実装する](#条件付きでjsonを返すカスタム処理を実装する)
- [GETクエリの内容を判定して対応したJSONを返すカスタム処理を実装する](#getクエリの内容を判定して対応したjsonを返すカスタム処理を実装する)

## シンプルな文字列を返すカスタム処理を実装する

### カスタム処理の内容
カスタム処理一覧画面より、「PlainCustomFunction」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1cdd5e7e2e08e966e1d45ae54d303d4f.png)

カスタム処理の実行内容フィールドに下記を記載し、[更新する]をクリックします。

```php
{* シンプルなダミー文字列を返します。 *}
{capture name=data}
{literal}
    response text
{/literal}
{/capture}
{assign var=data value=$smarty.capture.data}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/71d96c544053b445e38d384af60ce612.png)

### SwaggerUIにて動作確認
SwaggerUI画面より、[plain-custom-endpoint]をクリックします。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/408821848b40886fcbfd92b634733ac7.png)
[Try it out]をクリックします。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/ed40a21db9b785e925e7bdfb9a3fe25f.png)
[Execute]をクリックします。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/5601074a29c44c0cc14df57304ac1a71.png)
「Response body」にシンプルな文字列がレスポンスされます。  
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/3e41849347bfe3930ab29206a2fb603d.png)
## JSONを返すカスタム処理を実装する

### カスタム処理の内容
カスタム処理一覧画面より、「PlainCustomFunction」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1cdd5e7e2e08e966e1d45ae54d303d4f.png)

カスタム処理の実行内容フィールドに下記を記載し、[更新する]をクリックします。

```php
{* JSONを返します。 *}
{capture name=data}
{literal}
    {
        "key1": "val1"
    }
{/literal}
{/capture}
{assign var=data value=$smarty.capture.data|@json_decode}
```
![Image from Gyazo](https://t.gyazo.com/teams/diverta/887768d2a4d47f08046d14897562e8fa.png)

### SwaggerUIにて動作確認
SwaggerUI画面より、[plain-custom-endpoint]をクリックします。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/408821848b40886fcbfd92b634733ac7.png)
[Try it out]をクリックします。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/ed40a21db9b785e925e7bdfb9a3fe25f.png)
[Execute]をクリックします。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/5601074a29c44c0cc14df57304ac1a71.png)
「Response body」にJSONがレスポンスされます。  
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/8c99c3d599255449d3b3943c02b8684a.png)
## 条件付きでJSONを返すカスタム処理を実装する

### カスタム処理の内容
カスタム処理一覧画面より、「PlainCustomFunction」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1cdd5e7e2e08e966e1d45ae54d303d4f.png)

カスタム処理の実行内容フィールドに下記を記載し、[更新する]をクリックします。

```php
{* 条件を設定します。 *}
{assign var=condition value=false}

{* 条件により内容を変更しつつ返します。 *}
{capture name=data}
{if $condition}
    {literal}
        {
            "condition_value": true
        }
    {/literal}
{else}
    {literal}
        {
            "condition_value": false
        }
    {/literal}
{/if}
{/capture}

{assign var=data value=$smarty.capture.data|@json_decode}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f9d7ca55220f423bc852735e282e3422.jpg)
### SwaggerUIにて動作確認
SwaggerUI画面より、[plain-custom-endpoint]をクリックします。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/408821848b40886fcbfd92b634733ac7.png)
[Try it out]をクリックします。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/ed40a21db9b785e925e7bdfb9a3fe25f.png)
[Execute]をクリックします。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/5601074a29c44c0cc14df57304ac1a71.png)
「Response body」に条件を判定した結果のJSONがレスポンスされます。  
![fetched from Gyazo](https://t.gyazo.com/teams/diverta/44ebaa40d27315e658608db4ad7be3a8.png)
## GETクエリの内容を判定して対応したJSONを返すカスタム処理を実装する

### カスタム処理の内容

カスタム処理一覧画面より、「PlainCustomFunction」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1cdd5e7e2e08e966e1d45ae54d303d4f.png)

カスタム処理の実行内容フィールドに下記を記載し、[更新する]をクリックします。

```php
{* GETパラメータにより内容を変更しつつ返します。 *}
{capture name=data}

{if $smarty.get.status == 'new'}
    {literal}
        {
            "requested_status": "NEW"
        }
    {/literal}
{elseif $smarty.get.status == 'old'}
    {literal}
        {
            "requested_status": "OLD"
        }
    {/literal}
{else}
    {literal}
        {
            "requested_status": "ANY"
        }
    {/literal}
{/if}
{/capture}

{assign var=data value=$smarty.capture.data|@json_decode}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d5efc7d664efbb07fff1ede2eebae567.png)
### SwaggerUIの確認
SwaggerUI画面より、[plain-custom-endpoint]をクリックします。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/408821848b40886fcbfd92b634733ac7.png)
[Try it out]をクリックします。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/ed40a21db9b785e925e7bdfb9a3fe25f.png)
[Execute]をクリックします。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/5601074a29c44c0cc14df57304ac1a71.png)
「Response body」には、`status`が存在しないリクエストの場合、`ANY`がレスポンスされることを確認できます。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/8f15ec125b9345903ba1454f4f9e5090.png)
### curlにて動作確認
このカスタム処理では、GETクエリの`status`に指定された値で処理を分岐しています。  

紐づいたAPIエンドポイントと合わせると、`/rcms-api/1/plain-custom-endpoint?status=...`という形のURLへGETリクエストが送信される想定です。
しかしながら、このリクエストはSwaggerUI上からは実行できないため、curlで動作確認をします。

SwaggerUIの「Curl」に記載されている内容をコピーします。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/4d14b4b3060fa78a86f090c156ed5b5a.png)
```
curl -X 'GET' \
'https://[サイトキー].g.kuroco.app/rcms-api/1/plain-custom-endpoint' \
-H 'accept: */*'
```

ターミナルを開き、コピーしたURLを貼り付け確認します。
その際に、URL末尾に`?クエリキー名=値`を指定するとGETクエリを付加できます。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/b27b4ad1dbfbb940da1b9630e5e7c83d.png)
:::tip
`status`をSwaggerUI上で指定できない理由は、[FAQ -> SwaggerUIで確認できないリクエストがあります。確認する方法はありますか？](/ja/docs/faq/how-do-i-verify-requests-that-cannot-be-verified-with-swagger-ui/)を参照してください。
:::

## 関連ドキュメント
- [カスタム処理と紐づいたAPIエンドポイントを作成する](/ja/docs/tutorials/creating-a-custom-function-endpoint/)
- [カスタム処理](/ja/docs/management/function/)
- [Swagger UIを利用して、APIのセキュリティを確認する](/ja/docs/tutorials/how-to-use-swagger-ui/)
- [カスタム処理に利用できるトリガと変数の一覧](/ja/docs/reference/trigger-variables/)


---

# Swagger UIを利用して、コンテンツのデータ構造を確認する

> 元ページ: `tutorials/using-swagger-to-check-the-structure-of-data` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/using-swagger-to-check-the-structure-of-data/

Swagger UIを利用すると、KurocoのAPIのレスポンスを確認できます。
今回はSwagger UIを利用して、コンテンツ定義で設定した拡張項目のデータ構造を確認してみます。

### 1. コンテンツ定義を作成する 
[コンテンツ定義](/ja/docs/management/content-structure-topics-group/)のページから右上の[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/7bc3399fac90126f8e7c3ae477ed3dca.png)

[コンテンツ定義編集](/ja/docs/management/content-structure-topics-group/)や[コンテンツ定義で利用できる拡張項目一覧](/ja/docs/reference/list-of-extra-column-available-on-content/)を参考に、「画像」の拡張項目を設定してコンテンツ定義を追加します。

今回は下記設定にて項目追加します。

| 設定項目 | 設定           |             |
| :------- | :------------- | :---------- |
| 項目名 | 画像 |
| 項目設定 | 画像（KurocoFilesにアップロード） |
| 拡張子 | jpeg、jpg、png |  |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bed45c8f04f29675ac416a552ae7562a.jpg)

作成したコンテンツ定義のグループIDを控えておきます。(ここでは`7`)
![Image from Gyazo](https://t.gyazo.com/teams/diverta/8a54874fc8f448f0b039a691b8f1f7ef.png)

### 2. 記事を作成する
[記事一覧](/ja/docs/management/content-structure-topics/)のページから右上の[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3780203e3397d238f77f5c61895f936d.png)

[記事編集](/ja/docs/management/content-structure-topics/)を参考に下記のように入力し、[追加する]をクリックして記事を作成します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4b877fd5a077b051292c2bdee5698350.png)

作成した記事のトピックスIDを控えておきます。(ここでは`3`)  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e0e6a55349eb14485ca2b09a7d181f9b.png)

### 3. エンドポイントを作成する
APIのページで[新しいエンドポイントの追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f74bf45953dabfbd888e0385842ff4b9.png)

今回は下記設定にてエンドポイントを作成します。

| 設定項目 | 設定           |             |
| :------- | :------------- | :---------- |
| パス | test |             |
|  | 有効/無効 | 有効 |
| モデル | カテゴリー | コンテンツ |
|  | モデル | Topics |
|  | オペレーション | Details |
| topics_group_id | 作成したコンテンツ定義のグループID（ここでは7） |  |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/143d2555a47b210844b7a97c792e50e3.jpg)

入力後、[追加する]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a7c9a61ef4438ac9fde4f9f67b9def73.png)

### 4. Swagger UIで拡張項目の構造を確認する
APIのページで[Swagger UI]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6db88e33453e407b66a18d418a3f092f.png)

先ほど作成したエンドポイントをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/86f8e4f3eff41ccd3e0ceb665b52ab5d.png)  

[Try it out]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/fa80414c9b4975615266373b09a380ed.png)

2で確認したトピックスIDを入力して、[Execute]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/cd306ec697163fb046334b6254dfdafb.png)

Responsesの項目のDetailsを確認します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/622853db60e957d130b98c47f6e90b4e.png)

拡張項目のID=1に登録した「画像」の拡張項目については下記のデータ構造になっています。

```
"ext_1": {
  "id": "3_ext_01_0",
  "url": "https://kuroco-*****.g.kuroco-img.app/v=1659513618/files/topics/3_ext_1_0.png",
  "desc": "Kurocoロゴ",
  "url_org": "https://kuroco-*****.g.kuroco-img.app/files/topics/3_ext_1_0.png"
},
```
- 画像のURL: details.ext_1.url  
- 画像の説明: details.ext_1.desc  


同じ要領で他の拡張項目や、list形式のAPIエンドポイントのレスポンスなど、様々なデータを確認できますので、フロントエンドの構築にご活用ください。

## 関連ドキュメント
- [Swagger UIを利用して、APIのセキュリティを確認する](/ja/docs/tutorials/how-to-use-swagger-ui/)
- [エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)
- [コンテンツ定義](/ja/docs/management/content-structure-topics-group/)
- [コンテンツ定義で利用できる項目設定一覧](/ja/docs/reference/list-of-extra-column-available-on-content/)
