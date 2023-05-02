const { resolve } = require('path');
import FullReload from 'vite-plugin-full-reload'

module.exports = {
  plugins: [
      FullReload(['../templates/**/*'])
  ],
  base: '/static/',
  server: {
    host: 'localhost',
    port: 3000,
    open: false,
    watch: {
      disableGlobbing: false,
    },
  },
  build: {
    manifest: true,
    rollupOptions: {
      input: {
        main: resolve('src/main.js'),
      },
    },
  },
};