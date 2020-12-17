<template>
  <v-app>
    <v-app-bar app color="transparent" flat dense>
      <v-spacer></v-spacer>
      <sign-in-up></sign-in-up>
    </v-app-bar>
    <v-main>
      <home-page></home-page>
    </v-main>
  </v-app>
</template>

<script>
import HomePage from "./HomePage.vue";
import SignInUp from "@/components/SignInUp.vue";

export default {
  name: "App",

  components: {
    HomePage,
    SignInUp,
  },
};
</script>
