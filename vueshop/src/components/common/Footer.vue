<template>
    <div class="footer">
      <ul>
        <li v-for="nav in nav_list">
          <a :href="nav.link" v-if="nav.opt==2">{{nav.name}}</a>
<!--          <router-link :to="nav.link" v-else>{{nav.name}}</router-link>-->
        </li>
      </ul>
      <p>Copyright © zqm-shop</p>
    </div>
</template>

<script>
    export default {
        name: "Footer",
        data(){
            return {
                nav_list:[]
            }
        },
        created() {
            this.get_nav();
        },
        methods:{
            get_nav(){
                // 获取导航
                this.$axios.get(`${this.$settings.Host}/home/nav/`).then(response=>{
                    this.nav_list = response.data;
                }).catch(error=>{
                    this.$alert('导航信息获取失败！', "shop");
                })
            }
        }
    }
</script>

<style scoped>
.footer {
  width: 100%;
  height: 128px;
  background: #25292e;
  color: #fff;
}
.footer ul{
  margin: 0 auto 16px;
  padding-top: 38px;
  width: 810px;
}
.footer ul li{
  float: left;
  width: 112px;
  margin: 0 10px;
  text-align: center;
  font-size: 14px;
}
.footer ul::after{
  content:"";
  display:block;
  clear:both;
}
.footer p{
  text-align: center;
  font-size: 12px;
}
.footer ul li a{
  color: white;
}
</style>
