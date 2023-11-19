/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Components
import App from "./App.vue";

// Composables
import { createApp } from "vue";
import { createPinia } from "pinia";

// Plugins
import { registerPlugins } from "@/plugins";

// Components
import Notification from "@/components/shared/Notification.vue";

import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";

const app = createApp(App);
app.use(createPinia());
app.directive("role", (el, binding, vnode) => {
  const roles = localStorage.getItem("roles").split(",");
  const requiredRole = binding.value;

  console.log("Role Required", requiredRole);
  if (!roles.includes(requiredRole)) {
    el.style.display = "none";
  }
});

registerPlugins(app);

app.component("Notification", Notification);
app.use(Toast);
app.mount("#app");
