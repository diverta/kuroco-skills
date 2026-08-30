# Kurocoドキュメント: 管理画面 / コンテンツ管理

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- コンテンツ定義の拡張機能（`content-structure-extensions`）
- コンテンツ（`content-structure-topics`）
- コンテンツカテゴリ（`content-structure-topics-category`）
- コンテンツカテゴリアップロード（`content-structure-topics-category-upload`）
- コンテンツアップロード/ダウンロード（`content-structure-topics-csv`）
- コンテンツ定義（`content-structure-topics-group`）
- マスタ（`master`）
- タグ（`tag`）
- タグカテゴリ（`tag-category`）
- タグ一覧（`tag-list`）
- タグアップロード（`tag-upload`）


---

# コンテンツ定義の拡張機能

> 元ページ: `management/content-structure-extensions` ｜ 公式ページ: https://kuroco.app/ja/docs/management/content-structure-extensions/

コンテンツ定義編集画面の左サイドメニューに「拡張機能」として表示される追加機能の設定項目です。

## 確認方法

左メニューの **[コンテンツ定義]** → 設定したいコンテンツ定義のタイトルをクリック → 左サブメニューの **拡張機能** をクリックします。

:::info
拡張機能タブの表示は、[コンテンツ定義編集の全般](/ja/docs/management/content-structure-topics-group/#全般)にある「データ種別」の選択によって制御されます。選択した種別に対応するタブのみ表示されます。
:::

## AI自動処理

コンテンツが保存されたタイミングでAIを自動で動かす設定ができます。

このタブには目的の異なる2つの機能があります。

| 機能 | 目的 |
| :--- | :--- |
| **AI自動後処理** | コンテンツ保存後にAIがフィールドを自動加工・生成します |
| **AIバリデーション** | コンテンツ保存時にAIが内容の妥当性をチェックします |

### AI自動後処理

プロンプトで指定した処理を、コンテンツが保存された**後**にAIが自動で実行する機能です。

**[有効にする]** トグルをONにすると、変換ルールの設定欄が表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/674ac4e925682fe0b971fef07e221817.png)

#### 変換ルール

**[+ ルールを追加]** をクリックして複数のルールを登録できます。

##### プロンプト（必須）

AIへの指示を自由に入力します。あるフィールドの内容を読んで別のフィールドに書き込む処理を自然言語で指示できます。

**例:**
- 「`body` フィールドの本文を200字以内に要約して `bodySummary` フィールドに書いてください」
- 「`body` フィールドの内容からカテゴリを "技術" / "営業" / "総務" の中から1つ選んで `category` フィールドに書いてください」

##### 実行タイミング

| 選択肢 | 説明 |
| :--- | :--- |
| 新規作成時のみ | コンテンツを新しく作成したときだけ実行します |
| 新規作成・更新時 | どちらでも実行します |
| 更新時のみ | コンテンツを更新したときだけ実行します |

##### 作成ステータス

処理を実行する対象コンテンツの公開状態を指定します（例：「公開」のみ対象にするなど）。

##### オプション設定

| 項目 | 説明 |
| :--- | :--- |
| **入力フィールド** | AIに渡すフィールドを選択します |
| **出力フィールド** | AIの処理結果を書き込むフィールドを選択します |
| **モデルを使用 / AIエージェントを使用** | 処理をLLMに直接任せるか、AIエージェントに任せるかを選択します |
| **モデル** | 使用するAIモデルを指定します |

### AIバリデーション

プロンプトで指定した判定基準にもとづいてAIが内容をチェックする機能です。問題があると判定された場合、その理由がエラーメッセージとして表示されます。

:::info
AIバリデーションは、通常のバリデーション（必須チェックなど）が事前に実行された後、最後に実行されます。事前のバリデーションでエラーがある場合、AIバリデーションは実行されません。
:::

**[有効にする]** トグルをONにすると、バリデーションルールの設定欄が表示されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/48bcfcbc62dbff45fe72cfeea5b5b4e5.png)

#### バリデーションルール

**[+ ルールを追加]** をクリックして複数のルールを登録できます。

##### プロンプト（必須）

AIに渡す判定基準を入力します。問題があると判定された場合、この内容がエラーメッセージとして表示されます。

**例:**
- 「不適切な表現や攻撃的な言葉が含まれていないか確認してください」
- 「顧客名・期日・担当者の3つが記載されているか確認してください」

##### 実行タイミング

バリデーションを実行するタイミングを選択します。

| 選択肢 | 説明 |
| :--- | :--- |
| 追加時のみ | 新規コンテンツのみ実行します |
| 追加・更新時 | どちらでも実行します |
| 更新時のみ | コンテンツを更新したときだけ実行します |

##### 入力フィールド

チェック対象のフィールドを選択します。空のままにすると、利用可能なすべてのフィールド（タイトル・本文、およびコンテンツ定義に設定された拡張項目すべて）が送信されます。特定のフィールドを選択すると、AIが参照する範囲を絞り込めます。

##### モデル

使用するAIモデルを指定します。**自動（Auto）** を選ぶとシステム既定のモデルが使用されます。

#### AIバリデーションの動作仕様

- **各ルールは独立して評価されます。** チェーンや途中終了（ショートサーキット）はなく、却下したすべてのルールがそれぞれエラーを返すため、編集者は1回の保存操作ですべての却下理由を確認できます。
- **バリデーションは最後に実行されます。** AI以外のすべてのバリデーションを通過した場合にのみ呼び出されるため、すでに不正と判明している登録内容に対してトークンを消費しません。
- **フェイルクローズ。** AIリクエスト自体が失敗（通信エラーや解析エラー）した場合は、未検証の内容をそのまま通すのではなく、汎用的なバリデーションエラーで保存をブロックします。
- **却下理由は編集中の言語で返されます。** 編集者が作業している言語で説明が表示されます。
- 承認も含め、各判定はアプリケーションログに記録されるため、管理者は登録内容が承認・却下された理由を後から確認できます。

## メール受信

受信メールと送信メールに関する設定です。「メール受信を有効にする」をオンにすると、メールの送受信に必要な拡張項目（送信元・宛先・本文など）がコンテンツ定義に自動的に追加されます。

:::info
メール受信タブは、[コンテンツ定義編集の全般](/ja/docs/management/content-structure-topics-group/#全般)の「データ種別」で「メール」を選択すると表示されます。
:::

<a><img src="https://t.gyazo.com/teams/diverta/2b5aa78591773dbbbf7fe8dc0126f761.png" style={{ width: 600, maxHeight: 'none' }} /></a>
<a><img src="https://t.gyazo.com/teams/diverta/b6af7846de7af6ce0363bc5e0c6961a7.png" style={{ width: 600, maxHeight: 'none' }} /></a>

### 受信メール

| 項目 | 説明 |
| :--- | :--- |
|メール受信を有効にする|有効にすると、設定した受信アドレスへのメールを受信し、コンテンツとして自動登録します。|
|メール受付メールを返信する|有効にすると、受信したメールへの返信機能が有効になります。|
|メールアドレスの種別|受信メールの処理タイプを選択します。<ul><li>受信専用メール：@recv.kuroco.email のサフィックスが付与されます。</li><li>送受信メール：@agent.kuroco.email のサフィックスが付与されます。</li></ul>|
|受信メールアドレス|メールを受け付けるアドレスのローカル部分（@より前の部分）を入力します。半角英数字とハイフン (-) のみ使用できます。|
|SPF 失敗時に拒否|有効にすると、SPF認証に失敗した受信メールを拒否します。|
|DKIM 失敗時に拒否|有効にすると、DKIM認証に失敗した受信メールを拒否します。|
|送信許可ドメイン・メールアドレス|受信を許可するメールアドレスまたはドメインを改行区切りで入力します。|
|メンバー連携グループ|受信メールから関連メンバーを参照する際に絞り込むグループを選択します。「なし」を選択した場合はすべてのメンバーが対象になります。|

## クローリング

「Webページを有効にする」をオンにすると、クロール取得したWebページのデータを格納するための拡張項目（URL・コンテンツ・言語など）がコンテンツ定義に自動的に追加されます。

:::info
クローリングタブは、[コンテンツ定義編集の全般](/ja/docs/management/content-structure-topics-group/#全般)の「データ種別」で「クローリング」を選択すると表示されます。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e4bd5047e44f42b37925c67bab947737.png)

| 項目 | 説明 |
| :--- | :--- |
|連携クローラー設定|クロール元URLや設定を選択します。クローラー設定の詳細は[クローラー設定一覧](/ja/docs/management/spider-list/)を参照してください。|

## Slack

Slackの受信webhookイベントと送信APIメッセージを1メッセージ1レコードで保存する設定です。

:::info
Slackタブは、[コンテンツ定義編集の全般](/ja/docs/management/content-structure-topics-group/#全般)の「データ種別」で「Slack」を選択すると表示されます。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e5028e226c9451101a8cbff888247e96.png)

| 項目 | 説明 |
| :--- | :--- |
|保存するイベント種別|保存対象にするSlackイベント種別を選択します。<ul><li>両方（message / app_mention）：message と app_mention の両方が保存されます（デフォルト）。</li><li>message のみ</li><li>app_mention のみ</li></ul>|
|受付自動返信|有効にすると、@mention 付きの受信メッセージ保存後に、受付メッセージを自動送信します。|
|返信メッセージ|チャネルに送る受付メッセージです。受付自動返信が有効な場合は必須です。|
|Slackチャネル|受信したSlackメッセージを保存するチャネルID（例：C0123456ABC）を指定します。サイト内で同じチャネルIDを複数のコンテンツ定義に設定することはできません。空のままにすると、どのコンテンツ定義にも該当しないチャネルのメッセージを受け取るデフォルトとして扱われます（サイト内で1つのコンテンツ定義のみ設定可能）。|

## LINE

LINE Messaging APIから受信したWebhookイベントを1メッセージ1レコードで保存する設定です。

:::info
LINEタブは、[コンテンツ定義編集の全般](/ja/docs/management/content-structure-topics-group/#全般)の「データ種別」で「LINE」を選択すると表示されます。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/67b276119fd7e6368e59466400ada308.png)

| 項目 | 説明 |
| :--- | :--- |
|受付自動返信|有効にすると、受信メッセージ保存後に受付メッセージを自動送信します。|
|返信メッセージ|チャネルに送る受付メッセージです。受付自動返信が有効な場合は必須です。|

## Microsoft Teams

Microsoft Teams Bot Frameworkから受信したmessage activityを1メッセージ1レコードで保存する設定です。

:::info
Microsoft Teamsタブは、[コンテンツ定義編集の全般](/ja/docs/management/content-structure-topics-group/#全般)の「データ種別」で「Microsoft Teams」を選択すると表示されます。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5eb9ecf4bacccf9d0d7de13920736428.png)

| 項目 | 説明 |
| :--- | :--- |
|受付自動返信|有効にすると、受信メッセージ保存後に受付メッセージを自動送信します。|
|返信メッセージ|チャネルに送る受付メッセージです。受付自動返信が有効な場合は必須です。|
|Teams conversation ID|特定のTeams会話だけをこのコンテンツ定義に保存する場合にconversation.idを入力します。空欄の場合は未指定会話の保存先になります。|

## 関連ドキュメント

- [コンテンツ定義](/ja/docs/management/content-structure-topics-group/)
- [クローラー設定一覧](/ja/docs/management/spider-list/)
- [Kurocoで利用可能な定数一覧](/ja/docs/reference/constant-variables/)


---

# コンテンツ

> 元ページ: `management/content-structure-topics` ｜ 公式ページ: https://kuroco.app/ja/docs/management/content-structure-topics/

コンテンツでは、作成したコンテンツの一覧の確認・追加・更新ができます。

## コンテンツ一覧
### 確認方法
[コンテンツ定義]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6d477495dee779847cbef94b8f191b26.png)

コンテンツ定義ページから確認をしたいコンテンツ定義の[一覧]をクリックします。   
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4a93fba15b29aab7a803aa0ecb3209e5.png)

### 詳細検索
[詳細検索]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/7ac8b61bf2bc063c206ad820c0d80d20.png)

絞り込み条件を作成できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b2f51ab170bc00381d9e97ff5b5e7995.png)

### 表示項目設定
コンテンツ一覧右上の歯車マークをクリックすると、表示項目設定が表示されます。  
コンテンツ一覧に表示する項目を設定できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/11aa07a2d8b12b6979bbae1590ad5a49.png)

|項目   |説明  |
| :--- | :--- |
|表示項目|ドラッグ&ドロップで表示項目の位置を変更できます。|
|選択|一覧に表示するリストから選択し追加できます。|
|キャンセル|設定変更をキャンセルされます。|
|適用する|設定変更を適用します。|

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/7b7fe6681bb8979d10c86e073ccb8434.png)

|項目   |説明  |
| :--- | :--- |
|公開|コンテンツの公開状態を確認できます。<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/f6ba28f304045d08a896b276917750d1.jpg)：公開<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/fdf3714bf49ef20ec1f90b6c9e957697.png)：アクセス制限有り<br/>![Image from Gyazo](https://t.gyazo.com/teams/diverta/ded341265dda92d33617efd4d4857cb2.png)：非公開|
|日付|コンテンツに設定した日付が表示されます。|
|タイトル|コンテンツのタイトルが表示されます。|
|更新日時|コンテンツを最後に更新した日時が表示されます。|

### 一括処理ボタン
![Image from Gyazo](https://t.gyazo.com/teams/diverta/58ad409f70ab2f43c514260aeca630a9.png)

一覧の左端のチェックボックスにチェックを入れて、下記いずれかをクリックすると、選択したコンテンツに対して一括で処理を行います。

また、承認ワークフローを選択すると状態の更新を一括で申請します。

|項目   |説明  |
| :--- | :--- |
|公開にする|コンテンツを公開にします。|
|非公開にする|コンテンツを非公開にします。|
|削除する|コンテンツを削除します。|

### 更新履歴の確認
コンテンツ一覧画面右上の「その他」をクリックし、[更新履歴]をクリックすると、各コンテンツの編集履歴が一覧で確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/21497edcbc1262569380cd1c3ed3892e.png)

#### コンテンツ更新履歴
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2b80d350e3ef441565cab2bf2073d169.png)

|項目 |説明 |
| :--- | :--- |
|更新日時|コンテンツが更新された日時を表示します。|
|更新者|コンテンツを更新したメンバー名を表示します。|
|タイトル|コンテンツのタイトルを表示します。|
|モジュール|モジュール種類を表示します。|
|言語|言語を表示します。|
|アクション|実行した処理の種類を表示します。<br/>アクションは以下の6種類です。<br/><ul><li>新規追加</li><li>更新</li><li>削除</li><li>申請</li><li>承認</li><li>承認差し戻し</li></ul>|

## コンテンツの編集
### 編集方法
[コンテンツ]より、該当のコンテンツ定義名をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/71324e8a98849045114f1954f87d56f8.png)
コンテンツ一覧ページから編集をしたいコンテンツの[タイトル]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0a78372c7deb7a93e32a5228c771ef93.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4402626ccb36ed642fb3a87f4f8d1149.png)

|項目   |説明  |
| :--- | :--- |
|Slug|コンテンツのSlugを設定します。<br/>項目名の（ID：）にはコンテンツ新規作成時に自動採番されたコンテンツIDが表示されます。<br/><br/>Slugに使用できる文字列は以下のとおりです。<br/><ul><li>半角英数字</li><li>ハイフン（-）</li><li>アンダースコア（_）</li></ul>また、以下の制限があります。<br/><ul><li>数字のみの Slug は使用できません</li><li>コンテンツ定義をまたいで、サイト全体で重複はできません</li></ul>|
|日付|コンテンツの日付を設定します。|
|タイトル|コンテンツのタイトルを入力します。|

:::tip
その他、コンテンツ定義編集で設定した拡張項目の内容が表示されます。  
:::

:::tip
APIの新規作成権限がある場合、追加で設定した拡張項目の横にフィールド名(デフォルトのext_x、もしくはSlugを設定している場合はその値)が表示されます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/480b55f6950d3544e57d0d8fa18c9812.png)
:::

### コンテンツのコピー
コンテンツ編集画面右上の[コピー]をクリックすると、コンテンツをコピーして新しいコンテンツを作成できます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/cf5bda7760fe053cba9564d0347aa1c1.png)

表示されたメッセージの[OK]ボタンをクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c5414f98b0cf714037524519ffda1e18.png)

コピーされた新しいコンテンツの編集画面が開きます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/16fd1660b698b8abf642aa3dac46b778.png)

コピー内容を確認し、必要に応じて編集後に[追加する]をクリックしてコンテンツを保存します。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/41cb36e92033faa558b241d567c5b80a.png)

### 詳細設定
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4d3d4269bed4c7e7ba04370200720054.png)

|項目   |説明  |
| :--- | :--- |
|一覧に表示する|コンテンツ一覧のページに表示するか設定します。|
|上位表示する|コンテンツ一覧のページで上位に表示するか設定します。|
|APIリクエスト制限|APIリクエストを許可する範囲を選択します。複数選択可能です。この範囲は、カスタムメンバーフィルターで追加・編集できます。|

### 関連するタグ
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d44cec72533b7fe63007d14644465270.png)

コンテンツに設定するタグを設定します。
[タグを追加する]をクリックすると新規のタグを追加登録できます。

### 公開時連携の設定
![Image from Gyazo](https://t.gyazo.com/teams/diverta/78b82aa5c934fbc7aaa521fb83550ee8.png)

|項目   |説明  |
| :--- | :--- |
|連携配信|コンテンツと連動する配信を設定します。<br/>設定するとコンテンツの追加/更新時に配信機能の編集画面に遷移します。|

### 公開設定
![Image from Gyazo](https://t.gyazo.com/teams/diverta/e3482dd962676ed8baae30c537e1bf57.png)

|項目   |説明  |
| :--- | :--- |
|公開にする|コンテンツを公開します。|
|非公開にする|コンテンツを非公開にします。|
|公開日指定|開始日付、終了日付を任意に指定してコンテンツを公開します。|

### GitHub
![Image from Gyazo](https://t.gyazo.com/teams/diverta/319f32ddee44bc1ce26a6a1b02a88a15.png)

|項目   |説明  |
| :--- | :--- |
|ワークフロー|連携したGitHubの動作を選択します。<br/>無効：連携したGitHubでの動作はありません。<br/>有効：連携したGitHubでGitHub actionsが実行されます。|

### 承認ワークフロー設定
承認ワークフローの承認対象コンテンツに指定すると表示されます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/003eee0377ee727098984172bbd89012.jpg)

|項目   |説明  |
| :--- | :--- |
|ワークフロー|承認ワークフローを選択します。|
|承認の反映日時|承認が反映される日時を設定します。|
|タグ|関連する承認ワークフローのタグを選択します。<br/>承認ワークフローのタグは「タグを追加する」ボタンで追加、または承認ワークフロータグ一覧画面で追加や削除ができます。|

### 各ボタン/更新コメント
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ed6ff0e374b004cdc272e030c7065495.png)

|項目   |説明  |
| :--- | :--- |
|更新する|コンテンツの変更内容を反映します。|
|途中保存する|コンテンツの変更内容を保存します。|
|プレビューを確認する|コンテンツのプレビューを確認します。<br/>参考) [KurocoとNuxt.jsで、プレビュー画面を構築する](/ja/docs/tutorials/integrate-preview-page/)|
|削除する|表示しているコンテンツを削除します。|
|更新コメント|コンテンツを更新する際にコメントを残すことができます。|

### 更新履歴の確認
コンテンツ編集画面右上の「その他」をクリックし、[更新履歴]をクリックすると、各コンテンツの編集履歴が一覧で確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/91f9cec89fd948a98516637bb29a2ec8.png)

#### コンテンツ更新履歴
更新履歴の一覧が表示されます。  
また、異なる2つの履歴を選択して[比較する]をクリックすると差分の比較ができます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a9b17bb95b308c2aecc36c679167ac81.png)

|項目 |説明 |
| :--- | :--- |
|版|版を表示します。<br/>クリックすると対象の版の状態を確認できます。|
|更新日時|コンテンツが更新された日時を表示します。|
|更新者|コンテンツを更新したメンバー名を表示します。|
|アクション|実行した処理の種類を表示します。<br/>アクションは以下の6種類です。<br/><ul><li>新規追加</li><li>更新</li><li>削除</li><li>申請</li><li>承認</li><li>承認差し戻し</li></ul>|
|コメント|更新時に残したコメントを表示します。|
|内容|更新した内容を表示します。|

## 関連ドキュメント
- [コンテンツ編集画面の表示を変更する](/ja/docs/tutorials/change-the-display-of-the-content-editing-page/)
- [コンテンツを公開したまま、指定の日時に更新する](/ja/docs/tutorials/scheduling-updates-for-published-contents/)
- [コンテンツの更新時にGitHub Actionsを自動実行する](/ja/docs/tutorials/auto-run-github-with-contents-update/)
- [WYSIWYGエディターのプレースホルダー機能を実装する](/ja/docs/tutorials/how-to-use-ckeditor-placeholder-feature/)
- [カスタム処理を利用して、コンテンツに独自のバリデーションを実装する](/ja/docs/tutorials/how-to-implement-original-validation-in-contents-edit-by-using-function/)
- [カスタム処理を利用して、コンテンツ追加時にメールを送信する](/ja/docs/tutorials/how-to-implement-original-function-into-the-middle-of-processing-by-using-function/)
- [キーワード検索用文字列を用意する](/ja/docs/tutorials/how-to-implement-cutom-body-search/)
- [WYSIWYGエディタの使用方法](/ja/docs/reference/wysiwyg/)
- [Kuroco管理画面の検索機能について](/ja/docs/reference/search-function-on-kuroco-admin-panel/)
- [KurocoとNuxt.jsで、コンテンツ一覧ページを作成する](/ja/docs/tutorials/integrate-kuroco-with-nuxt/)
- [KurocoとNuxt.jsで、コンテンツ一覧ページにページネーションを実装する](/ja/docs/tutorials/splitting-the-contents-list-into-multiple-pages/)
- [KurocoとNuxt.jsで、プレビュー画面を構築する](/ja/docs/tutorials/integrate-preview-page/)
- [関連情報選択で選択したコンテンツの全情報をレスポンスに追加するにはどうしたら良いですか？](/ja/docs/faq/add-all-information-on-the-content-selected-in-the-relational-data-selection-to-the-response/)
- [コンテンツ公開日時の設定で、時間の選択間隔を変更できますか？](/ja/docs/faq/can-i-change-the-time-selection-interval-for-the-publication-settings/)
- [カスタムテンプレートの使い方を教えてください。](/ja/docs/faq/can-i-customize-the-display-of-tables-on-the-conten-editing-screen/)
- [コンテンツ編集画面の表示を変更できますか？](/ja/docs/faq/can-i-modify-the-display-of-the-content-editor-screen/)
- [「公開設定」の選択肢をデフォルトで「非公開」にできますか？](/ja/docs/faq/can-i-set-the-public-settings-option-to-private-by-default/)


---

# コンテンツカテゴリ

> 元ページ: `management/content-structure-topics-category` ｜ 公式ページ: https://kuroco.app/ja/docs/management/content-structure-topics-category/

コンテンツカテゴリ一覧ではコンテンツ定義で作成したカテゴリを一覧で確認できます。

## コンテンツカテゴリ一覧
### 確認方法
[コンテンツ定義]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6d477495dee779847cbef94b8f191b26.png)

カテゴリを確認したいコンテンツ定義の［カテゴリ設定］をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3a81b97d776c2046834a2ce63b723fa3.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0a21ecd5d207fa48c097c532cee99d46.png)

|項目   |説明  |
| :--- | :--- |
|ダウンロードする|登録されているコンテンツカテゴリ情報をダウンロードします。|
|公開|公開状態を確認できます。<br/>![fetched from Gyazo](https://t.gyazo.com/teams/diverta/04844a6327ba668f74880a0f10682489.png)：公開<br/>![fetched from Gyazo](https://t.gyazo.com/teams/diverta/f5923e63675ff30a82d61133019736d2.png)：APIリクエスト制限有り<br/>![fetched from Gyazo](https://t.gyazo.com/teams/diverta/b483e6f928fc3319266dad8bc633f086.png)：非公開|
|ID|カテゴリ毎に固有のIDを表示します。|
|カテゴリ名|カテゴリ名を表示します。クリックするとカテゴリ編集画面へ遷移します。|
|メモ|カテゴリ編集画面で入力したメモが表示されます。|
|並び順|並び順は数字の大きい順に並びます。カテゴリの並び順を入力後［並び順を更新する］をクリックすると、一括で変更することができます。|

### 一括処理ボタン
![Image from Gyazo](https://t.gyazo.com/teams/diverta/646ae41345447547991f40eafabd30a0.png)

一覧の左端のチェックボックスにチェックを入れて、下記いずれかをクリックすると、選択したカテゴリに対して一括で処理を行います。

|項目   |説明  |
| :--- | :--- |
|公開にする|カテゴリを公開にします。|
|非公開にする|カテゴリを非公開にします。|
|削除する|カテゴリを削除します。|
|並び順を更新する|並び順フィールドに記載された順に並び順を変更します。数字のみ利用可能で、数が大きい方が上位表示されます。|

### ダウンロード
ダウンロードするボタンを押すとダウンロード設定モーダルが開きます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b44b0132bab37060858ebe69e21b6c32.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/449c1740663be67e52e85e6f434780a0.png)

| 項目 | 説明 |
| :--- | :--- |
| 生成されるCSVの行数 |ダウンロードされるデータの件数が表示されます。|
| 文字コード | ダウンロードする文字コードを指定します。 |
| キャンセル | モーダルを閉じます。 |
| CSVをダウンロードする | 設定した内容でダウンロードします。 |

### 更新履歴の確認
コンテンツカテゴリ一覧画面右上の「その他」をクリックし、[更新履歴]をクリックすると、各コンテンツカテゴリの編集履歴が一覧で確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/71e02db18d7b95c2081052e86bc754fb.png)

#### コンテンツ更新履歴

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fcb58739de06665c4c920472782e0744.png)

|項目 |説明 |
| :--- | :--- |
|更新日時|コンテンツカテゴリが更新された日時を表示します。|
|更新者|コンテンツカテゴリを更新したメンバー名を表示します。|
|タイトル|コンテンツカテゴリのタイトルを表示します。|
|モジュール|モジュール種類を表示します。|
|言語|言語を表示します。|
|アクション|実行した処理の種類を表示します。<br/>アクションは以下の3種類です。<br/><ul><li>新規追加</li><li>更新</li><li>削除</li></ul>|

## カテゴリ編集
### 確認方法
[コンテンツ定義]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6d477495dee779847cbef94b8f191b26.png)

コンテンツの［カテゴリ設定］をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3a81b97d776c2046834a2ce63b723fa3.png)

編集したいカテゴリの[カテゴリ名]をクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/abb019dfb91ed0fa3bcebe1f3de1234b.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c21c5adb4a0f2a35401f6eb4050d63c0.jpg)

|項目   |説明  |
| :--- | :--- |
|カテゴリ名|カテゴリ名です。クリックするとカテゴリの編集画面が表示されます。|
|Slug|コンテンツカテゴリのSlugを入力します。|
|親カテゴリ|親カテゴリを選択できます。|
|並び順|数字の大きい順に並びます。|
|拡張項目 01〜拡張項目 05|カテゴリの補足説明を入力します。|
|APIリクエスト制限|APIリクエスト制限がかかっているカテゴリが1つでもコンテンツに設定されている場合、対象のグループに属するメンバーだけがそのコンテンツをからのレスポンスを得られるようになります。|
|編集制限|カテゴリの編集制限を指定します。選択されたグループのメンバーのみ編集可能になります。|
|メモ|用途などを記入しておくと便利です。登録した内容は管理画面のカテゴリ一覧にも表示されます。|

### 公開設定
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a904f58e602063d85b5cfbb1f178f35a.png)

|項目   |説明  |
| :--- | :--- |
|ダウンロードする|登録されているコンテンツカテゴリ情報をダウンロードします。|
|公開にする|カテゴリを公開します。|
|非公開にする|カテゴリを非公開にします。|
|公開日指定|開始日付、終了日付を任意に指定してカテゴリを公開します。|

### 各ボタン/更新コメント
![Image from Gyazo](https://t.gyazo.com/teams/diverta/15fe167da764062967b2100623d5c372.png)

|項目   |説明  |
| :--- | :--- |
|更新する|カテゴリを更新します。|
|途中保存する|カテゴリを一時保存します。|
|削除する|表示しているカテゴリを削除します。|
|更新コメント|カテゴリを更新する際にコメントを残すことができます。|

### 更新履歴の確認
コンテンツカテゴリ編集画面右上の「その他」をクリックし、[更新履歴]をクリックすると、各コンテンツの編集履歴が一覧で確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/45c3a624fa3f79eec525169a8dade751.png)

#### コンテンツカテゴリ更新履歴
更新履歴の一覧が表示されます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a6aa3c087068d7f8e0971fdbe8abc5bd.png)

|項目 |説明 |
| :--- | :--- |
|版|版を表示します。<br/>クリックすると対象の版の状態を確認できます。|
|更新日時|コンテンツカテゴリが更新された日時を表示します。|
|更新者|コンテンツカテゴリを更新したメンバー名を表示します。|
|アクション|実行した処理の種類を表示します。<br/>アクションは以下の3種類です。<br/><ul><li>新規追加</li><li>更新</li><li>削除</li></ul>|
|コメント|更新時に残したコメントを表示します。|
|内容|更新した内容を表示します。|

## 関連ドキュメント
- [カテゴリ拡張設定を利用する](/ja/docs/tutorials/using-category-ext-configuration/)


---

# コンテンツカテゴリアップロード

> 元ページ: `management/content-structure-topics-category-upload` ｜ 公式ページ: https://kuroco.app/ja/docs/management/content-structure-topics-category-upload/

コンテンツカテゴリアップロードではCSVをアップロードしてカテゴリを一括で更新できます。

## コンテンツカテゴリアップロードの確認方法
［コンテンツ定義］をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6d477495dee779847cbef94b8f191b26.png)

カテゴリを確認したいコンテンツ定義の［カテゴリ設定］をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3a81b97d776c2046834a2ce63b723fa3.png)

コンテンツカテゴリ一覧の画面から右上の[その他]をクリックし、[アップロード]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b920b5dd92770f321052b229669faf64.png)

## コンテンツカテゴリアップロードの項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/766fb20992554b609b80414fc3298b7e.png)

|項目   |説明  |
| :--- | :--- |
|CSVファイル|[ファイルを選択]をクリックしてアップロードするCSVファイルを選択します。<br/>CSVファイルのサンプルは右上の三点リーダをクリックし、[ダウンロード]から取得できます。|
|文字コード|文字コードを選択します。|
|アップロードする|アップロードしたCSVファイルの内容を反映します。|

## コンテンツカテゴリアップロード時の挙動
- 新規追加：カテゴリIDが空の場合は、新規追加になります。
- 更新：カテゴリIDが存在している場合は、更新になります。
- 削除：カテゴリIDを指定して、削除フラグに1を入れると、削除になります。

## 関連ドキュメント
- [コンテンツカテゴリ](/ja/docs/management/content-structure-topics-category/)
- [コンテンツアップロード/ダウンロード](/ja/docs/management/content-structure-topics-csv/)
- [コンテンツ定義](/ja/docs/management/content-structure-topics-group/)
- [CSVでコンテンツを一括更新する](/ja/docs/tutorials/bulk-upload-in-csv/)
- [CSVによるコンテンツのアップロードはできますか？](/ja/docs/faq/can-i-upload-topics-using-csv-files/)


---

# コンテンツアップロード/ダウンロード

> 元ページ: `management/content-structure-topics-csv` ｜ 公式ページ: https://kuroco.app/ja/docs/management/content-structure-topics-csv/

## コンテンツアップロード
### 確認方法
［コンテンツ定義］をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6d477495dee779847cbef94b8f191b26.png)

コンテンツをアップロードしたいコンテンツ定義の［アップロード］をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a325cd1abb71531b9b65ab09e3ae5f20.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/337903f8cdd6516b06f74465905b4c8e.jpg)

|項目   |説明  |
| :--- | :--- |
|CSVファイル|アップロードするCSVファイルを登録します。CSVファイルの雛形はコンテンツダウンロードからダウンロードできます。|
|ファイル・メディアファイル（ZIP）|画像をはじめ、使用するファイルをZIPファイルにまとめて一括アップロードします。ファイル名は、CSVファイルに記載しておく必要があります。|
|クラウドソースフォルダ|クラウドストレージ（S3/GCS）が有効な場合に表示されます。CSVで参照するファイルの取得元となるクラウドストレージ上のフォルダパスを指定します。ZIPファイルのアップロードの代わりに、クラウドストレージ上の既存ファイルを利用する場合に使用します。<br/>入力欄の先頭には `files/a/private/`（S3の場合）または `files/g/private/`（GCSの場合）が自動的に付与されます。|
|文字コード|文字コードを選択します。|
|値がない場合の動作|値がないときの動作を選択します。|
|ファイル・メディアファイル名の入力チェック|ファイル・メディアファイル名の入力チェック方法を選択します。|
|コンテンツIDがない場合にSlugから設定する|有効にすると、CSVのコンテンツID列が空の場合に、Slug列の値を使って既存コンテンツを検索します。同一コンテンツ定義内に一致するSlugのコンテンツが見つかった場合、そのコンテンツIDを自動的に設定して更新処理を行います。<br/>新規コンテンツをSlugで管理し、CSVで一括更新したい場合に便利です。|
|ワークフロー|連携したGitHubの動作を選択します。<br/>無効：連携したGitHubでの動作はありません。<br/>有効：連携したGitHubでGitHub actionsが実行されます。|
|アップロードする|CSVをアップロードします。|
|バッチ処理でアップロードする|CSVアップロードをバッチ処理で実行します。件数が多い場合にはこちらをご利用ください。|
|入力チェックする|アップロード前に、エラーの有無を事前に確認できます。|

### 画像容量について
CSVアップロード時に添付できる画像容量は、S3はAmazon Web Services(以下AWS)の、Google Cloud Storage(以下GCS)はGCSの仕様に準じます。それぞれの仕様は下記リンクをご参照ください。

- S3の仕様について[Amazon Simple Storage Service (S3)](https://docs.aws.amazon.com/ja_jp/AmazonS3/latest/dev/UploadingObjects.html)
- GCSの仕様について[割り当てと上限](https://cloud.google.com/storage/quotas)

## コンテンツダウンロード
コンテンツに登録されている情報を、一括でダウンロードできます。データはCSV形式です。

### 確認方法
［コンテンツ定義］をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6d477495dee779847cbef94b8f191b26.png)

コンテンツをダウンロードしたいコンテンツ定義の［ダウンロード］をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b352b635f3b33c5f364fe779d7c2057c.png)

### 項目説明

![Image from Gyazo](https://t.gyazo.com/teams/diverta/18c04be9ce399c9e917649de63f88a63.png)

|項目   |説明  |
| :--- | :--- |
|適用中のフィルター|詳細検索で絞り込み条件を作成している場合に、その内容が表示されます。|
|生成されるCSVの行数|ダウンロードされるデータの件数が表示されます。|
|文字コード|ダウンロードする文字コードを指定します。|
|繰り返し表示方法|繰り返し表示方法を選択します。<ul><li>繰り返す拡張項目を合わせて表示：拡張項目が繰り返しの場合、1つのセルに表示します。</li><li>繰り返す拡張項目を別々に表示：拡張項目が繰り返しの場合、繰り返しの項目ごとにセルを分けて表示します。</li><li>親子項目をグループ化して表示：拡張項目が親子項目になっている場合、グループ化して表示します。</li></ul>|
|言語選択|出力する言語を選択します。|
|出力する列を選択する。|クリックすると、列名一覧が表示されます。出力したい列を選択します。|
| キャンセル| モーダルを閉じます。|
|CSVをダウンロードする|画像以外のデータをCSV形式でダウンロードします。|
|ファイルダウンロードする|画像をZIP形式でダウンロードします。|
|CSVのダウンロードリンクを生成する|バッチ処理でコンテンツダウンロードを実行します。件数が多い場合にはこちらをご利用ください。<br/>バッチ処理が完了するとダウンロードリンクから画像以外のデータをダウンロードできます。|
|ファイルのダウンロードリンクを生成する|バッチ処理でファイルダウンロードを実行します。<br/>バッチ処理が完了するとダウンロードリンクから画像をZIP形式でダウンロードできます。|

CSVに入力されるコンテンツカテゴリは通常カテゴリ名で表示されますが、以下の条件の場合はコンテンツIDの表示に変わります。  
- コンテンツカテゴリ名に重複がある場合  
- 数字のみのコンテンツカテゴリ名が存在する場合

## 関連ドキュメント
- [CSVでコンテンツを一括更新する](/ja/docs/tutorials/bulk-upload-in-csv/)


---

# コンテンツ定義

> 元ページ: `management/content-structure-topics-group` ｜ 公式ページ: https://kuroco.app/ja/docs/management/content-structure-topics-group/

コンテンツ定義では、コンテンツ定義の一覧が表示されます。
## コンテンツ定義
### 確認方法
[コンテンツ定義]をクリックします。   
![Image from Gyazo](https://t.gyazo.com/teams/diverta/045bbb8687db7c9d690bc6a3cf7c416f.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4ffec355697201fd01e7b7c30553147b.png)

|項目   |説明  |
| :--- | :--- |
|検索機能|コンテンツ定義の絞り込み検索を行えます。|
|表示項目設定ボタン（歯車アイコン）|デフォルトではコンテンツ定義一覧に表示されていない項目を追加することができます。|
|ID|コンテンツ定義ごとに固有のIDが表示されます。|
|公開|コンテンツ定義の公開状態を確認できます。<br/>![fetched from Gyazo](https://t.gyazo.com/teams/diverta/04844a6327ba668f74880a0f10682489.png)：公開<br/>![fetched from Gyazo](https://t.gyazo.com/teams/diverta/f5923e63675ff30a82d61133019736d2.png)：閲覧制限有り<br/>![fetched from Gyazo](https://t.gyazo.com/teams/diverta/b483e6f928fc3319266dad8bc633f086.png)：非公開|
|タイトル|コンテンツ定義の名前が表示されます。コンテンツ定義の名前をクリックすると編集画面へ移動し、コンテンツ定義の細かな設定を行えます。
|編集|各画面へ移動します。<ul><li>追加：コンテンツ作成画面へ遷移します。</li><li>一覧：コンテンツ定義内のコンテンツを一覧で表示します。</li><li>カテゴリ設定：コンテンツ定義に設定したカテゴリを一覧で表示します。</li><li>アップロード：CSVによる一括アップロードが出来ます。</li><li>ダウンロード：コンテンツ定義内のコンテンツをCSVで一括ダウンロード出来ます。</li></ul>|
|APIリクエスト制限|コンテンツ定義編集でグループを選択している場合は、グループ名が表示されます。|
|編集制限|コンテンツ定義編集でグループを選択している場合は、グループ名が表示されます。|
|所有コンテンツ限定で編集制限|コンテンツ定義編集でグループを選択している場合は、グループ名が表示されます。|
|件数|登録済みのコンテンツの件数が表示されます。|
|並び順|並び順を入力します。数値の大きい順に並びます。|
|更新日時|最後にコンテンツを更新した日時が表示されます。|

### 詳細検索
[詳細検索]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/be65ecf21f62d0f493c885a49c347ae9.png)

絞り込み条件を作成できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/428974017fa78f848685efa5446cf5c4.png)

### 表示項目設定
![Image from Gyazo](https://t.gyazo.com/teams/diverta/26c0c37900cb5a73f9eeba0bc3238922.png)

|項目   |説明  |
| :--- | :--- |
| 表示項目 |ドラッグ&ドロップで表示項目の位置を変更できます。 |
|選択|	一覧に表示するリストから選択し追加できます。|
|キャンセル|	設定変更をキャンセルされます。|
|適用する|	設定変更を適用します。|

### 一括処理
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d2f49f58716a12bf34b79f586460bdfc.png)

一覧の左端のチェックボックスにチェックを入れて、下記いずれかをクリックすると、選択したコンテンツ定義に対して一括で処理を行います。

|項目   |説明  |
| :--- | :--- |
|公開にする|コンテンツ定義を公開にします。|
|非公開にする|コンテンツ定義を非公開にします。|
|削除する|コンテンツ定義を削除します。コンテンツ定義に紐付くコンテンツは全て削除されます。|
|並び順を更新する|並び順フィールドに記載された順に並び順を変更します。数字のみ利用可能で、数が大きい方が上位表示されます。|

## コンテンツ定義編集
### 確認方法
[コンテンツ定義]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/045bbb8687db7c9d690bc6a3cf7c416f.png)

編集をしたいコンテンツ定義の[タイトル]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c48cd7e48025055dcf9748696054c0fa.png)

### 項目説明(基本)
#### 全般
##### 全般

<a><img src="https://t.gyazo.com/teams/diverta/b5f9dfed47f55f70563e361d2352c7b0.png" style={{ width: 600, maxHeight: 'none' }} /></a>
<a><img src="https://t.gyazo.com/teams/diverta/db22604368acb559585c43cd1d6a37fe.png" style={{ width: 600, maxHeight: 'none' }} /></a>

|項目   |説明  |
| :--- | :--- |
|ID|コンテンツ定義のグループIDを表示します。<br/>IDは自動で採番されます。|
|コンテンツ定義名|コンテンツ定義のグループ名を入力します。|
|API説明（OpenAPI / MCP連携用）|コンテンツ定義の説明を入力します。このコンテンツ定義のAPIスキーマ説明文として、OpenAPI仕様および admin_api / MCPツールに公開されます。|
|データ種別|データの取り込み元を選択します。選択した種別に対応する拡張機能タブがサイドメニューに表示され、その取り込みが有効になります。<br/>選択肢は以下のとおりです。<ul><li>**コンテンツ**: 取り込み元を使用しません（デフォルト）。</li><li>**メール**: メールの受信に必要な項目（差出人、宛先、本文、添付ファイルなど）が自動で追加されます。</li><li>**クローリング**: Webページ用の項目（URL、説明、画像、last-modifiedなど）と関連する初期設定が保存時に自動で適用されます。</li><li>**Slack**: Slackの受信webhookイベントと送信APIメッセージが1メッセージ1レコードで保存されます。</li><li>**LINE**: LINE Messaging APIから受信したWebhookイベントが1メッセージ1レコードで保存されます。</li><li>**Microsoft Teams**: Microsoft Teams Bot Frameworkから受信したmessage activityが1メッセージ1レコードで保存されます。</li></ul>|
|コンテンツ公開を前提にしない|有効にすると、コンテンツ編集画面の「公開／非公開」ラベルが「利用する／利用しない」に切り替わります。<br/>社内向けデータベースやナレッジ管理など、Kurocoを公開サイトのCMSとしてではなく認証必須の業務アプリの基盤として利用するユースケースに適しています。<br/>※ この設定を有効にする場合、閲覧制限（secure_level）の設定が必須になります。|

##### 公開設定
![Image from Gyazo](https://t.gyazo.com/teams/diverta/cf343ca7f3a326c38c0b876ca7f166ba.png)

|項目   |説明  |
| :--- | :--- |
|公開にする|コンテンツを公開します。|
|非公開にする|コンテンツを非公開にします。|
|公開日指定|開始日付、終了日付を任意に指定してコンテンツを公開します。|

#### 項目設定

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7554b183977d5a5ecab9e9d331cdd9c2.png)

|項目   |説明  |
| :--- | :--- |
|項目名|項目名が表示されます。|
|編集ボタン|クリックすると項目の設定が開きます。|
|項目設定|項目設定が表示されます。<br/>詳細は[コンテンツ定義で利用できる拡張項目一覧](/ja/docs/reference/list-of-extra-column-available-on-content/)をご確認ください。|
|Slug/ID|Slug/IDが表示されます。|
|入力制限|必須設定の有無が確認できます。|

#### 詳細設定

<a><img src="https://t.gyazo.com/teams/diverta/c0a10bc9b871e6ccc4d5f2a537c595dc.png" style={{ width: 600, maxHeight: 'none' }} /></a>

<a><img src="https://t.gyazo.com/teams/diverta/d8d6a2a92eed4c7e95172b8292696e10.png" style={{ width: 600, maxHeight: 'none' }} /></a>

<a><img src="https://t.gyazo.com/teams/diverta/c2a1f90281da134fb5f74a56c855425a.png" style={{ width: 600, maxHeight: 'none' }} /></a>

<a><img src="https://t.gyazo.com/teams/diverta/ef3797124b4fcd763907668841bf78b3.png" style={{ width: 600, maxHeight: 'none' }} /></a>

<a><img src="https://t.gyazo.com/teams/diverta/7a0bfb8738d239fdfb7d65028dd8e541.jpg" style={{ width: 600, maxHeight: 'none' }} /></a>

|項目   |説明  |
| :--- | :--- |
|並び順(大きい方が上)|コンテンツ定義グループ一覧での並び順を入力します。数字が大きい方が上に表示されます。|
|最大コンテンツ数|最大コンテンツ数を入力します。<br/>※ 無制限にしたい場合：0<br/>※ 一覧ページを作成しない場合：1|
|プレビューの対象とするページのURL|コンテンツ編集でプレビュー表示をした際に表示するページのURLを設定します。<br/>[参考) KurocoとNuxt.jsで、プレビュー画面を構築する](/ja/docs/tutorials/integrate-preview-page/)|
|更新履歴を残さない|チェックを入れると更新履歴を残らない代わりに、パフォーマンスが向上します。後から有効化した場合、既存の履歴データは消去されます。|
|コンテンツに設定できるカテゴリ数|コンテンツ編集画面で設定可能なカテゴリの数を指定します。|
|カテゴリツリー表示|コンテンツ編集ページでのカテゴリの表示方法を設定します。|
|カテゴリ拡張設定|サンプルを参考に記述すると、コンテンツカテゴリ編集の入力項目を修正することができます。|
|デフォルト表示フィールド|コンテンツ一覧に表示するデフォルト項目を設定します。<br/>ユーザーがコンテンツ一覧画面で表示項目を個別に設定している場合は、その内容が優先されます。|
|選択ボックスにタグを表示する|コンテンツ編集ページでのタグの表示方法を設定します。|
|非公開タグの設定を許可する|有効にするとコンテンツ編集画面で非公開のタグも設定できるようになります。|
|ドラッグ&ドロップで拡張項目の並び替えを有効にする|有効にすると繰り返しが設定された項目の並び順をドラッグ&ドロップで変更できるようになります。|
|カスタマイズCSS|CSSのURLをセットすると、指定したCSSをコンテンツ内の全てのエディタで読み込みます。|
|注意事項|注意事項を入力します。|
|CSS|コンテンツ編集画面のCSSを設定することができます。<br/>※Smartyが有効になっているので、`{ }`を使用する場合は、`{literal}` `{/literal}`で囲むように記述します。|
|JavaScript|コンテンツ編集画面のJSを設定することができます。|
{/*
|AI Post-Processing|コンテンツの追加・更新時にAIによる後処理（翻訳などの任意の処理）を自動で実行するかどうかを設定します。<br/>*この機能を利用するには、定数 `USE_AI_POSTPROCESS` を `1` に設定する必要があります。詳しくは[Kurocoで利用可能な定数一覧](/ja/docs/reference/constant-variables/)を参照してください。*|
*/}

#### 権限設定

![Image from Gyazo](https://t.gyazo.com/teams/diverta/40b346c281dd571ed9e68d0ec240e5e0.png)

|項目   |説明  |
| :--- | :--- |
|APIリクエスト制限|対象のグループに属するメンバーだけがコンテンツのレスポンスを得られるようになります。|
|編集制限|当該コンテンツ定義を編集できるグループを選択します。<br/>編集を「許可する」設定です。|
|所有コンテンツ限定で編集制限|自分が作成したコンテンツのみ編集できます。権限を与えたいグループを選択します。<br/>編集を「制限する」設定です。|
|要申請グループ|コンテンツ編集時、申請が必要になるグループを設定します。<br/>ただし、グループ権限設定の「管理者」にチェックがあると、申請不要になります。<br/>編集を「制限する」設定です。|
|申請権限での非公開・下書き保存許可|多言語設定をしているサイトにのみ表示されます。<br/>副言語のコンテンツを投稿するには、まず主言語のコンテンツを作成する必要がありますが、許可を出すことで、ワークフローの利用が必須のグループでも非公開であれば主言語のコンテンツを作成することができます。|

#### 一括設定

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c7f7aa83191e77d21187a7e40de23826.png)

|項目   |説明  |
| :--- | :--- |
|ファイル|JSONファイルを選択して更新すると、拡張項目を一括で設定できます。|
|JSON|現在の拡張項目の設定内容をJSON形式でダウンロードします。|

#### 検索設定

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0cd1201d40fe828910892c3fe3fb3a89.png)

|項目   |説明  |
| :--- | :--- |
|キーワード検索にテンプレートを利用する|チェックを入れるとfull_text_searchでこのテンプレートを検索できるようになり検索の柔軟性やパフォーマンスが向上します。|
|キーワードテンプレート|全文検索に用いる文字列を登録します。Smartyを使って必要なコンテンツの内容を出力してください。<br/>詳しい使い方は[キーワード検索用文字列を用意する](/ja/docs/tutorials/how-to-implement-cutom-body-search/)を参照してください。|
|ベクトルデータに変換する|チェックを入れるとAPIのchatの回答に利用されるコンテンツとして登録されたり、ベクトル検索に利用できるようになります。|
|AIによるベクトルデータの最適化|チェックを入れるとベクトルデータを作る際にAIによって最適化やデータの拡張を行います。|
|埋め込みモデル|埋め込みモデルを選択します。|
|キーワードテンプレート(AI/Vector)|OpenAIに参照させたいデータを空白区切りで登録します。Smartyを使って必要なコンテンツの内容を出力してください。改行は自動で空白に置換されます。|
|キーワードテンプレート(AI/Vector)向けのAI辞書|設定すると、キーワードテンプレートに対してAI辞書を適用します。|

### 項目説明(拡張機能)
コンテンツ定義編集画面の左サイドメニューに「拡張機能」として表示される追加機能の設定項目です。各項目の詳細は [コンテンツ定義の拡張機能](/ja/docs/management/content-structure-extensions/) を参照してください。

### 各ボタン/更新コメント
![Image from Gyazo](https://t.gyazo.com/teams/diverta/523118bc8f202bcc33d30a1538b1d599.png)

|項目   |説明  |
| :--- | :--- |
|更新する|コンテンツ定義の変更を反映します。|
|削除する|表示しているコンテンツ定義を削除します。|
|更新コメント|コンテンツ定義を更新する際にコメントを残すことができます。|

### 更新履歴の確認
コンテンツ定義編集画面右上の[その他]をクリックし、[更新履歴]をクリックすると、編集履歴が一覧で確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/28c5e943620b283165eec62c0476c35a.png)

#### コンテンツ定義更新履歴
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a76010a294109c313f680493ccfafdae.png)

|項目 |説明 |
| :--- | :--- |
|版|版を表示します。<br/>クリックすると対象の版の状態を確認できます。|
|更新日時|コンテンツが更新された日時を表示します。|
|更新者|コンテンツを更新したメンバー名を表示します。|
|アクション|実行した処理の種類を表示します。<br/>アクションは以下の6種類です。<br/><ul><li>新規追加</li><li>更新</li><li>削除</li><li>申請</li><li>承認</li><li>承認差し戻し</li></ul>|
|コメント|更新時に残したコメントを表示します。|
|内容|更新した内容を表示します。|

## 項目の並び替え・グループ化
追加項目はドラッグアンドドロップで並び替え及びグループ化が可能です。

**並び替え**
![Image from Gyazo](https://t.gyazo.com/teams/diverta/21e3f81afc610ce40c56c6f1749c072a.gif)

**グループ化**
![Image from Gyazo](https://t.gyazo.com/teams/diverta/9fe953e6f32f18b74f2df9a4c65dc590.gif)

## 関連ドキュメント
- [コンテンツ定義の拡張機能](/ja/docs/management/content-structure-extensions/)
- [コンテンツ定義を作成する](/ja/docs/tutorials/adding-a-topics/)
- [WYSIWYGエディターのプレースホルダー機能を実装する](/ja/docs/tutorials/how-to-use-ckeditor-placeholder-feature/)
- [カテゴリ拡張設定を利用する](/ja/docs/tutorials/using-category-ext-configuration/)
- [コンテンツ編集画面の表示を変更する](/ja/docs/tutorials/change-the-display-of-the-content-editing-page/)
- [コンテンツ定義で利用できる拡張項目一覧](/ja/docs/reference/list-of-extra-column-available-on-content/)
- [WYSIWYGエディタの使用方法](/ja/docs/reference/wysiwyg/)
- [WYSIWYG カスタムカラーの設定方法](/ja/docs/reference/wysiwyg-custom-color-settings/)
- [Firebaseと連携して、Storageにファイルを保存する](/ja/docs/tutorials/firebase/)
- [Amazon S3と連携して、Storageにファイルを保存する](/ja/docs/tutorials/amazon-s3/)
- [Vimeoと連携して動画をアップロードする](/ja/docs/tutorials/how-to-connect-to-vimeo/)
- [管理画面プラグインを利用して、Kuroco管理画面に任意のVueコンポーネントを適用する](/ja/docs/tutorials/apply-vue-to-a-kuroco-management-screen-with-the-plugin/)
- [キーワード検索用文字列を用意する](/ja/docs/tutorials/how-to-implement-cutom-body-search/)
- [画像(FileManagerにアップロード)を利用してアップロードしたファイルを他のコンテンツのファイル(ファイルマネージャーから)で使用できますか？](/ja/docs/faq/can-i-attach-files-from-other-content-structure-via-filemanager/)
- [カスタムテンプレートの使い方を教えてください。](/ja/docs/faq/can-i-customize-the-display-of-tables-on-the-conten-editing-screen/)
- [コンテンツ編集画面の表示を変更できますか？](/ja/docs/faq/can-i-modify-the-display-of-the-content-editor-screen/)


---

# マスタ

> 元ページ: `management/master` ｜ 公式ページ: https://kuroco.app/ja/docs/management/master/

マスタでは、作成したマスタの一覧の確認・追加・更新ができます。

## マスタ一覧
### 確認方法
[コンテンツ] -> [マスタ]をクリックします。   
![Image from Gyazo](https://t.gyazo.com/teams/diverta/8edefc6a674045fb0cb60020cd9ebd39.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/de17f8ae736a0d5270440bc09020f01a.png)

|項目   |説明  |
| :--- | :--- |
|ID|マスタのIDを表示します。IDは自動で採番されます。|
|タイトル|マスタのタイトルを表示します。|
|更新日時|マスタが最後に更新された日時を表示します。|
|並び順|数の大きな順に並びます。一覧画面で入力して、画面下の[並び順を更新する]をクリックすると、一覧画面上で並び順だけ変更することができます。|

### 一括処理ボタン
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d7c8d1d12712ca0309616bc2a1579a66.png)

一覧の左端のチェックボックスにチェックを入れて、下記いずれかをクリックすると、選択したマスタに対して一括で処理を行います。

|項目   |説明  |
| :--- | :--- |
|削除する|マスタを削除します。|
|並び順を更新する|並び順フィールドに記載された順に並び順を変更します。数字のみ利用可能で、数が大きい方が上位表示されます。|

## マスタの編集
### 編集方法
[コンテンツ] -> [マスタ]をクリックします。   
![Image from Gyazo](https://t.gyazo.com/teams/diverta/8edefc6a674045fb0cb60020cd9ebd39.png)

マスタ一覧ページから編集をしたいマスタの[タイトル]をクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1b02a06d2250608957daa2ea7251e2d9.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/05dd90bd26b98284b54757802fbb0e7f.jpg)

|項目   |説明  |
| :--- | :--- |
|タイトル|マスタのタイトルを入力します。|
|表組み(テーブル)|表の内容を入力します。|
|CSVで更新|CSVを選択して表の更新ができます。|
|メモ|マスタに関してメモを入力することができます。|
|編集権限|マスタの編集権限を設定します。|

### 承認ワークフロー設定
承認ワークフローの承認対象コンテンツにマスタを指定すると表示されます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3e455ba5b34c382211831be38213bb15.png)

|項目   |説明  |
| :--- | :--- |
|ワークフロー|承認ワークフローを選択します。|
|承認の反映日時|承認が反映される日時を設定します。|
|タグ|関連する承認ワークフローのタグを選択します。<br/>承認ワークフローのタグは「タグを追加する」ボタンで追加、または承認ワークフロータグ一覧画面で追加や削除ができます。|

### 各ボタン/更新コメント
![Image from Gyazo](https://t.gyazo.com/teams/diverta/94f7b6500ef1dff940acffc0ed998f48.png)

|項目   |説明  |
| :--- | :--- |
|更新コメント|更新時にコメントを残すことができます。|
|更新する|マスタの変更を反映します。|
|途中保存する|編集内容を途中保存します。|
|削除する|表示しているマスタを削除します。|

### 更新履歴の確認
マスタ編集画面右上の「その他」をクリックし、[更新履歴]をクリックすると、各コンテンツの編集履歴が一覧で確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4485c13eb91e4408630bfb77d68d96e3.png)

#### マスタ編集更新履歴
![Image from Gyazo](https://t.gyazo.com/teams/diverta/044e0c62b2e671e338975c34dab989a6.png)

|項目 |説明 |
| :--- | :--- |
|版|版を表示します。<br/>クリックすると対象の版の状態を確認できます。|
|更新日時|コンテンツが更新された日時を表示します。|
|更新者|コンテンツを更新したメンバー名を表示します。|
|アクション|実行した処理の種類を表示します。<br/>アクションは以下の6種類です。<br/><ul><li>新規追加</li><li>更新</li><li>削除</li><li>申請</li><li>承認</li><li>承認差し戻し</li></ul>|
|コメント|更新時に残したコメントを表示します。|
|内容|更新した内容を表示します。|

## 関連ドキュメント
- [コンテンツ定義](/ja/docs/management/content-structure-topics-group/)
- [承認ワークフロー](/ja/docs/management/workflow/)
- [マスタ形式を使って動的に変化する選択項目を設定する](/ja/docs/tutorials/setting-up-dynamic-options-using-master/)


---

# タグ

> 元ページ: `management/tag` ｜ 公式ページ: https://kuroco.app/ja/docs/management/tag/

タグでは、作成したタグの一覧の確認・追加・更新ができます。

## タグ一覧
### 確認方法
[コンテンツ] -> [タグ]をクリックします。   
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b6f66c1cc9d73f7ec8cb3b5ba8d3b94a.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d8fe05565a7f2bd9c76cb90fbf63223a.png)

|項目  |説明  |
| :--- | :--- |
|検索|登録済みのタグを検索できます。[詳細検索]をクリックすると、カテゴリ・公開状況・表示件数の選択欄が表示されます。条件を入力し、[検索する]をクリックすると、タグの絞り込みが可能です。|
|ダウンロードする|登録されているタグ情報をダウンロードします。|
|公開|公開、非公開のいずれかを表示します。<br/>![fetched from Gyazo](https://t.gyazo.com/teams/diverta/04844a6327ba668f74880a0f10682489.png)：公開<br/>![fetched from Gyazo](https://t.gyazo.com/teams/diverta/b483e6f928fc3319266dad8bc633f086.png)：非公開|
|ID|タグ作成時に自動で採番されます。|
|カテゴリ|編集画面で選択されたカテゴリを表示します。|
|タイトル|タグ名を表示します。|
|更新日時|最後に更新された日時を表示します。|
|関連する公開コンテンツ数|タグが紐付けられているコンテンツのうち、公開されているコンテンツの数を表示します。|
|関連する全コンテンツ数|タグが紐付けられているコンテンツの総数を表示します。|
|並び順|数の大きな順に並びます。一覧画面で入力して、画面下の[並び順を更新する]をクリックすると、一覧画面上で並び順だけ変更することができます。|

### 一括処理ボタン
![Image from Gyazo](https://t.gyazo.com/teams/diverta/588bc35ef45d430a48edbd5d5c005a78.jpg)

一覧の左端のチェックボックスにチェックを入れて、下記いずれかをクリックすると、選択したタグに対して一括で処理を行います。

|項目   |説明  |
| :--- | :--- |
|公開にする|タグを公開にします。|
|非公開にする|タグを非公開にします。|
|削除する|タグを削除します。|
|並び順を更新する|並び順フィールドに記載された順に並び順を変更します。数字のみ利用可能で、数が大きい方が上位表示されます。|。

### ダウンロード
ダウンロードするボタンを押すとダウンロード設定モーダルが開きます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ea160b09759686c317cff26f974154d9.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/36f881b2ad317696419e4bb2cb7151ee.png)

| 項目 | 説明 |
| :--- | :--- |
| 生成されるCSVの行数 |ダウンロードされるデータの件数が表示されます。|
| 文字コード | ダウンロードする文字コードを指定します。 |
| キャンセル | モーダルを閉じます。 |
| CSVをダウンロードする | 設定した内容でダウンロードします。 |

## タグの編集
### 編集方法
[コンテンツ] -> [タグ]をクリックします。   
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b6f66c1cc9d73f7ec8cb3b5ba8d3b94a.png)

タグ一覧ページから編集をしたいタグの[タイトル]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/dad0e3befb46d59d546a6379dbeaf51e.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5b109bcd5a9180e063d6521dbe180568.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bbb1e3d3311cf077f5bf3f92bea42b84.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/78493727155920ddb5349fe84ca0f407.png)

|項目  |説明  |
| :--- | :--- |
|タイトル|タグ名を入力します。|
|カテゴリ|タグのカテゴリを選択します。詳しくは後述の「タグカテゴリ」をご参照ください。|
|並び順|入力すると数の大きな順に並びます。|
|関連する公開コンテンツ数|タグが紐付けられているコンテンツのうち、公開されているコンテンツの数を表示します。|
|関連する全コンテンツ数|タグが紐付けられているコンテンツの総数を表示します。|
|項目１～１０|APIで取得できます。|

### 公開設定
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a904f58e602063d85b5cfbb1f178f35a.png)

|項目   |説明  |
| :--- | :--- |
|ダウンロードする|登録されているコンテンツカテゴリ情報をダウンロードします。|
|公開にする|カテゴリを公開します。|
|非公開にする|カテゴリを非公開にします。|
|公開日指定|開始日付、終了日付を任意に指定してカテゴリを公開します。|

### 承認ワークフロー設定
承認ワークフローの承認対象コンテンツにタグを指定すると表示されます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/d1d58f5a2b61a83bc7a24544950d538f.png)

|項目   |説明  |
| :--- | :--- |
|ワークフロー|承認ワークフローを選択します。|
|承認の反映日時|承認が反映される日時を設定します。|
|タグ|関連する承認ワークフローのタグを選択します。<br/>承認ワークフローのタグは「タグを追加する」ボタンで追加、または承認ワークフロータグ一覧画面で追加や削除ができます。|

### 各ボタン/更新コメント
![Image from Gyazo](https://t.gyazo.com/teams/diverta/418dd62976d9bc318dbb72877797bd0e.png)

|項目   |説明  |
| :--- | :--- |
|更新する|タグの変更を反映します。|
|途中保存する|編集中の内容を反映せずに途中保存します。|
|削除する|表示しているタグを削除します。|
|更新コメント|更新時にコメントを残すことができます。|

### 更新履歴の確認
タグ編集画面右上の[その他]をクリックし、[更新履歴]をクリックすると、編集履歴が一覧で確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c1c2ccbb7c869982586b63e5910b91c3.png)

#### タグ編集更新履歴
![Image from Gyazo](https://t.gyazo.com/teams/diverta/89febc0eedaeda3f31e2c295410c90ab.png)

|項目 |説明 |
| :--- | :--- |
|版|版を表示します。<br/>クリックすると対象の版の状態を確認できます。|
|更新日時|コンテンツが更新された日時を表示します。|
|更新者|コンテンツを更新したメンバー名を表示します。|
|アクション|実行した処理の種類を表示します。<br/>アクションは以下の6種類です。<br/><ul><li>新規追加</li><li>更新</li><li>削除</li><li>申請</li><li>承認</li><li>承認差し戻し</li></ul>|
|コメント|更新時に残したコメントを表示します。|
|内容|更新した内容を表示します。|

## 関連ドキュメント
- [タグカテゴリ](/ja/docs/management/tag-category/)
- [タグ一覧](/ja/docs/management/tag-list/)
- [タグアップロード](/ja/docs/management/tag-upload/)
- [承認ワークフロー](/ja/docs/management/workflow/)
- [タグ名にスペースを含めたい](/ja/docs/faq/can-i-use-spaces-in-tag-names/)
- [APIのレスポンスをタグカテゴリで絞り込みたい](/ja/docs/faq/filtering-api-responses-by-tag-category/)


---

# タグカテゴリ

> 元ページ: `management/tag-category` ｜ 公式ページ: https://kuroco.app/ja/docs/management/tag-category/

タグカテゴリは、作成したタグカテゴリの一覧の確認・追加・更新ができます。

## タグカテゴリ一覧
### 確認方法
[コンテンツ] -> [タグ]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b6f66c1cc9d73f7ec8cb3b5ba8d3b94a.png)

タイトル「タグ一覧」上のドロップダウンメニューから[カテゴリ設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1d2f4af5d3b6640f56633f5a357780d2.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/2f4babe9db5ecdeed0ed2e73c2e4b009.png)

|項目  |説明  |
| :--- | :--- |
|ダウンロードする|登録されているタグカテゴリ情報をダウンロードします。|
|ID|タグカテゴリの作成時に自動採番されます。|
|カテゴリ名|タグのカテゴリ名です。クリックするとカテゴリの編集画面に遷移します。|
|更新日時|最後に更新された日時を表示します。|
|並び順|数の大きな順に並びます。一覧画面で入力して、画面下の[並び順を更新する]をクリックすると、一覧画面上で並び順だけ変更することができます。|

### 一括処理ボタン
![Image from Gyazo](https://t.gyazo.com/teams/diverta/999b8dd3833bec63a6ed3511049bf8dd.jpg)

一覧の左端のチェックボックスにチェックを入れて、下記いずれかをクリックすると、選択したタグカテゴリに対して一括で処理を行います。

|項目   |説明  |
| :--- | :--- |
|削除する|タグカテゴリを削除します。|
|並び順を更新する|並び順フィールドに記載された順に並び順を変更します。数字のみ利用可能で、数が大きい方が上位表示されます。|。

### ダウンロード
ダウンロードするボタンを押すとダウンロード設定モーダルが開きます。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/37d95642596840b87b985156f10d2be3.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bef850bf050dd09a9ba1280b0f091c6b.png)

| 項目 | 説明 |
| :--- | :--- |
| 生成されるCSVの行数 |ダウンロードされるデータの件数が表示されます。|
| 文字コード | ダウンロードする文字コードを指定します。 |
| キャンセル | モーダルを閉じます。 |
| CSVをダウンロードする | 設定した内容でダウンロードします。 |

## タグカテゴリの編集
### 編集方法
[コンテンツ] -> [タグ]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b6f66c1cc9d73f7ec8cb3b5ba8d3b94a.png)

タイトル「タグ一覧」上のドロップダウンメニューから[カテゴリ設定]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/1d2f4af5d3b6640f56633f5a357780d2.png)

タグカテゴリ一覧ページから編集をしたいタグカテゴリの[カテゴリ名]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/3f13f8482f1cd08788e3669425a11527.png)

### 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a82375d374a7dca74cf384044bab8d44.png)

|項目  |説明  |
| :--- | :--- |
|カテゴリ名|タグのカテゴリを入力します。|
|親カテゴリ|親カテゴリを選択します。|
|対象|カテゴリが設定されたタグが表示される対象の機能を限定できます。<br/>コンテンツ定義IDを空にした場合は全てのコンテンツが対象になります。<br/>対象の設定は子カテゴリに引き継がれます。|
|並び順|数の大きな順に並べ替えできます。|
|編集制限|このカテゴリの編集を制限する・しないを選択します。デフォルトは「制限なし」にチェックがあります。<br/>「制限あり」にするときは、編集を許可するグループを選択してください。グループは複数選択できます。|
|更新する|タグカテゴリの変更内容を反映します。|
|削除する|表示しているタグカテゴリを削除します。|

## 関連ドキュメント
- [タグ](/ja/docs/management/tag/)
- [タグ一覧](/ja/docs/management/tag-list/)
- [タグアップロード](/ja/docs/management/tag-upload/)
- [APIのレスポンスをタグカテゴリで絞り込みたい](/ja/docs/faq/filtering-api-responses-by-tag-category/)


---

# タグ一覧

> 元ページ: `management/tag-list` ｜ 公式ページ: https://kuroco.app/ja/docs/management/tag-list/

ここではタグの一覧を確認できます。

## タグ一覧の確認方法
[コンテンツ] -> [タグ]をクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/3ea77ad6ce477ce27a9ac2fa4ce9034d.png)

## タグ一覧の項目説明
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/2f504f93eba92d86ee3e13c4f39ba417.png)
|項目  |説明  |
| :--- | :--- |
|検索|登録済みのタグを検索できます。カテゴリ等を選択して[検索]ボタンをクリックしてください。|
|公開|公開、非公開のいずれかを表示します。<br/>![fetched from Gyazo](https://t.gyazo.com/teams/diverta/04844a6327ba668f74880a0f10682489.png)：公開<br/>![fetched from Gyazo](https://t.gyazo.com/teams/diverta/b483e6f928fc3319266dad8bc633f086.png)：非公開|
|ID|タグ作成時に自動で採番されます。|
|カテゴリ|編集画面で選択されたカテゴリを表示します。|
|タイトル|タグ名を表示します。|
|関連する公開コンテンツ数|タグが紐付けられているコンテンツのうち、公開されているコンテンツの数を表示します。|
|関連する全コンテンツ数|タグが紐付けられているコンテンツの総数を表示します。|
|最終更新日時|最後に更新された日時を表示します。|
|並び順|数の大きな順に並びます。一覧画面で入力して、画面下の[並び順を更新する]をクリックすると、一覧画面上で並び順だけ変更することができます。|

## 一括処理
タグ一覧の左端のチェックボックスにチェックを入れて、[公開にする][非公開にする][削除する]のいずれかをクリックすると、選択したタグに対して一括で処理を行います。

## 関連ドキュメント
- [タグ](/ja/docs/management/tag/)
- [タグカテゴリ](/ja/docs/management/tag-category/)
- [タグアップロード](/ja/docs/management/tag-upload/)
- [タグ名にスペースを含めたい](/ja/docs/faq/can-i-use-spaces-in-tag-names/)


---

# タグアップロード

> 元ページ: `management/tag-upload` ｜ 公式ページ: https://kuroco.app/ja/docs/management/tag-upload/

ここではCSVファイルをアップして、タグを一括で更新・追加できます。

## タグアップロードの確認方法
[コンテンツ] -> [タグ]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b6f66c1cc9d73f7ec8cb3b5ba8d3b94a.png)

タイトル「タグ一覧」上のドロップダウンメニューから、[アップロード]をクリックします。
![Image from Gyazo](https://t.gyazo.com/teams/diverta/69bb5ac6835bd0648366ab7c6c2d6004.png)

## タグアップロード 項目説明
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b363480fe77f3907fb44d2ec907986cc.png)

|項目  |説明  |
| :--- | :--- |
|ファイル設定(タグ)|[ファイルを選択]をクリックしてアップロードするCSVファイルを選択します。<br/>[サンプルをダウンロード]をクリックするとアップロード形式を確認するためのサンプルファイルがダウンロードできます。|
|アップロードする|アップロードしたCSVファイルの内容を反映します。|

## タグアップロード更新時の挙動
- 新規追加：タグIDが空の場合は、新規追加になります。
- 更新：タグIDが存在している場合は、更新になります。
- 削除：タグIDを指定して、削除フラグに1を入れると、削除になります。

## 関連ドキュメント
- [タグ](/ja/docs/management/tag/)
- [タグカテゴリ](/ja/docs/management/tag-category/)
- [タグ一覧](/ja/docs/management/tag-list/)
