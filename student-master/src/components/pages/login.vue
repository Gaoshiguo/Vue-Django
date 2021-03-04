<template>
    <div class="container">
        <div :style="{'width':container_width+'px','height':container_height+'px'}">
            <el-row style="height: 100%;">
                <el-col :span="15" style="height: 100%;"></el-col>
                <el-col class="login_box" :span="6" :style="{'margin-top':container_height*0.2+'px','height':container_height*0.5+'px'}">
                    <el-row style="height: 30%;">
                        <el-col :span="24" style="margin-top: 30px;">
                            <el-image style="border-radius: 50%; width: 100px; height: 100px" src="../../../static/img/logo.png" fit="fill">
                            </el-image>
                        </el-col>
                    </el-row>
                    <el-row style="height: 50%;text-align: left;margin-top: 30px;">
                        <el-col :span="24">
                            <span style="margin-left: 30px;color: #C47943;">
                                您好，请登录！
                            </span>
                            <el-form style="margin-top: 30px;">
                                <el-form-item>
                                    <el-input :maxlength="18" :minlength="15" style="width: 90%;margin-left: 5%;"
                                        placeholder="请输入账号" prefix-icon="el-icon-user" v-model="user_id">
                                    </el-input>
                                </el-form-item>
                                <el-form-item>
                                    <el-input show-password :maxlength="18" style="width: 90%;margin-left: 5%;"
                                        placeholder="请输入密码" prefix-icon="el-icon-lock" v-model="user_password">
                                    </el-input>
                                </el-form-item>
                                <el-form-item>
                                    <el-button type="primary" style="width: 90%;margin-right:5%;float: right;" @click="login">登陆</el-button>
                                </el-form-item>
                            </el-form>

                        </el-col>
                    </el-row>
                </el-col>
            </el-row>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                container_height: document.documentElement.clientHeight,
                container_width: document.documentElement.clientWidth,
                user_id: null,
                user_password: null,
            }
        },
        mounted() {
            //设置监听器，监听页面大小变化
            let _me = this;
            window.onresize = () => {
                return (() => {
                    _me.container_height = document.documentElement.clientHeight;
                    _me.container_width = document.documentElement.clientWidth;

                })();
            };
            //清空缓存
            if (sessionStorage.getItem('user_id') && sessionStorage.getItem('user_id') !== "") {
                sessionStorage.clear();
            }
            //清空内存
            if (this.$store.state.user_id !== null || this.$store.state.user_id !== "") {
                this.$store.commit("login_out");
            }
        },
        watch: {},
        methods: {
            login() {
                if (!this.user_id || this.user_id === '' || this.user_id.length <= 0) {
                    this.$message({
                        type: "error",
                        message: "账号错误，请正确输入！"
                    })
                } else {
                    let _me = this;
                    // this.axios.post('/api/login', {
                    //     user_id: _me.user_id,
                    // }).then((res) => {
                    //     if (res.data === "success") {
                    // this.$store.commit("login",_me.user_id);
                    //         this.$route.push({path:"/home"})
                    //     }
                    // })
                    this.$store.commit("login", _me.user_id);
                    console.log("存储");
                    sessionStorage.setItem('user_id', _me.user_id);
                    console.log("存储完成")
                    this.$router.replace({
                        path: "/index"
                    })
                }

            }
        },

    }
</script>

<style>
    .container {
        position: fixed;
        width: 100%;
        height: 100%;
        background-image: url(../../../static/img/bg.jpg);
        background-repeat: no-repeat;
        background-size: cover;
    }

    .login_box {
        border: 2px solid #909399;
        border-radius: 20px;
        background-color: rgb(255, 255, 255, 0.9);
    }
</style>
