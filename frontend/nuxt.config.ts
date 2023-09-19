import { defineNuxtConfig } from 'nuxt/config'

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules: [
    '@vite-pwa/nuxt',
    '@nuxtjs/device',
    '@element-plus/nuxt',
    'nuxt-swiper',
    '@pinia/nuxt',
    '@pinia-plugin-persistedstate/nuxt',
  ],
  routeRules: {
    '/index': {redirect: '/welcome'},
  },
  swiper: {
    // modules: ['pagination']
  },
  // elementPlus: { /** Options */ },
  app: {
    pageTransition: {
      name: 'blur',
      mode: 'out-in'
    },
    layoutTransition: {
      name: 'pageup',
      mode: "out-in"
    },
    head: {
      link: [
        {
          rel: "stylesheet",
          href: "https://fonts.googleapis.com/css?family=Roboto:300,400,500,700,900&display=swap",
        },
      ],
    }
  },
  css: ['~/assets/css/main.scss', 'animate.css/animate.min.css'],
  vite: {
    // server: {
    //   hmr: {
    //     protocol: "ws",
    //     clientPort: 24678,
    //     port: 24678
    //   },
    //   watch: {
    //     usePolling: true,
    //   }
    // },
    css: {
      preprocessorOptions: {
        scss: {
          additionalData: '@use "sass:math"; @use "sass:string"; '
        }
      }
    }
  },
  // pinia: {
  //   autoImports: [
  //     // automatically imports `defineStore`
  //     'defineStore', // import { defineStore } from 'pinia'
  //   ],
  // },
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
  devtools: { enabled: false },
  pages: true,
  pwa: {
    // workbox: {
    //   navigateFallback: "/login"
    // },
    devOptions: {
        enabled: true,
        type: "module"
    },
    manifest: {
      name: "FABRIC-pwa",
      short_name: "FABRIC",
      description: "pwa practice of FABRIC application",
      theme_color: "#ffffff",
      icons: [
          {
              src: '/pwa-icons/pwa-64x64.png',
              sizes: '64x64',
              type: 'image/png'
          },
          {
              src: '/pwa-icons/pwa-144x144.png',
              sizes: '144x144',
              type: 'image/png'
          },
          {
              src: '/pwa-icons/pwa-192x192.png',
              sizes: '192x192',
              type: 'image/png'
          },
          {
              src: '/pwa-icons/pwa-512x512.png',
              sizes: '512x512',
              type: 'image/png'
          },
      ]
    }
  }

})
