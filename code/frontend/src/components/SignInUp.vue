<template>
  <div>
    <v-menu open-on-hover offset-y>
      <template v-slot:activator="{ on, attrs }">
        <v-icon v-bind="attrs" v-on="on" @click.stop="clickIcon"
          >mdi-account</v-icon
        >
      </template>

      <v-list dense v-if="userName">
        <v-list-item-group>
          <v-list-item>
            <v-list-item-title @click="signOut">Sign out</v-list-item-title>
          </v-list-item></v-list-item-group
        >
      </v-list>
    </v-menu>

    <v-dialog v-model="dialog" max-width="600px">
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
                        v-model="signUpData.name"
                      ></v-text-field>
                    </v-col>

                    <v-col v-if="item.showStat" cols="12" md="6">
                      <v-text-field
                        label="Phone number*"
                        hint="Any number string with length of 11"
                        v-model="signUpData.phone_number"
                      ></v-text-field>
                    </v-col>

                    <v-col cols="12">
                      <v-text-field
                        label="Password*"
                        type="password"
                        required
                        v-model="signUpData.password"
                      ></v-text-field>

                      <v-col v-if="item.showStat && !isSaler" cols="12">
                        <v-file-input
                          accept="image/*"
                          show-size
                          label="Upload a full-body image"
                          filled
                          prepend-icon="mdi-camera"
                          @change="
                            (file) => {
                              currentFile = file;
                            }
                          "
                        ></v-file-input>
                      </v-col>
                    </v-col>
                  </v-row>
                </v-container>
                <small>*indicates required field</small>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                  v-if="item.showStat"
                  text
                  color="blue darken-1"
                  @click="signUp"
                >
                  Sign Up
                </v-btn>
                <v-btn v-else color="blue darken-1" text @click="signIn">
                  Sign In
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
  </div>
</template>

<script>
import sign from "./sign";

export default {
  name: "SignInUp",
  data: () => ({
    keyList: [
      { name: "Sign in", showStat: false },
      { name: "Sign up", showStat: true },
    ],
    signUpData: {
      name: null,
      password: null,
      phone_number: null,
    },
    isSaler: 0,
    dialog: false,
    tab: null,
    currentFile: null,
    userName: null,
  }),
  created() {
    this.userName = localStorage.getItem("name");
    console.log(this.userName);
  },
  methods: {
    clickIcon() {
      let id = localStorage.getItem("isSaler");
      let name = localStorage.getItem("name");

      if (name) {
        if (id === "n") {
          window.location.href = "/customerinfo";
        } else {
          window.location.href = "/salerinfo";
        }
      } else {
        this.dialog = true;
      }
    },
    signIn() {
      sign.in(this.signInData, this.isSaler);
    },
    signOut() {
      sign.out();
    },
    signUp() {
      sign.up(this.signUpData, this.isSaler, this.currentFile);
    },
  },
  computed: {
    signInData() {
      let foo = this.signUpData;
      delete foo["phone_number"];
      return foo;
    },
  },
};
</script>