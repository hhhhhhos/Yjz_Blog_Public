<template>
  <div class="block">
    <span class="demonstration">Click 指示器触发</span>
    <el-carousel trigger="click" height="150px">
      <el-carousel-item v-for="item in items" :key="item.id">
          <h3 class="small" >{{ item.title }}</h3>
      </el-carousel-item>
    </el-carousel>
    <div :style="{ backgroundImage: 'url(' + require('../assets/s2.webp') + ')', height: '300px' }"></div>
  </div>
</template>

<style>
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 150px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
     background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
     background-color: #d3dce6;
  }
</style>

<script>
export default {
  data () {
    return {
      items: [
        { id: 1, title: '标题1', image: '../assets/s1.webp' },
        { id: 2, title: '标题2', image: '../assets/s2.webp' },
        { id: 3, title: '标题3', image: '../assets/s3.webp' },
        { id: 4, title: '标题4', image: '../assets/s4.webp' }
      ]
    }
  }
}
</script>
