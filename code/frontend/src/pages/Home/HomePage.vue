<template>
  <v-container class="text-center">
    <v-row>
      <v-col cols="12" class="mt-10 my-5">
        <h1>Virtual Try-On</h1>
        <!-- A logo should be placed here -->
      </v-col>
    </v-row>

    <v-row>
      <v-spacer> </v-spacer>
      <v-col cols="8">
        <v-text-field
          prepend-inner-icon="mdi-magnify"
          rounded
          single-line
          outlined
          label=""
        >
        </v-text-field>
      </v-col>
      <v-spacer> </v-spacer>
    </v-row>
    <v-row>
      <v-col>
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
