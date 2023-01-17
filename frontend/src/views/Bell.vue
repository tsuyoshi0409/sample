<template>
  <b-container class="my-5">
    <div>
      <button v-on:click="openModal">
        <notification-bell
          :size="20"
          :count="count"
          :upper-limit="50"
          counter-location="upperRight"
          counter-style="roundRectangle"
          counter-background-color="#FF0000"
          counter-text-color="#FFFFFF"
          icon-color="#FFFFFF"
          font-size="10px"
          :animated="true"
          v-on:mouseover="openModal"
        ></notification-bell>
      </button>
      <v-overlay :value="showContent">
        <b-list-group>
          <b-list-group-item class="text-dark" v-for="item in list" :key="item.id">
            <div v-if="item.message_number == 1">
              <router-link :to="{ name: 'parent', params: { parent_id: item.parent_id} }">
                {{ '台帳No.' + item.parent_id}}
              </router-link> - 新規登録しました - {{ item.updated_user_last_name }}{{ item.updated_user_first_name }} {{ item.updated_at }}
              <button class="btn btn-danger" type="button" @click="deleteItem(item.id)">削除</button>
            </div>
            <div v-else-if="item.message_number == 2">
              <router-link :to="{ name: 'parent', params: { parent_id: item.parent_id} }">
                {{ '台帳No.' + item.parent_id}}
              </router-link> - 確認済です - {{ item.updated_user_last_name }}{{ item.updated_user_first_name }} {{ item.updated_at }}
              <button class="btn btn-danger" type="button" @click="deleteItem(item.id)">削除</button>
            </div>
            <div v-else-if="item.message_number == 3">
              <router-link :to="{ name: 'parent', params: { parent_id: item.parent_id} }">
                {{ '台帳No.' + item.parent_id}}
              </router-link> - 確認事項あり - {{ item.updated_user_last_name }}{{ item.updated_user_first_name }} {{ item.updated_at }}
              <button class="btn btn-danger" type="button" @click="deleteItem(item.id)">削除</button>
            </div>
            <div v-else-if="item.message_number == 4">
              <router-link :to="{ name: 'parent', params: { parent_id: item.parent_id} }">
                {{ '台帳No.' + item.parent_id}}
              </router-link> - コメントしました - {{ item.updated_user_last_name }}{{ item.updated_user_first_name }} {{ item.updated_at }}
              <button class="btn btn-danger" type="button" @click="deleteItem(item.id)">削除</button>
            </div>
          </b-list-group-item>
        </b-list-group>
        <button v-on:click="closeModal">Close</button>
      </v-overlay>
    </div>
  </b-container>

</template>
  
<script>
import NotificationBell from 'vue-notification-bell'
import api from "@/services/api"
import moment from "moment"

export default {
  components: {
    'notification-bell':NotificationBell 
  },
  data() {
    return {
      list: null,
      showContent: false,
      user_id: null,
      updated_at: null,
      count: 0
    };
  },
  computed: {
    username: function() {
      return this.$store.state.auth.username;
    },
  },
  methods: {
    getItems: function() {
      api.get("/auth/users/me/").then(response => {
        this.user_id = response.data.id
        api({
          method: "GET",
          url: `/getbells4/${this.user_id}/True/`
        }).then(response => {
          this.list = response.data
          this.count = this.list.length
          for (let i = 0; i < this.list.length; i++) {
            this.list[i].updated_at = moment(this.list[i].updated_at).format("YYYY/MM/DD/HH:mm")
          }
        })
      })
    },
    deleteItem: function(id) {
      api({
        method: "PATCH",
        url: `/bells/${id}/`,
        data: {
          is_active: false
        }
      }).then(
        // this.list.splice(id, 1)
        this.$router.go({
          name: "bell"
        })
      )
    },
    openModal: function(){
      this.showContent = true
    },
    closeModal: function(){
      this.showContent = false
    }
  },
  created() {
    this.getItems()
  }
}
</script>