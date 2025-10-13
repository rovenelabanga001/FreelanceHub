import { defineStore } from "pinia";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    user: null,
    token: null,
    loading: false,
    error: null,
  }),

  actions: {
    async signup(payload) {
      const { $toast } = useNuxtApp();
      this.loading = true;
      this.error = null;

      try {
        const res = await $fetch("/api/auth/signup", {
          method: "POST",
          body: payload,
        });

        this.user = res.user;
        this.token = res.token;
        localStorage.setItem("token", res.token);
        localStorage.setItem("user", JSON.stringify(res.user));

        $toast.success("Signup successful!", {
          position: "bottom-right",
          autoClose: 3000,
        });

        navigateTo("/auth/login");
      } catch (err) {
        this.error = err?.data?.message || "Signup failed";

        $toast.error("Signup failed, try again later", {
          position: "bottom-right",
          autoClose: 3000,
        });
      } finally {
        this.loading = false;
      }
    },

    restoreSession() {
      const token = localStorage.getItem("token");
      const user = localStorage.getItem("user");

      if (token && user) {
        this.token = token;
        this.user = JSON.parse(user);
      }
    },
  },
});
