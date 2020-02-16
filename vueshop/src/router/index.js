import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)
import Home from '@/components/Home'
import Login from "../components/Login"
import Register from "../components/Register";
export default new Router({
  mode:'history',
  routes: [
    {
      path: '/',
      name:'Home',
      component:Home,

    },
    {
      path: '/home',
      name:'Home',
      component:Home,

    },
    {
      path: '/login',
      name:'Login',
      component:Login,

    },
    {
      path:'/register',
      name:'register',
      component:Register,
    },

  ]
})
