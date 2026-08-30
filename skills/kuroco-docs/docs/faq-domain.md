# Kurocoドキュメント: FAQ / domain

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- 現在利用しているサイトURLをKurocoでも利用できますか？（`can-i-continue-to-use-my-current-site-url-in-kuroco`）
- KurocoでXMLsitemapは作成できますか（`can-i-create-xmlsitemap-with-kuroco`）
- 独自ドメインでwwwなしでもサイト表示できますか？（`can-i-display-my-site-on-custom-domain-without-www`）
- Kurocoへの移行時に既存記事のURLを変えずに移行できますか？（`can-i-migrate-to-kuroco-without-changing-existing-urls`）
- 複数の独自ドメインを使用できますか？（`can-i-use-more-than-one-domain`）
- 独自ドメインの変更方法を教えてください。（`how-do-i-change-my-domain-name`）
- 特定のIPアドレス以外はメンテナンスページを表示したいです（`how-to-display-maintenance-page-except-for-specific-ip-addresses`）
- 複数のIPアドレスをまとめて設定できますか？（`is-it-possible-to-set-multiple-ip-addresses-at-once`）
- 社内ネットワークにアクセスするドメインの許可が必要です。どのドメインが利用されていますか？（`permission-required-for-accessing-internal-network-which-domain-is-in-use`）
- ページがGoogle等の検索に引っかからないようにしたいです。（`prevent-my-webpage-from-appearing-in-search-engines`）
- Kurocoで利用するドメインの種類について教えてください（`what-types-of-domains-does-kuroco-use`）
- 使用できないURLを教えてください（`what-urls-cannot-be-used`）


---

# 現在利用しているサイトURLをKurocoでも利用できますか？

> 元ページ: `faq/can-i-continue-to-use-my-current-site-url-in-kuroco` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-continue-to-use-my-current-site-url-in-kuroco/
> 概要: URLに関しては、フロントエンド側の実装に依存します。そのため、現在のURLをkurocoでも利用できるかは、フロントエンドを構築される方にご確認いただきますようお願いいたします。

URLに関しては、フロントエンド側の実装に依存します。  
そのため、現在のURLをkurocoでも利用できるかは、フロントエンドを構築される方にご確認いただきますようお願いいたします。

その上で、Kurocoにて対応可能な項目を以下にまとめますのでご確認ください。

## 独自ドメインについて
KurocoではKurocoFrontを利用することにより、独自ドメインを設定できます。

:::info
独自ドメインの利用方法は[KurocoFrontで独自ドメインを利用する手順](/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/)をご確認ください。
:::

## コンテンツURLについて
コンテンツ投稿時に「Slug」を設定することにより、SlugをコンテンツのURLパスとして利用可能です。

:::info
参考FAQ:[コンテンツのidを指定したり、変更することはできますか？](/ja/docs/faq/can-i-specify-or-change-topic-ids/)
:::

## リダイレクトについて
KurocoFrontではリダイレクトを設定も可能です。

:::info
KurocoFrontでのリダイレクトについては、[kuroco_front.jsonとは何ですか？ -> redirects：リダイレクトの設定](/ja/docs/faq/what-is-kuroco_front_json/#redirects%EF%BC%9A%E3%83%AA%E3%83%80%E3%82%A4%E3%83%AC%E3%82%AF%E3%83%88%E3%81%AE%E8%A8%AD%E5%AE%9A)をご確認ください。
:::

## 関連ドキュメント
- [独自ドメイン/TLS証明書](/ja/docs/management/custom-domain-tls-certificate/)
- [KurocoFrontで独自ドメインを利用する手順](/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/)
- [別サイトで使用しているドメインをKurocoに切り替える際の手順](/ja/docs/tutorials/transferring-your-domain-from-another-site-to-kuroco/)
- [Kurocoへの移行時に既存記事のURLを変えずに移行できますか？](/ja/docs/faq/can-i-migrate-to-kuroco-without-changing-existing-urls/)
- [kuroco_front.jsonとは何ですか？](/ja/docs/faq/what-is-kuroco_front_json/)


---

# KurocoでXMLsitemapは作成できますか

> 元ページ: `faq/can-i-create-xmlsitemap-with-kuroco` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-create-xmlsitemap-with-kuroco/
> 概要: 現状では、XMLsitemap(sitemap.xml)を自動で作成する機能は用意しておりません。XMLsitemapはフロントエンドにて実装をお願いいたします。

現状では、XMLsitemap(sitemap.xml)を自動で作成する機能は用意しておりません。XMLsitemapはフロントエンドにて実装をお願いいたします。

## XMLsitemapを実装するには

Headless CMSでは、コンテンツ管理（バックエンド）と表示（フロントエンド）が分離されているため、
ページ数など実際の URL の構造はフロントエンド側で決定されます。(Kurocoのコンテンツ数=ページ数にはならない)  
そのため、XMLsitemapはフロント側で対応をすることが一般的です。

## 基本的な実装方法
各フレームワークごとに、実装方法は異なります。
以下のドキュメントを一例に XMLsitemap の実装方法をご検討ください。

- [Next.js](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap)
- [Nuxt 3](https://nuxtseo.com/docs/sitemap/getting-started/introduction)

### Next.js
例えば Next.js では、`app` ディレクトリに`sitemap.ts`（または`sitemap.js`）を作成することで、XML サイトマップを生成できます：

```typescript
// app/sitemap.ts
import type { MetadataRoute } from 'next';

export default function sitemap(): MetadataRoute.Sitemap {
  return [
    {
      url: 'https://www.diverta.co.jp/',
      lastModified: new Date(),
      changeFrequency: 'yearly',
      priority: 1,
    },
    {
      url: 'https://www.diverta.co.jp/about',
      lastModified: new Date(),
      changeFrequency: 'monthly',
      priority: 0.8,
    },
    {
      url: 'https://www.diverta.co.jp/products',
      lastModified: new Date(),
      changeFrequency: 'weekly',
      priority: 0.5,
    },
  ];
}
```

このコードは以下のような XML を生成します：

```xml
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://www.diverta.co.jp/</loc>
    <lastmod>2024-01-06T15:02:24.021Z</lastmod>
    <changefreq>yearly</changefreq>
    <priority>1</priority>
  </url>
  <!-- 他のURLエントリー -->
</urlset>
```

### Nuxt.js

Nuxt 3 では、[@nuxtjs/sitemap](https://nuxtseo.com/docs/sitemap/getting-started/installation) モジュールを使用して XML サイトマップを生成できます。

#### 1. モジュールのインストール

```bash
npx nuxi module add @nuxtjs/sitemap
```

#### 2. `nuxt.config.ts` での設定

```typescript
// nuxt.config.ts
export default defineNuxtConfig({
  modules: ['@nuxtjs/sitemap'],
  site: {
    url: 'https://your-site.com',
  },
});
```

この設定により、静的ページは自動的に検出されサイトマップに追加されます。生成されたサイトマップは `/sitemap.xml` で確認できます。

#### 3. 動的URLの追加

Kuroco をヘッドレス CMS として使用する場合、ブログ記事などの動的 URL をサイトマップに追加する必要があります。

##### サーバーAPIエンドポイントの作成

`server/api/__sitemap__/urls.get.ts` ファイルを作成して、Kuroco からコンテンツを取得します：

:::tip
ファイル名は `urls.get.ts` とし、`.get.ts` 拡張子を使用してください。これにより、GETリクエストとして明示的に認識されます。
:::

```typescript
// server/api/__sitemap__/urls.get.ts
import type { SitemapUrl } from '#sitemap/types';

export default defineSitemapEventHandler(async () => {
  const config = useRuntimeConfig();
  const urls: SitemapUrl[] = [];

  try {
    // ニュース記事を取得
    const newsResponse = await $fetch<any>(
      `${config.public.kurocoApiDomain}/rcms-api/1/news/list`
    );

    if (newsResponse?.list) {
      const newsUrls = newsResponse.list.map((news: any) => ({
        loc: `/news/detail/${news.topics_id}`,
        lastmod: news.ymd || news.update_date,
      }));
      urls.push(...newsUrls);
    }
  } catch (error) {
    console.error('Failed to fetch news for sitemap:', error);
  }

  return urls;
});
```

##### nuxt.config.tsの設定

`nuxt.config.ts` に以下の設定を追加します：

```typescript
// nuxt.config.ts
export default defineNuxtConfig({
  modules: ['@nuxtjs/sitemap'],

  site: {
    url: 'https://your-site.com',
  },

  sitemap: {
    // 動的URLソースを明示的に登録
    sources: [
      '/api/__sitemap__/urls',
    ],
    // 会員限定ページやプレビューページを除外
    exclude: [
      '/mypage/**',
      '/preview/**',
    ],
  },
});
```

##### 生成されるsitemap.xmlの例

上記の設定により、以下のようなsitemap.xmlが生成されます：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <!-- 静的ページ -->
    <url>
        <loc>https://your-site.com/</loc>
    </url>
    <url>
        <loc>https://your-site.com/company</loc>
    </url>
    <url>
        <loc>https://your-site.com/news</loc>
    </url>

    <!-- 動的ページ（Kurocoから取得） -->
    <url>
        <loc>https://your-site.com/news/detail/1</loc>
        <lastmod>2023-06-20</lastmod>
    </url>
    <url>
        <loc>https://your-site.com/news/detail/3</loc>
        <lastmod>2023-03-20</lastmod>
    </url>
</urlset>
```

## 関連ドキュメント
- [コンテンツ一覧/詳細ページを作成する](/ja/docs/tutorials/integrate-kuroco-with-nuxt/)
- [Nuxt.jsのSSGでページ内リンクされていないページを生成することはできますか？](/ja/docs/faq/can-i-use-nuxt-js-ssg-to-generate-pages-that-are-not-linked-in-the-page/)
- [ページがGoogle等の検索に引っかからないようにしたいです。](/ja/docs/faq/prevent-my-webpage-from-appearing-in-search-engines/)


---

# 独自ドメインでwwwなしでもサイト表示できますか？

> 元ページ: `faq/can-i-display-my-site-on-custom-domain-without-www` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-display-my-site-on-custom-domain-without-www/
> 概要: Kuroco管理画面でリダイレクトドメインの設定をすると、設定したドメインからフロントエンドドメインへのリダイレクトが可能です。

Kuroco管理画面でリダイレクトドメインの設定をすると、設定したドメインからフロントエンドドメインへのリダイレクトが可能です。

## 設定方法
[環境設定]->[[独自ドメイン/TLS証明書](/ja/docs/management/custom-domain-tls-certificate/)] にアクセスします。  

リダイレクトドメインにリダイレクト元のドメインを入力して[追加する]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f474d05ba73da2a52337a26004afc449.jpg)

ドメイン所有権の確認と、ドメインを利用する為のDNSレコードが表示されるので、DNSの設定します。 

:::tip
DNSレコードの反映及び、TLS証明書のCDNへの反映は時間がかかります。反映されない場合は少し時間をおいてから[リロードする]をクリックしてください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/efa23f5eb631483d601e56fd2636ac59.png)

表示がOKになったら設定は完了です。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5900ff6edc566f938ed969df142dffa4.png)

## リダイレクトの仕様
- リダイレクトは301リダイレクトになります。
- 同じディレクトリ構成へのリダイレクトになります。  
  例：`https://example.com/news/` → `https://www.example.com/news/`
- `http://`でアクセスした場合でも自動で`https://`にリダイレクトします。  
  例：`http://example.com/` → `https://example.com/` → `https://www.example.com/`

:::tip
リダイレクトドメインに設定できるのは1ドメインのみで、wwwなしからwwwへリダイレクトするといった用途を想定しています。  
複数のリダイレクトを実施したい場合は[サポート](/ja/docs/about/support/)にご相談ください。
:::

## 関連ドキュメント
- [KurocoFrontで独自ドメインを利用する手順](/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/)


---

# Kurocoへの移行時に既存記事のURLを変えずに移行できますか？

> 元ページ: `faq/can-i-migrate-to-kuroco-without-changing-existing-urls` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-migrate-to-kuroco-without-changing-existing-urls/
> 概要: Kurocoへの移行時に既存記事のURL（例：/blog/12345/）を変えずに移行することは可能です。移行記事にはslugを設定し、新規記事にはトリガーでslugを自動生成する方法が利用できます。

Kurocoへの移行時に既存記事のURL（例：`https://example.com/blog/12345/`）を変えずに移行することは可能です。

例えば、以下のような方法が取れます：

- 既存記事は、slugに`blog-12345`のような形式で移行
- Kuroco上で追加する新規記事は`blog-[記事ID]`で自動的にslugを作るようにトリガーを作成
- フロントエンドは、`/blog/12345/` のページでは `blog-12345` でAPIを取得

## ステップ1：既存記事をslugを設定して移行する

既存の記事をインポートする際に、現在のURLパスに合わせたslugを各記事に設定します。  
例えば、既存URLが `https://example.com/blog/12345/` の場合、slugを `blog-12345` に設定します。

:::tip
slugは[コンテンツ編集](/ja/docs/management/content-structure-topics/#content-editor)画面の「ID/Slug」フィールドで設定できます。また、[CSVでコンテンツをアップロード](/ja/docs/faq/can-i-upload-topics-using-csv-files/)する際にslug列を含めることも可能です。
:::

## ステップ2：コンテンツIDの重複を避ける

既存記事が旧IDをslugの一部として使用しているため（例：`blog-12345`）、Kurocoが自動採番する新しいコンテンツIDが移行済み記事の番号と重複しないようにする必要があります。

[環境設定 -> 管理画面](/ja/docs/management/management-screen/)の「次のコンテンツID」設定を使って、移行済み記事と重複しない番号までtopics_idの採番を飛ばしてください。

例えば、移行した記事の最大番号が`12345`の場合、次のコンテンツIDを`12346`以上に設定します。

## ステップ3：新規記事のslugを自動生成するトリガーを作成する

対象のコンテンツ定義IDに対して、トリガー[「コンテンツの追加後」](/ja/docs/reference/trigger-variables/)を設定した[カスタム処理](/ja/docs/management/function/)を作成し、新規コンテンツ追加時にslugを自動設定します。

### トリガーのサンプルコード

```smarty
{* トリガー：コンテンツの追加後 *}
{* slug を "blog-[topics_id]" の形式で自動生成する *}

{* ループの場合は処理をスキップ *}
{if $smarty.server.HTTP_RCMS_X_API_REQUEST_CNT > 0}
    {return}
{/if}

{* topics_id を使ってslugを生成 *}
{assign var='new_slug' value="blog-`$topics_id`"}

{* api_internal でコンテンツのslugを更新 *}
{assign_array var='body'      values=''}
{assign       var='body.slug' value=$new_slug}

{api_internal
    var='response'
    status_var='status'
    endpoint="/rcms-api/1/topics/`$topics_id`"
    method='POST'
    queries=$body
    use_current_session=1}
```

:::tip
移行前のURLがゼロ埋めのIDを使っている場合は、`string_format`修飾子で桁数を揃えられます（例：`{$topics_id|string_format:"%06d"}`）。詳細は[修飾子](/ja/docs/reference/smarty-php-function/#修飾子)を参照してください。
:::

:::info
- `$topics_id` は[「コンテンツの追加後」](/ja/docs/reference/trigger-variables/)トリガーで利用できる変数で、新しく作成されたコンテンツのIDがアサインされます。。
- `api_internal` プラグインは内部APIリクエストを送信してコンテンツを更新します。コンテンツ更新用のエンドポイント（例：`Topics::update`）が設定されている必要があります。詳細は[カスタム処理からKurocoのAPIを呼び出す方法](/ja/docs/faq/how-to-request-kuroco-api-from-smarty-function/)をご参照ください。
:::

## ステップ4：フロントエンドでslugを使ってコンテンツを取得する

フロントエンドでは、URLから取り出したIDを使い、Topics::details エンドポイントへslugをパスパラメータとして渡してコンテンツを取得します。

### Fetchの例（JavaScript）

```js
// 例：/blog/12345/ のようなページでslugを使ってコンテンツを取得する
const id = '12345'; // URLパスから抽出

const response = await fetch(
  `https://your-site-key.g.kuroco.app/rcms-api/1/topics_details/blog-${id}`,
  { method: 'GET' }
);

const data = await response.json();
console.log(data.details.subject); // 記事のタイトル
```

## 関連ドキュメント
- [現在利用しているサイトURLをKurocoでも利用できますか？](/ja/docs/faq/can-i-continue-to-use-my-current-site-url-in-kuroco/)
- [コンテンツのidを指定したり変更することはできますか？](/ja/docs/faq/can-i-specify-or-change-topic-ids/)
- [カスタム処理からKurocoのAPIを呼び出す方法](/ja/docs/faq/how-to-request-kuroco-api-from-smarty-function/)
- [カスタム処理に利用できるトリガと変数の一覧](/ja/docs/reference/trigger-variables/)
- [管理画面の設定](/ja/docs/management/management-screen/)


---

# 複数の独自ドメインを使用できますか？

> 元ページ: `faq/can-i-use-more-than-one-domain` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-i-use-more-than-one-domain/
> 概要: Kurocoでは、1つのサイトキーに対して1つの独自ドメインと1つのkuroco-front.appドメインをご利用いただけます。複数のドメインでサイトを構築したい場合は、サイト一覧からサブサイトを作成し、各サブサイトにご希望の独自ドメインを登録してください。

KurocoFrontでは、1つのサイトキーに対して1つの独自ドメインと1つの`kuroco-front.app`ドメインをご利用いただけます。  
複数の独自ドメインでサイトをホスティングしたい場合は、[サイト一覧](/ja/docs/management/site-list/)からサブサイトを作成し、各サブサイトにそれぞれの独自ドメインを登録してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5ea3dbf69dbfb2d9c69395655661dce8.png)

:::info
- 利用料金はメインサイトにまとめて請求されます。
- メインサイトのスーパーユーザーは、SSO（シングルサインオン）でサブサイトにもログイン可能です。
:::

:::tip
メインサイトと同じコンテンツを利用する場合でも、複数の独自ドメインでホスティングを行いたい場合は、ドメインごとにサブサイトを作成する必要があります。  
同一コンテンツの共有方法には以下の対応が考えられます。

- 同期機能を使用し、メインサイトのコンテンツをサブサイトにも登録する  
  - [同期項目一覧](/ja/docs/reference/sync-site-data/)
- サブサイトからメインサイトのコンテンツを参照する  
  - [Kurocoに登録したコンテンツを複数のサイトから利用できますか](/ja/docs/faq/can-the-content-registered-in-kuroco-be-used-from-multiple-sites/)
:::

## 関連ドキュメント
- [サイト一覧](/ja/docs/management/site-list/)
- [独自ドメイン/TLS証明書](/ja/docs/management/custom-domain-tls-certificate/)
- [同期項目一覧](/ja/docs/reference/sync-site-data/)
- [Kurocoに登録したコンテンツを複数のサイトから利用できますか](/ja/docs/faq/can-the-content-registered-in-kuroco-be-used-from-multiple-sites/)
- [Kurocoで利用するドメインの種類について教えてください](/ja/docs/faq/what-types-of-domains-does-kuroco-use/)


---

# 独自ドメインの変更方法を教えてください。

> 元ページ: `faq/how-do-i-change-my-domain-name` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-do-i-change-my-domain-name/
> 概要: KurocoFrontで設定した独自ドメインは、一度追加すると変更ができません。間違えて入力した場合は、弊社サポートまでご連絡ください。

KurocoFrontで設定した独自ドメインは、一度追加すると変更ができません。  
間違えて入力した場合は、[弊社サポート](https://kuroco.zendesk.com/)までご連絡ください。

## 関連ドキュメント
- [独自ドメイン/TLS証明書](/ja/docs/management/custom-domain-tls-certificate/)
- [KurocoFrontで独自ドメインを利用する手順](/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/)
- [別サイトで使用しているドメインをKurocoに切り替える際の手順](/ja/docs/tutorials/transferring-your-domain-from-another-site-to-kuroco/)
- [独自ドメインを設定しましたがサイトが表示できません。何を確認すれば良いでしょうか？](/ja/docs/faq/setting-up-a-custom-domain/)
- [複数の独自ドメインを使用できますか？](/ja/docs/faq/can-i-use-more-than-one-domain/)


---

# 特定のIPアドレス以外はメンテナンスページを表示したいです

> 元ページ: `faq/how-to-display-maintenance-page-except-for-specific-ip-addresses` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-to-display-maintenance-page-except-for-specific-ip-addresses/
> 概要: KurocoFrontのip_restricted_maintenance機能を使用して、特定のIPアドレス以外のアクセスに対してメンテナンスページを表示する方法を説明します。

KurocoFrontの`ip_restricted_maintenance`機能を使用して、特定のIPアドレス以外のアクセスに対してメンテナンスページを表示することができます。

## 設定概要

`ip_restricted_maintenance`設定では以下が可能です：
- 指定したIPアドレス以外の全てのアクセスにメンテナンスページを表示
- カスタムHTMLメンテナンスページの使用
- サブネットマスク記法による柔軟なIP範囲設定
- 複数のIPアドレスや範囲の設定

## 基本設定

### kuroco_front.json設定ファイル

`kuroco_front.json`設定ファイルを以下の内容で作成または更新します：

```json
{
    "ip_restricted_maintenance": [
        "111.111.111.111/32",
        "222.222.222.222/32",
        "192.168.1.0/24"
    ],
    "error_page": {
        "status_ip_503": "/maintenance.html"
    }
}
```

**フレームワーク別ファイル配置場所：**
- **Nuxt 3**: `/public/kuroco_front.json`
- **Next.js**: `/public/kuroco_front.json`
- **その他のフレームワーク**: ビルド出力のルートディレクトリ

:::tip
カスタムメンテナンスページを指定しない場合、許可されていないIPアドレスからのアクセスには標準的な「503 Service Unavailable」エラーが表示されます。
:::

### カスタムメンテナンスページ（HTML）

カスタムメンテナンスページのHTMLファイルを以下の内容で作成します：

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>メンテナンス中</title>
    <style>
        body {
            font-family: 'Hiragino Sans', 'Hiragino Kaku Gothic ProN', 'Noto Sans JP', sans-serif;
            text-align: center;
            padding: 50px;
            background-color: #f5f5f5;
            margin: 0;
        }
        .maintenance-container {
            max-width: 600px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #e74c3c;
            margin-bottom: 20px;
        }
        p {
            color: #666;
            line-height: 1.8;
            margin-bottom: 15px;
        }
        .contact {
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #eee;
            font-size: 14px;
            color: #999;
        }
    </style>
</head>
<body>
    <div class="maintenance-container">
        <h1>🔧 メンテナンス中</h1>
        <p>現在、サービス向上のため定期メンテナンスを実施しております。</p>
        <p>ご不便をおかけして申し訳ございません。</p>
        <p>メンテナンス完了まで今しばらくお待ちください。</p>
        <div class="contact">
            <p>緊急のお問い合わせ: support@example.com</p>
        </div>
    </div>
</body>
</html>
```

**フレームワーク別ファイル配置場所：**
- **Nuxt 3**: `/public/maintenance.html`
- **Next.js**: `/public/maintenance.html`

## IPアドレスの形式

| 形式 | 説明 | 例 |
|------|------|-----|
| 単一IP | 特定のIPアドレス | `"192.168.1.100/32"` |
| サブネット | CIDR記法によるIP範囲 | `"192.168.1.0/24"` |
| 複数IP | IPアドレス/範囲の配列 | `["10.0.0.1/32", "192.168.0.0/16"]` |

## 参考：KurocoEdgeとの比較

KurocoFrontでは基本的なメンテナンスシナリオに対応できますが、KurocoEdgeを利用すると、スケジュール設定されたメンテナンス時間の指定やパス単位でのアクセス制限など、より高度な設定が可能です。

詳しくは[KurocoEdge](https://kurocoedge.com/ja/)のドキュメントを参照してください。

| 機能 | KurocoFront | KurocoEdge |
|------|-------------|------------|
| IPベース制限 | ✅ | ✅ |
| カスタムメンテナンスページ | ✅ | ✅ |
| スケジュール設定 | ❌ | ✅ |
| パス固有の制限 | ❌ | ✅ |

## 関連ドキュメント
- [KurocoFront設定](/ja/docs/management/kuroco-front-settings/)
- [kuroco_front.jsonとは何ですか？](/ja/docs/faq/what-is-kuroco_front_json/)
- [時間指定でサイトをメンテナンス表示にできますか？](/ja/docs/faq/can-i-schedule-site-to-display-maintenance-at-specific-time/)
- [複数のIPアドレスをまとめて設定できますか？](/ja/docs/faq/is-it-possible-to-set-multiple-ip-addresses-at-once/)


---

# 複数のIPアドレスをまとめて設定できますか？

> 元ページ: `faq/is-it-possible-to-set-multiple-ip-addresses-at-once` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/is-it-possible-to-set-multiple-ip-addresses-at-once/
> 概要: 定数にIPSETS_*の名前で改行区切りのIPアドレスを設定すると、[[IPSETS_*]]で複数のIPアドレスのグループを設定できます。

定数に`IPSETS_*`の名前で改行区切りのIPアドレスをすると、
`[[IPSETS_*]]`で複数のIPアドレスのグループを設定できます。

## 設定例
[定数](/ja/docs/management/constants/)のページで以下のように設定します。
- 名前を`IPSETS_*`に設定する
- IPアドレスのリストを改行区切りで入力する

![Image from Gyazo](https://t.gyazo.com/teams/diverta/61c122b67b3679ca9eb95e1e6acd1899.png)

:::tip
`#コメント`の書式でIPアドレスにメモを入力できます。
:::

## 利用可能な箇所
現在は以下のIPアドレス制限に対応しています。  
IPアドレス制限の項目に、設定した定数名を`[[IPSETS_*]]`で入力します。

- API定義のIPアドレス制限
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/d8b94d50dc0c7259eb8cf6ff2d4c08ee.png)

- [環境設定]->[管理画面]の「KurocoFilesのアクセス制限(IPアドレス)」
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/69bbe3174dbc8efde4a01f872d905381.png)

- [環境設定]->[管理画面]の「Admin MCPのアクセス制限(IPアドレス)」

- [環境設定]->[管理画面]の「拒否IPアドレスの設定」
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/070de1132d063102fe9ebf0dda6c9681.png)

- [環境設定]->[サイト管理]の「投稿制限IPアドレス」  
  ※コメントの記述をサポートしていないため、定数側でもコメントを除いてIPアドレスのリストのみを描く必要があります。
  ![Image from Gyazo](https://t.gyazo.com/teams/diverta/5ac562ae2e3e1f0d021670208de423c0.png)

## 関連ドキュメント
- [定数](/ja/docs/management/constants/)
- [API セキュリティ](/ja/docs/management/api-security/)
- [管理画面](/ja/docs/management/management-screen/)
- [サイト管理](/ja/docs/management/site-settings/)
- [APIリクエスト制限の優先順位について教えてください](/ja/docs/faq/in-what-order-are-viewing-restrictions-applied/)


---

# 社内ネットワークにアクセスするドメインの許可が必要です。どのドメインが利用されていますか？

> 元ページ: `faq/permission-required-for-accessing-internal-network-which-domain-is-in-use` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/permission-required-for-accessing-internal-network-which-domain-is-in-use/
> 概要: kuroco_front.jsonとは、KurocoFrontoを利用するために必要なJSONファイルです。Kuroco_front.jsonを利用することで、リダイレクト設定やBasic認証設定、エラーページの設定が可能となります。

[環境設定] -> [[アカウント設定](/ja/docs/management/account/)]にある以下の許可をお願いいたします。

### Kurocoのドメイン

- 管理画面URL
- フロントエンド ドメイン
- APIドメイン
- KurocoFilesドメイン

### その他のドメイン
- `https://fonts.gstatic.com/`
- `https://fonts.googleapis.com/`

## 関連ドキュメント
- [アカウント設定](/ja/docs/management/account/)
- [Kurocoで利用するドメインの種類について教えてください](/ja/docs/faq/what-types-of-domains-does-kuroco-use/)
- [KurocoFilesディレクトリとドメインの使い分けについて](/ja/docs/tutorials/kurocofiles-directories-and-domains-usage/)


---

# ページがGoogle等の検索に引っかからないようにしたいです。

> 元ページ: `faq/prevent-my-webpage-from-appearing-in-search-engines` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/prevent-my-webpage-from-appearing-in-search-engines/
> 概要: フロントエンド側でrobots.txtの配置や、noindexのメタタグで実装をお願いします。

フロントエンド側でrobots.txtの配置や、noindexのメタタグで実装をお願いします。

## robots.txtを配置する場合
フロントエンドのルートディレクトリにrobots.txtを配置ください。  
Nuxt.jsの場合は`/static`ディレクトリに配置します。

## noindexのメタタグをセットする場合
`<meta name="robots" content="noindex">`のメタタグをセットください。  
Nuxt.jsの場合は、以下のようになります。

```js
export default {
  head () {
    return {
      meta: [
        { hid: 'robots', name: 'robots', content: 'noindex' }
      ]
    }
  }
}
```

:::caution
noindex が有効に機能するためには、robots.txt ファイルでページまたはリソースをブロックせず、クローラがページにアクセスできる必要があります。
:::

## 参考
- [robots.txt の概要](https://developers.google.com/search/docs/advanced/robots/intro?hl=ja)
- [noindex を使用して検索インデックス登録をブロックする](https://developers.google.com/search/docs/advanced/crawling/block-indexing?hl=ja)
- [Meta Tags and SEO](https://nuxtjs.org/ja/docs/features/meta-tags-seo/)

## 関連ドキュメント
- [サイト内で利用している静的ファイル（画像、JS、CSSなど）はどこに配置するのが良いでしょうか？](/ja/docs/faq/how-to-place-static-files/)
- [KurocoでXMLsitemapは作成できますか](/ja/docs/faq/can-i-create-xmlsitemap-with-kuroco/)
- [KurocoFrontについて](/ja/docs/about/kurocofront/)


---

# Kurocoで利用するドメインの種類について教えてください

> 元ページ: `faq/what-types-of-domains-does-kuroco-use` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/what-types-of-domains-does-kuroco-use/
> 概要: Kurocoで利用するドメインは４種類あります。各ドメインと、独自ドメインへの利用可否をまとめましたのでご確認ください。

Kurocoで利用するドメインは４種類あります。各ドメインと、独自ドメインへの利用可否をまとめましたのでご確認ください。

| 項目 | ドメイン | 独自ドメイン利用可否 | 備考 |
| :--- | :--- | :--: | :-- |
| 管理画面 | [サイトキー].g.kuroco-mng.app | × | 独自ドメインを使うにはKuroco Edge を利用する必要があります。 |
| KurocoFiles | [サイトキー].g.kuroco-img.app | ◯ | 追加費用はありませんが、利用する場合は以下を[サポート](https://kuroco.zendesk.com/hc/requests/new?ticket_form_id=900002698183)までご連絡ください。<ul><li>サイトキー</li><li>ご希望の独自ドメイン (例：`files.example.com`)</li></ul> |
| KurocoFront | [サイトキー].g.kuroco-front.app | ◯ |
| API | [サイトキー].g.kuroco.app | ◯ |

## 独自ドメインへの変更方法について

独自ドメインへ変更をご希望の場合は、下記ドキュメントをご参照ください。

### KurocoFrontを独自ドメインに変更する場合

- [KurocoFrontで独自ドメインを利用する手順](/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/)

### APIドメインを変更する場合

- [別サイトで使用しているドメインをKurocoに切り替える際の手順（APIのドメインの変更方法）](/ja/docs/tutorials/transferring-your-domain-from-another-site-to-kuroco/#4-%E7%8B%AC%E8%87%AAapi%E3%83%89%E3%83%A1%E3%82%A4%E3%83%B3%E3%82%92%E7%99%BB%E9%8C%B2%E3%81%99%E3%82%8B%E5%BF%85%E8%A6%81%E3%81%AA%E6%96%B9%E3%81%AE%E3%81%BF)

:::caution
Cookieで認証をする場合は、APIのドメインを変更する必要があります。
:::

## 関連ドキュメント
- [独自ドメイン/TLS証明書](/ja/docs/management/custom-domain-tls-certificate/)
- [KurocoFrontで独自ドメインを利用する手順](/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/)
- [別サイトで使用しているドメインをKurocoに切り替える際の手順](/ja/docs/tutorials/transferring-your-domain-from-another-site-to-kuroco/)
- [KurocoFrontで独自APIドメインを利用する手順](/ja/docs/tutorials/using-your-own-api-domain-with-kurocofront/)
- [複数の独自ドメインを使用できますか？](/ja/docs/faq/can-i-use-more-than-one-domain/)
- [独自ドメインの変更方法を教えてください。](/ja/docs/faq/how-do-i-change-my-domain-name/)


---

# 使用できないURLを教えてください

> 元ページ: `faq/what-urls-cannot-be-used` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/what-urls-cannot-be-used/
> 概要: 使用できないドメインはありません。ただし、日本語ドメインはブラウザに依存するため、弊社ではご利用を推奨しておりません。

## ドメイン
使用できないドメインはありません。  
ただし、日本語ドメインはブラウザの挙動に依存するため、弊社ではご利用を推奨しておりません。

- OK： `https://example.com`
- 非推奨： `https://てすと.com`

## ディレクトリ

KurocoFront は日本語のディレクトリ名でもホスティング可能ですが、Slugは日本語に対応していません。  
そのため、日本語ディレクトリを使用しない実装を推奨いたします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/f018fc93f1329cdcb02da4b24e1fee23.png)

:::info
Slugに使用できる文字列は以下のとおりです。
- 半角英数字
- ハイフン（-）
- アンダースコア（_）

また、以下の制限があります。
- 数字のみの Slug は使用できません
- コンテンツ定義をまたいで、サイト全体で重複はできません
:::

## 関連ドキュメント
- [独自ドメイン/TLS証明書](/ja/docs/management/custom-domain-tls-certificate/)
- [KurocoFrontで独自ドメインを利用する手順](/ja/docs/tutorials/using-a-custom-domain-name-on-kurocofront/)
- [Kurocoで利用するドメインの種類について教えてください](/ja/docs/faq/what-types-of-domains-does-kuroco-use/)
- [他のコンテンツと同じSlugを設定できますか？](/ja/docs/faq/can-i-set-the-same-slug-as-other-content/)
