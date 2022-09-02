<template>
  <section class="add">
    <el-form ref="form" :model="form" label-width="100px">
      <el-page-header @back="goBack" content="推荐系统">
      </el-page-header>
    <!-- <h2>信息收集工具</h2> -->
    <el-main>
    <el-form-item>
       <button @click='getResult()' v-trigger>信息收集工具</button>
      <!-- <el-button type="primary" @click="getResult();">点击事件</el-button> -->
    </el-form-item>
     <!-- <el-input type="textarea" v-model="form.toolname"></el-input> -->
     <el-form-item >
      工具名称
      <el-input type="textarea" v-model="form.toolname"></el-input>
      策略
      <el-input type="textarea" v-model="form.test[form.index]"></el-input>
      指令
      <el-input type="textarea" v-model="form.test[form.index+1]"></el-input>
      策略
      <el-input type="textarea" v-model="form.test[form.index+2]"></el-input>
      指令
      <el-input type="textarea" v-model="form.test[form.index+3]"></el-input>
     数据来源
      <el-input type="textarea" v-model="form.desc"></el-input>
      <el-button type="primary" @click="goBack()">返回工具列表</el-button>
      <el-button type="primary" @click="flash1()">上一页</el-button>
      <el-button type="primary" @click="flash()">下一页</el-button>
      <el-button type="primary" @click="next()">进行漏洞扫描</el-button>
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
    <div>工具使用示例</div>
    <div v-if="form.toolname=='whatweb'">
     <img src="\images\whatweb1.png" alt="">
     <img src="\images\whatweb2.png" alt="">
    </div>
    <div v-if="form.toolname=='chinaz'">
     <img src="\images\chinaz1.png" alt="">
     <img src="\images\chinaz2.png" alt="">
    </div>
    <div v-if="form.toolname=='ping'">
     <img src="\images\chinaz1.png" alt="">
     <img src="\images\chinaz2.png" alt="">
    </div>
    <div v-if="form.toolname=='nmap'">
     <img src="\images\nmap1.png" alt="">
     <img src="\images\nmap2.png" alt="">
    </div>
    <div v-if="form.toolname=='御剑'">
     <img src="\images\御剑1.png" alt="">
     <img src="\images\御剑2.png" alt="">
    </div>
    <div v-if="form.toolname=='whois'">
     <img src="\images\whois1.png" alt="">
     <img src="\images\whois2.png" alt="">
    </div>
    <div v-if="form.toolname=='cansina'">
     <img src="\images\cansina.png" alt="">
  
    </div>
    <div v-if="form.toolname=='dirbuster'">
     <img src="\images\dirbuster1.jpg" alt="">

    </div>
    <div v-if="form.toolname=='wwwscan'">
     <img src="\images\wwwscan1.png" alt="">

    </div>
    <div v-if="form.toolname=='masscan'">
     <img src="\images\masscan1.png" alt="">
     <img src="\images\masscan2.png" alt="">
    </div>
     <div v-if="form.toolname=='netcraft'">
     <img src="\images\netcraft1.jpg" alt="">

    </div>
        <el-button type="primary" @click="open()">具体使用方法</el-button>
  </section>
  <section class="img2">
    <div>收集内容</div>
    <!-- <el-input type="textarea" v-model="form.toolname"></el-input>   -->
    <!-- <el-input type="textarea">示例</el-input> -->
    <div v-if="form.toolname=='whatweb'">
     <img src="\images\主机.png" alt="">
  
    </div>
    <div v-if="form.toolname=='chinaz'">
     <img src="\images\ip地址.png" alt="">

    </div>
    <div v-if="form.toolname=='ping'">
     <img src="\images\ip地址.png" alt="">

    </div>
    <div v-if="form.toolname=='nmap'">
     <img src="\images\主机.png" alt="">

    </div>
    <div v-if="form.toolname=='御剑'">
     <img src="\images\目录.png" alt="">
   
    </div>
    <div v-if="form.toolname=='whois'">
     <img src="\images\注册信息.png" alt="">

    </div>
    <div v-if="form.toolname=='cansina'">
     <img src="\images\主机.png" alt="">
  
    </div>
     <div v-if="form.toolname=='wwwscan'">
     <img src="\images\目录.png" alt="">
  
    </div>
    <div v-if="form.toolname=='dirbuster'">
     <img src="\images\目录.png" alt="">

    </div>
    <div v-if="form.toolname=='masscan'">
     <img src="\images\主机.png" alt="">

    </div>
     <div v-if="form.toolname=='netcraft'">
     <img src="\images\主机.png" alt="">

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
        tactics: '端口扫描',
        desc: 'neo4j',
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
      open(){
        if(this.$route.query.name=='nmap'){
           window.open("https://blog.csdn.net/qq_54037445/article/details/123469988", "_blank");}
        if(this.$route.query.name=='chinaz') {
           window.open("https://ping.chinaz.com/", "_blank");}
        if(this.$route.query.name=='whatweb') {
           window.open("https://www.jianshu.com/p/f955ebe90fd8", "_blank");}
        if(this.$route.query.name=='御剑') {
           window.open("https://blog.csdn.net/qq_45076423/article/details/103018509", "_blank");}
           if(this.$route.query.name=='whois') {
           window.open("https://whois.chinaz.com/", "_blank");}
           if(this.$route.query.name=='cansina') {
           window.open("https://blog.csdn.net/weixin_33725126/article/details/86250694", "_blank");}
           if(this.$route.query.name=='dirbuster') {
           window.open("https://blog.csdn.net/weixin_45116657/article/details/101531332", "_blank");}
           if(this.$route.query.name=='masscan') {
           window.open("https://blog.csdn.net/qq_33608000/article/details/124831900", "_blank");}
           if(this.$route.query.name=='netcraft') {
           window.open("http://t.zoukankan.com/luxh-p-2768982.html", "_blank");}
          if(this.$route.query.name=='wwwscan') {
           window.open("https://blog.csdn.net/tianjin_ren/article/details/88773106", "_blank");}
           
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
        _this.$axios.get('http://127.0.0.1:5000/api/tool/?name='+_this.form.toolname).then
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
  width: 100px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
  height:200px;
  position: absolute;
  left: -65%;
  top:20%;
  transform: translate(0%,0%);

}
</style>