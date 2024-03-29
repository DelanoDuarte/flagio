/**
 * plugins/vuetify.js
 *
 * Framework documentation: https://vuetifyjs.com`
 */

// Styles
import "@mdi/font/css/materialdesignicons.css";
import "vuetify/styles";

// Composables
import { VDatePicker } from "vuetify/labs/VDatePicker";
import { createVuetify } from "vuetify";

// https://vuetifyjs.com/en/introduction/why-vuetify/#feature-guides

const defaultTheme = {
  dark: false,
  colors: {
    primary: "#1867C0",
    secondary: "#5CBBF6",
  },
};

const darkTheme = {
  dark: true,
  colors: {
    primary: "#2196F3",
    secondary: "#616161",
    accent: "#FF4081",
    error: "#FF5252",
    info: "#2196F3",
    success: "#4CAF50",
    warning: "#FFC107",
  },
};

export default createVuetify({
  components: {
    VDatePicker,
  },
  theme: {
    defaultTheme: "defaultTheme",
    themes: {
      defaultTheme,
      darkTheme,
    },
  },
});
