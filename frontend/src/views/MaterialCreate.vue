<template>
  <div id="create-page">
    <GlobalHeader />
    <GlobalMessage />
    <!-- メインエリア -->
    <main class="container mt-3 p-3">
      <p class="h5 mb-5">材料登録</p>
      <b-form v-on:submit.prevent="submitSave">
        <div class="row form-group">
          <label class="col-sm-3 col-form-label" for="material_shape"
            >材料形状</label
          >
          <div class="col-sm-8">
            <b-form-select id="material_big" v-model="material_shape">
              <option value="">----</option>
              <option value="材料形状1">材料形状1</option>
              <option value="材料形状2">材料形状2</option>
            </b-form-select>
          </div>
        </div>
        <div class="row form-group">
          <label class="col-sm-3 col-form-label">材質</label>
          <div class="col-sm-8">
            <b-input type="text" class="form-control" v-model="material_sml_txt" />
          </div>
        </div>
        <div class="row form-group">
          <label class="col-sm-3 col-form-label">記号</label>
          <div class="col-sm-8">
            <b-input type="text" class="form-control" v-model="material_symbol" />
          </div>
        </div>
        <div class="row form-group">
          <label class="col-sm-3 col-form-label">硬度・仕上げ</label>
          <div class="col-sm-8">
            <b-input type="text" class="form-control" v-model="hardness" />
          </div>
        </div>
        <div class="row form-group">
          <label class="col-sm-3 col-form-label">板厚</label>
          <div class="col-sm-8">
            <b-input type="text" class="form-control" v-model="sheet_thickness" />
          </div>
        </div>
        <div class="row form-group">
          <label class="col-sm-3 col-form-label">W</label>
          <div class="col-sm-8">
            <b-input type="text" class="form-control" v-model="material_size_w" />
          </div>
        </div>
        <div class="row form-group">
          <label class="col-sm-3 col-form-label">L</label>
          <div class="col-sm-8">
            <b-input type="text" class="form-control" v-model="material_size_l" />
          </div>
        </div>

        <div class="row text-center mt-5">
          <div class="col-sm-12">
            <router-link
              :to="{
                  name: 'material_list',
                }"
                class="material-link"
            >
              <b-button variant="light" class="mx-1">戻る</b-button>
            </router-link>
            <b-button type="submit" variant="primary" class="mx-1">
              送信
            </b-button>
          </div>
        </div>
      </b-form>
    </main>
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
  name: "MaterialCreate",
  data() {
    return {
      // 入力フォームの内容
      material_shape: null,
      material_sml_txt: null,
      material_symbol: null,
      hardness: null,
      sheet_thickness: null,
      material_size_w: null,
      material_size_l: null
    };
  },
  methods: {
    submitSave: function() {
      api({
        method: "POST",
        url: "/materials/",
        data: {
          material_id: this.material_id,
          material_shape: this.material_shape,
          material_sml_txt: this.material_sml_txt,
          material_symbol: this.material_symbol,
          hardness: this.hardness,
          sheet_thickness: this.sheet_thickness,
          material_size_w: this.material_size_w,
          material_size_l: this.material_size_l,
        }
      }).then(response => {
        this.$router.push({
          name: "material",
          params: {
            material_id: response.data.material_id
          }
        });
      });
    }
  },
  created() {
    document.title = "Create - Material";
  }
};
</script>
