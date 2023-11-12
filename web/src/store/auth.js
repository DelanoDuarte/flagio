import { defineStore } from "pinia";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    user: undefined,
    token: undefined,
  }),
  actions: {
    signin(token) {
      this.token = token;
      localStorage.setItem("access_token", token);
    },
    signout() {
      this.token = undefined;
      this.user = undefined;
      localStorage.removeItem("access_token");
    },
    isAuthenticated() {
      return localStorage.getItem("access_token") != undefined;
    },
  },
});
