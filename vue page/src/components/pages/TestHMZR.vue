<template>
  <section class="add">
    <el-form ref="form" :model="form" label-width="100px">
      <el-page-header @back="goBack" content="推荐系统">
      </el-page-header>
    <!-- <h2>信息收集工具</h2> -->
    <el-main>
    <el-form-item>
       <button @click='getResult()' v-trigger>渗透攻击步骤推荐</button>
      <!-- <el-button type="primary" @click="getResult();">点击事件</el-button> -->
    </el-form-item>
     <!-- <el-input type="textarea" v-model="form.toolname"></el-input> -->
     <el-form-item >
      类型
      <el-input type="textarea" v-model="form.test[form.index]"></el-input>
      id
      <el-input type="textarea" v-model="form.test[form.index+1]"></el-input>
      方法
      <el-input type="textarea" v-model="form.test[form.index+2]"></el-input>
  
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
    <div v-if="form.toolname=='报错注入，延时注入，爆表，爆字段，获取字段，目录遍历，写入文件，目录遍历，蚁剑连接'">
     <a>爆表<img src="\images\爆表.png" alt=""></a>
     <a>目录遍历<img src="\images\御剑1.png" alt=""></a>
     <a>写入文件<img src="\images\脚本上传.png" alt=""></a>
     <a>蚁剑连接<img src="\images\御剑2.png" alt=""></a>
    </div>
    <div v-if="form.toolname=='字典暴破，登录ssh，反弹shell，注入测试，暴破目录，DirBuster暴破，获取shell，登录index首页，反弹shell'">
     <a>字典暴破<img src="\images\字典暴破.png" alt=""></a>
     <a>登录ssh<img src="\images\ssh连接.png" alt=""></a>
     <a>反弹shell<img src="\images\反弹shell.png" alt=""></a>
     <a>暴破目录<img src="\images\御剑1.png" alt=""></a>
     <a>获取shell<img src="\images\获取shell.png" alt=""></a>

    </div>
    <div v-if="form.toolname=='尝试put上传，设置攻击载荷，提交表单数据，重新填充到对应的表单数据中，绕过了安全限制，执行任意命令poc，GET传输拼接，反弹shell'">
     <a>上传<img src="\images\脚本上传.png" alt=""></a>
     <a>攻击载荷<img src="\images\攻击载荷.png" alt=""></a>
     <a>绕过<img src="\images\绕过.png" alt=""></a>
     <a>反弹shell<img src="\images\反弹shell.png" alt=""></a>
    </div>
    <div v-if="form.toolname=='抓包，命令注入，反弹shell，本机监听，获得普通用户权限，得到shell，redis提权'">
     <a>抓包<img src="\images\抓包.png" alt=""></a>
     <a>反弹shell<img src="\images\反弹shell.png" alt=""></a>
     <a>监听<img src="\images\nc监听.png" alt=""></a>
     <a>获取shell<img src="\images\获取shell.png" alt=""></a>
    </div>
    <div v-if="form.toolname=='OpenVAS'">
     <img src="\images\openvas1.png" alt="">
     <img src="\images\openvas2.png" alt="">
    </div>
        <!-- <el-button type="primary" @click="open()">具体使用方法</el-button> -->
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
        result:'获取目标shell',
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
        if(this.$route.query.name=='Xscan'){
           window.open("https://blog.csdn.net/qq_39116519/article/details/117249379", "_blank");}
        if(this.$route.query.name=='AppScan') {
           window.open("https://blog.csdn.net/weixin_44940180/article/details/108215834", "_blank");}
        if(this.$route.query.name=='Nessus') {
           window.open("https://blog.csdn.net/hackzkaq/article/details/122842698", "_blank");}
        if(this.$route.query.name=='NeXpose') {
           window.open("https://blog.csdn.net/weixin_44534461/article/details/88557754", "_blank");}
           if(this.$route.query.name=='OpenVAS') {
           window.open("https://blog.csdn.net/weixin_44657888/article/details/123514576", "_blank");}
          
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
        _this.$axios.get('http://127.0.0.1:5000/api/hms/?name='+_this.form.toolname).then
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