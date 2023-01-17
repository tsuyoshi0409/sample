<template>
  <div>
    <GlobalHeader />
    <GlobalMessage />
    <b-container v-if="parent" fluid="xl" class="border my-5">
      <b-container class="my-3">
        <h2>依頼内容</h2>
      </b-container>
      <b-row>
        <b-col cols="2" class="bg-dark border text-light">依頼No.</b-col>
        <b-col cols="2" class="border">{{ parent_id }}</b-col>
        <b-col cols="2" class="bg-dark border text-light">登録日時</b-col>
        <b-col cols="2" class="border">{{ created_at }}</b-col>
        <b-col cols="2" class="bg-dark border text-light">依頼者</b-col>
        <b-col cols="2" class="border">{{ parent.author_last_name }}{{ parent.author_first_name }}</b-col>
      </b-row>
      <b-row>
        <b-col cols="2" class="bg-dark border text-light">ステータス</b-col>
        <b-col cols="2" class="border">
          <div v-if="parent.status === 0">未確認</div>
          <div v-else-if="parent.status === 1">確認中</div>
          <div v-else-if="parent.status === 2">確認済</div>
        </b-col>
        <b-col cols="2" class="bg-dark border text-light">確認日時</b-col>
        <b-col cols="2" class="border">
          {{ scrutiny_at }}
        </b-col>
        <b-col cols="2" class="bg-dark border text-light">確認者</b-col>
        <b-col cols="2" class="border">
          {{ parent.scrutinizer_last_name }}{{ parent.scrutinizer_first_name }}
        </b-col>
      </b-row>
      <b-row>
        <b-col cols="2" class="bg-dark border text-light">顧客名</b-col>
        <b-col cols="6" class="border">{{ parent.customer_name }}</b-col>
        <b-col cols="2" class="bg-dark border text-light">顧客ID</b-col>
        <b-col cols="2" class="border">{{ parent.customer_id }}</b-col>
      </b-row>
      <b-row>   
        <b-col cols="2" class="bg-dark border text-light">営業</b-col>
        <b-col cols="2" class="border">{{ parent.sales_last_name }}{{ parent.sales_first_name }}</b-col>
        <b-col cols="2" class="bg-dark border text-light">アシスタント</b-col>
        <b-col cols="2" class="border">{{ parent.assistant_last_name }}{{ parent.assistant_first_name }}</b-col>
        <b-col cols="2" class="bg-dark border text-light">生産管理</b-col>
        <b-col cols="2" class="border">{{ parent.production_control_last_name }}{{ parent.production_control_first_name }}</b-col>
      </b-row>
      <b-row>
        <b-col cols="2" class="bg-dark border text-light">(組図)品名</b-col>
        <b-col cols="10" class="border">{{ parent.parent_name }}</b-col>
      </b-row>
      <b-row>
        <b-col cols="2" class="bg-dark border text-light">(組)図番</b-col>
        <b-col cols="10" class="border">{{ parent.parent_figure_number }}</b-col>
      </b-row>
      <b-row>
        <b-col cols="2" class="bg-dark border text-light">数量</b-col>
        <b-col cols=2 class="border">{{ parent.necessary_amount }}</b-col>
        <b-col cols="2" class="bg-dark border text-light">納入形態</b-col>
        <b-col cols="2" class="border">
          <div v-if="parent.delivery_form === 0">納入形態1</div>
          <div v-else-if="parent.delivery_form === 1">納入形態2</div>
          <div v-else-if="parent.delivery_form === 2">納入形態3</div>
          <div v-else>{{ parent.delivery_form }}</div>
        </b-col>
      </b-row>
      <b-row>
        <b-col cols="2" class="bg-dark border text-light">見積回答</b-col>
        <b-col cols="2" class="border">{{ estimate_answer }}</b-col>
        <b-col cols="2" class="bg-dark border text-light">希望納期</b-col>
        <b-col cols="2" class="border">{{ desired_delivery_date }}</b-col>
      </b-row>
      <b-row>
        <b-col cols="2" class="bg-dark border text-light">材料</b-col>
        <b-col cols="2" class="border">
          <div v-if="parent.material_big === 0">材料1</div>
          <div v-else-if="parent.material_big === 1">材料2</div>
          <div v-else-if="parent.material_big === 2">材料3</div>
          <div v-else>{{ parent.material_big }}</div>
        </b-col>
        <b-col cols="2" class="bg-dark border text-light">材料ID</b-col>
        <b-col cols="2" class="border">{{ parent.material_id }}</b-col>
        <b-col cols="2" class="bg-dark border text-light">記号</b-col>
        <b-col cols="2" class="border">{{ parent.material_symbol }}</b-col>
      </b-row>
      <b-row>
        <b-col cols="2" class="bg-dark border text-light">硬度仕上げ</b-col>
        <b-col cols="2" class="border">{{ parent.hardness }}</b-col>
        <b-col cols="2" class="bg-dark border text-light">板厚</b-col>
        <b-col cols="2" class="border">
          <div v-if="parent.sheet_thickness">{{ parent.sheet_thickness }} μm</div>
        </b-col>
        <b-col cols="2" class="bg-dark border text-light">材料サイズ</b-col>
        <b-col cols="2" class="border">
          <div v-if="parent.material_size_w || parent.material_size_l">
            {{ parent.material_size_w }} × {{ parent.material_size_l }} mm
          </div>
        </b-col>
      </b-row>
      <b-row>
        <b-col cols="2" class="bg-dark border text-light">類似No.</b-col>
        <b-col cols="4" class="border">{{ parent.similar_directions_number }}</b-col>
      </b-row>
      <b-row>
        <b-col cols="2" class="bg-dark border text-light">添付ファイル</b-col>
        <b-col cols="2" class="border"><a :href="url">{{ parent.file_name }}</a></b-col>
        <b-col cols="2" class="bg-dark border text-light">ファイル最終更新</b-col>
        <b-col cols="2" class="border">{{ file_created_at }}</b-col>
        <b-col cols="2" class="bg-dark border text-light">ファイル登録者</b-col>
        <b-col cols="2" class="border">{{ parent.file_author_last_name }}{{ parent.file_author_first_name }}</b-col>
      </b-row>
      <b-row>
        <b-col cols="12" class="bg-dark border text-light">連絡事項</b-col>
      </b-row>
      <b-row>
        <b-col cols="12" class="border">
          <b-textarea 
            class="bg-white"
            rows="5"
            v-model="parent.sales_prior_information"
            disabled
          ></b-textarea>
        </b-col>
      </b-row>
      <b-container class="text-center my-5">
        <router-link :to="{ name: 'editor', params: { parent_id: parent.parent_id } }">
          <b-button variant="warning" class="text-dark mx-1">編集</b-button>
        </router-link>
        <b-button @click="deleteParentData" variant="danger" class="text-dark mx-1">削除</b-button>
      </b-container>
    </b-container>
    <ChildrenListVue v-bind:parent_id="parent_id" />
    <PartListVue v-bind:parent_id="parent_id" />
    <CommentsListVue v-bind:parent_id="parent_id" />
    <StatusVue v-bind:parent_id="parent_id" />
  </div>
</template>

<script>
import api from "@/services/api"
import GlobalHeader from "@/components/GlobalHeader.vue"
import GlobalMessage from "@/components/GlobalMessage.vue"
import ChildrenListVue from "./ChildrenList.vue"
import CommentsListVue from "./CommentsList.vue"
import StatusVue from "./Status.vue"
import PartListVue from "./PartList.vue"
import moment from "moment"

export default {
  components: {
    GlobalHeader,
    GlobalMessage,
    ChildrenListVue,
    CommentsListVue,
    StatusVue,
    PartListVue,
  },
  props: {
    parent_id: {
      required: true
    }
  },
  data() {
    return {
      parent: null,
      created_at: null,
      scrutiny_at: null,
      estimate_answer: null,
      desired_delivery_date: null,
      file_name: null,
      url: null,
      scrutinizer: null,
      file_created_at: null
    };
  },
  watch: {
    $route() {
      location.reload()
    }
  },
  computed: {
    username: function() {
      return this.$store.state.auth.username;
    }
  },
  methods: {
    getData: function() {
      // parent_idを指定してParentのデータを取得
      api({
        method: "get",
        url: `/parents/${this.parent_id}/`
      }).then(response => {
        this.parent = response.data;
        this.created_at = moment(response.data.created_at).format("YYYY/MM/DD HH:mm")
        if (response.data.scrutiny_at) {
          this.scrutiny_at = moment(response.data.scrutiny_at).format("YYYY/MM/DD HH:mm")
        }
        if (response.data.estimate_answer) {
          this.estimate_answer = moment(response.data.estimate_answer).format("YYYY/MM/DD")
        }
        if (response.data.desired_delivery_date) {
          this.desired_delivery_date = moment(response.data.desired_delivery_date).format("YYYY/MM/DD")
        }
        if (response.data.file_created_at) {
          this.file_created_at = moment(response.data.file_created_at).format("YYYY/MM/DD HH:mm")
        }
        if (response.data.file_name) {
          this.url = process.env.VUE_APP_ROOT_API + `download/${this.parent_id}/`
        }
      })
    },
    // Parent削除
    deleteParentData: function() {
      var result = window.confirm('削除してもよろしいですか？');
      if(result) {
        api({
          method: "delete",
          url: `/parents/${this.parent_id}/`
        }).then(() => {
          this.$router.push({
            name: "home"
          });
        });
      }
    }
  },
  created() {
    this.getData()
  }
};
</script>
