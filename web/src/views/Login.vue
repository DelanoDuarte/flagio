<template>
    <v-container>
        <v-row justify="center">
            <v-col cols="12" sm="8" md="4">
                <v-card>
                    <v-card-title class="headline">Login</v-card-title>

                    <!-- Form for username and password -->
                    <v-card-text>
                        <v-form @submit.prevent="authenticate">
                            <v-text-field v-model="login.username" label="Username"></v-text-field>
                            <v-text-field v-model="login.password"
                                :append-inner-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                                :type="showPassword ? 'text' : 'password'" label="Password" required
                                @click:append-inner="showPassword = !showPassword"></v-text-field>

                            <!-- Remember me checkbox -->
                            <v-checkbox v-model="login.rememberMe" label="Remember Me"></v-checkbox>

                            <div class="d-flex flex-row mb-6">
                                <!-- Forgot password link -->
                                <v-btn text>Forgot Password?</v-btn>

                                <!-- Login button -->
                                <v-btn type=" submit" color="primary">Login</v-btn>
                            </div>
                        </v-form>
                    </v-card-text>

                    <!-- Social login options -->
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn icon>
                            <v-icon color="red">mdi-google</v-icon>
                        </v-btn>
                        <v-btn icon>
                            <v-icon color="blue">mdi-facebook</v-icon>
                        </v-btn>
                        <v-btn icon>
                            <v-icon color="blue">mdi-twitter</v-icon>
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/store/auth';
import { useToast } from "vue-toastification";
import { signin } from '@/services/api'

const router = useRouter()
const toast = useToast()
const login = ref({
    username: "",
    password: "",
    rememberMe: false
})
const showPassword = ref(false)

const authenticate = () => {
    signin({ ...login.value })
        .then((res) => {
            // Get access token
            useAuthStore().signin(res)
            router.push({ path: "/" })
            toast.success('Successful Login')
        })
        .catch((error) => {
            console.log(error)
            toast.warning('Usernamr or password is wrong.')
        })
}
</script>