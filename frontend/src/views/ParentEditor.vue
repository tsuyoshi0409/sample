<template>
  <div id="edit-page">
    <GlobalHeader />
    <GlobalMessage />
    <!-- メインエリア -->
    <b-container class="mt-3">
      <h2>見積依頼</h2>
    </b-container>
    <b-container>
      <b-form v-on:submit.prevent="submitSave" enctype="multipart/form-data">
        <b-container class="border">
          <h5 class="mt-3">製品情報</h5>
          <b-row>
            <b-col>
              <label class="font-weight-bold">(組図)品名</label>
            </b-col>
          </b-row>
          <b-row class="mb-3">
            <b-col>
              <b-input type="text" v-model="parent_name" />
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <label class="font-weight-bold">(組)図番</label>
            </b-col>
          </b-row>
          <b-row class="mb-3">
            <b-col>
              <b-input type="text" v-model="parent_figure_number" />
            </b-col>
          </b-row>
        </b-container>
        <b-container class="border mt-5">
          <h5 class="mt-3">顧客情報</h5>
          <b-row>
            <b-col>
              <label class="font-weight-bold">顧客名</label>
            </b-col>
          </b-row>
          <b-row class="mb-3">
            <b-col cols="12" md="9">
              <v-autocomplete v-model="customer_name" :items="customer_list" item-text="customer_name" label="顧客名" v-on:change=" changeCustomerId"></v-autocomplete>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <label class="font-weight-bold">顧客ID</label>
            </b-col>
          </b-row>
          <b-row class="mb-3">
            <b-col cols="5" md="3">
              <v-autocomplete v-model="customer_id" :items="customer_list" item-text="customer_id" label="顧客ID" v-on:change=" changeCustomerName"></v-autocomplete>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <label class="font-weight-bold">営業担当</label>
            </b-col>
          </b-row>
          <b-row class="mb-3">
            <b-col cols="5" md="3">
              <b-form-select
                v-model="sales" 
                :options="sales_list" 
              ></b-form-select>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <label class="font-weight-bold">アシスタント</label>
            </b-col>
          </b-row>
          <b-row class="mb-3">
            <b-col cols="5" md="3">
              <b-form-select
                v-model="assistant"
                :options="assistant_list"
              ></b-form-select>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <label class="font-weight-bold">生産管理</label>
            </b-col>
          </b-row>
          <b-row class="mb-3">
            <b-col cols="5" md="3">
              <b-form-select
                v-model="production_control"
                :options="production_control_list"
              ></b-form-select>
            </b-col>
          </b-row>
        </b-container>
        <b-container class="border mt-5">
          <h5 class="mt-3">見積情報</h5>
          <b-row>
            <b-col>
              <label class="font-weight-bold">必要数</label>
            </b-col>
          </b-row>
          <b-row class="mb-3">
            <b-col cols="4" md="3">
              <b-input type="text" v-model="necessary_amount" />
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <label class="font-weight-bold">納入形態</label>
            </b-col>
          </b-row>
          <b-row class="mb-3">
            <b-col cols="4" md="3">
              <b-form-select v-model="delivery_form" :options="delivery_form_options">
              </b-form-select>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <label class="font-weight-bold">見積回答</label>
            </b-col>
          </b-row>
          <b-row class="mb-3">
            <b-col cols="5" md="3">
              <b-input type="date" v-model="estimate_answer" />
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <label class="font-weight-bold">希望納期</label>
            </b-col>
          </b-row>
          <b-row class="mb-3">
            <b-col cols="5" md="3">
              <b-input type="date" v-model="desired_delivery_date" />
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
                v-on:change="change_material"></v-autocomplete>
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
              <b-form-input type="text" v-model="sheet_thickness" />
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
              <b-form-input type="text" v-model="material_size_w" />
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
              <b-form-input type="text" v-model="material_size_l" />
            </b-col>
            <b-col cols="1">
              <p>mm</p>
            </b-col>
          </b-row>
        </b-container>
        <b-container class="border mt-5">
          <h5 class="mt-3">類似品情報</h5>
          <b-row>
            <b-col>
              <label class="font-weight-bold">類似No.</label>
            </b-col>
          </b-row>
          <b-row class="mb-3">
            <b-col sm="6">
              <b-input type="text" v-model="similar_directions_number" />
            </b-col>
          </b-row>
        </b-container>
        <b-container class="border my-5">
          <h5 class="mt-3">添付ファイル</h5>
          <b-row>
            <b-col>
              <label class="font-weight-bold">現在のファイル</label>
            </b-col>
          </b-row>
          <b-row class="mb-3">
            <b-col sm="12">{{ this.file_name }}</b-col>
          </b-row>
          <b-row class="mb-3">
            <b-col>
              <input @change="selectedFile" type="file" name="file" />
            </b-col>
          </b-row>
        </b-container>
        <b-container class="border mt-5">
          <h5 class="mt-3">連絡事項</h5>
          <textarea
              type="text"
              class="form-control mb-3"
              rows="5"
              v-model="sales_prior_information"
            ></textarea>
        </b-container>
        <b-container class="text-center my-5">
          <div class="col-sm-12">
            <router-link
              :to="{
                  name: 'parent',
                  params: {
                    parent_id: parent_id
                  }
                }"
                class="parent-link"
            >
              <b-button variant="light" class="mx-1">戻る</b-button>
            </router-link>
            <b-button type="submit" variant="primary" class="mx-1">
              送信
            </b-button>
          </div>
        </b-container>
      </b-form>
    </b-container>
  </div>
</template>

<script>
import api from "@/services/api";
import api2 from "@/services/api2";
import GlobalHeader from "@/components/GlobalHeader.vue";
import GlobalMessage from "@/components/GlobalMessage.vue";
import moment from "moment";

// グループID
const SALES = 1; // 営業
const ASSISTANT = 2; // アシスタント
const PRODUCTION_CONTROL = 4; // 生産管理

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
      parent_name: null,
      parent_figure_number: null,
      necessary_amount: null,
      customer_list: [],
      customer_dict: {},
      customer_dict2: {},
      assistant_list: [
        {"value": null, "text": "----"}
      ],
      sales_list: [
        {"value": null, "text": "----"}
      ],
      production_control_list: [
        {"value": null, "text": "----"}
      ],
      customer_name: null,
      customer_id: null,
      assistant: null,
      sales: null,
      production_control: null,
      order_status: null,
      assy: null,
      estimate_answer: null,
      desired_delivery_date: null,
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
      delivery_form: null,
      delivery_form_options: [
        { value: null, text: "----"},
        { value: 0, text: "納入形態1"},
        { value: 1, text: "納入形態2"},
        { value: 2, text: "納入形態3"}
      ],
      sales_prior_information: null,
      production_checklist: null,
      similar_directions_number: null,
      product_affinity_number: null,
      formData: null,
      file: null,
      file_name: null,
      file_created_at: null,
      file_author: null,
      author: null,
    }
  },
  computed: {
    username: function() {
      return this.$store.state.auth.username
    }
  },
  methods: {
    change_material() {
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
    createDict: function() {
      // 材料情報取得
      api({
        method: "GET",
        url: "/materials/"
      }).then(response => {
        if (response.data) {
          this.material_list = response.data
          for (let i = 0; i < response.data.length; i++) {
            this.material_dict[response.data[i].material_id] = [response.data[i].material_shape, response.data[i].material_sml_txt, response.data[i].material_symbol, response.data[i].hardness, response.data[i].sheet_thickness, response.data[i].material_size_w, response.data[i].material_size_l]
          }
        }
      })
      // 顧客取得
      api({
        method: "GET",
        url: "/customers/"
      }).then(response => {
        this.customer_list = response.data
        for (let i = 0; i < response.data.length; i++) {
          this.customer_dict[response.data[i].customer_id] = [response.data[i].customer_name, response.data[i].assistant, response.data[i].sales, response.data[i].production_control]
          this.customer_dict2[response.data[i].customer_name] = [response.data[i].customer_id, response.data[i].assistant, response.data[i].sales, response.data[i].production_control]
        }
      })
      // ログイン中のユーザーを取得
      api({
        method: "GET",
        url: `/getusers2/${this.username}/`
      }).then(response => {
        this.author = response.data[0].id
      })
      // アシスタントグループのユーザー取得
      api({
        method: "GET",
        url: `/getusers/${ASSISTANT}/`
      }).then(response => {
        for (let i = 0; i < response.data.length; i++) {
          this.assistant_list.push({"value": response.data[i].id, "text": response.data[i].last_name + response.data[i].first_name})
        }
      })
      // 営業グループのユーザー取得
      api({
        method: "GET",
        url: `/getusers/${SALES}/`
      }).then(response => {
        for (let i = 0; i < response.data.length; i++) {
          this.sales_list.push({"value": response.data[i].id, "text": response.data[i].last_name + response.data[i].first_name})
        }
      })
      // 生産管理グループのユーザー取得
      api({
        method: "GET",
        url: `/getusers/${PRODUCTION_CONTROL}/`
      }).then(response => {
        for (let i = 0; i < response.data.length; i++) {
          this.production_control_list.push({"value": response.data[i].id, "text": response.data[i].last_name + response.data[i].first_name})
        }
      })
    },
    selectedFile: function(e) {
        // 選択された File の情報を保存しておく
        e.preventDefault();
        let files = e.target.files;
        this.uploadFile = files[0];
        this.formData = new FormData();
        this.formData.append('file', this.uploadFile, this.uploadFile.name);
        this.file_name = this.uploadFile.name;
        this.file_created_at = moment().format()
        this.file_author = this.author
    },
    // 顧客名を入力したらID、アシスタント、営業担当、生産管理が入力される
     changeCustomerId() {
      if (this.customer_name in this.customer_dict2) {
        this.customer_id = this.customer_dict2[this.customer_name][0]
        this.assistant = this.customer_dict2[this.customer_name][1]
        this.sales = this.customer_dict2[this.customer_name][2]
        this.production_control = this.customer_dict2[this.customer_name][3]
      } else {
        this.customer_id = null
        this.assistant = null
        this.sales = null
        this.production_control = null
      }
    },
    // 顧客IDを入力したら顧客名、アシスタント、営業担当、生産管理が入力される
     changeCustomerName() {
      if (this.customer_id in this.customer_dict) {
        this.customer_name = this.customer_dict[this.customer_id][0]
        this.assistant = this.customer_dict[this.customer_id][1]
        this.sales = this.customer_dict[this.customer_id][2]
        this.production_control = this.customer_dict[this.customer_id][3]
      } else {
        this.customer_name = null
        this.assistant = null
        this.sales = null
        this.production_control = null
      }
    },
    // Parent編集
    submitSave: function() {
      if (this.estimate_answer === "") {
        this.estimate_answer = null;
      }
      if (this.desired_delivery_date === "") {
        this.desired_delivery_date = null;
      }
      api({
        method: "PUT",
        url: `/parents/${this.parent_id}/`,
        data: {
          parent_id: this.parent_id,
          parent_name: this.parent_name,
          parent_figure_number: this.parent_figure_number,
          necessary_amount: this.necessary_amount,
          customer_name: this.customer_name,
          customer_id: this.customer_id,
          assistant: this.assistant,
          sales: this.sales,
          production_control: this.production_control,
          order_status: this.order_status,
          assy: this.assy,
          estimate_answer: this.estimate_answer,
          desired_delivery_date: this.desired_delivery_date,
          material_big: this.material_big,
          material_id: this.material_id,
          material_shape: this.material_shape,
          material_sml_txt: this.material_sml_txt,
          material_symbol: this.material_symbol,
          hardness: this.hardness,
          sheet_thickness: this.sheet_thickness,
          material_size_w: this.material_size_w,
          material_size_l: this.material_size_l,
          delivery_form: this.delivery_form,
          sales_prior_information: this.sales_prior_information,
          production_checklist: this.production_checklist,
          similar_directions_number: this.similar_directions_number,
          product_affinity_number: this.product_affinity_number,
          file_name: this.file_name,
          file_created_at: this.file_created_at,
          file_author: this.file_author
        }
      }).then(response => {
        // ファイル登録
        if (this.formData) {
          api2({
            method: "PATCH",
            url: `/files/${response.data.parent_id}/`,
            data: this.formData
          })
        }
        this.$router.push({
          name: "parent",
          params: {
            parent_id: response.data.parent_id
          }
        })
      });
    },
  },
  // 初期値をフォームにセット
  async beforeRouteEnter(to, from, next) {
    let endpoint = `/parents/${to.params.parent_id}/`
    let data = await api({ url: endpoint });
    return next(vm => {
      (vm.parent_name = data.data.parent_name),
      (vm.parent_figure_number = data.data.parent_figure_number),
      (vm.necessary_amount = data.data.necessary_amount),
      (vm.customer_name = data.data.customer_name),
      (vm.customer_id = data.data.customer_id),
      (vm.assistant = data.data.assistant),
      (vm.sales = data.data.sales),
      (vm.production_control = data.data.production_control),
      (vm.order_status = data.data.order_status),
      (vm.assy = data.data.assy),
      (vm.estimate_answer = data.data.estimate_answer),
      (vm.desired_delivery_date = data.data.desired_delivery_date),
      (vm.material_big = data.data.material_big),
      (vm.material_id = data.data.material_id),
      (vm.material_shape = data.data.material_shape),
      (vm.material_sml_txt = data.data.material_sml_txt),
      (vm.material_symbol = data.data.material_symbol),
      (vm.hardness = data.data.hardness),
      (vm.sheet_thickness = data.data.sheet_thickness),
      (vm.material_size_w = data.data.material_size_w),
      (vm.material_size_l = data.data.material_size_l),
      (vm.delivery_form = data.data.delivery_form),
      (vm.sales_prior_information = data.data.sales_prior_information),
      (vm.production_checklist = data.data.production_checklist),
      (vm.similar_directions_number = data.data.similar_directions_number),
      (vm.product_affinity_number = data.data.product_affinity_number),
      (vm.file = data.data.file),
      (vm.file_name = data.data.file_name),
      (vm.file_created_at = data.data.file_created_at),
      (vm.file_author = data.data.file_author)
    });
  },
  created() {
    this.createDict()
  }
}
</script>
