# Nuxt.js 統合パターン

## Nuxt 3 設定

```typescript
// nuxt.config.ts
export default defineNuxtConfig({
  runtimeConfig: {
    public: {
      apiBase: process.env.NUXT_PUBLIC_API_BASE || '',
      apiId: process.env.API_ID || '1'
    }
  }
})
```

## API呼び出しComposable

```typescript
// composables/useKurocoApi.ts
export function useKurocoApi() {
  const config = useRuntimeConfig()
  const apiBase = config.public.apiBase
  const apiId = config.public.apiId

  async function get<T>(endpoint: string, params?: Record<string, any>): Promise<T> {
    const query = params ? `?${new URLSearchParams(params)}` : ''
    const response = await $fetch<T>(
      `${apiBase}/rcms-api/${apiId}/${endpoint}${query}`,
      { credentials: 'include' }
    )
    return response
  }

  async function post<T>(endpoint: string, body: Record<string, any>): Promise<T> {
    const response = await $fetch<T>(
      `${apiBase}/rcms-api/${apiId}/${endpoint}`,
      {
        method: 'POST',
        credentials: 'include',
        headers: { 'Content-Type': 'application/json' },
        body
      }
    )
    return response
  }

  return { get, post }
}
```

## コンテンツ一覧（Nuxt 3）

```vue
<script setup lang="ts">
interface NewsItem {
  topics_id: number
  subject: string
  ymd: string
  contents: string
}

interface NewsResponse {
  list: NewsItem[]
  pageInfo: {
    totalCnt: number
    perPage: number
    totalPageCnt: number
    pageNo: number
  }
}

const { get } = useKurocoApi()
const { data: newsData } = await useAsyncData('news', () =>
  get<NewsResponse>('news', { cnt: 10 })
)
</script>

<template>
  <div>
    <h1>お知らせ一覧</h1>
    <ul v-if="newsData">
      <li v-for="news in newsData.list" :key="news.topics_id">
        <NuxtLink :to="`/news/${news.topics_id}`">
          {{ news.subject }}
        </NuxtLink>
        <time>{{ news.ymd }}</time>
      </li>
    </ul>

    <!-- ページネーション -->
    <div v-if="newsData?.pageInfo">
      <span>{{ newsData.pageInfo.pageNo }} / {{ newsData.pageInfo.totalPageCnt }} ページ</span>
    </div>
  </div>
</template>
```

## コンテンツ詳細（Nuxt 3）

```vue
<script setup lang="ts">
interface NewsDetail {
  topics_id: number
  subject: string
  contents: string
  ymd: string
  ext_col_01?: string
}

interface NewsDetailResponse {
  details: NewsDetail
}

const route = useRoute()
const { get } = useKurocoApi()

const { data: newsDetail } = await useAsyncData(
  `news-${route.params.slug}`,
  () => get<NewsDetailResponse>(`newsdetail/${route.params.slug}`)
)
</script>

<template>
  <article v-if="newsDetail">
    <h1>{{ newsDetail.details.subject }}</h1>
    <time>{{ newsDetail.details.ymd }}</time>
    <div v-html="newsDetail.details.contents"></div>
  </article>
</template>
```

## Nuxt 2 パターン

```vue
<template>
  <div>
    <h1>お知らせ一覧</h1>
    <ul>
      <li v-for="news in newsList" :key="news.topics_id">
        <nuxt-link :to="`/news/${news.topics_id}`">
          {{ news.subject }}
        </nuxt-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  async asyncData({ $axios }) {
    const response = await $axios.$get('/rcms-api/1/news', {
      withCredentials: true
    })
    return { newsList: response.list }
  }
}
</script>
```

## SSG対応（Nuxt 3）

```typescript
// nuxt.config.ts
export default defineNuxtConfig({
  nitro: {
    prerender: {
      routes: ['/news', '/about']
    }
  }
})
```

動的ルートの事前生成:

```typescript
// nuxt.config.ts
export default defineNuxtConfig({
  hooks: {
    async 'nitro:config'(nitroConfig) {
      const response = await fetch('https://example.g.kuroco.app/rcms-api/1/news?cnt=0')
      const data = await response.json()

      const routes = data.list.map((item: any) => `/news/${item.topics_id}`)
      nitroConfig.prerender?.routes?.push(...routes)
    }
  }
})
```

## 認証Composable（Nuxt 3）

```typescript
// composables/useAuth.ts
export function useAuth() {
  const user = useState<ProfileResponse | null>('user', () => null)
  const isLoggedIn = computed(() => user.value !== null)
  const { get, post } = useKurocoApi()

  async function login(email: string, password: string) {
    await post('login', { email, password })
    await fetchProfile()
  }

  async function logout() {
    await post('logout', {})
    user.value = null
  }

  async function fetchProfile() {
    try {
      const response = await get<ProfileResponse>('profile')
      user.value = response
    } catch {
      user.value = null
    }
  }

  return {
    user: readonly(user),
    isLoggedIn,
    login,
    logout,
    fetchProfile
  }
}
```
