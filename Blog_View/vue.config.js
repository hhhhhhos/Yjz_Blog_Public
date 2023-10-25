const { defineConfig } = require('@vue/cli-service')

// 解决Loading chunk {n} failed错误尝试
const Timestamp = new Date().getTime() // 当前时间为了防止打包缓存不刷新，所以给每个js文件都加一个时间戳

module.exports = defineConfig({
  publicPath: '/',
  transpileDependencies: true,
  // 解决Uncaught runtime errors:报错
  devServer: {
    client: {
      overlay: false
    },
    // 自己加的跨域尝试 可以用在开发环境 生产环境 nginx反代
    proxy: 'http://localhost:8001'
  },

  // 解决Loading chunk {n} failed错误尝试
  filenameHashing: true, // 建议开启 防止静态资源(图片)替换后 未即时生效
  configureWebpack: {
    output: { // 输出重构  打包编译后的 文件路径  文件名称  【时间戳】
      filename: `./static/js/[name].${Timestamp}.js?v=${Timestamp}`,
      chunkFilename: `./static/js/[name].${Timestamp}.js?v=${Timestamp}`
    }
  }
})
