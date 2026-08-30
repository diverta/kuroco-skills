# Field Type Details and Examples

Per-type properties for every `ext_type`, the repeatable-group example, and complete `topics_group-create` payloads. The `ext_type` ↔ `type` table and the shared field properties live in `SKILL.md`.

> **Primary source**: `topics_group-describe` (optionally `{ "ext_type": N }`) returns the live per-type parameter list. This file is a snapshot reconciled against it on 2026-08-27; if anything here conflicts with `topics_group-describe`, **describe wins**.

## Table of Contents

- [Text (0)](#text-ext_type-0-type-text) · [Textarea (1)](#textarea-ext_type-1-type-textarea) · [WYSIWYG (6)](#wysiwyg-editor-ext_type-6-type-wysiwyg)
- [Select (2)](#select-box-ext_type-2-type-select) · [Checkbox (5)](#checkbox-ext_type-5-type-checkbox) · [Boolean (36)](#boolean-ext_type-36-type-bool)
- [Image (4)](#image-upload-ext_type-4-type-image) · [File (9)](#file-upload-ext_type-9-type-file) · [File Manager (30)](#file-manager-ext_type-30-type-filemanager)
- [Number (35)](#number-ext_type-35-type-number) · [Date (8)](#date-ext_type-8-type-date) · [Link (7)](#link-ext_type-7-type-link) · [Counter (34)](#counter-ext_type-34-type-counter)
- [Relation (20)](#relation-ext_type-20-type-relation) · [CSV Table (29)](#csv-table-ext_type-29-type-csvtable) · [CSV Table Checkbox (37)](#csv-table-checkbox-ext_type-37-type-csvtable_checkbox) · [Autocomplete (13)](#autocomplete-ext_type-13-type-textauto)
- [Location (11)](#location-ext_type-11-type-location) · [JSON (28)](#json-ext_type-28-type-json) · [Table (10)](#table-ext_type-10-type-table) · [HTML (21)](#html-ext_type-21-type-html) · [Block Editor (38)](#block-editor-ext_type-38-type-block_editor) · [API (32)](#api-integration-ext_type-32-type-api)
- [Reserved slug names](#reserved-slug-names)
- [Field Group Example](#field-group-example)
- [Practical Examples](#practical-examples)

## Field Type Details

### Text (ext_type: 0, type: "text")

Single-line text input field.

```json
{
  "ext_title": "Title",
  "ext_slug": "title",
  "ext_type": 0,
  "type": "text",
  "required": true,
  "searchable": true,
  "placeholder": "Enter text...",
  "default_value": "",
  "min_length": 0,
  "max_length": 255,
  "type_limitation": "email"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `placeholder` | string | Placeholder text |
| `default_value` | string | Default value |
| `min_length` | number | Minimum character count |
| `max_length` | number | Maximum character count |
| `type_limitation` | string | Input validation type: `"email"`, `"tel"`, `"zip"`, `"url"`, `"number"`, `"regex"` |
| `regex` | string | Regex pattern (when type_limitation is `"regex"`) |

### Textarea (ext_type: 1, type: "textarea")

Multi-line text input area.

```json
{
  "ext_title": "Description",
  "ext_slug": "description",
  "ext_type": 1,
  "type": "textarea",
  "placeholder": "Enter description...",
  "width": "100%",
  "height": "200px",
  "min_length": 0,
  "max_length": 10000
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `width` | string | Input width (e.g., `"100%"`, `"500px"`) |
| `height` | string | Input height (e.g., `"200px"`, `"10em"`) |
| `placeholder` | string | Placeholder text |
| `default_value` | string | Default value |
| `min_length` | number | Minimum character count |
| `max_length` | number | Maximum character count |

### WYSIWYG Editor (ext_type: 6, type: "wysiwyg")

Rich text editor.

```json
{
  "ext_title": "Article Body",
  "ext_slug": "body",
  "ext_type": 6,
  "type": "wysiwyg",
  "required": true,
  "searchable": true,
  "width": "100%",
  "height": "400px",
  "output_format": "html"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `width` / `height` | string | Editor size |
| `toolbar` | string | Use the reduced toolbar instead of the full one |
| `removePlugins` | string | Toolbar items to remove, comma-separated (e.g. `"bold,italic"`) |
| `allow_all_tags` | boolean | Store submitted HTML unfiltered instead of stripping disallowed tags |
| `use_markdown` | boolean | Enable Markdown input |
| `output_format` | string | `"html"` or `"markdown"` |
| `use_font_size_px` | boolean | Express font sizes in pixels |
| `use_magicline` | boolean | Insert a paragraph between block elements (magic line) |
| `largeColorPalette` / `customColors` | boolean / string | Extended palette; extra colors comma-separated |
| `custom_css` | string | CSS loaded into the editor so preview matches the site |
| `resource` | string | Resource path uploads from the editor are written to |
| `add_content_linked_folder` | boolean | Upload into a folder tied to the content record |
| `auto_use_iframely` | boolean | Turn pasted URLs into Iframely embeds |
| `auto_use_token` | boolean | Append an access token to links to restricted files |
| `placeholders` | string | Insertable placeholder definitions, as JSON |
| `wysiwyg_options` | string | Additional editor options, newline-separated `key::value` |
| `default_value` | string | Default HTML |

### Select Box (ext_type: 2, type: "select")

Single-choice field (dropdown or radio buttons). **`options` is required**.

```json
{
  "ext_title": "Category",
  "ext_slug": "category",
  "ext_type": 2,
  "type": "select",
  "required": true,
  "options": [
    { "key": "news", "val": "News", "default": true },
    { "key": "blog", "val": "Blog" },
    { "key": "event", "val": "Event" }
  ],
  "use_radio": false
}
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `options` | array | Yes | List of choices (minimum 1) |
| `options[].key` | string | Yes | Internal value of the option |
| `options[].val` | string | Yes | Display text of the option |
| `options[].default` | boolean | No | Whether this is the default selection |
| `use_radio` | boolean | No | Display as radio buttons instead of dropdown |
| `radio_separator` | string | No | Separator between radio buttons |

### Checkbox (ext_type: 5, type: "checkbox")

Multiple-choice checkbox field. **`options` is required**.

```json
{
  "ext_title": "Tags",
  "ext_slug": "topic_tags",
  "ext_type": 5,
  "type": "checkbox",
  "options": [
    { "key": "important", "val": "Important" },
    { "key": "featured", "val": "Featured", "default": true },
    { "key": "archived", "val": "Archived" }
  ],
  "use_multiselect": false
}
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `options` | array | Yes | List of choices (minimum 1) |
| `options[].key` | string | Yes | Internal value of the option |
| `options[].val` | string | Yes | Display text of the option |
| `options[].default` | boolean | No | Whether this is selected by default |
| `use_multiselect` | boolean | No | Use multi-select widget instead of checkboxes |
| `checkbox_separator` | string | No | Separator between checkboxes |

### Boolean (ext_type: 36, type: "bool")

True/false value rendered as radio buttons with customizable labels.

```json
{
  "ext_title": "Published",
  "ext_slug": "is_published",
  "ext_type": 36,
  "type": "bool",
  "default_value": "false",
  "true_label": "公開",
  "false_label": "非公開"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `default_value` | string | `"true"` or `"false"` |
| `true_label` / `false_label` | string | Labels for the two options (default: localized Yes / No) |

### Image Upload (ext_type: 4, type: "image")

```json
{
  "ext_title": "Main Image",
  "ext_slug": "main_image",
  "ext_type": 4,
  "type": "image",
  "required": true,
  "extensions": ["jpg", "jpeg", "png", "gif", "webp"],
  "file_size": "5"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `extensions` | string[] (or comma-separated string) | Allowed image extensions |
| `file_size` | string | Maximum upload size in MB (1 … site `MAX_FILE_SIZE`) |
| `ext_no_image_explain` | string | Hide the built-in caption input — send `"1"` (the admin UI stores `"1"`; omit the key to keep the caption). The image type already carries one caption per image — use it when one caption is enough, and a separate `text` field in a group only when the caption needs its own validation or slug |

### File Upload (ext_type: 9, type: "file")

File upload stored in Kuroco files.

```json
{
  "ext_title": "Attachment",
  "ext_slug": "attachment",
  "ext_type": 9,
  "type": "file",
  "file_type": ["pdf", "doc", "docx", "xlsx"],
  "file_size": "10"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `file_type` | string[] (or comma-separated string) | Allowed file extensions |
| `file_size` | string | Maximum upload size in MB (1 … site `MAX_FILE_SIZE`) |
| `ext_no_file_name` | string | Hide the display-name input |

### Number (ext_type: 35, type: "number")

```json
{
  "ext_title": "Price",
  "ext_slug": "price",
  "ext_type": 35,
  "type": "number",
  "required": true,
  "searchable": true,
  "min": 0,
  "max": 1000000,
  "number_type": "integer"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `min` / `max` | number | Accepted range |
| `number_type` | string | `"integer"` = whole numbers only; `""` = integers and decimals |
| `allow_exponential_notation` | boolean | Accept `1e5`-style input |

### Date (ext_type: 8, type: "date")

Date, or date and time, picker.

```json
{
  "ext_title": "Publish Date",
  "ext_slug": "publish_date",
  "ext_type": 8,
  "type": "date",
  "required": true,
  "add_time": "1",
  "placeholder": "YYYY-MM-DD"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `placeholder` | string | Placeholder text |
| `default_value` | string | Default value; relative `strtotime()` expressions are accepted |
| `add_time` | string | Include a time-of-day picker (`topics_group-describe` types it as string — send `"1"` and confirm by read-back) |
| `minute_interval` | string | Minute step of the time picker (1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30) |

### Link (ext_type: 7, type: "link")

URL input field.

```json
{
  "ext_title": "External Link",
  "ext_slug": "external_link",
  "ext_type": 7,
  "type": "link",
  "type_limitation": "url"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `type_limitation` | string | Validation type: `"url"` or `"regex"` |
| `regex` | string | Regex pattern (when type_limitation is `"regex"`) |

### Relation (ext_type: 20, type: "relation")

Reference to records of another module. **`module` is required**. The API returns id + label only by default — see Part 1 §3 in SKILL.md.

```json
{
  "ext_title": "Related Articles",
  "ext_slug": "related_articles",
  "ext_type": 20,
  "type": "relation",
  "module": "topics",
  "group_id": "1",
  "self_only": false
}
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `module` | string | Yes | `"topics"`, `"member"`, `"inquiry"` |
| `group_id` | string | No | Content definition ID(s) to pick from when `module=topics`; comma-separated for several |
| `contents_type` | string | No | Category ID(s) the candidates are limited to; comma-separated |
| `has_permissions` | boolean | No | Limit candidates to records the editor is allowed to see |
| `self_only` | boolean | No | Limit candidates to records the editor authored (picker scope — not the same as `my_topics_only_limit_groups`) |
| `secure_off` | boolean | No | Skip the viewing-limit check on the candidates |
| `order` | string | No | Sort order of the candidates |

### Location (ext_type: 11, type: "location")

Geographic coordinates picked on a map.

```json
{
  "ext_title": "Store Location",
  "ext_slug": "store_location",
  "ext_type": 11,
  "type": "location",
  "default_location": "{\"lat\": 35.6762, \"lng\": 139.6503, \"address\": \"Shibuya, Tokyo\"}"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `default_location` | string | Initial map position, **as a JSON string** (not an object) |

### JSON (ext_type: 28, type: "json")

Structured value entered as JSON. Use it to fold many non-searchable auxiliary settings into one field (Part 1 §2).

```json
{
  "ext_title": "Metadata",
  "ext_slug": "metadata",
  "ext_type": 28,
  "type": "json",
  "width": "100%",
  "height": "300px",
  "default_value": "{}"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `width` / `height` | string | Input size |
| `default_value` | string | Default JSON value |
| `schema` | string | JSON Schema the value is validated against |
| `build_ui_from_schema` | boolean | Generate the input form from `schema` instead of showing raw JSON |
| `dont_use_editor` | boolean | Plain textarea instead of the JSON editor |

### Table (ext_type: 10, type: "table")

Fixed-size grid of text cells.

```json
{
  "ext_title": "Specifications",
  "ext_slug": "specifications",
  "ext_type": 10,
  "type": "table",
  "rows": 5,
  "cols": 3,
  "cells": ["{\"0-0\": \"Property\", \"0-1\": \"Value\", \"0-2LOCK\": \"Notes\"}"]
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `rows` / `cols` | number | Grid size |
| `cells` | string[] | Per-cell settings as JSON. Keys are `"row-col"`; append `LOCK` to a key to make that cell read-only |

### HTML (ext_type: 21, type: "html")

Raw HTML code input field.

```json
{
  "ext_title": "Custom HTML",
  "ext_slug": "custom_html",
  "ext_type": 21,
  "type": "html",
  "width": "100%",
  "height": "300px",
  "allow_all_tags": true
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `width` | string | Input width |
| `height` | string | Input height |
| `default_value` | string | Default HTML value |
| `allow_all_tags` | boolean | Allow all HTML tags |
| `dont_use_editor` | boolean | Use plain text editor |

### Counter (ext_type: 34, type: "counter")

Auto-increment counter. Used for sequential numbers (e.g., receipt numbers). Values are assigned automatically.

```json
{
  "ext_title": "Receipt Number",
  "ext_slug": "receipt_number",
  "ext_type": 34,
  "type": "counter",
  "searchable": true
}
```

Only common properties are available for this field type.

### Block Editor (ext_type: 38, type: "block_editor")

Block-based content editor. **Allowed only as the first field of a field group** — the group's remaining fields are the block definitions. Takes no per-type parameters.

```json
{
  "group_nm": "Page Blocks",
  "group_slug": "page_blocks",
  "group_repetitions": 20,
  "fields": [
    { "ext_title": "Page Content", "ext_slug": "page_content", "ext_type": 38, "type": "block_editor", "repetitions": 1 },
    { "ext_title": "Heading", "ext_slug": "block_heading", "ext_type": 0, "type": "text", "repetitions": 1 },
    { "ext_title": "Body", "ext_slug": "block_body", "ext_type": 6, "type": "wysiwyg", "repetitions": 1 },
    { "ext_title": "Image", "ext_slug": "block_image", "ext_type": 4, "type": "image", "repetitions": 1 }
  ]
}
```

### Autocomplete (ext_type: 13, type: "textauto")

Text field with autocomplete functionality.

```json
{
  "ext_title": "Author Name",
  "ext_slug": "author_name",
  "ext_type": 13,
  "type": "textauto",
  "topics_group_id": "1",
  "field": "ext_col_01"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `topics_group_id` | string | Source TopicsGroup ID for suggestions |
| `field` | string | Field name to display as suggestions |
| `placeholder` | string | Placeholder text |
| `default_value` | string | Default value |

### File Manager (ext_type: 30, type: "filemanager")

File picked through the file manager.

```json
{
  "ext_title": "File Manager",
  "ext_slug": "file_manager",
  "ext_type": 30,
  "type": "filemanager",
  "resource": "/files/user/docs/"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `resource` | string | Resource path the file manager opens at |

> `s3file` (27), `vimeo` (31) and `gcsfile` (33) are **not listed by `topics_group-describe`**, so creating them through `topics_group-create` is unverified. If a design needs them, create the field in the admin UI or test on the live site first.

### CSV Table (ext_type: 29, type: "csvtable")

Single choice taken from a CSV table (master data — Part 1 §3). **`csv_master_id` is required.** Get the ID from `csvtable-list`, or create the table first with `csvtable-create` (read its `inputSchema` via `tools/list` for the payload shape; the columns you define decide `key` / `value` below).

```json
{
  "ext_title": "Master Data Selection",
  "ext_slug": "prefecture",
  "ext_type": 29,
  "type": "csvtable",
  "csv_master_id": "1",
  "key": "0",
  "value": "1"
}
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `csv_master_id` | string | Yes | CSV table the choices come from |
| `key` | string | No | **0-based** column index holding the stored value (default `"0"`; the header row is excluded). For cascading choices send a JSON array `"[parent_idx, idx]"` together with `parent_ext_id` |
| `value` | string | No | **0-based** column index holding the displayed label (default `"1"`). Read the table's columns with `csvtable-get` to pick the indexes |
| `default` | string | No | Default value |
| `parent_ext_id` | string | No | `ext_index` of another CSV table field this one is narrowed by (cascading choices) |

### CSV Table Checkbox (ext_type: 37, type: "csvtable_checkbox")

Multiple choice taken from a CSV table. Same parameters as `csvtable` plus:

```json
{
  "ext_title": "Master Data Multi-Select",
  "ext_slug": "prefectures",
  "ext_type": 37,
  "type": "csvtable_checkbox",
  "csv_master_id": "1",
  "key": "0",
  "value": "1",
  "use_multiselect": true
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `use_multiselect` | boolean | Multi-select widget instead of checkboxes |
| `checkbox_separator` | string | Markup placed between checkboxes |

### API Integration (ext_type: 32, type: "api")

Value chosen from an external API through a picker popup.

```json
{
  "ext_title": "External Data",
  "ext_slug": "external_product",
  "ext_type": 32,
  "type": "api",
  "popup_title": "Select a Product",
  "api_settings": "[{\"title\": \"Product Search\", \"url\": \"https://api.example.com/products?q={query}\", \"path_to_list\": \"results\", \"display_format\": \"{name} - {price}\", \"saved_format\": \"{id}\"}]"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `api_settings` | string | API definitions **as a JSON string**. The inner keys shown above (`title` / `url` / `path_to_list` / `display_format` / `saved_format`) come from the admin UI and are not enumerated by `topics_group-describe` — confirm by read-back |
| `popup_title` | string | Title of the picker popup |
| `restore_api_url` | string | API URL called to restore the stored value for display |
| `on_select_hook` / `on_save_hook` | string | JavaScript hook names run on select / on save |
| `use_smarty` | boolean | Evaluate the configured URLs as Smarty at runtime (e.g. `{$smarty.const.ROOT_URL}`) |

## Reserved slug names

`ext_slug` and `group_slug` accept `[a-zA-Z0-9_-]*` **except** the names below (taken from the `pattern` of the `topics_group-create` / `-update` schema on 2026-08-27; the live schema wins if it differs). Anything not listed — `title`, `description`, `price`, `body`, `category`, `image` … — is allowed.

Patterns: `ext_<n>`, `ext_col_<n>`, `contents_type_<n>`, `tmpfile_ext_<n>` / `del_file_ext_<n>` (and `_ext_col_<n>` variants), `category_parent_id_<n>`, `contents_type_ext_col_<n>`, `contents_type_nm_<n>`, `contents_type_parent_nm_<n>`, `contents_type_slug_<n>`, `contents_type_<n>_ext_col_<n>`, `favorite<n>_cnt`, `last_favorite<n>_ymdhi`, `my_favorite<n>_flg`.

Literal names: `admin_name`, `ai_postprocess_state`, `batch_ext_data`, `col_sort`, `contents`, `contents_type`, `contents_type_expand`, `dflg`, `ext`, `ext_group_sort`, `inst_ymdhi`, `member_id`, `ogp_data`, `open_flg`, `order_no`, `pdf_title1`, `pdf_title2`, `pdf_title3`, `post_time`, `pre_embedding_text`, `regular_flg`, `season`, `secure_level`, `secure_level_jsonb`, `slug`, `subject`, `topics_flg`, `topics_group_id`, `topics_id`, `update_ymdhi`, `vector768`, `vector1536`, `ymd`, `MODE`, `_doc_lang`, `_doc_waiting`, `approvalflow_id`, `compare_by_columns`, `data_waiting_id`, `ext_group`, `keyword`, `lang`, `lightweight_mode`, `lang_open_type`, `lang_open_type_org`, `open_end_date`, `open_end_time`, `open_end_ymdhi`, `open_sta_date`, `open_sta_time`, `open_sta_ymdhi`, `open_type`, `open_type_org`, `own_member_id`, `preview_token`, `reject_to`, `require_columns`, `search_keyword`, `tag_id`, `tag_ids`, `tag_relation`, `unuse_columns`, `update_comment`, `upsert_by_columns`, `use_columns`, `validate_only`, `category_parent_id`, `close_date`, `comment_cnt`, `contents_type_cnt`, `contents_type_list`, `contents_type_nm`, `contents_type_parent_nm`, `contents_type_slug`, `date_comment_cnt`, `favorite_cnt`, `group_description`, `group_nm`, `last_favorite_ymdhi`, `member_info`, `my_favorite_flg`, `open_date`, `product_ids`, `tags`, `vector_distance`

## Field Group Example

Fields inside a group must have `repetitions: 1`; `group_repetitions` sets how many times the whole group can repeat (ceiling: `whoami` → `site.limits.topics_ext_group_loop`).

```json
{
  "group_nm": "Product Variations",
  "group_slug": "product_variation",
  "group_repetitions": 10,
  "fields": [
    {
      "ext_title": "Color",
      "ext_slug": "color",
      "ext_type": 0,
      "type": "text",
      "repetitions": 1,
      "required": true
    },
    {
      "ext_title": "Size",
      "ext_slug": "size",
      "ext_type": 2,
      "type": "select",
      "repetitions": 1,
      "options": [
        { "key": "S", "val": "S" },
        { "key": "M", "val": "M" },
        { "key": "L", "val": "L" }
      ]
    },
    {
      "ext_title": "Price",
      "ext_slug": "price",
      "ext_type": 35,
      "type": "number",
      "repetitions": 1,
      "min": 0
    },
    {
      "ext_title": "Image",
      "ext_slug": "image",
      "ext_type": 4,
      "type": "image",
      "repetitions": 1,
      "extensions": ["jpg", "png", "webp"]
    }
  ]
}
```

## Practical Examples

> **Reminder**: These examples set only `name` / `description` / `fields`, so they inherit the recommended `content_input_type: 2` — the body is an explicit field, as in Example 1's `Article Body`. Add the access-rule parameters from [Content Definition Parameters](../SKILL.md#content-definition-parameters) whenever the request implies restricted visibility.

### Example 1: News Articles

> `Category` below is a fixed exclusive `select`. When editors should manage the choices themselves, model it as a category (`contents_type`, created with `topics_category-*`) instead — see Part 1 §4 in SKILL.md.

```json
{
  "name": "News Articles",
  "description": "Content structure for a news website",
  "fields": [
    {
      "ext_title": "Subtitle",
      "ext_slug": "subtitle",
      "ext_type": 0,
      "type": "text",
      "searchable": true,
      "max_length": 200
    },
    {
      "ext_title": "Category",
      "ext_slug": "category",
      "ext_type": 2,
      "type": "select",
      "required": true,
      "options": [
        { "key": "politics", "val": "Politics" },
        { "key": "economy", "val": "Economy" },
        { "key": "sports", "val": "Sports" },
        { "key": "entertainment", "val": "Entertainment" }
      ]
    },
    {
      "ext_title": "Main Image",
      "ext_slug": "main_image",
      "ext_type": 4,
      "type": "image",
      "required": true,
      "extensions": ["jpg", "jpeg", "png", "webp"],
      "file_size": "5"
    },
    {
      "ext_title": "Article Body",
      "ext_slug": "body",
      "ext_type": 6,
      "type": "wysiwyg",
      "required": true,
      "height": "500px"
    },
    {
      "ext_title": "Related Articles",
      "ext_slug": "related_articles",
      "ext_type": 20,
      "type": "relation",
      "module": "topics"
    }
  ]
}
```

### Example 2: Product Catalog

```json
{
  "name": "Products",
  "description": "Product catalog for an e-commerce site",
  "fields": [
    {
      "ext_title": "Product Code",
      "ext_slug": "product_code",
      "ext_type": 0,
      "type": "text",
      "required": true,
      "searchable": true,
      "max_length": 50
    },
    {
      "ext_title": "Price",
      "ext_slug": "price",
      "ext_type": 35,
      "type": "number",
      "required": true,
      "min": 0,
      "number_type": "integer"
    },
    {
      "ext_title": "Product Description",
      "ext_slug": "product_description",
      "ext_type": 6,
      "type": "wysiwyg",
      "height": "300px"
    },
    {
      "ext_title": "In Stock",
      "ext_slug": "in_stock",
      "ext_type": 36,
      "type": "bool",
      "default_value": "true"
    },
    {
      "ext_title": "Tags",
      "ext_slug": "topic_tags",
      "ext_type": 5,
      "type": "checkbox",
      "options": [
        { "key": "new", "val": "New Arrival" },
        { "key": "sale", "val": "On Sale" },
        { "key": "recommended", "val": "Recommended" }
      ]
    },
    {
      "group_nm": "Product Images",
      "group_slug": "product_images",
      "group_repetitions": 5,
      "fields": [
        {
          "ext_title": "Image",
          "ext_slug": "image",
          "ext_type": 4,
          "type": "image",
          "repetitions": 1,
          "extensions": ["jpg", "png", "webp"]
        },
        {
          "ext_title": "Caption",
          "ext_slug": "caption",
          "ext_type": 0,
          "type": "text",
          "repetitions": 1
        }
      ]
    }
  ]
}
```

### Example 3: Event Management

```json
{
  "name": "Events",
  "description": "Event information management",
  "fields": [
    {
      "ext_title": "Start Date/Time",
      "ext_slug": "start_at",
      "ext_type": 8,
      "type": "date",
      "required": true,
      "add_time": "1"
    },
    {
      "ext_title": "End Date/Time",
      "ext_slug": "end_at",
      "ext_type": 8,
      "type": "date",
      "add_time": "1"
    },
    {
      "ext_title": "Venue Location",
      "ext_slug": "venue",
      "ext_type": 11,
      "type": "location",
      "default_location": "{\"lat\": 35.6762, \"lng\": 139.6503, \"address\": \"Tokyo\"}"
    },
    {
      "ext_title": "Capacity",
      "ext_slug": "capacity",
      "ext_type": 35,
      "type": "number",
      "min": 1,
      "number_type": "integer"
    },
    {
      "ext_title": "Registration Number",
      "ext_slug": "registration_no",
      "ext_type": 34,
      "type": "counter"
    },
    {
      "ext_title": "Details",
      "ext_slug": "details",
      "ext_type": 6,
      "type": "wysiwyg",
      "height": "400px"
    },
    {
      "ext_title": "Flyer",
      "ext_slug": "flyer",
      "ext_type": 9,
      "type": "file",
      "file_type": ["pdf"],
      "file_size": "10"
    }
  ]
}
```
