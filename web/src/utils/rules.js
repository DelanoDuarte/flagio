export const nameRules = [
  (value) => {
    if (value) return true;
    return "Name is required.";
  },
  (value) => {
    if (value?.length <= 64) return true;
    return "Name must be less than 64 characters.";
  },
];
