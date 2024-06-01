<template>
  <el-container class="container">
    <el-form ref="form" :model="form" label-width="120px" :rules="rules" @submit.native.prevent="handleSubmit">
      <el-form-item label="存证内容" prop="content">
        <el-input v-model="form.content" required></el-input>
        <el-checkbox v-model="form.contentEncrypted">加密</el-checkbox>
      </el-form-item>

      <el-form-item label="存证单位" prop="unit">
        <el-input v-model="form.unit" required></el-input>
        <el-checkbox v-model="form.unitEncrypted">加密</el-checkbox>
      </el-form-item>

      <el-form-item label="存证人" prop="person">
        <el-input v-model="form.person" required></el-input>
        <el-checkbox v-model="form.personEncrypted">加密</el-checkbox>
      </el-form-item>

      <el-form-item label="数据来源" prop="source">
        <el-input v-model="form.source" required></el-input>
        <el-checkbox v-model="form.sourceEncrypted">加密</el-checkbox>
      </el-form-item>

      <el-form-item label="存证时间" prop="date">
        <el-date-picker v-model="form.date" type="date" placeholder="选择日期" required></el-date-picker>
        <el-checkbox v-model="form.dateEncrypted">加密</el-checkbox>
      </el-form-item>

      <el-form-item label="作品类型" prop="type">
        <el-radio-group v-model="form.type">
          <el-radio label="image">图片</el-radio>
          <el-radio label="video">视频</el-radio>
        </el-radio-group>
      </el-form-item>

      <el-form-item label="选择存证文件" prop="file">
        <el-upload
          action="#"
          :show-file-list="false"
          :before-upload="handleFileChange"
        >
          <el-button type="primary">选择文件</el-button>
        </el-upload>
        <div v-if="form.file">
          <p>已选择文件：{{ form.file.name }}</p>
          <img v-if="isImage(form.file)" :src="form.fileUrl" alt="预览" style="max-width: 100%; margin-top: 10px;">
        </div>
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
        fileUrl: '',
        description: ''
      },
      rules: {
        content: [{ required: true, message: '请输入存证内容', trigger: 'blur' }],
        unit: [{ required: true, message: '请输入存证单位', trigger: 'blur' }],
        person: [{ required: true, message: '请输入存证人', trigger: 'blur' }],
        source: [{ required: true, message: '请输入数据来源', trigger: 'blur' }]
      }
    };
  },
  methods: {
    handleFileChange(file) {
      this.form.file = file;
      this.form.fileUrl = URL.createObjectURL(file);
      // Prevent auto upload
      return false;
    },
    isImage(file) {
      return file && file.type.startsWith('image/');
    },
    handleSubmit() {
      this.$refs.form.validate((valid) => {
        if (valid) {
          const formData = new FormData();
          for (const key in this.form) {
            formData.append(key, this.form[key]);
          }
          // handle form submission
          console.log('Form submitted:', this.form);
        } else {
          console.log('Form validation failed');
          return false;
        }
      });
    },
    handleCancel() {
      this.$refs.form.resetFields();
      this.form.file = null;
      this.form.fileUrl = '';
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
