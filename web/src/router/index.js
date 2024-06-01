// 文件路径: src/router/index.js
import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '@/views/main.vue'
import UploadFile from '@/components/UploadFile.vue'
import SearchFile from '@/components/SearchFile.vue'
import VerifyFile from '@/components/VerifyFile.vue'
import Intro from '@/components/introduction.vue'
import Login from '../views/login.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: 'login'
  },
  {
    path: '/login',
    name: '登录',
    component: Login 
  },
  {
    path: '/main',
    name: 'Main',
    component: Main,
    children: [

      {
        path: 'upload',
        name: 'UploadFile',
        component: UploadFile,
      },
      {
        path: 'search',
        name: 'SearchFile',
        component: SearchFile,
      },
      {
        path: 'verify',
        name: 'VerifyFile',
        component: VerifyFile,
      },
      {
        path: 'intro',
        name: 'Intro',
        component: Intro,
      },
    ],
  },
]

const router = new VueRouter({
  mode: 'history', // 使用 HTML5 History 模式
  routes,
})

export default router
