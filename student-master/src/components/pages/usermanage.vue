<template>
    <div style="height: 100%;" v-cloak>
        <el-drawer
            append-to-body
            title="学生详细信息"
            :visible.sync="show_detail"
            direction="rtl"
            size="30%">
            <div class="demo-drawer__content" >
                <el-row :gutter="10" v-for="(value,key,index) in detail_student" :key="index" style="border-bottom: 1px #404040;background-color:#ECF5FF;margin-top: 5px;margin-left: 10px;margin-right: 10px;">
                <el-col :span="6" style="height:30px;line-height: 30px;text-align: right;">{{key}}:</el-col>
                <el-col :span="18" style="height:30px;line-height: 30px;padding-left: 10px;">{{value}}</el-col>
            </el-row>
            </div>
        </el-drawer>

        <div style="height: 100%;" v-loading="loading">
            <el-row style="height: 100%;">
                <el-col ref="one_height" :span="24" style="height: 100%;">
                    <el-row ref="one_one_height">
                        <el-col :span="24" style="background-color: #FFFFFF;height:80px;padding: 20px 20px;">
                            <el-row>
                                <el-col :span="24">
                                    <el-row :gutter="10">
                                        <el-col :span="3" style="height: 36px;line-height: 36px;">查询条件：</el-col>
                                        <el-col :span="3">
                                            <el-select style="width: 100%;" v-model="search_student_department" size="medium"
                                                clearable placeholder="请选择院系">
                                                <el-option v-for="item in search_student_department_list" :key="item.department_id"
                                                    :label="item.department_name" :value="item.department_name">
                                                </el-option>
                                            </el-select>
                                        </el-col>
                                        <el-col :span="3">
                                            <el-select style="width: 100%;" v-model="search_student_major" size="medium"
                                                clearable placeholder="请选择专业">
                                                <el-option v-for="item in search_student_major_list" :key="item.major_id" :label="item.major_name"
                                                    :value="item.major_name">
                                                </el-option>
                                            </el-select>
                                        </el-col>
                                        <el-col :span="3">
                                            <el-select style="width: 100%;" v-model="search_student_grade" size="medium"
                                                clearable placeholder="请选择年级">
                                                <el-option v-for="item in search_student_grade_list" :key="item" :label="item"
                                                    :value="item">
                                                </el-option>
                                            </el-select>
                                        </el-col>
                                        <el-col :span="3">
                                            <el-select style="width: 100%;" v-model="search_student_class" size="medium"
                                                clearable placeholder="请选择班级">
                                                <el-option v-for="item in search_student_class_list" :key="item.class_id" :label="item.class_name"
                                                    :value="item.class_name">
                                                </el-option>
                                            </el-select>
                                        </el-col>
                                        <el-col :span="3">
                                            <el-input v-model="search_student_number" size="medium" clearable placeholder="请输入学号"></el-input>
                                        </el-col>
                                        <el-col :span="3">
                                            <el-input v-model="search_student_name" size="medium" clearable placeholder="请输入姓名"></el-input>
                                        </el-col>
                                    </el-row>
                                </el-col>
                            </el-row>
                        </el-col>
                    </el-row>
                    <el-row :style="{'margin-top': '5px'}" >
                        <el-col :span="24">
                            <el-table
                            size="small"
                            highlight-current-row border
                            :data="current_student"
                            :height='one_second_height-30'
                            :header-cell-style="{background:'#eef1f6',color:'#606266'}"
                            @row-click="show_detail_student">
                                <el-table-column type="index"></el-table-column>
                                <el-table-column :label="show_table_list[0]" align="center" sortable>
                                    <template slot-scope="scope">
                                        <i class="el-icon-custom-Idcard"></i>
                                        <span style="margin-left: 5px;">{{scope.row.student_id}}</span>
                                    </template>
                                </el-table-column>
                                <el-table-column :label="show_table_list[1]" align="center">
                                    <template slot-scope="scope">
                                        <i class="el-icon-s-custom"></i>
                                        <span style="margin-left: 5px;">{{scope.row.student_name ==="" || !scope.row.student_name?"无":scope.row.student_name}}</span>
                                    </template>
                                </el-table-column>
                                <el-table-column :label="show_table_list[2]" align="center">
                                    <template slot-scope="scope">
                                        <span style="margin-left: 5px;">{{scope.row.department_name}}</span>
                                    </template>
                                </el-table-column>
                                <el-table-column :label="show_table_list[3]" align="center">
                                    <template slot-scope='scope'>
                                        <span style="margin-left: 5px;">{{scope.row.major_name }}</span>
                                    </template>
                                </el-table-column>
                                <el-table-column :label="show_table_list[4]" align="center">
                                    <template slot-scope="scope">
                                        <span style="margin-left: 5px;">{{scope.row.student_grade }}</span>
                                    </template>
                                </el-table-column>
                                <el-table-column :label="show_table_list[5]" align="center">
                                    <template slot-scope="scope">
                                        <span style="margin-left: 5px;">{{scope.row.class_name}}</span>
                                    </template>
                                </el-table-column>
                                <el-table-column :label="show_table_list[6]" align="center">
                                    <template slot-scope="scope">
                                        <span style="margin-left: 5px;">{{scope.row.counselor_name}}</span>
                                    </template>
                                </el-table-column>
                            </el-table>
                        </el-col>
                    </el-row>
                    <el-row ref="one_third_height" style="padding:15px 15px;background-color: #FFFFFF;">
                        <el-pagination
                            background
                            :current-page="current_page"
                            :page-sizes="[5,10, 20, 30, 40]"
                            :page-size="page_size"
                            layout="total, sizes, prev, pager, next"
                            :total="after_search_student.length"
                            @current-change="change_current_page"
                            @size-change="change_size_page"
                            @prev-click="change_prev"
                            @next-click="change_next">
                        </el-pagination>
                    </el-row>
                </el-col>
            </el-row>
        </div>
    </div>
</template>

<script>
    import qs from "qs"
    export default {
        data() {
            return {
                //列表展示的字段
                show_table_list: ['学号', '姓名', '院系', '专业', '年级', '班级', '辅导员'],
                //页面高度配置项
                one_second_height: null,
                one_one_button_height: null,

                //查询配置项
                search_student_number: null,
                search_student_name: null,
                search_student_department: null,
                search_student_major: null,
                search_student_grade: null,
                search_student_class: null,

                search_student_department_list: null,
                search_student_major_list: null,
                search_student_grade_list: null,
                search_student_class_list: null,
                //所有的学生信息
                all_student: [],
                //筛选后的数据
                after_search_student: [],
                //当前列表显示的学生信息
                current_student: null,
                //详情页显示的学生信息
                current_select_student_id:null,
                show_detail: false,
                detail_student: null,
                //分页配置
                current_page: 1,
                page_size: 10,
            }
        },
        watch: {
            //监视查询条件
            search_student_class(newVal) {
                this.update_data_depend_search();
            },
            search_student_grade(newVal) {
                this.update_data_depend_search();
            },
            search_student_major(newVal) {
                this.update_data_depend_search();
            },
            search_student_department(newVal) {
                this.update_data_depend_search();
            },
            search_student_name(newVal) {
                this.update_data_depend_search();
            },
            search_student_number(newVal) {
                this.update_data_depend_search();
            },
            //监视当前页码变化
            current_page() {
                this.update_current_user_information_table();
            },
        },
        beforeMount() {
            this.get_all_user_data();
            this.get_all_category();
        },
        mounted() {
            let _me = this;
            this.$nextTick(() => {
                //重写获取数据方式
                this.update_current_user_information_table();
                console.log(this.$refs.one_height)
                let temp_one_height=document.documentElement.clientHeight-60;
                let temp_one_one_height = this.$refs.one_one_height.$el.offsetHeight;
                let temp_one_third_height = this.$refs.one_third_height.$el.offsetHeight;
                _me.one_second_height = temp_one_height - temp_one_one_height - temp_one_third_height;
            })
        },
        computed: {
            loading() {
                if (this.all_student === null || this.all_student.length<=0) {
                    return true
                }
                return false
            },
            //是否显示查询按钮
            show_search_button() {
                if (this.search_identity_card && this.search_identity_card !== "") {
                    return true;
                }
                if (this.search_phone_number && this.search_phone_number !== "") {
                    return true;
                }
                return false;
            },
        },
        methods: {
            //依据当前界面的查询条件，进行查询
            update_data_depend_search() {
                let [...temp_all_data] = this.all_student;
                let num = temp_all_data.length;
                console.log()
                if (num > 0){
                    if (this.search_student_department && this.search_student_department != '' && num > 0) {
                        for (let i = 0; i < num; i++) {
                            if (temp_all_data[i]['department_name'] !== this.search_student_department) {
                                temp_all_data.splice(i, 1);
                                i -= 1;
                                num = temp_all_data.length;
                            }
                        }
                    }
                    num = temp_all_data.length;
                    if (this.search_student_class && this.search_student_class !== '' && num > 0) {
                        for (let i = 0; i < num; i++) {
                            if (temp_all_data[i]['class_name'] !== this.search_student_class) {
                                temp_all_data.splice(i, 1);
                                i -= 1;
                                num = temp_all_data.length;
                            }
                        }
                    }
                    num = temp_all_data.length;
                    if (this.search_student_grade && this.search_student_grade != '' && num > 0) {
                        for (let i = 0; i < temp_all_data.length; i++) {
                            if (temp_all_data[i]['student_grade'] != this.search_student_grade) {
                                temp_all_data.splice(i, 1);
                                i -= 1;
                                num = temp_all_data.length;
                            }
                        }
                    }
                    num = temp_all_data.length;
                    if (this.search_student_major && this.search_student_major != '' && num > 0) {
                        for (let i = 0; i < temp_all_data.length; i++) {
                            if (temp_all_data[i]['major_name'] != this.search_student_major) {
                                temp_all_data.splice(i, 1);
                                i -= 1;
                                num = temp_all_data.length;
                            }
                        }
                    }
                    num = temp_all_data.length;
                    if (this.search_student_name && this.search_student_name !== '' && num > 0) {
                        for (let i = 0; i < temp_all_data.length; i++) {
                            let index = temp_all_data[i]['student_name'].indexOf(this.search_student_name);
                            if (index == -1) {
                                temp_all_data.splice(i, 1);
                                i -= 1;
                                num = temp_all_data.length;
                            }
                        }
                    }
                    num = temp_all_data.length;
                    if (this.search_student_number && this.search_student_number !== '' && num > 0) {
                        for (let i = 0; i < temp_all_data.length; i++) {
                            let index = temp_all_data[i]['student_id'].indexOf(this.search_student_number);
                            if (index == -1) {
                                temp_all_data.splice(i, 1);
                                i -= 1;
                                num = temp_all_data.length;
                            }
                        }
                    }
                    num = temp_all_data.length;
                    this.after_search_student = temp_all_data;
                    this.update_current_user_information_table();
                }
            },
            update_current_user_information_table() {
                if (this.after_search_student !== null) {
                    console.log("执行分页")
                    console.log(this.after_search_student)
                    this.current_student = this.after_search_student.slice((this.current_page - 1) * this.page_size,
                        this.current_page * this.page_size);
                }
                console.log("当前表格数据",this.current_student)
            },
            //分页变化更新
            change_current_page(val) {
                // console.log("当前第页", val);
                this.current_page = val;
                // this.update_current_user_information_table();
            },
            change_size_page(val) {
                // console.log("每页条数据", val);
                this.current_page = 1;
                this.page_size = val;
                this.update_current_user_information_table();
            },
            change_prev(val) {
                this.current_page = val;
                // console.log("上一页，当前第页", val);
                // this.update_current_user_information_table();
            },
            change_next(val) {
                this.current_page = val;
                // console.log("下一页，当前第页", val);
                // this.update_current_user_information_table();
            },

            //获取所有用户的信息
            get_all_user_data() {
                let _me = this;
                _me.axios.get('/api/student/get_all_student_information/')
                    .then((res) => {
                        // console.log(res.data)
                        if (res.data['has_data']) {
                            _me.all_student = res.data['data_list'];
                            _me.update_data_depend_search();
                            console.log("数据更新完毕")
                        } else {
                            _me.all_student = []
                        }
                    }).catch((e) => {
                        console.log("错误信息：", e)
                    });
            },
            //单击列表行，显示详情数据
            show_detail_student(row){
                let _me=this;
                this.current_select_student_id=row.student_id;
                this.axios({
                    method:"get",
                    url:"/api/student/get_current_detail_student/",
                    params:{
                        student_id:this.current_select_student_id
                    }
                }).then((res)=>{
                    if(res.data['has_data']){
                        console.log("详细信息：",res.data['data_list'])
                        _me.detail_student=res.data['data_list'];
                        _me.show_detail=true;
                    }else{
                        _me.$message({
                            type:"error",
                            message:"系统繁忙，请稍后重试！"
                        });
                        _me.detail_student=[];
                    }
                }).catch((e)=>{
                    _me.$message({
                        type:"error",
                        message:"系统繁忙，请稍后重试！"
                    });
                    _me.show_detail=true;
                    console.log(e);
                })
            },
            //获取所有分类
            get_all_category(){
                let _me=this;
                this.axios({
                    method:"get",
                    url:"/api/counselor/get_all_school_information/",
                }).then((res)=>{
                    if(res.data['has_data']){
                        console.log(res.data['data_list'])
                        _me.search_student_class_list=res.data['data_list']['class_list'];
                        _me.search_student_department_list=res.data['data_list']['department_list'];
                        _me.search_student_grade_list=res.data['data_list']['grade_list'];
                        _me.search_student_major_list=res.data['data_list']['major_list'];
                    }
                }).catch((e)=>{
                    console.log(e);
                })
            },
        }
    }
</script>

<style>
    [v-cloak] {
        display: none !important;
    }

    .el-table .warning-row {
        background: oldlace;
    }

    .el-table .success-row {
        background: #f0f9eb;
    }

    .el-table tbody tr:hover>td {
        background-color: #CCCCCC !important
    }

    .el-table__body tr.current-row>td {
        background-color: #CCCCCC !important;

        /* color: #f19944; */
        /* 设置文字颜色，可以选择不设置 */
    }

    .permission-warning {
        color: red;
    }
</style>
