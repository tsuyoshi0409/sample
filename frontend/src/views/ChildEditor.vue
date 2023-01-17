<template>
  <div id="edit-page">
    <GlobalHeader />
    <GlobalMessage />
    <!-- メインエリア -->
    <b-container class="mt-3">
      <h2>見積内容編集</h2>
    </b-container>
    <b-container class="mb-5">
      <b-form v-on:submit.prevent="submitSave">
      <b-container class="border">
        <h5 class="mt-3">製品情報</h5>
        <b-row>
          <b-col>
            <label class="font-weight-bold">品名</label>
          </b-col>
        </b-row>
        <b-row class="mb-3">
          <b-col>
            <b-form-input type="text" v-model="child_name" />
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <label class="font-weight-bold">図番</label>
          </b-col>
        </b-row>
        <b-row class="mb-3">
          <b-col>
            <b-form-input type="text" v-model="child_figure_number" />
          </b-col>
        </b-row>
      </b-container>
      <b-container class="border mt-5">
        <h5 class="mt-3">材料</h5>
        <b-row>
          <b-col>
            <label class="font-weight-bold">材料種類</label>
          </b-col>
        </b-row>
        <b-row class="mb-3">
          <b-col cols="4" md="3">
            <b-form-select v-model="material_big" :options="material_big_options">
            </b-form-select>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <label class="font-weight-bold">材料ID</label>
          </b-col>
        </b-row>
        <b-row class="mb-3">
          <b-col cols="4" md="3">
            <v-autocomplete
              dense
              v-model="material_id"
              :items="material_list"
              item-text="material_id"
              @change="changeMaterial"></v-autocomplete>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <label class="font-weight-bold">材料形状</label>
          </b-col>
        </b-row>
        <b-row class="mb-3">
          <b-col cols="5" md="4">
            <b-form-input type="text" v-model="material_shape" />
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <label class="font-weight-bold">材質</label>
          </b-col> 
        </b-row>
        <b-row class="mb-3">
          <b-col cols="5" md="4">
            <b-form-input type="text" v-model="material_sml_txt" />
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <label class="font-weight-bold">記号</label>
          </b-col> 
        </b-row>
        <b-row class="mb-3">
          <b-col cols="5" md="4">
            <b-form-input type="text" v-model="material_symbol" />
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <label class="font-weight-bold">硬度・仕上げ</label>
          </b-col> 
        </b-row>
        <b-row class="mb-3">
          <b-col cols="5" md="4">
            <b-form-input type="text" v-model="hardness" />
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <label class="font-weight-bold">板厚</label>
          </b-col> 
        </b-row>
        <b-row class="mb-3">
          <b-col cols="5" md="4">
            <b-form-input type="text" v-model="sheet_thickness" @change="changePieceSeat" />
          </b-col>
          <b-col cols="1">
            <p>μm</p>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <label class="font-weight-bold">材料サイズW</label>
          </b-col> 
        </b-row>
        <b-row class="mb-3">
          <b-col cols="5" md="4">
            <b-form-input type="text" v-model="material_size_w" @change="changePieceSeat" />
          </b-col>
          <b-col cols="1">
            <p>mm</p>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <label class="font-weight-bold">材料サイズL</label>
          </b-col> 
        </b-row>
        <b-row class="mb-3">
          <b-col cols="5" md="4">
            <b-form-input type="text" v-model="material_size_l" @change="changePieceSeat" />
          </b-col>
          <b-col cols="1">
            <p>mm</p>
          </b-col>
        </b-row>
      </b-container>
      <b-container class="border mt-5">
        <h5 class="mt-3">数</h5>
        <b-row>
          <b-col>
            <label class="font-weight-bold">数</label>
          </b-col>
        </b-row>
        <b-row>
          <b-col cols="4" md="3">
            <b-form-input
              type="number"
              v-model="imposition_amount_piece_seat"
            />
          </b-col>
          <b-col cols="4" md="3">
            <p>個/シート</p>
          </b-col>
        </b-row>
        <b-row>
          <b-col cols="4" md="3">
            <b-form-input
              type="number"
              v-model="imposition_amount_piece_flame"
            />
          </b-col>
          <b-col cols="4" md="3">
            <p>個/フレーム</p>
          </b-col>
        </b-row>
        <b-row class="mb-3">
          <b-col cols="4" md="3">
            <b-form-input
              type="number"
              v-model="imposition_amount_flame_seat"
            />
          </b-col>
          <b-col cols="4" md="3">
            <p>フレーム/シート</p>
          </b-col>
        </b-row>
      </b-container>
      <b-container class="border mt-5">
        <h5 class="mt-3">確認事項</h5>
        <b-form-textarea
          type="text"
          class="mb-3"
          rows="5"
          v-model="fixes"
        ></b-form-textarea>
      </b-container>
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
      child_name: null,
      child_figure_number: null,
      material_big: null,
      material_big_options: [
        { value: null, text: "----"},
        { value: 0, text: "材料1"},
        { value: 1, text: "材料2"},
        { value: 2, text: "材料3"}
      ],
      material_list: [],
      material_dict: {},
      material_id: null,
      material_shape: null,
      material_sml_txt: null,
      material_symbol: null,
      hardness: null,
      sheet_thickness: null,
      material_size_w: null,
      material_size_l: null,
      imposition_amount_piece_seat: null,
      imposition_amount_piece_flame: null,
      imposition_amount_flame_seat: null,
      fixes: null,
    }
  },
  computed: {
    username: function() {
      return this.$store.state.auth.username
    }
  },
  methods: {
    createDict: function() {
      // 材料情報取得
      api({
        method: "GET",
        url: "/materials/"
      }).then(response => {
        this.material_list = response.data;
        for (let i = 0; i < response.data.length; i++) {
          this.material_dict[response.data[i].material_id] = [response.data[i].material_shape, response.data[i].material_sml_txt, response.data[i].material_symbol, response.data[i].hardness, response.data[i].sheet_thickness, response.data[i].material_size_w, response.data[i].material_size_l]
        }
      })
    },
    changeMaterial() {
      if (this.material_id in this.material_dict) {
        this.material_shape = this.material_dict[this.material_id][0]
        this.material_sml_txt = this.material_dict[this.material_id][1]
        this.material_symbol = this.material_dict[this.material_id][2]
        this.hardness = this.material_dict[this.material_id][3]
        this.sheet_thickness = this.material_dict[this.material_id][4]
        this.material_size_w = this.material_dict[this.material_id][5]
        this.material_size_l = this.material_dict[this.material_id][6]
      } else {
        this.material_shape = null
        this.material_sml_txt = null
        this.material_symbol = null
        this.hardness = null
        this.sheet_thickness = null
        this.material_size_w = null
        this.material_size_l = null
      }
    },
    // 編集処理
    submitSave: function() {
      if (this.size_x == "") {
        this.size_x = null
      }
      if (this.size_y == "") {
        this.size_y = null
      }
      if (this.imposition_amount_piece_seat == "") {
        this.imposition_amount_piece_seat = null
      }
      if (this.imposition_amount_piece_flame == "") {
        this.imposition_amount_piece_flame = null
      }
      if (this.imposition_amount_flame_seat == "") {
        this.imposition_amount_flame_seat = null
      }
      api({
        method: "PATCH",
        url: `/children/${this.child_id}/`,
        data: {
          child_name: this.child_name,
          child_figure_number: this.child_figure_number,
          material_big: this.material_big,
          material_id: this.material_id,
          material_shape: this.material_shape,
          material_sml_txt: this.material_sml_txt,
          material_symbol: this.material_symbol,
          hardness: this.hardness,
          sheet_thickness: this.sheet_thickness,
          material_size_w: this.material_size_w,
          material_size_l: this.material_size_l,
          imposition_amount_piece_seat: this.imposition_amount_piece_seat,
          imposition_amount_piece_flame: this.imposition_amount_piece_flame,
          imposition_amount_flame_seat: this.imposition_amount_flame_seat,
          fixes: this.fixes,
          size_x: this.size_x,
          size_y: this.size_y,
        }
      }).then(response => {
        this.$router.push({
          name: "child",
          params: {
            parent_id: response.data.parent_id,
            child_id: response.data.child_id
          }
        });
      });
    }
  },
  // フォームに初期値をセット
  async beforeRouteEnter(to, from, next) {
    let endpoint = `/children/${to.params.child_id}/`
    let data = await api({ url: endpoint })
    return next(vm => {
      (vm.child_name = data.data.child_name),
      (vm.child_figure_number = data.data.child_figure_number),
      (vm.material_big = data.data.material_big),
      (vm.material_id = data.data.material_id),
      (vm.material_shape = data.data.material_shape),
      (vm.material_sml_txt = data.data.material_sml_txt),
      (vm.material_symbol = data.data.material_symbol),
      (vm.hardness = data.data.hardness),
      (vm.sheet_thickness = data.data.sheet_thickness),
      (vm.material_size_w = data.data.material_size_w),
      (vm.material_size_l = data.data.material_size_l),
      (vm.imposition_amount_piece_seat =
        data.data.imposition_amount_piece_seat),
      (vm.imposition_amount_piece_flame =
        data.data.imposition_amount_piece_flame),
      (vm.imposition_amount_flame_seat =
        data.data.imposition_amount_flame_seat),
      (vm.fixes = data.data.fixes),
      (vm.size_x = data.data.size_x),
      (vm.size_y = data.data.size_y)
    })
  },
  created() {
    this.createDict()
  }
};
</script>
