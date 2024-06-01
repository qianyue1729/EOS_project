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
      <el-button type="primary" @click="searchFile">搜索</el-button>
    </div>
    
    <el-table v-if="1" :data="filteredFiles" style="width: 100%">
      <el-table-column prop="filename" label="文件名" width="180"></el-table-column>
      <el-table-column prop="dataId" label="数据ID" width="180"></el-table-column>
      <el-table-column prop="blockId" label="区块ID" width="180"></el-table-column>
      <el-table-column prop="fileHash" label="文件哈希值" width="180"></el-table-column>
    </el-table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SearchFile',
  props: {
    username: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      searchType: 0,
      searchValue: '',
      filteredFiles: []
    }
  },
  computed: {
    placeholderText() {
      return this.searchType === 0 ? '请输入数据ID' : '请输入区块ID';
    }
  },
  methods: {
    async searchFile() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/get_files', {
          params: {
            searchtype: this.searchType,
            searchValue: this.searchValue,
            username: this.username
          }
        });
        this.filteredFiles = response.data;
        //test
        console.log(response.data)

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
