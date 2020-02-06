<template>
  <div class="cart">
    <Header/>
    <div class="cart-info">
      <h3 class="cart-top">购物车结算 <span>共1门课程</span></h3>
      <div class="cart-title">
        <el-row>
          <el-col :span="2">&nbsp;</el-col>
          <el-col :span="10">课程</el-col>
          <el-col :span="8">有效期</el-col>
          <el-col :span="4">价格</el-col>
        </el-row>
      </div>
      <div class="cart-item" v-for="course in course_list">
        <el-row>
          <el-col :span="2" class="checkbox">&nbsp;&nbsp;</el-col>
          <el-col :span="10" class="course-info">
            <img :src="course.course_img" alt="">
            <div class="course_text">
              <span>{{course.course_name}}</span><br>
              <span class="discount_name">{{course.discount_name}}</span>
            </div>
          </el-col>
          <el-col :span="8"><span>{{course.expire_text}}</span></el-col>
          <el-col :span="4" class="course-price">
            <p>¥{{course.real_price.toFixed(2)}}</p>
            <p class="original_price">原价：¥{{course.price.toFixed(2)}}</p>
          </el-col>
        </el-row>
      </div>
      <!-- 优惠券和积分相关代码 -->
      <div class="discount">
        <div id="accordion">
          <div class="coupon-box">
            <div class="icon-box">
              <span class="select-coupon">使用优惠劵：</span>
              <a class="select-icon unselect" :class="use_coupon?'is_selected':''" @click="use_coupon=!use_coupon"><img
                class="sign is_show_select" src="static/image/12.png" alt=""></a>
              <span class="coupon-num">有{{coupon_list.length}}张可用</span>
            </div>
            <p class="sum-price-wrap">商品总金额：<span class="sum-price">¥ {{total_price.toFixed(2)}}元</span></p>
          </div>
          <div id="collapseOne" v-if="use_coupon">
            <ul class="coupon-list" v-if="coupon_list.length>0">
              <li class="coupon-item" @click="check_disable(item.start_time,item.now_time,item.id)"
                  :class="check_coupon(item.start_time,item.now_time,item.id,coupon)" v-for="(item,key) in coupon_list">
                <p class="coupon-name">{{item.coupon.name}}</p>
                <p class="coupon-condition" v-if="item.coupon.condition>0">满{{item.coupon.condition}}元可以使用</p>
                <p class="coupon-condition" v-else>没有使用条件</p>
                <p class="coupon-time start_time">开始时间：{{item.start_time.replace("T"," ")}}</p>
                <p class="coupon-time end_time">过期时间：{{item.end_time.replace("T"," ")}}</p>
              </li>
            </ul>
            <div class="no-coupon" v-else>
              <span class="no-coupon-tips">暂无可用优惠券</span>
            </div>
          </div>
        </div>
        <div class="credit-box">
          <label class="my_el_check_box">
            <el-checkbox class="my_el_checkbox" v-model="use_credit"></el-checkbox>
          </label>
          <p class="discount-num1" v-if="!use_credit">使用我的积分</p>
          <p class="discount-num2" v-else><span>总积分：{{user_credit}}，抵扣 <el-input-number @change="handleChange"
                                                                                        v-model="credit" :min="0"
                                                                                        :max="parseInt(user_credit)"
                                                                                        label="请填写积分"></el-input-number>，本次花费{{credit}}分可以抵扣{{credit_price}}元，扣除以后剩余{{parseInt(user_credit-credit)}}积分</span>
          </p>
        </div>
      </div>
      <div class="calc">
        <el-row class="pay-row">
          <el-col :span="4" class="pay-col"><span class="pay-text">支付方式：</span></el-col>
          <el-col :span="8">
            <span class="alipay" v-if="pay_type==1" @click="pay_type=1"><img src="/static/image/alipay2.png"
                                                                             alt=""></span>
            <span class="alipay" v-else @click="pay_type=1"><img src="/static/image/alipay.png" alt=""></span>
            <span class="alipay wechat" v-if="pay_type==2" @click="pay_type=2"><img src="/static/image/wechat2.png"
                                                                                    alt=""></span>
            <span class="alipay wechat" v-else @click="pay_type=2"><img src="/static/image/wechat.png" alt=""></span>
          </el-col>
          <el-col :span="8" class="count">实付款： <span>¥{{(total_price-coupon_price-credit_price).toFixed(2)}}</span>
          </el-col>
          <el-col :span="4" class="cart-pay"><span @click="payhander">{{pay_type===1?'支付宝':'微信'}}支付</span></el-col>
        </el-row>
      </div>
    </div>
    <Footer/>
  </div>
</template>

<script>
    import Header from "./common/Header"
    import Footer from "./common/Footer"

    export default {
        name: "Order",
        data() {
            return {
                token: "",
                pay_type: 1,
                credit: 0,  // 本次订单使用的积分
                coupon: 0,  // 用户选择使用的优惠券ID
                coupon_price: 0,  // 优惠券抵扣的金额
                credit_price: 0,  // 积分抵扣的金额
                course_list: [],
                total_price: 0, // 当前订单的价格
                use_coupon: false,  // 用户是否选择使用了优惠券
                use_credit: false,  // 使用户是否选择使用了积分
                user_credit: 0,  // 当前用户拥有的积分
                coupon_list: [],    // 后端提供的当前用户拥有的优惠券列表
            }
        },
        components: {
            Header,
            Footer,
        },
        watch: {
            use_coupon() {
                if (!this.use_coupon) {
                    // 在用户选择不同优惠券时，计算当前优惠券产生的抵扣金额
                    this.coupon = 0;
                }
            },
            coupon() {
                // 当用户使用优惠券时，关闭积分兑换
                this.use_credit = false;
                // 在用户选择不同优惠券时，计算当前优惠券产生的抵扣金额
                this.get_coupon_price();
            },
            use_credit() {
                if (!this.use_credit) {
                    // 当用户收起积分选项，则表示取消使用积分，当前抵扣积分重置为0.
                    this.credit = 0;
                }
            },
            credit() {
                this.check_credit();
                // // 在用户调整本次订单兑换的积分时，计算当前积分抵扣的金额
                this.get_credit_price();
            }
        },
        created() {
            this.check_user();
            this.user_credit = sessionStorage.user_credit;
            this.get_selected_course();
            this.get_user_coupon_list();
        },
        methods: {
            check_user() {
                this.token = this.$settings.check_user_login();
                if (!this.token) {
                    let self = this;
                    this.$alert("对不起，您尚未登录，请登录后再访问！", "路飞学城", {
                        callback() {
                            self.$router.push("/user/login");
                        }
                    })
                }
            },
            get_selected_course() {
                //获取购物车勾选商品的信息
                this.$axios.get(`${this.$settings.Host}/cart/order`, {
                    headers: {
                        Authorization: "jwt " + this.token,
                    }
                }).then(response => {
                    this.course_list = response.data;
                    // 计算当前所有商品的总价格
                    let total = 0;
                    for (let course of this.course_list) {
                        total += parseFloat(course.real_price);
                    }
                    this.total_price = total;
                }).catch(error => {
                    let self = this;
                    this.$alert("获取购物车信息失败，请稍后再试！", "路飞学城", {
                        callback() {
                            self.$router.go(-1);
                        }
                    });
                });
            },
            payhander() {
                // 生成订单
                this.$axios.post(`${this.$settings.Host}/order/`, {
                    pay_type: this.pay_type,
                    coupon: this.coupon,
                    credit: this.credit,
                }, {
                    headers: {
                        Authorization: "jwt " + this.token,
                    }
                }).then(response => {
                    // 去支付
                    if (response.data.order_number) {
                        this.get_pay_url(response.data.order_number);
                    }
                }).catch(error => {
                    this.$message.error("对不起,订单下单失败,请稍后再试！");
                });
            },
            get_pay_url(order_number) {
                // 获取支付链接地址
                this.$axios.get(`${this.$settings.Host}/payments/alipay/`, {
                    params: {
                        order_number: order_number,
                    }
                }).then(response => {
                    // 跳转到指定的支付链接地址
                    location.assign(response.data.url);
                }).catch(error => {
                    this.$message.error("对不起，未知的错误导致无法进行支付～请联系客服工作人员！")
                })
            },
            get_user_coupon_list() {
                // 获取当前登录用户的ID
                let user_id = localStorage.user_id || sessionStorage.user_id;
                // 获取当前用户可用的优惠券列表
                this.$axios.get(`${this.$settings.Host}/coupon/`, {
                    params: {
                        user_id: user_id,
                    },
                    headers: {
                        Authorization: "jwt " + this.token,
                    }
                }).then(response => {
                    this.coupon_list = response.data;
                }).catch(error => {
                    this.$message.error("获取优惠券列表失败!");
                })
            },
            check_coupon(start_time, now_time, coupon_id, current_coupon) {
                start_time = (new Date(start_time) - 0) / 1000;

                if (start_time > now_time) {
                    return "disable";   // 当前优惠券不能用
                }
                if (current_coupon === coupon_id) {
                    return "active";
                }
            },
            get_coupon_price() {
                // 优惠券ID切换为0时，抵扣价格也是0
                if (this.coupon === 0) {
                    this.coupon_price = 0;
                    return false;
                }
                // 获取优惠券抵扣的金额
                for (let item of this.coupon_list) {
                    if (item.id === this.coupon) {
                        let sale = parseFloat(item.coupon.sale.substr(1));
                        if (item.coupon.coupon_type === 0) {
                            // 折扣优惠
                            this.coupon_price = this.total_price * (1 - sale);
                        } else {
                            // 减免优惠
                            this.coupon_price = sale;
                        }
                    }
                }
            },
            check_disable(start_time, now_time, coupon_id) {
                // 判断当前优惠券是不是可以使用
                start_time = (new Date(start_time) - 0) / 1000;

                if (start_time > now_time) {
                    return false;
                }
                this.coupon = coupon_id;
            },
            get_credit_price() {
                // 计算积分抵扣的金额
                let credit_money = sessionStorage.credit_money;
                this.credit_price = this.credit / credit_money
            },
            check_credit() {
                // 判断积分的时候，是否超额
                // 先比较用户积分和实付金额，提取最小数值
                let credit_money = sessionStorage.credit_money;  // 积分兑换比例
                let order_credit = Math.floor((this.total_price - this.coupon_price) * credit_money);
                let min_credit = 0;
                if (order_credit > this.user_credit) {
                    min_credit = this.user_credit;
                } else {
                    min_credit = order_credit;
                }
                if (this.credit >= min_credit) {
                    this.credit = min_credit;
                }
            },
            handleChange() {

            }
        }
    }
</script>

<style scoped>
  .cart {
    margin-top: 80px;
  }

  .cart-info {
    overflow: hidden;
    width: 1200px;
    margin: auto;
  }

  .cart-top {
    font-size: 18px;
    color: #666;
    margin: 25px 0;
    font-weight: normal;
  }

  .cart-top span {
    font-size: 12px;
    color: #d0d0d0;
    display: inline-block;
  }

  .cart-title {
    background: #F7F7F7;
    height: 70px;
  }

  .calc {
    margin-top: 25px;
    margin-bottom: 40px;
  }

  .calc .count {
    text-align: right;
    margin-right: 10px;
    vertical-align: middle;
  }

  .calc .count span {
    font-size: 36px;
    color: #333;
  }

  .calc .cart-pay {
    margin-top: 5px;
    width: 110px;
    height: 38px;
    outline: none;
    border: none;
    color: #fff;
    line-height: 38px;
    background: #ffc210;
    border-radius: 4px;
    font-size: 16px;
    text-align: center;
    cursor: pointer;
  }

  .cart-item {
    height: 120px;
    line-height: 120px;
    margin-bottom: 30px;
  }

  .course-info img {
    width: 175px;
    height: 115px;
    margin-right: 35px;
    vertical-align: middle;
    float: left;
  }

  .course-price .original_price {
    color: #9b9b9b;
  }

  .course-info .course_text .discount_name {
    color: #ffc210;
    display: block;
  }

  .course-info::after {
    clear: both;
  }

  .course-info .course_text {
    float: left;
    line-height: 36px;
  }

  .alipay {
    display: inline-block;
    height: 48px;
  }

  .alipay img {
    height: 100%;
    width: auto;
  }

  .pay-text {
    display: block;
    text-align: right;
    height: 100%;
    line-height: 100%;
    vertical-align: middle;
    margin-top: 20px;
  }

  .course-price p {
    line-height: 36px;
  }

  /** 优惠券 **/
  .coupon-box {
    text-align: left;
    padding-bottom: 22px;
    padding-left: 30px;
    border-bottom: 1px solid #e8e8e8;
  }

  .coupon-box::after {
    content: "";
    display: block;
    clear: both;
  }

  .icon-box {
    float: left;
  }

  .icon-box .select-coupon {
    float: left;
    color: #666;
    font-size: 16px;
  }

  .icon-box::after {
    content: "";
    clear: both;
    display: block;
  }

  .select-icon {
    width: 20px;
    height: 20px;
    float: left;
  }

  .select-icon img {
    max-height: 100%;
    max-width: 100%;
    margin-top: 2px;
    transform: rotate(-90deg);
    transition: transform .5s;
  }

  .is_show_select {
    transform: rotate(0deg) !important;
  }

  .coupon-num {
    height: 22px;
    line-height: 22px;
    padding: 0 5px;
    text-align: center;
    font-size: 12px;
    float: left;
    color: #fff;
    letter-spacing: .27px;
    background: #fa6240;
    border-radius: 2px;
    margin-left: 20px;
  }

  .sum-price-wrap {
    float: right;
    font-size: 16px;
    color: #4a4a4a;
    margin-right: 45px;
  }

  .sum-price-wrap .sum-price {
    font-size: 18px;
    color: #fa6240;
  }

  .no-coupon {
    text-align: center;
    width: 100%;
    padding: 50px 0px;
    align-items: center;
    justify-content: center; /* 文本两端对其 */
    border-bottom: 1px solid rgb(232, 232, 232);
  }

  .no-coupon-tips {
    font-size: 16px;
    color: #9b9b9b;
  }

  .credit-box {
    height: 30px;
    margin-top: 40px;
    display: flex;
    align-items: center;
    justify-content: flex-end
  }

  .my_el_check_box {
    position: relative;
  }

  .my_el_checkbox {
    margin-right: 10px;
    width: 16px;
    height: 16px;
  }

  .discount {
    overflow: hidden;
  }

  .discount-num1 {
    color: #9b9b9b;
    font-size: 16px;
    margin-right: 45px;
  }

  .discount-num2 {
    margin-right: 45px;
    font-size: 16px;
    color: #4a4a4a;
  }

  .sun-coupon-num {
    margin-right: 45px;
    margin-bottom: 43px;
    margin-top: 40px;
    font-size: 16px;
    color: #4a4a4a;
    display: inline-block;
    float: right;
  }

  .sun-coupon-num span {
    font-size: 18px;
    color: #fa6240;
  }

  .coupon-list {
    margin: 20px 0;
  }

  .coupon-list::after {
    display: block;
    content: "";
    clear: both;
  }

  .coupon-item {
    float: left;
    margin: 15px 8px;
    width: 180px;
    height: 100px;
    padding: 5px;
    background-color: #fa3030;
    cursor: pointer;
  }

  .coupon-list .active {
    background-color: #fa9000;
  }

  .coupon-list .disable {
    cursor: not-allowed;
    background-color: #fa6060;
  }

  .coupon-condition {
    font-size: 12px;
    text-align: center;
    color: #fff;
  }

  .coupon-name {
    color: #fff;
    font-size: 24px;
    text-align: center;
  }

  .coupon-time {
    text-align: left;
    color: #fff;
    font-size: 12px;
  }

  .unselect {
    margin-left: 0px;
    transform: rotate(-90deg);
  }

  .is_selected {
    transform: rotate(-1turn) !important;
  }

  [class*=" el-icon-"], [class^=el-icon-] {
    font-size: 12px;
  }

</style>
