<template>
  <v-app-bar app color="" flat dense>
    <v-toolbar-title>
      <v-btn href="/" text> Virtual Try-On </v-btn>
    </v-toolbar-title>
    <v-sheet class="mx-4" height="40" width="360" color="transparent">
      <v-text-field
        @keypress.enter="bar"
        single-line
        solo
        dense
        rounded
        prepend-inner-icon="mdi-magnify"
      >
      </v-text-field>
    </v-sheet>
    <v-spacer></v-spacer>
    <v-icon @click="foo">mdi-account</v-icon>
  </v-app-bar>
</template>

<script>
export default {
  name: "TopBar",
  methods: {
    foo() {
      window.location.href = "/customerinfo";
    },
    bar() {
      window.location.href = "/search";
    },
  },
};
</script>