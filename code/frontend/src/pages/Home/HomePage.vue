<template>
  <v-container class="text-center">
    <v-responsive max-width="980" class="mx-auto">
      <v-row>
        <v-col cols="12" class="mt-10 my-5">
          <h1>Virtual Try-On</h1>
          <!-- A logo should be placed here -->
        </v-col>
      </v-row>

      <v-row>
        <v-spacer> </v-spacer>
        <v-col cols="8">
          <v-text-field
            @keypress.enter="search"
            @click:prepend-inner="search"
            prepend-inner-icon="mdi-magnify"
            rounded
            single-line
            outlined
            label=""
            v-model="searchInput"
          >
          </v-text-field>
        </v-col>
        <v-spacer> </v-spacer>
      </v-row>
      <v-row>
        <v-col>
          <v-btn class="mx-4" @click="search">搜索</v-btn>
          <v-btn class="mx-4" @click="lucky">运气不错</v-btn>
        </v-col>
      </v-row>
    </v-responsive>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "HomePage",
  data: () => ({
    searchInput: "",
  }),
  methods: {
    search() {
      if (this.searchInput) {
        window.location.href = "/search" + "?q=" + this.searchInput;
      } else {
        window.location.href = "/search";
      }
    },
    lucky() {
      axios
        .get("/api/products/")
        .then((response) => {
          console.log(response);
          let ra = Math.floor(Math.random() * response.data.length);
          window.location.href = "/productdetail?id=" + response.data[ra].id;
        })
        .catch((error) => {
          alert(error);
        });
    },
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap");

h1 {
  font-family: "Dancing Script", cursive;
  font-size: 45px;
}
</style>