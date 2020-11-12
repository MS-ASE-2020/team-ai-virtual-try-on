<template>
  <v-container v-if="userData">
    <v-responsive max-width="1368" class="mx-auto">
      <v-row>
        <v-spacer></v-spacer>
        <v-col cols="12" md="5">
          <v-row justify="center" class="mt-md-16 mb-5">
            <v-img
              height="400"
              tile
              contain
              :src="userData.self_pics"
            ></v-img>
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
            <p>用户ID：{{ userData.name }}</p>
          </v-row>
          <v-row align="center">
            <p>性别：{{ userGender }}</p>
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
import axios from "axios";
import rqt from "@/variables.js";

export default {
  name: "CustomerInfo",
  data: () => ({
    userData: null,
    model: 0,
    colors: ["primary", "secondary"],
    userID: "testtesttest",
    userGender: "男",
  }),
  async beforeCreate() {
    const urlParams = new URLSearchParams(window.location.search);
    const name = urlParams.get("id");
    try {
      const response = await axios.get(
        rqt.api + "/api/customers/" + name + "/"
      );
      this.userData = response.data;
      console.log(response);
    } catch (error) {
      console.error(error);
    }
  },
};
</script>

