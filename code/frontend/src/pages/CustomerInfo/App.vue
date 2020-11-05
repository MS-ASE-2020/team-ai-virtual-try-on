<template>
  <v-app>
    <topbar />
    <v-main>
      <customerinfo />
    </v-main>
  </v-app>
</template>

<script>
import customerinfo from "./CustomerInfo";
import topbar from "@/components/TopBar";

export default {
  name: "App",

  components: {
    customerinfo,
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
