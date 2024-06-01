<template>
    <el-container class="container">
      <el-form ref="form" :model="form" label-width="120px" @submit.native.prevent="handleSubmit">
        <el-form-item label="存证内容">
          <el-input v-model="form.content" required></el-input>
          <el-checkbox v-model="form.contentEncrypted">加密</el-checkbox>
        </el-form-item>
  
        <el-form-item label="存证单位">
          <el-input v-model="form.unit" required></el-input>
          <el-checkbox v-model="form.unitEncrypted">加密</el-checkbox>
        </el-form-item>
  
        <el-form-item label="存证人">
          <el-input v-model="form.person" required></el-input>
          <el-checkbox v-model="form.personEncrypted">加密</el-checkbox>
        </el-form-item>
  
        <el-form-item label="数据来源">
          <el-input v-model="form.source" required></el-input>
          <el-checkbox v-model="form.sourceEncrypted">加密</el-checkbox>
        </el-form-item>
  
        <el-form-item label="存证时间">
          <el-date-picker v-model="form.date" type="date" placeholder="选择日期" required></el-date-picker>
          <el-checkbox v-model="form.dateEncrypted">加密</el-checkbox>
        </el-form-item>
  
        <el-form-item label="作品类型">
          <el-radio-group v-model="form.type">
            <el-radio label="image">图片</el-radio>
            <el-radio label="video">视频</el-radio>
          </el-radio-group>
        </el-form-item>
  
        <el-form-item label="选择存证文件">
          <el-upload
            action="#"
            :show-file-list="false"
            :on-change="handleFileChange"
          >
            <el-button slot="trigger" type="primary">选 择 文 件</el-button>
          </el-upload>
        </el-form-item>
  
        <el-form-item label="存证描述">
          <el-input
            type="textarea"
            v-model="form.description"
            :maxlength="10000000"
          ></el-input>
        </el-form-item>
  
        <el-form-item>
          <el-button type="primary" @click="handleSubmit">提交</el-button>
          <el-button @click="handleCancel">取消</el-button>
        </el-form-item>
      </el-form>
    </el-container>
  </template>
  
  <script>
  export default {
  name: 'UploadFile',
    data() {
      return {
        form: {
          content: '',
          contentEncrypted: false,
          unit: '',
          unitEncrypted: false,
          person: '',
          personEncrypted: false,
          source: '',
          sourceEncrypted: false,
          date: '',
          dateEncrypted: false,
          type: 'image',
          file: null,
          description: ''
        }
      };
    },
    methods: {
      handleFileChange(file) {
        this.form.file = file.raw;
      },
      handleSubmit() {
        const formData = new FormData();
        for (const key in this.form) {
          formData.append(key, this.form[key]);
        }
        // handle form submission
        console.log('Form submitted:', this.form);
      },
      handleCancel() {
        this.$refs.form.resetFields();
        this.form.file = null;
      }
    }
  };
  </script>
  
  <style>
  .container {
    max-width: 600px;
    margin: 0 auto;
  }
  .el-form-item {
    margin-bottom: 15px;
  }
  </style>
  