// import { defineNuxtConfig } from 'nuxt/config'

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules: [
    '@vite-pwa/nuxt',
    '@nuxtjs/device',
    '@element-plus/nuxt',
    'nuxt-swiper',
  ],
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
    }
  },
  css: ['~/assets/css/main.scss'],
  vite: {
    css: {
      preprocessorOptions: {
        scss: {
          additionalData: '@use "sass:math"; @use "sass:string";'
        }
      }
    }
  },
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
  devtools: { enabled: true },
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
