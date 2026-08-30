#!/usr/bin/env node
// 仕様書ディレクトリ (Markdown + Mermaid) を 1つのPDFに変換し、ソースごと zip にする。
//
// Usage:
//   node build-pdf.mjs <specDir> [-o <outDir>] [--html-only] [--no-zip] [--force]
//
// 依存: Node.js 18+ / Chrome か Chromium (PATH または CHROME_PATH) / zip コマンド
// レンダラー (markdown-it, mermaid) は CDN から読むためネットワーク接続が必要。
// Chrome が無い環境では --html-only で HTML 生成まで行い、手動で印刷する。

import { execFileSync, spawnSync } from 'node:child_process'
import { existsSync, mkdirSync, readdirSync, readFileSync, statSync, writeFileSync } from 'node:fs'
import os from 'node:os'
import path from 'node:path'
import process from 'node:process'

const out = (msg) => process.stdout.write(`${msg}\n`)
const err = (msg) => process.stderr.write(`${msg}\n`)
const fail = (msg) => {
  err(`error: ${msg}`)
  process.exit(1)
}

// ---------- 引数 ----------

function parseArgs(argv) {
  const flags = { outDir: 'dist', htmlOnly: false, noZip: false, force: false }
  const rest = []
  for (let i = 0; i < argv.length; i += 1) {
    const a = argv[i]
    if (a === '-o' || a === '--out') {
      i += 1
      if (!argv[i]) fail('-o requires a directory')
      flags.outDir = argv[i]
    } else if (a === '--html-only') flags.htmlOnly = true
    else if (a === '--no-zip') flags.noZip = true
    else if (a === '--force') flags.force = true
    else rest.push(a)
  }
  if (rest.length !== 1) fail('usage: node build-pdf.mjs <specDir> [-o <outDir>] [--html-only] [--no-zip] [--force]')
  return { ...flags, specDir: rest[0] }
}

// ---------- ファイル収集 (README.md の目次順) ----------

function walkMarkdown(dir, base = dir) {
  return readdirSync(dir, { withFileTypes: true })
    .sort((a, b) => a.name.localeCompare(b.name))
    .flatMap((e) => {
      const full = path.join(dir, e.name)
      if (e.isDirectory()) return walkMarkdown(full, base)
      if (e.isFile() && e.name.endsWith('.md')) return [path.relative(base, full).split(path.sep).join('/')]
      return []
    })
}

// README.md からリンクを再帰的に辿った到達順（読み順）で並べる。
// _index.md からリンクされる各定義ページが _index の直後に来る。
function linkedOrder(specDir) {
  const seen = new Set()
  const ordered = []
  const visit = (rel) => {
    if (seen.has(rel) || !existsSync(path.join(specDir, rel))) return
    seen.add(rel)
    ordered.push(rel)
    const text = readFileSync(path.join(specDir, rel), 'utf8')
    const dir = path.posix.dirname(rel)
    for (const m of text.matchAll(/\]\((?!https?:|#|mailto:)([^)#\s]+\.md)(?:#[^)]*)?\)/g)) {
      visit(path.posix.normalize(path.posix.join(dir, m[1])))
    }
  }
  visit('README.md')
  return ordered
}

function collectFiles(specDir) {
  const all = walkMarkdown(specDir)
  if (all.length === 0) fail(`no .md files under ${specDir}`)
  const ordered = linkedOrder(specDir).filter((rel) => all.includes(rel))
  const unlinked = all.filter((rel) => !ordered.includes(rel))
  if (unlinked.length > 0) err(`warn: not reachable from README.md links, appended last: ${unlinked.join(', ')}`)
  return [...ordered, ...unlinked]
}

// ---------- Markdown 前処理 (相対リンク → ページ内アンカー) ----------

const anchorId = (rel) => `p-${rel.replace(/[^a-zA-Z0-9]+/g, '-').replace(/^-|-$/g, '')}`

// HTMLコメント（kuroco-spec メタデータ等）は印刷物に出さない。
// markdown-it を html:false で使うためコメントも平文として描画されてしまうのを防ぐ。
const stripHtmlComments = (markdown) => markdown.replace(/<!--[\s\S]*?-->\n?/g, '')

function rewriteLinks(markdown, relFile) {
  const dir = path.posix.dirname(relFile)
  return markdown.replace(/\]\((?!https?:|#|mailto:)([^)#\s]+\.md)(#[^)]*)?\)/g, (_m, href) => {
    const target = path.posix.normalize(path.posix.join(dir, href))
    return `](#${anchorId(target)})`
  })
}

// ---------- HTML 生成 ----------

const PAGE_CSS = `
  :root { color-scheme: light; }
  * { box-sizing: border-box; }
  body { font-family: -apple-system, "Hiragino Sans", "Noto Sans CJK JP", "Yu Gothic", sans-serif;
         font-size: 10.5pt; line-height: 1.7; color: #1a1a1a; margin: 0; }
  @page { size: A4; margin: 18mm 16mm; }
  section.page { max-width: 178mm; margin: 0 auto; }
  section.page + section.page { break-before: page; }
  h1 { font-size: 17pt; border-bottom: 2px solid #333; padding-bottom: 4px; }
  h2 { font-size: 13pt; border-bottom: 1px solid #bbb; padding-bottom: 2px; margin-top: 1.6em; }
  h3 { font-size: 11.5pt; margin-top: 1.4em; }
  table { border-collapse: collapse; width: 100%; font-size: 9.5pt; margin: 0.8em 0; }
  th, td { border: 1px solid #999; padding: 4px 8px; text-align: left; vertical-align: top; }
  th { background: #f0f0f0; }
  code { font-family: ui-monospace, "SF Mono", Menlo, monospace; font-size: 0.92em;
         background: #f4f4f4; padding: 1px 4px; border-radius: 3px; }
  pre { background: #f7f7f7; border: 1px solid #ddd; padding: 10px; overflow-x: auto; }
  pre code { background: none; padding: 0; }
  blockquote { border-left: 3px solid #ccc; margin-left: 0; padding-left: 12px; color: #555; }
  .mermaid svg { max-width: 100%; height: auto; }
  .mermaid, table, pre { break-inside: avoid; }
  .mermaid-error { border: 2px solid #c00; background: #fee; padding: 10px; color: #900;
                   font-family: ui-monospace, monospace; font-size: 9pt; white-space: pre-wrap; }
`

const RENDER_JS = `
  import markdownit from 'https://cdn.jsdelivr.net/npm/markdown-it@14/+esm'
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs'

  const md = markdownit({ html: false, linkify: true })
  const sections = JSON.parse(document.getElementById('spec-data').textContent)
  const root = document.getElementById('root')
  let errorCount = 0

  for (const s of sections) {
    const section = document.createElement('section')
    section.className = 'page'
    section.id = s.id
    section.dataset.file = s.file
    section.innerHTML = md.render(s.md)
    root.appendChild(section)
  }

  mermaid.initialize({ startOnLoad: false, theme: 'neutral' })
  const blocks = [...document.querySelectorAll('pre > code.language-mermaid')]
  for (let i = 0; i < blocks.length; i += 1) {
    const code = blocks[i]
    const file = code.closest('section.page').dataset.file
    const holder = document.createElement('div')
    holder.className = 'mermaid'
    code.parentElement.replaceWith(holder)
    const source = code.textContent
    try {
      const { svg } = await mermaid.render('mmd-' + i, source)
      holder.innerHTML = svg
    } catch (e) {
      errorCount += 1
      holder.className = 'mermaid-error'
      holder.dataset.mermaidError = String(e.message || e).slice(0, 300)
      holder.dataset.file = file
      holder.textContent = 'MERMAID ERROR (' + file + '): ' + (e.message || e) + '\\n\\n' + source
    }
  }
  document.querySelectorAll('[id^="dmmd-"], [id^="mmd-"]').forEach((el) => {
    if (el.tagName !== 'svg' && !el.closest('.mermaid')) el.remove()
  })
  const done = document.createElement('div')
  done.id = 'render-done'
  done.dataset.errors = String(errorCount)
  document.body.appendChild(done)
`

function buildHtml(title, sections) {
  const data = JSON.stringify(sections).replace(/</g, '\\u003c')
  return `<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>${title}</title>
<style>${PAGE_CSS}</style>
</head>
<body>
<div id="root"></div>
<script id="spec-data" type="application/json">${data}</script>
<script type="module">${RENDER_JS}</script>
</body>
</html>
`
}

// ---------- Chrome ----------

function findChrome() {
  const candidates = [
    process.env.CHROME_PATH,
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/Applications/Chromium.app/Contents/MacOS/Chromium',
    'google-chrome-stable',
    'google-chrome',
    'chromium-browser',
    'chromium',
  ].filter(Boolean)
  for (const c of candidates) {
    if (c.includes('/') && existsSync(c)) return c
    const found = spawnSync('which', [c], { encoding: 'utf8' })
    if (found.status === 0) return found.stdout.trim()
  }
  return null
}

function runChrome(chrome, args) {
  const result = spawnSync(chrome, ['--headless', '--disable-gpu', '--virtual-time-budget=20000', ...args], {
    encoding: 'utf8',
    maxBuffer: 256 * 1024 * 1024,
  })
  if (result.error) fail(`chrome failed to start: ${result.error.message}`)
  return result
}

function verifyRender(chrome, htmlPath, force) {
  const dom = runChrome(chrome, ['--dump-dom', `file://${htmlPath}`]).stdout
  if (!dom.includes('id="render-done"')) {
    fail('rendering did not finish — CDN (jsdelivr) に到達できているかネットワークを確認する')
  }
  const errors = [...dom.matchAll(/data-mermaid-error="([^"]*)"[^>]*data-file="([^"]*)"/g)]
  if (errors.length === 0) return
  err(`mermaid render errors: ${errors.length}`)
  errors.forEach(([, message, file], i) => err(`  ${i + 1}. ${file}: ${message}`))
  if (!force) fail('図を修正して再実行する（無視して出力する場合は --force）')
}

// ---------- zip ----------

function buildZip(zipPath, specDir, pdfPath) {
  if (spawnSync('which', ['zip'], { encoding: 'utf8' }).status !== 0) {
    err('warn: zip command not found — skipped zip (PDFのみ出力)')
    return false
  }
  const specParent = path.dirname(specDir)
  const specName = path.basename(specDir)
  execFileSync('zip', ['-r', '-q', zipPath, specName, '-x', '*/.DS_Store'], { cwd: specParent })
  execFileSync('zip', ['-j', '-q', zipPath, pdfPath])
  return true
}

// ---------- main ----------

function main() {
  const args = parseArgs(process.argv.slice(2))
  const specDir = path.resolve(args.specDir)
  if (!existsSync(specDir) || !statSync(specDir).isDirectory()) fail(`not a directory: ${args.specDir}`)

  const outDir = path.resolve(args.outDir)
  mkdirSync(outDir, { recursive: true })

  const files = collectFiles(specDir)
  const sections = files.map((rel) => ({
    id: anchorId(rel),
    file: rel,
    md: rewriteLinks(stripHtmlComments(readFileSync(path.join(specDir, rel), 'utf8')), rel),
  }))
  out(`pages: ${files.length} (${files[0]} → ${files[files.length - 1]})`)

  const stamp = new Date().toISOString().slice(0, 10).replace(/-/g, '')
  const base = `${path.basename(specDir)}-${stamp}`
  const htmlPath = path.join(args.htmlOnly ? outDir : os.tmpdir(), `${base}.html`)
  writeFileSync(htmlPath, buildHtml(`${path.basename(specDir)} 仕様書`, sections))

  if (args.htmlOnly) {
    out(`html: ${htmlPath}（ブラウザで開いて印刷でPDF化できる）`)
    return
  }

  const chrome = findChrome()
  if (!chrome) fail('Chrome/Chromium not found — CHROME_PATH で指定するか --html-only を使う')

  verifyRender(chrome, htmlPath, args.force)

  const pdfPath = path.join(outDir, `${base}.pdf`)
  runChrome(chrome, ['--no-pdf-header-footer', `--print-to-pdf=${pdfPath}`, `file://${htmlPath}`])
  if (!existsSync(pdfPath)) fail('PDF was not produced')
  out(`pdf: ${pdfPath}`)

  if (!args.noZip) {
    const zipPath = path.join(outDir, `${base}.zip`)
    if (buildZip(zipPath, specDir, pdfPath)) out(`zip: ${zipPath}（PDF + Markdownソース一式）`)
  }
}

main()
