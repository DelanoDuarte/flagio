/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'
import { createPinia } from 'pinia';

// Plugins
import { registerPlugins } from '@/plugins'

// Components
import Notification from '@/components/shared/Notification.vue'

import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";

const app = createApp(App)
app.use(createPinia());

registerPlugins(app)

app.component('Notification', Notification)
app.use(Toast)
app.mount('#app')
