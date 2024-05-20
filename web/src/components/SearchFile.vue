<template>
  <div>
    <div class="block">
      <el-input v-model="searchValue" :placeholder="placeholderText"></el-input>
    </div>
  
    <div class="block">
      <el-radio-group v-model="searchType">
        <el-radio label="dataId">数据ID</el-radio>
        <el-radio label="blockId">区块ID</el-radio>
      </el-radio-group>
    </div>

    <div class="block">
      <el-button type="primary" @click="searchFile">搜索</el-button>
    </div>
    
    <el-table v-if="filteredFiles.length" :data="filteredFiles" style="width: 100%">
      <el-table-column prop="name" label="文件名" width="180"></el-table-column>
      <el-table-column prop="size" label="文件大小 (KB)" width="180"></el-table-column>
      <el-table-column prop="type" label="文件类型" width="180"></el-table-column>
      <el-table-column prop="uploadTime" label="上传时间" width="180"></el-table-column>
      <el-table-column prop="dataId" label="数据ID" width="180"></el-table-column>
      <el-table-column prop="blockId" label="区块ID" width="180"></el-table-column>
    </el-table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SearchFile',
  data() {
    return {
      searchType: 'dataId',
      searchValue: '',
      filteredFiles: []
    }
  },
  computed: {
    placeholderText() {
      return this.searchType === 'dataId' ? '请输入数据ID' : '请输入区块ID';
    }
  },
  methods: {
    async searchFile() {
      try {
        const response = await axios.get('http://10.122.223.44:1234/get_files', {
          params: {
            type: this.searchType,
            value: this.searchValue
          }
        });
        this.filteredFiles = response.data;
      } catch (error) {
        console.error('Error fetching files:', error);
      }
    }
  }
}
</script>

<style scoped>
.block {
  margin-bottom: 20px;
}
</style>
