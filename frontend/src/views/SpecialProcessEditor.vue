<template>
  <div id="edit-page">
    <GlobalHeader />
    <GlobalMessage />
    <!-- メインエリア -->
    <b-container class="my-3">
      <h2>社内特殊工程</h2>
      <b-container>
        <b-form v-on:submit.prevent="submitSave">
          <b-row>
            <b-col cols="4">
              <label class="font-weight-bold">工程名</label>
            </b-col>
          </b-row>
          <b-row class="mb-3">
            <b-col>
              <b-form-input type="text" v-model="operation_name" />
            </b-col>
          </b-row>
          <div class="row text-center mt-5">
            <div class="col-sm-12">
              <router-link
                :to="{
                    name: 'child',
                    params: {
                      parent_id: parent_id,
                      child_id: child_id
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
          <b-col class="bg-dark border text-light">工程名</b-col>
          <b-col class="bg-dark border" cols="2"></b-col>
        </b-row>
        <b-row v-for="operation in operations" :key="operation.operation_id">
          <b-col class="border">{{ operation.operation_name }}</b-col>
          <b-col class="border" cols="2">
            <b-button
              variant="danger"
              @click="deleteOperation(operation.operation_id)"
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
    },
    child_id: {
      required: true
    }
  },
  data() {
    return {
      // 入力フォームの内容
      operation_name: null,
      operations: null
    }
  },
  methods: {
    submitSave: function() {
      api({
        method: "POST",
        url: "/operations/",
        data: {
          operation_name: this.operation_name,
          company_id: this.company_id,
          is_outsourcing: 2,
          child_id: this.child_id,
          parent_id: this.parent_id
        }
      }).then(response => {
        this.$router.go({
          name: "special_process_editor",
          params: {
            parent_id: response.data.parent_id,
            child_id: response.data.child_id
          }
        })
      })
    },
    getOperation: function() {
      api({
        method: "GET",
        url: `/getoperations/${this.child_id}/2/`
      }).then(response => {
        this.operations = response.data
      })
    },
    deleteOperation: function(operation_id) {
      api({
        method: "DELETE",
        url: `/operations/${operation_id}/`
      }).then(
        this.$router.go({
          name: "outsourcing_editor",
          params: {
            parent_id: this.parent_id,
            child_id: this.child_id
          }
        })
      )
    }
  },
  created() {
    this.getOperation()
  }
}
</script>