<template>
  <div name="comment_input" class="testcss">
      <el-input
      type="text"
      name="comm_name"
      placeholder="昵称(选填)"
      v-model="sendcomments.text"
      maxlength="10"
      show-word-limit
      style="width: 40% ;float: left;margin-bottom: 20px;"
      >
      </el-input>
      <div style="margin: 20px 0;"></div>
      <el-input
        type="textarea"
        name="comm_say"
        :placeholder="placeholder_text"
        v-model="sendcomments.textarea"
        maxlength="150"
        show-word-limit
        rows=4
      >
      </el-input>
      <el-button type="primary" :loading="sendcomments.loading" v-on:click="btnclick" style="margin:10px 0;float: left;"  >发送</el-button>
      <div style="clear: both;"></div>
      <div style="height:20px;"></div>
    </div>
</template>

<script>
import { api1, api7 } from '@/api/myapi'
import myrest from '@/utils/myrest'
export default {
  // <slot></slot>里放组件渲染的东西
  name: 'SendWin',
  props: {
    IsSub: {
      type: Boolean, // 是否是父评论下的回复
      default: false
    },
    comment_id: {
      type: Number, // 是父评论下的回复的话 传入父评论id
      default: -1
    },
    IsSubSub: {
      type: Boolean, // 是否是子评论下的回复
      default: false
    },
    SubSub_Rname: {
      type: String, // 要回复人的名字
      default: '?'
    }
  },
  data () {
    return {
      // 给后端的数据格式
      sendcomments: {
        text: '',
        textarea: '',
        loading: false
      },
      // 输入框文字
      placeholder_text: '在此输入内容'
    }
  },
  methods: {
    btnclick () {
      this.sendcomments.loading = true
      // this.$router.push({ path: this.redirect || '/about' })
      console.log('发送评论到后台')
      if (this.sendcomments.textarea.trim() === '') {
        myrest.err_win(this, '不能输入为空')
        this.sendcomments.loading = false
      } else {
        if (this.sendcomments.text.trim() === '') { this.sendcomments.text = '匿名B友' }
        // 不是子评论 添加到主评论表
        if (!this.IsSub) {
          api1(this, this.sendcomments).then(response => {
            if (response.status === 200) {
              myrest.suc_win(this, '发送成功')
              this.fuwei()
            } else {
              myrest.err_win(this, '发送失败了? TAT')
              this.fuwei()
            }
          })
        // 是子评论 添加到子评论表
        } else {
          // 如果是子子评论回复 加前缀
          if (this.IsSubSub) this.sendcomments.textarea = '回复 @' + this.SubSub_Rname + ' : ' + this.sendcomments.textarea
          api7(this, this.sendcomments, { modelname: 'SubComments', comment_id: this.comment_id }).then(response => {
            if (response.status === 200) {
              myrest.suc_win(this, '发送成功')
              this.fuwei()
            } else {
              myrest.err_win(this, '发送失败了? TAT')
              this.fuwei()
            }
          })
        }
      }
      this.sendcomments.textarea = '' // 清空对话框
      this.sendcomments.text = ''
    },
    fuwei () {
      this.sendcomments.loading = false // 复原发送
      setTimeout(() => window.location.reload(), 2000) // 重新加载评论
    }
  },
  mounted () {
    // 是子评论下的回复 加上回复前缀
    if (this.IsSubSub) {
      this.placeholder_text = '回复 @' + this.SubSub_Rname + ':'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.testcss{
  width: 85%;
  margin: 0 ;
  border-radius: 10px;
  min-width: 250px;
}
</style>
