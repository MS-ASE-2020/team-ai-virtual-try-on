<template>
  <v-app>
    <v-app-bar app color="transparent" flat dense>
      <v-spacer></v-spacer>

      <!-- <v-btn icon small color="grey" class="mx-1"> -->
      <signinup />
      <!-- </v-btn> -->
    </v-app-bar>
    <v-main>
      <homepage />
    </v-main>
  </v-app>
</template>

<script>
import homepage from "./HomePage";
import signinup from "@/components/SignInUp";

export default {
  name: "App",

  components: {
    homepage,
    signinup,
  },

  data: () => ({
    //
  }),

  methods: {
    foo() {
      window.location.href = "/customerinfo";
    },
  },
};
</script>
