import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import nightwatchPlugin from 'vite-plugin-nightwatch'
import vueJsx from '@vitejs/plugin-vue-jsx'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    nightwatchPlugin(),
    vueJsx() // Добавляем плагин парсера Vue для поддержки JSX
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
   esbuild: {
    // Установите загрузчик '.js' на '.jsx'
    loader: {
       '.js': 'jsx'
    }
  }
})