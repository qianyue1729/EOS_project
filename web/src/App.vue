<template>
  <div id="app">
    <el-container>
      <el-header>
        <h1 class="title">EOS可信存证系统</h1>
      </el-header>
      <el-main>
        <el-tabs v-model="activeTab" @tab-click="handleClick">
          <el-tab-pane label="上传文件" name="upload">
            <UploadFile />
          </el-tab-pane>
          <el-tab-pane label="使用数据ID搜索文件" name="search">
            <SearchFile />
          </el-tab-pane>
          <el-tab-pane label="校验文件" name="verify">
            <VerifyFile />
          </el-tab-pane>
          <el-tab-pane label="项目介绍" name="intro">
            <Intro />
          </el-tab-pane>
        </el-tabs>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import UploadFile from './components/UploadFile.vue'
import SearchFile from './components/SearchFile.vue'
import VerifyFile from './components/VerifyFile.vue'
import Intro from './components/introduction.vue'
export default {
  name: 'App',
  components: {
    UploadFile,
    SearchFile,
    VerifyFile,
    Intro
  },
  data() {
    return {
      activeTab: 'upload'
    }
  }
}
</script>

<style>
.title {
  font-family: 'PingFang SC';
  font-size: 36px;
  text-align: top;
  margin: 0,0;
  color: #ffffff;
  line-height: 0px;
}
</style>
