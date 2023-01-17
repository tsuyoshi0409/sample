<template>
  <div id="edit-page">
    <GlobalHeader />
    <GlobalMessage />
    <!-- メインエリア -->
    <b-container class="my-3">
      <h2>工程フロー</h2>
      <b-row>
        <b-col cols="3">プリセット</b-col>
        <b-col cols="4">
          <b-form-select
            v-model="preset_selected"
            :options="preset_options"
          >
          </b-form-select>
        </b-col>
        <b-col>
          <b-button variant="primary" @click="setPreset">セット</b-button>
        </b-col>
      </b-row>
    </b-container>
    <b-container class="my-3">
      <b-row>
        <b-col cols="3">社内工程</b-col>
        <b-col cols="4">
          <b-form-select
            v-model="in_selected"
            :options="in_options"
            value-field="operation_id"
            text-field="operation_name"
          ></b-form-select>
        </b-col>
        <b-col>
          <b-button variant="primary" @click="addOperation1">追加</b-button>
        </b-col>
      </b-row>
    </b-container>
    <b-container class="my-3">
      <b-row>
        <b-col cols="3">社内特殊工程</b-col>
        <b-col cols="4">
          <b-form-select
            v-model="special_selected"
            :options="special_options"
            value-field="operation_id"
            text-field="operation_name"
          ></b-form-select>
        </b-col>
        <b-col>
          <b-button variant="primary" @click="addOperation3">追加</b-button>
        </b-col>
      </b-row>
    </b-container>
    <b-container class="my-3">
      <b-row>
        <b-col cols="3">外注工程</b-col>
        <b-col cols="4">
          <b-form-select
            v-model="out_selected"
            :options="out_options"
            value-field="operation_id"
            text-field="operation_name"
          ></b-form-select>
        </b-col>
        <b-col>
          <b-button variant="primary" @click="addOperation2">追加</b-button>
        </b-col>
      </b-row>
    </b-container>
    <b-container>
      <b-form v-on:submit.prevent="submitSave">
        <b-container class="my-3">
          <b-row>
            <b-col class="border font-weight-bold" cols="2">工程番号</b-col>
            <b-col class="border font-weight-bold" cols="2">工程名</b-col>
            <b-col class="border font-weight-bold" cols="2">加工場所</b-col>
            <b-col class="border font-weight-bold">外注先</b-col>
            <b-col class="border" cols="2"></b-col>
          </b-row>
          <b-row
            v-for="(operation, index) in operations"
            :key="operation.operation_id"
            :draggable="true"
            @dragstart="dragStart(index)"
            @dragenter="dragEnter(index)"
            @dragover.prevent
            @dragend="dragEnd"
            :class="index === dragIndex ? 'dragging' : ''"
          >
            <b-col class="border" cols="2">{{ index + 1 }}</b-col>
            <b-col class="border" cols="2">{{ operation_dict[operation] }}</b-col>
            <b-col class="border" cols="2">{{ is_outsourcing_dict[operation] }}</b-col>
            <b-col class="border">{{ outsourcing_dict[operation] }}</b-col>
            <b-col class="border" cols="2">
              <b-button
                variant="danger"
                @click="deleteOperation(index)"
              >削除</b-button>
            </b-col>
          </b-row>
        </b-container>
        <b-container class="text-center my-5">
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
        </b-container>
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
      operations: [],
      dragIndex: null,
      in_selected: null,
      in_options: null,
      out_selected: null,
      out_options: null,
      special_selected: null,
      special_options: null,
      operation_dict: {},
      outsourcing_dict: {},
      is_outsourcing_dict: {},
      preset_options: [
        {value: [1, 2, 3, 4, 5, 6, 7], text: '通常工程'}
      ],
      preset_selected: null,
      before_operations: null
    }
  },
  methods: {
    submitSave: async function() {
      var promise_ary = []
      // 更新前より更新後の工程が多い場合
      if (this.before_operations.length < this.operations.length) {
        for (let i = 0; i < this.operations.length; i++) {
          if (this.before_operations.length > i) {
            var promise = api({
              method: "PATCH",
              url: `/children_operations/${this.before_operations[i].id}/`,
              data: {
                operation_id: this.operations[i]
              }
            })
            promise_ary.push(promise)
          }
          else {
            var promise2 = api({
              method: "POST",
              url: '/children_operations/',
              data: {
                index: i,
                parent_id: this.parent_id,
                child_id: this.child_id,
                operation_id: this.operations[i]
              }
            })
            promise_ary.push(promise2)
          }
        }
      }
      // 更新前より更新後の工程が少ないか同じ場合
      else {
        for (let i = 0; i < this.before_operations.length; i++) {
          if (this.operations.length > i) {
            var promise3 = api({
              method: "PATCH",
              url: `/children_operations/${this.before_operations[i].id}/`,
              data: {
                operation_id: this.operations[i]
              }
            })
            promise_ary.push(promise3)
          }
          else {
            var promise4 = api({
              method: "DELETE",
              url: `/children_operations/${this.before_operations[i].id}/`
            })
            promise_ary.push(promise4)
          }
        }
      }
      Promise.all(promise_ary).then(() => {
        this.$router.push({
          name: "child",
          params: {
            parent_id: this.parent_id,
            child_id: this.child_id
          }
        })
      })
    },
    getOperations: function() {
      api({
        method: "GET",
        url: `/getoperations/${this.child_id}/1/`
      }).then(response => {
        for (let i = 0; i < response.data.length; i++) {
          this.operation_dict[response.data[i].operation_id] = response.data[i].operation_name
          this.outsourcing_dict[response.data[i].operation_id] = response.data[i].company_name
          this.is_outsourcing_dict[response.data[i].operation_id] = "外注"
        }
      })
      api({
        method: "GET",
        url: `/getoperations/${this.child_id}/2/`
      }).then(response => {
        for (let i = 0; i < response.data.length; i++) {
          this.operation_dict[response.data[i].operation_id] = response.data[i].operation_name
          this.is_outsourcing_dict[response.data[i].operation_id] = "社内"
        }
      })
      api({
        method: "GET",
        url: "/getoperations3/0/"
      }).then(response => {
        this.in_options = response.data
        for (let i = 0; i < response.data.length; i++) {
          this.operation_dict[response.data[i].operation_id] = response.data[i].operation_name
          this.is_outsourcing_dict[response.data[i].operation_id] = "社内"
        }
      })
      api({
        method: "GET",
        url: `/getoperations/${this.child_id}/1/`
      }).then(response => {
        this.out_options = response.data
      })
      api({
        method: "GET",
        url: `/getoperations/${this.child_id}/2/`
      }).then(response => {
        this.special_options = response.data
      })
    },
    dragStart: function(index) {
      this.dragIndex = index
    },
    dragEnter: function(index) {
      if (index === this.dragIndex) return
      const deleteElement = this.operations.splice(this.dragIndex, 1)[0]
      this.operations.splice(index, 0, deleteElement)
      this.dragIndex = index
    },
    dragEnd: function() {
      this.dragIndex = null
    },
    addOperation1: function() {
      this.operations.push(this.in_selected)
    },
    addOperation2: function() {
      this.operations.push(this.out_selected)
    },
    addOperation3: function() {
      this.operations.push(this.special_selected)
    },
    deleteOperation: function(index) {
      this.operations.splice(index, 1)
    },
    setPreset: function() {
      this.operations = this.preset_selected
    },
    getChildOperation: function() {
      api({
        method: 'GET',
        url: `/get_children_operations/${this.child_id}/`
      }).then(response => {
        this.before_operations = response.data
        for (let i = 0; i < response.data.length; i++) {
          this.operations.push(response.data[i].operation_id)
        }
      })
    }
  },
  created() {
    this.getOperations()
    this.getChildOperation()
  }
}
</script>

<style>
.dragging {
  background-color: #eee;
}
</style>
