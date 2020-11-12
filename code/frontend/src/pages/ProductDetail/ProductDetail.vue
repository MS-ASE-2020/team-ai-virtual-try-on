<template>
  <v-container>
    <v-responsive max-width="1368" class="mx-auto">
      <v-row v-if="productInfo">
        <v-spacer></v-spacer>
        <v-col cols="12" md="5">
          <v-row justify="center" class="my-md-16">
            <v-carousel
              height="400"
              v-model="picPos"
              hide-delimiter-background
              hide-delimiters
            >
              <v-carousel-item>
                <v-img contain height="100%" tile :src="productInfo.pics"></v-img>
              </v-carousel-item>
              <v-carousel-item>
                <v-img
                  height="100%"
                  tile
                  src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
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
            <div> <strong> TryOn 评分 </strong> </div>
            <v-rating
              v-model="rating"
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
                v-for="(rate, i) in productInfo.rateList"
                :key="i"
                cols="12"
                align="center"
              >
                <div class="mx-2">{{ 5 - i }}分</div>
                <v-sheet width="300">
                  <v-progress-linear height="20" :value="rate">
                    <strong>{{ Math.ceil(rate) }}%</strong>
                  </v-progress-linear>
                </v-sheet>
              </v-row>
            </v-col>
          </v-row>
          <v-row>
            <v-btn class="mx-4 my-6" x-large :href="productInfo.link"
              >立即购买</v-btn
            >
            <v-btn class="mx-4 my-6" x-large>上传照片</v-btn>
          </v-row>
        </v-col>
        <v-spacer></v-spacer>
      </v-row>
    </v-responsive>
  </v-container>
</template>

<script>
import rqt from "@/variables.js";
import axios from "axios";

export default {
  name: "ProductDetail",
  data: () => ({
    picPos: 0,
    productInfo: null,
    rating: 4,
  }),
  async beforeCreate() {
    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get("id");
    try {
      const response = await axios.get(rqt.api + "/api/products/" + id + "/");
      console.log(response);
      let data = response.data;
      data.rateList = [
        data.number_people_scoring_five,
        data.number_people_scoring_four,
        data.number_people_scoring_three,
        data.number_people_scoring_two,
        data.number_people_scoring_one,
      ];
      this.productInfo = data;
    } catch (error) {
      console.error(error);
    }
  },
};
</script>

