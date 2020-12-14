<template>
  <div v-if="item">
    <v-dialog @input="$emit('input', $event)" :value="value" max-width="600px">
      <v-card>
        <v-card flat>
          <v-card-title>
            <span class="headline">Modify product</span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col cols="12" md="6">
                  <v-text-field
                    label="Product Name"
                    v-model="productInfo.name"
                    :placeholder="item.name"
                  ></v-text-field>
                </v-col>

                <v-col cols="12" md="6">
                  <v-text-field
                    label="Price"
                    v-model="productInfo.price"
                    :placeholder="item.price"
                  ></v-text-field>
                </v-col>

                <v-col cols="12">
                  <v-text-field
                    label="Link"
                    hint="Offer a link so that customers can find where to buy this product"
                    v-model="productInfo.link"
                    :placeholder="item.link"
                  ></v-text-field>

                  <v-col cols="12">
                    <v-file-input
                      accept="image/*"
                      show-size
                      label="Upload a product image"
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
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn text color="blue darken-1" @click="uploadProduct">
              UPLOAD
            </v-btn>
            <v-btn color="blue darken-1" text @click="$emit('input', false)">
              Cancel
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from "axios";
import getCookieName from '@/components/GetCookie'

export default {
  name: "ModifyProduct",
  props: {
    value: Boolean,
    item: Object,
  },
  data: () => ({
    productInfo: {
      name: null,
      price: null,
      link: null,
    },
    currentFile: null,
  }),
  methods: {
    uploadProduct() {
      const formData = new FormData();
      if (this.currentFile) {
        formData.append("pics", this.currentFile);
      }
      Object.keys(this.productInfo).forEach((key) => {
        if (this.productInfo[key]) {
          formData.append(key, this.productInfo[key]);
        }
      });
      axios
        .patch("/api/products/" + this.item.id + "/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
            "X-CSRFToken": getCookieName("csrftoken"),
          },
        })
        .then(() => {
          // confirm("Modify product successfully!");
          window.location.reload();
        })
        .catch((error) => {
          console.log(error);
          alert(error);
        });
    },
  },
};
</script>