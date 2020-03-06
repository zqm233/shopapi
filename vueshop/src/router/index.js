import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)
import Home from '@/components/Home'
import Login from "../components/Login"
import Register from "../components/Register";
import Course from "../components/Course";
import Detail from "../components/Detail";
import Cart from "../components/Cart";

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
      name:'Register',
      component:Register,
    },
    {
      path:'/courses',
      name:'Courses',
      component:Course,
    },
    {
      path:'/courses/:id',
      name:'Detail',
      component:Detail
    },
    {
      path:'/cart',
      name:'Cart',
      component:Cart
    },

  ]
})
