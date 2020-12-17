<template>
  <v-app>
    <top-bar></top-bar>
    <v-main>
      <saler-info></saler-info>
    </v-main>
  </v-app>
</template>

<script>
import TopBar from "@/components/TopBar.vue";
import SalerInfo from "./SalerInfo.vue";

export default {
  name: "App",
  components: {
    SalerInfo,
    TopBar,
  },
};
</script>
