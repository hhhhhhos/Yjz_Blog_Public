<template>
  <div>
    <H
    msg="123123"
    />
    <div
      style="width: 80px;margin: 0 auto;background-color: aqua;position: absolute;left:500px;top:200px;"
      id="test"
      @mousedown="mousedown"
      draggable="false"
    >
      {{this.xchange}} &ensp;{{this.ychange}}
      <div style="background-color: aqua;"></div>
    </div>
  </div>
</template>

<style scoped>

</style>

<script>
import H from '../components/HelloWorld.vue'
export default {
  components: {
    H
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
        this.xchange = dom.style.left // 实时传给显示数字 /////
        this.ychange = dom.style.top
      }
    }
  },
  mounted () {
    window.addEventListener('mousemove', this.mousemove) // 刚挂载？生命周期钩子 全局事件监听器 监听mousemove事件 触发this.mousemove方法
    window.addEventListener('mouseup', this.mouseup)
  },
  beforeDestroy () {
    window.removeEventListener('mousemove', this.mousemove) // 离开销毁 不销毁会咋样
    window.removeEventListener('mouseup', this.mouseup)
  }
}
</script>
