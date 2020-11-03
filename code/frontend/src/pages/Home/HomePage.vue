<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12" class="mt-10 my-5">
        <h1>Virtual Try-On</h1>
      </v-col>

      <v-col cols="12">
        <v-card max-width="200">
          <v-text-field
            prepend-inner-icon="mdi-magnify"
            rounded
            single-line
            outlined
            label=""
          >
          </v-text-field>
        </v-card>
        <br />
        <v-btn class="mx-4">搜索</v-btn>
        <v-btn class="mx-4">运气不错</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "HomePage",
  data: () => ({
    //
  }),
};
</script>

<style scoped>
.search-width {
  width: 400px;
}
</style>