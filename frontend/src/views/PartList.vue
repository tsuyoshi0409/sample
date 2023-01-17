<template>
  <div>
    <b-container fluid="xl" class="mt-3 border">
      <b-row>
        <b-col cols="3" md="2"><h3>購入品</h3></b-col>
        <b-col v-show="this.seigi_bool">
          <router-link
            :to="{ name: 'part_editor', params: { parent_id: parent_id } }"
          >
            <b-button variant="warning" class="text-dark mx-1">編集</b-button>
          </router-link>
        </b-col>
      </b-row>
    </b-container>
    <b-container fluid="xl">
      <b-row>
        <b-col class="bg-dark border text-light" cols="2">購入品ID</b-col>
        <b-col class="bg-dark border text-light" cols="5">部品名</b-col>
        <b-col class="bg-dark border text-light" cols="5">仕入先</b-col>
      </b-row>
      <b-row v-for="part in parts" :key="part.part_id">
        <b-col class="border" cols="2">{{ part.part_id }}</b-col>
        <b-col class="border" cols="5">{{ part.part_name }}</b-col>
        <b-col class="border" cols="5">{{ part.company_name }}</b-col>
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
      parts: null,
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
        url: `/parents/${this.parent_id}/parts/`
      }).then(response => {
        this.parts = response.data
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