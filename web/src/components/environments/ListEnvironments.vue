<template>
    <v-table>
        <thead>
            <tr>
                <th id="name" class="text-left">Name</th>
                <th id="key" class="text-left">Key</th>
                <th id="name" class="text-left">Created on</th>
                <th id="actions" class="text-center"></th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="{ id, name, key, created_on } in props.environments" :key="id">
                <td>{{ name }}</td>
                <td>{{ key }}</td>
                <td>{{ created_on }}</td>
                <td>
                    <v-menu location="end" transition="scale-transition">
                        <template v-slot:activator="{ props }">
                            <v-btn icon size="small" v-bind="props" class="elevation-0">
                                <v-icon>mdi-dots-vertical</v-icon>
                            </v-btn>
                        </template>
                        <v-card class="mx-auto" max-width="300">
                            <v-list density="compact" nav>
                                <v-list-item color="primary" rounded="xl" @click="console.log('Delete Action')">
                                    <template v-slot:prepend>
                                        <v-icon size="x-small">mdi-delete</v-icon>
                                    </template>
                                    <v-list-item-title>Delete</v-list-item-title>
                                </v-list-item>
                                <v-list-item color="primary" rounded="xl" :disabled="key != undefined"
                                    @click="emit('onGenerateKey', id)">
                                    <template v-slot:prepend>
                                        <v-icon size="x-small">mdi-shield-key</v-icon>
                                    </template>
                                    <v-list-item-title>Generate Key</v-list-item-title>
                                </v-list-item>
                                <v-list-item color="primary" rounded="xl">
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
        <!-- <v-pagination :length="5"></v-pagination> -->
    </v-table>
</template>

<script setup>
const props = defineProps(['environments'])

const emit = defineEmits(['onGenerateKey'])
</script>