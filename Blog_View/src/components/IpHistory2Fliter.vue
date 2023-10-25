<template>
  <div>
    <el-dropdown
      trigger="click"
      placement="bottom"
      :hide-on-click="false"
      @visible-change="handleVisibleChange"
    >
      <!-- 下拉框头 -->
      <div :style="'height: 100%;cursor: pointer;color: ' + draw_title_color " class="hoverable el-dropdown-link" @click="gettypeDatas(scope.column.property)">
        <div style="display: inline;">
          {{scope.column.label}}
        </div>
        <i style="padding-left: 2px;font-weight:bolder; font-size: 15px;pointer-events: none;" class="el-icon-arrow-down"></i>
      </div>

      <!-- 下拉菜单 -->
      <el-dropdown-menu slot="dropdown" :style="'margin-left: 10px;width: '+ Width +';max-height: 200px; overflow-y: auto;'">

        <!-- 搜索框 -->
        <el-dropdown-item style="padding: 0 20px;margin: 0;">
          <input v-model="searchText" @input="debouncedSearch" placeholder="请输入内容" style="border: none;height: 18px;outline: none;font-size: 14px;color:#606266;">
        </el-dropdown-item>
        <!-- 等待加载ico -->
        <i v-if="typeDatas_loading" class="el-icon-loading" style="margin: 0 100px 0 100px;"></i>
        <!-- 下拉菜单子项 -->
        <div v-else>
          <el-dropdown-item v-for="typeData in typeDatas" :key="typeData.type" style="display: flex;">
            <el-checkbox
              v-model="typeData.checked"
              @change="handleSubmenuChange(typeData,scope.column.property)"
            />
            <div :style="'margin-left: 10px;width: ' + (parseInt(Width.slice(0, -2))-98).toString() + 'px' +';'">
              {{ typeData.type }}
            </div>
            <div style="float:right;color:#9499A0;">
              {{ typeData.count }}
            </div>
          </el-dropdown-item>
        </div>
      </el-dropdown-menu>

    </el-dropdown>
  </div>
</template>

<script>
import { api6, api8 } from '@/api/myapi'
import _ from 'lodash'

export default {
  // <slot></slot>里放组件渲染的东西
  props: {
    scope: Object,
    Width: { // 下拉筛选框宽度
      type: String, // 是否是父评论下的回复
      default: '218px'
    }
  },
  data () {
    return {
      tableData: [],
      // post /iphistory2/info 的 body
      searchModel: {
        PageNo: 1,
        PageSize: 5,
        datas: [] // 筛选motivate_item和motivate_item_name
      },
      total: 0,
      loading: true,
      typeDatas: [], // ip下拉框列表
      draw_title_color: '#909399;',
      searchModel_datas_ischange: false, // 子框是否被点击 从而决定要不要更新 现在输入搜索后也要更新
      searchText: '', // 下拉框过滤检索文本
      debouncedSearch: _.debounce(this.search, 500), // 延迟筛选
      typeDatas_loading: true // 下拉菜单是否加载状态
    }
  },
  methods: {
    // 当下拉菜单 显示 和 隐藏 时做一些事
    handleVisibleChange (visible) {
      if (visible) {
        // 显示时记录改变前状态
        console.log('下拉菜单已显示')
        this.searchModel_datas_ischange = false
      } else {
        console.log('下拉菜单已隐藏')
        // 如果筛选表变化 筛选传到总表 向后台更新刷新table
        if (this.searchModel_datas_ischange) {
          this.$store.state.fliters[this.scope.column.property] = this.searchModel.datas
          console.log(this.$store.state.fliters)
          // 判断数组不为空 就高亮小标题 注意！数组为空还是true 用.length代替
          if (this.searchModel.datas.length) {
            this.draw_title_color = 'rgba(28, 114, 225, 0.87);'
          } else {
            this.draw_title_color = '#909399;'
          }
          this.$emit('MyEvent', 'NeedUpdateDatas')
        }
      }
    },
    // 获取scope.column.property数据类型和数量
    gettypeDatas (ColumnStr) {
      // 只typeDatas为空获取
      if (this.typeDatas_loading) {
        api6(this, 'IpHistory2', ColumnStr).then(response => {
          this.typeDatas = response.data
          this.typeDatas_loading = false
        })
        this.typeDatas.forEach(typeData => {
          // 为每个对象添加一个 checked 属性，初始值为 false
          this.$set(typeData, 'checked', false)
        })
      }
    },
    // 子栏的框被 勾选 或 取消勾选 时触发
    handleSubmenuChange (TypeData, prop) {
      console.log('type:' + TypeData.type + ',stat:' + TypeData.checked)
      console.log(prop)
      this.searchModel_datas_ischange = true
      // 被勾选 searchModel.datas 增加筛选
      if (TypeData.checked) {
        this.searchModel.datas.push({
          motivate_item: prop,
          motivate_item_name: TypeData.type
        })
      } else {
        // 被取消勾选 searchModel.datas 删除筛选
        const index = this.searchModel.datas.findIndex(data => data.motivate_item ===
        prop && data.motivate_item_name === TypeData.type)
        if (index !== -1) {
          this.searchModel.datas.splice(index, 1)
        }
      }
    },
    // 向后端查询
    search () {
      // 在这里执行查询操作
      console.log(this.searchText)
      // 清空 遮拦 需更新
      this.searchModel.datas = []
      this.typeDatas_loading = true
      this.searchModel_datas_ischange = true
      api8(this, 'IpHistory2', this.scope.column.property, { filter_text: this.searchText }).then(response => {
        this.typeDatas = response.data
        this.typeDatas_loading = false
      })
      this.typeDatas.forEach(typeData => {
        // 为每个对象添加一个 checked 属性，初始值为 false
        this.$set(typeData, 'checked', false)
      })
    }
  },
  // 这个computed有点像守望者 有值变化就会更新 我要废弃这个了 改成向后端查询
  /*
  computed: {
    filteredTypeDatas () {
      if (this.searchText) {
        return this.typeDatas.filter(typeData => typeData.type.includes(this.searchText))
      } else {
        return this.typeDatas
      }
    }
  },
  */
  created () {
    // console.log(this.scope)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .hoverable:hover div{
  color:rgba(28, 114, 225, 0.87); /* 鼠标悬浮时的字体颜色 */
  }
</style>
