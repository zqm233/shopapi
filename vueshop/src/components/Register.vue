<template>
  <div class="box">
    <img src="../../static/image/Loginbg.3377d0c.jpg" alt="">
    <div class="register">
      <div class="register_box">
        <div class="register-title">注册路飞学城</div>
        <div class="inp">
          <input v-model="mobile" type="text" @blur="checkMobile" placeholder="手机号码" class="user">
          <input v-model="password" type="password" placeholder="登录密码" class="user">
          <input v-model="password2" type="password" placeholder="确认密码" class="user">
          <div class="sms-box">
            <input v-model="sms_code" maxlength="6" type="text" placeholder="短信验证码" class="user">
            <div class="sms-btn" @click="">{{sms_text}}</div>
          </div>
          <div id="geetest"></div>
          <button class="register_btn" @click="registerHandler">注册</button>
          <p class="go_login">已有账号
            <router-link to="/user/login">直接登录</router-link>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
    export default {
        name: 'Register',
        data() {
            return {
                sms_code: "",
                mobile: "",
                password: "",
                is_send: false, // 是否处于短信发送冷却时间内
                sms_text: "点击发送验证码",
                password2: "",
            }
        },
        created() {
        },
        methods: {
            registerHandler() {
                // 注册处理
                // 验证数据,在前端js中，正则是一种对象，我们可以直接编写正则对象然后调用正则提供的方法来完成字符串的操作
                let ret = /1[3-9]\d{9}$/.test(this.mobile);
                if (!ret) {
                    this.$alert("对不起,手机号码格式有误！");
                    return;
                }

                if (this.sms_code.length < 4 || this.sms_code.length > 6) {
                    this.$alert("对不起,短信验证码格式错误！");
                    return;
                }

                if (this.password.length < 6 || this.password.length > 16) {
                    this.$alert("对不起,密码长度必须在6-16个字符之间！");
                    return;
                }
                this.$axios.post(`${this.$settings.Host}/users/user/`, {
                    mobile: this.mobile,
                    password: this.password,
                    password2:this.password2,
                    sms_code: this.sms_code,
                }).then(response => {
                    // 保存登录状态
                    sessionStorage.user_id = response.data.id;
                    sessionStorage.user_name = response.data.username;
                    sessionStorage.user_token = response.data.token;
                    // 保存积分数量及兑换比例
                    // sessionStorage.user_credit = response.data.credit;
                    // sessionStorage.credit_money = response.data.credit_money;
                    let self = this;
                    this.$alert("注册成功！欢迎加入路飞学城！", "路飞学城", {
                        callback() {
                            self.$router.push("/");
                        }
                    });
                }).catch(error => {
                    this.$alert("对不起，注册用户失败！");
                });
            },
            checkMobile() {

              let ret = /1[3-9]\d{9}$/.test(this.mobile);
                if (!ret) {
                    this.$alert("对不起,手机号码格式有误！");
                    return;
                }

                // 验证手机号的唯一性
                this.$axios.get(`${this.$settings.Host}/users/mobile/${this.mobile}/`).then(response => {

                }).catch(error => {
                    this.$message("当前手机号已经被注册！");
                    this.mobile = "";
                });
            },
            // smsHander() {
            //     // 发送短信处理
            //     let ret = /1[3-9]\d{9}$/.test(this.mobile);
            //     if (!ret) {
            //         this.$alert("对不起，手机号码格式有误！");
            //         return;
            //     }
            //     if (this.is_send) {
            //         this.$alert("对不起，验证码已发送，请留意您的手机。不要频繁发送验证码！");
            //         return;
            //     }
            //     this.$axios.get(`${this.$settings.Host}/users/sms/${this.mobile}/`).then(response => {
            //         this.$message("短信验证码发送成功，请注意查收！");
            //         this.is_send = true;  // 让短信进去冷却状态
            //         let self = this;
            //         let num = 60;
            //         let t = setInterval(() => {
            //             if (num < 1) {
            //                 self.sms_text = "点击发送验证码";
            //                 this.is_send = false;
            //                 clearInterval(t); // 关闭定时器
            //             } else {
            //                 num--;  //等同与 num = num - 1;
            //                 self.sms_text = `${num}秒后点击重新发送`;
            //             }
            //         }, 1000);
            //     }).catch(error => {
            //         this.$alert(error.response.data.message);
            //     })
            //
            // }
        },

    };
</script>

<style scoped>
  .box {
    width: 100%;
    height: 100%;
    position: relative;
    overflow: hidden;
  }

  .box img {
    width: 100%;
    min-height: 100%;
  }

  .box .register {
    position: absolute;
    width: 500px;
    height: 400px;
    top: 0;
    left: 0;
    margin: auto;
    right: 0;
    bottom: 0;
    top: -338px;
  }

  .register .register-title {
    width: 100%;
    font-size: 24px;
    text-align: center;
    padding-top: 30px;
    padding-bottom: 30px;
    color: #4a4a4a;
    letter-spacing: .39px;
  }

  .register-title img {
    width: 190px;
    height: auto;
  }

  .register-title p {
    font-family: PingFangSC-Regular;
    font-size: 18px;
    color: #fff;
    letter-spacing: .29px;
    padding-top: 10px;
    padding-bottom: 50px;
  }

  .register_box {
    width: 400px;
    height: auto;
    background: #fff;
    box-shadow: 0 2px 4px 0 rgba(0, 0, 0, .5);
    border-radius: 4px;
    margin: 0 auto;
    padding-bottom: 40px;
  }

  .register_box .title {
    font-size: 20px;
    color: #9b9b9b;
    letter-spacing: .32px;
    border-bottom: 1px solid #e6e6e6;
    display: flex;
    justify-content: space-around;
    padding: 50px 60px 0 60px;
    margin-bottom: 20px;
    cursor: pointer;
  }

  .register_box .title span:nth-of-type(1) {
    color: #4a4a4a;
    border-bottom: 2px solid #84cc39;
  }

  .inp {
    width: 350px;
    margin: 0 auto;
  }

  .inp input {
    border: 0;
    outline: 0;
    width: 100%;
    height: 45px;
    border-radius: 4px;
    border: 1px solid #d9d9d9;
    text-indent: 20px;
    font-size: 14px;
    background: #fff !important;
  }

  .inp input.user {
    margin-bottom: 16px;
  }

  .inp .rember {
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    margin-top: 10px;
  }

  .inp .rember p:first-of-type {
    font-size: 12px;
    color: #4a4a4a;
    letter-spacing: .19px;
    margin-left: 22px;
    display: -ms-flexbox;
    display: flex;
    -ms-flex-align: center;
    align-items: center;
    /*position: relative;*/
  }

  .inp .rember p:nth-of-type(2) {
    font-size: 14px;
    color: #9b9b9b;
    letter-spacing: .19px;
    cursor: pointer;
  }

  .inp .rember input {
    outline: 0;
    width: 30px;
    height: 45px;
    border-radius: 4px;
    border: 1px solid #d9d9d9;
    text-indent: 20px;
    font-size: 14px;
    background: #fff !important;
  }

  .inp .rember p span {
    display: inline-block;
    font-size: 12px;
    width: 100px;
    /*position: absolute;*/
    /*left: 20px;*/

  }

  #geetest {
    margin-top: 20px;
  }

  .register_btn {
    width: 100%;
    height: 45px;
    background: #84cc39;
    border-radius: 5px;
    font-size: 16px;
    color: #fff;
    letter-spacing: .26px;
    margin-top: 30px;
  }

  .inp .go_login {
    text-align: center;
    font-size: 14px;
    color: #9b9b9b;
    letter-spacing: .26px;
    padding-top: 20px;
  }

  .inp .go_login span {
    color: #84cc39;
    cursor: pointer;
  }

  .sms-box {
    position: relative;
  }

  .sms-box .sms-btn {
    position: absolute;
    font-size: 14px;
    letter-spacing: 0.26px;
    top: 10px;
    right: 16px;
    border-left: 1px solid #484848;
    padding-left: 16px;
    padding-bottom: 4px;
    cursor: pointer;
    background: #ffffff;
  }
</style>
