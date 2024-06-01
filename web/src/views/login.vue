<template>
  <div class="login-container">
    <vue-starry-sky :stars-count="2000" :distance="500"></vue-starry-sky>
    <el-form :model="ruleForm" :rules="rules"
             status-icon
             ref="ruleForm"
             label-position="left"
             label-width="0px"
             class="demo-ruleForm login-page">
      <h3 class="title">EOS系统登录</h3>
      <el-form-item prop="username">
        <el-input type="text"
                  v-model="ruleForm.username"
                  placeholder="用户名"
        ></el-input>
      </el-form-item>
      <el-form-item prop="password">
        <el-input type="password"
                  v-model="ruleForm.password"
                  placeholder="密码"
        ></el-input>
      </el-form-item>
      <el-form-item style="width:100%;">
        <a href="#" class="login-btn" @click="handleSubmit">登录</a>
      </el-form-item>
      <el-form-item style="width:100%;">
        <a href="#" class="register-btn" @click="showRegister">注册</a>
      </el-form-item>
    </el-form>
    
    <!-- 注册表单 -->
    <el-dialog title="注册" :visible.sync="showRegisterForm">
      <el-form :model="registerForm" :rules="registerRules"
               ref="registerForm"
               label-position="left"
               label-width="100px"
               class="demo-registerForm">
        <el-form-item label="用户名" prop="username">
          <el-input v-model="registerForm.username" placeholder="用户名"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input type="password" v-model="registerForm.password" placeholder="密码"></el-input>
        </el-form-item>
        <el-form-item label="确认密码" prop="confirmPassword">
          <el-input type="password" v-model="registerForm.confirmPassword" placeholder="确认密码"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="handleRegister">注册</el-button>
          <el-button @click="showRegisterForm = false">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script>
  export default {
    name: "Login",
    data() {
      return {
        logining: false,
        ruleForm: {
          username: '',
          password: ''
        },
        type: 'systemAdmin',
        rules: {
          username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
          password: [{ required: true, message: '请输入密码', trigger: 'blur' }]
        },
        showRegisterForm: false, // 控制注册表单显示与隐藏
        registerForm: {
          username: '',
          password: '',
          confirmPassword: ''
        },
        registerRules: {
          username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
          password: [{ required: true, message: '请输入密码', trigger: 'blur' }],
          confirmPassword: [{ required: true, message: '请确认密码', trigger: 'blur' }]
        }
      }
    },
    methods: {
      note() {
        (function () {
          var a_idx = 0;
          window.onclick = function (event) {
            var a = new Array("牢大", "丁真", "牢杜", "坤坤", "维尼", "基尼", "太美", "谢帝", "diss", "😆", "👉", "🤡");
            var heart = document.createElement("b"); // 创建b元素
            heart.onselectstart = new Function('event.returnValue=false'); // 防止拖动
            document.body.appendChild(heart).innerHTML = a[a_idx]; // 将b元素添加到页面上
            a_idx = (a_idx + 1) % a.length;
            heart.style.cssText = "position: fixed;left:-100%;"; // 给p元素设置样式

            var f = 16, // 字体大小
                x = event.clientX - f / 2, // 横坐标
                y = event.clientY - f, // 纵坐标
                c = randomColor(), // 随机颜色
                a = 1, // 透明度
                s = 1.2; // 放大缩小

            var timer = setInterval(function () { // 添加定时器
              if (a <= 0) {
                document.body.removeChild(heart);
                clearInterval(timer);
              } else {
                heart.style.cssText = "font-size:16px;cursor: default;position: fixed;color:" +
                    c + ";left:" + x + "px;top:" + y + "px;opacity:" + a + ";transform:scale(" +
                    s + ");";
                y--;
                a -= 0.016;
                s += 0.002;
              }
            }, 15)
          }
          // 随机颜色
          function randomColor() {
            return "rgb(" + (~~(Math.random() * 255)) + "," + (~~(Math.random() * 255)) + "," + (~~(Math.random() * 255)) + ")";
          }
        }());
      },
      handleSubmit() {
        this.$refs.ruleForm.validate((valid) => {
          if (valid) {
            this.logining = true;
            axios.post('http://127.0.0.1:5000/login', {
              username: this.ruleForm.username,
              password: this.ruleForm.password
            })
            .then((response) => {
              this.logining = false;
              if (response.data.success) {
                // 保存用户名到 localStorage
                localStorage.setItem('username', this.ruleForm.username);
                localStorage.setItem('userData', JSON.stringify(response.data.data));
                this.$router.replace({ path: '/main/upload' });
              } else {
                this.$alert(response.data.message, '登录失败', {
                  confirmButtonText: '确定'
                });
              }
            })
            .catch((error) => {
              this.logining = false;
              if (error.response && error.response.status === 401) {
                this.$alert(error.response.data.message, '登录失败', {
                  confirmButtonText: '确定'
                });
              } else {
                console.error("There was an error!", error);
              }
            });
          }
        });
      },
      showRegister() {
        this.showRegisterForm = true;
      },
      handleRegister() {
        this.$refs.registerForm.validate((valid) => {
          if (valid) {
            if (this.registerForm.password !== this.registerForm.confirmPassword) {
              this.$alert('两次输入的密码不一致', '注册失败', {
                confirmButtonText: '确定'
              });
              return;
            }
            axios.post('http://127.0.0.1:5000/register', {
              username: this.registerForm.username,
              password: this.registerForm.password
            })
            .then((response) => {
              if (response.data.success) {
                this.$alert('注册成功', '成功', {
                  confirmButtonText: '确定',
                  callback: () => {
                    this.showRegisterForm = false;
                  }
                });
              } else {
                this.$alert(response.data.message, '注册失败', {
                  confirmButtonText: '确定'
                });
              }
            })
            .catch((error) => {
              console.error("There was an error!", error);
            });
          }
        });
      }
    },
    mounted() {
      this.note()
    }
  };
</script>

<style scoped>
  .login-container {
    width: 100%;
    height: 100vh; /* 使用视口高度保证容器占满整个屏幕 */
    display: flex;
    justify-content: center; /* 水平居中 */
    align-items: center; /* 垂直居中 */
    background: rgba(237, 233, 233, 0); /* 可选：添加背景半透明 */
  }
  .login-page {
    border-radius: 10px;
    margin: auto;
    width: 350px;
    padding: 35px 35px 15px;
    background: #fff;
    background: linear-gradient(to right, #8a90b8, #c3c0c0); /* 渐变背景色 */
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    backdrop-filter: blur(10px); /* 背景模糊 */
    border: none;
  }
  .login-btn, .register-btn {
    display: inline-block;
    width: 100%;
    padding: 5px 0;
    margin: 0;
    color: #21ebff;
    background: transparent;
    text-align: center;
    font-size: 16px;
    text-transform: uppercase;
    transition: 0.5s;
    overflow: hidden;
    position: relative;
    text-decoration: none;
    -webkit-box-reflect: below 1px linear-gradient(transparent, #0003);
  }
  .login-btn:hover, .register-btn:hover {
    background: #21ebff;
    color: #111;
    box-shadow: 0 0 50px #21ebff;
    transition-delay: 0.5s;
  }
  .login-btn::before, .login-btn::after, .register-btn::before, .register-btn::after {
    content: '';
    position: absolute;
    transition: 0.5s;
    transition-delay: 0.5s;
    border: 2px solid #21ebff;
  }
  .login-btn::before, .register-btn::before {
    top: 0;
    left: 0;
    width: 10px;
    height: 10px;
  }
  .login-btn:hover::before, .register-btn:hover::before {
    width: 100%;
    height: 100%;
    transition-delay: 0s;
  }
  .login-btn::after, .register-btn::after {
    right: 0;
    bottom: 0;
    width: 10px;
    height: 10px;
  }
  .login-btn:hover::after, .register-btn:hover::after {
    width: 100%;
    height: 100%;
    transition-delay: 0s;
  }
  .el-input {
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  .el-button {
    border: none;
    background-color: #42a5f5;
    color: white;
    border-radius: 5px;
    transition: background-color 0.3s, transform 0.2s;
  }
  .el-button:hover {
    background-color: #1e88e5;
    transform: translateY(-2px);
  }
  .el-input:focus {
    border-color: #42a5f5;
    box-shadow: 0 0 0 2px rgba(66,165,245,0.2);
  }
  .title {
    font-size: 32px; /* 标题字体大小 */
    text-align: center; /* 居中标题 */
    color: rgb(44, 39, 39); /* 白色文本 */
    background: linear-gradient(90deg, rgb(5, 1, 22) 0%, rgb(88, 5, 33) 10%, rgb(32, 32, 29) 20%, rgb(14, 7, 28) 30%, rgba(63,218,216,1) 40%, rgba(47,201,226,1) 50%, rgba(28,127,238,1) 60%, rgba(95,21,242,1) 70%, rgba(186,12,248,1) 80%, rgba(251,7,217,1) 90%, rgba(255,0,0,1) 100%);
    background-size: 200% 200%; /* 背景大小 */
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: AnimationName 10s ease infinite; /* 动画设置 */
    text-shadow: 0px 0px 10px rgba(255,255,255,0.5); /* 文本阴影 */
  }
  @keyframes AnimationName {
    0%{background-position:0% 50%}
    50%{background-position:100% 50%}
    100%{background-position:0% 50%}
  }
  .demo-registerForm {
    width: 300px;
    margin: 0 auto;
  }
</style>
