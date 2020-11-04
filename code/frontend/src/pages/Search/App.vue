<template>
  <v-app>
    <v-app-bar app color="" flat dense>
      <v-toolbar-title>Virtual Try-On</v-toolbar-title>
      <v-sheet class="mx-4" height="40" width="360" color="transparent">
      <v-text-field single-line solo dense rounded prepend-inner-icon="mdi-magnify" > </v-text-field>
      </v-sheet>
      <v-spacer></v-spacer>
      <v-icon @click="foo">mdi-account</v-icon>
    </v-app-bar>
    <v-main>
      <search />
    </v-main>
  </v-app>
</template>

<script>
import search from "./Search";

export default {
  name: "App",

  components: {
    search,
  },

  data: () => ({
    //
  }),

  methods: {
    foo() {},
  },
};
</script>
