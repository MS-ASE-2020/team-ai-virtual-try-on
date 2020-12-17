<template>
  <v-app>
    <top-bar></top-bar>
    <v-main>
      <search-page></search-page>
    </v-main>
    <my-footer></my-footer>
  </v-app>
</template>

<script>
import TopBar from "@/components/TopBar.vue";
import SearchPage from "./Search.vue";
import MyFooter from "@/components/MyFooter.vue";

export default {
  name: "App",
  components: { TopBar, SearchPage, MyFooter },
};
</script>
