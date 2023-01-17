<template>
  <div>
    <b-container class="mt-3">
      <b-row>
        <b-col cols="5" md="4"><h3>工程フロー</h3></b-col>
        <b-col v-show="this.seigi_bool">
          <router-link
            :to="{ name: 'process_flow_editor', params: { parent_id: parent_id, child_id: child_id } }"
          >
            <b-button variant="warning" class="text-dark mx-1">編集</b-button>
          </router-link>
        </b-col>
      </b-row>
    </b-container>
    <b-container class="mb-5">
      <b-row>
        <b-col class="bg-dark border text-light" cols="2">工程番号</b-col>
        <b-col class="bg-dark border text-light" cols="2">工程名</b-col>
        <b-col class="bg-dark border text-light" cols="2">加工場所</b-col>
        <b-col class="bg-dark border text-light">外注先</b-col>
      </b-row>
      <b-row v-for="operation in operations" :key="operation.index">
          <b-col class="border" cols="2">{{ operation.index + 1 }}</b-col>
          <b-col class="border" cols="2">{{ operation.operation_name }}</b-col>
          <b-col class="border" cols="2">
            <div v-if="operation.is_outsourcing == 1">外注</div>
            <div v-else-if="operation.is_outsourcing == 0 || operation.is_outsourcing == 2">社内</div>
          </b-col>
          <b-col class="border">{{ operation.company_name }}</b-col>
        </b-row>
    </b-container>
  </div>
</template>

<script>
import api from "@/services/api"

export default {
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
      group: null,
      seigi_bool: null,
      operations: null,
      SEIGI: 3 // 生技のグループID
    }
  },
  computed: {
    username: function() {
      return this.$store.state.auth.username
    }
  },
  methods: {
    getData: function() {
      api({
        method: "GET",
        url: `/getusers2/${this.username}/`
      }).then(response =>{
        this.group = response.data[0].groups
        this.seigi_bool = this.group.includes(this.SEIGI)
      })
      api({
        method: "GET",
        url: `/get_children_operations/${this.child_id}/`,
      }).then(response => {
        this.operations = response.data
      })
    }
  },
  created() {
    this.getData()
  }
}
</script>
