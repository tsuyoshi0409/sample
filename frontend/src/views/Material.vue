<template>
  <div>
    <GlobalHeader />
    <GlobalMessage />
    <b-container fluid="xl" class="my-5">
      <h2>材料詳細</h2>
    </b-container>
    <b-container fluid="xl" class="border my-5">
      <b-row>
        <b-col sm="1" class="bg-dark border text-light">材料ID</b-col>
        <b-col sm="2" class="bg-dark border text-light">材料形状</b-col>
        <b-col sm="2" class="bg-dark border text-light">材質</b-col>
        <b-col sm="2" class="bg-dark border text-light">記号</b-col>
        <b-col sm="2" class="bg-dark border text-light">硬度・仕上げ</b-col>
        <b-col sm="1" class="bg-dark border text-light">板厚</b-col>
        <b-col sm="1" class="bg-dark border text-light">W</b-col>
        <b-col sm="1" class="bg-dark border text-light">L</b-col>
      </b-row>
      <b-row>
        <b-col sm="1" class="border">{{ material.material_id }}</b-col>
        <b-col sm="2" class="border">{{ material.material_shape }}</b-col>
        <b-col sm="2" class="border">{{ material.material_sml_txt }}</b-col>
        <b-col sm="2" class="border">{{ material.material_symbol }}</b-col>
        <b-col sm="2" class="border">{{ material.hardness }}</b-col>
        <b-col sm="1" class="border">{{ material.sheet_thickness }}</b-col>
        <b-col sm="1" class="border">{{ material.material_size_w }}</b-col>
        <b-col sm="1" class="border">{{ material.material_size_l }}</b-col>
      </b-row>
    </b-container>
    <b-container fluid="xl" class="my-5 text-center">
      <router-link
        :to="{
          name: 'material_list'
        }"
        class="material-link"
      >
        <b-button class="text-white mx-1" variant="primary">戻る</b-button>
      </router-link>
      <router-link
        :to="{ name: 'material_editor', params: { material_id: material.material_id } }"
      >
        <b-button variant="warning" class="text-dark mx-1">編集</b-button>
      </router-link>
      <b-button @click="deleteMaterialData" class="text-dark mx-1" variant="danger">削除</b-button>
    </b-container>
    
  </div>
</template>

<script>
import api from "@/services/api";
import GlobalHeader from "@/components/GlobalHeader.vue";
import GlobalMessage from "@/components/GlobalMessage.vue";

export default {
  components: {
    GlobalHeader,
    GlobalMessage
  },
  props: {
    material_id: {
      required: true
    }
  },
  data() {
    return {
      material: {}
    };
  },
  methods: {
    setPageTitle(title) {
      document.title = title;
    },
    getMaterialData: function() {
      api({
        method: "get",
        url: `/materials/${this.material_id}/`
      }).then(response => {
        this.material = response.data;
      });
    },
    deleteMaterialData: function() {
      var result = window.confirm('削除してもよろしいですか？')
      if(result) {
        api({
          method: "delete",
          url: `/materials/${this.material_id}/`
        }).then(() => {
          this.$router.push({
            name: "material_list"
          });
        });
      }
    }
  },
  created() {
    this.getMaterialData();
  }
};
</script>
