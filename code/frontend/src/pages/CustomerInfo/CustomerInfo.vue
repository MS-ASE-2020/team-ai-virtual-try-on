<template>
  <v-container v-if="userData">
    <v-responsive max-width="1368" class="mx-auto">
      <v-row>
        <v-spacer></v-spacer>
        <v-col cols="12" md="5">
          <v-row justify="center" class="mt-md-16 mb-5">
            <v-img height="400" tile contain :src="userData.self_pics"></v-img>
          </v-row>
          <v-row justify="center">
            <div>我的全身照</div>
          </v-row>
        </v-col>
        <v-col cols="12" md="7" class="px-16 py-md-16">
          <v-row class="py-6">
            <h2>个人信息</h2>
          </v-row>

          <v-row class="py-2" align="center">
            <div>用户ID：{{ userData.name }}</div>
          </v-row>
          <v-row class="py-2" align="center">
            <div>电话：</div>
            <div v-if="!tableStat.phone_number">
              {{ userData.phone_number }}
            </div>
            <v-sheet v-else width="200px" height="40px">
              <v-text-field
                autofocus
                dense
                flat
                solo
                outlined
                @blur="tableStat.phone_number = false"
                v-model="userData.phone_number"
              ></v-text-field>
            </v-sheet>
            <v-icon class="mx-2" @click="tableStat.phone_number = true">
              mdi-pencil
            </v-icon>
          </v-row>
          <v-row class="py-2" align="center">
            <div>密码：</div>
            <div v-if="!tableStat.password">********</div>
            <v-sheet v-else width="200px" height="40px">
              <v-text-field
                autofocus
                dense
                flat
                solo
                outlined
                label="********"
                @blur="tableStat.password = false"
                v-model="userData.password"
              ></v-text-field>
            </v-sheet>
            <v-icon class="mx-2" @click="tableStat.password = true">
              mdi-pencil
            </v-icon>
          </v-row>

          <v-row>
            <v-sheet class="mx-4 my-6" width="200">
              <v-file-input
                accept="image/*"
                show-size
                label="上传新照片"
                filled
                prepend-icon="mdi-camera"
                @change="
                  (file) => {
                    currentFile = file;
                  }
                "
              ></v-file-input>
            </v-sheet>
            <v-btn @click="updateProfile" class="mx-4 my-6" x-large
              >更新个人信息</v-btn
            >
          </v-row>
        </v-col>
        <v-spacer></v-spacer>
      </v-row>
    </v-responsive>
  </v-container>
</template>

<script>
import axios from "axios";
import getCookieName from '@/components/GetCookie'

export default {
  name: "CustomerInfo",
  data: () => ({
    userData: null,
    tableStat: {
      phone_number: false,
      password: false,
    },
    model: 0,
    colors: ["primary", "secondary"],
    userID: "testtesttest",
    userGender: "男",
    currentFile: null,
  }),
  async beforeCreate() {
    // const urlParams = new URLSearchParams(window.location.search);
    // const name = urlParams.get("id");
    const name = localStorage.getItem("name");
    try {
      const response = await axios.get("/api/customers/" + name + "/");
      this.userData = response.data;
      console.log(response);
    } catch (error) {
      console.error(error);
    }
  },
  methods: {
    updateProfile() {
      const formData = new FormData();
      console.log(this.currentFile);
      if (this.currentFile) {
        formData.append("self_pics", this.currentFile);
      }
      if (this.userData["password"]) {
        formData.append("password", this.userData["password"]);
      }
      formData.append("phone_number", this.userData["phone_number"]);

      axios
        .put("/api/customers/" + this.userData.name + "/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
            "X-CSRFToken": getCookieName("csrftoken"),
          },
        })
        .then((response) => {
          console.log(response);
          // confirm("Update profiles successfully!");
          window.location.reload();
        })
        .catch((error) => {
          alert(error);
        });
    },
  },
};
</script>

