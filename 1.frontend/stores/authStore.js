import { defineStore } from "pinia";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    user: null,
    token: null,
    loading: false,
    error: null,
  }),

  getters: {
    isAuthenticated: (state) => !!state.user,
  },

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

        $toast.success(res.message || "Signup successful!", {
          position: "bottom-right",
          autoClose: 3000,
        });

        navigateTo("/auth/login");
      } catch (err) {
        const errorMessage =
          err?.data?.error ||
          err?.data?.message ||
          err?.message ||
          "Signup failed";

        this.error = errorMessage;

        $toast.error(errorMessage, {
          position: "bottom-right",
          autoClose: 3000,
        });
      } finally {
        this.loading = false;
      }
    },

    async signin(payload) {
      const { $toast } = useNuxtApp();
      this.loading = true;
      this.error = null;

      try {
        const res = await $fetch("/api/auth/signin", {
          method: "POST",
          body: payload,
        });

        this.user = res.user;

        navigateTo("/");

        $toast.success(res.message || "Login successful!", {
          position: "bottom-right",
          autoClose: 3000,
          theme: "dark",
        });
      } catch (err) {
        const errorMessage =
          err?.data?.message || "Login failed. Please try again.";

        this.error = errorMessage;

        $toast.error(errorMessage, {
          position: "bottom-right",
          autoClose: 3000,
        });

        console.error("Login error:", err);
      } finally {
        this.loading = false;
      }
    },

    async logout() {
      const { $toast } = useNuxtApp();
      this.loading = true;

      try {
        await $fetch("/api/auth/logout", {
          method: "POST",
          credentials: "include",
        });

        this.user = null;

        navigateTo("/auth/login", { replace: true });
        $toast.success("Successfully logged out!", {
          position: "bottom-right",
          autoClose: 3000,
        });
      } catch (err) {
        const errorMessage = err?.data?.message || "Logout failed";
        $toast.error(errorMessage, {
          position: "bottom-right",
          autoClose: 3000,
        });
        console.log(errorMessage);

        console.error("Logout error:", err);
      } finally {
        this.loading = false;
      }
    },

    restoreSession() {
      const user = useCookie("auth_user").value;
      console.log(user);

      if (user) {
        try {
          this.user = JSON.parse(user);
        } catch (err) {
          console.error("Failed to parse auth_user cookie:", err);
          this.user = null;
          useCookie("auth_user").value = null;
          navigateTo("/auth/login");
        }
      } else {
        this.user = null;
        navigateTo("/auth/login");
      }
    },
  },
});
