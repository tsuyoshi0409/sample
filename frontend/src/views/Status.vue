<template>
  <div id="status-page">
    <b-container fluid="xl" class="border my-5">
        <b-container class="my-3">
          <h4 class="mt-3">通知</h4>
        </b-container>
        <b-row class="mb-3">
          <b-col>
            <b-card no-body class="mb-1">
              <b-card-header header-tag="header" class="p-1" role="tab">
                <b-button block v-b-toggle.accordion-1 variant="outline-primary">営業</b-button>
              </b-card-header>
              <b-collapse id="accordion-1" accordion="my-accordion" role="tabpanel">
                <b-card-body>
                  <b-card-text>
                    <b-form-checkbox-group
                      v-model="after_users_list"
                      :options="sales_list"
                      stacked
                    ></b-form-checkbox-group>
                  </b-card-text>
                </b-card-body>
              </b-collapse>
            </b-card>
          </b-col>
        </b-row>
        <b-row class="mb-3">
          <b-col>
            <b-card no-body class="mb-1">
              <b-card-header header-tag="header" class="p-1" role="tab">
                <b-button block v-b-toggle.accordion-2 variant="outline-primary">アシスタント</b-button>
              </b-card-header>
              <b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
                <b-card-body>
                  <b-card-text>
                    <b-form-checkbox-group
                      v-model="after_users_list"
                      :options="assistant_list"
                      stacked
                    ></b-form-checkbox-group>
                  </b-card-text>
                </b-card-body>
              </b-collapse>
            </b-card>
          </b-col>
        </b-row>
        <b-row class="mb-3">
          <b-col>
            <b-card no-body class="mb-1">
              <b-card-header header-tag="header" class="p-1" role="tab">
                <b-button block v-b-toggle.accordion-3 variant="outline-primary">生産管理</b-button>
              </b-card-header>
              <b-collapse id="accordion-3" accordion="my-accordion" role="tabpanel">
                <b-card-body>
                  <b-card-text>
                    <b-form-checkbox-group
                      v-model="after_users_list"
                      :options="production_control_list"
                      stacked
                    ></b-form-checkbox-group>
                  </b-card-text>
                </b-card-body>
              </b-collapse>
            </b-card>
          </b-col>
        </b-row>
        <b-row class="mb-3">
          <b-col>
            <b-card no-body class="mb-1">
              <b-card-header header-tag="header" class="p-1" role="tab">
                <b-button block v-b-toggle.accordion-4 variant="outline-primary">購買</b-button>
              </b-card-header>
              <b-collapse id="accordion-4" accordion="my-accordion" role="tabpanel">
                <b-card-body>
                  <b-card-text>
                    <b-form-checkbox-group
                      v-model="after_users_list"
                      :options="purchase_list"
                      stacked
                    ></b-form-checkbox-group>
                  </b-card-text>
                </b-card-body>
              </b-collapse>
            </b-card>
          </b-col>
        </b-row>
        <b-container class="text-center my-5">
          <b-button
            v-show="seigi_bool"
            @click="changeStatus(2, 2)"
            class="text-light mx-1"
            variant="primary"
          >精査済</b-button>
          <b-button
            v-show="seigi_bool"
            @click="changeStatus(1, 3)"
            class="mx-1"
            variant="warning"
          >確認事項あり</b-button>
          <b-button
            @click="changeStatus(5, 4)"
            class="mx-1"
            variant="success"
          >コメントしました</b-button>
        </b-container>
      </b-container>
  </div>
</template>
  
<script>
import api from "@/services/api";
import moment from "moment";

// グループID
const SALES = 1; // 営業
const ASSISTANT = 2; // アシスタント
const SEIGI = 3; // 生技
const PRODUCTION_CONTROL = 4; // 生産管理
const PURCHASE = 5; // 購買
  
export default {
  props: ["parent_id"],
  data() {
    return {
      scrutinizer: null,
      group: null,
      seigi_bool: null,
      bell_id_dict: {},
      before_users_list: [],
      after_users_list: [],
      assistant_list: [],
      sales_list: [],
      production_control_list: [],
      purchase_list: [],
    };
  },
  computed: {
    username: function() {
      return this.$store.state.auth.username;
    },
  },
  methods: {
    getData: function() {
      // ログイン中のユーザー情報取得
      api({
        method: "GET",
        url: `/getusers2/${this.username}/`
      }).then(response =>{
        this.scrutinizer = response.data[0].id
        this.group = response.data[0].groups
        this.seigi_bool = this.group.includes(SEIGI)
        // parent_idに紐づくベルを取得
        api({
          method: "GET",
          url: `/getbells3/${this.parent_id}/`
        }).then(response =>{
          for (let i = 0; i < response.data.length; i++) {
            this.before_users_list.push(response.data[i].user)
            this.after_users_list.push(response.data[i].user)
            this.$set(this.bell_id_dict, response.data[i].user, response.data[i].id)
          }
          if (!this.after_users_list.includes(this.scrutinizer)) {
            this.after_users_list.push(this.scrutinizer)
          }
        })
      })
      // アシスタントグループのリスト作成
      api({
        method: "GET",
        url: `/getusers/${ASSISTANT}/`
      }).then(response => {
        for (let i = 0; i < response.data.length; i++) {
          this.assistant_list.push({"value": response.data[i].id, "text": response.data[i].last_name + response.data[i].first_name})
        }
      })
      // 営業グループのリスト作成
      api({
        method: "GET",
        url: `/getusers/${SALES}/`
      }).then(response => {
        for (let i = 0; i < response.data.length; i++) {
          this.sales_list.push({"value": response.data[i].id, "text": response.data[i].last_name + response.data[i].first_name})
        }
      })
      // 生産管理グループのリスト作成
      api({
        method: "GET",
        url: `/getusers/${PRODUCTION_CONTROL}/`
      }).then(response => {
        for (let i = 0; i < response.data.length; i++) {
          this.production_control_list.push({"value": response.data[i].id, "text": response.data[i].last_name + response.data[i].first_name})
        }
      })
      // 購買グループのリスト作成
      api({
        method: "GET",
        url: `/getusers/${PURCHASE}/`
      }).then(response => {
        for (let i = 0; i < response.data.length; i++) {
          this.purchase_list.push({"value": response.data[i].id, "text": response.data[i].last_name + response.data[i].first_name})
        }
      })
    },
    changeStatus: function(status, message_number) {
      // 精査済みか確認事項ありならステータスを変更する
      if (status == 1 || status == 2) {
        api({
          method: "PUT",
          url: `/parents/${this.parent_id}/`,
          data: {
            status: status,
            scrutinizer: this.scrutinizer,
            scrutiny_at: moment().format()
          }
        })
      }
      // 通知が新規か変更か判定し、通知
      for (let i = 0; i < this.after_users_list.length; i++) {
        if (!this.before_users_list.includes(this.after_users_list[i])) {
          api({
            method: "POST",
            url: "/bells/",
            data: {
              user: this.after_users_list[i],
              parent_id: this.parent_id,
              is_active: true,
              updated_at: moment().format(),
              updated_user: this.scrutinizer,
              message_number: message_number
            }
          })
        }
        else {
          api({
            method: "PATCH",
            url: `/bells/${this.bell_id_dict[this.after_users_list[i]]}/`,
            data: {
              is_active: true,
              updated_at: moment().format(),
              updated_user: this.scrutinizer,
              message_number: message_number
            }
          })
        }
      }
      this.$router.go({
        name: "parent",
        params: {
          parent_id: this.parent_id
        }
      })
    }
  },
  created() {
    this.getData()
  }
};
</script>