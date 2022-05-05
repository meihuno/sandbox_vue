import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue' // add
import 'bootstrap/dist/css/bootstrap.css' // add
// import 'bootstrap-vue/dist/bootstrap-vue.css' // add

import VuePaginate from "vue-paginate";
import ReactiveSearch from "@appbaseio/reactivesearch-vue";

Vue.use(ReactiveSearch);
Vue.use(VuePaginate);
Vue.use(BootstrapVue) // add
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
