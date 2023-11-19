<template>
    <div>
        <v-table>
            <thead>
                <tr>
                    <th id="name" class="text-left">Name</th>
                    <th id="active" class="text-left">Active</th>
                    <th id="actions" class="text-left">
                        <v-icon>mdi-archive-edit-outline</v-icon>
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="{
                    id,
                    username,
                    active,
                } in props.users" :key="id" v-memo="[active]">
                    <td>{{ username }}</td>
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
                                    <v-list-item color="primary">
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
import { ref } from 'vue'

const props = defineProps(['users'])
const onStatusChange = (user_id, value) => {
    console.log(`User switch ${user_id}`, value)
}
</script>