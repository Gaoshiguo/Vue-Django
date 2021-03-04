// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import axios from 'axios';
import VueAxios from 'vue-axios';
import Vuex from 'vuex'
import store from '../store/index.js'
//引入三方图标
import './assets/icon/iconfont.css'
import qs from "qs"
//引入echarts
import echarts from 'echarts'
import "echarts/lib/chart/line"
import "echarts/lib/chart/pie"
import VECharts from 'vue-echarts';



Vue.use(Vuex)
Vue.use(ElementUI);
Vue.use(VueAxios, axios)
Vue.component('v-chart', VECharts)
Vue.prototype.$echarts = echarts
Vue.config.productionTip = false


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
