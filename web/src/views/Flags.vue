<template>
    <div>
        <div class="text-h5">
            All Feature Flags
        </div>

        <br />
        <Transition name="fade" mode="out-in">
            <v-skeleton-loader boilerplate type="card">
                <v-card elevated title="Flags">
                    <v-card-text class="text-right">
                        <NewFlag :key="newFlagComponent" @onNewFlag="onNewFlag" />
                    </v-card-text>
                    <ListFlags :flags="flags" @onFlagRemoval="onDeleteFlag($event)" @onFlagChanged="fetchFlags" />
                    <DeleteFlagDialog ref="deleteDialog" @onConfirmDelete="confirmDelete($event)" />
                </v-card>
            </v-skeleton-loader>
        </Transition>
    </div>
</template>
  
<script setup>
import ListFlags from "@/components/flags/ListFlags.vue";
import NewFlag from "@/components/flags/NewFlag.vue";
import DeleteFlagDialog from "@/components/flags/DeleteFlagDialog.vue";

import { ref, watchEffect } from 'vue';
import { useToast } from "vue-toastification";
import { fetchAllFlags, deleteFlag } from '@/services/api'

const toast = useToast();

const flags = ref([])
const newFlagComponent = ref(0)
const isLoading = ref(true)
const deleteDialog = ref(DeleteFlagDialog)

const fetchFlags = async () => {
    flags.value = await fetchAllFlags().finally(() => isLoading.value = false);
}

const onNewFlag = () => {
    fetchFlags();
    newFlagComponent.value += 1
}

const confirmDelete = (id) => {
    deleteFlag(id)
        .then((flag) => {
            toast.success(`Flag deleted`)
        })
        .catch(err => {
            console.log(err)
        }).finally(() => {
            fetchFlags();
        })
}

const onDeleteFlag = (id) => {
    deleteDialog.value?.open(id);
}

watchEffect(async () => {
    fetchFlags()
});
</script>
  