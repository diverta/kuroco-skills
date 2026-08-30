# フォーム・UIプラグイン

## 目次

- [fileupload](#fileupload) - File upload component supporti...
- [inquiry_input](#inquiry_input) - Replace placeholder comments i...
- [pager](#pager) - Generate pagination navigation...

---

## fileupload

File upload component supporting both S3 and local file uploads with preview and delete functionality.

### Parameters

|-----------|------|----------|---------|-------------|
| default | String | Optional | - | Default file URL/path for preview |

### Return Value

HTML containing file preview area, file upload input fields, delete checkbox with label, and JavaScript initialization in bodyend.

### Usage Example

```smarty
{* Basic file upload *}
{fileupload id=1 url="/direct/jcdata/file_upload/width=%26height=%26file_type=jpg,jpeg,png,gif" default=$formData.photo_url1 hidden_nm='photo_url1' file_type='jpg'}
{/fileupload}
{* S3 upload with custom script data *}
{fileupload id="ext_01" url=$s3_upload_url default=$formData.file_url hidden_nm='ext_col_01' file_type='pdf' max_file_size=50 script_data=$script_data}
{/fileupload}
```

### Notes

- Returns false if database connection is unavailable or system error
- JavaScript is appended to _bodyend_ template variable
- Delete checkbox name uses format del_file_{id} with hyphen replacement for ext_col patterns
- Supports UTF-8 extended characters in URLs

---

## inquiry_input

Replace placeholder comments in content with actual form values based on inquiry field configuration.

### Parameters

|-----------|------|----------|---------|-------------|
| default | String | Optional | '' | Default value when user hasn't submitted |

### Return Value

Content with placeholder comments replaced by actual values and form elements.

### Usage Example

```smarty
{inquiry_input item="email" inquiry_header=$inquiry_header formData=$formData current_mode="INPUT"}
  <input type="text" name="<!--q:name-->" value="<!--q:value-->" placeholder="<!--q:placeholder-->">
  <!--q:hidden-->
{/inquiry_input}
{* Multi-item field (e.g., name with first/last) *}
{inquiry_input item="name" inquiry_header=$inquiry_header formData=$formData}
  <input type="text" name="<!--q1:name-->" value="<!--q1:value-->">
  <input type="text" name="<!--q2:name-->" value="<!--q2:value-->">
{/inquiry_input}
```

### Notes

- Returns early if field is not enabled in user_profile (must be INQUIRY_PROFILE_ON or INQUIRY_PROFILE_REQUIRE)
- Returns early if selection field has no options configured
- Special handling for Facebook user info auto-fill (name, email)
- Supports USE_INQUIRY_EXT_JSONB mode for extended field storage
- Parameters can be inherited from parent inquiry_* blocks in the tag stack
- In CONFIRM mode, text inputs are replaced with their display value and hidden inputs are automatically generated

---

## pager

Generate pagination navigation links for list pages.

### Parameters

|-----------|------|----------|---------|-------------|

### Return Value

HTML string containing pagination navigation elements.

### Usage Example

```smarty
{pager info=$pageInfo}
{pager info=$pageInfo msg="No results found."}
{if $topics_list}
  {foreach $topics_list as $topic}
    <article>{$topic.subject}</article>
  {/foreach}
  {pager info=$pageInfo}
{/if}
```

### Notes

- Returns empty string if info is not provided or empty
- Returns msg content when totalCnt is 0
- Page links preserve existing URL parameters via param
- Translation keys used for link text (First, Previous, Next, Last)

