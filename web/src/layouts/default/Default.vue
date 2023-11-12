<template>
  <v-app color="grey lighten-3">
    <v-app-bar app color="primary" flat>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>FlagIO</v-toolbar-title>

      <!-- User information -->
      <v-spacer></v-spacer>
      <v-menu offset-y>
        <template v-slot:activator="{ props, on }">
          <v-btn v-bind="props" text v-slot:prepend>
            <v-avatar size="32">
              <v-img src="https://randomuser.me/api/portraits/women/85.jpg" alt="User Avatar"></v-img>
            </v-avatar>
            <!-- {{ user.name }} -->
            Sandra Adams
          </v-btn>
        </template>

        <v-list :lines="false" density="compact" nav>
          <v-list-item v-for="(item, i) in user_options" :key="i" :value="item" color="primary" @click="item.onClick">
            <template v-slot:prepend>
              <v-icon :icon="item.icon"></v-icon>
            </template>

            <v-list-item-title v-text="item.text"></v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>

    <v-layout>
      <v-navigation-drawer expand-on-hover rail v-model="drawer">
        <v-divider></v-divider>

        <v-list density="compact" nav class="mt-16">
          <v-list-item prepend-icon="mdi-home" to="/" title="Home" value="myfiles"></v-list-item>
          <v-list-item prepend-icon="mdi-security" to="/administration" title="Administration"
            value="dministration"></v-list-item>
          <v-list-item prepend-icon="mdi-flag" to="/flags" title="Flags" value="flags"></v-list-item>
          <v-list-item prepend-icon="mdi-folder" to="/environments" title="Environments" value="starred"></v-list-item>
        </v-list>
      </v-navigation-drawer>

      <v-main>
        <default-view />
      </v-main>
    </v-layout>
  </v-app>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import DefaultBar from "./AppBar.vue";
import DefaultView from "./View.vue";

import { useAuthStore } from '@/store/auth'

const authStore = useAuthStore()
const router = useRouter()

const drawer = ref(false);
const user_options = ref([
  { text: 'My Account', icon: 'mdi-folder', "onClick": () => { } },
  { text: 'Sign In', icon: 'mdi-login', "onClick": () => { } },
  { text: 'Sign out', icon: 'mdi-logout', "onClick": () => signout() }
])

const signout = () => {
  console.log("Logout action")
  authStore.signout()
  router.push("/")
}

</script>
