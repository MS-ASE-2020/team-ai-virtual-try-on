<template>
  <v-container>
    <v-responsive max-width="1368" class="mx-auto">
      <v-row>
        <v-col
          v-for="item in clothList"
          :key="item.id"
          cols="12"
          sm="6"
          md="4"
          lg="3"
        >
          <v-hover v-slot="{ hover }">
            <v-card
              class="mx-auto"
              :href="'/productdetail?id=' + item.id"
              max-width="374"
            >
              <v-img contain height="300" :src="item.pics">
                <v-expand-transition>
                  <v-img
                    v-if="hover"
                    class="d-flex transition-fast-in-fast-out v-card--reveal display-3"
                    style="height: 100%"
                    src="https://cdn.vuetifyjs.com/images/cards/kitchen.png"
                  >
                  </v-img>
                </v-expand-transition>
              </v-img>
              <v-card-text>
                <!-- Bershka 女士 2020新款简约V领短款气质针织开衫 -->
                {{ item.name }}
              </v-card-text>
            </v-card>
          </v-hover>
        </v-col>
      </v-row>
      <v-row justify="center" class="my-12">
        <v-pagination
          v-if="clothList"
          v-model="page"
          :length="Math.ceil(clothList.length / 12)"
        ></v-pagination
      ></v-row>
    </v-responsive>
  </v-container>
</template>

<script>
import rqt from "@/variables.js";
import axios from "axios";

export default {
  name: "Search",
  data: () => ({
    page: 1,
    clothList: null,
  }),
  async beforeCreate() {
    // const urlParams = new URLSearchParams(window.location.search)
    // const searchWord = urlParams.get("q")
    try {
      const response = await axios.get(rqt.api + "/api/products/");
      console.log(response);
      this.clothList = response.data;
    } catch (error) {
      console.error(error);
    }
  },
};
</script>

