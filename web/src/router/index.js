// 文件路径: src/router/index.js
import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '@/views/main.vue'
import UploadFile from '@/components/UploadFile.vue'
import SearchFile from '@/components/SearchFile.vue'
import VerifyFile from '@/components/VerifyFile.vue'
import Intro from '@/components/introduction.vue'
import Datalist from '@/components/Datalist.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'login'
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
      {
        path: 'Datalist',
        name: 'Datalist',
        component: Datalist,
      },
    ],
  },
]

const router = new VueRouter({
  mode: 'history', // 使用 HTML5 History 模式
  routes,
})

export default router
