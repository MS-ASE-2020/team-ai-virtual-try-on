<template>
  <v-app>
    <top-bar></top-bar>
    <v-main>
      <customer-info></customer-info>
    </v-main>
    <my-footer></my-footer>
  </v-app>
</template>

<script>
import TopBar from "@/components/TopBar.vue";
import CustomerInfo from "./CustomerInfo.vue";
import MyFooter from "@/components/MyFooter.vue";

export default {
  name: "App",

  components: {
    CustomerInfo,
    TopBar,
    MyFooter,
  },
};
</script>
