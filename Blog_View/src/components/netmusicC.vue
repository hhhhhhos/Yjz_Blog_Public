<template>
  <div>
    <button @click=testfunc()>我是按钮测试我的事件</button>
  </div>
</template>

<script>
export default {
  props: {
    id: String,
    type: String
  },
  methods: {
    testfunc () {
      this.$emit('MyEvent', '我是傻逼')
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
