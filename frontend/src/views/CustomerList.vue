<template>
  <div id="home-page">
    <GlobalHeader />
    <GlobalMessage />
    <b-container fluid="xl">
      <div class="my-5">
        <a href="/customer_create">
          <b-button variant="primary" class="text-white">新規登録</b-button>
        </a>
      </div>
    </b-container>
    <b-container fluid="xl" class="border my-5">
      <div class="my-5">
        <b-row class="my-1">
          <b-col sm="2">顧客ID</b-col>
          <b-col sm=4>
            <input class="form-control mr-sm-2" type="text" v-model="Q_customer_id" />
          </b-col>
          <b-col sm="2">顧客名</b-col>
          <b-col sm=4>
            <input class="form-control mr-sm-2" type="text" v-model="Q_customer_name" />
          </b-col>
        </b-row>
        <b-row class="my-1">
          <b-col sm="2">アシスタント</b-col>
          <b-col sm="4">
            <b-form-select v-model="Q_assistant" :options="options_assistant">
            </b-form-select>
          </b-col>
          <b-col sm="2">営業担当</b-col>
          <b-col sm="4">
            <b-form-select v-model="Q_sales" :options="options_sales">
            </b-form-select>
          </b-col>
        </b-row>
        <b-row class="my-1">
          <b-col sm="2">生産管理</b-col>
          <b-col sm="4">
            <b-form-select v-model="Q_production_control" :options="options_production_control">
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
        <b-col sm="1" class="bg-dark border text-light">顧客ID</b-col>
        <b-col sm="5" class="bg-dark border text-light">顧客名</b-col>
        <b-col sm="2" class="bg-dark border text-light">アシスタント</b-col>
        <b-col sm="2" class="bg-dark border text-light">営業担当</b-col>
        <b-col sm="2" class="bg-dark border text-light">生産管理</b-col>
      </b-row>
      <div v-for="customer in customers" :key="customer.customer_id">
        <b-row>
          <b-col sm="1" class="border">
            <router-link
              :to="{ name: 'customer', params: { customer_id: customer.customer_id } }"
              class="customer-link"
              >{{ customer.customer_id }}
            </router-link>
          </b-col>
          <b-col sm="5" class="border">{{ customer.customer_name }}</b-col>
          <b-col sm="2" class="border">{{ customer.assistant_last_name }}{{ customer.assistant_first_name }}</b-col>
          <b-col sm="2" class="border">{{ customer.sales_last_name }}{{ customer.sales_first_name }}</b-col>
          <b-col sm="2" class="border">{{ customer.production_control_last_name }}{{ customer.production_control_first_name }}</b-col>
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
      customers: "",
      next: null,
      previous: null,
      loadingMaterials: false,
      Q_customer_id: "",
      Q_customer_name: "",
      Q_assistant: "",
      Q_sales: "",
      Q_production_control: "",
      assistant_list: [],
      sales_list: [],
      production_control_list: [],
      options_assistant: [
        { value: '', text: '----' }
      ],
      options_sales: [
        { value: '', text: '----' }
      ],
      options_production_control: [
        { value: '', text: '----' }
      ]
    };
  },
  methods: {
    getMaterials: function() {
      this.loadingMaterials = true;
      api({
        method: "get",
        url: "/customers/"
      }).then(response => {
        this.customers = response.data;
        this.loadingMaterials = false;
      });
    },
    getArticles: function() {
      api({
        method: "get",
        url: `/customers/?Q_customer_id=${this.Q_customer_id}&Q_customer_name=${this.Q_customer_name}&Q_assistant=${this.Q_assistant}&Q_sales=${this.Q_sales}&Q_production_control=${this.Q_production_control}`
      }).then(response => {
        this.customers = response.data
        this.loadingMaterials = false;
      })
    }
  },
  created() {
    this.getMaterials();
    document.title = "Material Board";
    api({
      method: "GET",
      url: "/customers/"
    }).then(response => {
      if (response.data) {
        for (let i = 0; i < response.data.length; i++) {
          this.assistant_list.push(response.data[i].assistant)
          this.sales_list.push(response.data[i].sales)
          this.production_control_list.push(response.data[i].production_control)
        }
        this.assistant_list = Array.from(new Set(this.assistant_list))
        this.sales_list = Array.from(new Set(this.sales_list))
        this.production_control_list = Array.from(new Set(this.production_control_list))
        for (let i = 0; i < this.assistant_list.length; i++) {
          this.options_assistant.push({value: this.assistant_list[i], text: this.assistant_list[i]})
        }
        for (let i = 0; i < this.sales_list.length; i++) {
          this.options_sales.push({value: this.sales_list[i], text: this.sales_list[i]})
        }
        for (let i = 0; i < this.production_control_list.length; i++) {
          this.options_production_control.push({value: this.production_control_list[i], text: this.production_control_list[i]})
        }
      }
    });
  }
};
</script>