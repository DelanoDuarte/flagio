<template>
    <div>
        <v-row no-gutters>
            <v-col cols="12">
                <v-card elevated title="Profile">
                    <v-card-title>
                        <div class="d-flex flex-row justify-end mb-6">
                            <v-col>
                                <v-avatar size="60" class="justify-center">
                                    <img src="https://i.pravatar.cc/60" alt="User Avatar">
                                </v-avatar>
                            </v-col>
                            <v-btn class="ma-2 pa-2" prepend-icon="mdi mdi-pencil" variant="outlined" color="primary"
                                v-if="!isEditable" @click="isEditable = !isEditable">
                                Edit
                            </v-btn>
                            <v-btn class="ma-2 pa-2" prepend-icon="mdi mdi-cancel" variant="outlined" color="orange"
                                v-if="isEditable" @click="isEditable = !isEditable">
                                Cancel Edit
                            </v-btn>
                            <v-btn class="ma-2 pa-2" prepend-icon="mdi mdi-delete" variant="outlined" color="red">
                                Delete
                            </v-btn>
                            <v-btn class="ma-2 pa-2" prepend-icon="$vuetify" color="green" v-if="isEditable"
                                @click.prevent="save()">
                                Save
                            </v-btn>
                        </div>
                    </v-card-title>
                    <v-card-text>
                        <v-list>
                            <v-list-item>
                                <v-list-item-content>
                                    <v-list-item-title>Firstname</v-list-item-title>
                                    <v-list-item-subtitle>
                                        <v-text-field label="First Name" :value="user?.firstname" v-model="user.firstname"
                                            :disabled="!isEditable"></v-text-field>
                                    </v-list-item-subtitle>
                                </v-list-item-content>
                            </v-list-item>
                            <v-list-item>
                                <v-list-item-content>
                                    <v-list-item-title>Lastname</v-list-item-title>
                                    <v-list-item-subtitle>
                                        <v-text-field label="Last Name" :value="user?.lastname" v-model="user.lastname"
                                            :disabled="!isEditable"></v-text-field>
                                    </v-list-item-subtitle>
                                </v-list-item-content>
                            </v-list-item>
                            <v-list-item>
                                <v-list-item-content>
                                    <v-list-item-title>Email</v-list-item-title>
                                    <v-list-item-subtitle>
                                        <v-text-field label="Email" :value="user?.email" v-model="user.email"
                                            :disabled="!isEditable"></v-text-field>
                                    </v-list-item-subtitle>
                                </v-list-item-content>
                            </v-list-item>
                            <v-list-item>
                                <v-list-item-content>
                                    <v-list-item-title>Roles</v-list-item-title>
                                    <v-list-item-subtitle>
                                        <v-chip v-for="role  in  user?.roles" v-bind:key="role" class="ma-2 text-uppercase"
                                            color="green" variant="flat" label>
                                            <v-icon start icon="mdi-account-circle-outline" />
                                            {{ role }}
                                        </v-chip>
                                    </v-list-item-subtitle>
                                </v-list-item-content>
                            </v-list-item>
                            <!-- Add more details as needed -->
                        </v-list>
                    </v-card-text>
                </v-card>
            </v-col>

        </v-row>
    </div>
</template>
<script setup>
import { ref, watchPostEffect } from "vue";
import { useRoute } from "vue-router";

const route = useRoute()
const isEditable = ref(false)
const user = ref({ firstname: "", lastname: "", email: "" })
const props = defineProps(["user"])
const emit = defineEmits(['onEdit'])

const save = () => {
    isEditable.value = !isEditable.value
    emit('onEdit', { ...user.value })
}

watchPostEffect(() => {
    user.value = { ...props.user }
})
</script>