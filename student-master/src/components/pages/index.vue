<template>
    <div style="width: 100%;height: 100%;">

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


        <div style="width: 100%;height: 100%;">
            <el-row :gutter="15">
                <el-col :span="6">
                    <el-card class="box-card" shadow="hover" style="background-color: #FFFFFF;">
                        <el-row :gutter="5" style="height: 80px;">
                            <el-col :span="12">
                                <i class="el-icon-custom-zhangdanguanli" style="font-size:80px;color: seagreen;"></i>
                            </el-col>
                            <el-col :span="12">
                                <el-row>
                                    <el-col :span="24" style="height: 30px;line-height: 30px;margin-top: 10px;">
                                        年级：
                                    </el-col>
                                </el-row>
                                <el-row>
                                    <el-col :span="24" style="height: 30px;line-height: 30px;margin-bottom: 10px;">
                                        {{grade_num+" "}}届
                                    </el-col>
                                </el-row>
                            </el-col>
                        </el-row>
                    </el-card>
                </el-col>
                <el-col :span="6">
                    <el-card class="box-card" shadow="hover" style="background-color: #FFFFFF;">
                        <el-row :gutter="5" style="height: 80px;">
                            <el-col :span="12">
                                <i class="el-icon-custom-wenjianguanli" style="font-size:80px;color: #6AB0B8;"></i>
                            </el-col>
                            <el-col :span="12">
                                <el-row>
                                    <el-col :span="24" style="height: 30px;line-height: 30px;margin-top: 10px;">
                                        班级：
                                    </el-col>
                                </el-row>
                                <el-row>
                                    <el-col :span="24" style="height: 30px;line-height: 30px;margin-bottom: 10px;">
                                        {{class_num+" "}}个
                                    </el-col>
                                </el-row>
                            </el-col>
                        </el-row>
                    </el-card>
                </el-col>
                <el-col :span="6">
                    <el-card class="box-card" shadow="hover" style="background-color: #FFFFFF;">
                        <el-row :gutter="5" style="height: 80px;">
                            <el-col :span="12">
                                <i class="el-icon-custom-yonghu" style="font-size:80px;color: #66B1FF;"></i>
                            </el-col>
                            <el-col :span="12">
                                <el-row>
                                    <el-col :span="24" style="height: 30px;line-height: 30px;margin-top: 10px;">
                                        学生人数：
                                    </el-col>
                                </el-row>
                                <el-row>
                                    <el-col :span="24" style="height: 30px;line-height: 30px;margin-bottom: 10px;">
                                        {{student_num+" "}}人
                                    </el-col>
                                </el-row>
                            </el-col>
                        </el-row>
                    </el-card>
                </el-col>
                <el-col :span="6">
                    <el-card class="box-card" shadow="hover" style="background-color: #FFFFFF;">
                        <el-row :gutter="5" style="height: 80px;">
                            <el-col :span="12">
                                <i class="el-icon-custom-zuoyeguanli" style="font-size:80px;color: #F17F42;"></i>
                            </el-col>
                            <el-col :span="12">
                                <el-row>
                                    <el-col :span="24" style="height: 30px;line-height: 30px;margin-top: 10px;">
                                        课程总量：
                                    </el-col>
                                </el-row>
                                <el-row>
                                    <el-col :span="24" style="height: 30px;line-height: 30px;margin-bottom: 10px;padding-left: 15px;">
                                        {{course_num+' '}}门
                                    </el-col>
                                </el-row>
                            </el-col>
                        </el-row>
                    </el-card>
                </el-col>
            </el-row>
            <el-row style="margin-top: 10px;">
                <el-col :span="24">
                    <el-card class="box-card">
                        <div slot="header" class="clearfix" style="height: 25px; text-align: left;color: #66B1FF;margin-bottom: 10px;">
                            <i class="el-icon-custom-yonghu"></i>
                            <span style="margin-left: 5px;">挂科人数分布</span>
                            <span style="float: right;">
                                <span style="color: #333333;">查询条件:</span>
                                <span style="margin-left: 5px;">
                                    <el-select clearable style="width: 150px;" v-model="search_student_department" placeholder="院系">
                                        <el-option v-for="item in search_student_department_list" :key="item.department_id"
                                            :value="item.department_id"
                                            :label="item.department_name"></el-option>
                                    </el-select>
                                </span>
                                <span style="margin-left: 5px;">
                                    <el-select clearable style="width: 150px;" v-model="search_student_major" placeholder="专业">
                                        <el-option v-for="item in search_student_major_list" :key="item.major_id"
                                            :value="item.major_id"
                                            :label="item.major_name"></el-option>
                                    </el-select>
                                </span>
                                <span style="margin-left: 5px;">
                                    <el-select clearable style="width: 150px;" v-model="search_student_grade" placeholder="年级">
                                        <el-option v-for="item in search_student_grade_list" :key="item" :value="item"
                                            :label="item"></el-option>
                                    </el-select>
                                </span>
                                <span style="margin-left: 5px;">
                                    <el-select clearable style="width: 150px;" v-model="search_student_class" placeholder="班级">
                                        <el-option v-for="item in search_student_class_list" :key="item.class_id" :value="item.class_id"
                                            :label="item.class_name"></el-option>
                                    </el-select>
                                </span>
                                <span style="margin-left: 5px;">
                                    <el-button type="primary" icon="el-icon-search" @click="get_current_chart_data">查询</el-button>
                                </span>
                            </span>
                        </div>
                        <div>
                            <el-row :gutter="25">
                                <el-col :span="13" style="padding: 10px 10px;"  v-loading="loading">
                                    <span v-if="chart_option===null || chart_option.length <=0" :style="{'height':chart_height+'px','line-height':chart_height+'px'}">
                                        暂无数据！
                                    </span>
                                    <v-chart v-else :style="{'width': '100%','height':chart_height+'px'}" :options="chart_option"
                                        auto-resize manual-update @click="get_current_student_table">
                                    </v-chart>
                                </el-col>
                                <el-col :span="11" v-loading="table_loading">
                                    <el-row :gutter="3">
                                        <el-col :span="3" style="height: 10px;line-height: 10px;margin-top: 5px;margin-bottom:15px;font-size: 10px;color: red;">等级划分:</el-col>
                                        <el-col :span="1" style="display: inline;">
                                            <div style="width: 100%; height: 10px;margin-top: 5px;background-color: green;float: right;"></div>
                                        </el-col>
                                        <el-col :span="4" style="text-align: left;">
                                            <span style="height: 10px;line-height: 10px;margin-top: 5px;margin-bottom:15px;font-size: 10px;">无等级(0学分)</span>
                                        </el-col>
                                        <el-col :span="1" style="display: inline;">
                                            <div style="width: 100%; height: 10px;margin-top: 5px;background-color: yellowgreen;float: right;"></div>
                                        </el-col>
                                        <el-col :span="4" style="text-align: left;">
                                            <span style="height: 10px;line-height: 10px;margin-top: 5px;margin-bottom:15px;font-size: 10px;">一级(0-3学分)</span>
                                        </el-col>
                                        <el-col :span="1" style="display: inline;">
                                            <div style="width: 100%; height: 10px;margin-top: 5px;background-color: orange;float: right;"></div>
                                        </el-col>
                                        <el-col :span="4" style="text-align: left;">
                                            <span style="height: 10px;line-height: 10px;margin-top: 5px;margin-bottom:15px;font-size: 10px;">二级(3-10学分)</span>
                                        </el-col>
                                        <el-col :span="1" style="display: inline;">
                                            <div style="width: 100%; height: 10px;margin-top: 5px;background-color: red;float: right;"></div>
                                        </el-col>
                                        <el-col :span="5" style="text-align: left;">
                                            <span style="height: 10px;line-height: 10px;margin-top: 5px;margin-bottom:15px;font-size: 10px;">三级(10学分以上)</span>
                                        </el-col>
                                    </el-row>
                                    <el-table
                                    size="small"
                                    border
                                    :data="current_student_list"
                                    :height="table_hieght"
                                    :header-cell-style="{background:'#eef1f6',color:'#606266'}"
                                    :cell-class-name="set_rank_class"
                                    @row-click="show_detail_student">>
                                        <el-table-column type="index" align="center"></el-table-column>
                                        <el-table-column label="学号" align="center">
                                            <i class="el-icon-custom-Idcard"></i>
                                            <template slot-scope="scope">
                                                <span>{{scope.row.student_id}}</span>
                                            </template>
                                        </el-table-column>
                                        <el-table-column label="姓名" align="center">
                                            <i class="el-icon-s-custom"></i>
                                            <template slot-scope="scope">
                                                <span>{{scope.row.student_name}}</span>
                                            </template>
                                        </el-table-column>
                                        <el-table-column label="挂科总学分" align="center">
                                            <template slot-scope="scope">
                                                <span>{{current_sum_score}}</span>
                                            </template>
                                        </el-table-column>
                                        <el-table-column label="挂科等级" align="center">
                                            <template slot-scope="scope">
                                                <span>{{set_rank()}}</span>
                                            </template>
                                        </el-table-column>
                                    </el-table>
                                    <el-pagination
                                    style="margin-top: 15px;"
                                    background
                                    :current-page="current_page"
                                    :page-sizes="[5,10, 20, 30, 40]"
                                    :page-size="page_size" :pager-count="5" layout="total, sizes, prev, pager, next"
                                    :total="all_student_list===null ? 0:all_student_list.length"
                                    @current-change="change_current_page"
                                    @size-change="change_size_page"
                                    @prev-click="change_prev"
                                    @next-click="change_next">
                                    </el-pagination>
                                </el-col>
                            </el-row>
                        </div>
                    </el-card>
                </el-col>
            </el-row>
        </div>
    </div>
</template>

<script>
    import qs from 'qs';
    export default {
        data() {
            return {
                //定义高度
                chart_height: null,
                table_hieght: null,
                //分页配置
                current_page: 1,
                page_size: 10,
                //绑定的查询信息
                search_student_department: null,
                search_student_major: null,
                search_student_grade: null,
                search_student_class: null,
                search_student_department_list: [],
                search_student_major_list: [],
                search_student_grade_list: [],
                search_student_class_list: [],
                //页面顶端显示数据
                student_num: null,
                course_num: null,
                //绑定图表
                chart_option: null,
                chart_data:null,
                //列表
                all_student_list:[],
                after_search_student_list:[],
                current_student_list:[],
                //右侧列表展示
                current_sum_score:null,
                //定义挂科等级
                failed_rank:['无','一级','二级','三级'],
                //抽屉数据
                show_detail:false,
                detail_student:null,
            }
        },
        computed:{
            //图表加载
            loading(){
                if(this.chart_option === null){
                    return true;
                }
                return false;
            },
            //表格加载
            table_loading(){
                if(this.all_student_list === null){
                    return true;
                }
                return false;
            },
            grade_num(){
                return this.search_student_grade_list.length;
            },
            class_num(){
                return this.search_student_class_list.length;
            },
        },
        watch:{
            current_page() {
                this.update_current_user_information_table();
            },
        },
        beforeMount() {
            this.get_all_category();
            this.get_current_chart_data();
            this.get_header_data();
        },
        mounted() {
            this.$nextTick(() => {
                let temp_sum_heihgt = document.documentElement.clientHeight;
                this.chart_height = temp_sum_heihgt - 340;
                this.table_hieght = this.chart_height - 62;
            })
        },
        methods: {

            //获取所有分类
            get_all_category() {
                let _me = this;
                this.axios({
                    method: "get",
                    url: "/api/counselor/get_all_school_information/",
                }).then((res) => {
                    if (res.data['has_data']) {
                        _me.search_student_class_list = res.data['data_list']['class_list'];
                        _me.search_student_department_list = res.data['data_list']['department_list'];
                        _me.search_student_grade_list = res.data['data_list']['grade_list'];
                        _me.search_student_major_list = res.data['data_list']['major_list'];
                    }
                }).catch((e) => {
                    console.log(e);
                })
            },
            //获取图表
            get_current_chart_data(){
                this.chart_option=null;
                let _me=this;
                this.axios({
                    method:"get",
                    url:"/api/student/get_student_score_chart/",
                    params:{
                        student_grade:_me.search_student_grade,
                        department_id:_me.search_student_department,
                        class_id:_me.search_student_class,
                        major_id:_me.search_student_major
                    }
                }).then((res)=>{
                    // console.log(res.data)
                    if(res.data['has_data']){
                        _me.chart_option=JSON.parse(res.data['chart_option']);
                        _me.chart_data=res.data['chart_data'];
                    }else{
                        _me.chart_option=[]
                    }
                }).catch((e)=>{
                    console.log(e)
                })
            },
            //获取表格
            get_current_student_table(data){
                if(data.componentType==="series"){
                    this.all_student_list=null;
                    console.log(data)
                    this.current_sum_score=parseInt(data.name,10);
                    let _me=this;
                    let temp_data=this.chart_data[data.name]
                    // console.log(temp_data)
                    let return_data={
                        student_id:JSON.stringify(temp_data)
                    }
                    this.axios({
                        method: "post",
                        headers: {
                            'Content-Type': 'application/x-www-form-urlencoded',
                        },
                        url: '/api/student/get_student_depend_score/',
                        data: qs.stringify(return_data),
                    }).then((res)=>{
                        console.log(res.data)
                        if(res.data['has_data']){
                            _me.all_student_list=res.data['data_list']
                            _me.update_current_user_information_table()
                        }else{
                            _me.$message({
                                type:"error",
                                message:"系统繁忙，请稍后重试！"
                            })
                        }
                    }).catch((e)=>{
                        console.log(e);
                        _me.$message({
                            type:"error",
                            message:"系统繁忙，请稍后重试！"
                        })
                    })
                }
            },
            //划分等级，0  0-3  3-10  10以上
            set_rank(){
                let num=parseInt(this.current_sum_score,10);
                if(num===0){
                    return this.failed_rank[0];
                }
                if(num>0 && num<=3){
                    return this.failed_rank[1];
                }
                if(num > 3 && num <= 10){
                    return this.failed_rank[2];
                }
                if(num>10){
                    return this.failed_rank[3];
                }
            },
            set_rank_class(data){
                // console.log(data)
                let num=parseInt(this.current_sum_score,10);
                if(data.column.label==="挂科等级" || data.column.label==="挂科总学分"){
                    if(this.current_sum_score !== null){
                        if(num === 0){
                            return "score-green"
                        }
                        if(num>0 && num<=3){
                            return "score-orange"
                        }
                        if(num > 3 && num <= 10){
                            return "score-orangered"
                        }
                        if(num>10){
                            return "score-red"
                        }
                    }
                }
            },

            get_header_data(){
                let _me=this;
                this.axios.get('/api/student/get_student_number/').then((res)=>{
                    _me.student_num=res.data;
                })
                this.axios.get('/api/course/get_course_number/').then((res)=>{
                    _me.course_num=res.data;
                })
            },
            //单击列表行，显示详情数据
            show_detail_student(row){
                let _me=this;
                this.axios({
                    method:"get",
                    url:"/api/student/get_current_detail_student/",
                    params:{
                        student_id:row.student_id,
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


            //按照分页，更新当前表格
            update_current_user_information_table(){
                if(this.all_student_list !==null){
                    this.current_student_list = this.all_student_list.slice((this.current_page - 1) * this.page_size,
                    this.current_page * this.page_size);
                }
            },
            //分页变化更新
            change_current_page(val) {
                this.current_page = val;
            },
            change_size_page(val) {
                this.current_page = 1;
                this.page_size = val;
                this.update_current_user_information_table();
            },
            change_prev(val) {
                this.current_page = val;
            },
            change_next(val) {
                this.current_page = val;
            },
        },
    }
</script>

<style>
    .score-green{
        color: green;
    }
    .score-orange{
        color:yellowgreen;
    }
    .score-orangered{
        color: orange;
    }
    .score-red{
        color: red;
    }
</style>
