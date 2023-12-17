<!-- eslint-disable vue/no-unused-vars -->
<template>
  <div style="margin-top: 48px;">
    <el-table
      :data="tableData"
      style="width: 100%;margin-top: -30px;"
      v-loading="loading"
      >
      <el-table-column
        prop="datetime"
        label="访问时间"
        width="170">
        <IpHistory2Fliter
        slot="header"
        slot-scope="scope"
        :scope="scope"
        Width="280px"
        @MyEvent="get_comminfo"/>
        <div slot-scope="scope">{{ scope.row.datetime.replace('T', ' ') }}</div>
      </el-table-column>
      <el-table-column
        prop="ip"
        label="访客ip"
        width="150">
        <IpHistory2Fliter
        slot="header"
        slot-scope="scope"
        :scope="scope"
        @MyEvent="get_comminfo"/>
      </el-table-column>
      <el-table-column
        prop="ip_location"
        label="ip地点"
        width="150">
        <IpHistory2Fliter
        slot="header"
        slot-scope="scope"
        :scope="scope"
        @MyEvent="get_comminfo"/>
      </el-table-column>
      <el-table-column
        prop="browser_name"
        label="浏览器名称"
        width="80">
        <IpHistory2Fliter
        slot="header"
        slot-scope="scope"
        :scope="scope"
        @MyEvent="get_comminfo"/>
      </el-table-column>
      <el-table-column
        prop="browser_version"
        label="浏览器版本"
        width="80">
        <IpHistory2Fliter
        slot="header"
        slot-scope="scope"
        :scope="scope"
        @MyEvent="get_comminfo"/>
      </el-table-column>
      <el-table-column
        prop="os_name"
        label="操作系统名称"
        width="80">
        <IpHistory2Fliter
        slot="header"
        slot-scope="scope"
        :scope="scope"
        @MyEvent="get_comminfo"/>
      </el-table-column>
      <el-table-column
        prop="os_version"
        label="操作系统版本"
        width="80">
        <IpHistory2Fliter
        slot="header"
        slot-scope="scope"
        :scope="scope"
        @MyEvent="get_comminfo"/>
      </el-table-column>
      <el-table-column
        prop="device_name"
        label="设备名称"
        width="80">
        <IpHistory2Fliter
        slot="header"
        slot-scope="scope"
        :scope="scope"
        @MyEvent="get_comminfo"/>
      </el-table-column>
      <el-table-column
        prop="device_brand"
        label="设备版本"
        width="80">
        <IpHistory2Fliter
        slot="header"
        slot-scope="scope"
        :scope="scope"
        @MyEvent="get_comminfo"/>
      </el-table-column>
      <el-table-column
        prop="is_bot"
        label="是否为爬虫器"
        width="80">
        <IpHistory2Fliter
        slot="header"
        slot-scope="scope"
        :scope="scope"
        @MyEvent="get_comminfo"/>
        <div slot-scope="scope">{{ scope.row.is_bot ? '是' : '否' }}</div>
      </el-table-column>
      <el-table-column
        prop="unicode"
        label="访客标识"
        width="250"
        >
        <IpHistory2Fliter
        slot="header"
        slot-scope="scope"
        :scope="scope"
        Width="327px"
        @MyEvent="get_comminfo"/>
      </el-table-column>
      <el-table-column
        prop="request_method"
        label="访问方法"
        width="95">
        <IpHistory2Fliter
        slot="header"
        slot-scope="scope"
        :scope="scope"
        @MyEvent="get_comminfo"/>
        <template slot-scope="scope">
          <el-tag
            style="margin-left: 5px;"
            :type="scope.row.request_method === 'GET' ? 'primary' :
            scope.row.request_method === 'POST' ? 'success' :
            scope.row.request_method === 'PUT' ? 'warning' :
            scope.row.request_method === 'DELETE' ? 'info' : 'danger'"
            disable-transitions>{{scope.row.request_method}}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column
        prop="request_url"
        label="访问url"
        width="250"
        >
        <IpHistory2Fliter
        slot="header"
        slot-scope="scope"
        :scope="scope"
        Width="327px"
        @MyEvent="get_comminfo"/>
      </el-table-column>
    </el-table>
    <div class="block">
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="searchModel.PageNo"
        :page-sizes="[5, 10, 15, 20]"
        :page-size="searchModel.PageSize"
        layout="total, sizes, prev, pager, next, jumper"
        :total= 'total'
        >
      </el-pagination>
    </div>
    <el-pagination
      small
      layout="prev, pager, next"
      @current-change="handleCurrentChange"
      :page-size="searchModel.PageSize"
      :current-page="searchModel.PageNo"
      :total="total"
      class="block2">
    </el-pagination>
  </div>
</template>

<script>
import { api5 } from '@/api/myapi'
// import myrest from '@/utils/myrest'
import IpHistory2Fliter from '@/components/IpHistory2Fliter.vue'
export default {
  components: {
    IpHistory2Fliter
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
      total: 0, // 分页返回总数量
      loading: true // el-table的loading
    }
  },
  //
  //
  methods: {
    handleSizeChange (val) {
      this.searchModel.PageSize = val
      // console.log(`每页 ${val} 条`)
      this.get_comminfo()
    },
    handleCurrentChange (val) {
      this.searchModel.PageNo = val
      // console.log(`当前页: ${val}`)
      this.get_comminfo()
    },
    // 获取后台ip访问记录 参数为子组件emit的 是否需要更新datas
    get_comminfo (NeedUpdateDatas) {
      console.log('获取后台ip访问记录')
      this.loading = true
      // 如果要更新 this.$store.state.fliters拆开 合并到datas
      if (NeedUpdateDatas) this.searchModel.datas = [].concat(...Object.values(this.$store.state.fliters))
      api5(this, this.searchModel, 'IpHistory2').then(response => {
        this.total = response.data.total
        this.tableData = response.data.list
        this.loading = false
      })
    }
  },
  //
  //
  created () {
    // 获取访问记录
    this.get_comminfo()
  }
}
</script>

<style scoped>
.testcss{
  width: 75%;
  margin: 0 auto;
  border-radius: 10px;
  min-width: 250px;
}
.block{
  margin-top: 20px;
  margin-bottom: 20px;
}
.block2{
  margin-top: 10px;
  display: none;
}
@media screen and (max-width: 750px){
  .block{
  display: none;
  }
  .block2{
  display:block;
  }
  .testcss{
    width: 85%;
  }
}
</style>

<style scoped>
  .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }

  .grid-content {
    border-radius: 4px;
    min-height: 36px;
    padding-top: 5px;
    padding-left: 5px;
    text-align: left;
  }
  .row-bg {
    padding: 10px 0;
    background: #d3dce6;
  }
  .myclass{
    padding-top: 20px;
    padding-bottom: 10px;
    padding-left: 20px;
    padding-right: 20px;
    text-align: left;
  }
  .myclass2{
    float: right;
    padding-right: 10px;
  }
  .pbzero{
    padding-bottom: 0;
  }
  .hoverable:hover div{
  color:rgba(28, 114, 225, 0.87); /* 鼠标悬浮时的字体颜色 */
  }

</style>
