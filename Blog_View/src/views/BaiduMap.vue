<template>
  <!-- 主页面 -->
  <div style="background-color:rgba(242,243,245);padding:0 45px 25px 45px;">
    <!-- 操作面板 -->
    <div style="padding: 45px 85px 25px 0;min-width: 600px;">
      <div class="myitem" style="display: block;">
        <div style="color: #1F2F3D;font-weight:bold ;">链家爬虫可视化作业</div>
        <div style="display: flex;">爬取城市:<el-input style="max-width: 200px;height: 5px;margin-left: 15px;" v-model="input1" placeholder="(选填) 默认广州"></el-input></div>
        <div style="display: flex;">爬取价格:
          <el-checkbox-group style="margin-left: 15px;" v-model="checkboxGroup2" size="medium" @change="limitToOne">
            <el-checkbox-button v-for="city in cities" :label="city" :key="city">{{city}}</el-checkbox-button>
          </el-checkbox-group>
        </div>
        <div style="display: flex;">爬取页数:<el-input-number size="small" style="max-width: 200px;height: 5px;margin: 10px 15px;" v-model="num" :min="1" :max="3" label="描述文字"></el-input-number><el-button :disabled=button1_isdisable @click="buildsocket" type="primary" style="height: 32px;margin: 10px 0 0 10px;padding: 0 20px;">确认</el-button></div>
        <!-- 返回结果面板 -->
        <div class="myitem2">
          <div class="myitem3">
            <div v-for="consoledata in consoledatas" :key="consoledata.id">
              {{consoledata.info}}
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- 地图面板 -->
    <div style="display: flex;">
      <!-- 地图 -->
      <baidu-map ref="myMap" style="min-width: 1000px;border-radius: 5px;border: 5px solid #ffffff;box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);" class="map" :center="this.centerpoint" :zoom=13 :scroll-wheel-zoom="true">
        <!-- 杂七杂八控件 -->
        <bm-scale anchor="BMAP_ANCHOR_TOP_RIGHT"></bm-scale>
        <bm-control style="display: flex;">
          <el-switch
            v-model="showmode"
            active-text="按总租金显示图标"
            inactive-text="按平方租金显示图标"
            style="margin: 5px 0 0 90px;padding: 12px 16px;background-color: #ffffff;" class="myborder">
          </el-switch>
          <div v-if="!showmode" style="display:flex;margin: 5px 0 0 10px;height: 32px;background-color: #ffffff;" class="myborder">
            <img :src="require('../assets/locb.svg')" style="margin: 0 0 0 0 ;width:20px;">
            <div>>&nbsp;200</div>
            <img :src="require('../assets/locr.svg')" style="margin: 0 0 0 15px ;width:20px;">
            <div>>&nbsp;100</div>
            <img :src="require('../assets/locblue.svg')" style="margin: 0 0 0 15px ;width:20px;">
            <div>>&nbsp;50</div>
            <img :src="require('../assets/locg.svg')" style="margin: 0 0 0 15px ;width:20px;">
            <div>>&nbsp;20</div>
            <img :src="require('../assets/locw.svg')" style="margin: 0 0 0 15px ;width:20px;">
            <div>>&nbsp;0</div>
          </div>
          <div v-else style="display:flex;margin: 5px 0 0 10px;height: 32px;background-color: #ffffff;" class="myborder">
            <img :src="require('../assets/locb.svg')" style="margin: 0 0 0 0 ;width:20px;">
            <div>>&nbsp;10000</div>
            <img :src="require('../assets/locr.svg')" style="margin: 0 0 0 15px ;width:20px;">
            <div>>&nbsp;5000</div>
            <img :src="require('../assets/locblue.svg')" style="margin: 0 0 0 15px ;width:20px;">
            <div>>&nbsp;2500</div>
            <img :src="require('../assets/locg.svg')" style="margin: 0 0 0 15px ;width:20px;">
            <div>>&nbsp;500</div>
            <img :src="require('../assets/locw.svg')" style="margin: 0 0 0 15px ;width:20px;">
            <div>>&nbsp;0</div>
          </div>
        </bm-control>
        <bm-navigation anchor="BMAP_ANCHOR_TOP_RIGHT"></bm-navigation>
        <bm-map-type :map-types="['BMAP_NORMAL_MAP', 'BMAP_HYBRID_MAP']" anchor="BMAP_ANCHOR_TOP_LEFT"></bm-map-type>
        <!-- 红点 -->
        <div v-for="Data in Datas" :key="Data.index">
          <BaiduMapDot :Data="Data" :showmode="showmode" ref="child"/>
        </div>
      </baidu-map>
      <!-- 历史记录 -->
      <div class="myborder" style="margin-left:  5px;width: 300px;height: 600px;">
        <!-- 历史记录标题 -->
        <div class="myborder" style="color: var(--textcolor1);padding: 4px 0;background-color: #ffffff;">历史记录&nbsp;&nbsp;&nbsp;</div>
        <!-- 模拟数据 -->
        <div class="myborder" style="margin: 5px 0 0 0;height: 540px;overflow-y: auto;background-color: #ffffff;">
          <div v-for="(Data, index) in sortDatas" :key="Data.index" style="display: flex;cursor: pointer;" @click="test(Data)" class="myhover">
            <div style="flex-grow: 1;text-align: left;">{{index+1}}.{{Data.小区[0]}}</div>
            <div style="text-align: right;">{{Data.价格}}</div>
          </div>
          <div style="color: var(--bs-gray-500);">没有更多了...</div>
        </div>
      </div>
    </div>
    <!-- echarts面板 -->
    <div id="main" style="margin: 10px 85px 0 0;height:400px;background-color: #ffffff;" class="myborder"></div>
  </div>
</template>

<style scoped>
.myhover{
  color: var(--bs-gray-700);
}
.myhover:hover{
  color: var(--bs-gray-400);
}
.myborder {
  border-radius: 5px;
  border: 5px solid #ffffff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
}
.map {
  width: 100%;
  height: 600px;
}
::v-deep .el-input__inner{
  height: 32px;
}

.myitem{
  text-align:left;
  line-height: 45px;
  border-radius: 5px; /* 所有四个角都是 10px 的圆角 */
  padding: 35px 45px 35px 45px;
  background-color:rgb(255, 255, 255);
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
}

.myitem2{
  margin: 20px 0 0 0;
  display: block;
  text-align:left;
  line-height: 45px;
  border-radius: 5px; /* 所有四个角都是 10px 的圆角 */
  padding: 10px;
  height: 200px;
  background-color:rgb(255, 255, 255);
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
}

.myitem3{
  display: block;
  color: white;
  height: 180px;
  text-align:left;
  line-height: 30px;
  padding: 10px 20px;
  background-color:rgba(0, 0, 0, 0.729);
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
  overflow-y: scroll; /* 总是添加滚动条 */
}

:root {
  --textcolor1: #2c3e50;
  --bgcolor1: #F5F8FA;
}
</style>

<script>
import BaiduMapDot from '@/components/BaiduMapDot.vue'
import Pinyin from 'pinyin'
import pinyin2 from 'js-pinyin'
import * as echarts from 'echarts'
const cityOptions = ['默认', '最贵', '最低']
pinyin2.setOptions({ checkPolyphone: false, charCase: 1 })

export default {
  components: {
    BaiduMapDot
  },
  data () {
    return {
      // #region 爬取类型变量
      centerpoint: '广州',
      checkboxGroup2: ['默认'],
      cities: cityOptions,
      // #endregion
      showmode: true,
      websocket: null,
      show: false,
      infostyle: false,
      input1: '',
      num: 1, // 爬取页数
      button1_isdisable: false,
      consoledata_id: 0,
      consoledatas: [
        {
          id: this.consoledata_id,
          info: '...'
        }
      ],
      Datas: [],
      sortDatas: [],
      // 下面是控制台滚动脚本参数
      scrollFlag: true,
      oldScrollTop: 0,
      // echarts
      myChart: null,
      resizeTimeout: null
    }
  },
  methods: {
    // #region 下面是土著功能
    // echarts 地图移动到坐标
    test2 (e, index) {
      console.log()
      this.$refs.child[index].infoWindowOpen()
      this.centerpoint = { lng: e[0], lat: e[1] }
    },
    // 点击右边侧栏 地图移动到组件坐标
    test (e) {
      console.log()
      this.$refs.child[e.index].infoWindowOpen()
      this.centerpoint = { lng: e.坐标[0], lat: e.坐标[1] }
    },
    // 右边侧栏数据排序
    sortDatasFunc () {
      if (this.checkboxGroup2[0] !== '最低') {
        const sortedDatas = this.Datas.slice()
        // 高到低
        return sortedDatas.sort((a, b) => b.价格 - a.价格)
      } else {
        const sortedDatas = this.Datas.slice()
        return sortedDatas.sort((a, b) => a.价格 - b.价格)
      }
    },
    // 爬虫模式限选一个
    limitToOne () {
      if (this.checkboxGroup2.length > 1) {
        this.checkboxGroup2 = this.checkboxGroup2.slice(-1)
      }
    },
    // 当前年月日方法
    get_myDatetime () {
      const now = new Date()
      const year = now.getFullYear() // 获取完整的年份 (4位,1970-????)
      let month = now.getMonth() + 1 // 获取当前月份 (0-11,0代表1月)
      let day = now.getDate() // 获取当前日 (1-31)
      let hour = now.getHours() // 获取当前小时数 (0-23)
      let minute = now.getMinutes() // 获取当前分钟数 (0-59)
      let second = now.getSeconds() // 获取当前秒数 (0-59)

      // 如果月份、日期、小时、分钟或秒的值小于10，前面加上0
      month = month < 10 ? '0' + month : month
      day = day < 10 ? '0' + day : day
      hour = hour < 10 ? '0' + hour : hour
      minute = minute < 10 ? '0' + minute : minute
      second = second < 10 ? '0' + second : second

      return year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':' + second
    },
    infoWindowClose () {
      this.show = false
    },
    infoWindowOpen () {
      this.show = true
    },
    // 悬浮在红点时显示的文字
    infoshow () {
      this.infostyle = true
    },
    infohide () {
      this.infostyle = false
    },
    // 城市转首字母 有bug！不行啊
    getInitials (city) {
      const py = Pinyin(city, {
        style: Pinyin.STYLE_INITIALS,
        heteronym: false
      })
      console.log(py)
      let res = ''
      for (const c of py) {
        res += c[0][0]
      }
      return res
    },
    // #endregion
    // #region 下面是控制台（滚动）功能
    myconsole (str) {
      this.consoledata_id++
      this.consoledatas.push({ id: this.consoledata_id.toString(), info: `[${Date().toString().slice(0, 24)}]:${str}` })
      if (this.scrollFlag) {
        // 如果user没向上滚 就自动跳转最低（有新消息时）
        this.scrollToBottom()
      }
    },
    scrollToBottom () {
      this.$nextTick(() => {
        const container = this.$el.querySelector('.myitem3')
        container.scrollTop = container.scrollHeight
      })
    },
    scrolling () {
      const scrollTop = document.querySelector('.myitem3').scrollTop
      const scrollStep = scrollTop - this.oldScrollTop
      this.oldScrollTop = scrollTop
      if (scrollStep < 0) {
        this.scrollFlag = false
      } else {
        this.scrollFlag = true
      }
    },
    // #endregion
    // #region 下面是socket方法
    // 点击button1后触发
    buildsocket () {
      this.button1_isdisable = true
      // 创建socket链接
      this.setupWebSocket()
    },
    // 初始化socket链接
    setupWebSocket () {
      this.websocket = new WebSocket('ws://localhost:8001/ws') // 创建WebSocket连接
      this.websocket.onopen = this.onWebSocketOpen // WebSocket连接打开时的处理函数
      this.websocket.onerror = this.onWebSocketError //
      this.websocket.onmessage = this.onWebSocketMessage // 收到WebSocket消息时的处理函数
      this.websocket.onclose = this.onWebSocketClose // WebSocket连接关闭时的处理函数
    },
    // socket成功建立后 开始发数据
    onWebSocketOpen () {
      this.myconsole('[local]:socket链接成功')
      let city = pinyin2.getCamelChars(this.input1)
      // '哈尔滨'heb链家是hrb 特殊情况特殊处理
      if (this.input1 === '哈尔滨') {
        city = 'hrb'
      }
      this.sendMessag({
        method: '爬虫',
        params: {
          city: city,
          page: this.num.toString(),
          city_chn: this.input1,
          mode: this.checkboxGroup2[this.checkboxGroup2.length - 1]
        }
      })
    },
    onWebSocketError () {
      console.log('链接错误')
      this.myconsole('[local]:socket链接错误')
    },
    // 接收信息函数
    onWebSocketMessage (event) {
      // json转js对象
      const data = JSON.parse(event.data)
      // method console
      if (event.data && data.method === 'console') {
        this.myconsole('[sever]:' + data.params.message.toString())
      // method data
      } else if (event.data && data.method === 'data') {
        // 返回数据本地表赋值
        this.Datas = data.params.message
        this.sortDatas = this.sortDatasFunc()

        // 返浏览器存储数据
        const BaiduMapDatasall = {
          BaiduMap_Datas: data.params.message,
          BaiduMap_Datas_city_chn: data.params.city_chn,
          BaiduMap_Datas_mode: data.params.mode
        }
        localStorage.setItem('BaiduMap_Datas_all', JSON.stringify(BaiduMapDatasall))
      }
      // 有新数据 跟新echarts
      this.drawallChart()
    },
    onWebSocketClose (event) {
      if (this.websocket) {
        this.websocket.close() // 关闭WebSocket连接
        console.log(event)
        this.myconsole('[local]:socket链接被本机或服务器关闭')
        this.button1_isdisable = false
      }
    },
    // 发送信息函数
    sendMessag (message) {
      // js转json
      message = JSON.stringify(message)
      if (this.websocket && this.websocket.readyState === WebSocket.OPEN) {
        this.websocket.send(message)
        console.log('已发送') // 发送消息到WebSocket服务器
        this.myconsole(`[local]:已发送：${message}`)
      } else {
        console.log('发送失败')
        this.myconsole(`[local]:发送:${message}失败`)
      }
    },
    // #endregion
    // #region 下面是echarts方法
    // 画所有表
    drawallChart () {
      this.drawChart()
    },
    // 基础表1
    drawChart () {
      const chartDom = document.getElementById('main')
      this.myChart = echarts.init(chartDom)
      let option = {}

      option = {
        tooltip: {
          trigger: 'axis',
          axisPointer: { type: 'cross' },
          textStyle: { align: 'left' }
        },
        title: {
          text: '',
          left: 'center'
        },
        xAxis: {
          type: 'category',
          data: this.sortDatas.map(data => data.小区[0]),
          axisLabel: {
            interval: 0,
            rotate: 45 // 设置标签旋转30度
          }
        },
        yAxis:
        [
          {
            type: 'value',
            name: '租金',
            position: 'left'
          },
          {
            type: 'value',
            name: '面积',
            position: 'right',
            axisLabel: {
              formatter: '{value} ㎡'
            }
          }
        ],
        series: [
          {
            name: '租金',
            data: this.sortDatas.map(data => ({
              value: data.价格,
              MyData: data.访问链接, // 这里是你的自定义属性
              MyData2: data.坐标,
              MyData3: data.index
            })),
            type: 'bar',
            yAxisIndex: 0
          },
          {
            name: '面积',
            type: 'line',
            smooth: true,
            data: this.sortDatas.map(data => data.面积),
            yAxisIndex: 1

          }
        ]
      }

      option && this.myChart.setOption(option)
      this.myChart.on('click', (params) => {
        console.log(params.data)
        window.scrollTo(0, 500)
        this.test2(params.data.MyData2, params.data.MyData3)
      })
    },
    // 监听1表重绘
    handleresize () {
      if (this.resizeTimeout) {
        clearTimeout(this.resizeTimeout)
      }
      this.resizeTimeout = setTimeout(() => {
        this.myChart.resize()
      }, 400)
    }
    // #endregion
  },
  // #region 钩子函数
  created () {
    const BaiduMapDatasall = JSON.parse(localStorage.getItem('BaiduMap_Datas_all'))
    // 本地读取浏览器存储
    if (BaiduMapDatasall) {
      this.Datas = BaiduMapDatasall.BaiduMap_Datas
      this.input1 = BaiduMapDatasall.BaiduMap_Datas_city_chn
      this.checkboxGroup2[this.checkboxGroup2.length - 1] =
      BaiduMapDatasall.BaiduMap_Datas_mode
    }
    // 本地初始化
    this.sortDatas = this.sortDatasFunc()
    console.log(new Date().getTime())
    console.log(this.get_myDatetime())
  },
  beforeDestroy () {
    this.onWebSocketClose() // 在组件销毁前关闭WebSocket连接
  },
  // 真正守望者 值变化会触发 1.绑定input1和地图中心点 2.坐标点显示模式
  watch: {
    input1: function (newVal, oldVal) {
      if (this.input1) this.centerpoint = newVal
    }
  },
  // #region 下面是事件监听 为1.实现控制台滚动功能 2.echarts表实例化 3.监听屏变防抖重绘
  mounted () {
    document.querySelector('.myitem3').addEventListener('scroll', this.scrolling)
    this.drawallChart()
    // 3.监听屏变防抖重绘
    window.addEventListener('resize', this.handleresize)
  },
  destroyed () {
    document.querySelector('.myitem3').removeEventListener('scroll', this.scrolling)
    window.removeEventListener('resize', this.handleresize)
  }
  // #endregion
// #endregion
}
</script>
