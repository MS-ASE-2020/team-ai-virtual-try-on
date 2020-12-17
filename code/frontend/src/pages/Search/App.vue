<template>
  <v-app>
    <top-bar></top-bar>
    <v-main>
      <search-page></search-page>
    </v-main>
  </v-app>
</template>

<script>
import TopBar from "@/components/TopBar.vue";
import SearchPage from "./Search.vue";

export default {
  name: "App",
  components: { TopBar, SearchPage },
};
</script>
