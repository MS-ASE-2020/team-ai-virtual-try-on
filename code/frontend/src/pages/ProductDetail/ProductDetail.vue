<template>
  <v-container>
    <v-responsive max-width="1368" class="mx-auto">
    <v-row>
      <v-spacer></v-spacer>
      <v-col cols="12" md="5">
        <v-row justify="center" class="my-md-16">
          <v-carousel height="400" v-model="model" hide-delimiter-background hide-delimiters>
            <v-carousel-item v-for="color in colors" :key="color">
              <!-- <v-sheet :color="color" height="100%" tile>
                <v-row class="fill-height" align="center" justify="center">
                  <div class="display-3">Slide {{ i + 1 }}</div>
                </v-row>
              </v-sheet> -->
              <v-img
                height="100%"
                tile
                src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
              ></v-img>
            </v-carousel-item>
          </v-carousel>
        </v-row>
        <v-row justify="center">
          <v-btn class="ma-4">服装</v-btn>
          <v-btn class="ma-4">try on</v-btn>
        </v-row>
      </v-col>
      <v-col cols="12" md="7" class="px-16 py-md-16">
        <v-row class="py-6">
          <h2>{{ productName }}</h2>
        </v-row>

        <v-row class="py-6">
          价格<span>{{ price }}</span>
        </v-row>

        <v-row align="center">
          <div>TryOn 评分</div>
          <v-rating
            v-model="rating"
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
                  <strong>{{ Math.ceil(rate) }}%</strong>
                </v-progress-linear>
              </v-sheet>
            </v-row>
          </v-col>
        </v-row>
        <v-row >
          <v-btn class="mx-4 my-6" x-large>立即购买</v-btn>
          <v-btn class="mx-4 my-6" x-large>上传照片</v-btn>
        </v-row>
      </v-col>
      <v-spacer></v-spacer>
    </v-row>
    </v-responsive>
  </v-container>
</template>

<script>
export default {
  name: "ProductDetail",
  data: () => ({
    model: 0,
    colors: ["primary", "secondary"],
    productName: "Bershka 女士 2020新款简约V领短款气质针织开衫",
    price: 999,
    rating: 4,
    rateList: [10, 20, 30, 20, 20],
  }),
};
</script>

