// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import App from './App';
import router from './router';
import ElementUI from 'element-ui';
import settings from "./settings";
import axios from 'axios'
import '../static/css/reset.css'
import 'element-ui/lib/theme-chalk/index.css';
axios.defaults.withCredentials=false
Vue.prototype.$axios = axios;
Vue.prototype.$settings = settings;
Vue.config.productionTip = false
Vue.use(ElementUI);
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
