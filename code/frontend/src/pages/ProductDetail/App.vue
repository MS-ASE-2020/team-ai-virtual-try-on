<template>
  <v-app>
    <topbar />
    <v-main>
      <productdetail />
    </v-main>
  </v-app>
</template>

<script>
import productdetail from "./ProductDetail";
import topbar from "@/components/TopBar";

export default {
  name: "App",

  components: {
    productdetail,
    topbar,
  },

  data: () => ({
    //
  }),

  methods: {
    foo() {},
  },
};
</script>
