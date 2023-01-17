<template>
  <div id="home-page">
    <GlobalHeader />
    <GlobalMessage />
    <b-container fluid="xl">
      <div class="my-5">
        <a href="/material_create">
          <b-button variant="primary" class="text-white">新規登録</b-button>
        </a>
      </div>
    </b-container>
    <b-container fluid="xl" class="border my-5">
      <div class="my-5">
        <b-row class="my-1">
          <b-col sm="2">原材料ID</b-col>
          <b-col sm=4>
            <input class="form-control mr-sm-2" type="text" v-model="Q_material_id" />
          </b-col>
          <b-col sm="2">材料形状</b-col>
          <b-col sm="4">
            <b-form-select v-model="Q_material_shape" :options="options_material_shape">
            </b-form-select>
          </b-col>
        </b-row>
        <b-row class="my-1">
          <b-col sm="2">材質</b-col>
          <b-col sm="4">
            <b-form-select v-model="Q_material_sml_txt" :options="options_material_sml_txt">
            </b-form-select>
          </b-col>
          <b-col sm="2">記号</b-col>
          <b-col sm="4">
            <b-form-select v-model="Q_material_symbol" :options="options_material_symbol">
            </b-form-select>
          </b-col>
        </b-row>
      </div>

      <div class="text-center my-5">
        <button class="btn btn-outline-success" v-on:click.prevent="getArticles()">
          検索
        </button>
      </div>
    </b-container>
    <b-container fluid="xl" class="my-5">
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
      <div v-for="material in materials" :key="material.material_id">
        <b-row>
          <b-col sm="1" class="border">
            <router-link
              :to="{ name: 'material', params: { material_id: material.material_id } }"
              class="material-link"
              >{{ material.material_id }}
            </router-link>
          </b-col>
          <b-col sm="2" class="border">{{ material.material_shape }}</b-col>
          <b-col sm="2" class="border">{{ material.material_sml_txt }}</b-col>
          <b-col sm="2" class="border">{{ material.material_symbol }}</b-col>
          <b-col sm="2" class="border">{{ material.hardness }}</b-col>
          <b-col sm="1" class="border">{{ material.sheet_thickness }}</b-col>
          <b-col sm="1" class="border">{{ material.material_size_w }}</b-col>
          <b-col sm="1" class="border">{{ material.material_size_l }}</b-col>
        </b-row>
      </div>
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
  name: "home",
  data() {
    return {
      materials: "",
      next: null,
      previous: null,
      loadingMaterials: false,
      Q_material_id: "",
      Q_material_shape: "",
      Q_material_sml_txt: "",
      Q_material_symbol: "",
      Q_hardness: "",
      Q_sheet_thickness: "",
      material_shape_list: [],
      material_sml_txt_list: [],
      material_symbol_list: [],
      hardness_list: [],
      options_material_shape: [
        { value: '', text: '----'}
      ],
      options_material_sml_txt: [
        { value: '', text: '----'}
      ],
      options_material_symbol: [
        { value: '', text: '----'}
      ]
    };
  },
  methods: {
    getMaterials: function() {
      this.loadingMaterials = true;
      api({
        method: "get",
        url: "/materials/"
      }).then(response => {
        this.materials = response.data;
        this.loadingMaterials = false;
      });
    },
    getArticles: function() {
      api({
        method: "get",
        url: `/materials/?Q_material_id=${this.Q_material_id}&Q_material_shape=${this.Q_material_shape}&Q_material_sml_txt=${this.Q_material_sml_txt}&Q_material_symbol=${this.Q_material_symbol}&Q_hardness=${this.Q_hardness}&Q_sheet_thickness=${this.Q_sheet_thickness}`
      }).then(response => {
        this.materials = response.data
        this.loadingMaterials = false;
      })
    }
  },
  created() {
    this.getMaterials();
    document.title = "Material Board";
    api({
      method: "GET",
      url: "/materials/"
    }).then(response => {
      if (response.data) {
        for (let i = 0; i < response.data.length; i++) {
          this.material_shape_list.push(response.data[i].material_shape)
          this.material_sml_txt_list.push(response.data[i].material_sml_txt)
          this.material_symbol_list.push(response.data[i].material_symbol)
        }
        this.material_shape_list = Array.from(new Set(this.material_shape_list))
        this.material_sml_txt_list = Array.from(new Set(this.material_sml_txt_list))
        this.material_symbol_list = Array.from(new Set(this.material_symbol_list))
        for (let i = 0; i < this.material_shape_list.length; i++) {
          this.options_material_shape.push({value: this.material_shape_list[i], text: this.material_shape_list[i]})
        }
        for (let i = 0; i < this.material_sml_txt_list.length; i++) {
          this.options_material_sml_txt.push({value: this.material_sml_txt_list[i], text: this.material_sml_txt_list[i]})
        }
        for (let i = 0; i < this.material_symbol_list.length; i++) {
          this.options_material_symbol.push({value: this.material_symbol_list[i], text: this.material_symbol_list[i]})
        }
      }
    });
  }
};
</script>