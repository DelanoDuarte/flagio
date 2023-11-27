<template>
  <div>
    <v-row no-gutters>
      <v-col v-for="{ key, title, qt, icon, color } in cards" v-bind:key="key">
        <v-card max-width="368">
          <v-card-item :title="title"> </v-card-item>

          <v-card-text class="py-0">
            <v-row align-content="center" no-gutters>
              <v-col class="text-h3" cols="6"> {{ qt }} </v-col>

              <v-col cols="6" class="text-right">
                <v-icon :color="color" :icon="icon" size="88"></v-icon>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const cards = ref([
  {
    key: 1,
    title: "Requests",
    qt: "61",
    icon: "mdi-arrow-bottom-right-thick",
    color: "success"
  },
  {
    key: 2,
    title: "Requests",
    qt: "61",
    icon: "mdi-arrow-bottom-right-thick",
    color: "success"
  },
  {
    key: 3,
    title: "Requests",
    qt: "61",
    icon: "mdi-arrow-bottom-right-thick",
    color: "success"
  }
]);
</script>
