// const CompressionPlugin = require('compression-webpack-plugin')

module.exports = {
  productionSourceMap: false,
  pages: {
    'index': {
      entry: './src/pages/Home/main.js',
      template: 'public/index.html',
      filename: 'index.html',
      title: 'Virtual Try-On',
    },
    'search': {
      entry: './src/pages/Search/main.js',
      template: 'public/index.html',
      filename: 'search.html',
      title: 'Search',
    },
    'productdetail': {
      entry: './src/pages/ProductDetail/main.js',
      template: 'public/index.html',
      filename: 'productdetail.html',
      title: 'Product Detail',
    },
    'customerinfo': {
      entry: './src/pages/CustomerInfo/main.js',
      template: 'public/index.html',
      filename: 'customerinfo.html',
      title: 'Customer Info',
    },
    'salerinfo': {
      entry: './src/pages/SalerInfo/main.js',
      template: 'public/index.html',
      filename: 'salerinfo.html',
      title: 'Saler Info',
    }
  },
  transpileDependencies: [
    "vuetify"
  ],
  configureWebpack: {
    // externals: {
    //   "vue": 'Vue',
    // },
    // plugins: [
    //   new CompressionPlugin({
    //     algorithm: 'gzip',
    //     test: /\.(js|css)$/,// 匹配文件名
    //     threshold: 10240, // 对超过10k的数据压缩
    //     deleteOriginalAssets: true, // 不删除源文件
    //     minRatio: 0.8 // 压缩比
    //   })
    // ]
  },
}

