<template>
    <v-dialog v-model="dialog" max-width="400">
        <v-card>
            <v-card-title class="headline">
                Are you sure you want to delete?
            </v-card-title>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
                <v-btn color="red darken-1" text @click="confim">Delete</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script setup>
import { ref } from 'vue'

const emit = defineEmits(["onConfirmDelete"])
const dialog = ref(false);
const key = ref(null)

const open = (reference) => {
    key.value = reference
    dialog.value = true;
}

const close = () => {
    dialog.value = false;
}
const confim = () => {
    emit('onConfirmDelete', key.value);
    close();
}

defineExpose({
    open
})
</script>