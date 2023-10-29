<template>
    <v-dialog width="500" v-model="dialog">
        <template v-slot:activator="{ props }">
            <v-btn v-bind="props" color="primary" text="New Environment"> </v-btn>
        </template>

        <template v-slot:default="{ isActive }">
            <v-card title="New Environment">
                <v-card-text>
                    <v-container>
                        <v-row>
                            <v-col cols="12">
                                <v-text-field v-model="environment.name" label="Name *" required></v-text-field>
                            </v-col>
                        </v-row>
                    </v-container>
                </v-card-text>

                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue-darken-1" variant="text" @click="dialog = false">
                        Close
                    </v-btn>
                    <v-btn color="blue-darken-1" variant="text" @click="newEnv"> Save </v-btn>
                </v-card-actions>
            </v-card>
        </template>
    </v-dialog>
</template>

<script setup>
import { createEnvironment } from '@/services/api';
import { ref } from "vue";

const emit = defineEmits(['onNewEnvironment'])

const dialog = ref(false);
const environment = ref({
    name: "",
});

const newEnv = () => {
    createEnvironment(environment.value)
        .then((result) => {
            dialog.value = false;
            emit("onNewEnvironment");
        })
        .catch((err) => {
            console.log(err);
        });
};
</script>
