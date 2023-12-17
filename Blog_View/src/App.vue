<template>
  <div id="app">
      <el-menu
      :default-active="this.$store.state.global_route"
      class="el-menu-demo"
      mode="horizontal"
      router
      :style="menuc"
      @select="handleSelect">
          <el-menu-item index="/" style="height: 48px;line-height: 50px;"><i class="myicon el-icon-s-home"></i>首页</el-menu-item>
          <el-menu-item index="/comm" style="height: 48px;line-height: 50px;"><i class="myicon el-icon-edit"></i>留言</el-menu-item>
          <el-menu-item index="/visitors" style="height: 48px;line-height: 50px;"><i class="myicon el-icon-user"></i>访客</el-menu-item>
          <el-menu-item index="/about2" style="height: 48px;line-height: 50px;"><i class="myicon el-icon-s-fold"></i>其他</el-menu-item>
      </el-menu>
      <div class="line" style="height: 40px;"></div>
      <router-view style="" />

      <div style="height: 100px;background-color: rgb(245, 248, 250);border-top: 1px solid #e1e8ed ;">
        <div class="hr" style="margin-top: 50px;margin-bottom: 5px;width: 12%;border: 1px solid #e1e8ed;"></div>
        <div style="margin-top: 5px;color: #bdc2c6;font-size: small;">Copyright © 2023&ensp;&ensp; YJZ'S BLOG</div>
      </div>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.el-textarea__inner {
    font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;

}

.menucss{
  margin-bottom: 20px;
  height: 49px;
  position: fixed;
  top: 0;
  z-index: 1000;
  background-color:rgb(255, 255, 255);
  width: 100%;
}

.menucss2{
  margin-bottom: 20px;
  height: 49px;
  position: fixed;
  top: 0;
  z-index: 1000;
  background-color:white;
  width: 100%;
}
.myicon {
  font-size: 12px;
  padding-right: 5px;
}
.hr{
  display: block;
  unicode-bidi: isolate;
  margin-block-start: 0.5em;
  margin-block-end: 0.5em;
  margin-inline-start: auto;
  margin-inline-end: auto;
  overflow: hidden;
  border-style: inset;
  border-width: 1px;
}
html{
  background-color: rgb(245, 248, 250);
}

.el-table tbody tr:hover>td {
  background-color:unset !important
}
</style>

<script>

export default {
  data () {
    return {
      menuc: 'margin-bottom: 20px;height: 49px;position: fixed;top: 0;z-index: 1000;background-color:rgb(255, 255, 255);width: 100%;'
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
      this.activeIndex = keyPath
      console.log(this.$route.path)
    },
    // 监听窗口大小变化 变化就触发
    handleResize () {
      this.$store.state.windowWidth = window.innerWidth
      if (this.$store.state.windowWidth < 600) {
        // 当窗口宽度小于600px时，更改某个值
        // ...
        this.$store.state.show_desktop = false
        // console.log('小于六百')
      } else {
        // console.log('大于六百')
        this.$store.state.show_desktop = true
      }
      // console.log(this.$store.state.handleResize)
    }
  },
  mounted () {
    console.log(this.$router)
    console.log(this.$route)
    console.log(this.$store.state.count)
    console.log(this.$route.path)

    window.addEventListener('resize', this.handleResize) // 监听窗口变化 触发this.handleResize
    this.handleResize()
  },
  destroyed () {
    window.removeEventListener('resize', this.handleResize)
  }
}
</script>
