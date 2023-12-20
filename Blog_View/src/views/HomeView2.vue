<template>
  <div style="padding: 20px ;background-color:rgba(242,243,245);display: flex;justify-content: center;">
    <div style="width: 1000px;">
      <div class="infinite-list-wrapper" style="overflow:auto">
        <ul
          class="list"
          v-infinite-scroll="load"
          infinite-scroll-disabled="disabled"
          style="padding: 0;">
          <li v-for="i in count" class="list-item" :key="i" style="margin: 10px;">
            <div v-if="i==1" style="color: var(--bs-gray-600);">
              广告位招租
            </div>
            <div v-else>
              {{ i }}
            </div>
          </li>
        </ul>
        <div>
          <p v-if="loading" style="margin: 32px 0 16px 0;color: #909399;">加载中</p>
          <p v-if="noMore" style="margin: 32px 0 16px 0;color: #909399;">没有更多了</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      count: 10,
      loading: false
    }
  },
  computed: {
    noMore () {
      return this.count >= 20
    },
    disabled () {
      return this.loading || this.noMore
    }
  },
  methods: {
    load () {
      this.loading = true
      setTimeout(() => {
        this.count += 2
        this.loading = false
      }, 2000)
    },
    // webapi获取用户设备
    getDeviceType () {
      const ua = navigator.userAgent
      if (/(tablet|ipad|playbook|silk)|(android(?!.*mobi))/i.test(ua)) {
        return 'tablet'
      }
      if (/Mobile|iP(hone|od)|Android|BlackBerry|IEMobile|Kindle|Silk-Accelerated|(hpw|web)OS|Opera M(obi|ini)/.test(ua)) {
        return 'mobile'
      }
      return 'desktop'
    }
  }
}
</script>

<style scoped>
.list-item {
  display: flex;
  border-radius: 5px; /* 所有四个角都是 10px 的圆角 */
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  height: 200px;
  background-color: white;
}
.list-item:hover {
  background-color: rgb(247,248,250);
}
</style>
