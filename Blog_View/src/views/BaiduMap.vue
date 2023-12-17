<template>
  <!-- 主页面 -->
  <div style="background-color:rgba(242,243,245);padding:0 45px 25px 45px;">
    <!-- 操作面板 -->
    <div style="padding: 45px 85px 25px 0;min-width: 600px;">
      <div class="myitem" style="display: block;">
        <div style="color: #1F2F3D;">链家爬虫可视化作业</div>
        <div style="display: flex;">爬取城市:<el-input style="max-width: 200px;height: 5px;margin-left: 15px;" v-model="input1" placeholder="(选填) 默认广州"></el-input></div>
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
      <baidu-map style="border-radius: 5px;border: 5px solid #ffffff;box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);" class="map" :center="input1===''?'广州': input1" :zoom=13 :scroll-wheel-zoom="true">
        <!-- 杂七杂八控件 -->
        <bm-scale anchor="BMAP_ANCHOR_TOP_RIGHT"></bm-scale>
        <bm-control>

        </bm-control>
        <bm-navigation anchor="BMAP_ANCHOR_TOP_RIGHT"></bm-navigation>
        <bm-map-type :map-types="['BMAP_NORMAL_MAP', 'BMAP_HYBRID_MAP']" anchor="BMAP_ANCHOR_TOP_LEFT"></bm-map-type>
        <!-- 红点 -->
        <div v-for="Data in Datas" :key="Data.index">
          <BaiduMapDot :Data="Data" />
        </div>
      </baidu-map>
      <div class="myborder" style="margin-left:  5px;width: 300px;height: 600px; overflow-y: auto;">
        <div v-for="Data in Datas" :key="Data.index">
          {{Data.index}}
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
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
</style>

<script>
import BaiduMapDot from '@/components/BaiduMapDot.vue'
import Pinyin from 'pinyin'

export default {
  components: {
    BaiduMapDot
  },
  data () {
    return {
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
      Datas: [
        {
          index: 0,
          地点: [
            '增城',
            '荔城西区'
          ],
          小区: [
            '创基天峰'
          ],
          面积: 103,
          价格: 1600,
          每平方租金: 15,
          访问链接: 'https://gz.lianjia.com/zufang/GZ1742120536063868928.html',
          坐标: [
            113.80418795579757,
            23.283976990912365
          ]
        },
        {
          index: 1,
          地点: [
            '荔湾',
            '大坦沙'
          ],
          小区: [
            '珠岛花园'
          ],
          面积: 6,
          价格: 1081,
          每平方租金: 180,
          访问链接: 'https://gz.lianjia.com/zufang/GZ1790306855952580608.html',
          坐标: [
            113.23120181017529,
            23.13668937911409
          ]
        },
        {
          index: 2,
          地点: [
            '增城',
            '新塘南'
          ],
          小区: [
            '保利东江首府'
          ],
          面积: 136,
          价格: 3000,
          每平方租金: 22,
          访问链接: 'https://gz.lianjia.com/zufang/GZ1826133400197529600.html',
          坐标: [
            113.63808902129374,
            23.11516902284898
          ]
        },
        {
          index: 3,
          地点: [],
          小区: [
            '独栋·miniG公寓',
            'miniG公寓-天河路店'
          ],
          面积: 20,
          价格: 3500,
          每平方租金: 175,
          访问链接: 'https://gz.lianjia.com/apartment/69095.html',
          坐标: [
            113.4592853519665,
            23.046844214472234
          ]
        },
        {
          index: 4,
          地点: [
            '黄埔',
            '知识城'
          ],
          小区: [
            '广州绿地城'
          ],
          面积: 42,
          价格: 2100,
          每平方租金: 50,
          访问链接: 'https://gz.lianjia.com/zufang/GZ1825747348450443264.html',
          坐标: [
            113.55661298105731,
            23.328377704249164
          ]
        },
        {
          index: 5,
          地点: [],
          小区: [
            '独栋·红林物业',
            '设计之都二店'
          ],
          面积: 35,
          价格: 2480,
          每平方租金: 70,
          访问链接: 'https://gz.lianjia.com/apartment/48759.html',
          坐标: [
            113.29025048556537,
            23.228382429918323
          ]
        },
        {
          index: 6,
          地点: [
            '黄埔',
            '香雪'
          ],
          小区: [
            '时代天韵（黄埔）'
          ],
          面积: 81,
          价格: 3300,
          每平方租金: 40,
          访问链接: 'https://gz.lianjia.com/zufang/GZ1827325999373615104.html',
          坐标: [
            113.45372888323635,
            23.101054587832454
          ]
        },
        {
          index: 7,
          地点: [],
          小区: [
            '独栋·华仔国际公寓',
            '智萃旗舰店'
          ],
          面积: 38,
          价格: 1980,
          每平方租金: 52,
          访问链接: 'https://gz.lianjia.com/apartment/47535.html',
          坐标: [
            113.27143134445974,
            23.135336306695006
          ]
        },
        {
          index: 8,
          地点: [
            '黄埔',
            '大沙地'
          ],
          小区: [
            '金碧世纪花园'
          ],
          面积: 158,
          价格: 5500,
          每平方租金: 34,
          访问链接: 'https://gz.lianjia.com/zufang/GZ1829057911251271680.html',
          坐标: [
            113.4358903324251,
            23.12051782286747
          ]
        },
        {
          index: 9,
          地点: [],
          小区: [
            '独栋·盛世国际物业',
            '天河公寓时尚店'
          ],
          面积: 35,
          价格: 2500,
          每平方租金: 71,
          访问链接: 'https://gz.lianjia.com/apartment/67956.html',
          坐标: [
            113.36079387825733,
            23.140209579145036
          ]
        },
        {
          index: 10,
          地点: [
            '越秀',
            '麓景'
          ],
          小区: [
            '麓湖盛景'
          ],
          面积: 35,
          价格: 3200,
          每平方租金: 91,
          访问链接: 'https://gz.lianjia.com/zufang/GZ1830111241033482240.html',
          坐标: [
            113.2821150715475,
            23.15142871532774
          ]
        },
        {
          index: 11,
          地点: [
            '天河',
            '车陂'
          ],
          小区: [
            '美好居'
          ],
          面积: 10,
          价格: 1711,
          每平方租金: 171,
          访问链接: 'https://gz.lianjia.com/zufang/GZ1812486267993063424.html',
          坐标: [
            113.39987663572813,
            23.131587577592708
          ]
        },
        {
          index: 12,
          地点: [
            '花都',
            '镜湖大道'
          ],
          小区: [
            '朗悦君廷'
          ],
          面积: 130,
          价格: 2600,
          每平方租金: 20,
          访问链接: 'https://gz.lianjia.com/zufang/GZ1777970835127009280.html',
          坐标: [
            113.25701821221801,
            23.35903573219703
          ]
        }
      ],
      // 下面是控制台滚动脚本参数
      scrollFlag: true,
      oldScrollTop: 0
    }
  },
  methods: {
    // #region 下面是土著功能
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
    // 城市转首字母
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
      this.websocket = new WebSocket('ws://localhost:8002/ws') // 创建WebSocket连接
      this.websocket.onopen = this.onWebSocketOpen // WebSocket连接打开时的处理函数
      this.websocket.onerror = this.onWebSocketError //
      this.websocket.onmessage = this.onWebSocketMessage // 收到WebSocket消息时的处理函数
      this.websocket.onclose = this.onWebSocketClose // WebSocket连接关闭时的处理函数
    },
    onWebSocketOpen () {
      this.myconsole('[local]:socket链接成功')
      this.sendMessag({
        method: '爬虫',
        params: {
          city: this.getInitials(this.input1),
          page: this.num.toString(),
          city_chn: this.input1
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
      if (event.data && data.method === 'console') {
        this.myconsole('[sever]:' + data.params.message.toString())
      } else if (event.data && data.method === 'data') {
        this.Datas = data.params.message
        localStorage.setItem('BaiduMap_Datas', JSON.stringify(this.Datas))
      }
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
    }
    // #endregion
  },
  created () {
    if (localStorage.getItem('BaiduMap_Datas')) {
      this.Datas = JSON.parse(localStorage.getItem('BaiduMap_Datas'))
    }
    console.log(new Date().getTime())
    console.log(this.get_myDatetime())
  },
  beforeDestroy () {
    this.onWebSocketClose() // 在组件销毁前关闭WebSocket连接
  },
  // #region 下面是事件监听 为实现控制台滚动功能
  mounted () {
    document.querySelector('.myitem3').addEventListener('scroll', this.scrolling)
  },
  destroyed () {
    document.querySelector('.myitem3').removeEventListener('scroll', this.scrolling)
  }
  // #endregion
}
</script>
