<template>
  <v-app>
    <v-app-bar app color="transparent" flat dense>
      <v-spacer></v-spacer>

      <!-- <v-btn icon small color="grey" class="mx-1"> -->
      <v-icon @click="foo">mdi-account</v-icon>
      <!-- </v-btn> -->
    </v-app-bar>
    <v-main>
      <homepage />
    </v-main>
  </v-app>
</template>

<script>
import homepage from "./HomePage";

export default {
  name: "App",

  components: {
    homepage,
  },

  data: () => ({
    //
  }),

  methods:{
    foo(){

    },
  }
};
</script>
