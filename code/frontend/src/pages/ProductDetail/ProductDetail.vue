<template>
  <v-container class="pa-0">
    <v-responsive max-width="1368" class="mx-auto">
      <v-row v-if="productInfo">
        <v-col cols="12" md="5">
          <v-row justify="center" class="my-md-16">
            <v-carousel
              height="400"
              v-model="picPos"
              hide-delimiter-background
              hide-delimiters
            >
              <v-carousel-item>
                <v-img
                  contain
                  height="100%"
                  tile
                  :src="productInfo.pics"
                ></v-img>
              </v-carousel-item>
              <v-carousel-item>
                <v-sheet
                  color="transparent"
                  v-if="!synImage"
                  height="100%"
                  tile
                >
                  <v-row class="fill-height" align="center" justify="center">
                    <v-progress-circular
                      v-if="progressCircular"
                      :size="50"
                      color="primary"
                      indeterminate
                    ></v-progress-circular>
                    <p v-else class="black--text">
                      Sign in as customers to see try-on images
                    </p>
                  </v-row>
                </v-sheet>
                <v-img
                  v-else
                  height="100%"
                  contain
                  tile
                  :src="synImage ? synImage : testImg"
                ></v-img>
              </v-carousel-item>
            </v-carousel>
          </v-row>
          <v-row justify="center">
            <v-btn class="ma-4" @click="picPos = 0">服装</v-btn>
            <v-btn class="ma-4" @click="picPos = 1">try on</v-btn>
          </v-row>
        </v-col>
        <v-col cols="12" md="7" class="px-16 py-md-16">
          <v-row class="py-6">
            <h2>{{ productInfo.name }}</h2>
          </v-row>

          <v-row class="py-6">
            <strong class="red--text">
              ￥ <span style="font-size: 30px"> {{ productInfo.price }} </span>
            </strong>
          </v-row>

          <v-row align="center">
            <div v-if="!rateClickStatus">
              <strong> 请为本次 TryOn 评分 </strong>
            </div>
            <div v-else><strong> 感谢您的评价！！！！ </strong></div>
            <v-rating
              :readonly="rateClickStatus"
              :value="rating"
              @input="rateTryOn($event)"
              class="mx-4"
              background-color="orange lighten-3"
              color="orange"
              length="5"
              large
              hover
              dense
            ></v-rating>
          </v-row>
          <v-row class="ma-4">
            <v-col>
              <v-row
                v-for="(rate, i) in rateList"
                :key="i"
                cols="12"
                align="center"
              >
                <div class="mx-2">{{ 5 - i }}分</div>
                <v-sheet width="300">
                  <v-progress-linear height="20" :value="rate">
                    <strong>{{ rateNum[i] }}</strong>
                  </v-progress-linear>
                </v-sheet>
              </v-row>
            </v-col>
          </v-row>
          <v-row>
            <v-btn class="mx-4 my-6" x-large :href="productInfo.link"
              >立即购买</v-btn
            >
            <div class="text-center">
              <v-menu offset-y>
                <template v-slot:activator="{ on, attrs }">
                  <v-btn class="mx-4 my-6" v-bind="attrs" v-on="on" x-large>
                    分享照片
                  </v-btn>
                </template>
                <v-list>
                  <a
                    :href="qzonelink"
                    style="text-decoration: none"
                    target="_blank"
                  >
                    <v-list-item>
                      <v-list-item-title>QQ空间</v-list-item-title>
                    </v-list-item>
                  </a>
                  <a
                    :href="qfriendlink"
                    style="text-decoration: none"
                    target="_blank"
                  >
                    <v-list-item>
                      <v-list-item-title>QQ好友</v-list-item-title>
                    </v-list-item>
                  </a>
                  <a
                    href="https://www.weibo.com"
                    style="text-decoration: none"
                    target="_blank"
                  >
                    <v-list-item>
                      <v-list-item-title> 新浪微博 </v-list-item-title>
                    </v-list-item>
                  </a>
                </v-list>
              </v-menu>
            </div>
          </v-row>
        </v-col>
      </v-row>
      <v-row>
        <v-col col="12">
          <v-card flat outlined>
            <v-card-actions>
              <v-textarea
                v-model="comment"
                outlined
                auto-grow
                rows="2"
                append-outer-icon="mdi-send"
                label="写下你的评论"
                @click:append-outer="sendComment"
              ></v-textarea>
            </v-card-actions>
            <v-card-title>评论</v-card-title>
            <v-list v-if="productInfo" two-line>
              <template v-for="(item, i) in productInfo.comments">
                <v-list-item :key="i">
                  <v-list-item-content>
                    <v-list-item-title>{{ item.user_id }}</v-list-item-title>

                    <v-list-item-subtitle class="text--primary">
                      {{ item.comment }}
                    </v-list-item-subtitle>
                  </v-list-item-content>

                  <v-list-item-action>
                    <v-list-item-action-text>
                      {{
                        item.submit_date.slice(0, item.submit_date.indexOf("T"))
                      }}
                    </v-list-item-action-text>
                    <v-icon
                      v-if="name === item.user_id"
                      @click="deleteComment(item.id)"
                      >mdi-delete</v-icon
                    >
                  </v-list-item-action>
                </v-list-item>
              </template>
            </v-list>
          </v-card>
        </v-col>
      </v-row>
    </v-responsive>
  </v-container>
</template>

<script>
import axios from "axios";
import getCookieName from '@/components/GetCookie'

export default {
  name: "ProductDetail",
  data: () => ({
    name: null,
    userid: null,
    progressCircular: true,
    picPos: 0,
    productInfo: null,
    rateNum: null,
    rateList: null,
    rating: 0,
    synImage: null,
    rateClickStatus: false,
    comment: "",
  }),
  async beforeCreate() {
    const urlParams = new URLSearchParams(window.location.search);
    const productId = urlParams.get("id");
    try {
      const response = await axios.get("/api/products/" + productId + "/");
      console.log(response);
      let data = response.data;
      this.productInfo = data;
      this.productInfo.comments.reverse();
      this.rateNum = [
        data.number_people_scoring_five,
        data.number_people_scoring_four,
        data.number_people_scoring_three,
        data.number_people_scoring_two,
        data.number_people_scoring_one,
      ];
    } catch (error) {
      console.error(error);
    }

    this.name = localStorage.getItem("name");
    this.userid = localStorage.getItem("isSaler");

    if (!this.name || this.userid === "y") {
      this.progressCircular = false;
      return;
    }
    const url =
      "/api/tryon?" +
      "customer_name=" +
      this.name +
      "&product_name=" +
      productId;
    try {
      const response = await axios.get(url);
      const data = response.data;
      this.synImage = data[0].url;
    } catch (error) {
      console.log(error);
    }
  },
  methods: {
    sendComment() {
      if (!this.name) {
        alert("请先登录!");
        return;
      }
      let commentData = {
        comment: this.comment,
        product: this.productInfo.id,
      };
      axios
        .post("/api/comments/", commentData, {
          headers: {
            "X-CSRFToken": getCookieName("csrftoken"),
          },
        })
        .then(() => {
          window.location.reload();
        })
        .catch((error) => {
          alert(error);
          console.log(error);
        });
    },
    deleteComment(cid) {
      axios
        .delete("/api/comments/" + cid + "/", {
          headers: {
            "X-CSRFToken": getCookieName("csrftoken"),
          },
        })
        .then(() => {
          window.location.reload();
        })
        .catch((error) => {
          alert(error);
          console.log(error);
        });
    },
    rateTryOn(rate) {
      console.log(rate);
      let updata = {};
      let nowRate = this.rateNum[5 - rate] + 1;
      switch (rate) {
        case 1: {
          updata["number_people_scoring_one"] = nowRate;
          break;
        }
        case 2: {
          updata["number_people_scoring_two"] = nowRate;
          break;
        }
        case 3: {
          updata["number_people_scoring_three"] = nowRate;
          break;
        }
        case 4: {
          updata["number_people_scoring_four"] = nowRate;
          break;
        }
        case 5: {
          updata["number_people_scoring_five"] = nowRate;
          break;
        }
        default:
          break;
      }
      axios
        .patch("/api/products/" + this.productInfo.id + "/", updata, {
          headers: {
            "X-CSRFToken": getCookieName("csrftoken"),
          },
        })
        .then(() => {
          // this.rateNum[5 - rate] = nowRate;
          this.$set(this.rateNum, 5 - rate, nowRate);
          this.rateClickStatus = true;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  watch: {
    rateNum() {
      let sumStar = 0;
      this.rateNum.forEach((item) => {
        sumStar += item;
      });
      let foo = [];
      if (sumStar === 0) {
        sumStar = 1;
      }
      this.rateNum.forEach((item) => {
        foo.push((item / sumStar) * 100);
      });
      this.rateList = foo;
    },
  },
  computed: {
    qzonelink() {
      let picurl = window.location.host + this.synImage;
      let url =
        "https://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url=" +
        picurl +
        "&sharesource=qzone&title=" +
        "tryon" +
        "&pics=" +
        picurl +
        "&summary=" +
        "快来康康我的tryon结果！";
      return url;
    },
    qfriendlink() {
      let picurl = window.location.host + this.synImage;
      let url =
        "http://connect.qq.com/widget/shareqq/index.html?url=" +
        picurl +
        "&sharesource=qzone&title=" +
        "tryon" +
        "&pics=" +
        "快来看看" +
        "&summary=" +
        "快来康康我的tryon结果！" +
        "&desc=";
      return url;
    },
  },
};
</script>

