<template>
  <v-dialog v-model="dialog" max-width="600px">
    <template v-slot:activator="{ on, attrs }">
      <v-icon v-bind="attrs" v-on="on">mdi-account</v-icon>
    </template>

    <v-card>
      <v-tabs v-model="tab" centered icons-and-text>
        <v-tabs-slider></v-tabs-slider>
        <v-tab v-for="item in keyList" :key="item.name">
          {{ item.name }}
        </v-tab>
      </v-tabs>

      <v-tabs-items v-model="tab">
        <v-tab-item v-for="item in keyList" :key="item.name">
          <v-card flat>
            <v-card-title>
              <span class="headline">{{ item.name }}</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12">
                    <v-row class="px-3" align="center">
                      <div class="py-auto" style="font-size: 16px">I'm a</div>
                      <v-radio-group class="mx-3" v-model="isSaler" row>
                        <v-radio label="Customer"></v-radio>
                        <v-radio label="Saler"></v-radio>
                      </v-radio-group>
                    </v-row>
                  </v-col>

                  <v-col cols="12" md="6">
                    <v-text-field
                      label="Name*"
                      hint="Your name should be unique from others"
                      required
                    ></v-text-field>
                  </v-col>

                  <v-col v-if="item.showStat" cols="12" md="6">
                    <v-text-field
                      label="Phone number*"
                      hint="Any number string with length of 11"
                    ></v-text-field>
                  </v-col>

                  <v-col cols="12">
                    <v-text-field
                      label="Password*"
                      type="password"
                      required
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
              <small>*indicates required field</small>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="dialog = false">
                {{ item.name }}
              </v-btn>
              <v-btn color="blue darken-1" text @click="dialog = false">
                Cancel
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-tab-item>
      </v-tabs-items>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "SignInUp",
  data: () => ({
    keyList: [
      { name: "Sign in", showStat: false },
      { name: "Sign up", showStat: true },
    ],
    isSaler: 0,
    dialog: false,
    tab: null,
  }),
};
</script>