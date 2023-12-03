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

const hasRoleGuard = (to, from, next) => {
  const roles = useAuthStore().getRoles();
  const requiredRoles = to.meta.roles;

  if (!requiredRoles || requiredRoles.some((role) => roles.includes(role))) {
    next();
  } else {
    next("/unauthorized"); // Redirect to unauthorized page or handle accordingly
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
    beforeEnter: [isAuthenticatedGuard, hasRoleGuard],
    component: () => import("@/layouts/default/Default.vue"),
    meta: {
      roles: ["admin"],
    },
    children: [
      {
        path: "",
        name: "Administration",
        component: () =>
          import(/* webpackChunkName: "home" */ "@/views/Administration.vue"),
      },
      {
        path: "users/:id",
        name: "UserInformation",
        component: () =>
          import(/* webpackChunkName: "home" */ "@/views/UserInformation.vue"),
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
