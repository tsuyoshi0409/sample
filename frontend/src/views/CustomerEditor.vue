<template>
  <div id="edit-page">
    <GlobalHeader />
    <GlobalMessage />
    <!-- メインエリア -->
    <main class="container mt-5 p-5">
      <p class="h5 mb-5">顧客編集</p>
      <b-form v-on:submit.prevent="submitSave">
        <div class="row form-group">
          <label class="col-sm-3 col-form-label">顧客名</label>
          <div class="col-sm-8">
            <b-input type="text" class="form-control" v-model="customer_name" />
          </div>
        </div>
        <div class="row form-group">
          <label class="col-sm-3 col-form-label">アシスタント</label>
          <div class="col-sm-8">
            <b-input type="text" class="form-control" v-model="assistant" />
          </div>
        </div>
        <div class="row form-group">
          <label class="col-sm-3 col-form-label">営業担当</label>
          <div class="col-sm-8">
            <b-input type="text" class="form-control" v-model="sales" />
          </div>
        </div>
        <div class="row form-group">
          <label class="col-sm-3 col-form-label">生産管理</label>
          <div class="col-sm-8">
            <b-input type="text" class="form-control" v-model="production_control" />
          </div>
        </div>

        <div class="row text-center mt-5">
          <div class="col-sm-12">
            <router-link
              :to="{
                  name: 'customer',
                  params: {
                    customer_id: customer_id
                  }
                }"
                class="customer-link"
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
  name: "CustomerEditor",
  props: {
    customer_id: {
      required: true
    }
  },
  data() {
    return {
      // 入力フォームの内容
      customer_name: null,
      assistant: null,
      sales: null,
      production_control: null
    };
  },
  methods: {
    submitSave: function() {
      api({
        method: "PUT",
        url: `/customers/${this.customer_id}/`,
        data: {
          customer_id: this.customer_id,
          customer_name: this.customer_name,
          assistant: this.assistant,
          sales: this.sales,
          production_control: this.production_control
        }
      }).then(response => {
        this.$router.push({
          name: "customer",
          params: {
            customer_id: response.data.customer_id
          }
        });
      });
    }
  },
  async beforeRouteEnter(to, from, next) {
    let endpoint = `/customers/${to.params.customer_id}/`;
    let data = await api({ url: endpoint });
    return next(vm => {
      (vm.customer_id = data.data.customer_id),
      (vm.customer_name = data.data.customer_name),
      (vm.assistant = data.data.assistant),
      (vm.sales = data.data.sales),
      (vm.production_control = data.data.production_control)
    });
  },
  created() {
    document.title = "Editor - Customer";
  }
};
</script>