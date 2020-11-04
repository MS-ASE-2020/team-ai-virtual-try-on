<template>
  <v-container>
    <v-row>
      <v-spacer></v-spacer>
      <v-col cols="12" md="4">
        <v-row class="text-center">
          <v-col cols="12" class="py-md-16">
            <v-carousel
              v-model="model"
              hide-delimiter-background
              hide-delimiters
            >
              <v-carousel-item v-for="(color, i) in colors" :key="color">
                <v-sheet :color="color" height="100%" tile>
                  <v-row class="fill-height" align="center" justify="center">
                    <div class="display-3">Slide {{ i + 1 }}</div>
                  </v-row>
                </v-sheet>
              </v-carousel-item>
            </v-carousel>
          </v-col>
          <v-col cols="12">
            <v-btn class="mx-4">服装</v-btn>
            <v-btn class="mx-4">try on</v-btn>
          </v-col>
        </v-row>
      </v-col>
      <v-col cols="12" md="6" class="px-16 py-md-16">
        <v-row>
          <v-col cols="12" class="py-6">
            <h2>{{ productName }}</h2>
          </v-col>
          <v-col cols="12" class="py-6">
            <p>
              价格<span>{{ price }}</span>
            </p>
          </v-col>
          <v-col cols="2"><p>TryOn 评分</p> </v-col>
          <v-col cols="8">
            <v-rating
              v-model="rating"
              background-color="orange lighten-3"
              color="orange"
              length="5"
              large
              hover
              dense
            ></v-rating>
          </v-col>
          <v-col cols="12">
            <v-sheet width="300" class="mx-4">
              <div v-for="(rate, i) in rateList" :key="i">
                <v-row class="my-n3">
                  <v-col cols="2">{{ 5 - i }}分</v-col>
                  <v-col cols="10">
                    <v-progress-linear height="20" :value="rate">
                      <strong>{{ Math.ceil(rate) }}%</strong>
                    </v-progress-linear>
                  </v-col>
                </v-row>
              </div>
            </v-sheet>
          </v-col>
          <v-col cols="4" class="my-16">
            <v-btn x-large>立即购买</v-btn>
          </v-col>
          <v-col cols="4" class="my-16">
            <v-btn x-large>上传照片</v-btn>
          </v-col>

        </v-row>
      </v-col>
      <v-spacer></v-spacer>
    </v-row>
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

