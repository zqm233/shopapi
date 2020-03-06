// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import App from './App';
import router from './router';
import ElementUI from 'element-ui';
import settings from "./settings";
import store from "./store/index";
import axios from 'axios'
import '../static/css/reset.css'
import 'element-ui/lib/theme-chalk/index.css';
axios.defaults.withCredentials=false
Vue.prototype.$axios = axios;
Vue.prototype.$settings = settings;
Vue.config.productionTip = false
Vue.use(ElementUI);
/* eslint-disable no-new */

require('video.js/dist/video-js.css');
require('vue-video-player/src/custom-theme.css');
import VideoPlayer from 'vue-video-player'
Vue.use(VideoPlayer);


new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
