<template>
  <v-container>
    <v-row v-for="i in [1, 2]" :key="i">
      <v-col v-for="j in [1, 2, 3, 4]" :key="(i - 1) * 4 + j" cols="3">
        <v-hover v-slot="{ hover }">
          <v-card class="mx-auto" max-width="374">
            <v-img
              height="300"
              src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
            >
              <v-expand-transition>
                <v-img
                  v-if="hover"
                  class="d-flex transition-fast-in-fast-out v-card--reveal display-3"
                  style="height: 100%"
                  src="https://cdn.vuetifyjs.com/images/cards/kitchen.png"
                >
                </v-img>
              </v-expand-transition>
            </v-img>
            <v-card-text>
              Bershka 女士 2020新款简约V领短款气质针织开衫
            </v-card-text>
          </v-card>
        </v-hover>
      </v-col>
    </v-row>

    <v-row justify="center" class="my-12">
      <v-pagination v-model="page" :length="6"></v-pagination
    ></v-row>
  </v-container>
</template>

<script>
export default {
  name: "Search",
  data: () => ({ page: 1 }),
};
</script>

