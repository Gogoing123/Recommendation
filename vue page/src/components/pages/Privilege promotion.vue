<template>
  <section class="add">
    <el-form ref="form" :model="form" label-width="100px">
      <el-page-header @back="goBack" content="推荐系统">
      </el-page-header>
    <!-- <h2>推荐信息收集工具</h2> -->
    <el-main>
 
    <el-form-item>
        <button @click='getResult()' v-trigger>推荐权限提升方法</button>
      
    </el-form-item>
    <div>
    <a :href="'http://localhost:8080/#/Privilege promotion func?name='+form.test[form.index]">{{form.test[form.index].substr(0,15)}}</a>
  </div>
  <h>
   ------------------------------------------
  </h>
  <div>
    <a :href="'http://localhost:8080/#/Privilege promotion func?name='+form.test[form.index+1]">{{form.test[form.index+1].substr(0,15)}}</a>
  </div>
   <h>
   ------------------------------------------
  </h>
  <div>
    <a :href="'http://localhost:8080/#/Privilege promotion func?name='+form.test[form.index+2]">{{form.test[form.index+2].substr(0,15)}}</a>
  </div>
   <h>
   ------------------------------------------
  </h>
  <div>
    <a :href="'http://localhost:8080/#/Privilege promotion func?name='+form.test[form.index+3]">{{form.test[form.index+3].substr(0,15)}}</a>
  </div>
  <h>
   ------------------------------------------
  </h>
  <div>
    <a :href="'http://localhost:8080/#/Privilege promotion func?name='+form.test[form.index+4]">{{form.test[form.index+4]}}</a>
  </div>
    <h>
   ------------------------------------------
  </h>
<el-form-item>
    <el-button type="primary" @click="first()">返回</el-button>
    <el-button type="primary" @click="flashs1()">上一页</el-button>
    <el-button type="primary" @click="flashs()">下一页</el-button>
      
    </el-form-item>
    </el-main>
    </el-form>
     <!-- <div><img src="\images\01.png" alt=""></div> -->
      <!-- <el-button type="button" @click="getResult()">获取</el-button> -->
      <!-- <p>{{form.test}}</p> -->
      <!-- <p>{{test1}}</p> -->
      <!-- <div>{{form.tactics}}</div> -->
  </section>


</template>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>


<script>



export default {
  data() {
    return {
      form: { //表单数据初始化
        tactics: null,
        desc: '111',
        test:'test',
         toolname:this.$route.query.name,
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
    first(){
    this.$router.push({path: '/Collection Choice'})
    },
    tool(){
    this.$router.push({path: '/GetInformationTool'})
    },
    flashs(){
      if (this.form.index<this.form.test.length-3){
      this.form.index=this.form.index+4;}
      else{
        alert('没有了');
      }
    },
      flashs1(){
      if (this.form.index<this.form.test.length-3){
      this.form.index=this.form.index-4;}
      else{
        alert('没有了');
      }
    },
    flash(){
      if (this.form.index<this.form.test.length-1){
      this.form.index++;}
      else{
        alert('没有了');
      }
    },
    goBack(){
        this.$router.back()
    },
    getResult:function() {
        var _this = this
        _this.$axios.get('http://127.0.0.1:5000/api/tq/?name='+_this.form.toolname).then
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

