import axios from "axios";

const instance = axios.create({
  timeout: 10000,
  baseURL: import.meta.env.VITE_BASE_URL,
});

instance.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("access_token");
    if (token) {
      config.headers["Content-Type"] = "application/json";
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

instance.interceptors.response.use(
  ({ data }) => data,
  ({ message, response }) => {
    if (response.status === 401) {
      window.localStorage.clear();
      window.location = "/login";
      console.log("Interceptor Login");
      return Promise.reject(error);
    }
    Promise.reject(response ? response.data : message);
  }
);
export default instance;
