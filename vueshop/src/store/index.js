import Vue from 'vue'

import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
 // 数据仓库,类似vue组件里面的data
 state: {
    cart:{
      num : 0,
    }
 },
 // 数据操作方法,类似vue里面的methods
 mutations: {
   update_num(state,data){
     state.cart.num =data
   }

 }
});
