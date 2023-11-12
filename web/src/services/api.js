import request from "../utils/request";

// Flags Requests
export const fetchAllFlags = () => request.get("/flags");
export const createFlag = (flag) =>
  request.post("/flags", JSON.stringify(flag), {
    headers: { "Content-Type": "application/json" },
  });
export const activateFlag = (id) => request.post(`/flags/${id}/activate`);
export const deactivateFlag = (id) => request.post(`/flags/${id}/deactivate`);
export const deleteFlag = (id) => request.delete(`/flags/${id}`);

// Environments Requests
export const fetchAllEnvironments = () => request.get("/environments");
export const createEnvironment = (environment) =>
  request.post("/environments/", JSON.stringify(environment), {
    headers: { "Content-Type": "application/json" },
  });
export const environmentKeyGenerator = () =>
  request.post("/environments/key/generator", {
    headers: { "Content-Type": "application/json" },
  });

export const environmentKeyGeneratorById = (id) =>
  request.put(`/environments/${id}/key/generate`, {
    headers: { "Content-Type": "application/json" },
  });

// Authentication Requests
export const signin = ({ username, password }) =>
  request.post("/auth/token", {
    username,
    password,
  });

// Users Requests
export const register = ({ username, password }) =>
  request.post("/user", {
    username,
    password,
  });
