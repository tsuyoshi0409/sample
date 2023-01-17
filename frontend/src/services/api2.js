import axios from "axios";
import store from "@/store";
// import { CSRF_TOKEN } from "./csrf_token";

// function handleResponse(response) {
//   if (response.status === 204) {
//     return "";
//   } else if (response.status === 404) {
//     return null;
//   } else {
//     return response.json();
//   }
// }

// function apiService(endpoint, method, data) {
//   const config = {
//     method: method || "GET",
//     body: data !== undefined ? JSON.stringify(data) : null,
//     headers: {
//       "content-type": "application/json",
//       "X-CSRFTOKEN": CSRF_TOKEN
//     }
//   };
//   return fetch(endpoint, config).then(handleResponse);
// }

// export { apiService };

const api2 = axios.create({
  baseURL: process.env.VUE_APP_ROOT_API,
  timeout: 5000,
  headers: {
    "Content-Type": "multipart/form-data",
    "X-Requested-With": "XMLHttpRequest"
  }
});

// 共通前処理
api2.interceptors.request.use(
  config => {
    // メッセージをクリア
    store.dispatch("message/clearMessages");
    // 認証用トークンがあればリクエストヘッダに加える
    const token = localStorage.getItem("access");
    if (token) {
      config.headers.Authorization = "JWT " + token;
      return config;
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

// 共通エラー処理
api2.interceptors.response.use(
  response => {
    return response;
  },
  error => {
    console.log("error.response=", error.response);
    const status = error.response ? error.response.status : 500;

    // エラーの内容に応じてstoreのメッセージを更新
    let message;
    if (status === 400) {
      // バリデーションNG
      const messages = [].concat.apply([], Object.values(error.response.data));
      store.dispatch("message/setWarningMessages", { messages: messages });
    } else if (status === 401) {
      // 認証エラー
      const token = localStorage.getItem("access");
      if (token != null) {
        message = "ログイン有効期限切れ";
      } else {
        message = "認証エラー";
      }
      store.dispatch("auth/logout");
      store.dispatch("message/setErrorMessage", { message: message });
    } else if (status === 403) {
      // 権限エラー
      message = "権限エラーです。";
      store.dispatch("message/setErrorMessage", { message: message });
    } else {
      // その他のエラー
      message = "想定外のエラーです。";
      store.dispatch("message/setErrorMessage", { message: message });
    }
    return Promise.reject(error);
  }
);

export default api2;
