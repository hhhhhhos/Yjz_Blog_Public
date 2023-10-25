<template>
  <div>
    <netmusicC @MyEvent.once="omg=>testevent(omg)"/>
    <netmusicC @MyEvent="testevent"/>
    <netmusicC @MyEvent="testevent()"/>
    <div :class="p"></div>
    <button @click="change3()">button3</button>
    <el-collapse v-model="activeNames" @change="handleChange">
      <el-collapse-item name="2">
        <div>与现实生活一致：与现实生活的流程、逻辑保持一致，遵循用户习惯的语言和概念；</div>
      </el-collapse-item>
    </el-collapse>

     <el-table
      :data="tableData"
      style="width: 100%">
      <el-table-column
        label="日期"
        width="180">
            <div id="test" style="background-color: bisque;display: block;height: 300px;transition:all 0.3s;"></div>
            <button @click="change3()">button</button>
      </el-table-column>
      </el-table>
      <div  id="" style="height: myheight;background-color: aquamarine;transition:all 0.3s;">
    <b-button v-b-toggle="'collapse-2'" style="margin-top: 250px;">Toggle Collapse</b-button>
    <b-collapse id="collapse-2" >
      <b-card style="height: 800px;background-color: bisque;">I am collapsible content!</b-card>
    </b-collapse>
    </div>
    <!-- Element to collapse -->

    <div style="height: 1200px;">
    </div>
    <el-checkbox v-model="checked" @change="handleChange">Check me</el-checkbox>
    <el-table
    :data="tableData"
    style="width: 100%">
      <el-table-column
      label="留言"
        >
          <el-checkbox @change="handleChange">Check me</el-checkbox>
      </el-table-column>
    </el-table>
    <div v-for="typeData in typeDatas" :key="typeData.id">
      {{ typeData.id }}&nbsp;{{ typeData.data }}
    </div>
    <button @click="click()">click</button>

    <div v-for="typeData in typeDatas" :key="typeData.id" style="display: flex;">
      <el-checkbox
        @click="handleSubmenuChange(typeData.type)"
      />
      <div style="margin-left: 10px;width: 120px;">
        {{ typeData.id }}
      </div>
      <div style="float:right;color:#9499A0;">
        {{ typeData.data }}
      </div>
    </div>
    <el-dropdown
              trigger="click"
              placement="bottom"
              :hide-on-click="false"
            >
              <!-- 下拉框头 -->
              <div style="height: 100%;cursor: pointer;color: #909399;" class="hoverable el-dropdown-link" @click="gettypeDatas('ip_location')">
                <div style="display: inline;">
                  ip地点
                </div>
                <i style="padding-left: 2px;font-weight:bolder; font-size: 1px;pointer-events: none;" class="el-icon-arrow-down"></i>
              </div>

              <!-- 下拉菜单 -->
              <el-dropdown-menu slot="dropdown">
                <!-- 等待加载ico -->
                <i v-if="!typeDatas.length" class="el-icon-loading" style="margin: 0 20px 0 20px;"></i>
                <el-dropdown-item>
                  <el-input v-model="testdd" placeholder="请输入内容"></el-input>
                </el-dropdown-item>
                <el-dropdown-item v-for="typeData in typeDatas" :key="typeData.type" style="display: flex;">
                  <el-checkbox
                    v-model="checked"
                    @click.native="handleSubmenuChange(typeData.type)"
                  />
                  <div style="margin-left: 10px;width: 120px;">
                    {{ typeData.id }}
                  </div>
                  <div style="float:right;color:#9499A0;">
                    {{ typeData.data }}
                  </div>
                </el-dropdown-item>
              </el-dropdown-menu>

            </el-dropdown>
            {{ filteredTypeDatas }}
              <el-table
                :data="tableData"
                style="width: 100%">
                <el-table-column
                  label="日期"
                  width="180">
                    <IpHistory2Fliter2
                    slot-scope="scope"
                    :scope="scope"
                    />
                </el-table-column>
              </el-table>
              <input type="text" v-model="query" @input="debouncedSearch" />
              <i style="width:20px;padding-left: 2px;font-weight:bolder; font-size: 100px;pointer-events: none;" class="el-icon-arrow-down"></i>
</div>
</template>

<script>
import netmusicC from '@/components/netmusicC.vue'
import IpHistory2Fliter2 from '@/components/IpHistory2Fliter.vue'
import _ from 'lodash'
export default {
  // ...
  components: {
    netmusicC,
    IpHistory2Fliter2
  },
  data () {
    return {
      p: 'te',
      activeNames: 1,
      tableData: [{
        date: '2016-05-02',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-04',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1517 弄'
      }, {
        date: '2016-05-01',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1519 弄'
      }, {
        date: '2016-05-03',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1516 弄'
      }],
      myheight: '300px',
      checked: false,
      typeDatas: [
        {
          id: 'e', data: '3333'
        },
        {
          id: 'ee', data: '13333'
        }
      ],
      count: 1,
      testdd: '12333',
      keyvalue: { a: [1, 2, 3], b: [4, 5, 6] },
      query: '',
      debouncedSearch: _.debounce(this.search, 500)
    }
  },
  methods: {
    handleChange () {
      if (this.p === 'te') this.p = 'te2'
      else this.p = 'te'
      console.log(this.checked)
    },
    change2 () {
      // 将 emoji 转换为 Unicode 字符串
      const emoji = '😊'
      const unicodeStr = encodeURIComponent(emoji)
      console.log(unicodeStr) // 输出：%uD83D%uDE0A

      // 将 Unicode 字符串转换回 emoji
      const emojiAgain = decodeURIComponent(unicodeStr)
      console.log(emojiAgain) // 输出：😊
    },
    change3 () {
      console.log('123123')
      if (this.myheight === '0px') this.myheight = '300px'
      else this.myheight = '0px'
      sessionStorage.setItem('key', this.count++)
    },
    click () {
      this.typeDatas = []
    },
    testevent (str) {
      alert('father:' + str)
    },
    search () {
      // 在这里执行查询操作
      console.log('search:' + this.query)
    }
  },
  computed: {
    filteredTypeDatas () {
      console.log(this.count)
      return this.testdd + '我是computed'
    }
  },
  created () {
    console.log([].concat(...Object.values(this.keyvalue))) // 测试分支 //12312331
  }
}
</script>

<style scoped>
@import 'https://cdn.jsdelivr.net/npm/aplayer/dist/APlayer.min.css';
@keyframes my-animation {
  from { background-color: red; }
  to { background-color: yellow; }
}

.te {
  background-color: red;
  height: 300px;
}

.te2 {
  height: 300px;
  animation: my-animation 0.3s;
  animation-fill-mode: forwards;
}

</style>
