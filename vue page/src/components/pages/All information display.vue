<template>
  <section class="add">
       <el-form ref="form" :model="form" label-width="100px">
                <h2></h2>
       <el-header>  
  
      <el-page-header  @back="goBack" content="推荐系统">
      </el-page-header>
    </el-header>
     <h2 >过程记录</h2>
     <el-main>
      <el-form-item label="信息收集方法">
        <el-input v-model="form.recommendedCollectionMethod"></el-input>
      </el-form-item>
      <el-form-item label="漏洞扫描方法">
        <el-input v-model="form.vulnerabilityScanningMethod"></el-input>
      </el-form-item>
        <el-form-item label="渗透步骤">
        <el-input v-model="form.recommendedPenetrationSteps"></el-input>
      </el-form-item>
        <el-form-item label="痕迹清理方法">
        <el-input v-model="form.recommendationsForTraceCleaning"></el-input>
        </el-form-item>
         <el-form-item>
          <el-button type="primary" @click="goBack()">上一步</el-button>
        
          <el-button type="primary" @click="flash()">结果保存</el-button>
          <el-button type="primary" @click="flash()">退出</el-button>
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
        recommendedCollectionMethod: null,
        vulnerabilityScanningMethod: null,
        recommendedPenetrationSteps:null,
        recommendationsForTraceCleaning:null  
      },
    };
  },
  methods: {
     goBack(){
     this.$router.back();
    },
    flash(){
       this.$router.push({path: '/All information display'})
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
}
</style>

