import Vue from 'vue'
import Router from 'vue-router'
import Index from "../components/Index";
import Home from "../components/Home/Home";
import News from "../components/News/News";
import Cart from "../components/ShopCart/Cart";
import User from "../components/User/User";
import Search from "../components/Search/Search";
Vue.use(Router)

export default new Router({
  mode:'history',
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index,
      children:[
        {
          path: 'home',
          name: 'Home',
          component: Home,
        },
        {
          path: 'news',
          name: 'News',
          component: News,
        },
        {
          path: 'cart',
          name: 'Cart',
          component: Cart,
        },
        {
          path: 'search',
          name: 'Search',
          component: Search,
        },
        {
          path: 'user',
          name: 'User',
          component: User,
        },
      ],
    },


  ],

})
