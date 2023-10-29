<template>
  <v-row no-gutters>
    <v-col v-for="{ title, qt, icon, color } in cards">
      <v-card max-width="368">
        <v-card-item :title="title"> </v-card-item>

        <v-card-text class="py-0">
          <v-row align="center" no-gutters>
            <v-col class="text-h3" cols="6"> {{ qt }} </v-col>

            <v-col cols="6" class="text-right">
              <v-icon :color="color" :icon="icon" size="88"></v-icon>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script setup>
import { ref } from 'vue'

const cards = ref([
  {
    title: "Requests",
    qt: "61",
    icon: "mdi-arrow-bottom-right-thick",
    color: "success"
  },
  {
    title: "Requests",
    qt: "61",
    icon: "mdi-arrow-bottom-right-thick",
    color: "success"
  },
  {
    title: "Requests",
    qt: "61",
    icon: "mdi-arrow-bottom-right-thick",
    color: "success"
  }
]);
</script>
