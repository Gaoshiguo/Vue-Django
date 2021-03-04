import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const routerPush = Router.prototype.push
Router.prototype.push = function push(location) {
    return routerPush.call(this, location).catch(error => error)
}
Vue.use(Router)

export default new Router({
    routes: [{
            path: "/",
            component: resolve => require(['../components/pages/login.vue'], resolve),
            name:"login"
        },
        {
            path: "/home",
            component: resolve => require(['../components/pages/home.vue'], resolve),
            children: [{
                path: '/index',
                component: resolve => require(['../components/pages/index.vue'], resolve),
                name: "index"
            },{
                path: '/studentinformation',
                component: resolve => require(['../components/pages/usermanage.vue'], resolve),
                name: "studentinformation"
            },{
                path:"/userinformation",
                component:resolve=> require(['../components/pages/userinformation.vue'],resolve),
                name:"userinformation"
            }]
        }
    ]
})
