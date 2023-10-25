<template>
  <div :style="'display: flex;padding: ' + padding + ' 0 5px 0;'">

    <!-- 头像 .电脑显示-->
    <div v-if="this.$store.state.show_desktop" class="destop" style="position: absolute;">
      <el-avatar size="large" :src="require('../assets/404.webp')" fit="fill"></el-avatar>
    </div>

    <!-- 头像 .手机显示-->
    <div v-else class="mobile" style="position: absolute;">
      <el-avatar size="large" :src="require('../assets/404.webp')" fit="fill"></el-avatar>
    </div>

    <!-- 评论框 -->
    <div style="width: 100%;">

      <!-- 父评论框 -->
      <div style="margin-left: 50px;">
        <!-- 用户名 .父评论-->
        <div v-if="!amisub || !this.$store.state.show_desktop" style="font-size: 13px;color: #61666D;margin: 0 0 4px;">
            {{ scope.row.name }}
      </div>

        <!-- 用户名 .子评论-->
        <div v-else style="float:left;font-size: 13px;color: #61666D;margin: 0 16px 4px 0;padding: 0;">
            {{ scope.row.name }}
        </div>

        <!-- 日期 ip属地 .手机显示-->
        <div v-if="!this.$store.state.show_desktop" class="mobile" style="font-size:11px;color: #9499A0;padding-right: 16px;margin-top: -5px;">
          <!-- 暂时不用{{ (scope.row.date).replace('T', ' ').substring(0,16) }}-->
          {{ formatDate_mobile(scope.row.datetime) }}&nbsp;&nbsp;IP属地:&nbsp;{{ formatString_mobile(scope.row.ip_location) }}
        </div>

        <!-- 评论内容 -->
        <div style="font-size:15px;color: #18191C;margin: 12px 0 4px;">
          <i v-if="scope.row.is_top" class="top-icon">置顶</i>{{ scope.row.info }}
        </div>

        <!-- 日期 点赞 回复 下拉查看子评论 .电脑显示-->
        <div v-if="this.$store.state.show_desktop" class="destop" style="font-size:13px;color: #9499A0;">
          <!-- 暂时不用{{ (scope.row.date).replace('T', ' ').substring(0,16) }} 这里不指定width和0mar 0pad b-collaspe就会高度计算错误 原因未知 后来发现是el-table-column的min-width设置了180 导致超过这个大小后 b-collaspe就会高度错误 自动计算多一行？ 原因未知 -->
            {{ formatDate(scope.row.datetime) }}
          <svg id="svg1" style="display:block;margin:4px 4px 0 25px;cursor: pointer;" t="1636093575017" class="icon hoverable2" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3323" width="14px" height="14px">
            <path d="M594.176 151.168a34.048 34.048 0 0 0-29.184 10.816c-11.264 13.184-15.872 24.064-21.504 40.064l-1.92 5.632c-5.632 16.128-12.8 36.864-27.648 63.232-25.408 44.928-50.304 74.432-86.208 97.024-23.04 14.528-43.648 26.368-65.024 32.576v419.648a4569.408 4569.408 0 0 0 339.072-4.672c38.72-2.048 72-21.12 88.96-52.032 21.504-39.36 47.168-95.744 63.552-163.008a782.72 782.72 0 0 0 22.528-163.008c0.448-16.832-13.44-32.256-35.328-32.256h-197.312a32 32 0 0 1-28.608-46.336l0.192-0.32 0.64-1.344 2.56-5.504c2.112-4.8 5.12-11.776 8.32-20.16 6.592-17.088 13.568-39.04 16.768-60.416 4.992-33.344 3.776-60.16-9.344-84.992-14.08-26.688-30.016-33.728-40.512-34.944zM691.84 341.12h149.568c52.736 0 100.864 40.192 99.328 98.048a845.888 845.888 0 0 1-24.32 176.384 742.336 742.336 0 0 1-69.632 178.56c-29.184 53.44-84.48 82.304-141.76 85.248-55.68 2.88-138.304 5.952-235.712 5.952-96 0-183.552-3.008-244.672-5.76-66.432-3.136-123.392-51.392-131.008-119.872a1380.672 1380.672 0 0 1-0.768-296.704c7.68-72.768 70.4-121.792 140.032-121.792h97.728c13.76 0 28.16-5.504 62.976-27.456 24.064-15.104 42.432-35.2 64.512-74.24 11.904-21.184 17.408-36.928 22.912-52.8l2.048-5.888c6.656-18.88 14.4-38.4 33.28-60.416a97.984 97.984 0 0 1 85.12-32.768c35.264 4.096 67.776 26.88 89.792 68.608 22.208 42.176 21.888 84.864 16 124.352a342.464 342.464 0 0 1-15.424 60.544z m-393.216 477.248V405.184H232.96c-40.448 0-72.448 27.712-76.352 64.512a1318.912 1318.912 0 0 0 0.64 282.88c3.904 34.752 32.96 61.248 70.4 62.976 20.8 0.96 44.8 1.92 71.04 2.816z" p-id="3324" fill="#9499a0">
            </path>
          </svg>
          <svg id="svg2" style="display:none;margin:4px 4px 0 25px;cursor: pointer;" t="1636093991833" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4447" width="14px" height="14px">
            <path d="M860.032 341.12h-182.08c7.488-17.408 14.72-38.528 18.048-60.544 5.952-39.872 4.992-87.36-18.368-129.088-21.76-38.848-50.304-60.928-83.52-61.376-30.72-0.384-53.888 18.176-65.728 33.408a199.296 199.296 0 0 0-32.064 59.264l-1.92 5.184c-5.44 14.976-10.88 29.952-23.04 51.456-19.712 34.816-48.832 56.128-77.696 74.368a391.936 391.936 0 0 1-30.976 17.92v552.448a4621.952 4621.952 0 0 0 351.872-5.312c51.264-2.752 100.672-28.544 127.488-76.032 24.32-43.136 55.168-108.16 74.368-187.264 20.416-84.16 24.64-152.704 24.576-195.968-0.128-46.336-38.72-78.4-80.96-78.4z m-561.344 541.312V341.12H215.808c-59.712 0-113.408 42.048-120.896 104.32a1376 1376 0 0 0 0.64 330.368c7.36 58.688 56.128 100.032 113.024 102.848 25.024 1.28 55.552 2.56 90.112 3.712z" p-id="4448" fill="#00aeec">
            </path>
          </svg>
          {{ scope.row.love_num }}
          <!-- 回复 -->
          <div class="hoverable" style="display:block;margin:0 0 0 25px;padding: 0;width:30px;cursor: pointer;">
            <div v-b-toggle="'collapse-sendcomm-' + scope.row.id + amisub">
              回复
            </div>
          </div>

          <!-- 下拉查看n条评论 （子评论不显示）-->
          <div v-if="!amisub" style="display: inline-block;margin:0 0 0 25px;padding: 0;width: 150px;">
            <div :id="'open-' + scope.row.id" v-if="scope.row.sub_num && !amisub" v-b-toggle="'collapse-' + scope.row.id" @click="getsubbyid(scope.row.id)" style="display: inline;cursor: pointer;">
              <div class="hoverable">
                下拉查看{{scope.row.sub_num}}条评论
                <i style="padding-left: 2px;" class="el-icon-arrow-down"></i>
              </div>
            </div>
          </div>

        </div>

        <!-- 点赞 回复 下拉查看子评论 .手机显示-->
        <div v-else class="mobile" style="font-size:13px;color: #9499A0;padding-right: 16px;">

          <svg id="svg1" style="display:block;margin:4px 4px 0 0;cursor: pointer;" t="1636093575017" class="icon hoverable2" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3323" width="14px" height="14px">
            <path d="M594.176 151.168a34.048 34.048 0 0 0-29.184 10.816c-11.264 13.184-15.872 24.064-21.504 40.064l-1.92 5.632c-5.632 16.128-12.8 36.864-27.648 63.232-25.408 44.928-50.304 74.432-86.208 97.024-23.04 14.528-43.648 26.368-65.024 32.576v419.648a4569.408 4569.408 0 0 0 339.072-4.672c38.72-2.048 72-21.12 88.96-52.032 21.504-39.36 47.168-95.744 63.552-163.008a782.72 782.72 0 0 0 22.528-163.008c0.448-16.832-13.44-32.256-35.328-32.256h-197.312a32 32 0 0 1-28.608-46.336l0.192-0.32 0.64-1.344 2.56-5.504c2.112-4.8 5.12-11.776 8.32-20.16 6.592-17.088 13.568-39.04 16.768-60.416 4.992-33.344 3.776-60.16-9.344-84.992-14.08-26.688-30.016-33.728-40.512-34.944zM691.84 341.12h149.568c52.736 0 100.864 40.192 99.328 98.048a845.888 845.888 0 0 1-24.32 176.384 742.336 742.336 0 0 1-69.632 178.56c-29.184 53.44-84.48 82.304-141.76 85.248-55.68 2.88-138.304 5.952-235.712 5.952-96 0-183.552-3.008-244.672-5.76-66.432-3.136-123.392-51.392-131.008-119.872a1380.672 1380.672 0 0 1-0.768-296.704c7.68-72.768 70.4-121.792 140.032-121.792h97.728c13.76 0 28.16-5.504 62.976-27.456 24.064-15.104 42.432-35.2 64.512-74.24 11.904-21.184 17.408-36.928 22.912-52.8l2.048-5.888c6.656-18.88 14.4-38.4 33.28-60.416a97.984 97.984 0 0 1 85.12-32.768c35.264 4.096 67.776 26.88 89.792 68.608 22.208 42.176 21.888 84.864 16 124.352a342.464 342.464 0 0 1-15.424 60.544z m-393.216 477.248V405.184H232.96c-40.448 0-72.448 27.712-76.352 64.512a1318.912 1318.912 0 0 0 0.64 282.88c3.904 34.752 32.96 61.248 70.4 62.976 20.8 0.96 44.8 1.92 71.04 2.816z" p-id="3324" fill="#9499a0">
            </path>
          </svg>
          <svg id="svg2" style="display:none;margin:4px 4px 0 0;cursor: pointer;" t="1636093991833" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4447" width="14px" height="14px">
            <path d="M860.032 341.12h-182.08c7.488-17.408 14.72-38.528 18.048-60.544 5.952-39.872 4.992-87.36-18.368-129.088-21.76-38.848-50.304-60.928-83.52-61.376-30.72-0.384-53.888 18.176-65.728 33.408a199.296 199.296 0 0 0-32.064 59.264l-1.92 5.184c-5.44 14.976-10.88 29.952-23.04 51.456-19.712 34.816-48.832 56.128-77.696 74.368a391.936 391.936 0 0 1-30.976 17.92v552.448a4621.952 4621.952 0 0 0 351.872-5.312c51.264-2.752 100.672-28.544 127.488-76.032 24.32-43.136 55.168-108.16 74.368-187.264 20.416-84.16 24.64-152.704 24.576-195.968-0.128-46.336-38.72-78.4-80.96-78.4z m-561.344 541.312V341.12H215.808c-59.712 0-113.408 42.048-120.896 104.32a1376 1376 0 0 0 0.64 330.368c7.36 58.688 56.128 100.032 113.024 102.848 25.024 1.28 55.552 2.56 90.112 3.712z" p-id="4448" fill="#00aeec">
            </path>
          </svg>
          {{ scope.row.love_num }}
          <div style="margin:1px 20px 0 20px;cursor: pointer;">
            <div v-b-toggle="'collapse-sendcomm-' + scope.row.id + amisub">
              <i class="el-icon-chat-square hoverable3" ></i>
            </div>
          </div>

          <!-- 下拉查看n条评论 （子评论不显示）-->
          <div style="display: inline-block;margin: 0;padding: 0;width: 150px;">
            <div :id="'open-' + scope.row.id" v-if="scope.row.sub_num && !amisub" v-b-toggle="'collapse-' + scope.row.id" @click="getsubbyid(scope.row.id)" style="display: inline;cursor: pointer;">
              <div class="hoverable" >
                下拉查看{{scope.row.sub_num}}条评论
                <i style="padding-left: 2px;" class="el-icon-arrow-down"></i>
              </div>
            </div>
          </div>

        </div>

        <!-- 回复展开 -->
        <b-collapse :id="'collapse-sendcomm-' + scope.row.id + amisub" class="mt-2" accordion="my-accordion" >
          <b-card style="height: 100%;border: none;">
            <sendwinc
            v-if="!amisub"
            :IsSub="true"
            :IsSubSub="amisub"
            :SubSub_Rname="scope.row.name"
            :comment_id="fatherid"
            />
            <sendwinc
            v-else
            :IsSub="true"
            :IsSubSub="amisub"
            :SubSub_Rname="scope.row.name"
            :comment_id="fatherid"
            style="padding-right: 20px;"
            />
          </b-card>
        </b-collapse>

      </div>

      <!-- 子评论框 -->
      <div style="margin-left: 20px;">

        <!-- 子评论展开 （没子评论不渲染）&&（子评论不渲染）.电脑显示-->
        <b-collapse v-if="!amisub && scope.row.sub_num && this.$store.state.show_desktop" :id="'collapse-' + scope.row.id" class="m-1 collapse-loading" >
          <b-card v-loading="this.subloading" style="height: 100%;border: none;">
            <p class="card-text" style="">
              <el-table
                :data="subData"
                style="width: 100%;">
                <el-table-column
                :min-width="450"
                style="margin: 0 0 0 0;">
                <CoM
                  slot-scope="scope"
                  :scope=scope
                  :amisub="true"
                  :fatherid="fatherid"
                />
                </el-table-column>
              </el-table>
            </p>

            <!-- 分页 -->
            <el-pagination
              small
              layout="prev, pager, next"
              @current-change="handleCurrentChange"
              :page-size="searchModel.PageSize"
              :current-page="searchModel.PageNo"
              :total="subtotal"
              style="display: inline-block;"
              :hide-on-single-page="true"
              >
            </el-pagination>

            <!-- 上拉收起 -->
            <div v-b-toggle="'collapse-' + scope.row.id" @click="getsubbyid(scope.row.id)" style="float: right;margin-right: 80px;font-size:13px;color: #9499A0;margin-top: 5px;">
                <div class="hoverable">上拉收起评论<i style="padding-left: 2px;" class="el-icon-arrow-up"></i></div>
            </div>
          </b-card>
        </b-collapse>

        <!-- 子评论展开 （没子评论不渲染）&&（子评论不渲染）.手机显示-->
        <b-collapse v-if="!amisub && scope.row.sub_num && !this.$store.state.show_desktop" :id="'collapse-' + scope.row.id" class="m-1 collapse-loading" >
          <b-card v-loading="this.subloading" style="height: 100%;border: none;">
            <p class="card-text" style="">
              <el-table
                :data="subData"
                style="width: 100%;">
                <el-table-column
                :min-width="270"
                style="margin: 0 0 0 0;">
                <CoM
                  slot-scope="scope"
                  :scope=scope
                  :amisub="true"
                  :fatherid="fatherid"
                />
                </el-table-column>
              </el-table>
            </p>

            <!-- 分页 -->
            <el-pagination
              small
              layout="prev, pager, next"
              @current-change="handleCurrentChange"
              :page-size="searchModel.PageSize"
              :current-page="searchModel.PageNo"
              :total="subtotal"
              style="display: inline-block;"
              :hide-on-single-page="true"
              >
            </el-pagination>

            <!-- 上拉收起 -->
            <div v-b-toggle="'collapse-' + scope.row.id" @click="getsubbyid(scope.row.id)" style="float: right;font-size:13px;color: #9499A0;margin-top: 5px;">
                <div class="hoverable">上拉收起评论<i style="padding-left: 2px;" class="el-icon-arrow-up"></i></div>
            </div>

          </b-card>
        </b-collapse>

      </div>

    </div>
  </div>
</template>

<script>
import { api4 } from '@/api/myapi'
import moment from 'moment'
import sendwinc from '@/components/SendwinC.vue'

export default {
  name: 'CoM',
  components: {
    sendwinc
  },
  props: {
    scope: Object,
    amisub: Boolean, // 判断自己是否是子评论
    fatherid: Number, // 父评论id
    padding: {
      type: String, // 测试 用来绑定评论上内边距
      default: '8px'
    }
  },
  data () {
    return {
      subloading: false, // 子评论是否在加载
      subData: [], // 子评论数据
      subtotal: 0, // 子评论总数
      searchModel: { // 子评论分页
        PageNo: 1,
        PageSize: 4,
        comment_id: 0 // 子评论外键 父评论id
      },
      subData_test: [
        {
          name: '匿名B友',
          ip_location: '新加坡.',
          info: '213',
          love_num: null,
          ip: '139.59.252.137',
          id: 9001,
          date: '2023-09-23T13:33:54',
          saw_num: null
        },
        {
          name: '匿名B友',
          ip_location: 'Unknow',
          info: '333',
          love_num: null,
          ip: 'Unknow',
          id: 9002,
          date: '2023-09-23T10:55:40',
          saw_num: null
        }],
      is_pagination_need: false // 是否是分页需要获取子评论数据
    }
  },
  methods: {
    getsubbyid (id) {
      console.log('测试' + id)
      const dom = document.getElementById('open-' + id)
      if (this.is_pagination_need) {
        this.getsub(id) // 向后端获取子评论
        this.is_pagination_need = false
        return
      }
      if (dom.style.display === 'inline') {
        dom.style.display = 'none'
        this.getsub(id) // 向后端获取子评论
      } else dom.style.display = 'inline'
    },
    getsub (id) {
      // 如果加载过了 且不是分页要求获取 直接返回
      if (this.subData.length && !this.is_pagination_need) {
        this.is_pagination_need = false
        return
      }
      console.log('获取评论的子评论')
      this.subloading = true
      this.searchModel.comment_id = id
      api4(this, this.searchModel).then(response => {
        this.subtotal = response.data.subcomments_total
        this.subData = response.data.subcomments_list
        this.subloading = response.data.loading
      })
    },
    formatDate (date) {
      if (!date) return '未知' // 防空报错
      const now = moment()
      const inputDate = moment(date)

      const diffInSeconds = now.diff(inputDate, 'seconds')
      const diffInMinutes = now.diff(inputDate, 'minutes')
      const diffInHours = now.diff(inputDate, 'hours')
      const diffInDays = now.diff(inputDate, 'days')

      if (diffInSeconds < 60) {
        return `${diffInSeconds}秒前`
      } else if (diffInMinutes < 60) {
        return `${diffInMinutes}分钟前`
      } else if (diffInHours < 24) {
        return `${diffInHours}小时前`
      } else if (diffInDays < 3) {
        return `${diffInDays}天前`
      } else {
        return inputDate.format('YYYY-M-D HH:mm')
      }
    },
    formatDate_mobile (date) {
      if (!date) return '未知'
      const now = moment()
      const inputDate = moment(date)

      const diffInSeconds = now.diff(inputDate, 'seconds')
      const diffInMinutes = now.diff(inputDate, 'minutes')
      const diffInHours = now.diff(inputDate, 'hours')
      const diffInDays = now.diff(inputDate, 'days')

      if (diffInSeconds < 60) {
        return `${diffInSeconds}秒前`
      } else if (diffInMinutes < 60) {
        return `${diffInMinutes}分钟前`
      } else if (diffInHours < 24) {
        return `${diffInHours}小时前`
      } else if (diffInDays < 3) {
        return `${diffInDays}天前`
      } else {
        return inputDate.format('M月D日')
      }
    },
    formatString_mobile (str) {
      if (!str) return '未知'
      const parts = str.split('.')
      const result = parts.length > 1 && parts[1].trim() !== '' ? parts[1] : parts[0]
      return result.length > 7 ? result.substring(0, 76) : result
    },
    handleCurrentChange (val) {
      this.searchModel.PageNo = val
      this.is_pagination_need = true // 我子评论要翻页
      this.getsubbyid(this.fatherid)
    }

  },
  mounted () {
    this.$store.state.count++
    console.log('count:' + this.$store.state.count + '  id:' + this.scope.row.id)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
    padding-top: 5px;
    padding-left: 5px;
    text-align: left;
  }
  .hoverable:hover {
  color:rgba(28, 114, 225, 0.87); /* 鼠标悬浮时的字体颜色 */
  }

  .hoverable2:hover path {
    fill: rgba(28, 114, 225, 0.87); /* 鼠标悬浮时的颜色 */
  }

  .hoverable3:hover {
    color:rgba(28, 114, 225, 0.87);
  }

  .myclass{
    padding-top: 20px;
    padding-bottom: 10px;
    padding-left: 10px;
    padding-right: 20px;
    text-align: left;

  }
  .myclass2{
    float: right;
    padding-right: 10px;
  }
  .card-text .is-leaf{
  display: none;
  }
  .card-text .el-table_2_column_2 {
    border-right: none;
}
.card-body{
  padding-left: 0;
  padding-right: 0;
  padding-top: 0px;
}
.child-right > * {
  margin:0 6px;
}

.destop{
  display:flex;
}
.mobile{
  display:flex;
}

 .top-icon {
  top: -2px;
  display: inline-flex;
  justify-content: center;
  align-items: center;
  position: relative;
  width: 30px;
  height: 18px;
  border: 1px solid #ff6699;
  border-radius: 3px;
  margin-right: 5px;
  font-size: 12px;
  color: #ff6699;
  font-style: normal; /* 添加这一行 */
}

</style>
