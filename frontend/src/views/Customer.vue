<template>
  <div>
    <GlobalHeader />
    <GlobalMessage />
    <b-container fluid="xl" class="my-5">
      <h2>顧客詳細</h2>
    </b-container>
    <b-container fluid="xl" class="border my-5">
      <b-row>
        <b-col sm="1" class="bg-dark border text-light">顧客ID</b-col>
        <b-col sm="5" class="bg-dark border text-light">顧客名</b-col>
        <b-col sm="2" class="bg-dark border text-light">アシスタント</b-col>
        <b-col sm="2" class="bg-dark border text-light">営業担当</b-col>
        <b-col sm="2" class="bg-dark border text-light">生産管理</b-col>
      </b-row>
      <b-row>
        <b-col sm="1" class="border">{{ customer.customer_id }}</b-col>
        <b-col sm="5" class="border">{{ customer.customer_name }}</b-col>
        <b-col sm="2" class="border">{{ customer.assistant }}</b-col>
        <b-col sm="2" class="border">{{ customer.sales }}</b-col>
        <b-col sm="2" class="border">{{ customer.production_control }}</b-col>
      </b-row>
    </b-container>
    <b-container fluid="xl" class="my-5 text-center">
      <router-link
        :to="{
          name: 'customer_list'
        }"
        class="customer-link"
      >
        <b-button class="text-white mx-1" variant="primary">戻る</b-button>
      </router-link>
      <router-link
        :to="{ name: 'customer_editor', params: { customer_id: customer.customer_id } }"
      >
        <b-button variant="warning" class="text-dark mx-1">編集</b-button>
      </router-link>
      <b-button @click="deleteCustomerData" class="text-dark mx-1" variant="danger">削除</b-button>
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
  name: "customer",
  props: {
    customer_id: {
      required: true
    }
  },
  data() {
    return {
      customer: {}
    };
  },
  methods: {
    setPageTitle(title) {
      document.title = title;
    },
    getCustomerData: function() {
      api({
        method: "get",
        url: `/customers/${this.customer_id}/`
      }).then(response => {
        this.customer = response.data;
        this.setPageTitle(response.data.customer_id);
      });
    },
    deleteCustomerData: function() {
      var result = window.confirm('削除してもよろしいですか？')
      if(result) {
        api({
          method: "delete",
          url: `/customers/${this.customer_id}/`
        }).then(() => {
          this.$router.push({
            name: "customer_list"
          });
        });
      }
    }
  },
  created() {
    this.getCustomerData();
  }
};
</script>
