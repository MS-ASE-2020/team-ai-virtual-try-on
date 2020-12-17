<template>
  <v-app>
    <top-bar></top-bar>
    <v-main>
      <saler-info></saler-info>
    </v-main>
    <my-footer></my-footer>
  </v-app>
</template>

<script>
import TopBar from "@/components/TopBar.vue";
import SalerInfo from "./SalerInfo.vue";
import MyFooter from "@/components/MyFooter.vue";

export default {
  name: "App",
  components: {
    SalerInfo,
    TopBar,
    MyFooter,
  },
};
</script>
