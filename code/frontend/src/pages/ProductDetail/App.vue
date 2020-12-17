<template>
  <v-app>
    <top-bar></top-bar>
    <v-main>
      <product-detail></product-detail>
    </v-main>
  </v-app>
</template>

<script>
import ProductDetail from './ProductDetail.vue';
import TopBar from '@/components/TopBar.vue';

export default {
  name: "App",
  components: {
    ProductDetail,
    TopBar,
  },
};
</script>
