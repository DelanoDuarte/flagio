<template>
    <div>
        <div class="text-h5">All Environments</div>
        <br />

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

        <br />

        <Transition name="fade" mode="out-in">
            <v-card elevated title="Environments">
                <v-card-text class="text-right">
                    <NewEnvironment @onNewEnvironment="fetchEnvironments" />
                </v-card-text>
                <ListEnvironments :environments="environments" @onGenerateKey="generateKey($event)" />
            </v-card>
        </Transition>
    </div>
</template>

<script setup>
import { watchEffect, ref } from "vue";
import { useToast } from "vue-toastification";
import ListEnvironments from "@/components/environments/ListEnvironments.vue";
import NewEnvironment from "@/components/environments/NewEnvironment.vue";
import { fetchAllEnvironments, environmentKeyGeneratorById } from "@/services/api";

const environments = ref([]);
const cards = ref([
    {
        title: "Requests",
        qt: "61",
        icon: "mdi-arrow-bottom-right-thick",
        color: "success"
    },
]);
const toast = useToast()

const fetchEnvironments = async () => {
    environments.value = await fetchAllEnvironments();
};
const generateKey = async (id) => {
    environmentKeyGeneratorById(id)
        .then((env) => {
            fetchEnvironments();
            toast.success(`Key generated for environment ${env.name}`);
        })
        .catch((error) => console.log(error))
}

watchEffect(async () => {
    fetchEnvironments();
});
</script>
