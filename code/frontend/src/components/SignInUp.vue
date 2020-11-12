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
                          @change="selectFile"
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
import axios from "axios";
import rqt from "@/variables.js";

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
    // function getCookieName(k) {
    //   return (document.cookie.match("(^|; )" + k + "=([^;]*)") || 0)[2];
    // }
    this.userName = sessionStorage.getItem("name");
  },
  methods: {
    signOut() {
      try {
        if (sessionStorage.getItem("isSaler") === "n") {
          axios.get(rqt.api + "/api/customer/logout");
        } else if (this.sName) {
          axios.get(rqt.api + "/api/saler/logout");
        }
      } catch (error) {
        alert(error);
        return;
      }
      sessionStorage.clear();
      window.location.href = "/";
    },
    clickIcon() {
      let id = sessionStorage.getItem("isSaler");
      if (this.userName) {
        if (id === "n") {
          window.location.href = "/customerinfo?id=" + this.cName;
        } else {
          window.location.href = "/salerinfo?id=" + this.sName;
        }
      } else {
        this.dialog = true;
      }
    },
    selectFile(file) {
      this.currentFile = file;
    },
    signIn() {
      // alert("This feature has not been implemented!");
      let url = rqt.api;
      if (this.isSaler) {
        url += "/api/saler/login";
      } else {
        url += "/api/customer/login";
      }
      axios
        .post(url, this.signInData)
        .then((response) => {
          console.log(response);
          confirm("Sign in successfully!");
          let data = response.data;

          ////////////////////

          // axios
          //   .get(rqt.api + "/api/customers/" + data.name + "/")
          //   .then((response) => {
          //     console.log(response);
          //   })
          //   .catch((error) => {
          //     alert(error);
          //   });

          // axios
          //   .get(rqt.html + "/")
          //   .then((response) => {
          //     console.log(response);
          //   })
          //   .catch((error) => {
          //     alert(error);
          //   });

          ////////////////
          sessionStorage.setItem("name", data.name);
          if (data.is_saler) {
            sessionStorage.setItem("isSaler", "y");
            window.location.href = "/salerinfo";
          } else {
            sessionStorage.setItem("isSaler", "n");
            window.location.href = "/customerinfo";
          }
        })
        .catch((error) => {
          alert(error);
        });
    },
    signUp() {
      const formData = new FormData();

      Object.keys(this.signUpData).forEach((key) =>
        formData.append(key, this.signUpData[key])
      );
      let url = rqt.api;
      if (this.isSaler) {
        url += "/api/saler/signup";
      } else {
        url += "/api/customer/signup";
        formData.append("self_pics", this.currentFile);
      }
      axios
        .post(url, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          console.log(response);
          confirm("Sign up successfully!");
        })
        .catch((error) => {
          alert(error);
        });
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