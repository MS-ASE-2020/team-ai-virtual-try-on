<template>
  <v-container>
    <v-responsive max-width="1368" class="mx-auto">
      <v-row>
        <v-col
          v-for="(item, i) in clothList"
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
              @mouseenter="getSynImage(i)"
            >
              <v-img contain height="300" :src="item.pics">
                <v-expand-transition>
                  <v-img
                    v-if="hover"
                    class="d-flex transition-fast-in-fast-out v-card--reveal display-3"
                    style="height: 100%"
                    :src="
                      clothList[i].synImage ? clothList[i].synImage : testImg
                    "
                  >
                  </v-img>
                </v-expand-transition>
              </v-img>
              <v-card-title style="font-size: 15px">
                <!-- Bershka 女士 2020新款简约V领短款气质针织开衫 -->
                {{ item.name }}
              </v-card-title>
              <v-card-subtitle>
                <strong class="red--text">
                  ￥ <span style="font-size: 15px"> {{ item.price }} </span>
                </strong>
              </v-card-subtitle>
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
import axios from "axios";

export default {
  name: "Search",
  data: () => ({
    page: 1,
    clothList: null,
    testImg: "https://cdn.vuetifyjs.com/images/cards/cooking.png",
  }),
  async beforeCreate() {
    // const urlParams = new URLSearchParams(window.location.search)
    // const searchWord = urlParams.get("q")
    try {
      const response = await axios.get("/api/products/");
      console.log(response);
      this.clothList = response.data;
    } catch (error) {
      console.error(error);
    }
  },

  methods: {
    getSynImage(i) {
      const name = localStorage.getItem("name");
      const id = localStorage.getItem("isSaler");

      if (!name || id === "y" || this.clothList[i].synImage) {
        return;
      }
      const url =
        "/api/tryon?" +
        "customer_name=" +
        name +
        "&product_id=" +
        this.clothList[i].id;
      axios
        .get(url)
        .then((response) => {
          const data = response.data;
          console.log(data[0].url);
          this.clothList[i].synImage =
            // "/media/tryon/0000_9cde8835-9079-4863-9008-a5c03be69a4f.jpg"; // TODO
            this.clothList[i].synImage = data[0].url;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

