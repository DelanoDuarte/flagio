<template>
    <v-alert v-if="enabled" :type="type" :text="text" :icon="icon">

        <template v-slot:icon v-if="icon">
            {{ icon }}
        </template>

        <template v-slot:title v-if="title">
            {{ title }}
        </template>
    </v-alert>
</template>

<script setup>
import { ref } from 'vue'

const enabled = ref(true)

const type = ref('info')
const title = ref(undefined)
const text = ref('Random')
const icon = ref(undefined)

const show = (alertType, alertTitle, alertText, alertIcon) => {
    enabled.value = true

    type.value = alertType;
    title.value = alertTitle;
    text.value = alertText;
    icon.value = alertIcon;
}

defineExpose({
    show
})
</script>
