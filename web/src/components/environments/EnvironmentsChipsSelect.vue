<template>
  <v-select
    @update:modelValue="emit('onChange', $event)"
    :items="props.environments"
    :item-title="props['item-label']"
    :item-value="props['item-value']"
    :label="props.label"
    chips
    multiple
  >
  </v-select>
</template>

<script setup>
const props = defineProps(["environments", "label", "item-label", "item-value"]);
const emit = defineEmits(["onChange"]);
</script>
