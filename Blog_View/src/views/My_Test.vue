<template>
  <div>
    <el-table
      :data="tableData"
      :header-cell-style="{'text-align':'center'}"
      class="testcss"
      v-loading="loading">
      <el-table-column
        label="留言"
        :min-width="180">
          <comment
          slot-scope="scope"
          :scope=scope
          :amisub="false"
          :fatherid="scope.row.id"
          padding="22px"
        />
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

    <sendwinc
    />

  </div>
</template>

<script>
import { api5 } from '@/api/myapi'
import comment from '@/components/comment.vue'
import sendwinc from '@/components/SendwinC.vue'
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  components: {
    // HelloWorld
    comment,
    sendwinc
  },
  data () {
    return {
      tableData: [],
      searchModel: {
        PageNo: 1,
        PageSize: 5,
        datas: []
      },
      total: 0,
      loading: true
    }
  },
  //
  //
  //
  //
  methods: {
    handleSizeChange (val) {
      this.searchModel.PageSize = val
      console.log(`每页 ${val} 条`)
      this.get_comminfo()
    },
    handleCurrentChange (val) {
      this.searchModel.PageNo = val
      console.log(`当前页: ${val}`)
      this.get_comminfo()
    },
    get_comminfo () {
      console.log('获取后台评论')
      this.loading = true
      api5(this, this.searchModel, 'Comments').then(response => {
        this.total = response.data.total
        this.tableData = response.data.list
        this.loading = false
      })
    }
  },

  //
  //
  created () {
    // 获取评论
    this.get_comminfo()
  }
}
</script>

<style scoped>
.testcss{
  width: 85%;
  margin: 0 auto 0 auto;
  border-radius: 10px;
  min-width: 250px;
}
.block{
  margin-top: 60px;
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
    width: 95%;
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

  .row-bg {
    padding: 10px 0;
    background: #d3dce6;
  }

  .pbzero{
    padding-bottom: 0;
  }

</style>
