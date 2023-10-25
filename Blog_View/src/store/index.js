import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    count: 1,
    global_route: '',
    windowWidth: 0, // 全局变量 监听窗口大小 移动端适配
    window_height: 0,
    show_desktop: true, // 是否按电脑显示
    fliters: {} // IpHistory2总筛选 格式为{'ip':[1,2,3],'ip2':[4,5,6]}
  },
  getters: {
  },
  mutations: {
    increment (state) {
      // 变更状态
      state.count++
    }
  },
  actions: {
  },
  modules: {
  }
})
