<template>
  <v-container>
    <v-responsive max-width="1368" class="mx-auto">
    <v-row>
      <v-spacer></v-spacer>
      <v-col cols="12" md="5">
        <v-row justify="center" class="mt-md-16 mb-5">
          <!-- <v-carousel height="400" v-model="model" hide-delimiter-background hide-delimiters> -->
            <!-- <v-carousel-item v-for="color in colors" :key="color"> -->
              <!-- <v-sheet :color="color" height="100%" tile>
                <v-row class="fill-height" align="center" justify="center">
                  <div class="display-3">Slide {{ i + 1 }}</div>
                </v-row>
              </v-sheet> -->
              <v-img
                height="400"
                tile
                src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
              ></v-img>
            <!-- </v-carousel-item> -->
          <!-- </v-carousel> -->
        </v-row>
        <v-row justify="center">
          <p>我的全身照</p>
        </v-row>
      </v-col>
      <v-col cols="12" md="7" class="px-16 py-md-16">
        <v-row class="py-6">
          <h2>个人信息</h2>
        </v-row>

        <v-row align="center">
         <p>用户ID：{{userID}}</p>
        </v-row>
        <v-row align="center">
          <p>性别：{{userGender}}</p>
        </v-row>
        <v-row>
          <v-btn class="mx-4 my-6" x-large>上传新照片</v-btn>
          <v-btn class="mx-4 my-6" x-large>修改个人信息</v-btn>
        </v-row>
      </v-col>
      <v-spacer></v-spacer>
    </v-row>
    </v-responsive>
  </v-container>
</template>

<script>
export default {
  name: "CustomerInfo",
  data: () => ({
    model: 0,
    colors: ["primary", "secondary"],
    userID: "testtesttest",
    userGender: "男",
  }),
};
</script>

