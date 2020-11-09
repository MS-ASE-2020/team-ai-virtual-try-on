<template>
  <v-app>
    <topbar />
    <v-main>
      <salerinfo />
    </v-main>
  </v-app>
</template>

<script>
import salerinfo from "./SalerInfo";
import topbar from "@/components/TopBar";

export default {
  name: "App",

  components: {
    salerinfo,
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
