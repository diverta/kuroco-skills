# Kurocoドキュメント: チュートリアル / 外部サービス連携（2/2）

収録ページ一覧。目的のページは Grep でタイトルまたは slug を検索し、該当行から Read してください。

## 収録ページ

- 自身のサイトにGoogle Mapを埋め込む（`how-to-setup-google-maps`）
- VAddyと連携してAPIエンドポイントに対する自動診断を設定する。（`integrating-with-vaddy`）
- Microsoft Teams と連携する（`microsoft-teams-setup`）
- Postmanを利用した正式版反映前のリグレッションテスト（`regression-testing-before-stable-version-release-using-postman`）
- OpenWeatherMapを利用して現在の天気を入力するAPIフィールドを設定する（`setting-up-api-field-for-current-weather-input-with-openweathermap`）
- X（旧Twitter）と連携し、コンテンツ投稿時にXへ自動投稿する（`setting-up-twitter-integration`）


---

# 自身のサイトにGoogle Mapを埋め込む

> 元ページ: `tutorials/how-to-setup-google-maps` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/how-to-setup-google-maps/
> 概要: このページでは、Google Mapを自身のサイトに埋め込む方法を説明します。

このページでは、Google Mapを自身のサイトに埋め込み、フロントエンドから位置情報を更新する方法を説明します。

## 概要

Kuroco のコンテンツにはGoogle Mapの位置情報を保存するための拡張形式が準備されています。
Kuroco管理画面から位置情報を入力する場合は、Kuroco管理画面のコンテンツ編集画面で表示される地図上の位置をクリックするだけで位置情報を指定できますが、フロントエンドでマップを表示する場合や、指定した位置情報を保存するインターフェースを提供する場合にはAPIを利用した実装が必要になります。
このチュートリアルでは、フロントエンドにGoogle Mapsのインターフェースを表示し、位置情報を更新する方法を説明します。  

### 前提条件

:::info
このページはKurocoでのプロジェクトが構築済みであることを前提としています。  
まだ構築していない場合は、下記のチュートリアルを参照してください。  
[Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)  
:::

:::info
本チュートリアルでは以下のバージョンでコードを書いています。  
Nuxt2: v2.15.8  
Nuxt3: v3.8.0  
:::

## GoogleMapの設定

### GCPで新しいプロジェクトを作成

まず、Google Cloud Platform（GCP）で新しいプロジェクトを作成します。
Google Cloud Platformにログインし、ヘッダー部のプロジェクトプルダウンをクリックしてください。  
表示されたポップアップ上部の「新しいプロジェクト」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1923da7ed0f335affd606e0357401173.png)

新しいプロジェクト設定画面で、任意のプロジェクト名を入力し、「作成」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/97657b8d4ac9413a85dfef9a23a199a1.png)

以上で新しいプロジェクトが作成されました。

### APIの有効化

続いてGCPのコンソールで必要なAPIを有効にします。

まずGCPコンソールのヘッダー部のプルダウンから作成したプロジェクトを選択します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9cc03d60984cfbdaad5527e7ec6c904d.png)

続いてサイドバーから「APIとサービス」- 「有効なAPIとサービス」を選択してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bd8e30b1dc7b41bddabe338fe57a35de.png)

サイドバーから「ライブラリ」を選択するとAPIライブラリページが表示されます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/bbf06293f26e7d3b2c8bfab0e7311a71.png)

ここで「Places API」と「Maps JavaScript API」を検索しそれぞれAPIを有効にしてください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5bc3b735d7049919eaca1f1040ed521b.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/dcf6d1ffb5c71003e19504c7e6e2bf19.png)

次にAPIキーを発行します。サイドバーから「認証情報」を選択し、「+認証情報を作成」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d90fbf56e1abad84ff550a2ad636863c.png)

APIキーを選択します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/548d59ce70f66dce5962931aa84aa4bd.png)

これにより、APIキーが生成されます。後で使用しますので控えてください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8167a435004c93af8cec6c377ce30aec.png)

### 許可ドメインの設定

ウェブサイトのドメインをAPIキー登録することで、APIの使用を制御します。これにより、他のウェブサイトからの不正アクセスが防げます。

認証情報の画面内にて、先ほど作成したAPIキーの右にあるボタンから「APIキーを編集」を選択します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e03ad86d2bf670719ac2d4389d73bbb8.png)

APIキーに任意の名前を入力し、アプリケーションの制限の設定から「ウェブサイト」を選択します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2181cc532512ffae3b6eeddc833594a6.png)

「ADD」ボタンをクリックし、利用する予定のサイトのドメインを入力、「完了」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a16c9bdc6ff9cd9c46c849301398be50.png)

## Kurocoの設定

### コンテンツ定義の設定

Kurocoのコンテンツ定義で拡張項目の任意の箇所に、以下の項目を設定します。

項目名 | 入力値
:-- | :--
項目名 | 地図（googleマップ）
識別子 | gmap
項目設定 | 地図


![Image from Gyazo](https://t.gyazo.com/teams/diverta/03d858234eab0adaccbc322ca5748b2c.png)

### エンドポイントの作成

Kurocoのコンテンツからマップの位置情報を取得するエンドポイントを作成します。  
以下のように入力してください。

項目名 | 入力値
:-- | :--
パス | `/rmcs-api/(API ID)/map/details/{topics_id}`
モデル | コンテンツ - Topics - details
APIリクエスト制限 | （閲覧を許可するグループまたはメンバーフィルタを選択）
キャッシュ | 86400
topics_group_id | （表示するコンテンツのコンテンツ定義ID）

![Image from Gyazo](https://t.gyazo.com/teams/diverta/15515a2a7ce1629825e3f94e4a670475.png)

次に、マップの位置情報更新用のエンドポイントを作成します。  
以下のように入力してください。

項目名 | 入力値
:-- | :--
パス | `/rmcs-api/(API ID)/map/update/{topics_id}`
モデル | コンテンツ - Topics - update
APIリクエスト制限 | （変更を許可するグループまたはメンバーフィルタを選択）
topics_group_id | （更新したいコンテンツのコンテンツ定義ID）
use_columns | `gmap`

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1cf6f21eed5d3cb834e6c493fa277917.png)


## フロントエンドの実装

### モジュールのインストール  

Google MapsのVue.jsコンポーネントを提供するモジュールをインストールします。

**Nuxt2:**

```sh
npm install vue2-google-maps
```

**Nuxt3:**

```sh
npm install vue3-google-map
```


### GCP KEYをconfigに記載

生成されたAPIキーを、ウェブサイトの設定ファイル（通常はconfigファイル）に記述します。これにより、ウェブサイトがAPIを利用できるようになります。  
Nuxt.jsで実装している場合、.env などに以下のように記載してください。


```markup title=".env"
BASE_URL=https://sample-service-site.g.kuroco.app
GCP_KEY=**************************************
```

:::tip
.envファイルの内容をデプロイ時に利用する場合は、.gitignoreから.envを削除して、.envもGitHubで管理するか、
GitHubのシークレットに登録した内容をGitHubActionsで読み込んで使用します。
:::

上記の設定を読み込むため、設定ファイルに以下のように追記してください。

**Nuxt2:**

```js title="nuxt.config.js"
export default {
  env: {
    GCP_KEY: process.env.GCP_KEY
  },
  // (中略)

  plugins: [
    // (中略)
    '@/plugins/vue2-google-maps.client'
  ],
```

**Nuxt3:**


```ts title="nuxt.config.ts"
export default defineNuxtConfig({
    runtimeConfig: {
        // Public keys that are exposed to the client
        public: {
            gcpKey: process.env.GCP_KEY,
            apiBase: 'https://*********.g.kuroco.app'
        }
    },
```


#### (Nuxt2のみ)

plugins/ ディレクトリに`vue2-google-maps.client.js` というファイルを追加し、以下のように記載してください。

**Nuxt2:**

```markup title="/plugins/vue2-google-maps.client.js"
import Vue from 'vue';
import * as VueGoogleMaps from 'vue2-google-maps';

Vue.use(VueGoogleMaps, {
    load: {
        key: process.env.GCP_KEY,
        libraries: 'places'
    }
});
```


### GoogleMapを表示するページの実装

ウェブサイトにGoogle Mapを表示してみましょう。
インストールしたコンポーネントを使用し、以下のように実装します。

**Nuxt2:**

```markup title="/pages/map/details/_id.vue"
<template>
  <div class="container">
    <h3>地図（googleマップ）</h3>
    <form id="topics_edit" @submit.prevent="update">
      <div>
        <GmapMap
          ref="gmap"
          :center="mapCenter"
          :zoom="gmap_zoom"
          :map-type-id="gmap_type"
          style="width: 500px; height: 300px"
        >
          <GmapMarker
            v-if="markPlace"
            :position="markPlace"
          />
        </GmapMap>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  async asyncData({ $axios, route }) {
    const id = route.params.id;
    const url = `/rcms-api/1/test/${id}`;

    const contents = await $axios
      .$get(url)
      .then((response) => {
        if (response.details) {
          return response.details;
        }
        return {};
      })
      .catch((error) => {
        console.log(error);
        return {};
      });
    // Googleマップの初期状態をセット
    let mapCenter = { lat: 35.66107078220203, lng: 139.7584319114685 };
    let markPlace = null;
    if (contents.gmap?.gmap_x && contents.gmap?.gmap_y) {
      const lat = Number(contents.gmap.gmap_y);
      const lng = Number(contents.gmap.gmap_x);
      mapCenter = { lat, lng };
      markPlace = { lat, lng };
    }

    return {
      mapCenter,
      markPlace,
      id,
      contents,
      errors: []
    };
  },
  computed: {
    gmap_zoom() {
      return Number(this.contents.gmap?.gmap_zoom) || 15;
    },
    gmap_type() {
      return this.contents.gmap?.gmap_type || 'roadmap';
    }
  }
};
</script>
```

**Nuxt3:**

```markup title="/pages/map/details/[id].vue"
<template>
  <div v-if="data" class="container">
    <h3>地図（googleマップ）</h3>
    <form id="topics_edit" @submit.prevent="update">
      <div>
        <GoogleMap
          :mapId="MAP_ID"
          ref="gmap"
          :center="mapCenter"
          :zoom="gmap_zoom"
          :map-type-id="gmap_type"
          style="width: 500px; height: 300px"
          @click="mark($event)"
          @zoom_changed="setZoom"
          @maptypeid_changed="gmap_type = $event"
          :api-key="key"
        >
          <AdvancedMarker
            v-if="markPlace"
            :options="markerOptions"
            @click="mapClicked"
          />
        </GoogleMap>
      </div>
      <input type="submit" value="Save" />
    </form>
  </div>
</template>

<script setup>
import { AdvancedMarker, GoogleMap } from "vue3-google-map";
const route = useRoute();
const config = useRuntimeConfig();
const key = config.public.gcpKey;
const gmap = ref(null);
const mapCenter = ref({ lat: 35.66107078220203, lng: 139.7584319114685 });
const markPlace = ref(null);
const markerOptions = computed(() => ({
  position: markPlace.value || mapCenter.value,
  draggable: true,
}));
const id = ref(route.params.id);
const contents = ref({});
const MAP_ID = "DEMO_MAP_ID";
console.log("googleMap", gmap.value);
const { data } = await useAsyncData("mapDetails", async () => {
  const url = `/rcms-api/1/newsdetail/${id.value}`;
  try {
    const response = await $fetch(url, {
      method: "GET",
      baseURL: config.public.apiBase,
      credentials: "include",
    });
    if (response.details) {
      return response.details;
    }
    return {};
  } catch (error) {
    return {};
  }
});
onMounted(() => {
  contents.value = data.value;
  if (contents.value.gmap?.gmap_x && contents.value.gmap?.gmap_y) {
    const lat = Number(contents.value.gmap.gmap_y)
      ? Number(contents.value.gmap.gmap_y)
      : 35.66107078220203;
    const lng = Number(contents.value.gmap.gmap_x)
      ? Number(contents.value.gmap.gmap_x)
      : 139.7584319114685;
    mapCenter.value = { lat, lng };
    markPlace.value = { lat, lng };
  }
});
const gmap_zoom = computed({
  get: () => Number(contents.value.gmap?.gmap_zoom) || 15,
  set: (val) => {
    if (!contents.value.gmap) contents.value.gmap = {};
    contents.value.gmap.gmap_zoom = String(val);
  },
});
const gmap_type = computed({
  get: () => contents.value.gmap?.gmap_type || "roadmap",
  set: (val) => {
    if (!contents.value.gmap) contents.value.gmap = {};
    contents.value.gmap.gmap_type = val;
  },
});
function mapClicked(event) {
  // console.log("mapCLicked", { event });
}
function setZoom() {
  contents.value.gmap.gmap_zoom = gmap.value.zoom;
}
</script>
``` 


:::caution
利用するエンドポイントのURLはご自身のものに調整してください。
:::

実行結果は以下のようになります。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/78356a2a924751626fccc06779951e14.png)

### GoogleMapの位置情報を更新するページの実装

続いて、フロントエンドから位置情報を更新できるようにしてみましょう。

**Nuxt2:**

```markup title="/pages/map/edit/_id.vue"
<template>
  <div class="container">
    <h3>地図（googleマップ）</h3>
    <div>
      地図上をクリックすると設定される位置が変わります。ズームなどの状態も設定できます。
    </div>
    <form id="topics_edit" @submit.prevent="update">
      <div>
        <form onsubmit="return false;">
          <GmapAutocomplete
            :options="{fields: ['geometry']}"
            :select-first-on-enter="true"
            @place_changed="setPlace"
          />
          <GmapMap
            ref="gmap"
            :center="mapCenter"
            :zoom="gmap_zoom"
            :map-type-id="gmap_type"
            style="width: 500px; height: 300px"
            @click="mark($event)"
            @zoom_changed="gmap_zoom = $event"
            @maptypeid_changed="gmap_type = $event"
          >
            <GmapMarker
              v-if="markPlace"
              :position="markPlace"
            />
          </GmapMap>
        </form>
      </div>
      <input
        type="submit"
        value="保存"
      >
    </form>
  </div>
</template>

<script>
export default {
  async asyncData({ $axios, route }) {
    const id = route.params.id;
    const url = `/rcms-api/1/test/${id}`;

    const contents = await $axios
      .$get(url)
      .then((response) => {
        if (response.details) {
          return response.details;
        }
        return {};
      })
      .catch((error) => {
        console.log(error);
        return {};
      });
    // Googleマップの初期状態をセット
    let mapCenter = { lat: 35.66107078220203, lng: 139.7584319114685 };
    let markPlace = null;
    if (contents.gmap?.gmap_x && contents.gmap?.gmap_y) {
      const lat = Number(contents.gmap.gmap_y);
      const lng = Number(contents.gmap.gmap_x);
      mapCenter = { lat, lng };
      markPlace = { lat, lng };
    }

    return {
      mapCenter,
      markPlace,
      id,
      contents,
      errors: []
    };
  },
  computed: {
    gmap_zoom: {
      get() { return Number(this.contents.gmap?.gmap_zoom) || 15; },
      set(val) { this.contents.gmap.gmap_zoom = String(val); }
    },
    gmap_type: {
      get() { return this.contents.gmap?.gmap_type || 'roadmap'; },
      set(val) { this.contents.gmap.gmap_type = val; }
    }
  },
  methods: {
    setPlace(place) {
      if (place.geometry) {
        this.markPlace = {
          lat: place.geometry.location.lat(),
          lng: place.geometry.location.lng()
        };
        if (place.geometry.viewport) {
          this.$refs.gmap.fitBounds(place.geometry.viewport);
        } else {
          this.$refs.gmap.panTo(place.geometry.location);
        }
      }
    },
    mark(event) {
      this.markPlace = {
        lat: event.latLng.lat(),
        lng: event.latLng.lng()
      };
    },
    async update() {
      const params = {
        gmap: {
          gmap_x: '',
          gmap_y: '',
          gmap_zoom: (this.contents?.gmap?.gmap_zoom || 15),
          gmap_type: (this.contents?.gmap?.gmap_type || 'roadmap')
        }
      };
      if (this.markPlace) {
        params.gmap.gmap_x = String(this.markPlace.lng);
        params.gmap.gmap_y = String(this.markPlace.lat);
      }
      await this.$axios.post(
        '/rcms-api/1/update_news/' + this.$route.params.id,
        params
      ).then((response) => {
        if (response.data.errors?.length) {
          console.log(response.data.errors);
        }
        this.errors = [];
      }).catch((error) => {
        console.log(error);
      });
    }
  }
};
</script>
```

**Nuxt3:**

```markup title="/pages/map/edit/[id].vue"
<template>
  <div v-if="data" class="container">
    <h3>地図（googleマップ）</h3>
    <div>
      地図上をクリックすると設定される位置が変わります。ズームなどの状態も設定できます。
    </div>
    <form id="topics_edit" @submit.prevent="update">
      <div>
        <GoogleMap
          :mapId="MAP_ID"
          ref="gmap"
          :center="mapCenter"
          :zoom="gmap_zoom"
          :map-type-id="gmap_type"
          style="width: 500px; height: 300px"
          @click="mark($event)"
          @zoom_changed="setZoom"
          @maptypeid_changed="gmap_type = $event"
          :api-key="key"
        >
          <AdvancedMarker
            v-if="markPlace"
            :options="markerOptions"
            @click="mapClicked"
          />
        </GoogleMap>
      </div>
      <input type="submit" value="保存" />
    </form>
  </div>
</template>

<script setup>
import { AdvancedMarker, GoogleMap } from "vue3-google-map";
const route = useRoute();
const config = useRuntimeConfig();
const key = config.public.gcpKey;
const gmap = ref(null);
const mapCenter = ref({ lat: 35.66107078220203, lng: 139.7584319114685 });
const markPlace = ref(null);
const markerOptions = computed(() => ({
  position: markPlace.value || mapCenter.value,
  draggable: true,
}));
const id = ref(route.params.id);
const contents = ref({});
const errors = ref([]);
const MAP_ID = "DEMO_MAP_ID";
console.log("googleMap", gmap.value);
const { data } = await useAsyncData("mapDetails", async () => {
  const url = `/rcms-api/1/newsdetail/${id.value}`;
  try {
    const response = await $fetch(url, {
      method: "GET",
      baseURL: config.public.apiBase,
      credentials: "include",
    });
    if (response.details) {
      return response.details;
    }
    return {};
  } catch (error) {
    return {};
  }
});

onMounted(() => {
  contents.value = data.value;
  if (contents.value.gmap?.gmap_x && contents.value.gmap?.gmap_y) {
    const lat = Number(contents.value.gmap.gmap_y)
      ? Number(contents.value.gmap.gmap_y)
      : 35.66107078220203;
    const lng = Number(contents.value.gmap.gmap_x)
      ? Number(contents.value.gmap.gmap_x)
      : 139.7584319114685;
    mapCenter.value = { lat, lng };
    markPlace.value = { lat, lng };
  }
});

const gmap_zoom = computed({
  get: () => Number(contents.value.gmap?.gmap_zoom) || 15,
  set: (val) => {
    if (!contents.value.gmap) contents.value.gmap = {};
    contents.value.gmap.gmap_zoom = String(val);
  },
});
const gmap_type = computed({
  get: () => contents.value.gmap?.gmap_type || "roadmap",
  set: (val) => {
    if (!contents.value.gmap) contents.value.gmap = {};
    contents.value.gmap.gmap_type = val;
  },
});

function mark(event) {
  markPlace.value = {
    lat: event.latLng.lat(),
    lng: event.latLng.lng(),
  };
  update();
}

function setZoom() {
  contents.value.gmap.gmap_zoom = gmap.value.map.zoom;
}

async function update() {
  const params = {
    gmap: {
      gmap_x: "",
      gmap_y: "",
      gmap_zoom: String(contents.value?.gmap?.gmap_zoom) || "15",
      gmap_type: contents.value?.gmap?.gmap_type || "roadmap",
    },
  };
  if (markPlace.value) {
    params.gmap.gmap_x = String(markPlace.value.lng);
    params.gmap.gmap_y = String(markPlace.value.lat);
  }
  try {
    const response = await $fetch(
      "/rcms-api/1/update_news/" + route.params.id,
      {
        method: "POST",
        credentials: "include",
        baseURL: config.public.apiBase,
        body: params,
      }
    );
    // console.log(response);
    if (response.data.errors?.length) {
      console.log(response.data.errors);
    }
    errors.value = [];
  } catch (error) {}
}
</script>

```


:::caution
利用するエンドポイントのURLはご自身のものに調整してください。
:::

実行結果は以下のようになります。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/a3e5f55c3d08dfa97cf5799c7fe7eca7.png)

保存ボタンをクリックするとピンを立てた位置やズームの状態などがKurocoのDBに書き込まれます。

:::caution
上記のサンプルコードでは簡単のため、非ログイン状態でもページが表示されるようになってますが、通常はログインしてから更新をおこないます。ログインについては以下をご参照ください。  
[KurocoとNuxt.jsで、ログイン画面を構築する](/ja/docs/tutorials/integrate-login/)
:::

以上で、Google Mapをあなたのウェブサイトに埋め込み、ウェブサイト上からKuroco管理画面と同様に位置情報を変更する事ができるようになりました。これらの手順によって、ウェブサイトのユーザーに素晴らしい地図体験を提供できます。

## 関連ドキュメント
- [Kurocoビギナーズガイド](/ja/docs/tutorials/beginners-guide/)
- [エンドポイントの設定方法](/ja/docs/tutorials/configure-endpoint/)
- [コンテンツ定義で利用できる項目設定一覧](/ja/docs/reference/list-of-extra-column-available-on-content/)
- [位置情報による並び替え](/ja/docs/reference/order-by-location/)


---

# VAddyと連携してAPIエンドポイントに対する自動診断を設定する。

> 元ページ: `tutorials/integrating-with-vaddy` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/integrating-with-vaddy/

KurocoではVAddyと連携することで、バックエンドで設定されている全てのAPIエンドポイントに対する脆弱性診断の自動的な定期実行が可能です。

このチュートリアルでは、Kuroco管理画面でのVAddyとの連携方法を説明します。

:::caution
VAddy側の仕様の変更により、VAddy側での操作方法は本チュートリアルと異なる箇所がある場合もございます。詳細は[VAddyサポートサイト](https://support.vaddy.net/hc/ja)で最新情報をご確認ください。  
:::

## 1. VAddyを申し込む  
Kuroco管理画面にアクセスし、[外部システム連携] -> [VAddy]をクリックします。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/18d2347f905e24b249c63e09c9f8bd43.png)
Kuroco管理画面の[VAddyページ](/ja/docs/management/vaddy/)から「VAddyの申し込みはこちらから」をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/8bbcaecbe913121ee07f68ed74d8e4f6.png)

サービスコードが適用された状態でVAddyのお申込みページに遷移しますので、VAddyのアカウント作成をお願いいたします。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/01cae640647c3ed0ba1e293928c51dae.png)

## 2. VAddyのプロジェクトを追加する
VAddyでは本番環境のサーバーへのスキャン実行は禁止されているため、診断を実施するためのFQDNを確認します。  
Kuroco管理画面にアクセスし、[外部システム連携] -> [VAddy]をクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/18d2347f905e24b249c63e09c9f8bd43.png)
Server FQDNに表示されている `kuroco-vaddy.com` のドメインのURLを確認します。  
こちらが診断を実施するためのFQDNになります。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/c69620c42538bfa4f46da1416ea93d3c.png)

次に[VAddyのスタートアップガイド](https://support.vaddy.net/hc/ja/articles/115006110548--STEP-1-%E3%83%97%E3%83%AD%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E3%81%AE%E4%BD%9C%E6%88%90)に従って、VAddy側でプロジェクトの作成をします。  
Server FQDNは`https://`を指定して、先ほど確認をした`kuroco-vaddy.com` のドメインのURLを入力してください。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/c7babf808f993748b59b9a669e28a997.png)
プロジェクトが追加できたら、表示された[プロジェクトID]と[Project number]をメモしておきます。  
Project numberはURL末尾の数字になります。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/5ddd89a0c27bc4eecca520349cf52a63.png)
## 3. サーバー所有者確認を実施する
認証ファイルのファイル名をKuroco管理画面に入力することで所有者確認のための認証ファイル設置ができます。  
まずはVAddyのプロジェクトページで認証ファイルのファイル名を確認します。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/cb83a4b0f9e84bf3e3da33b05e5bf195.png)
次にKurocoの管理画面で`vaddy-`から`.html`までの認証ファイルのファイル名を入力し、[更新する]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3597246362c9ea0e3a9e016a51582477.png)

Kuroco管理画面で認証ファイルの項目を入力したらVAddy側の所有者確認に戻り、[認証ファイルの設置を確認する]をクリックします。  

![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/9f0850c70bb92eb486a5b2fa2696f13a.png)
:::tip
ユーザーから認証文字列確認用のURLにアクセスした場合は403エラーになりますが、VAddy側からは確認ができ、認証が通ります。  
:::

## 4. API Auth Key (VADDY_TOKEN)を取得する 
[VAddyのWebAPIの画面](https://console.vaddy.net/user/webapi)にアクセスし、[Create WebAPI Key]をクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/6b2109733ea3bcfc87bcf78331fe90cc.png)
表示された[User ID (VADDY_USER)]と[API Auth Key (VADDY_TOKEN)]をメモしておきます。  
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/5287c22736c12e6af0eb69c64683cd20.png)
以上でVAddy側での作業は完了です。  
Kurocoでの自動的な脆弱性診断はKurocoのエンドポイントをシステム側で自動的に登録するので、[「【STEP 2】クロールの設定と実行」](https://support.vaddy.net/hc/ja/articles/115005935107--STEP-2-%E3%82%AF%E3%83%AD%E3%83%BC%E3%83%AB%E3%81%AE%E8%A8%AD%E5%AE%9A%E3%81%A8%E5%AE%9F%E8%A1%8C)は実施不要です。  

## 5. Kurocoの設定をする。
次にKuroco側の設定をします。  
Kuroco管理画面にアクセスし、[外部システム連携] -> [VAddy]をクリックします。
![Image (fetched from Gyazo)](https://t.gyazo.com/teams/diverta/18d2347f905e24b249c63e09c9f8bd43.png)
「2. VAddyのプロジェクトを追加する」「4. API Auth Key (VADDY_TOKEN)を取得する」でメモした下記の情報を入力し、[更新する]をクリックします。  
- User ID (VADDY_USER)
- API Auth Key (VADDY_TOKEN)
- プロジェクトID
- Project number

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d1576073c76e57c26c703a191332d6a9.png)

以上でKurocoとVAddyの連携は完了です。
バックエンドで設定されている全てのAPIエンドポイントに対する脆弱性診断の自動的な定期実行がされるようになります。  
脆弱性診断は日次で、午前3時頃に実施されます。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d3673d45d08fb49559c68e47d512b066.png)

## 関連ドキュメント
- [VAddy](/ja/docs/management/vaddy/)
- [セキュリティ](/ja/docs/about/security/)
- [脆弱性診断・検査に関して教えてください](/ja/docs/faq/what-vulnerability-diagnostic-and-assessment-services-do-you-provide/)
- [脆弱性診断で指摘を受けたのでどうすればいいか教えてください](/ja/docs/faq/my-site-was-diagnosed-with-a-security-vulnerability/)


---

# Microsoft Teams と連携する

> 元ページ: `tutorials/microsoft-teams-setup` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/microsoft-teams-setup/
> 概要: KurocoエージェントをMicrosoft TeamsのBotとして設定し、TeamsのチャットでBotにメッセージを送るとManaged Agentが処理して返信する仕組みを構築する手順を説明します。

KurocoエージェントをMicrosoft TeamsのBotとして使えるようにする手順を説明します。

設定が完了すると、TeamsのチャットでBotにメッセージを送ると、Kurocoに登録されたManaged Agentが処理して返信するようになります。

:::info
**前提条件**

- Kurocoの管理者権限
- Azureのサブスクリプション（Botリソースを作成できる権限）
- Microsoft 365テナントの管理者権限（Teamsアプリを組織にインストールする場合）
:::

## 全体の流れ

```text
① Azureでアプリ登録（App ID・クライアントシークレット取得）
         ↓
② Azure Botリソースを作成
         ↓
③ KurocoでTeams連携を有効化（App ID等を入力・Teamsアプリパッケージを作成）
         ↓
④ Azure BotのMessaging endpointにKurocoのURLを設定
         ↓
⑤ TeamsチャネルをAzure Botに追加
         ↓
⑥ TeamsにBotアプリをインストール
         ↓
⑦ KurocoのAPIでMCPサーバー・teams_sendエンドポイントを確認・設定
         ↓
⑧ KurocoでManaged Agentを作成
         ↓
⑨ コンテンツ定義を作成してTeamsとAI自動処理を設定
```

メッセージの流れ：

```text
Teamsユーザーがメッセージ送信
  → Azure Bot（Messaging endpoint: KurocoのURL）
  → Kurocoがメッセージ受信・コンテンツ定義に保存
  → AI自動処理が起動（Managed Agentを自動呼び出し）
  → Managed Agentが処理
  → teams_send（Kuroco MCP）でTeamsに返信
```

## 1. Azureでアプリ登録を作成する

[Azure Portal](https://portal.azure.com) にアクセスしてサインインします。

上部の検索バーに「**アプリの登録**」と入力し、選択します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ee5d17f61d225f5b2e94b854f3e9fa0f.png)

**「＋ 新規登録」** をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5f8429b93a0b3821450cca7eb416d0ce.png)

以下を入力して **「登録」** をクリックします。

| 項目 | 入力値 |
|------|--------|
| 名前 | 任意（例：`KurocoBot`） |
| サポートされているアカウントの種類 | 下記を参照 |
| リダイレクト URI | 空欄のまま |

「サポートされているアカウントの種類」は利用シーンに合わせて選択します。

| 選択肢 | 説明 | 推奨シーン |
|--------|------|-----------|
| **シングル テナントのみ** | 自社テナントのユーザーのみ利用できる | 社内向けBotの場合（一般的） |
| 複数の Entra ID テナント | 複数の組織をまたいで利用できる | 複数社に提供する場合 |
| 任意の Entra ID テナント + 個人用 Microsoft アカウント | 組織アカウントに加え個人アカウントも利用できる | 外部ユーザーも含める場合 |
| 個人用アカウントのみ | 個人の Microsoft アカウントのみ | 一般消費者向けの場合 |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/da8acca6d4935af4375d88343f79f513.png)

登録完了後、**「概要」** 画面に表示される以下の値を控えます。手順3（Azure Bot作成）と手順4（Kuroco設定）で使います。

| 控える値 | 場所 | 使用する手順 |
|---------|------|------------|
| **アプリケーション（クライアント）ID** | 概要ページ上部 | 手順3・手順4 |
| **ディレクトリ（テナント）ID** | 概要ページ上部 | 手順3・手順4 |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/150953548a52340d2f073f2315d1487c.png)

## 2. クライアントシークレットを作成する

左メニューの **「証明書とシークレット」** をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9d8909bf8967e0230b6e44b0e9ad261c.png)

**「＋ 新しいクライアント シークレット」** をクリックします。

説明に任意の名前（例：`kuroco-teams-bot`）を入力し、有効期限を選択して **「追加」** をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2b349103dfbe36984e3d80ee4d465452.png)

:::caution
有効期限のデフォルトは180日（6か月）です。期限が切れるとBotが動作しなくなるため、本番運用では長めの期限を設定するか、期限切れ前に更新する運用ルールを設けてください。
:::

生成されたシークレットの **「値」** 列の文字列をコピーして安全な場所に控えます（例：パスワードマネージャー、または組織が管理する秘密情報の保管場所）。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ef0d64404401a1d11f03635cd75f5459.png)

:::caution
このシークレット値はこの画面を閉じると二度と表示されません。必ず今コピーしてください。
:::

## 3. Azure Botリソースを作成する

Azureポータルの検索バーに「**Azure Bot**」と入力します。検索結果の **「Marketplace」** セクションに表示される **「Azure Bot」** を選択します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/337ff13cb2249887943aba755734d5d0.png)

**「＋ 作成」** をクリックします。

**「Basics」タブ** で以下を入力します。

| 項目 | 入力値 |
|------|--------|
| Bot handle | 任意（例：`KurocoBot`） |
| サブスクリプション | 使用するサブスクリプションを選択 |
| リソース グループ | 既存を選択または**「新規作成」**をクリックして作成 |
| Data residency | **Global**（デフォルトのまま） |
| Type of App | **Single Tenant** |
| Creation type | **Use existing app registration** |
| App ID | 手順1で控えたアプリケーション（クライアント）ID |
| App tenant ID | 手順1で控えたディレクトリ（テナント）ID |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/7c59cd8f3e1ce9f378c5788bfc0d1ede.png)

価格レベルはデフォルトで **Standard** になっています。テスト・開発用途であれば **F0（無料）** に変更します。① **「Change plan」** をクリックし、② **「F0 Free」** を選択して、③ **「選択」** をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/27569f8d10b9ab38e955240ed8afc337.png)

**「確認と作成」→「作成」** をクリックします。

デプロイが完了したら **「リソースに移動」** をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/dcd9a8f4d9aeecb346fdce73f5f8f80a.png)

## 4. KurocoでTeams連携を有効化する

Kuroco管理画面にログインし、左メニューの **[チャネル] → [メッセージング] → [Microsoft Teams]** をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/61c460de60dc82e98a1f9c54cf907c6a.png)

**「有効にする」** トグルをONにします。

以下を入力します。

| 項目 | 入力値 |
|------|--------|
| **Microsoft App ID** | 手順1で控えたアプリケーション（クライアント）ID |
| **App Password（クライアントシークレット）** | 手順2で控えたシークレット値 |
| **アプリの種類** | SingleTenant |
| **テナントID** | 手順1で控えたディレクトリ（テナント）ID |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/53cd650f4d3980a7e7bbdebbf4c4ed55.png)

続けて **「マニフェスト設定」** セクションも入力します。

| 項目 | 入力値 |
|------|--------|
| **ボット名** | Teamsに表示されるBot名（例：`KurocoBot`） |
| **ボットの説明** | 任意（例：`A chat bot powered by Kuroco`） |

**「更新する」** をクリックします。

設定画面の **「Messaging endpoint URL」** に表示されているURLを控えます。

```text
https://{your-site}.g.kuroco.app/direct/topics/teams/
```

:::tip
このURLを次の手順でAzure Botに登録します。
:::

続けて同じ画面で、**「manifest.json」** セクションの **「manifest.jsonをダウンロード」** をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/63d34e74373de76024de60e98f94be3a.png)

以下のサイズのアイコン画像を2枚準備します。

| ファイル名 | サイズ |
|-----------|--------|
| `outline.png` | 32×32ピクセル・透過PNG |
| `color.png` | 192×192ピクセル |

以下の3ファイルをZIPファイルにまとめます。フォルダは作らず、3ファイルを直接ZIPに含めます。

```text
teams-app.zip
├── manifest.json
├── outline.png
└── color.png
```

:::tip
このZIPファイルは後の手順（手順7）でTeamsにインストールします。今すぐ使わなくても、ここで作成しておきましょう。
:::

## 5. Azure BotにMessaging endpointを設定する

Azureポータルで作成したAzure Botリソースを開き、**[構成]** をクリックします。

**「メッセージング エンドポイント」** に手順4で控えたURLを入力します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9f30c38a2ef0a7716d63a084fc9af7c3.png)

**「適用」** をクリックします。

## 6. TeamsチャネルをAzure Botに追加する

Azure Botリソースの左メニューで **[チャネル]** をクリックします。

**「Microsoft Teams」** を選択します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8f404a6d9d796cad9491f882becef10b.png)

**「Microsoft Teams Commercial (most common)」** が選択されていることを確認し、**「Apply」** をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6697cca606f023b7dd192e4623738867.png)

**「Terms of Service」** ダイアログが表示されます。チェックボックスにチェックを入れ、**「Agree」** をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1308647c5e972b39bd863507bf80b88f.png)

## 7. TeamsにBotアプリをインストールする

### 組織全体にインストールする場合（管理者向け）

[Microsoft Teams 管理センター](https://admin.teams.microsoft.com) にアクセスします。

**[Teams アプリ] → [アプリの管理]** を開きます。

**「＋ アップロード」→「カスタムアプリのアップロード」** をクリックし、手順4で作成したZIPファイルを選択します。

:::info
この操作にはMicrosoft 365テナントの管理者権限が必要です。権限がない場合は組織のTeams管理者に依頼してください。
:::

### テスト・開発用にサイドロードする場合

Microsoft Teamsのデスクトップアプリを開きます。

左メニュー下部の **「アプリ」** をクリックします。

**[アプリを管理] → [カスタムアプリをアップロード]** をクリックし、ZIPファイルを選択します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9faa11aa769ce71966a2c97043dc43aa.png)

:::caution
「カスタムアプリをアップロード」が表示されない場合、組織のTeams管理者にカスタムアプリのアップロード許可設定を依頼してください。
:::

### ボットを検索して追加する

アップロード後、Teamsの **「アプリ」** 検索欄にBotの名前を入力して選択します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2e1d8f0c496c98be6256055b13c1389a.png)

**「追加」** をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c9c8a819ab7917d5a3d2f5d7d34d0c2a.png)

「正常に追加されました。」と表示されたら **「開く」** をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b1fe705a7fc1b7613eb89decf3d2f943.png)

## 8. KurocoのAPIでMCPサーバーを確認する

Kuroco管理画面で **歯車アイコン（設定）** をクリックし、**「API」** から `teams_send` などのTeams連携ツールを含むAPIを開きます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/15e898e5f31a27344e2593d3918acc22.png)

**「MCPサーバー」** が **「有効」** になっていることを確認します。表示されているURLが、次の手順でエージェントに設定するMCPエンドポイントです。

```text
https://{your-site}.g.kuroco.app/rcms-api/{id}/mcp
```

:::info
MCPサーバーが有効になっていない場合は、「設定」ボタンから有効化してください。セキュリティは **「動的アクセストークン」** を選択します。
:::

続けて、**エンドポイント一覧** に `teams_send` が存在することを確認します。ない場合は **「＋」** ボタンをクリックして追加します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8258c68b7846f64e32175c4b2c4c7d41.png)

| 項目 | 設定値 |
|------|--------|
| **パス** | `teams_send` |
| **カテゴリー** | `Integrations` |
| **モデル** | `Teams` |
| **オペレーション** | `send` |
| **ステータス** | **「有効にする」** をON |

続けて左メニューの **「基本設定」** タブを開きます。以下のパラメータは **空欄のまま** にしてください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/018bb1648d6436f59b8f6f2579e55654.png)

| パラメータ | 説明 | 設定値 |
|-----------|------|--------|
| `conversation_id` | Teams 会話ID | **空欄**（実行時に動的に渡されます） |
| `service_url` | Teams serviceUrl | **空欄**（実行時に動的に渡されます） |
| `reply_to_id` | Teams 返信先Activity ID | **空欄**（実行時に動的に渡されます） |

続けて左メニューの **「MCP設定」** タブを開き、以下を設定します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2f027f28cf0310c0f21bbd8ae16ae17c.png)

| 項目 | 設定値 |
|------|--------|
| **ツール名** | `teams_send` |
| **入力データ定義** | **「デフォルトスキーマを使用」** をON（API定義から自動生成） |
| **出力データ定義** | 選択なし |
| **ステータス** | **「有効にする」** をON |

設定したら **「更新」** をクリックします。

## 9. KurocoでManaged Agentを作成する

Kuroco管理画面で **脳マークのアイコン** をクリックし、**「AIエージェント」** を選択します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/fc0161568e3b9746d5a8f025a3cbd806.png)

**「＋ 追加」** をクリックして新しいエージェントを作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e8f7a622bf1b58264007538d60579a6c.png)

以下を設定します。

| 項目 | 設定値 |
|------|--------|
| **名前** | 任意（例：`Teams Agent`） |
| **モデル** | 使用するClaudeモデルを選択（例：`claude-sonnet-5`） |
| **システムプロンプト** | 以下の例を参考に入力します |
| **ステータス** | **「有効にする」** をON |

**システムプロンプトの例:**

```text
あなたは社内ナレッジを検索してTeamsに回答するアシスタントです。

## 実行手順（この順番を必ず守ること）

### ステップ1: 意図判定

受信したメッセージを以下の3つに分類する：

- reply: 質問・相談・依頼など、回答が必要なメッセージ
- knowledge_add: 社内ナレッジへの追加・更新を明示的に意図した情報共有
  （「～を共有します」「～を追加してください」のように情報提供の意図が明確なもの。質問っぽいものは reply にする）
- both: reply と knowledge_add の両方が必要

判定に迷ったら reply に倒す。

---

### ステップ2: reply / both の場合

1. knowledge_search ツールで関連ナレッジを検索する
   - cnt=10 を必ず指定する
   - 必ず vector_search で検索する
   - 質問を2～3個のクエリに分解する
   - 1回目が不十分なら別キーワードで追加検索する

2. teams_send で返信する（Teams返信フォーマット参照）

both の場合はこの後ステップ3も実行する

---

### ステップ3: knowledge_add / both の場合

1. 重複チェック
   knowledge_search で類似ドキュメントを検索する（cnt=5、vector_search を利用）
   - 同内容が既に十分カバーされている → result =「既存ドキュメントあり: {タイトル}」として5へ
   - 追記が適切な場合 → そのファイルパスをメモして2へ

2. 既存 PR の確認
   同内容または対象ファイルへの更新 PR を確認する
   - 存在する → result =「既存 PR あり: {PR リンク}」として5へ
   - 存在しない → 3へ

3. ファイルパスの決定
   以下のディレクトリ構造に従って保存先を決定する：
   - Support/ — サポート・問い合わせ対応
   - Kuroco/ — Kuroco CMS の使い方・設定・API
   - Diverta Inc./ — 社内規程・会社情報
   - なんでもQA/ — 汎用的なQ&A
   ファイル名は内容を端的に表す日本語スラッグとする（例：メール自動返信設定.md）

4. Markdown の作成と GitHub PR の作成

   # タイトル

   ## 概要
   （1～2文で内容を説明）

   ## 詳細
   （手順・説明・コード例など）

   ## 関連
   （関連ドキュメント・リンクなど、あれば記載）

   - ブランチ名: knowledge/update/{YYYYMMDD-HHMMSS}
   - 決定したパスにファイルを作成または更新する
   - PR を作成する（タイトル: docs: {内容を要約したタイトル}、本文に情報源を記載）
   - PR はレビュー必須（自動マージしない）
   - result =「PR を作成しました: {PR URL}」として5へ

5. teams_send で結果を報告する

---

### ステップ4: query_log を記録する（必須・すべての意図で実行）

以下のフィールドのみを渡すこと（topics_id は不要・含めない）:
{
  "subject": "メッセージの要点（200文字以内）",
  "source": "teams",
  "maxDense": "0.9",
  "hitCount": 5
}
- maxDense は文字列で渡す（例: "0.9"）
- maxDense の基準:
  - "0.9"～"1.0": ナレッジに明確な回答があった
  - "0.5"～"0.8": 部分的に回答できたが情報が不完全だった
  - "0.0"～"0.4": ナレッジが見つからず回答できなかった
- hitCount は knowledge_search で得られたヒット件数の合計（整数）
- knowledge_add のみの場合は hitCount=0, maxDense="0.0" でよい

---

## Teams返信フォーマット（重要）

teams_send の message には、Teamsでそのまま表示される文章を入れること。

禁止:
- Markdown記法を使わない
- 箇条書きの「-」「*」を使わない
- 見出し記法「##」「###」を使わない
- 太字、斜体、コードブロック、表を使わない
- Markdownリンク記法 [表示名](URL) を使わない

返信フォーマット:
{検索結果に基づく回答。手順は番号付きリスト、ポイントは箇条書きで整形する}

参照ソース:
・{subject}: {URL}

## 参照ソースの書き方（重要）
- URL は必ず次のテンプレート:
  https://{your-site}.g.kuroco-mng.app/management/topics/topics_edit/?topics_id=TOPICS_ID
  TOPICS_ID は検索結果の topics_id（数値）で置き換える
- 表示テキストには検索結果の subject フィールドを使う
- GitHub の URL（github.com/...）や ext_2 のファイルパスは参照ソースとして使わない
- {your-site}.g.kuroco-mng.app のみを使う

## 注意事項
- 検索結果にない情報は「該当するナレッジが見つかりませんでした」と正直に伝える
- 推測や外部知識で補完しない。検索結果のみを使う
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b839ab0f2b314701ed94bee72aa205d0.png)

続けて **「エージェントに許可する行動」** セクションで以下を設定します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e77f5e322881b9f091925698e3386d3f.png)

| | 設定内容 |
|-|---------|
| **① MCPサーバー（Kuroco API）** | 手順8で確認したAPI（`teams_send` などのTeams連携ツールを含むもの）を選択 |
| **② MCP許可ポリシー** | **「常に許可」** を選択（エージェントが自律的にツールを実行するために必須） |
| **③ MCP認証メンバーID** | Kurocoでの自分のメンバーIDを入力 |
| **④ 更新する** | クリックして保存 |

**「更新する」** をクリックして保存します。

## 10. コンテンツ定義を作成してTeamsとAI自動処理を設定する

Kuroco管理画面で **「コンテンツ」** をクリックし、**「コンテンツ定義」** を選択します。**「＋ 追加」** をクリックして新しいコンテンツ定義を作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/edd6a592cb2855e5c93088a2a56f0f88.png)

**「全般」** タブで以下を設定します。

| 項目 | 設定値 |
|------|--------|
| **コンテンツ定義名** | 任意（例：`Teams`） |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a753adf9698c8483da191e14b473152e.png)

続けて左メニューの **「Microsoft Teams」** タブを開き、以下を設定します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4bc784868cef6fbbbc8e52844a784605.png)

| 項目 | 設定値 |
|------|--------|
| **Teamsメッセージ履歴を有効にする** | **ON** |
| **受付自動返信** | **ON** |
| **返信メッセージ** | 任意（例：`お問い合わせを受け付けました。処理内容によっては1～3分かかる場合があります。少々お待ちください。`） |
| **Teams conversation ID** | 空欄（全チャネルが対象になります） |

続けて左メニューの **「AI自動処理」** タブを開き、以下を設定します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8503ef477f96c14969cbd052f9745f30.png)

**「AI自動後処理」** を **「有効にする」** に切り替えます。

**「変換ルール」** の **「＋ 追加」** をクリックし、以下を設定します。

| 項目 | 設定値 |
|------|--------|
| **プロンプト** | `このtextに返信してください：　conversation_id='$conversation_id'　service_url='$service_url'　text='$text'` |
| **実行タイミング** | `新規作成時` |
| **作成ステータス** | `公開` |
| **入力フィールド** | 全て選択済み |
| **AIエージェントを使用** | 選択する |
| **AIエージェント** | 手順9で作成したエージェント（例：`Teams Agent`）を選択 |

:::info
「AIエージェントを使用」を選択すると、それ以降のルールは追加できなくなります。エージェントの選択でルールチェーンが完了します。
:::

**「更新する」** をクリックして保存します。

## 動作確認

Botとのチャット画面が開きます。メッセージを送信して、エージェントから返信が届くことを確認します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/15250c021b061c594d83568ca2c8e062.png)

## Kuroco管理画面からテスト送信する（オプション）

動作確認で一度Botとメッセージのやり取りをすると、手順10で作成したコンテンツ定義にTeamsとの会話情報が保存されます。この会話情報を使うと、Teamsアプリを開かずにKuroco管理画面だけからBotの送信を再現テストできます。

:::tip
Managed Agentのシステムプロンプトや返信フォーマットを調整するたびにTeamsからメッセージを送り直さなくても、一度取得した会話情報を使い回してKuroco側だけで送信を繰り返し検証できます。
:::

### 会話情報を確認する

Kuroco管理画面で、手順10で作成したコンテンツ定義（例：`Teams`）の一覧を開き、確認したいレコードをクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c151f96458b789478f05cf30b4630cca.png)

詳細画面で以下の値を控えます。

| 項目 | 場所 |
|------|------|
| **conversationId** | `conversationId` フィールド |
| **serviceUrl** | `serviceUrl` フィールド |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/baecddb211a624761c6a6848b5ce7978.png)

### テスト送信する

**[チャネル] → [メッセージング] → [Microsoft Teams]** の設定画面を開き、下部の **「テスト」** セクションに以下を入力します。

| 項目 | 入力値 |
|------|--------|
| **Teams serviceUrl** | 上記で確認したserviceUrl |
| **Teams 会話ID** | 上記で確認したconversationId |
| **メッセージ** | 任意の送信内容 |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5902f400f9dbfc9c7e790062e03c7408.png)

**「テストする」** をクリックすると、入力したメッセージがTeamsに送信されます。Teams側でメッセージが届くことを確認します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/9e3a27dd37148e3ead2bb66c15446bf4.png)

## トラブルシューティング

| 症状 | 確認箇所 |
|------|---------|
| Botがメッセージに返信しない | Azure BotのMessaging endpointが正しいか・Kurocoのトリガー設定を確認します |
| 認証エラーが出る | KurocoのApp IDとApp Passwordが正しいか確認します |
| Teamsでアプリが見つからない | ZIPファイルの構成（フォルダなし・3ファイル直下）を確認します |
| エージェントが起動しない | Kuroco側のAI自動処理（変換ルール）の設定を確認します |


---

# Postmanを利用した正式版反映前のリグレッションテスト

> 元ページ: `tutorials/regression-testing-before-stable-version-release-using-postman` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/regression-testing-before-stable-version-release-using-postman/
> 概要: 正式版の反映前後でAPIレスポンスが変化していないかを確認するため、Postmanを利用してリグレッションテストを行う方法を説明します。

## 概要
正式版の反映前後でAPIレスポンスが変化していないかを確認するため、Postmanを利用してリグレッションテストを行う方法を説明します。  
APIのレスポンスが変わる場合はSlackコミュニティ等でお知らせがされますが、対象のエンドポイントや使い方をしている箇所がないか確認するのにご活用ください。

### 前提条件
- 主にProject Managerを対象としています。クライアント案件サイトのAPIレスポンスが以前と変化していないことを最低限確認するためのテストです。
- Postmanのアプリケーションを利用して、ローカル環境から手動でテストを実行します。
- 静的アクセストークンのAPI (GETメソッド) のみを対象としています。

:::caution
- Postmanはテスト用のコレクションファイルや実行ログを日本国外(USまたはEU)に保管します。テスト実施可否を事前にクライアントへ確認し、必ず許可を得てください。  
  - [Security at Postman](https://www.postman.com/trust/security/)  
- 機密情報や個人情報を含むサイトは絶対に対象としないでください。必要な場合は、それらを全てダミーデータに置き換えたテスト用の環境を別途用意してください。 
::: 

### テスト実施のフロー
以下の流れで、正式版反映直前のRC版に対してテストを実行し、APIレスポンスに変化がないかを事前に確認します。

1. 正式版環境のAPIが返すレスポンスデータをすべて取得・保存する
2. RC版にバージョンを切り替える
3. 各APIに対してリクエストし、1の時点で保存していたAPIレスポンスと比較する

## 事前準備
まずは以下のURLからPostmanに登録します。
- https://identity.getpostman.com/signup

![Image from Gyazo](https://t.gyazo.com/teams/diverta/d68f157349ff14da2f87afbe9ecedd5a.png)

<!--ENキャプチャ-->
<!--
![Image from Gyazo](https://t.gyazo.com/teams/diverta/f291cdf6ced86f5caf55cf9f26f33bf6.png)
-->

登録ができたらPostmanでワークスペースの作成します。  
[ワークスペースの作成]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/aad2151ef6e65d392c6148eae4269ec5.png)

<!--ENキャプチャ-->
<!--
[Image from Gyazo](https://t.gyazo.com/teams/diverta/0f47af560e28e296d09e64d3ace290de.png)
-->

[空のワークスペース]を選択し、次へ進みます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b549d468be41f8067e8fa54c0d473764.png)

<!--ENキャプチャ-->
<!--
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ddd4b5de83b4ecca7eb20e72f2863e0e.png)
-->

プロジェクト名を入力し、Internal (非公開) が選択された状態で、ワークスペースを新規作成します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/dd8363e3db2b8a151ef9ab5a0dd71e53.png)

<!--ENキャプチャ-->
<!--
![Image from Gyazo](https://t.gyazo.com/teams/diverta/80ee275e68176771d31378511f9d720a.png)
-->

以降は、以下のURLからPostmanのアプリケーションをダウンロードしてデスクトップ版のPostmanを使用します。
- https://www.postman.com/downloads/

:::tip
ブラウザ版で進めることもできますが、その場合はCORSポリシーに従う必要があるため、Kuroco側のCORS設定に以下の追加が必要です。
- `CORS_ALLOW_ORIGINS`に`https://プロジェクト名.postman.co`を追加
- `CORS_ALLOW_HEADERS`に以下を追加
  - X-RCMS-API-ACCESS-TOKEN
  - User-Agent
  - Cache-Control
  - Postman-Token

:::

## テスト作成方法
### KurocoのAPIをOpenAPI形式でエクスポート
Kurocoの管理画面でテスト実行対象APIのエンドポイント一覧画面を開き、[OpenAPIエクスポートする] を選択します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/8b01423198d65c8e27d606257e96c9fa.png)

出力形式に [JSON] を選択し、`openapi.json` (APIの定義ファイル) をダウンロードします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b3683c7c734bb590b14385d58591c1ce.png) 

### Postmanコレクションファイルの作成
エクスポートしたAPIの定義を利用して、Postmanのコレクションファイル（実行するテストをまとめたファイル）を作成します。

API定義からPostmanコレクションファイルを作成するためのスクリプトを準備していますので、
Node.jsスクリプトを実行できる環境で、`openapi-to-postmanv2@^5.0.0`のをインストールし、以下のスクリプトを実行してください。  
https://gist.github.com/sakaguchi-diverta/2fbedcc430366126fea46d0f5a127a23

:::caution
スクリプトの内容や配置先は今後変更する可能性があります。
:::

スクリプト実行の詳細説明は省略します。  
AIエージェントに作業や解説を依頼しても構いません。  
弊社ではDevinに実行を依頼することでPostmanコレクションファイルを生成しました。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/729b3181ca220a218b94576bd481efec.png)

実行が完了すると、Postmanのコレクションファイル`postman_collection.json`が出力されます。

### Postmanコレクションのインポートと調整
Postmanのワークスペースに戻り、[インポート]を選択し、先ほど出力した`postman_collection.json`をアップロードします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/1666c94bed7c35f5ee66c92405485951.png)

<!--ENキャプチャ-->
<!--
![Image from Gyazo](https://t.gyazo.com/teams/diverta/151979d2599723fac774c789af006c17.png)
-->

インポートが完了すると、以下のように「サンプル保存」と「テスト」に分かれたフォルダ内に、各エンドポイントへのリクエスト情報が保存されます。

「サンプル保存」のフォルダで正式版のレスポンスを取得・保存し、「テスト」のフォルダでRC版のレスポンスを取得して正式版のレスポンスと比較しますので、
テスト実行対象から除外したいエンドポイントがある場合は、「テスト」フォルダから削除します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0d18c73f0756132b736cf57e96f9cf30.png)

<!--ENキャプチャ-->
<!--
![Image from Gyazo](https://t.gyazo.com/teams/diverta/b4bca1163f2742cf96db905245b529ab.png)
-->

詳細取得用のエンドポイント (details) の場合、ID/Slugの指定箇所が変数になっています。
以下のようにパス変数の箇所をテスト実行対象のIDに置き換えて、保存し直します。(サンプル保存のフォルダ、テストのフォルダの両方)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3622dc24316529cb9338a3463d508365.png)

<!--ENキャプチャ-->
<!--
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ad4c0a558d677540f28accf08eb4b1ce.png)
-->


テスト実行時に比較対象から無視したい項目がある場合は、テストファイルのエンドポイントを選択し、[スクリプト]タブの ignore_keysに対象の項目名 (APIレスポンスのキー) を追記し、保存ます。

例:

```
const ignore_keys = [
    "update_ymdhi",
    "ymd"
];
```

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c2ea9da755b67b3db36c6988633efe75.png)

<!--ENキャプチャ-->
<!--
![Image from Gyazo](https://t.gyazo.com/teams/diverta/57f54e2ee2b3814e63961d1a02129a03.png)
-->

### アクセストークンの保存
最後にAPIのアクセストークンを保存します。保存先としてPostman Vault(機密情報をローカル環境で管理するための領域)を利用します。

Postmanのフッターメニューから [Vault]を選択し、APIの静的アクセストークンを`RCMS_API_STATIC_TOKEN`として保存します。

:::note
`X-RCMS-API-ACCESS-TOKEN`ではないのでご注意ください。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/dca9b0bdbb143f7fdae88973201ad343.png)

<!--ENキャプチャ-->
<!--
![Image from Gyazo](https://t.gyazo.com/teams/diverta/edd9c616b8cefb10cfacf3da3695f46e.png)
-->

## テスト実行方法
### Kuroco正式版のサンプル保存
テスト実行対象のKurocoサイトを正式版に切り替えます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/03cd5565be777629bc81453674bd9f36.png)

Psotmanで、[サンプル保存] のフォルダを選択し[実行] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/206e3822a2e514924efa17488d963da0.png)

続けて、オレンジ色の実行ボタンをクリックし、サンプル保存リクエストを実行します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/3eb0e47d7421d5662a1eaeb994f63e73.png)

リクエストが実行され、200のレスポンスが返ってきていることを確認します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/568e757a84214d49d6529c80ca73355a.png)
 
実行完了後にコレクションの最上位のフォルダを選択し、[変数] タブを選択すると、先ほど取得したAPIレスポンスが変数内に保存されていることを確認できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/b44c119ad2bafcbcae18e16812edf4a2.png)

### KurocoRC版のサンプル保存
テスト実行対象のサイトをRC版に切り替えます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e09fdaa72af1b9c240123e8c84bcc6f7.png)

サンプル保存時と同様に、[テスト] フォルダを選択してリクエストを実行します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c93414f79c969dd5140611aaf83594ef.png)

実行完了後、結果を確認します。レスポンスに変化があった場合はFAILが、変化がなかった場合はPASSが出力されます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/89a02f9446a34b852f56361cfa6c2965.png)

<!--ENキャプチャ-->
<!--
![Image from Gyazo](https://t.gyazo.com/teams/diverta/4106a7f93069a84babd5ca3bc6969c95.png)
-->

FAILになった項目は正式版のレスポンスと比較します。  
今回の場合は画像に付く一時トークンの値が異なるためFAILになっていることが分かりました。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/94967cbd110eb1585f990dd76088bf1f.png)

Postmanを利用した正式版反映前のリグレッションテストの説明は以上になります。

## 関連ドキュメント
- [Kurocoのバージョン管理について](/ja/docs/update/roadmap-kuroco-version/)
- [静的アクセストークンによるAPIアクセス制限の方法](/ja/docs/tutorials/restricting-api-access-with-statictoken/)
- [API](/ja/docs/management/api-list/)
- [アップデートのスケジュールを教えてください](/ja/docs/faq/what-is-your-update-schedule-like/)


---

# OpenWeatherMapを利用して現在の天気を入力するAPIフィールドを設定する

> 元ページ: `tutorials/setting-up-api-field-for-current-weather-input-with-openweathermap` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/setting-up-api-field-for-current-weather-input-with-openweathermap/
> 概要: 本チュートリアルでは、APIフィールドの例として、OpenWeatherMapのWeather APIにリクエストを送り、選択した都市の現在の天気を入力できる拡張項目を設定します。

## 概要
Kurocoのコンテンツ定義で設定できるAPIフィールドでは、エンドポイントにリクエストを送り、そのレスポンスをコンテンツに登録することができます。  
エンドポイントはKurocoで作成したものでも、外部のものでも構いません。  

本チュートリアルでは、APIフィールドの例として、OpenWeatherMapのWeather APIにリクエストを送り、選択した都市の現在の天気を入力できる拡張項目を設定します。  

### 学べること
以下の手順でAPIフィールドを設定します。
- [OpenWeatherMapに登録する](#openweathermapに登録する)
- [マスタを登録する](#マスタを登録する)
- [APIを作成する](#apiを作成する)
- [コンテンツ定義を作成する](#コンテンツ定義を作成する)
- [動作の確認をする](#動作の確認をする)

### 前提条件
:::info
本チュートリアルでは天気情報の取得にOpenWeatherMapを使用します。  
サービスの詳細は[OpenWeatherMap](https://openweathermap.org/)を確認してください。
:::

## OpenWeatherMapに登録する

まずは[OpenWeatherMap](https://openweathermap.org/)にアクセスし、会員登録をします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/da4f20071ddba813fab7bcc8056b206f.jpg)

登録が完了したら[My API Keys](https://home.openweathermap.org/api_keys)にアクセスし、API keyを確認します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/22692b6ee38a2a453c48c61b481e3429.png)

## マスタを登録する
続いて、天気の情報を取得する都市とその緯度経度をマスタに登録します。  

[コンテンツ]->[マスタ]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/0b9562f89a784c1b7bc58ef86a28de58.png)

[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/6d3b166fbfa834a0b62daa2104899bd9.png)

CSVで更新を利用して天気情報を取得する選択肢となる都市とその緯度経度を登録します。  
今回は以下を登録しました。  

| city | lat | lon |
|:--|:--|:--|
| 東京 | 35.6894 | 139.6917  |
| クアラルンプール | 3.139 | 101.6868 |
| ニューヨーク | 40.7127 | -74.0059 |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/cfe8a815e75bc9f395976d639449cec4.png)

## APIを作成する
### APIフィールド用のAPI作成
Kuroco内部でのみ利用するエンドポイントはAPIを分けておくことをお勧めします。  
そこで、まずはAPIフィールドで利用するためのAPIを新規で作成します。  
既に追加済みの場合は次のステップに進んで構いません。  

#### APIの作成
Kuroco管理画面のAPIより「追加」をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/22c37e75a8244f384deb5b706d4979da.png)

API作成画面が表示されるので、下記入力し「追加する」をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/22d992c2dfbfceffed918a91e6d28f8a.png)

|項目|設定内容|
| :--- | :--- |
|タイトル|API field|
|版|1.0|
|ディスクリプション|APIフィールドで利用|

APIが作成されました。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/80707923e0e6b97831cb4939b9dba36e.png)

#### CORSの設定
次にCORSの設定をします。[CORSを設定する] をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e072fceea1d2954264a4e7fecdc091ad.png)

CORS_ALLOW_ORIGINSの [Add Origin] をクリックし、下記を追加します。

- 管理画面URL

CORS_ALLOW_METHODSの [Add Method] をクリックし、下記を追加します。

- GET  

CORS_ALLOW_CREDENTIALSの[Allow Credentials]にチェックが入っていることを確認します。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/5b8071c66d99aaa4519cd649b7cf284b.png)

問題なければ [保存する] をクリックします。 

### エンドポイントの作成
マスタに登録した都市データを取得するエンドポイントを作成します。  

[新しいエンドポイントの追加]をクリックします。  

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c8f53d98ae4c2f7cfe3181c16b4620b9.png)

以下の設定をします。  

|項目|設定内容|
| :--- | :--- |
|パス|get_city_master|
|カテゴリー|テーブル|
|モデル|Master|
|オペレーション|list|
|csvtable_id|利用するマスタID(2)|
|outputAs|objectを選択|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/2a1007462e2dd74b7f2e384cfe47bcc3.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6bd7723d9ab43cc15af03dccda0390aa.png)

設定ができたら[追加]をクリックしてエンドポイントを追加します。

## コンテンツ定義を作成する
### コンテンツ定義の作成
天気の自動入力を設定するコンテンツ定義を作成します。  

[コンテンツ定義]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/ccbcf6dbf64d984b7fb8d3290ee300ae.png)

[追加]をクリックします。  
![Image from Gyazo](https://t.gyazo.com/teams/diverta/5250008e6cced77b7f6f8c66e5b025fb.png)

以下の設定をします。  

**一般項目**

|項目|値|
|:--|:--|
|名前|OpenWeatherMap|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/c452484b663c95bde8d901980fc4ea17.png)

**追加項目**

|ID|項目名|項目設定|項目設定オプション|
|:--|:--|:--|:--|
|1|項目名:Weather<br/>識別子:weather|APIフィールド|以下の通り|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0ce4611bd0195e3be426ed4fe2b14b52.png)

**項目設定オプション**

|カラム|項目|値|
|:--|:--|:--|
|カラム#1|タイトル|都市|
||URL|`API_URL/rcms-api/4/get_city_master`|
||データ一覧パス|list|
||保存形式||
||表示形式|%city%|
||プレビュー URL||
|カラム#2|タイトル|天気|
||URL|`https://api.openweathermap.org/data/2.5/weather?lat=%lat%&lon=%lon%&appid={API key}&lang=ja`|
||データ一覧パス|weather|
||保存形式|%main%,%description%,%icon%|
||表示形式|%main% %description%|
||プレビュー URL|`https://openweathermap.org/img/wn/%icon%@2x.png`|

![Image from Gyazo](https://t.gyazo.com/teams/diverta/88ce1be36800abfd259152d215aff318.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/43cd6bb5f233b0ffd5c4cf0ec8a8be19.png)

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0df6c0935a04c6d228d7d82fd2c0115c.png)

:::caution
`API_URL`は自身のAPI URLに置き換えてください。  
`{API key}`は[OpenWeatherMapに登録する](#openweathermapに登録する)で確認したAPI keyに置き換えてください。
:::

設定ができたら[追加する]をクリックしてコンテンツ定義を追加します。

### APIフィールドの解説
APIフィールドの項目では、URLに設定したエンドポイントにGETリクエストを送り、レスポンスされたデータを一覧で表示します。  
データ一覧パスの項目にレスポンス内の利用するフィールド名を設定し、表示形式では`%key%`の形式でレスポンスのデータを利用して一覧で表示する内容を設定します。    
利用できるJSONレスポンスは以下のデータ構造になっている必要があります。  
```json
{
  "data":[
    {
    "key1":"value1,",
    "key2":"value2,"
    },
    {
    "key1":"value3,",
    "key2":"value4,"
    }
  ]
}
```
今回の例のカラム#1では以下のレスポンスが得られます。
```json
{
  "errors": [],
  "messages": [],
  "list": [
    {
      "city": "東京",
      "lat": "35.6894\t",
      "lon": "139.6917\t"
    },
    {
      "city": "クアラルンプール",
      "lat": "3.139\t",
      "lon": "101.6868\t"
    },
    {
      "city": "ニューヨーク",
      "lat": "40.7127\t",
      "lon": "-74.0059\t"
    }
  ]
}
```

:::info
レスポンスのデータ構造がAPIフィールドの求める構造と異なる場合や、GETリクエストのためにAPI keyをヘッダーに含める必要がある場合などは、Api::request_apiに設定したカスタム処理と{api}のSmartyプラグインを利用して、データの取得・整形をしてください。  
- [カスタム処理と紐づいたAPIエンドポイントを作成する](/ja/docs/tutorials/creating-a-custom-function-endpoint/)
- [Smartyプラグイン - api](/ja/docs/reference/smarty-plugin/#api)
:::

カラムを複数設定する場合、前のカラムのデータを`%key%`の形式で次のカラムのURL項目に利用できます。  
そのため、今回の例のカラム#2では`https://api.openweathermap.org/data/2.5/weather?lat=%lat%&lon=%lon%&appid={API key}&lang=ja`の記述でカラム#1で選択した都市の緯度経度をOpenWeatherMapのAPIに送り、天気の情報を得ています。

また、プレビューURLを設定するとプレビューのカラムで表示の確認ができます。  
こちらも`%key%`の形式でレスポンスの内容が利用できます。

:::info
プレビューURLに指定するURLはiframeでの表示を許可されている必要があります。
:::

最後に、[選択]をクリックした際にコンテンツに保存されるデータを、最終カラムの保存形式に設定します。  
`%key%`の形式でレスポンスの内容が利用できます。  

他の項目を含むAPIフィールドの説明は[コンテンツ定義で利用できる拡張項目一覧 - APIフィールド](/ja/docs/reference/list-of-extra-column-available-on-content/#apiフィールド)を参照してください。

## 動作の確認をする
追加したコンテンツ定義のコンテンツ編集画面でAPIフィールドの動作を確認します。  
うまく設定ができていれば以下のように選択した都市の現在の天気を入力できます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/44919934b9161ed72986b038dedbe0ba.gif)

## 関連ドキュメント
- [コンテンツ定義で利用できる拡張項目一覧](/ja/docs/reference/list-of-extra-column-available-on-content/)


---

# X（旧Twitter）と連携し、コンテンツ投稿時にXへ自動投稿する

> 元ページ: `tutorials/setting-up-twitter-integration` ｜ 公式ページ: https://kuroco.app/ja/docs/tutorials/setting-up-twitter-integration/
> 概要: KurocoではX（旧Twitter）と連携することで、コンテンツ投稿後にXへ自動投稿したり、APIを実行しXに投稿する等、X自動投稿機能が実装できます。

KurocoではX（旧Twitter）と連携することで、コンテンツ投稿後にXへ自動投稿したり、APIを実行しXに投稿する等、X自動投稿機能が実装できます。

本チュートリアルでは、KurocoとXの連携方法と、コンテンツ投稿時にXへ自動投稿する方法を記載します。

:::caution
X側の仕様変更により、本チュートリアルの手順や画面が実際と異なる場合があります。最新情報は[X Developer Platform](https://developer.x.com/)でご確認ください。
:::

:::caution
X APIは従量課金制（pay-per-use）です。ポスト作成は1件あたり$0.015（リンクを含む場合は$0.20）が課金されます。詳細は[X Developer Console](https://console.x.com/)で確認できます。  
Kurocoが使用するX API v2のエンドポイント（`POST /2/tweets`）を利用するには、*Pay-per-useプラン*が必要です。Freeプランではポストの投稿ができません。
:::

## Xの設定

### 1. Xアカウントを作成する
KurocoとXを連携する場合、Xアカウントを取得していることが前提となります。まだアカウントを持っていない場合は[X sign up](https://x.com/i/flow/signup)よりアカウント作成をお願いします。

:::info
Xへの登録方法は、[Xヘルプセンター](https://help.x.com/ja/using-x/create-x-account)をご確認ください。
:::

### 2. X Developer Consoleでアプリを作成する

[X Developer Console](https://console.x.com/)にアクセスし、Xアカウントでサインインします。
初回ログイン時、Developer AgreementおよびPolicyの同意や、利用目的などの基本情報の入力を施された場合は対応します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/98596f24a44bc67f633611fb86a13f56.png)

Developer Consoleのダッシュボードから、Pay-per-useプランのアプリを作成します。「アプリ in Pay per use」を選択し、[New App]（または[Create App]）をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/53f0fe02cf61d5953f8e69cf106c36ce.png)

:::caution
「アプリ in Free」では、Kurocoが使用するX API v2のポスト投稿エンドポイント（`POST /2/tweets`）にアクセスできません。
:::

環境は「Development」「Staging」「Production」から選択できます。本番運用では「Production」を選択してください。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/51ff9dd9268843208724ff889aa0a3b8.png)

[新しいクライアントアプリケーションを作成]をクリックしてアプリを作成します。

### 3. 認証情報を保存する

アプリが作成されると、以下の3つの認証情報が生成されます。

| 認証情報 | 説明 | Kurocoでの使用 |
| :--- | :--- | :--- |
| コンシューマーキー（Consumer Key） | アプリの識別に使用します。 | 使用する |
| Secret Key（Consumer Secret） | アプリの識別に使用します。 | 使用する |
| ベアラートークン（Bearer Token） | アプリ単位の認証（公開データの読み取り）に使用します。 | 使用しない |

コンシューマーキーとSecret Keyをコピーし、安全な場所に保存してください。

:::danger
認証情報は一度しか表示されません。紛失した場合は再生成が必要ですが、再生成すると以前の認証情報は無効になります。
:::

![Image from Gyazo](https://t.gyazo.com/teams/diverta/6684c975e4b06a6bc6217f43810b8623.png)

### 4. アプリの権限を設定する

Kurocoからポストを投稿するには、アプリの権限を「Read and write」に設定する必要があります。

Developer Consoleでアプリの設定画面を開き、Settingsを開きます。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0d64ec569c572619e57dd910ffbdd510.png)

「アプリの権限」で「読み取りと書き取り」を選択します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/ea74913347be58bf80bd6818605adc06.png)

| 権限レベル | 説明 |
| :--- | :--- |
| 読む | ポスト、ユーザー、公開データの閲覧のみ。投稿はできません。 |
| 読み取りと書き取り | Read onlyの権限に加えて、ポストの投稿・削除、フォロー/フォロー解除、いいね、リポストが可能です。 |
| 読み書きおよびダイレクトメッセージ | Read and writeの権限に加えて、ダイレクトメッセージの送受信が可能です。 |

コールバックURI （リダイレクトURL）とウェブサイトURLを設定し、[Save]をクリックします。

| 項目 | 記載例 | 説明 |
| --- | --- | --- |
| コールバックURI / リダイレクトURL | `https://example.com/twitter-to-kuroco` | OAuth認可後のコールバックURLを記入します。 |
| ウェブサイトURL | `https://example.com` | サイトURLを記入します。 |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/0603b73740f062db5d0df4d4ae785d13.png)

:::caution
権限を変更した場合、既存のAccess Tokenは新しい権限に対応しません。Kurocoとの連携後に権限を変更する場合は、アクセストークンとアクセストークンシークレットを再生成し、Kurocoに再設定する必要があります。
:::

### 5. Access Token and Secretを生成する

Developer Consoleでアプリの設定画面から[Keys and tokens]を開きます。
同じ[Keys and tokens]画面で、「アクセストークン」の[再生成]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/4849ab893c05389d44bb042a5faf5640.png)

アクセストークンとアクセストークンシークレットが生成されます。内容をコピーし、安全な場所に保存します。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/312c669e6dd79d7075e3805214c93b9e.png)

:::info
Access Tokenはアプリの所有者のXアカウントに紐づきます。投稿はこのアカウントから行われます。
:::

以上でX側の設定は完了です。

## Kurocoの設定

Kuroco管理画面より、[チャネル] -> [メッセージング] -> [X]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/50810a9881ea300c9d82a0ba954d3b02.png)

コピーした認証情報を記入し、[更新する]をクリックします。

X Developer Consoleの表記とKuroco管理画面の項目は以下のように対応しています。

| Kuroco管理画面の項目 | X Developer Consoleの表記 | 説明 |
| --- | --- | --- |
| 有効にする | — | チェックを入れます。 |
| API Key | コンシューマーキー | X Developer Consoleの「Consumer Key」を記入します。 |
| API Key Secret | コンシューマーキーシークレット | X Developer Consoleの「Consumer Secret」を記入します。 |
| Access Token | アクセストークン | X Developer Consoleの「Access Token」を記入します。 |
| Access Token Secret | アクセストークンシークレット | X Developer Consoleの「Access Token Secret」を記入します。 |

![Image from Gyazo](https://t.gyazo.com/teams/diverta/98c0df3075cfedf082cab85894f9fd0d.png)

Twitter Keyが登録されました。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/a251318b1ba2bd7f6660b4403de41ba7.png)

## 利用方法

### カスタム処理を使って自動投稿する

コンテンツの追加・更新をトリガーにXへ自動投稿するには、カスタム処理を使用します。

Kuroco管理画面より、[オペレーション] -> [カスタム処理]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/96f7457b084c67218e6f2f9ca9229d14.png)

カスタム処理一覧画面より[追加]をクリックします。

![Image from Gyazo](https://t.gyazo.com/teams/diverta/e8136ee37d0caa5c8337446b534671e9.png)

カスタム処理を下記設定にて作成します。

| 項目 | 記載例 |
| --- | --- |
|タイトル|X自動投稿|
|識別子|kuroco_to_twitter|
|トリガー|トリガー：コンテンツの追加後<br/>対象：コンテンツの追加後に投稿をしたいコンテンツ定義を選択|
|処理|下記ソースコードの内容を記載します。|

```php [実行内容]
{assign var=url value="`$smarty.const.ROOT_URL`/article/`$topicsData.slug`"}
{twitter_post_message var=res text="記事の更新をしました！`$url`"}
```
<a><img src="https://t.gyazo.com/teams/diverta/36e2dbc548836f3d4c27674f5a420cb2.png" style={{ width: 600, maxHeight: 'none' }} /></a>
<a><img src="https://t.gyazo.com/teams/diverta/b166f2b117569608cfa686a961e79671.png" style={{ width: 600, maxHeight: 'none' }} /></a>

入力後、[追加する]をクリックしカスタム処理を保存します。

:::info
カスタム処理で使用するSmartyプラグイン`{twitter_post_message}`の詳細は、[Smartyプラグインリファレンス](/ja/docs/reference/smarty-plugin/)をご確認ください。
:::

設定後、対象コンテンツ定義にコンテンツを投稿すると、カスタム処理で設定した内容がXにポストされます。

:::caution
X APIの従量課金により、テスト投稿にも料金が発生します。リンクを含むポストは1件あたり$0.20が課金されるため、テスト時はご注意ください。
:::

### メール送信でXに投稿する

X連携が有効な状態で、カスタム処理のメール送信先に `@tweets.twitter.r-cms.jp` 宛のアドレスを指定すると、メール本文の内容がXへのポストとして投稿されます。

既存のLINE（`@text.line.r-cms.jp`）やChatworkへのメール送信と同じ仕組みです。

#### 宛先フォーマット

```
<twitter_id>@tweets.twitter.r-cms.jp
```

`<twitter_id>` の部分には任意の識別子を指定します。投稿はサイトに設定されたX連携の認証情報（API Key / Access Token）を使用して行われます。

#### 設定例

カスタム処理のメール送信アクションで、宛先に `@tweets.twitter.r-cms.jp` を指定します。メール本文がそのままXへのポストとして投稿されます。

| 項目 | 設定値 |
| --- | --- |
| 宛先 | `<twitter_id>@tweets.twitter.r-cms.jp` |
| 本文 | Xに投稿したいテキスト |

## 関連ドキュメント
- [Twitter（管理画面マニュアル）](/ja/docs/management/twitter/)
- [Smartyプラグインリファレンス - twitter_post_message](/ja/docs/reference/smarty-plugin/)
