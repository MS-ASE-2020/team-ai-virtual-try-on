<template>
  <v-container v-if="userData">
    <v-responsive max-width="1368" class="mx-auto">
      <v-row>
        <v-spacer></v-spacer>

        <v-col cols="12" md="4" class="px-16 py-md-16">
          <v-row class="py-6">
            <h2>商家信息</h2>
          </v-row>

          <v-row align="center">
            <p>商家ID：{{ userData.name }}</p>
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
            <v-btn @click="updateProfile" class="mx-2 my-2" x-large
              >更新个人信息</v-btn
            >
          </v-row>
        </v-col>

        <v-col cols="12" md="8">
          <v-row class="mt-md-16 mb-5">
            <v-col cols="6" sm="4" md="6" lg="4">
              <v-hover v-slot="{ hover }">
                <v-card height="300" @click="createDialog = true">
                  <v-row class="fill-height" align="center" justify="center">
                    <v-scale-transition>
                      <v-icon class="mx-auto my-auto" :size="hover ? 100 : 50">
                        mdi-image-plus
                      </v-icon>
                    </v-scale-transition>
                  </v-row>
                </v-card>
              </v-hover>
            </v-col>
            <v-col
              v-for="(item, i) in productList"
              :key="item.id"
              cols="6"
              sm="4"
              md="6"
              lg="4"
            >
              <v-hover v-slot="{ hover }">
                <v-card>
                  <a :href="'/productdetail?id=' + item.id">
                    <v-img contain height="300" :src="item.pics"> </v-img>
                  </a>
                  <v-expand-transition>
                    <v-sheet v-if="hover" tile>
                      <v-card-title style="font-size: 15px">
                        <!-- Bershka 女士 2020新款简约V领短款气质针织开衫 -->
                        {{ item.name }}
                      </v-card-title>
                      <v-card-subtitle class="py-0">
                        <strong class="red--text">
                          ￥
                          <span style="font-size: 15px">
                            {{ item.price }}
                          </span>
                        </strong>
                      </v-card-subtitle>
                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn icon>
                          <v-icon
                            @click="
                              onEditItem = item;
                              modifyDialog = true;
                            "
                          >
                            mdi-pencil
                          </v-icon>
                        </v-btn>
                        <v-btn icon>
                          <v-icon @click="deleteProduct(i)">
                            mdi-trash-can-outline
                          </v-icon>
                        </v-btn>
                      </v-card-actions>
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
    <create-product v-model="createDialog"></create-product>
    <modify-product v-model="modifyDialog" :item="onEditItem"></modify-product>
  </v-container>
</template>

<script>
import axios from "axios";
import CreateProduct from "./CreateProduct";
import ModifyProduct from "./ModifyProduct";
import getCookieName from '@/components/GetCookie'

export default {
  name: "SalerInfo",
  components: {
    CreateProduct,
    ModifyProduct,
  },
  data: () => ({
    createDialog: false,
    modifyDialog: false,
    onEditItem: null,
    userData: null,
    productList: [],
    tableStat: {
      phone_number: false,
      password: false,
    },
  }),
  async beforeCreate() {
    const name = localStorage.getItem("name");
    try {
      const response = await axios.get("/api/salers/" + name + "/");
      this.userData = response.data;
      console.log(response);
    } catch (error) {
      console.error(error);
    }

    try {
      const allProduct = await axios.get("/api/products/");
      allProduct.data.forEach((item) => {
        if (item.owned_saler === this.userData.name) {
          this.productList.push(item);
        }
      });
      console.log(this.productList);
    } catch (error) {
      console.log(error);
    }
  },
  methods: {
    updateProfile() {
      const formData = new FormData();
      if (this.userData["password"]) {
        formData.append("password", this.userData["password"]);
      }
      formData.append("phone_number", this.userData["phone_number"]);

      axios
        .put("/api/salers/" + this.userData.name + "/", formData, {
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
    deleteProduct(idx) {
      axios
        .delete("/api/products/" + this.productList[idx].id + "/", {
          headers: {
            "X-CSRFToken": getCookieName("csrftoken"),
          },
        })
        .then(() => {
          // confirm("Successfully delete product!");
          window.location.reload();
        })
        .catch((error) => {
          alert(error);
        });
    },
  },
};
</script>

