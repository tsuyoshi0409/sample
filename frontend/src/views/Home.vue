<template>
  <div id="home-page">
    <GlobalHeader />
    <GlobalMessage />
    <b-container fluid="xl">
      <div class="my-5">
        <a href="/create">
          <b-button variant="primary" class="text-white">新規登録</b-button>
        </a>
      </div>
    </b-container>
    <b-container fluid="xl" class="border">
      <div class="my-5">
        <b-row class="my-1">
          <b-col sm="2">依頼No.</b-col>
          <b-col sm=4>
            <input class="form-control mr-sm-2" type="text" v-model="Q_parent_id" />
          </b-col>
          <b-col sm="2">ステータス</b-col>
          <b-col sm="4">
            <b-form-select v-model="Q_status">
              <option value="">----</option>
              <option value="0">未確認</option>
              <option value="1">確認中</option>
              <option value="2">確認済</option>
            </b-form-select>
          </b-col>
        </b-row>
        <b-row class="my-1">
          <b-col sm="2">品名</b-col>
          <b-col sm="4">
            <input class="form-control mr-sm-2" type="text" v-model="Q_parent_name" />
          </b-col>
          <b-col sm="2">図番</b-col>
          <b-col sm="4">
            <input class="form-control mr-sm-2" type="text" v-model="Q_parent_figure_number" />
          </b-col>
        </b-row>
        <b-row>
          <b-col sm="2">顧客名</b-col>
          <b-col sm="4">
            <input class="form-control mr-sm-2" type="text" v-model="Q_customer_name" />
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
        <b-col cols="1" class="bg-dark border text-light">依頼No.</b-col>
        <b-col cols="2" class="bg-dark border text-light">ステータス</b-col>
        <b-col cols="3" class="bg-dark border text-light">品名</b-col>
        <b-col cols="3" class="bg-dark border text-light">図番</b-col>
        <b-col cols="3" class="bg-dark border text-light">顧客名</b-col>
      </b-row>
      <div v-for="parent in parents.results" :key="parent.parent_id">
        <b-row>
          <b-col cols="1" class="border">
            <router-link
              :to="{ name: 'parent', params: { parent_id: parent.parent_id } }"
              >{{ parent.parent_id }}
            </router-link>
          </b-col>
          <b-col cols="2" class="border">
            <div v-if="parent.status === 0">未確認</div>
            <div v-else-if="parent.status === 1">確認中</div>
            <div v-else-if="parent.status === 2">確認済</div>
          </b-col>
          <b-col cols="3" class="border">{{ parent.parent_name }}</b-col>
          <b-col cols="3" class="border">{{ parent.parent_figure_number }}</b-col>
          <b-col cols="3" class="border">{{ parent.customer_name }}</b-col>
        </b-row>
      </div>
      <div class="my-5 text-center">
        <p v-show="loadingParents">...loading...</p>
        <b-button class="text-white mx-1" variant="primary" v-show="previous" @click="getPrevious">前へ</b-button>
        <b-button class="text-white mx-1" variant="primary" v-show="next" @click="getNext">次へ</b-button>
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
  data() {
    return {
      parents: "",
      next: null,
      previous: null,
      loadingParents: false,
      Q_parent_id: "",
      Q_parent_name: "",
      Q_parent_figure_number: "",
      Q_status: "",
      Q_customer_name: ""
    };
  },
  methods: {
    getParents: function() {
      this.loadingParents = true;
      api({
        method: "get",
        url: "/parents/"
      }).then(response => {
        this.parents = response.data;
        this.loadingParents = false;
        if (response.data.next) {
          this.next = response.data.next;
        } else {
          this.next = null;
        }
        if (response.data.previous) {
          this.previous = response.data.previous;
        } else {
          this.previous = null;
        }
      })
    },
    getNext: function() {
      let endpoint = "/parents/";
      if (this.next) {
        endpoint = this.next;
      } 
      this.loadingParents = true;
      api({
        method: "get",
        url: endpoint
      }).then(response => {
        this.parents = response.data;
        this.loadingParents = false;
        if (response.data.next) {
          this.next = response.data.next;
        } else {
          this.next = null;
        }
        if (response.data.previous) {
          this.previous = response.data.previous;
        } else {
          this.previous = null;
        }
      });
    },
        getPrevious: function() {
      let endpoint = "/parents/";
      if (this.previous) {
        endpoint = this.previous;
      } 
      this.loadingParents = true;
      api({
        method: "get",
        url: endpoint
      }).then(response => {
        this.parents = response.data;
        this.loadingParents = false;
        if (response.data.next) {
          this.next = response.data.next;
        } else {
          this.next = null;
        }
        if (response.data.previous) {
          this.previous = response.data.previous;
        } else {
          this.previous = null;
        }
      });
    },
    getArticles: function() {
      api({
        method: "get",
        url: `/parents/?Q_parent_id=${this.Q_parent_id}&Q_parent_name=${this.Q_parent_name}&Q_parent_figure_number=${this.Q_parent_figure_number}&Q_status=${this.Q_status}&Q_customer_name=${this.Q_customer_name}`
      }).then(response => {
        this.parents = response.data
        this.loadingParents = false;
        if (response.data.next) {
          this.next = response.data.next;
        } else {
          this.next = null;
        }
        if (response.data.previous) {
          this.previous = response.data.previous;
        } else {
          this.previous = null;
        }
      })
    }
  },
  created() {
    this.getParents();
  }
};
</script>
