<template>
  <div style="margin-top: 48px;padding: 15px;">
    <div style="border:1px solid #ccc;width: 800px;height: 300px;">
      <WangEditor
      ref="child"
      />
    </div>
    <button @click=funcblog()>send</button>
    <div v-html="res_data"></div>
  </div>
</template>

<script>
import WangEditor from '@/components/Wang_Editor.vue'
import { api9 } from '@/api/myapi'
import myrest from '@/utils/myrest'

export default {
  components: {
    WangEditor
  },
  data () {
    return {
      res_data: null
    }
  },
  //
  //
  //
  //
  methods: {
    funcblog () {
      api9(this, { content: this.$refs.child.html }).then(response => {
        if (response.status === 200) {
          myrest.suc_win(this, '发送成功')
          this.res_data = response.data
        } else {
          myrest.err_win(this, '发送失败了? TAT')
        }
      })
    }
  },

  //
  //
  created () {

  }
}
</script>

<style scoped>

</style>
