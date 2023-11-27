<template>
    <v-dialog width="700" v-model="dialog">
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
                        <v-row>
                            <v-col cols="12">
                                <v-text-field v-model="environment.key" variant="filled" label="Key" type="text">
                                    <template v-slot:prepend>
                                        <v-tooltip location="bottom">
                                            <template v-slot:activator="{ props }">
                                                <v-icon v-bind="props" icon="mdi-shield-key" @click="generateKey"></v-icon>
                                            </template>
                                            Generate Key
                                        </v-tooltip>
                                    </template>
                                </v-text-field>
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
import { createEnvironment, environmentKeyGenerator } from '@/services/api';
import { ref, watchEffect } from "vue";

const emit = defineEmits(['onNewEnvironment'])

const dialog = ref(false);
const environment = ref({
    name: "",
    key: undefined
});
const loadingKeyGen = ref(false)

const generateKey = async () => {
    loadingKeyGen.value = true
    environmentKeyGenerator()
        .then(key => environment.value.key = key)
        .finally(() => loadingKeyGen.value = false)
}

const newEnv = () => {
    createEnvironment(environment.value)
        .then((result) => {
            dialog.value = false;
            emit("onNewEnvironment");
        })
        .catch((err) => {
            console.error(err);
        });
};
</script>
