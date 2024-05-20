<template>
  <div>
    <el-upload
      class="upload-demo"
      action="http://10.122.223.44:1234/upload"
      :on-success="handleSuccess"
      :on-error="handleError"
      :before-upload="beforeUpload">
      <el-button size="small" type="primary">点击上传</el-button>
    </el-upload>
    <div v-if="uploadResponse">
      <h3>上传结果：</h3>
      <pre>{{ uploadResponse }}</pre>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UploadFile',
  data() {
    return {
      uploadResponse: null
    };
  },
  methods: {
    handleSuccess(response, file, fileList) {
      console.log('File uploaded successfully:', file);
      this.uploadResponse = response; // 保存服务器响应的数据
    },
    handleError(err, file, fileList) {
      console.error('File upload failed:', file);
    },
    beforeUpload(file) {
      return true;
    }
  }
}
</script>

<style scoped>
.upload-demo {
  margin: 20px 0;
}
</style>