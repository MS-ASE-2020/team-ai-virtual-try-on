module.exports = {
  "pages": {
    'index': {
      entry: './src/pages/Home/main.js',
      template: 'public/index.html',
      filename: 'index.html',
      title: 'Home',
      chunks: [ 'chunk-vendors', 'chunk-common', 'index' ]
    },
    // 'search': {
    //   entry: './src/pages/Search/main.js',
    //   template: 'public/index.html',
    //   title: 'About',
    //   chunks: [ 'chunk-vendors', 'chunk-common', 'about' ]
    // }
  },
  "transpileDependencies": [
    "vuetify"
  ]
}