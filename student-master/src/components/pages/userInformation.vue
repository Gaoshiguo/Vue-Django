<template>
    <div ref="sum_height" style="width: 100%;height: 100%;">
        <el-drawer
            append-to-body
            title="学生成绩详细信息"
            :visible.sync="show_detail"
            direction="rtl"
            size="30%">
            <div class="demo-drawer__content">
                <el-row :gutter="10" v-for="(value,key,index) in current_student_current_subject_detail" :key="index" style="border-bottom: 1px #404040;background-color: #ECF5FF;margin-top: 5px;margin-left: 10px;margin-right: 10px;">
                <el-col :class="set_detail_score(key,value)" :span="6" style="height:40px;line-height: 40px;text-align: right;">{{key}}:</el-col>
                <el-col :class="set_detail_score(key,value)" :span="18" style="height:40px;line-height: 40px;padding-left: 10px;">{{value}}</el-col>
            </el-row>
            </div>
        </el-drawer>

        <el-row :gutter="15" style="height: 100%;" v-loading="loading">
            <el-col :span="14" style="height: 100%;">
                <el-card class="box-card">
                    <div slot="header" class="clerafix" style="height: 25px;text-align: left;color: #0086B3;">
                        <i class="el-icon-custom-zuoyeguanli"></i>
                        <span>{{page_show_table_name[0]}}</span>
                        <span style="float: right;">
                            <span>筛选后挂科总人数：{{fail_student_number+" "}}人</span>
                        </span>
                    </div>
                    <div>
                        <el-row :gutter="10">
                            <el-col :span="3" style="height: 80px;line-height: 80px;">查询条件：</el-col>
                            <el-col :span="21">
                                <el-row>
                                    <el-col :span="24">
                                        <el-row :gutter="10">
                                            <el-col :span="6">
                                                <el-select style="width: 100%;" v-model="search_student_department" size="medium"
                                                    clearable placeholder="请选择院系">
                                                    <el-option v-for="item in search_student_department_list" :key="item.department_id"
                                                        :label="item.department_name" :value="item.department_name">
                                                    </el-option>
                                                </el-select>
                                            </el-col>
                                            <el-col :span="6">
                                                <el-select style="width: 100%;" v-model="search_student_major" size="medium"
                                                    clearable placeholder="请选择专业">
                                                    <el-option v-for="item in search_student_major_list" :key="item.major_id" :label="item.major_name"
                                                        :value="item.major_name">
                                                    </el-option>
                                                </el-select>
                                            </el-col>
                                            <el-col :span="6">
                                                <el-select style="width: 100%;" v-model="search_student_grade" size="medium"
                                                    clearable placeholder="请选择年级">
                                                    <el-option v-for="item in search_student_grade_list" :key="item" :label="item"
                                                        :value="item">
                                                    </el-option>
                                                </el-select>
                                            </el-col>
                                            <el-col :span="6">
                                                <el-select style="width: 100%;" v-model="search_student_class" size="medium"
                                                    clearable placeholder="请选择班级">
                                                    <el-option v-for="item in search_student_class_list" :key="item.class_id" :label="item.class_name"
                                                        :value="item.class_name">
                                                    </el-option>
                                                </el-select>
                                            </el-col>
                                        </el-row>
                                        <el-row :gutter="10" style="margin-top: 10px;">
                                            <el-col :span="6">
                                                <el-input v-model="search_student_id" size="medium" clearable placeholder="请输入学号"></el-input>
                                            </el-col>
                                            <el-col :span="6">
                                                <el-input v-model="search_student_name" size="medium" clearable placeholder="请输入姓名"></el-input>
                                            </el-col>
                                        </el-row>
                                    </el-col>
                                </el-row>

                            </el-col>

                        </el-row>
                        <hr />
                        <el-row>
                            <el-col :span="24">
                                <el-table
                                size="small"
                                :height="user_table_height"
                                :data="current_student_list"
                                border :header-cell-style="{background:'#eef1f6',color:'#606266'}"
                                @row-click="get_current_student"
                                :cell-class-name="set_score">
                                    <el-table-column label="学号" align="center" min-width="15%">
                                        <template slot-scope="scope">
                                            <i class="el-icon-s-custom"></i>
                                            <span style="margin-left:5px">
                                                {{scope.row.student_id}}
                                            </span>
                                        </template>
                                    </el-table-column>
                                    <el-table-column label="姓名" align="center" min-width="15%">
                                        <template slot-scope="scope">
                                            <span style="margin-left:5px">
                                                {{scope.row.student_name}}
                                            </span>
                                        </template>
                                    </el-table-column>
                                    <el-table-column label="院系" align="center" show-overflow-tooltip min-width="15%">
                                        <template slot-scope="scope">
                                            <span style="margin-left:5px">
                                                {{scope.row.department_name}}
                                            </span>
                                        </template>
                                    </el-table-column>
                                    <el-table-column label="专业" align="center" show-overflow-tooltip min-width="15%">
                                        <template slot-scope="scope">
                                            <span style="margin-left:5px">
                                                {{scope.row.major_name}}
                                            </span>
                                        </template>
                                    </el-table-column>
                                    <el-table-column label="年级" align="center" min-width="15%">
                                        <template slot-scope="scope">
                                            <span style="margin-left:5px">
                                                {{scope.row.student_grade}}
                                            </span>
                                        </template>
                                    </el-table-column>
                                    <el-table-column label="班级" align="center" min-width="15%">
                                        <template slot-scope="scope">
                                            <span style="margin-left:5px">
                                                {{scope.row.class_name}}
                                            </span>
                                        </template>
                                    </el-table-column>
                                    <el-table-column label="挂科" align="center" min-width="10%">
                                        <template slot-scope="scope">
                                            <span style="margin-left:5px">
                                                {{scope.row.is_failed}}
                                            </span>
                                        </template>
                                    </el-table-column>
                                </el-table>
                            </el-col>
                        </el-row>
                    </div>
                    <el-pagination
                        style="margin-top: 5px;"
                        background
                        :current-page="current_page"
                        :page-sizes="[5,10, 20, 30, 40]"
                        :page-size="page_size"
                        :pager-count="5"
                        layout="total, sizes, prev, pager, next"
                        :total="after_search_student_list.length"
                        @current-change="change_current_page"
                        @size-change="change_size_page"
                        @prev-click="change_prev"
                        @next-click="change_next">
                    </el-pagination>
                </el-card>
            </el-col>
            <el-col :span="10">
                <el-row :gutter="15">
                    <el-col :span="24">
                        <el-card class="box-card">
                            <div slot="header" class="clearfix" style="text-align: left;height: 25px;color: #2E8B57;">
                                <i class="el-icon-custom-zuoyeguanli"></i>
                                <span>{{page_show_table_name[1]}}</span>
                                <span style="float: right;">学号：{{current_student_id==null?'尚未选择':current_student_id}}</span>
                            </div>
                            <div>
                                <div>
                                    <el-table size="small" :height="history_score_height"
                                    border
                                    :data="current_student_subject"
                                    :header-cell-style="{background:'#eef1f6',color:'#606266'}"
                                    :row-class-name="set_current_all_score_class"
                                    @row-click="get_current_student_current_subject">
                                        <el-table-column show-overflow-tooltip label="课程名称" align="center">
                                            <template slot-scope="scope">
                                                <i class="el-icon-custom-category"></i>
                                                <span>{{scope.row.course_name}}</span>
                                            </template>
                                        </el-table-column>
                                        <el-table-column  label="课程学分" align="center">
                                            <template slot-scope="scope">
                                                <span>{{scope.row.course_grade}}</span>
                                            </template>
                                        </el-table-column>
                                        <el-table-column label="所得学分" align="center">
                                            <template slot-scope="scope">
                                                <span>{{scope.row.get_grade}}</span>
                                            </template>
                                        </el-table-column>
                                        <el-table-column label="综合成绩" align="center">
                                            <template slot-scope="scope">
                                                <span>{{scope.row.overall_score}}</span>
                                            </template>
                                        </el-table-column>
                                    </el-table>
                                    <el-row style="border: 1px solid #969896;margin-top: 7px;color: red;">
                                        <el-row>
                                        <el-col :span="6" style="height: 30px;line-height: 30px;text-align: right;">
                                            挂科数目：
                                        </el-col>
                                        <el-col :span="6" style="height: 30px;line-height: 30px;">
                                            {{fail_current_student_subject === 0?'无':fail_current_student_subject}}
                                        </el-col>
                                        <el-col v-if="fail_current_student_subject > 0" :span="2" style="text-align: left;">
                                            门
                                        </el-col>
                                    </el-row>
                                    <el-row>
                                        <el-col :span="6" style="height: 30px;line-height: 30px;text-align: right;">
                                            挂科总学分：
                                        </el-col>
                                        <el-col :span="6" style="height: 30px;line-height: 30px;">
                                            {{fail_current_student_grade === 0?'无':fail_current_student_grade}}
                                        </el-col>
                                        <el-col v-if="fail_current_student_grade > 0" :span="2" style="text-align: left;">学分</el-col>
                                    </el-row>
                                    </el-row>

                                </div>
                            </div>
                        </el-card>
                    </el-col>
                </el-row>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                //表格高度
                history_score_height:null,
                //抽屉开关
                show_detail:false,
                //表格高度
                user_table_height:null,
                //分页配置
                current_page:1,
                page_size:10,
                //页面显示的表格的标题
                page_show_table_name: ['学生信息', '课程成绩'],
                //查找条件绑定
                search_student_id:null,
                search_student_name:null,
                search_student_department:null,
                search_student_major:null,
                search_student_grade:null,
                search_student_class:null,

                search_student_department_list:[],
                search_student_major_list:[],
                search_student_grade_list:[],
                search_student_class_list:[],
                //列表
                all_student_list:[],
                after_search_student_list:[],
                current_student_list:[],
                //当前学生的所有成绩
                current_student_subject:[],
                //当前学生的当前课程的详细情况
                current_student_current_subject_detail:{},
                //选择的学生的学号
                current_student_id:null,
                //选择的学生的课程号
                current_course_id:null,
            }
        },
        computed:{
            loading(){
                if (this.all_student_list === null || this.all_student_list.length === 0){
                    return true
                }
                return false;
            },
            //挂科总人数
            fail_student_number(){
                let result=0;
                let num=this.after_search_student_list.length;
                for (let i=0;i<num;i++){
                    if(this.after_search_student_list[i]['is_failed'] === "是"){
                        result+=1;
                    }
                }
                return result;
            },
            //当前学生挂科总科目
            fail_current_student_subject(){
                let result=0;
                let num=this.current_student_subject.length;
                for(let i=0;i<num;i++){
                    if(this.current_student_subject[i]['overall_score']<60){
                        result+=1;
                    }
                }
                return result;
            },
            //当前学生挂科的总学分
            fail_current_student_grade(){
                let result=0;
                let num=this.current_student_subject.length;
                for(let i=0;i<num;i++){
                    if(this.current_student_subject[i]['is_failed']==="是"){
                        result+=parseFloat(this.current_student_subject[i]['course_grade'],10);
                    }
                }
                return result;
            },
        },
        beforeMount() {
            this.get_all_student_information();
            this.get_all_category();
        },
        mounted() {
            this.$nextTick(()=>{
                // console.log(this.$refs.sum_height.$el.offsetHeight)
                let temp=document.documentElement.clientHeight;
                console.log("总高：",temp)
                this.user_table_height=temp-332;
                this.history_score_height=temp-265;
            })
        },
        watch:{
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
            search_student_id(newVal) {
                this.update_data_depend_search();
            },
            //监视当前页码变化
            current_page() {
                this.update_current_user_information_table();
            },
        },
        methods: {
            //设置详情里分数及挂科颜色
            set_detail_score(key,value){
                if(key === "综合成绩" ){
                    if(value <60){
                        return "detail-score-not-pass"
                    }else{
                        return "detail-score-pass"
                    }
                }
                if(key === "是否挂科"){
                    if(value === "是"){
                        return "detail-score-not-pass"
                    }else{
                        return "detail-score-pass"
                    }
                }
            },
            //设置分数颜色
            set_score(data){
                // console.log(data)
                if(data.column.label === "学号" || data.column.label === "挂科"){
                    if(data.row.is_failed === "是"){
                        // console.log("挂科")
                        return "score-not-pass"
                    }else{
                        return "score-pass"
                    }

                }
            },
            set_current_all_score_class(data){
                // console.log(data)
                if(data.row.is_failed === "是"){
                    return "all-score-not-pass"
                }
            },

            //选择学生,尚未完善
            get_current_student(row){
                this.current_student_id=row.student_id;
                let _me=this;
                this.axios({
                    method:"get",
                    url:"/api/course/get_current_student_score/",
                    params:{
                        student_id:_me.current_student_id
                    }
                }).then((res)=>{
                    console.log(res.data)
                    if(res.data['has_data']==="success"){
                        _me.current_student_subject = res.data['data_list']
                    }else if(res.data['has_data']==="error"){
                        _me.$message({
                            type:"error",
                            message:"系统出错,请稍后重试！"
                        })
                        _me.current_student_id=null;
                    }else{
                        _me.$message({
                            type:"error",
                            message:"该学生暂无考试成绩！"
                        })
                        _me.current_student_id=null;
                    }
                }).catch((e)=>{
                    _me.current_student_id=null;
                    _me.$message({
                        type:"error",
                        message:"系统繁忙，请稍后重试！"
                    })
                })
            },

            //获取所有学生的信息
            get_all_student_information(){
                let _me = this;
                _me.axios.get('/api/student/get_all_student_information/')
                    .then((res) => {
                        // console.log(res.data)
                        if (res.data['has_data']) {
                            _me.all_student_list = res.data['data_list'];
                            _me.update_data_depend_search();
                            console.log("数据更新完毕")
                        } else {
                            _me.all_student_list = []
                        }
                    }).catch((e) => {
                        console.log("错误信息：", e)
                    });
            },
            //获取单个学生的单个成绩
            get_current_student_current_subject(row){
                this.current_course_id=row.course_id;
                let _me=this;
                this.axios({
                    method:"get",
                    url:"/api/course/get_current_student_detail_score/",
                    params:{
                        student_id:_me.current_student_id,
                        course_id:_me.current_course_id,
                    }
                }).then((res)=>{
                    if(res.data['has_data']){
                        //返回值为字典
                        _me.current_student_current_subject_detail=res.data['data_list'];
                        console.log(_me.current_student_current_subject_detail)
                        _me.show_detail=true;
                    }else{
                        _me.$message({
                            type:"error",
                            message:"系统出错,请稍后重试！"
                        })
                        _me.current_course_id=null;
                    }
                }).catch((e)=>{
                    _me.current_course_id=null;
                    _me.$message({
                        type:"error",
                        message:"系统繁忙，请稍后重试！"
                    })
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
                        _me.search_student_class_list=res.data['data_list']['class_list'];
                        _me.search_student_department_list=res.data['data_list']['department_list'];
                        _me.search_student_grade_list=res.data['data_list']['grade_list'];
                        _me.search_student_major_list=res.data['data_list']['major_list'];
                    }
                }).catch((e)=>{
                    console.log(e);
                })
            },
            //筛选数据
            update_data_depend_search(){
                let [...temp_all_data] = this.all_student_list;
                let num = temp_all_data.length;

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
                    if (this.search_student_id && this.search_student_id !== '' && num > 0) {
                        for (let i = 0; i < temp_all_data.length; i++) {
                            let index = temp_all_data[i]['student_id'].indexOf(this.search_student_id);
                            if (index == -1) {
                                temp_all_data.splice(i, 1);
                                i -= 1;
                                num = temp_all_data.length;
                            }
                        }
                    }
                    num = temp_all_data.length;
                    this.after_search_student_list = temp_all_data;
                    this.update_current_user_information_table();
                }
            },
            //按照分页，更新当前表格
            update_current_user_information_table(){
                if(this.after_search_student_list !==null){
                    this.current_student_list = this.after_search_student_list.slice((this.current_page - 1) * this.page_size,
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

    .score-perfect {
        color: cornflowerblue;
    }

    .score-good {
        color: #EE9900;
    }

    .score-pass {
        color: green;
    }

    .score-not-pass {
        color:red;
    }

    .detail-score-not-pass{
        color: red;
    }

    .detail-score-pass{
        color: green;
    }

    .el-table .all-score-not-pass {
        background-color:blanchedalmond;
    }
</style>
