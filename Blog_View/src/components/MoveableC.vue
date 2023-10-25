<template>
  <div>
    <div
      style="border-radius: 3px;margin: 0 auto;background-color: #dee2e5;position:fixed;left:20px;top:200px;z-index: 9999; border: 1px solid #e1e8ed;/* 这会确保音乐播放器总是在其他内容之上 */"
      id="test"
      @mousedown="mousedown"
      @touchstart="mousedown"
      >
      <div style="height: 10px;"></div>
      <slot>
        <!-- 里面放组件标签里渲染的东西 slot可以实现 -->
      </slot>
    </div>
  </div>
</template>

<script>
export default {
  // <slot></slot>里放组件渲染的东西
  // {{this.xchange}} &ensp;{{this.ychange}}
  props: {
  },
  data () {
    return {
      xchange: 0, // 仅用来展示数字 好了解目前属性的x值
      ychange: 0, // 仅用来展示数字 好了解目前属性的y值
      ismousedown: false, // 只有鼠标在div按下 @mousemove才往下执行
      recx: 0, // 计算窗口和鼠标的x轴差值
      recy: 0 // 计算窗口和鼠标的y轴差值
    }
  },
  methods: {
    mousedown (e) {
      this.ismousedown = true
      // 算鼠标和窗口的差值
      const dom = document.getElementById('test')
      this.recx = dom.getBoundingClientRect().left - e.clientX
      this.recy = dom.getBoundingClientRect().top - e.clientY
    },
    mouseup () {
      this.ismousedown = false
    },
    mousemove (e) {
      if (this.ismousedown) {
        const dom = document.getElementById('test') // test不能放css里 只能放html的style=""才能读取
        dom.style.left = e.clientX + this.recx + 'px' // 给div的left赋值
        dom.style.top = e.clientY + this.recy + 'px'
        // console.log(dom.getBoundingClientRect().left)
        this.xchange = dom.style.left // 实时传给显示数字
        this.ychange = dom.style.top
      }
    }
  },
  mounted () {
    window.addEventListener('mousemove', this.mousemove) // 刚挂载？生命周期钩子 全局事件监听器 监听mousemove事件 触发this.mousemove方法
    window.addEventListener('mouseup', this.mouseup)
    // 兼容ipad ios触屏
    window.addEventListener('touchmove', this.mousemove)
    window.addEventListener('touchend', this.mouseup)
  },
  beforeDestroy () {
    window.removeEventListener('mousemove', this.mousemove) // 离开销毁 不销毁会咋样
    window.removeEventListener('mouseup', this.mouseup)
    window.removeEventListener('touchmove', this.mousemove) // 离开销毁 不销毁会咋样
    window.removeEventListener('touchend', this.mouseup)
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
