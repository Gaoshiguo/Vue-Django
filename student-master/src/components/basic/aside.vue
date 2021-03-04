<template>
    <div class="aside">
        <div style="height: 100px;width: 200px;">
            <el-image style="background-color: #FFFFFF; width: 80px;height:80px;margin-top: 10px;border-radius: 50%;" src="../../../static/img/logo.png" fit="fill"
                @click="button_image">
            </el-image>
        </div>
        <el-menu style="margin-right: 5px;margin-left: 5px;" :default-active="onRoutes" class="el-menu-vertical-demo"
            mode="vertical" router text-color="#FFFFFF" background-color="rgba(255, 255, 255, 0)" active-text-color="#F17F42">
            <el-menu-item v-for="item in aside_bar" :index="item.index" :key="item.index" style="height: 50px;text-align: center;">
                <template slot="title">
                    <i :class="item.icon"></i>
                    <span v-if="item.name==='首页'">首&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;页</span>
                    <span v-else>
                        {{item.name}}
                    </span>
                </template>
            </el-menu-item>
        </el-menu>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                aside_bar: [{
                        index: "index",
                        name: "成绩预警",
                        icon: "el-icon-custom-zhangdanguanli"
                    },
                    {
                        index: 'studentinformation',
                        name: "学生信息",
                        icon: "el-icon-custom-yonghuguanli"
                    },
                    {
                        index: 'userinformation',
                        name: "成绩信息",
                        icon: "el-icon-custom-zuoyeguanli"
                    },
                ]
            }
        },
        computed: {
            onRoutes() {
                return this.$route.path.replace("/", "");
            },
            container_height() {
                return document.documentElement.clientHeight;
            },
        },
        methods: {
            button_image() {
                this.$router.replace({
                    path: "/index"
                })
            }
        },
    }
</script>

<style>
    .aside {
        height: 100%;
        position: relative;
    }

    .el-menu {
        border-right: 0 !important;
    }
</style>
