import { defineNuxtConfig } from "nuxt/config";

export default defineNuxtConfig({
  runtimeConfig: {
    public: {
      apiBase: process.env.API_BASE || "http://localhost:5000",
      secretKey: process.env.SECRET_KEY,
    },
  },
  devServer: {
    proxy: {
      "/api": {
        target: "http://localhost:5000", // backend
        changeOrigin: true,
        secure: false,
        cookieDomainRewrite: "localhost", // ensures cookies work
      },
    },
  },
  css: ["~/assets/css/global.css"],
  modules: ["@nuxtjs/tailwindcss", "@pinia/nuxt"],
});
