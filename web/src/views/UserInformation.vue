<template>
    <div class="mt-4">
        <v-row>
            <v-col cols="auto">
                <v-btn @click.prevent="router.back()" density="compact" variant="text">
                    <v-icon icon="mdi-arrow-left" size="large" />
                    <v-tooltip activator="parent" location="bottom">Back to {{ router.options.history.state.back
                    }}</v-tooltip>
                </v-btn>
            </v-col>
            <v-col cols="auto">
                <div class="mb-2">
                    <div class="text-h5">User Details</div>
                </div>
            </v-col>
        </v-row>
        <UserDetail :user="user" @onEdit="edit($event)" />
    </div>
</template>
<script setup>
import { ref, watchEffect } from "vue";
import { useToast } from "vue-toastification";
import { useRouter, useRoute } from "vue-router";
import UserDetail from "@/components/admin/UserDetail.vue";
import { getUserById, updateUser } from "@/services/api";

const router = useRouter()
const route = useRoute()
const toast = useToast()

const user = ref({})
const getUser = async () => {
    const id = route.params.id
    if (id) {
        user.value = await getUserById(id)
    }
}
const edit = (user) => {
    console.log(user)
    updateUser(user.id, user)
        .then(() => {
            toast.success(`Account ${user.name} updated`)
        })
        .catch(error => console.log(error))
}

watchEffect(async () => {
    getUser()
});
</script>