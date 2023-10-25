import Vue from 'vue'
import App from './App.vue'
import store from './store'// 写前面 router全局守卫才能设置全局变量
import router from './router'

// 自己加的
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
// ---------

Vue.config.productionTip = false
// 自己加的
Vue.use(ElementUI)
Vue.use(BootstrapVue) // 可选择安装 BootstrapVue 图标组件插件
Vue.use(IconsPlugin)
// ---------

new Vue({
  router,
  store,
  // 自己加的
  el: '#app',
  // ---------
  render: h => h(App)
}).$mount('#app')
