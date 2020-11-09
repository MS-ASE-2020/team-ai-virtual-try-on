<template>
  <v-container>
    <v-responsive max-width="1368" class="mx-auto">
      <v-row>
        <v-spacer></v-spacer>

        <v-col cols="12" md="4" class="px-16 py-md-16">
          <v-row class="py-6">
            <h2>商家信息</h2>
          </v-row>

          <v-row align="center">
            <p>商家ID：{{ userID }}</p>
          </v-row>
        </v-col>

        <v-col cols="12" md="8">
          <v-row justify="center" class="mt-md-16 mb-5">
            <v-col v-for="i in 6" :key="i" cols="6" sm="4" md="6" lg="4">
              <v-hover v-slot="{ hover }">
                <v-card>
                  <v-img
                    height="300"
                    src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
                  >
                  </v-img>
                  <v-expand-transition>
                    <v-sheet v-if="hover" tile>
                      <v-card-text>
                        Bershka 女士 2020新款简约V领短款气质针织开衫
                      </v-card-text>
                    </v-sheet>
                  </v-expand-transition>
                </v-card>
              </v-hover>
            </v-col>
          </v-row>
        </v-col>

        <v-spacer></v-spacer>
      </v-row>
    </v-responsive>
  </v-container>
</template>

<script>
export default {
  name: "CustomerInfo",
  data: () => ({
    model: null,
    userID: "testtesttest",
  }),
};
</script>

