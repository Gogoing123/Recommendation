<template>
  <section class="add">
    <el-form ref="form" :model="form" label-width="100px">
      <el-page-header @back="goBack" content="推荐系统">
      </el-page-header>
    <h2>推荐痕迹清除方法</h2>
    <el-main>
      <el-form-item label="需求"> 输入渗透的主机系统信息，如Linux
        <el-input v-model="form.tactics"></el-input>
      </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="goBack()">上一步</el-button>
     <!-- <a :href="'http://localhost:8080/#/Trace removal recommendations func?name='+form.tactics">推荐痕迹清除方法</a> -->
      <el-button type="primary" @click="TJ()">推荐痕迹清除方法</el-button>
      <el-button type="primary" @click="next()">下一步</el-button>
    </el-form-item>
    <el-form-item label="" v-model="showClass" v-if="showClass==true">
      系统
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
    <div>渗透测试--痕迹清除方法</div>
    <div>当我们达到了目的之后，有时候只是为了黑入网站挂黑页，或者在网站留下一个后门。
这里只是推荐一些痕迹清除方法，可以清除我们留下的一部分痕迹，并不能完全清除，完全清除入侵痕迹是不可能的！
主要是增加管理员发现入侵者的时间成本和人力成本。只要管理员想查，无论你怎么清除，还是能查到的。
最主要还是要以隐藏自身身份为主，最好的手段是在渗透前挂上代理，然后在渗透后痕迹清除。
      
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
        result:'清除痕迹信息',
        index:0
      },
       showClass: false  
    };
  },

  methods: {
    next(){
    this.$router.push({path: '/All information display'})
    },
      TJ(){
    this.$router.push({path:'Trace removal recommendations func?name='+this.form.tactics})},
    mounted(){
    location.reload();},
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
        _this.$axios.get('http://127.0.0.1:5000/api/hj/?name='+_this.form.tactics).then
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

