<template>
  <v-app-bar app color="" flat dense>
    <v-toolbar-title>
      <v-btn href="/" text class="text-capitalize font-weight-bold beauti-font"> Virtual Try-On </v-btn>
    </v-toolbar-title>
    <v-sheet class="mx-4" height="40" width="360" color="transparent">
      <v-text-field
        @keypress.enter="search"
        @click:prepend-inner="search"
        single-line
        solo
        dense
        rounded
        prepend-inner-icon="mdi-magnify"
        v-model="searchInput"
      >
      </v-text-field>
    </v-sheet>
    <v-spacer></v-spacer>
    <signinup />
  </v-app-bar>
</template>

<script>
import signinup from "@/components/SignInUp";

export default {
  name: "TopBar",
  components: {
    signinup,
  },
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
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap");

.beauti-font {
  font-family: "Dancing Script", cursive;
  font-size: 17px;
}
</style>