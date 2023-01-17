<template>
  <div id="comments_list-page">
    <b-container fluid="xl" class="border my-2">
      <b-container class="my-3">
        <h4>コメント</h4>
      </b-container>
      <div v-for="comment in comments" :key="comment.comment_id">
        <b-container class="border my-5">
          <b-row>
            <b-col cols="2">
              <p class="font-weight-bold">{{ comment.poster_last_name }}{{ comment.poster_first_name }}</p>
            </b-col>
            <b-col cols="3">
              <p>{{ comment.updated_at }}</p>
            </b-col>
            <b-col>
              <b-button
                v-if="comment.poster == poster"
                @click="editCommentData(comment.comment_id)"
                variant="warning">編集
              </b-button>
              <b-button
                v-if="comment.poster == poster"
                @click="deleteCommentData(comment.comment_id)"
                variant="danger">削除
              </b-button>
            </b-col>
          </b-row>
          <b-form v-on:submit.prevent="submitSave2(comment.comment_id, comment.comment)">
            <b-row>
              <b-col sm="12">
                <b-textarea
              v-model="comment.comment"
              v-bind:disabled="activate_dict[comment.comment_id]">
            </b-textarea>
              </b-col>
            </b-row>
            <b-container v-if="!activate_dict[comment.comment_id]" class="text-center">
              <b-button type="submit" variant="success">投稿</b-button>
            </b-container>
          </b-form>
        </b-container>
      </div>
      <b-form v-on:submit.prevent="submitSave">
        <b-textarea type="text" placeholder="コメント" v-model="comment" />
        <b-container class="text-center mb-3">
          <b-button type="submit" variant="success">投稿</b-button>
        </b-container>
      </b-form>
    </b-container>
  </div>
</template>
  
<script>
import api from "@/services/api";
import moment from "moment";
  
export default {
  props: ["parent_id"],
  data() {
    return {
      comments: "",
      comment: null,
      updated_at: null,
      poster: null,
      activate_dict: {},
    };
  },
  computed: {
    username: function() {
      return this.$store.state.auth.username;
    },
  },
  methods: {
    getComments: function() {
      api({
        method: "get",
        url: `/parents/${this.parent_id}/comments/`
      }).then(response => {
        this.comments = response.data;
        for (let i = 0; i < this.comments.length; i++) {
          this.comments[i].updated_at = moment(this.comments[i].updated_at).format("YYYY/MM/DD HH:mm")
          this.activate_dict[this.comments[i].comment_id] = true
        }
      });
    },
    editCommentData: function(comment_id) {
      this.$set(this.activate_dict, comment_id, false)
      this.$forceUpdate()
    },
    deleteCommentData: function(comment_id) {
      var result = window.confirm('削除してもよろしいですか？')
      if(result) {
        api({
          method: "delete",
          url: `/comments/${comment_id}/`
        }).then(() => {
          this.$router.go({
            name: "parent",
            params: {
              parent_id: this.parent_id
            }
          });
        });
      }
    },
    getData: function() {
      api({
        method: "GET",
        url: `/getusers2/${this.username}/`
      }).then(response => {
        this.poster = response.data[0].id
      })
    },
    submitSave: function() {
      api({
          method: "POST",
          url: "/comments/",
          data: {
              parent_id: this.parent_id,
              poster: this.poster,
              comment: this.comment
          }
      }).then(
          this.$router.go({
              name: "parent",
              params: {
                  parent_id: this.parent_id
              }
          })
      )
    },
    submitSave2: function(comment_id, comment) {
      api({
        method: "PUT",
        url: `/comments/${comment_id}/`,
        data: {
          comment: comment,
          poster: this.poster,
          parent_id: this.parent_id
        }
      }).then(
        this.$router.go({
          name: "parent",
          params: {
            parent_id: this.parent_id
          }
        })
      )
    }
  },
  created() {
    this.getData();
    this.getComments();
  }
};
</script>