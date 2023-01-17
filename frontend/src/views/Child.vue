<template>
  <div>
    <GlobalHeader />
    <GlobalMessage />
    <b-container fluid="xl" class="mt-5">
      <h2>見積作成内容</h2>
    </b-container>
    <b-container fluid="xl" class="border" v-if="child">
      <b-row>
        <b-col cols="2" class="bg-dark border text-light">品目ID</b-col>
        <b-col cols="2" class="border">{{ child.child_id }}</b-col>
      </b-row>
      <b-row>
        <b-col cols="2" class="bg-dark border text-light">品名</b-col>
        <b-col cols="10" class="border">{{ child.child_name }}</b-col>
      </b-row>
      <b-row>
        <b-col cols="2" class="bg-dark border text-light">図番</b-col>
        <b-col cols="10" class="border">{{ child.child_figure_number }}</b-col>
      </b-row>
      <b-row>
        <b-col cols="2" class="bg-dark border text-light">材料</b-col>
        <b-col cols="2" class="border">
          <div v-if="child.material_big === 0">材料1</div>
          <div v-else-if="child.material_big === 1">材料2</div>
          <div v-else-if="child.material_big === 2">材料3</div>
          <div v-else>{{ child.material_big }}</div>
        </b-col>
        <b-col cols="2" class="bg-dark border text-light">材料ID</b-col>
        <b-col cols="2" class="border">{{ child.material_id }}</b-col>
        <b-col cols="2" class="bg-dark border text-light">記号</b-col>
        <b-col cols="2" class="border">{{ child.material_symbol }}</b-col>
      </b-row>
      <b-row>
        <b-col cols="2" class="bg-dark border text-light">硬度仕上げ</b-col>
        <b-col cols="2" class="border">{{ child.hardness }}</b-col>
        <b-col cols="2" class="bg-dark border text-light">板厚</b-col>
        <b-col cols="2" class="border">
          <div v-if="child.sheet_thickness">{{ child.sheet_thickness }} μm</div>
        </b-col>
        <b-col cols="2" class="bg-dark border text-light">材料サイズ</b-col>
        <b-col cols="2" class="border">
          <div v-if="child.material_size_w || child.material_size_l">
            {{ child.material_size_w }} × {{ child.material_size_l }} mm
          </div>
        </b-col>
      </b-row>
      <b-row>
        <b-col cols="2" class="bg-dark border text-light">個/シート</b-col>
        <b-col cols="2" class="border">{{ child.imposition_amount_piece_seat }}</b-col>
        <b-col cols="2" class="bg-dark border text-light">個/フレーム</b-col>
        <b-col cols="2" class="border">{{ child.imposition_amount_piece_flame }}</b-col>
        <b-col cols="2" class="bg-dark border text-light">フレーム/シート</b-col>
        <b-col cols="2" class="border">{{ child.imposition_amount_flame_seat }}</b-col>
      </b-row>
      <b-row>
        <b-col cols="12" class="bg-dark border text-light">確認事項</b-col>
      </b-row>
      <b-row>
        <b-col cols="12">
          <b-textarea 
            class="bg-white"
            rows="3"
            v-model="child.fixes"
            disabled
          ></b-textarea>
        </b-col>
      </b-row>
      <b-row class="my-3 text-center" v-show="this.seigi_bool">
        <b-col>
          <router-link
            :to="{
              name: 'child_editor',
              params: {
                parent_id: parent_id,
                child_id: child_id
              }
            }"
          >
            <b-button variant="warning" class="text-dark mx-1">編集</b-button>
          </router-link>
          <b-button
          @click="deleteChildData"
          class="text-dark mx-1"
          variant="danger">削除</b-button>
        </b-col>
      </b-row>
    </b-container>
    <SpecialProcessVue v-bind:parent_id="parent_id" v-bind:child_id="child_id" />
    <OutsourcingVue v-bind:parent_id="parent_id" v-bind:child_id="child_id" />
    <ProcessFlowVue v-bind:parent_id="parent_id" v-bind:child_id="child_id" />
    <b-container class="my-3 text-center">
      <router-link
        :to="{
          name: 'parent',
          params: {
            parent_id: parent_id
          }
        }"
      >
        <b-button variant="light" class="mx-1">戻る</b-button>
      </router-link>
    </b-container>
  </div>
</template>

<script>
import api from "@/services/api"
import GlobalHeader from "@/components/GlobalHeader.vue"
import GlobalMessage from "@/components/GlobalMessage.vue"
import SpecialProcessVue from "./SpecialProcess.vue"
import OutsourcingVue from "./Outsourcing.vue"
import ProcessFlowVue from "./ProcessFlow.vue"

export default {
  components: {
    GlobalHeader,
    GlobalMessage,
    SpecialProcessVue,
    OutsourcingVue,
    ProcessFlowVue,
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
      child: null,
      group: null,
      seigi_bool: null,
      SEIGI: 3
    };
  },
  computed: {
    username: function() {
      return this.$store.state.auth.username
    }
  },
  methods: {
    getChildData: function() {
      api({
        method: "get",
        url: `/children/${this.child_id}/`
      }).then(response => {
        this.child = response.data
      })
      api({
        method: "GET",
        url: `/getusers2/${this.username}/`
      }).then(response =>{
        this.group = response.data[0].groups
        this.seigi_bool = this.group.includes(this.SEIGI)
      })
    },
    deleteChildData: function() {
      var result = window.confirm('削除してもよろしいですか？')
      if(result) {
        api({
          method: "delete",
          url: `/children/${this.child_id}/`
        }).then(() => {
          this.$router.push({
            name: "parent",
            params: {
              parent_id: this.parent_id
            }
          })
        })
      }
    }
  },
  created() {
    this.getChildData()
  }
};
</script>
