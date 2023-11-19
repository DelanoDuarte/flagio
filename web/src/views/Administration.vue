<template>
    <div>
        <h1>Administration</h1>

        <v-card elevated title="Users">
            <ListUsers :users="users" />
        </v-card>
    </div>
</template>

<script setup>
import { ref, watchEffect } from 'vue'
import { fetchAllUsers } from '@/services/api'
import ListUsers from '@/components/admin/ListUsers.vue'

const isLoading = ref(true)
const users = ref([])

const fetchUsers = async () => {
    users.value = await fetchAllUsers().finally(() => isLoading.value = false);
}

watchEffect(async () => {
    fetchUsers();
})

</script>