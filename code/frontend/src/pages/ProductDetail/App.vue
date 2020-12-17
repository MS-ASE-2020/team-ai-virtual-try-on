<template>
  <v-app>
    <top-bar></top-bar>
    <v-main>
      <product-detail></product-detail>
    </v-main>
    <my-footer></my-footer>
  </v-app>
</template>

<script>
import ProductDetail from './ProductDetail.vue';
import TopBar from '@/components/TopBar.vue';
import MyFooter from '@/components/MyFooter.vue';

export default {
  name: "App",
  components: {
    ProductDetail,
    TopBar,
    MyFooter,
  },
};
</script>
