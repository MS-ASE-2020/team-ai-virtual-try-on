<template>
  <v-container>
    <v-responsive max-width="1368" class="mx-auto">
      <v-row v-if="clothList">
        <v-col
          v-for="(item, i) in clothList.slice(
            (page - 1) * 12,
            Math.min(page * 12, clothList.length)
          )"
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
              @mouseenter="getSynImage(i + (page - 1) * 12)"
            >
              <v-img
                contain
                max-height="350"
                :src="(isSearch ? '/media/' : '') + item.pics"
              >
                <v-fade-transition>
                  <v-sheet  v-if="hover" color="transparent">
                  <v-progress-circular
                    v-if="sendRQT[item.id] && !item.synImage"
                    :size="50"
                    color="primary"
                    indeterminate
                  ></v-progress-circular>
                  <v-img
                    v-if="item.synImage"
                    class="d-flex transition-fast-in-fast-out v-card--reveal display-3"
                    contain
                    style="height: 100%"
                    :src="item.synImage"
                  >
                  </v-img>
                  </v-sheet>
                </v-fade-transition>
              </v-img>
              <v-card-title style="font-size: 15px">
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
    clothList: [],
    isSearch: false,  // TOO UGLY
    sendRQT: {},
    testImg: "https://cdn.vuetifyjs.com/images/cards/cooking.png",
  }),
  async beforeCreate() {
    const urlParams = new URLSearchParams(window.location.search);
    const searchWord = urlParams.get("q");
    try {
      let response = null;
      if (searchWord) {
        response = await axios.get("/api/search/?name=" + searchWord);
        this.isSearch = true;
      } else {
        response = await axios.get("/api/products/");
      }
      console.log(response);
      this.clothList = Object.assign([], this.clothList, response.data);
      console.log(this.clothList);
    } catch (error) {
      console.error(error);
    }
  },

  methods: {
    getSynImage(i) {
      const name = localStorage.getItem("name");
      const id = localStorage.getItem("isSaler");

      if (
        !name ||
        id === "y" ||
        this.clothList[i].synImage ||
        this.sendRQT[this.clothList[i].id]
      ) {
        return;
      }
      this.sendRQT[this.clothList[i].id] = true;
      const url =
        "/api/tryon?" +
        "customer_name=" +
        name +
        "&product_name=" +
        this.clothList[i].id;
      axios
        .get(url)
        .then((response) => {
          const data = response.data;
          console.log(data[0].url);
          let foo = this.clothList[i]
          foo.synImage = data[0].url
          this.$set(this.clothList, i ,foo)
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

