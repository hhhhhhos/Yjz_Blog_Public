<template>
  <div>
    <el-carousel :interval="8000" arrow="always" trigger="click" height="650px" style="margin-top:-40px;">
      <el-carousel-item v-for="item in items" :key="item.id"
      :style="{ backgroundImage: 'url(' + item.image + ')'}">
          <pre class="small">
            <div class="carousel-caption">
              <h3>{{item.title}}</h3>
              <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
              <!---->
            </div>
          </pre>
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
export default {
  data () {
    return {
      items: [
        { id: 1, title: 'First slide', image: require('../assets/s1.webp') },
        { id: 2, title: 'Second slide', image: require('../assets/s2.webp') },
        { id: 3, title: 'Third slide', image: require('../assets/s3.webp') },
        { id: 4, title: 'Forth slide', image: require('../assets/s4.webp') }
      ]
    }
  }
}
</script>

<style scoped>

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
  .myclass{
    background-size: cover ;
    background-position: center;
  }
  .carousel-caption {
    position: absolute;
    right: 15%;
    bottom: 1.25rem;
    left: 15%;
    padding-top: 1.25rem;
    padding-bottom: 1.25rem;
    color: #fff;
    text-align: center;
}
h3{
    font-size: calc(1.3rem + 0.6vw);
}
p {
    display: block;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    margin-top: 0;
    margin-bottom: 1rem;
}
</style>
