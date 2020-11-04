module.exports = {
  "pages": {
    'index': {
      entry: './src/pages/Home/main.js',
      template: 'public/index.html',
      filename: 'index.html',
      title: 'Home',
      chunks: [ 'chunk-vendors', 'chunk-common', 'index' ]
    },
    'search': {
      entry: './src/pages/Search/main.js',
      template: 'public/index.html',
      filename: 'search.html',
      title: 'Search Products',
      chunks: [ 'chunk-vendors', 'chunk-common', 'search' ]
    },
    'productdetail': {
      entry: './src/pages/ProductDetail/main.js',
      template: 'public/index.html',
      filename: 'productdetail.html',
      title: 'Product Detail',
      chunks: [ 'chunk-vendors', 'chunk-common', 'productdetail' ]
    }
  },
  "transpileDependencies": [
    "vuetify"
  ]
}