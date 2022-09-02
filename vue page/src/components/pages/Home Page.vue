<template>
  <section class="add">
    <el-form ref="form" :model="form" label-width="100px">
      <el-header>  
      
        <el-page-header  content="推荐系统">
        </el-page-header>
      </el-header>
      <h2 >首页</h2>
      <el-main>
    
      <b>
        渗透测试是通过模拟恶意黑客的攻击方法，来评估计算机网络系统安全的一种评估方法。
      </b>
      
      <b>本系统根据用户需求，可以推荐出一些工具和步骤帮助用户进行渗透测试，仅供参考
      </b>
  点击<el-button type="primary" @click="next()">开始</el-button>使用
      <el-form-item>
        <!-- <img src="\images\渗透.png"  class="tu"> -->
      <!-- <img src="\images\流程图1.png" alt=""> -->
     
      </el-form-item>
 
       </el-main>
      
    </el-form>
    
   
  </section>
  
</template>

<script>
export default {
  data() {
    return {
      form: { //表单数据初始化
        tactics: null,
        desc: '111'
      },
       showClass: false  
    };
  },
  methods: {
    next(){
    this.$router.push({path: '/Collection Choice'})
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
  width: 1400px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
  height:1000px;
}
.tu{
  width: 800px;
   height:550px;
}

</style>

