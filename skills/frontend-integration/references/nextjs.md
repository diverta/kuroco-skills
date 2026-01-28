# Next.js 統合パターン

## 設定

```javascript
// next.config.js
module.exports = {
  env: {
    NEXT_PUBLIC_API_BASE: process.env.NEXT_PUBLIC_API_BASE,
    API_ID: process.env.API_ID
  }
}
```

## APIユーティリティ

```typescript
// lib/api.ts
const API_BASE = process.env.NEXT_PUBLIC_API_BASE
const API_ID = process.env.API_ID || '1'

export async function apiGet<T>(
  endpoint: string,
  params?: Record<string, any>
): Promise<T> {
  const query = params ? `?${new URLSearchParams(params)}` : ''
  const response = await fetch(
    `${API_BASE}/rcms-api/${API_ID}/${endpoint}${query}`,
    {
      credentials: 'include',
      cache: 'no-store'
    }
  )

  if (!response.ok) {
    throw new Error(`API Error: ${response.status}`)
  }

  return response.json()
}

export async function apiPost<T>(
  endpoint: string,
  body: Record<string, any>
): Promise<T> {
  const response = await fetch(
    `${API_BASE}/rcms-api/${API_ID}/${endpoint}`,
    {
      method: 'POST',
      credentials: 'include',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body)
    }
  )

  if (!response.ok) {
    throw new Error(`API Error: ${response.status}`)
  }

  return response.json()
}
```

## コンテンツ一覧（App Router）

```tsx
// app/news/page.tsx
import Link from 'next/link'
import { apiGet } from '@/lib/api'

interface NewsItem {
  topics_id: number
  subject: string
  ymd: string
}

interface NewsResponse {
  list: NewsItem[]
  pageInfo: {
    totalCnt: number
    pageNo: number
    totalPageCnt: number
  }
}

export default async function NewsPage() {
  const data = await apiGet<NewsResponse>('news', { cnt: '10' })

  return (
    <div>
      <h1>お知らせ一覧</h1>
      <ul>
        {data.list.map((news) => (
          <li key={news.topics_id}>
            <Link href={`/news/${news.topics_id}`}>
              {news.subject}
            </Link>
            <time>{news.ymd}</time>
          </li>
        ))}
      </ul>
    </div>
  )
}
```

## コンテンツ詳細（App Router）

```tsx
// app/news/[slug]/page.tsx
import { apiGet } from '@/lib/api'
import { notFound } from 'next/navigation'

interface NewsDetailResponse {
  details: {
    topics_id: number
    subject: string
    contents: string
    ymd: string
  }
}

interface Props {
  params: { slug: string }
}

export default async function NewsDetailPage({ params }: Props) {
  try {
    const data = await apiGet<NewsDetailResponse>(`newsdetail/${params.slug}`)

    return (
      <article>
        <h1>{data.details.subject}</h1>
        <time>{data.details.ymd}</time>
        <div dangerouslySetInnerHTML={{ __html: data.details.contents }} />
      </article>
    )
  } catch (error) {
    notFound()
  }
}
```

## SSG（Static Generation）

```tsx
// app/news/[slug]/page.tsx
export async function generateStaticParams() {
  const response = await fetch(
    'https://example.g.kuroco.app/rcms-api/1/news?cnt=0'
  )
  const data = await response.json()

  return data.list.map((news: any) => ({
    slug: news.topics_id.toString()
  }))
}
```

## プロジェクト構成

```
app/
├── news/
│   ├── page.tsx       # 一覧ページ
│   └── [slug]/
│       └── page.tsx   # 詳細ページ
├── login/
│   └── page.tsx
├── signup/
│   └── page.tsx
└── profile/
    └── page.tsx
lib/
├── auth.ts            # 認証関連
└── api.ts             # API呼び出し
```
