<template>
  <div>
    <b-container class="mt-3">
      <b-row>
        <b-col cols="5" md="4"><h3>社内特殊工程</h3></b-col>
        <b-col v-show="this.seigi_bool">
          <router-link
            :to="{ name: 'special_process_editor', params: { parent_id: parent_id, child_id: child_id } }"
          >
            <b-button variant="warning" class="text-dark mx-1">編集</b-button>
          </router-link>
        </b-col>
      </b-row>
    </b-container>
    <b-container>
      <b-row>
        <b-col class="bg-dark border text-light">工程名</b-col>
      </b-row>
      <b-row v-for="operation in operations" :key="operation.operation_id">
        <b-col class="border">{{ operation.operation_name }}</b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import api from "@/services/api"

// グループID
const SEIGI = 3; // 生技

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
    };
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
        this.seigi_bool = this.group.includes(SEIGI)
      })
      api({
        method: "GET",
        url: `/getoperations/${this.child_id}/2/`,
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
