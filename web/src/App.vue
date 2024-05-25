<template>
  <div id="app">
    <el-container>
      <el-header>
        <div class="header">
          <h1 class="title">EOS可信存证系统</h1>
          <div class="user-info">
            <el-avatar icon="el-icon-user"></el-avatar>
            <span class="username">{{ username }}</span>
          </div>
        </div>
      </el-header>
      <el-main>
        <el-tabs v-model="activeTab" @tab-click="handleClick">
          <el-tab-pane label="上传文件" name="upload">
            <UploadFile :username="username" />
          </el-tab-pane>
          <el-tab-pane label="使用数据ID搜索文件" name="search">
            <SearchFile :username="username" />
          </el-tab-pane>
          <el-tab-pane label="校验文件" name="verify">
            <VerifyFile :username="username" />
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
      activeTab: 'upload',
      username: 'Current User'  // replace with the actual username source
    }
  }
}
</script>

<style>
body, html, #app {
  margin: 0;
  padding: 0;
  height: 100%;
}

.el-container {
  height: 100%;
}

.header {
  background-color: #ffffff39;
  padding: 0 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.title {
  font-family: 'PingFang SC';
  font-size: 36px;
  text-align: top;
  margin: 0;
  color: #ffffff;
  line-height: 0px;
}

.user-info {
  display: flex;
  align-items: center;
  color: #ffffff;
}

.username {
  margin-left: 10px;
  font-size: 16px;
}
</style>
