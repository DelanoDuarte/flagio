// Composables
import { createRouter, createWebHistory } from "vue-router";
import { useAuthStore } from "@/store/auth.js";

const isAuthenticatedGuard = (to, from, next) => {
  const auth = useAuthStore();
  if (to.name !== "Login" && !auth.isAuthenticated()) {
    next({ name: "Login" });
  } else {
    next();
  }
};

const routes = [
  {
    path: "/login",
    children: [
      {
        path: "",
        name: "Login",
        component: () =>
          import(/* webpackChunkName: "home" */ "@/views/Login.vue"),
      },
    ],
  },
  {
    path: "/",
    component: () => import("@/layouts/default/Default.vue"),
    beforeEnter: [isAuthenticatedGuard],
    children: [
      {
        path: "",
        name: "Home",
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
          import(/* webpackChunkName: "home" */ "@/views/Home.vue"),
      },
    ],
  },
  {
    path: "/flags",
    beforeEnter: [isAuthenticatedGuard],
    component: () => import("@/layouts/default/Default.vue"),
    children: [
      {
        path: "",
        name: "Flags",
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
          import(/* webpackChunkName: "home" */ "@/views/Flags.vue"),
      },
    ],
  },
  {
    path: "/environments",
    beforeEnter: [isAuthenticatedGuard],
    component: () => import("@/layouts/default/Default.vue"),
    children: [
      {
        path: "",
        name: "Environment",
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
          import(/* webpackChunkName: "home" */ "@/views/Environment.vue"),
      },
    ],
  },
  {
    path: "/administration",
    beforeEnter: [isAuthenticatedGuard],
    component: () => import("@/layouts/default/Default.vue"),
    children: [
      {
        path: "",
        name: "Administration",
        component: () =>
          import(/* webpackChunkName: "home" */ "@/views/Administration.vue"),
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
