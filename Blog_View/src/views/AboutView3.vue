<template>
  <div>
    <body>
    <div class="bg">
      <div class="container">
      <div class="jumbotron">
        <div class="panel panel-success">
          <div style="height: 220px;"></div>
          <div class="panel-heading"><h1>老铁，欢迎你！但&ensp;还&ensp;在&ensp;建</h1><h3>Welcome,&ensp;LaoTie &ensp;&ensp;&ensp;But the blog is GG!</h3></div>
        </div>
          <h3>挥一挥衣袖</h3>
          <li>不带走一片云彩</li>
          <li>学海无涯，回头是岸</li>
          <li>这么多坑一时半会填不完</li>
          <li>就这样吧~撒有拉拉</li>
        </div>
      </div>
    </div>
    <b-button v-b-toggle="'collapse-2'" class="m-1">Toggle Collapse</b-button>
    <!-- Element to collapse -->
    <b-collapse id="collapse-2" >
      <b-card style="height: 800px;background-color: bisque;">I am collapsible content!</b-card>
    </b-collapse>
    <div style="height: 820px;"></div>
    </body>

  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: {
  }
}
</script>

<style scoped>
.bg{
  background-image: url("../assets/bg5.webp");
  background-position:center;
  background-size:cover;
  height: 700px;
  width: 100%;
  margin-top: -90px;
}

</style>
