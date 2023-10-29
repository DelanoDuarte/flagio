<template>
  <div>
    <v-table>
      <thead>
        <tr>
          <th id="name" class="text-left">Name</th>
          <th id="created" class="text-left">Created On</th>
          <th id="created" class="text-left">Expiration Date</th>
          <th id="envs" class="text-left">Environments</th>
          <th id="active" class="text-left">Active</th>
          <th id="actions" class="text-left">
            <v-icon>mdi-archive-edit-outline</v-icon>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="{ id, name, active, created_on, expiration_date, environments } in props.flags" :key="id"
          v-memo="[active]">
          <td>{{ name }}</td>
          <td>{{ created_on }}</td>
          <td>
            <div v-if="expiration_date">
              <v-tooltip activator="parent" location="bottom">{{ moment(expiration_date).format("MMM Do YY")
              }}</v-tooltip>
              <v-icon icon="mdi-clock-outline" color="error"></v-icon>
              {{ moment(expiration_date).endOf('day').fromNow() }}
            </div>
          </td>
          <td>
            <v-chip-group>
              <v-chip elevated v-for="{ id, name } in environments">{{ name }}</v-chip>
            </v-chip-group>
          </td>
          <td class="text-left">
            <div>
              <v-switch label="Active" color="green" :model-value="active" inset
                @update:model-value="(newValue) => onStatusChange(id, newValue)">
              </v-switch>
            </div>
          </td>
          <td>
            <v-menu location="end" transition="scale-transition">
              <template v-slot:activator="{ props }">
                <v-btn icon size="small" v-bind="props" class="elevation-0">
                  <v-icon>mdi-dots-vertical</v-icon>
                </v-btn>
              </template>
              <v-card class="mx-auto" max-width="300">
                <v-list density="compact" nav>
                  <v-list-item color="primary" @click="remove(id)">
                    <template v-slot:prepend>
                      <v-icon size="x-small">mdi-delete</v-icon>
                    </template>
                    <v-list-item-title>Delete</v-list-item-title>
                  </v-list-item>
                  <v-list-item color="primary">
                    <template v-slot:prepend>
                      <v-icon size="x-small">mdi-pencil</v-icon>
                    </template>

                    <v-list-item-title>Edit</v-list-item-title>
                  </v-list-item>
                </v-list>
              </v-card>
            </v-menu>
          </td>
        </tr>
      </tbody>
    </v-table>
  </div>
</template>

<script setup>
import { onMounted, ref, defineProps } from "vue";
import { useToast } from "vue-toastification";
import moment from 'moment'

import request from "@/utils/request";

const emit = defineEmits(["onFlagRemoval", "onFlagChanged"]);
const props = defineProps(["flags"]);

const toast = useToast();

onMounted(() => { });

function onStatusChange(flag_id, value) {
  if (value) {
    activate(flag_id);
    return;
  }
  deactivate(flag_id);
}

const activate = (id) => {
  request({
    url: `/flags/${id}/activate`,
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((flag) => {
      toast.success(`Flag ${flag.name} Activated`)
    })
    .catch((err) => {
      console.log(err);
    })
    .finally(() => {
      emit("onFlagChanged");
    });
};

const deactivate = (id) => {
  request({
    url: `/flags/${id}/deactivate`,
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((flag) => {
      toast.warning(`Flag ${flag.name} Deactivated`)
    })
    .catch((err) => {
      console.log(err);
    })
    .finally(() => {
      emit("onFlagChanged");
    });
};

function remove(flag_id) {
  emit("onFlagRemoval", flag_id);
}
</script>
