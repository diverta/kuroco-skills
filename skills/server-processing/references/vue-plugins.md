# Vue.js・テンプレート連携プラグイン

## 目次

- [rcms_vue_component](#rcms_vue_component) - Load and mount a Vue.js compon...
- [head_include](#head_include) - Queue a template file to be in...
- [include](#include) - テンプレートをインクルードします。
- [function](#function) - 静的コンテンツで定義されたSmarty関数を実行します。

---

## rcms_vue_component

Load and mount a Vue.js component within a Smarty template.

### Parameters

|-----------|------|----------|---------|-------------|
| var | String | Optional | - | Variable name to store the component ID |

### Return Value

HTML containing component mount point and JavaScript initialization code.

### Usage Example

```smarty
{rcms_vue_component config="rcms-mng" name="modules/topics/TopicsList"}
{rcms_vue_component config="rcms-mng" name="modules/topics/TopicsEdit" props_data=$props_data}
{rcms_vue_component name="page-one" url="/files/user/js/app" keys="page-one.*;common.*"}
```

### Notes

- Component ID auto-generated as rcms_vue_component_{random} if not specified
- Props are JSON-encoded and passed to the component
- Multiple components can be mounted on the same page

---

## head_include

Queue a template file to be included in the HTML head section.

### Parameters

|-----------|------|----------|---------|-------------|

### Return Value

Empty string. The file path is added to the _headinclude_ template variable array.

### Usage Example

```smarty
{if $show_calendar}
  {head_include file="common/calendar_scripts.html"}
{/if}
{head_include file="modules/topics/head_meta.html"}
```

### Notes

- Duplicate Prevention: Same file path will not be included twice
- Files are rendered in the order they were added
- Useful for component-based templates where head content varies by page

---

## include

テンプレートをインクルードします。

### Parameters

|-----------|------|----------|---------|-------------|
| (additional) | any | Optional | - | インクルードしたテンプレートに渡す変数 |

### Return Value

インクルードしたテンプレートの出力が挿入されます。

### Usage Example

```smarty
{include file="/templates/header.html"}
{include file="/templates/item.html" item=$data}
```

### Notes

- 別のテンプレートファイルをインクルードします
- 追加パラメータはインクルードしたテンプレート内で使用できます

---

## function

静的コンテンツで定義されたSmarty関数を実行します。

### Parameters

|-----------|------|----------|---------|-------------|
| (additional) | any | Optional | - | 関数に渡す追加パラメータ |

### Return Value

定義された関数の戻り値が出力されます。

### Usage Example

```smarty
{function name="myFunction" param1="value1"}
```

### Notes

- 静的コンテンツで事前に定義された関数を呼び出します
- 追加パラメータは関数内で使用できます

