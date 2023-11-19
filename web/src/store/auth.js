import { defineStore } from "pinia";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    roles: [],
  }),
  actions: {
    signin(response) {
      const s_roles = response.roles.split(",");
      localStorage.setItem("access_token", response.access_token);
      localStorage.setItem("roles", s_roles);
      this.roles = s_roles;
    },
    signout() {
      localStorage.removeItem("access_token");
      localStorage.removeItem("roles");
      this.roles = [];
    },
    isAuthenticated() {
      return localStorage.getItem("access_token") != undefined;
    },
    getRoles() {
      const storage_roles = localStorage.getItem("roles");
      this.roles = storage_roles.split(",");
      return this.roles;
    },
  },
});
