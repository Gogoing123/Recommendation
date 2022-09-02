<template>
  <section class="add">
    <el-form ref="form" :model="form" label-width="100px">
      <el-page-header @back="goBack" content="推荐系统">
      </el-page-header>
    <!-- <h2>信息收集工具</h2> -->
    <el-main>
    <el-form-item>
       <button @click='getResult()' v-trigger>推荐痕迹清除方法</button>
      <!-- <el-button type="primary" @click="getResult();">点击事件</el-button> -->
    </el-form-item>
     <!-- <el-input type="textarea" v-model="form.toolname"></el-input> -->
     <el-form-item >
      系统类型
      <el-input type="textarea" v-model="form.test[form.index]"></el-input>
      id
      <el-input type="textarea" v-model="form.test[form.index+1]"></el-input>
      目标
      <el-input type="textarea" v-model="form.test[form.index+2]"></el-input>
      方法
      <el-input type="textarea" v-model="form.test[form.index+3]"></el-input>
  
        期望结果
      <el-input type="textarea" v-model="form.result"></el-input>
        数据来源
      <el-input type="textarea" v-model="form.desc"></el-input>
      <!-- <el-button type="primary" @click="goBack()">返回工具列表</el-button> -->
      <!-- <el-button type="primary" @click="flash1()">上一页</el-button> -->
      <!-- <el-button type="primary" @click="flash()">下一页</el-button> -->
      <!-- <el-button type="primary" @click="next()">进行漏洞扫描</el-button> -->
    </el-form-item>
 
    </el-main>
    </el-form>
     <!-- <div><img src="\images\01.png" alt=""></div> -->
      <!-- <el-button type="button" @click="getResult()">获取</el-button> -->
      <!-- <p>{{form.test}}</p> -->

    <!-- <div v-else>
      Not sorry
    </div> -->
      <!-- <div>{{form.tactics}}</div> -->
      <section class="img">
    <!-- <el-input type="textarea" v-model="form.toolname"></el-input>   -->
    <!-- <el-input type="textarea">示例</el-input> -->
    <!-- <div>工具使用示例</div> -->
    <div v-if="form.toolname=='仅清理当前用户'">
     <img src="\images\history -c.png" alt="">
    </div>
    <div v-if="form.toolname=='使系统不再保存命令记录'">
     <img src="\images\profile.png" alt="">

    </div>
    <div v-if="form.toolname=='删除登录失败记录'">
     <img src="\images\btmp.png" alt="">
    </div>
    <div v-if="form.toolname=='删除日志记录'">
     <img src="\images\secure.png" alt="">
    </div>
    <div v-if="form.toolname=='删除登录成功记录'">
     <img src="\images\wtmp.png" alt="">
    </div>
        <el-button type="primary" @click="open()">具体操作方法</el-button>
  </section>
  <!-- <section class="img2"> -->
    <!-- <div>漏洞扫描内容</div> -->
    <!-- <el-input type="textarea" v-model="form.toolname"></el-input>   -->
    <!-- <el-input type="textarea">示例</el-input> -->
    <!-- <div> -->
     <!-- <img src="\images\漏洞扫描内容.png" alt=""> -->
    <!-- </div> -->
  <!-- </section> -->
  </section>
</template>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>


<script>



export default {
  data() {
    return {
      form: { //表单数据初始化
        tactics: '端口扫描',
        desc: 'neo4j',
        test:'test',
        toolname:this.$route.query.name,
        // toolname1:'注入',
        result:'删除目标文件',
        index:0
      },
       showClass: false  
    };
  },
    directives:{
    trigger:{
     inserted(el,binging){
        el.click()
       //$(el).trigger('click')
      }
   }
    },
  methods: {
    next(){
    this.$router.push({path: '/Recommended vulnerability scanning methods'})
    },
      open(){
        if(this.$route.query.name=='仅清理当前用户'){
           window.open("https://blog.csdn.net/a772304419/article/details/121691048", "_blank");}
        if(this.$route.query.name=='使系统不再保存命令记录') {
           window.open("https://zhidao.baidu.com/question/121463086.html", "_blank");}
        if(this.$route.query.name=='删除登录失败记录') {
           window.open("https://www.cnblogs.com/renhaoblog/p/13667746.html ", "_blank");}
        if(this.$route.query.name=='删除登录成功记录') {
           window.open("https://www.cnblogs.com/renhaoblog/p/13667746.html ", "_blank");}
           if(this.$route.query.name=='删除日志记录') {
           window.open("https://www.cnblogs.com/renhaoblog/p/13667746.html ", "_blank");}
          
      // else{
      //   alert('没有了');
      // }
    },

    flash(){
      if (this.form.index<this.form.test.length-4){
      this.form.index=this.form.index+2;}
      else{
        alert('没有了');
      }
    },
    flash1(){
      if (this.form.index<this.form.test.length-3){
      this.form.index=this.form.index-2;}
      else{
        alert('没有了');
      }
    },
    goBack(){
        this.$router.back()
    },
    getResult:function() {
        var _this = this
        _this.$axios.get('http://127.0.0.1:5000/api/hjs/?name='+_this.form.toolname).then
        (function(resp){
          console.log(resp.data.result);
          _this.form.test=resp.data.result;
        },
        function(err){})
    },
    onSubmit() {
      let examDate = this.formatTime(this.form.examDate)
      this.form.examDate = examDate.substr(0,10)
      this.$axios(`/api/examManagePaperId`).then(res => {
        this.form.paperId = res.data.data.paperId + 1 
        this.$axios({
          url: '/api/exam',
          method: 'post', 
          data: {
            ...this.form
          }
        }).then(res => {
          if(res.data.code == 200) {
            this.$message({
              message: '数据添加成功',
              type: 'success'
            })
            this.$router.push({path: '/selectExam'})
          }
        })
      })
    },
    
  }
};
</script>

<style>
.add {
  padding: 0px 40px;
  width: 600px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
  height:800px;
  position: absolute;
  left: 50%;
  top:55%;
  transform: translate(-50%,-50%);

}
</style>

<style>
.img {
  padding: 0px 40px;
  width: 400px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
  height:600px;
  position: absolute;
  left: 100%;
  top:10%;
  transform: translate(0%,-10%);

}
.img2 {
  padding: 0px 40px;
  width: 300px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
  height:200px;
  position: absolute;
  left: -65%;
  top:20%;
  transform: translate(0%,0%);

}
</style>