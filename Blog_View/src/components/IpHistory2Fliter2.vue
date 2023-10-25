<template>
  <div style="height: 50px;background-color: aqua;">
    {{ scope.row.name }}
  </div>
</template>

<script>

export default {
  // <slot></slot>里放组件渲染的东西

  props: {
    scope: Object
  },
  data () {
    return {

    }
  },
  methods: {
  },
  mounted () {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
