# Kurocoドキュメント: FAQ / api-error

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- カスタム処理でデバッグを目的としたログを出力できますか？（`can-the-original-process-output-logs-for-debugging-purposes`）
- HARファイルの作り方を教えてください（`how-do-i-create-a-har-file`）
- Smarty エラーが発生しました。原因を教えてください。（`how-do-i-handle-errors-in-smarty`）
- Smartyでif文やforeachを使って記述を行なっていると、改行の出力がされない時があります解決方法を教えてください。（`how-do-i-insert-line-breaks-with-smarty-if-statements`）
- SwaggerUIで確認できないリクエストがあります。確認する方法はありますか？（`how-do-i-verify-requests-that-cannot-be-verified-with-swagger-ui`）
- PCのブラウザでJSエラーを確認する方法を教えてください。（`how-to-check-for-js-errors-in-a-pc-browser`）
- CORS設定の変更が反映されません。（`i-changed-cors-but-it-is-not-reflected`）
- 制限をかけていないのにAPIから403 forbidden が返ってきます（`the-api-returns-403-forbidden-even-though-no-restrictions-are-applied`）
- iPhoneやSafariでAPIと連携できないです。（`unable-to-connect-to-the-api-from-iphone-or-safari`）
- ログインロックについて教えてください。（`what-causes-accounts-to-be-locked`）
- APIが動かないです。どうしたらよいですか？（`what-should-i-do-if-the-api-is-not-working`）
- エラー発生時の確認方法を教えてください（`what-should-i-do-in-case-of-errors`）
- APIのエラーメッセージ一覧はありますか？（`where-can-i-find-a-list-of-api-error-messages`）


---

# カスタム処理でデバッグを目的としたログを出力できますか？

> 元ページ: `faq/can-the-original-process-output-logs-for-debugging-purposes` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/can-the-original-process-output-logs-for-debugging-purposes/
> 概要: カスタム処理の気になる箇所で下記のような記述を追加すると、変数の中身を確認できます。

カスタム処理の気になる箇所で下記のような記述を追加すると、変数の中身を確認できます。  

## loggerのプラグインを利用する
こちらのログは[カスタムログ](/ja/docs/management/custom-log-list/)で確認ができます。  
実行した結果をログに残したい場合はこちらをご利用ください。  

### 記述例

```smarty
{logger msg1=$json msg2=$output msg3=$smarty.requrst msg4=$example}
```

### ログの確認方法
[ログ管理]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6ebf4c8775159cbff04a6d18469039f2.png)
[ログ管理]のプルダウンメニューから[カスタムログ]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/80b9cab6214d79eea9009f07a24c47b5.png)
ログの内容が表示されます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4ca6ec4b619fe133273157dcd0d2fe36.png)
## `@debug_print_var` を利用する
loggerのプラグインはデータが大きいと、ログに残せない場合があります。  
大きいデータを扱う場合や、機能の実装中にその場でデータの内容を確認する場合はこちらをご利用ください。  
`@debug_print_var` の出力結果はログに残りません。

### 記述例

```smarty
test:{$json|@debug_print_var}
```

### ログの確認方法
[カスタム処理編集](/ja/docs/management/function/#カスタム処理編集)の画面で[テストする]をクリックすると[出力]の項目に表示されます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b28aab012f22f2f018e040f088fadd95.png)

## `put_file` を利用してKurocoFilesに保存する
loggerプラグインは1KBを超えるデータの場合、`...Over 1kb data.`と表示され途中で切り詰められるため、全体を確認できません。  
大きいデータをファイルとして保存したい場合は`put_file`プラグインを利用してKurocoFilesに保存できます。

### 記述例

```smarty
{assign var=filename value="/files/ltd/debug_"|cat:$row.topics_id|cat:"_"|cat:$smarty.now|cat:".json"}
{put_file value=$row|@json_encode path=$filename}
```

上記の例では、`$row`変数の内容をJSON形式で`/files/ltd/`ディレクトリに保存します。  
ファイル名にはコンテンツIDとタイムスタンプを含めることで、複数回実行しても上書きされないようにしています。

### ログの確認方法
[ファイル管理] -> [KurocoFiles]をクリックし、`ltd`フォルダを開くと保存したファイルを確認できます。  
ファイルをダウンロードして内容を確認してください。

:::tip
`/files/ltd/`ディレクトリは管理者のみがアクセスできるため、デバッグ用のログファイルの保存先として適しています。  
公開しても問題ないファイルの場合は`/files/user/`ディレクトリも利用できます。
:::

## 関連ドキュメント
- [カスタム処理](/ja/docs/management/function/)
- [カスタムログ](/ja/docs/management/custom-log-list/)
- [ログ管理](/ja/docs/management/log-management/)
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)


---

# HARファイルの作り方を教えてください

> 元ページ: `faq/how-do-i-create-a-har-file` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-do-i-create-a-har-file/
> 概要: 表示が遅い等のブラウザ由来の問題が発生しているときに作成したHARファイルを調べることで、問題発生時にブラウザが生成したネットワークリクエストに関する詳細情報を確認できます。

## HARファイルについて
表示が遅い等のブラウザ由来の問題が発生しているときに作成したHARファイルを調べることで、問題発生時にブラウザが生成したネットワークリクエストに関する詳細情報を確認できます。
 
## HARファイルの作り方
### Chrome
1. Google Chromeを開き、問題が発生しているページにアクセスする  
2. Chromeのメニューバー（要素を検証）から「表示」->「デベロッパー」->「デベロッパーツール(開発ツール)」を選択する  
3. 画面下部に表示されたパネルで、「Network」タブを選択する  
4. 左上端にある丸いRecordボタンを探し、ボタンが赤くなっていることを確認する  <br/>注意) ボタンが灰色になっている場合は、1回クリックすると赤くなります  
5. チェックボックス「Preserve log」にチェックを入れる  
6. Clearボタン（斜線が入った丸）をクリックして、既存のログをすべて消去する  
7. 発生した問題を再現する  
8. 問題が再現できたら、[Network] パネルの上部にあるアクションバーで、[download Export HAR (sanitized)...] をクリックし、HAR ファイルを保存する  

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/58598c5b759f100e0d46a62e223e8c69.gif)

:::tip
さらに詳しい操作方法は、[Chromeの公式ドキュメント](https://developer.chrome.com/docs/devtools/network/reference?hl=ja#export)をご覧ください。
:::

### Firefox
1. Firefoxで、問題が発生しているページを表示する  
2. ウィンドウ右上にあるFirefoxメニュー（3本の平行線）を選択し、「ウェブ開発」->「ウェブ開発ツール」を選択する  
3. 画面下部に表示されたパネルで、「ネットワーク」タブをクリックして、問題の動作を再現する<br/>注意) 記録は自動的に開始するので、ブラウザで実行してください  
4. すべてのアクションが開発者ネットワークパネルで生成されたことを確認したら、ネットワークパネル「ファイル」列の下の任意の場所を右クリックして、「HAR形式で全て保存」をクリックする  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/b05a7bf56e203d0250bce345e383c693.gif)

:::tip
さらに詳しい操作方法は、[Firefoxのソースドキュメント](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/toolbar/index.html)をご覧ください。
:::

### Microsoft Edge
1. Microsoft Edgeで、問題が発生しているページを表示する  
2. ページ上で右クリックし、ドロップダウンメニューから「開発者ツールで調査する」を選択する
3. 表示されたパネルの「Network (ネットワーク)」タブをクリックする  
4. 左上にある丸い「記録（Record）」ボタンを探し、それが赤色であることを確認する<br/> ボタンが灰色の場合は、一度クリックすると赤色になります
5. チェックボックス「Preserve log」にチェックを入れる
6. Clearボタン（斜線が入った丸）をクリックして、既存のログをすべて消去する
7. 発生した問題を再現する
8. 問題が再現できたら、[Network] パネルの上部にあるアクションバーで、[download Export HAR (sanitized)...] をクリックし、HAR ファイルを保存する  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/ed1dca0c49d0812317d763b45a92d7ab.gif)

:::tip
さらに詳しい操作方法は、[Microsoft Edgeの公式ドキュメント](https://learn.microsoft.com/ja-jp/microsoft-edge/devtools-guide-chromium/network/reference#export-requests-data)をご覧ください。
:::

## 注意事項
- ブラウザの項目名やボタンの位置は、ブラウザ側の仕様変更で本FAQの内容と異なる場合があります。　
- その他のブラウザでの生成方法は、「ブラウザ名　HARファイル　作り方」などのワードで検索エンジンにてご確認ください。
- HARファイルには、個人情報データが含まれます。
- HARファイルに含まれる個人情報や認証情報はお客様側でマスクして送付ください。
- Kurocoサポートへのお問い合わせの際は、HARファイルを添付して[サポート](https://kuroco.zendesk.com/)までお送りください。

## 関連ドキュメント
- [HARファイルを作成する](/ja/docs/tutorials/create-a-har-file/)
- [CDNにキャッシュされたレスポンスかどうかの確認方法を教えてください](/ja/docs/faq/how-do-i-verify-responses-in-the-cdn-cache/)
- [KurocoFrontでどのハッシュが利用されているかの確認方法を教えてください](/ja/docs/faq/how-do-i-verify-the-hash-responses-used-by-kurocofront/)
- [PCのブラウザでJSエラーを確認する方法を教えてください。](/ja/docs/faq/how-to-check-for-js-errors-in-a-pc-browser/)
- [お問い合わせのしおり](/ja/docs/troubleshooting/contact-guidelines/)


---

# Smarty エラーが発生しました。原因を教えてください。

> 元ページ: `faq/how-do-i-handle-errors-in-smarty` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-do-i-handle-errors-in-smarty/
> 概要: コンテンツ定義編集の「CSS」、ダッシュボードのウィジェット、カスタム処理編集などではSmartyを利用しているため、タグの属性が不足していたり、誤った変数名を指定していた時などに、次の例のようなエラーが表示されます。

[コンテンツ定義編集](/ja/docs/management/content-structure-topics-group/#コンテンツ定義編集)の「CSS」、[ダッシュボードのウィジェット](/ja/docs/management/dashboard-widget/)、[カスタム処理編集](/ja/docs/management/function/#カスタム処理編集)などではSmartyを利用しているため、タグの属性が不足していたり、誤った変数名を指定していた時などに、次の例のようなエラーが表示されます。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/7b93e994e30cc0c9f18a631b0425ea56.png?witdh=600)
 [line 4]は、エラー行番号、 syntax error: unrecognized tag: はエラー内容を示します。

原因としてよくある例としては、CSSやjavascriptなどで`{ }`を使用している場合です。  
`{ }`の部分を`{literal}` `{/literal}`で囲むように記述すると解消しますので、下記の例をご参照の上、設定してください。

例) コンテンツ定義編集の「CSS」に入力し、コンテンツ編集画面で「その他の設定」「関連するタグ」「公開時連携の設定」の表示を消す記述
```
{literal}
#detail_setting{display:none;}
#tag_edit{display:none;}
#open_action_setting{display:none;}
{/literal}
```

## 関連ドキュメント
- [Smartyエラーログ](/ja/docs/management/smarty-log-list/)
- [KurocoのSmarty基本構文](/ja/docs/reference/basic-syntax-kuroco-smarty/)
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)
- [Smartyのマニュアルはありますか？](/ja/docs/faq/where-can-i-find-the-manual-for-smarty/)
- [Smartyでif文やforeachを使って記述を行なっていると、改行の出力がされない時があります解決方法を教えてください。](/ja/docs/faq/how-do-i-insert-line-breaks-with-smarty-if-statements/)


---

# Smartyでif文やforeachを使って記述を行なっていると、改行の出力がされない時があります解決方法を教えてください。

> 元ページ: `faq/how-do-i-insert-line-breaks-with-smarty-if-statements` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-do-i-insert-line-breaks-with-smarty-if-statements/
> 概要: 下記タグの後ろにある改行はHTMLに変換される場合は削除されます。下記のように記載すると、改行されるようになります。

下記タグの後ろにある改行はHTMLに変換される場合は削除されます。

- `{if}`
- `{/if}`
- `{else}`
- `{elseif}`
- `{foreach}`
- `{/foreach}`
- `{section}`
- `{/section}`

## 改行したい場合
下記のように記載すると、改行されるようになります。 

```smarty title="コード例"
{if true}[改行]
Smartyのテスト[改行]
{else}[改行]
これは表示されない[改行]
{/if}[改行]
テスト文章  
```

```header title="表示例"
Smartyのテスト[改行]
テスト文章
```
 
## 改行しない場合
下記のように記載すると改行されません。
 
```smarty title="コード例"
{if true}Smartyのテスト{else}これは表示されない{/if}
テスト文章
```

```header title="表示例"
Smartyのテストテスト文章  
```

## 関連ドキュメント
- [KurocoのSmarty基本構文](/ja/docs/reference/basic-syntax-kuroco-smarty/)
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)
- [Smarty エラーが発生しました。原因を教えてください。](/ja/docs/faq/how-do-i-handle-errors-in-smarty/)
- [Smartyのマニュアルはありますか？](/ja/docs/faq/where-can-i-find-the-manual-for-smarty/)


---

# SwaggerUIで確認できないリクエストがあります。確認する方法はありますか？

> 元ページ: `faq/how-do-i-verify-requests-that-cannot-be-verified-with-swagger-ui` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-do-i-verify-requests-that-cannot-be-verified-with-swagger-ui/
> 概要: エンドポイント作成時に、カスタム処理を利用しGETクエリの内容で処理分岐させる場合、SwaggerUIでは確認できない場合があります。その場合は、SwaggerUIに表示されているCurlコマンドをコピーし、ターミナルで実行すると確認ができます。

エンドポイント作成時に、カスタム処理を利用しGETクエリの内容で処理分岐させる場合、SwaggerUIでは確認できない場合があります。

その場合は、SwaggerUIに表示されているCurlコマンドをコピーし、ターミナルで実行すると確認ができます。

## Curlの確認方法
対象のエンドポイントのSwaggerUIを開き、「Curl」に記載されている内容をコピーします。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/4d14b4b3060fa78a86f090c156ed5b5a.png)  

```
curl -X 'GET' \
'https://[サイトキー].g.kuroco.app/rcms-api/1/plain-custom-endpoint' \
-H 'accept: */*'
```

ターミナルを開き、コピーしたURLを貼り付け確認します。
その際に、URL末尾に`?クエリキー名=値`を指定するとGETクエリを付加できます。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/2b7664df5a9496ec7fbe1465636430d2.png)
## SwaggerUIを利用できない理由

SwaggerUIは、Kurocoが持つOpenAPIの仕様に準拠して画面を生成します。  
このため、OpenAPIの定義以外のリクエストをしたい場合はSwaggerUIで確認ができず、Curlを利用し独自にリクエストする必要があります。

例えば、カスタム処理が`status`というGETクエリの内容で処理分岐させる場合、SwaggerUIで確認はできません。  
SwaggerUIでは`status`パラメータは表示されないためです。

![fetched from Gyazo](https://t.gyazo.com/teams/diverta/82a06a58cac2c012c0324a8434708be7.png)
このように、カスタム処理でリクエストのstatusパラメータから処理を分岐した場合はOpenAPIの定義外となります。  
そのため、SwaggerUIではカスタム処理が期待するリクエストを発行できません。

SwaggerUIで確認ができない場合、今回のようにCurlにて確認をお願い致します。

## 関連ドキュメント
- [API](/ja/docs/management/api-list/)
- [Swagger UIを利用して、APIのセキュリティを確認する](/ja/docs/tutorials/how-to-use-swagger-ui/)
- [Swagger UIを利用して、コンテンツのデータ構造を確認する](/ja/docs/tutorials/using-swagger-to-check-the-structure-of-data/)
- [カスタム処理と紐づいたAPIエンドポイントを作成する](/ja/docs/tutorials/creating-a-custom-function-endpoint/)


---

# PCのブラウザでJSエラーを確認する方法を教えてください。

> 元ページ: `faq/how-to-check-for-js-errors-in-a-pc-browser` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/how-to-check-for-js-errors-in-a-pc-browser/
> 概要: ブラウザのコンソール画面より、JSエラーが発生しているかどうかを確認できます。各ブラウザのオフィシャルサイトにコンソールの確認方法の記載がありますので、以下をご案内いたします。

ブラウザのコンソール画面より、JSエラーが発生しているかどうかを確認できます。  
各ブラウザのオフィシャルサイトにコンソールの確認方法の記載がありますので、以下をご案内いたします。

## ブラウザのコンソール画面確認方法
### Google Chromeの場合
[Google Chrome](https://developers.google.com/web/tools/chrome-devtools/console)の「コンソールを開く」にあるリンクをご確認ください。  

### Firefoxの場合
[MDN Web Docs](https://developer.mozilla.org/ja/docs/Tools/Web_Console)の「ウェブコンソールを開く」をご確認ください。 

### Microsoft Edgeの場合
[Microsoft Docs](https://docs.microsoft.com/ja-jp/microsoft-edge/devtools-guide-chromium/console/reference)の「コンソール ツールを開く」をご確認ください。

## 関連ドキュメント
- [JavaScriptログ](/ja/docs/management/js-log-list/)
- [エラー発生時の確認方法を教えてください](/ja/docs/faq/what-should-i-do-in-case-of-errors/)
- [HARファイルの作り方を教えてください](/ja/docs/faq/how-do-i-create-a-har-file/)
- [PCブラウザのバージョンの確認方法を教えてください](/ja/docs/faq/how-do-i-check-my-browser-version/)


---

# CORS設定の変更が反映されません。

> 元ページ: `faq/i-changed-cors-but-it-is-not-reflected` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/i-changed-cors-but-it-is-not-reflected/
> 概要: プリフライトリクエストでチェックされたCORS（Cross-Origin Resource Sharing）は、レスポンスヘッダーのAccess-Control-Max-Ageで指定された秒数だけキャッシュされています。

プリフライトリクエストでチェックされたCORS（Cross-Origin Resource Sharing）は、レスポンスヘッダーのAccess-Control-Max-Ageで指定された秒数だけキャッシュされています。  
Access-Control-Max-Ageの値を確認し、ブラウザのキャッシュをクリアするか、Access-Control-Max-Ageを0に手動設定してください。

## 参考URL 
- [CORS](https://developer.mozilla.org/ja/docs/Web/HTTP/CORS)  
- [Access-Control-Max-Age](https://developer.mozilla.org/ja/docs/Web/HTTP/Headers/Access-Control-Max-Age)

## 関連ドキュメント
- [API セキュリティ](/ja/docs/management/api-security/)
- [APIが動かないです。どうしたらよいですか？](/ja/docs/faq/what-should-i-do-if-the-api-is-not-working/)
- [制限をかけていないのにAPIから403 forbidden が返ってきます](/ja/docs/faq/the-api-returns-403-forbidden-even-though-no-restrictions-are-applied/)
- [iPhoneやSafariでAPIと連携できないです。](/ja/docs/faq/unable-to-connect-to-the-api-from-iphone-or-safari/)


---

# 制限をかけていないのにAPIから403 forbidden が返ってきます

> 元ページ: `faq/the-api-returns-403-forbidden-even-though-no-restrictions-are-applied` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/the-api-returns-403-forbidden-even-though-no-restrictions-are-applied/
> 概要: いくつかのエンドポイントはセキュリティ上、ログイン状態での利用が前提となっており、直接パブリックに利用できません。ログイン処理後に取得するように設計するか、カスタム処理を利用してレスポンスを取得してください。

コンテンツの作成をするAPI(Topics::insert)など、いくつかのエンドポイントはセキュリティ上、ログイン状態での利用が前提となっており、直接パブリックに利用できません。
ログイン処理後に利用するように設計するか、カスタム処理を利用してエンドポイントにリクエストを送ってください。  

カスタム処理を利用して認証状態を付与した状態でエンドポイントを利用する方法には以下があります。

## api_internal を利用する方法
Api::request_api のエンドポイントで、カスタム処理を呼び出し、呼び出されたカスタム処理で api_internal のプラグインを利用することで、認証情報を付与したい状態でTopics:insertのエンドポイントにリクエストを送ります。  
api_internal では `member_id`パラメータを渡すことで、指定したメンバーIDが認証された状態でリクエストを実行できます。

### カスタム処理の設定
まず[カスタム処理](/ja/docs/management/function/)で以下のコードを設定します。

```smarty
{* リクエスト ボディ *}
{assign_array var='body'            values=''}
{assign       var='body.subject'    value=$smarty.request.subject}

{api_internal
    var='response'
    status_var='status'
    endpoint='/rcms-api/39/topics/insert'
    method='POST'
    queries=$body
    member_id='1'}

{assign var=data value=$response}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/14c79cc9fdf10d1a51c377b34c1730c4.png)

:::caution
`/rcms-api/39/topics/insert`のエンドポイントは Topics::insert のエンドポイントを使用し、APIの認証方式は「動的アクセストークン」に設定してください。
:::

### エンドポイントの設定
次にApi::request_api_post のエンドポイントを作成します。  
nameにはカスタム処理で設定した識別子を入力してください。  
また、APIは`/rcms-api/39/topics/insert`とは別にしてパブリックな認証にして下さい。  

例)  
Topics::insert：APIのセキュリティを動的アクセストークンにする。    
Api::request_api_post：APIのセキュリティをCookieにする。 

![Image from Gyazo](https://t.gyazo.com/teams/diverta/51abf9df3a797c09386c82ca5b90fb75.png)

Swagger UI でrequest_api_postのエンドポイントを叩くと、コンテンツが追加できていることが分かります。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c1f273d6911ab283f1827592b8d709fd.png)

## 前処理を利用する方法
権限を持ったメンバーIDでログインするカスタム処理を作成し、エンドポイントの前処理に設定することでレスポンスを取得します。  

### カスタム処理の設定
まず[カスタム処理](/ja/docs/management/function/)で以下のコードを設定します。コンテンツ定義の閲覧権限をもっているメンバーIDを指定してください。   

```smarty
{login member_id=1 overwrite=false} {* member_id:1としてログインをします *}
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/67da285ec25e4882a9464aaa68ae72a4.png)

### エンドポイントの設定
つづいて、追加したカスタム処理をTopics::insert のエンドポイントの前処理に設定します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/32a842214d9fb33fa62712529f51407e.png)

Swagger UI でエンドポイントを叩くと、コンテンツが追加できていることがわかります。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5c8ad254937ef43e81f00c3d3c2072d8.png)

## 関連ドキュメント
- [カスタム処理からKurocoのAPIを呼び出せますか？](/ja/docs/faq/how-to-request-kuroco-api-from-smarty-function/)
- [カスタム処理と紐づいたAPIエンドポイントを作成する](/ja/docs/tutorials/creating-a-custom-function-endpoint/)
- [Pre-processing](/ja/docs/reference/pre-processing/)
- [Smartyプラグイン](/ja/docs/reference/smarty-plugin/)


---

# iPhoneやSafariでAPIと連携できないです。

> 元ページ: `faq/unable-to-connect-to-the-api-from-iphone-or-safari` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/unable-to-connect-to-the-api-from-iphone-or-safari/
> 概要: Cookieによる認証を利用する場合、APIドメインとフロントエンドの登録可能ドメイン（eTLD+1）が異なると、Safariは認証Cookieをサードパーティ扱いしてブロックします。本ページでは原因、推奨構成、CNAMEベースのカスタムドメインに対するSafariの「7日間Cookie上限」について説明します。

## 症状

Safari（macOS / iOS / iPadOS）でCookie認証が断続的に失敗します。ログイン直後にAPIが 401 / 403 を返す、ユーザーが何度もログアウトされる、同じフローがChromeでは動作する、といった事象が起きます。これは Kuroco API が発行する認証Cookieが**サードパーティCookie**として扱われているためです。

## なぜ発生するのか

Cookieが**ファーストパーティ**として扱われるのは、Cookieのホストとページが同じ**登録可能ドメイン（eTLD+1）**を共有している場合のみです。クロスサイトCookieに対するブラウザの既定動作は次の通りです。

| ブラウザ | クロスサイトCookieの既定動作 |
| --- | --- |
| Safari | デフォルトでブロック（`SameSite=None; Secure` を付けても、「サイト越えトラッキングを防ぐ」が既定で有効なため拒否） |
| Firefox | Total Cookie Protectionによりトップレベルサイトごとに分離 |
| Chrome / Edge | `SameSite=None; Secure` で許可 |

Kurocoのデフォルト構成では登録可能ドメインが異なります — `www.example.com`（eTLD+1: `example.com`）と `example.a.kuroco.app`（eTLD+1: `kuroco.app`）— このため Safari は認証Cookieを破棄します。

## 推奨構成

カスタム APIドメインを設定し、フロントエンドとAPIで同じ登録可能ドメインを共有します。次のどちらでも構いません。

- `https://www.example.com` + `https://api.example.com`
- `https://example.com` + `https://api.example.com`

これによりCookieはファーストパーティ扱いとなり、デフォルトの `SameSite=Lax` で十分、Safari / Firefox の制限も対象外になります。

設定手順:

1. [独自ドメイン/TLS証明書](/ja/docs/management/custom-domain-tls-certificate/)で `api.example.com` を登録し、Kuroco環境に紐づける
2. [アカウント設定](/ja/docs/management/account/)からAPIベースURLを更新する

## ⚠️ 注意：Safariの7日間Cookie上限

親ドメインを揃えても、SafariはCookieの `Max-Age` / `Expires` を**7日**に制限する場合があります。KurocoのカスタムAPIドメインは `<sitekey>.g.kuroco.app` へのCNAMEで構成されており、WebKitのCNAMEクローキング対策（Safari 14で導入、Safari 16.4でページのサーバーとIPレンジが大きく異なる A/AAAA レコードにも拡張）がこの種のホストのCookieを7日に丸めるためです。CNAMEからAレコードに切り替えても回避できません — KurocoのAPI配信IPはフロントの配信IPとは別レンジになるため、Safari 16.4 以降は同じ扱いになります。

Cookie自体はブロックされず、アクティブなセッション中は正常に動作します。ただし7日以上アクセスのないユーザーは再ログインが必要になります。

| ユースケース | 影響 |
| --- | --- |
| 毎日利用される社内ツール / ダッシュボード | ✅ 実質的に問題なし |
| マーケティングサイト / 短期セッション用途 | ✅ 実質的に問題なし |
| ログイン頻度が低い一般公開サイト | ⚠️ Safariユーザーが予期せずログアウトされる可能性あり |
| Safariで長期の「ログイン状態を保持」 | ❌ Cookieでは不可。トークン認証を利用 |

### 回避策：トークン認証

**トークン認証**に切り替えてください。アクセストークンはCookieではなく `X-RCMS-API-ACCESS-TOKEN` リクエストヘッダーで送られるため、ITPのCookie制限の対象外です。リフレッシュトークンを使えば、ユーザーに再ログインを強いることなくアクセストークンを更新できます。

## 設定例

### ❌ API連携ができない例（Safariがクロスサイト Cookie をブロック）
- フロントエンド：`https://www.example.com`
- API：`https://example.a.kuroco.app`

### ✅ 推奨構成
- フロントエンド：`https://www.example.com`（または `https://example.com`）
- API：`https://api.example.com`

**※Cookie認証を利用していない場合は、ドメインを変更する必要はありません。** トークン認証は本問題の影響を受けません。

## 開発時のヒント

本事象は Chrome のデフォルト設定では発生しないため、開発時は Chrome が便利です。本番リリース前には Safari（macOS / iOS）でログインフロー、セッション継続、（長期セッションが要件であれば）7日以上アクセスしなかった後の挙動を確認してください。

:::info
APIドメインの設定手順の詳細は、[KurocoFrontで独自APIドメインを利用する手順](/ja/docs/tutorials/using-your-own-api-domain-with-kurocofront/)をご確認ください。
:::

## 関連ドキュメント
- [独自ドメイン/TLS証明書](/ja/docs/management/custom-domain-tls-certificate/)
- [アカウント設定](/ja/docs/management/account/)
- [KurocoFrontで独自APIドメインを利用する手順](/ja/docs/tutorials/using-your-own-api-domain-with-kurocofront/)
- [Kurocoで利用するドメインの種類について教えてください](/ja/docs/faq/what-types-of-domains-does-kuroco-use/)


---

# ログインロックについて教えてください。

> 元ページ: `faq/what-causes-accounts-to-be-locked` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/what-causes-accounts-to-be-locked/
> 概要: ログインがロックされるパターンは以下の通りです。Kurocoで共通の処理でロックされた。「ログインロック機能を使う」の機能でロックされた。

ログインロックがされると、正しいID/パスワードを入力してもログインに失敗するようになり、
対象メンバーのメンバー編集画面に`このメンバーはログインがロックされています。`のメッセージが表示されます。

ログインがロックされるパターンは以下の通りです。
 
## Kurocoで共通の処理でロックされた
### 原因
ログインフォームから複数回ログインに失敗した場合、Kurocoで共通に処理されているロック機能に引っかかります。
### 解決方法
1時間ほど時間をおくと、自動的に解除されます。

## 「ログインロック機能を使う」の機能でロックされた
### 原因
サイト管理の「ログインロック機能を使う」を利用している場合、5回ログインに失敗するとアカウントがロックされます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ee00b0ed0bc1473354ab8c239397e807.png)

### 解決方法
管理者が、[メンバー管理] -> [メンバー]で該当メンバーの編集画面を更新すると、ロックを解除できます。値や設定の変更などは必要ありませんので、そのまま更新してください。  

## 補足
- エラーメッセージではKurocoの共通の処理でのロックか、サイト管理での設定のロックかは区別がつきませんので、まずはサイト管理の「ログインロック機能を使う」の利用の有無をご確認ください。
- [オペレーション] -> [ログ管理] -> [ログインログ]を参照することで解決の手助けになる場合があります。

:::info
参考：管理画面マニュアル [ログインログ](/ja/docs/management/login-log-list/)
:::

- サイト管理者含めて全員ロックされている場合には、[サポート事務局](https://kuroco.zendesk.com/)までご連絡ください。

## 関連ドキュメント
- [ログインログ](/ja/docs/management/login-log-list/)
- [サイト管理](/ja/docs/management/site-settings/)
- [メンバー](/ja/docs/management/member/)
- [ログイン履歴の記録ロジックに関して教えてください](/ja/docs/faq/what-is-the-logic-behind-the-login-history/)


---

# APIが動かないです。どうしたらよいですか？

> 元ページ: `faq/what-should-i-do-if-the-api-is-not-working` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/what-should-i-do-if-the-api-is-not-working/
> 概要: まずは、APIへのリクエストに対してどのようなレスポンスが返ってきているかを確認してください。以下レスポンスの例を記載します。

まずは、APIへのリクエストに対してどのようなレスポンスが返ってきているかを確認してください。  
以下レスポンスの例を記載します。  

|JSONレスポンス|説明|
|:---|:---|
|```{"errors":["[GW] Malformed API URL"]}```|APIのエンドポイントのURIが間違っています。URIが合っているかご確認ください。|
|```{"errors":["[GW] API using this method and path does not exist"]}```|Method（POST/GETなど）が間違っています。Methodが合っているかご確認ください。|
|```{"errors":[{"code":"not_found","message":""}],"x-rcms-request-id":"****"}```|IDが異なる、またはデータがない状態です|
|```{"errors":["[GW] Access Token is required"]}```|トークンが必要なAPIでトークンがリクエストに含まれていないようです。|
|```{"errors":[{"code":"unprocessable_entity","message":"*****"}],"x-rcms-request-id":"*****"}```|何らかの処理の途中でエラーが発生しているようです。エラーメッセージをご確認ください。|
|リダイレクトされる|APIのエンドポイントのURIが間違っています。URIが合っているかご確認ください。|

:::tip
APIエラーレスポンスに関しては下記ページをご確認ください。  
- [APIエラーレスポンス](/ja/docs/reference/error/)
:::

エラーの内容が分からない場合はHARファイルを取得の上、サポートまでお問い合わせください。  
- [HARファイルの作り方を教えてください](/ja/docs/faq/how-do-i-create-a-har-file/)
- [フォームより問い合わせをする](https://kuroco.zendesk.com/hc/ja)

## 関連ドキュメント
- [APIログ](/ja/docs/management/api-log-list/)
- [APIエラーレスポンス](/ja/docs/reference/error/)
- [エラー発生時の確認方法を教えてください](/ja/docs/faq/what-should-i-do-in-case-of-errors/)
- [HARファイルの作り方を教えてください](/ja/docs/faq/how-do-i-create-a-har-file/)
- [制限をかけていないのにAPIから403 forbidden が返ってきます](/ja/docs/faq/the-api-returns-403-forbidden-even-though-no-restrictions-are-applied/)


---

# エラー発生時の確認方法を教えてください

> 元ページ: `faq/what-should-i-do-in-case-of-errors` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/what-should-i-do-in-case-of-errors/
> 概要: エラーが発生したときは、まずは下記ドキュメントを参考にエラーログを確認してください。

エラーが発生したときは、まずは下記ドキュメントを参考にエラーログを確認してください。

- [ログインログ](/ja/docs/management/login-log-list/)
- [APIログ](/ja/docs/management/api-log-list/)
- [管理画面ログ](/ja/docs/management/admin-log-list/)
- [メールログ](/ja/docs/management/mail-log-list/)
- [バッチログ](/ja/docs/management/batch-log-list/)
- [KurocoFilesログ](/ja/docs/management/img-log-list/)
- [KurocoFrontログ](/ja/docs/management/front-log-list/)
- [アプリケーションログ](/ja/docs/management/application-log-list/)

エラーログからエラーが解決できない場合、下記パターンを参考にサポート事務局まで[お問い合わせ](https://kuroco.zendesk.com/)ください。

## フロントエンドでエラーが発生した場合

### 問い合わせる前に確認すること
ブラウザ上で事象を再現し、HARファイルを作成してください。  

:::info
[HARファイルの作り方を教えてください](/docs/faq/how-do-i-create-a-har-file)
:::

### 問い合わせに必要な内容
- サイトURL
- HARファイル
- 事象の詳細、再現手順
- ご利用環境（OS,ブラウザ）
- 事象がいつから発生しているか

## APIでエラーが発生した場合

### ログの確認方法
[オペレーション] → [ログ管理] → [[APIログ](/ja/docs/management/api-log-list/)] をご確認ください。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/2db5369ac97f6d2f7f7deb6980298493.png)
### 問い合わせに必要な内容
- サイトURL
- APIログ情報
- ご利用環境（OS,ブラウザ）
- 事象がいつから発生しているか

## 管理画面でエラーが発生した場合

### ログの確認方法
[オペレーション] → [ログ管理] → [[管理画面ログ](/ja/docs/management/admin-log-list/)] をご確認ください。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/efab1de1b76bb64e521baa61aa64e80a.png)
### 問い合わせに必要な内容
- サイトURL
- 管理画面ログ情報
- 事象の詳細
- ご利用環境（OS,ブラウザ）
- 事象がいつから発生しているか

## メール送信でエラーが発生した場合

### ログの確認方法
[オペレーション] → [ログ管理] → [[メールログ](/ja/docs/management/mail-log-list/)] をご確認ください。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/2494d0146210dc8e466235686b55857b.png)
### 問い合わせる前に確認すること
下記ドキュメントを確認ください。

- [メールが送信できない場合の確認方法を教えてください。](/ja/docs/faq/how-do-i-fix-email-delivery-failure/)

### 問い合わせに必要な内容
- サイトURL
- メールログ情報
- 送信元メールアドレス(From)
- 送信先メールアドレス（To）
- コンテンツのID
- 送信日時（配信の場合）
- 受信日時（フォームの場合）
- 事象の詳細
- ご利用環境（OS,ブラウザ）
- 事象がいつから発生しているか

## バッチ処理でエラーが発生した場合

### ログの確認方法
[オペレーション] → [ログ管理] → [[バッチログ](/ja/docs/management/batch-log-list/)] をご確認ください。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/84eef850f0ac5a563105ad26b29bd063.png)
### 問い合わせに必要な内容
- サイトURL
- バッチログ情報
- 事象の詳細
- ご利用環境（OS,ブラウザ）
- 事象がいつから発生しているか

## コンテンツの更新時に、GitHub Actionsが起動しないとき

### 問い合わせる前に確認すること

下記ドキュメントを確認してください。

- [KurocoFrontにファイルが反映されないのですが、何をチェックすればよいですか？](/ja/docs/faq/what-should-I-do-if-file-updates-are-not-reflected-in-kurocofront/)

また、[コンテンツの編集](/ja/docs/management/content-structure-topics/#コンテンツの編集)時に「Workflow」を「連携する」にして更新しているかご確認ください。

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/aae024d6dade474763c0a18d3df8fbab.png)

### 問い合わせに必要な内容
- サイトURL
- 事象の詳細
- ご利用環境（OS,ブラウザ）
- 事象がいつから発生しているか

## 関連ドキュメント
- [ログ管理](/ja/docs/management/log-management/)
- [APIログ](/ja/docs/management/api-log-list/)
- [HARファイルの作り方を教えてください](/ja/docs/faq/how-do-i-create-a-har-file/)
- [APIが動かないです。どうしたらよいですか？](/ja/docs/faq/what-should-i-do-if-the-api-is-not-working/)
- [メールが送信できない場合の確認方法を教えてください。](/ja/docs/faq/how-do-i-fix-email-delivery-failure/)
- [KurocoFrontにファイルが反映されないのですが、何をチェックすればよいですか？](/ja/docs/faq/what-should-I-do-if-file-updates-are-not-reflected-in-kurocofront/)


---

# APIのエラーメッセージ一覧はありますか？

> 元ページ: `faq/where-can-i-find-a-list-of-api-error-messages` ｜ 公式ページ: https://kuroco.app/ja/docs/faq/where-can-i-find-a-list-of-api-error-messages/
> 概要: 下記のリファレンスページに、APIリクエスト時に発生するエラーの一覧をまとめておりますのでご参照ください。

下記のリファレンスページに、APIリクエスト時に発生するエラーの一覧をまとめておりますのでご参照ください。  
- [APIエラーレスポンス](/ja/docs/reference/error/)

## 関連ドキュメント
- [APIエラーレスポンス](/ja/docs/reference/error/)
- [APIログ](/ja/docs/management/api-log-list/)
- [APIが動かないです。どうしたらよいですか？](/ja/docs/faq/what-should-i-do-if-the-api-is-not-working/)
- [エラー発生時の確認方法を教えてください](/ja/docs/faq/what-should-i-do-in-case-of-errors/)
