<template>
    <div id="index">
      <mt-header fixed title="汽车之家" style="text-align: center"></mt-header>
      <div id="main">
        <router-view></router-view>
      </div>
      <mt-tabbar v-model="selected">
        <mt-tab-item id="Home" >
          <img slot="icon" src="../assets/主页.png">
          首页
        </mt-tab-item>
        <mt-tab-item id="News">
          <img slot="icon" src="../assets/资料.png">
          刷新
        </mt-tab-item>
        <mt-tab-item id="Search">
          <img slot="icon" src="../assets/搜索.png">
          搜索
        </mt-tab-item>
        <mt-tab-item id="Cart">
          <img slot="icon" src="../assets/购物车.png">
          购物车
        </mt-tab-item>
        <mt-tab-item id="User">
          <img slot="icon" src="../assets/个人中心.png">
          我的
        </mt-tab-item>
      </mt-tabbar>
    </div>
</template>

<script>
    export default {
        name: "Index",
      // created() {
      //     this.$router.push({path:'/detail'})
      // }
        data(){
          return{
            selected:''
          }

        },
      #设置监听selected,使用newV对象传递获取的id值,通过name属性与index.js中的name互相绑定传递路由
        watch: {
          selected (newV, oleV){
            this.$router.push({
              name:newV
            })

          }
        }

    }
</script>

<style scoped>
#main{
  margin-top: 50px;
  background-color: bisque;
}
</style>
