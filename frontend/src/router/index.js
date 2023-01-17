import Vue from "vue"
import VueRouter from "vue-router"
import store from "@/store"
import Home from "@/views/Home.vue"
import LoginPage from "@/views/LoginPage.vue"
import Parent from "@/views/Parent.vue"
import ParentCreate from "@/views/ParentCreate.vue"
import ParentEditor from "@/views/ParentEditor.vue"
import ChildrenList from "@/views/ChildrenList.vue"
import Child from "@/views/Child.vue"
import ChildEditor from "@/views/ChildEditor.vue"
import ChildCreate from "@/views/ChildCreate.vue"
import SpecialProcess from "@/views/SpecialProcess.vue"
import Outsourcing from "@/views/Outsourcing.vue"
import ProcessFlow from "@/views/ProcessFlow.vue"
import SpecialProcessEditor from "@/views/SpecialProcessEditor.vue"
import OutsourcingEditor from "@/views/OutsourcingEditor.vue"
import ProcessFlowEditor from "@/views/ProcessFlowEditor.vue"
import MaterialList from "@/views/MaterialList.vue"
import MaterialCreate from "@/views/MaterialCreate.vue"
import Material from "@/views/Material.vue"
import MaterialEditor from "@/views/MaterialEditor.vue"
import CustomerList from "@/views/CustomerList.vue"
import CustomerCreate from "@/views/CustomerCreate.vue"
import Customer from "@/views/Customer.vue"
import CustomerEditor from "@/views/CustomerEditor.vue"
import CommentsList from "@/views/CommentsList.vue"
import Bell from "@/views/Bell.vue"
import Status from "@/views/Status.vue"
import PartList from "@/views/PartList.vue"
import PartEditor from "@/views/PartEditor.vue"

Vue.use(VueRouter)

// ルート定義
const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
    // ログインが必要な画面には「requiresAuth」フラグを付けておく
    meta: { requiresAuth: true }
  },
  {
    path: "/parent/:parent_id",
    name: "parent",
    component: Parent,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: "/parent/:parent_id/children_list",
        name: "children_list",
        component: ChildrenList,
        props: true,
        meta: { requiresAuth: true }
  },
  {
    path: "/parent/:parent_id/special_process",
        name: "special_process",
        component: SpecialProcess,
        props: true,
        meta: { requiresAuth: true }
  },
  {
    path: "/parent/:parent_id/outsourcing",
        name: "outsourcing",
        component: Outsourcing,
        props: true,
        meta: { requiresAuth: true }
  },
  {
    path: "/parent/:parent_id/process_flow",
        name: "process_flow",
        component: ProcessFlow,
        props: true,
        meta: { requiresAuth: true }
  },
  {
    path: "/parent/:parent_id/comments_list",
    name: "comments_list",
    component: CommentsList,
    props: true,
    meta: { requiresAuth: true }
  },
  {
    path: "/parent/:parent_id/status",
    name: "status",
    component: Status,
    props: true,
    meta: { requiresAuth: true }
  },
  {
    path: "/parent/:parent_id/part_list",
    name: "part_list",
    component: PartList,
    props: true,
    meta: { requiresAuth: true }
  },
  {
    path: "/parent/:parent_id/part_editor",
    name: "part_editor",
    component: PartEditor,
    props: true,
    meta: { requiresAuth: true }
  },
  {
    path: "/create",
    name: "create",
    component: ParentCreate,
    props: true,
    meta: { requiresAuth: true }
  },
  {
    path: "/editor/:parent_id",
    name: "editor",
    component: ParentEditor,
    props: true,
    meta: { requiresAuth: true }
  },
  {
    path: "/parent/:parent_id/child/:child_id",
    name: "child",
    component: Child,
    props: true,
    meta: { requiresAuth: true }
  },
  {
    path: "/parent/:parent_id/child_create",
    name: "child_create",
    component: ChildCreate,
    props: true,
    meta: { requiresAuth: true }
  },
  {
    path: "/parent/:parent_id/child/:child_id/editor",
    name: "child_editor",
    component: ChildEditor,
    props: true,
    meta: { requiresAuth: true }
  },
  {
    path: "/parent/:parent_id/child/:child_id/special_process_editor",
    name: "special_process_editor",
    component: SpecialProcessEditor,
    props: true,
    meta: { requiresAuth: true }
  },
  {
    path: "/parent/:parent_id/child/:child_id/outsourcing_editor",
    name: "outsourcing_editor",
    component: OutsourcingEditor,
    props: true,
    meta: { requiresAuth: true }
  },
  {
    path: "/parent/:parent_id/child/:child_id/process_flow_editor",
    name: "process_flow_editor",
    component: ProcessFlowEditor,
    props: true,
    meta: { requiresAuth: true }
  },
  {
    path: "/material_list",
    name: "material_list",
    component: MaterialList,
    meta: { requiresAuth: true }
  },
  {
    path: "/material_create",
    name: "material_create",
    component: MaterialCreate,
    props: true,
    meta: { requiresAuth: true }
  },
  {
    path: "/material/:material_id",
    name: "material",
    component: Material,
    props: true,
    meta: { requiresAuth: true }
  },
  {
    path: "/material/:material_id/editor",
    name: "material_editor",
    component: MaterialEditor,
    props: true,
    meta: { requiresAuth: true }
  },
  {
    path: "/customer_list",
    name: "customer_list",
    component: CustomerList,
    meta: { requiresAuth: true }
  },
  {
    path: "/customer_create",
    name: "customer_create",
    component: CustomerCreate,
    props: true,
    meta: { requiresAuth: true }
  },
  {
    path: "/customer/:customer_id",
    name: "customer",
    component: Customer,
    props: true,
    meta: { requiresAuth: true }
  },
  {
    path: "/customer/:customer_id/editor",
    name: "customer_editor",
    component: CustomerEditor,
    props: true,
    meta: { requiresAuth: true }
  },
  {
    path: "/bell/",
    name: "bell",
    component: Bell,
    meta: { requiresAuth: true }
  },
  {
    path: "/login",
    component: LoginPage
  },
  {
    path: "/:catchAll(.*)",
    redirect: "/"
  }
];

// ルータインスタンスを作成
const router = new VueRouter({
  mode: "history",
  routes,
  scrollBehavior (to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { x: 0, y: 0 }
    }
  }
});

/**
 * 画面遷移をする直前に毎回実行されるナビゲーションガード
 */
router.beforeEach((to, from, next) => {
  const isLoggedIn = store.state.auth.isLoggedIn
  const token = localStorage.getItem("access")
  console.log("to.path=", to.path)
  console.log("isLoggedIn=", isLoggedIn)

  // ログインが必要な画面に遷移しようとした場合
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // ログインしていない場合
    if (!isLoggedIn) {
      console.log("User is not logged in.")
      // まだ認証用トークンが残っていればユーザー情報を再取得
      if (token != null) {
        console.log("Try to renew user info.")
        store
          .dispatch("auth/renew")
          .then(() => {
            // 再取得できたらそのまま次へ
            console.log("Succeeded to renew. So, free to next.")
            next()
          })
          .catch(() => {
            // 再取得できなければログイン画面へ
            forceToLoginPage(to)
          });
      } else {
        // 認証用トークンが無い場合は、ログイン画面へ
        forceToLoginPage(to)
      }
    } else {
      // ログインしている場合はそのまま次へ
      console.log("User is already logged in. So, free to next.")
      next()
    }
  } else {
    // ログインが不要な画面であればそのまま次へ
    console.log("Go to public page.")
    next()
  }
});

/**
 * ログイン画面へ強制送還
 */
function forceToLoginPage(to) {
  console.log("Force to login page.")
  router.replace({
    path: "/login",
    // 遷移先のURLはクエリ文字列として付加
    query: { next: to.fullPath }
  })
}

export default router
