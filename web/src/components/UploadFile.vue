<template>
  <section>
    <div class="wave">
      <span></span>
      <span></span>
      <span></span>
    </div>
    <div class="content">
      <el-upload
        class="upload-demo"
        action="http://10.122.223.44:1234/upload"
        :data="extraData"
        :on-success="handleSuccess"
        :on-error="handleError"
        :before-upload="beforeUpload">
        <el-button size="small" type="primary">点击上传</el-button>
      </el-upload>
      <div v-if="uploadResponse">
        <!-- <h3>上传结果：</h3> -->
        <pre>{{ uploadResponse }}</pre>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'UploadFile',
  props: {
    username: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      uploadResponse: null
    };
  },
  computed: {
    extraData() {
      return {
        username: this.username
      };
    }
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
  },
  watch: {
    username(newVal) {
      this.extraData.username = newVal;
    }
  }
}
</script>

<style scoped>
/* 全局样式重置和字体设置 */
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Poppins', sans-serif;
}

/* 设置section填充满整个页面 */
section{
  position: relative;
  height: 100%;
  width: 100%;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* 波浪特效容器样式 */
section .wave{
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: #4973ff;
  overflow: hidden;
}

/* 波浪特效的具体样式 */
section .wave span{
  position: absolute;
  width: 325vh;
  height: 325vh;
  top:0;
  left: 50%;
  transform: translate(-50%, -75%);
  background: #000;
}
section .wave span:nth-child(1) {
  animation: animate 5s linear infinite;
  border-radius: 45%;
  background: rgba(20,20, 20, 1);
}
section .wave span:nth-child(2) {
  animation: animate 10s linear infinite;
  border-radius: 40%;
  background: rgba(20, 20, 20, 0.5);
}
section .wave span:nth-child(3) {
  animation: animate 15s linear infinite;
  border-radius: 42.5%;
  background: rgba(20, 20, 20, 0.5);
}

@keyframes animate{
  0%{
    transform: translate(-50%, -75%) rotate(0deg);
  }
  100%{
    transform: translate(-50%, -75%) rotate(360deg);
  }
}

/* 设置上传组件和上传结果的样式 */
section .content {
  position: relative;
  z-index: 1;
  color: #fff;
  text-align: center;
}

section .upload-demo {
  margin: 20px 0;
}

/* 设置上传结果的标题和内容样式 */
section .content h3 {
  margin: 20px 0 10px;
  font-size: 24px;
}

section .content pre {
  background: rgba(255, 255, 255, 0.2);
  padding: 10px;
  border-radius: 5px;
  overflow-x: auto;
}
</style>
