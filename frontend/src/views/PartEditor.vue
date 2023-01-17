<template>
  <div id="edit-page">
    <GlobalHeader />
    <GlobalMessage />
    <!-- メインエリア -->
    <b-container class="my-3">
      <h2>購入品</h2>
      <b-container>
        <b-form v-on:submit.prevent="submitSave">
          <b-row>
            <b-col>
              <label class="font-weight-bold">購入品名</label>
            </b-col>
          </b-row>
          <b-row class="mb-3">
            <b-col cols="4">
              <b-form-input type="text" v-model="part_name" />
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <label class="font-weight-bold">仕入先</label>
            </b-col>
          </b-row>
          <b-row class="mb-3">
            <b-col cols="9" md="6">
              <v-autocomplete
                v-model="company_id"
                :items="company_list"
                item-text="company_name"
                item-value="company_id"
              ></v-autocomplete>
            </b-col>
          </b-row>
          <div class="row text-center mt-5">
            <div class="col-sm-12">
              <router-link
                :to="{
                    name: 'parent',
                    params: {
                      parent_id: parent_id
                    }
                  }"
              >
                <b-button variant="light" class="mx-1">戻る</b-button>
              </router-link>
              <b-button type="submit" variant="primary" class="mx-1">
                送信
              </b-button>
            </div>
          </div>
        </b-form>
      </b-container>
      <b-container class="my-5">
        <b-row>
          <b-col class="bg-dark border text-light">購入品名</b-col>
          <b-col class="bg-dark border text-light">仕入先</b-col>
          <b-col class="bg-dark border" cols="2"></b-col>
        </b-row>
        <b-row v-for="part in parts" :key="part.part_id">
          <b-col class="border">{{ part.part_name }}</b-col>
          <b-col class="border">{{ part.company_name }}</b-col>
          <b-col class="border" cols="2">
            <b-button
              variant="danger"
              @click="deletePart(part.part_id)"
            >削除</b-button>
          </b-col>
        </b-row>
      </b-container>
    </b-container>
  </div>
</template>

<script>
import api from "@/services/api"
import GlobalHeader from "@/components/GlobalHeader.vue"
import GlobalMessage from "@/components/GlobalMessage.vue"

export default {
  components: {
    GlobalHeader,
    GlobalMessage
  },
  props: {
    parent_id: {
      required: true
    }
  },
  data() {
    return {
      // 入力フォームの内容
      part_name: null,
      company_list: null,
      company_id: null,
      parts: null
    }
  },
  methods: {
    getCompany: function() {
      api({
        method: "GET",
        url: "/companies/"
      }).then(response => {
        this.company_list = response.data
      })
    },
    submitSave: function() {
      api({
        method: "POST",
        url: "/parts/",
        data: {
          part_name: this.part_name,
          company_id: this.company_id,
          parent_id: this.parent_id
        }
      }).then(response => {
        this.$router.go({
          name: "part_editor",
          params: {
            parent_id: response.data.parent_id
          }
        })
      })
    },
    getPart: function() {
      api({
        method: "GET",
        url: `/parents/${this.parent_id}/parts/`
      }).then(response => {
        this.parts = response.data
      })
    },
    deletePart: function(part_id) {
      api({
        method: "DELETE",
        url: `/parts/${part_id}/`
      }).then(
        this.$router.go({
          name: "part_editor",
          params: {
            parent_id: this.parent_id
          }
        })
      )
    }
  },
  created() {
    this.getCompany()
    this.getPart()
  }
}
</script>