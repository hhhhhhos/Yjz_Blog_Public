<template>
  <!-- 红点 -->
  <bm-marker @mouseover="infoshow" @mouseout="infohide" :position="{lng:Data.坐标[0],lat:Data.坐标[1]}" :dragging="false" @click="infoWindowOpen" :icon="{url: this.showmode === true ? getaddress(Data.每平方租金, Data.价格) : getaddress2(Data.每平方租金, Data.价格), size: {width: 35, height: 35}}">
    <!-- 点击后展开的框 -->
    <bm-info-window :show="show" @close="infoWindowClose" >
      <div style="display: flex;">
        <div style="height: 122px;width: 160px;overflow: hidden;margin-right: 10px;border: 3px solid #282828;display: flex;justify-content: center;align-items: center;">
          <img v-lazy="Data.图片" style="width: 100%;height: 100%;">
        </div>
        <div style="display: block;">
        <div v-if="Data.地点.length > 0">
          地区：{{Data.地点}}
        </div>
          小区：{{Data.小区}}
        <div>
          面积：{{Data.面积}}㎡ &nbsp;&nbsp;租金：{{Data.价格}}元
        </div>
        <div>
          每平方：{{Data.每平方租金}}元/㎡
        </div>
        <a :href="Data.访问链接" target="_blank">访问链接</a>
        </div>
      </div>
    </bm-info-window>
    <!-- 红点上悬浮的文字 -->
    <bm-label v-if=infostyle :content="Data.价格.toString()" :offset="{width: 5, height: -10}" :labelStyle="{color: 'white', fontSize: '8px', backgroundColor: 'rgba(0,0,0,0.5)', border: '0', borderRadius: '5px'}"/>
  </bm-marker>
</template>

<style>
</style>

<script>
import BmMarker from 'vue-baidu-map/components/overlays/Marker.vue'
import BmInfoWindow from 'vue-baidu-map/components/overlays/InfoWindow.vue'
import BmLabel from 'vue-baidu-map/components/overlays/Label.vue'
export default {
  components: {
    BmMarker,
    BmInfoWindow,
    BmLabel
  },
  props: {
    Data: Object,
    showmode: Boolean
  },
  data () {
    return {
      imageLoaded: false,
      show: false,
      infostyle: false,
      address: '../assets/locr.svg',
      icons: {
        b: require('../assets/locb.svg'),
        r: require('../assets/locr.svg'),
        blue: require('../assets/locblue.svg'),
        g: require('../assets/locg.svg'),
        w: require('../assets/locw.svg')
      }
    }
  },
  methods: {
    test () {
      this.imageLoaded = true
    },
    infoWindowClose () {
      this.show = false
    },
    infoWindowOpen () {
      this.show = !this.show
    },
    // 悬浮在红点时显示的文字
    infoshow () {
      this.infostyle = true
    },
    infohide () {
      this.infostyle = false
    },
    // 根据每平方米价格决定图标样式
    getaddress2 (price2, price1) {
      const price = price2
      if (price > 200) {
        return this.icons.b
      } else if (price > 100) {
        return this.icons.r
      } else if (price > 50) {
        return this.icons.blue
      } else if (price > 20) {
        return this.icons.g
      } else {
        return this.icons.w
      }
    },
    // 根据总租金价格决定图标样式
    getaddress (price2, price1) {
      const price = price1
      if (price > 10000) {
        return this.icons.b
      } else if (price > 5000) {
        return this.icons.r
      } else if (price > 2500) {
        return this.icons.blue
      } else if (price > 500) {
        return this.icons.g
      } else {
        return this.icons.w
      }
    }
  }
}
//
</script>
