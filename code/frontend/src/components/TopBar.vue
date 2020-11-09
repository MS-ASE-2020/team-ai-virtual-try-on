<template>
  <v-app-bar app color="" flat dense>
    <v-toolbar-title>
      <v-btn href="/" text> Virtual Try-On </v-btn>
    </v-toolbar-title>
    <v-sheet class="mx-4" height="40" width="360" color="transparent">
      <v-text-field
        @keypress.enter="search"
        single-line
        solo
        dense
        rounded
        prepend-inner-icon="mdi-magnify"
      >
      </v-text-field>
    </v-sheet>
    <v-spacer></v-spacer>
    <v-icon @click="bar">mdi-account</v-icon>
  </v-app-bar>
</template>

<script>
export default {
  name: "TopBar",
  methods: {
    search() {
      window.location.href = "/search" + "?q=" + this.searchInput;
    },
    bar(){
      window.location.href = "/customerinfo"
    }
  },
};
</script>