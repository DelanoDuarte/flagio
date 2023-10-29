<template>
    <v-dialog width="700" v-model="dialog">
        <template v-slot:activator="{ props }">
            <v-btn v-bind="props" color="primary" text="New Flag"> </v-btn>
        </template>

        <template v-slot:default="{ isActive }">
            <v-card title="New Flag">
                <v-card-text>
                    <v-container>
                        <v-row>
                            <v-col cols="12">
                                <v-text-field v-model="flag.name" ref="flagName" label="Name *" required
                                    :rules="[() => !!flagName || 'This field is required']">
                                </v-text-field>
                            </v-col>
                        </v-row>

                        <v-row>
                            <v-col cols="12">
                                <v-text-field v-model="flag.description" label="Description"></v-text-field>
                            </v-col>
                        </v-row>

                        <v-row>
                            <v-col cols="4">
                                <v-switch label="Expiration" color="green" inset v-model="flagWithExpiration"></v-switch>
                            </v-col>
                            <v-col cols="8">
                                <v-text-field 
                                    v-model="flag.expiration_date" 
                                    label="Expiration Date" 
                                    type="date"
                                    :disabled="!flagWithExpiration" 
                                    format="YYYY-MM-DD">
                                </v-text-field>
                            </v-col>
                        </v-row>

                        <v-row>
                            <v-col cols="12">
                                <EnvironmentsChipsSelect label="Environments" :environments="environments" item-label="name"
                                    item-value="id" @onChange="onSelectEnvironment($event)" />
                            </v-col>
                        </v-row>
                    </v-container>
                </v-card-text>

                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue-darken-1" variant="text" @click="dialog = false">
                        Close
                    </v-btn>
                    <v-btn color="blue-darken-1" variant="text" @click="newFlag"> Save </v-btn>
                </v-card-actions>
            </v-card>
        </template>
    </v-dialog>
</template>

<script setup>
import { ref, watchEffect } from "vue";
import { useToast } from "vue-toastification";

import EnvironmentsChipsSelect from "@/components/environments/EnvironmentsChipsSelect.vue";
import { createFlag, fetchAllEnvironments } from "@/services/api";

const emit = defineEmits(["onNewFlag"]);

const toast = useToast();

const dialog = ref(false);
const flagWithExpiration = ref(false);

const flag = ref({
    name: "",
    description: "",
    expiration_date: "",
    environments: [],
});
const environments = ref([]);

function newFlag() {
    createFlag(flag.value)
        .then((result) => {
            dialog.value = false;
            emit("onNewFlag");
            toast.success(`New flag ${flag.value.name} created`);
        })
        .catch((err) => {
            console.log(err);
        });
}

const onSelectEnvironment = (envs) => {
    console.log(envs);
    flag.value.environments = envs;
};

const fetchEnvironments = async () => {
    const envs = await fetchAllEnvironments();
    environments.value = envs.map((e) => ({
        title: e.name,
        value: e.id,
    }));
};

watchEffect(() => {
    fetchEnvironments();
});
</script>
