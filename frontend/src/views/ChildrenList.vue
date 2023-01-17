<template>
  <div>
    <b-container fluid="xl" class="border my-5">
      <b-container class="my-5" v-show="seigi_bool">
        <router-link
          :to="{ name: 'child_create',
            params: {
              parent_id: parent_id
            } }">
          <b-button class="text-light" variant="primary">新規登録</b-button>
        </router-link>
      </b-container>
      <b-container class="my-3">
        <h2>見積内容</h2>
      </b-container>
      <b-row>
        <b-col class="bg-dark border text-light" cols="2">品目ID</b-col>
        <b-col class="bg-dark border text-light" cols="5">品名</b-col>
        <b-col class="bg-dark border text-light" cols="5">図番</b-col>
      </b-row>
      <b-row v-for="child in children" :key="child.child_id">
        <b-col class="border" cols="2">
          <router-link
            :to="{ name: 'child', params: { parent_id: parent_id, child_id: child.child_id } }"
            >{{ child.child_id }}
          </router-link>
        </b-col>
        <b-col class="border" cols="5">{{ child.child_name }}</b-col>
        <b-col class="border" cols="5">{{ child.child_figure_number }}</b-col>
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
    }
  },
  data() {
    return {
      children: null,
      group: null,
      seigi_bool: null,
      SEIGI: 3 // 生技のグループID
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
        method: "get",
        url: `/parents/${this.parent_id}/children/`
      }).then(response => {
        this.children = response.data
      })
      api({
        method: "GET",
        url: `/getusers2/${this.username}/`
      }).then(response =>{
        this.group = response.data[0].groups
        this.seigi_bool = this.group.includes(this.SEIGI)
      })
    }
  },
  created() {
    this.getData()
  }
}
</script>
