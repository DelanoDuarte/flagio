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
  request.post("/environments", JSON.stringify(environment), {
    headers: { "Content-Type": "application/json" },
  });
