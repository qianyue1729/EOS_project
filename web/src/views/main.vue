<template>
  <div id="main">
    <el-container>
      <el-aside width="200px" class="aside">
        <div class="logo-container">
          <img src="@/assets/EOSlogo3.png" alt="Logo" class="logo" />
        </div>
        <el-menu
          :default-active="$route.path.split('/').pop()"
          class="el-menu-vertical-demo"
          @select="handleMenuSelect"
          :router="true">
          <el-submenu index="1">
            <template slot="title" >
              <i class="el-icon-menu"></i>
              <span>存证</span>
            </template>
            <el-menu-item index="upload">
              <i class="el-icon-upload"></i>
              <span slot="title">上传文件</span>
            </el-menu-item>
            <el-menu-item index="search">
              <i class="el-icon-search"></i>
              <span slot="title">查询</span>
            </el-menu-item>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title">
              <i class="el-icon-menu"></i>
              <span>查询</span>
            </template>
            <el-menu-item index="search">
              <i class="el-icon-search"></i>
              <span slot="title">查询</span>
            </el-menu-item>
            <el-menu-item index="verify">
              <i class="el-icon-document"></i>
              <span slot="title">校验文件</span>
            </el-menu-item>
            <el-menu-item index="intro">
              <i class="el-icon-info"></i>
              <span slot="title">项目介绍</span>
            </el-menu-item>
          </el-submenu>
          <el-submenu index="3">
            <template slot="title">
              <i class="el-icon-menu"></i>
              <span>校验</span>
            </template>
            <el-menu-item index="verify">
              <i class="el-icon-document"></i>
              <span slot="title">校验文件</span>
            </el-menu-item>
            <el-menu-item index="intro">
              <i class="el-icon-info"></i>
              <span slot="title">项目介绍</span>
            </el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-container>
        <el-header class="header">
          <div class="header-content">
            <h1 class="title">EOS可信存证系统</h1>
            <div class="user-info">
              <el-avatar icon="el-icon-user"></el-avatar>
              <span class="username">{{ username }}</span>
            </div>
          </div>
        </el-header>
        <el-main>
          <router-view/>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'Main',
  data() {
    return {
      username: localStorage.getItem('username') || 'Unknown User'
    }
  },
  methods: {
    handleMenuSelect(key) {
      const newPath = `/main/${key}`;
      if (this.$route.path !== newPath) {
        this.$router.push(newPath);
      }
    }
  }
}
</script>

<style>
body, html, #main {
  margin: 0;
  padding: 0;
  height: 100%;
}

.el-container {
  height: 100%;
}

.header {
  background-image: url('@/assets/header_background3.jpg'); /* 替换为你的背景图片路径 */
  background-size: cover; /* 让背景图片覆盖整个header */
  background-position: center; /* 让背景图片居中显示 */
  background-repeat: no-repeat; /* 不重复背景图片 */
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  padding: 0 20px;
}

.title {
  font-family: 'PingFang SC';
  font-size: 36px;
  text-align: top;
  margin: 0;
  color: #1890ff;
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

.aside {
  background-color: #000000;
  color: #ffffff;
}

.logo-container {
  text-align: center;
  padding: 0px 0;
  background-color: #000000;
}

.logo {
  max-width: 100%;
  height: 150px;
}

.el-menu-vertical-demo:not(.el-menu--collapse) {
  background-color: #000000;
  color: #000000;
  width: 99%;
  min-height: 60%;
}

.el-menu-item {
  color: #000000 !important;
}

.el-menu-item.is-active {
  background-color: #1890ff !important;
  border-radius: 10px;
}

.el-menu-item:hover {
  background-color: #188fff71 !important;
  border-radius: 10px;
}

.aside-menu:hover{
  background-color: #000000 !important;
}
</style>
