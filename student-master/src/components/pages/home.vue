<template>
    <div class="container" :style="{'height':container_height+'px','width':container_width+'px'}" v-cloak>
        <el-container :style="{'height':container_height+'px','width':'100%'}">
            <el-aside :style="{'height':container_height+'px','width':'200px'}">
                <cu-aside class="home_aside" style="background-color: #314255;"></cu-aside>
            </el-aside>
            <el-container :style="(container_width-200)+'px'">
                <el-header height="60px" style="padding: 0px;">
					<el-row height="60px" :gutter="10" style="background-color: #314255;line-height: 1;vertical-align: baseline">
                        <el-col :span="3" :offset="21" style="height: 60px;">
                            <el-dropdown @command="handle_command">
                                <span class="el-dropdown-link" style="height: 60px;line-height: 60px;color: #F17F42;">
                                    您好，管理员
                                </span>
                                <el-dropdown-menu slot="dropdown">
                                    <el-dropdown-item icon="el-icon-custom-tuichu" command="login_out">退出</el-dropdown-item>
                                </el-dropdown-menu>
                            </el-dropdown>
                        </el-col>
                    </el-row>
                </el-header>
                <el-main :style="{'height':(container_height-60)+'px','overflow-y': 'hidden'}" style="background-color:#CCCCCC;padding: 10px 10px;">
                    <transition
                        mode="out-in"
                        enter-class="fade-transverse-enter"
                        enter-active-class="fade-transverse-enter-active"
                        appear>
                        <router-view :key="router_key"></router-view>
                    </transition>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>

<script>
    import cuAside from '../basic/aside.vue'
    export default {
        data(){
            return {

            }
        },
        computed:{
            container_height(){
                return document.documentElement.clientHeight;
            },
            container_width(){
                return document.documentElement.clientWidth;
            },
            router_key(){
                console.log("路由KEY：",this.$route.name)
                return this.$route.name;
            },
            user_id(){
                return this.$store.state.user_id;
            }
        },
        beforeCreate() {
            console.log("查询",sessionStorage.getItem('user_id'))
            if(sessionStorage.getItem('user_id') && sessionStorage.getItem('user_id')!==""){
                this.$store.commit("login",sessionStorage.getItem('user_id'));
            }else{
                this.$router.replace({
                    path: "/"
                })
            }
            if(!this.$store.state.user_id || this.$store.state.user_id===""){
                this.$router.replace({
                    path: "/"
                })
            }
        },
        watch:{
            $route(toURL,fromURL){
                // console.log("去向:",to,"来向",from)
                console.log(fromURL.name)
                if(toURL.name==="login"){
                    this.login_out()
                }
            },
            user_id(newVal){
                if(newVal===null || newVal===""){
                    this.$router.replace({
                        path: "/"
                    })
                }
            }
        },
        components:{
            cuAside
        },
        methods:{
            login_out(){
                console.log("执行退出")
                sessionStorage.clear();
                this.$store.commit("login_out");
            },
            handle_command(command){
                if(command==="login_out"){
                    this.login_out();
                }
            },
        },
    }
</script>

<style>
    [v-cloak] {
        display: none !important;
    }
    .container{
        position: fixed;
        width: 100%;
    }
    .fade-transverse-leave-active,
    .fade-transverse-enter-active {
      transition: all .5s;
    }
    .fade-transverse-enter {
      opacity: 0;
      transform: translateX(-30px);
    }
    .fade-transverse-leave-to {
      opacity: 0;
      transform: translateX(30px);
    }
</style>
