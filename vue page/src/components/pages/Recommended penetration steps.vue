<template>
  <section class="add">
    <el-form ref="form" :model="form" label-width="100px">
      <el-page-header @back="goBack" content="推荐系统">
      </el-page-header>
    <h2>推荐渗透攻击方法</h2>
    <el-main>
      <el-form-item label="信息"> 收集到的漏洞信息，如漏洞编号，漏洞类型
        <el-input v-model="form.tactics"></el-input>
      </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="goBack()">上一步</el-button>

      <!-- <el-button type="primary" :href="'http://localhost:8080/#/Recommended penetration steps func?name='+form.tactics">推荐渗透攻击方法</el-button> -->
      <el-button type="primary" @click="TJ()">推荐渗透攻击方法</el-button>

      <el-button type="primary" @click="next()">下一步</el-button>
    </el-form-item>
    <el-form-item label="" v-model="showClass" v-if="showClass==true">
      类型
      <el-input type="textarea" v-model="form.test[form.index]"></el-input>
      标识id
      <el-input type="textarea" v-model="form.test[form.index+1]"></el-input>
      方法
      <el-input type="textarea" v-model="form.test[form.index+2]"></el-input>
      期望结果
      <el-input type="textarea" v-model="form.result"></el-input>
      数据来源
      <el-input type="textarea" v-model="form.desc"></el-input>
      <el-button type="primary" @click="flash()">下一条</el-button>
    </el-form-item>
    </el-main>
    </el-form>
     <!-- <div><img src="\images\01.png" alt=""></div> -->
      <!-- <el-button type="button" @click="getResult()">获取</el-button> -->
      <!-- <p>{{form.test}}</p> -->
      <!-- <p>{{test1}}</p> -->
      <!-- <div>{{form.tactics}}</div> -->

      <section class="img2">
    <!-- <el-input type="textarea" v-model="form.toolname"></el-input>   -->
    <!-- <el-input type="textarea">示例</el-input> -->
    <!-- <div>信息收集内容</div> -->
    <div>渗透测试--渗透攻击方法</div>
    <div>当我们探测到了该网站存在漏洞之后，就要对该漏洞进行利用了。
      不同的漏洞有不同的利用方法，通过漏洞我们拿到网站的webshell
      
    </div>

  </section>
      
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
        desc: 'neo4j',
        test:'test',
        result:'获取目标系统权限',
        index:0
      },
       showClass: false  
    };
  },

  methods: {
    next(){
    this.$router.push({path: '/Trace removal recommendations'})
    },
     mounted(){
    location.reload();},
     TJ(){
    this.$router.push({path:'Recommended penetration steps func?name='+this.form.tactics})},
    flash(){
      if (this.form.index<this.form.test.length-3){
      this.form.index=this.form.index+3;}
      else{
        alert('没有了');
        this.mounted();
      }
    },
    goBack(){
        this.$router.back()
    },
    getResult:function() {
        var _this = this
        _this.$axios.get('http://127.0.0.1:5000/api/st/?name='+_this.form.tactics).then
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
  height:1000px;
  position: absolute;
  left: 50%;
  top:50%;
  transform: translate(-50%,-30%);

}
.img2 {
  padding: 0px 40px;
  width: 300px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
  height:500px;
  position: absolute;
  left: -58%;
  top:5%;
  transform: translate(0%,0%);

}
</style>

