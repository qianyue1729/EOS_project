<template>
  <div>
    <div class="block">
      <el-input v-model="searchValue" :placeholder="placeholderText"></el-input>
    </div>
  
    <div class="block">
      <el-radio-group v-model="searchType">
        <el-radio :label="0">数据ID</el-radio>
        <el-radio :label="1">区块ID</el-radio>
      </el-radio-group>
    </div>
    <div class="block">
      <el-upload
        class="upload-demo"
        action=""
        :before-upload="beforeUpload"
        :on-remove="handleRemove"
        :file-list="fileList"
        list-type="picture">
        <el-button size="small" type="primary">选择图片</el-button>
      </el-upload>
      <div v-if="imageUrl">
        <h3>图片预览：</h3>
        <img :src="imageUrl" alt="Image Preview" class="image-preview"/>
      </div>
    </div>
  
    <div class="block">
      <el-input v-model="hashValue" placeholder="请输入图片哈希值"></el-input>
    </div>

    <div class="block">
      <el-button type="primary" @click="verifyFile">校验</el-button>
    </div>
    
    <div v-if="verifyResult">
      <h3>校验结果：</h3>
      <pre>{{ verifyResult }}</pre>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'VerifyFile',
  data() {
    return {
      searchType: 0,
      searchValue: '',
      fileList: [],
      hashValue: '',
      verifyResult: null,
      imageUrl: null
    }
  },
  computed:{
    placeholderText(){
      return this.searchType === 0 ? '请输入数据ID' : '请输入区块ID';
    }
  },
  methods: {
    beforeUpload(file) {
      this.fileList = [file];
      this.previewImage(file);
      return false;  // 阻止自动上传，手动上传
    },
    handleRemove(file, fileList) {
      this.fileList = [];
      this.imageUrl = null;
    },
    previewImage(file) {
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = (e) => {
        this.imageUrl = e.target.result;
      };
    },
    async verifyFile() {
      if (this.fileList.length === 0 || !this.hashValue) {
        this.$message.error('请上传图片并输入哈希值');
        return;
      }

      const formData = new FormData();
      formData.append('file', this.fileList[0]);
      formData.append('hash', this.hashValue);

      try {
        const response = await axios.post('http://10.122.223.44:1234/verify_file', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
        this.verifyResult = response.data;
      } catch (error) {
        console.error('Error verifying file:', error);
      }
    }
  }
}
</script>

<style scoped>
.block {
  margin-bottom: 20px;
}
.image-preview {
  max-width: 50%;
  height: auto;
  margin-top: 10px;
}
</style>
