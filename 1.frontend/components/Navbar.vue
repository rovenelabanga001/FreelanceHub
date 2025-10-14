<template>
  <header>
    <div
      class="fixed top-0 z-50 border-b w-full flex p-4 h-16 justify-between bg-white"
    >
      <div>
        <NuxtLink to="/" class="flex items-center gap-2 cursor-pointer"
          ><Briefcase class="text-blue-600 h-6 w-6" /><span
            >FreelanceHub</span
          ></NuxtLink
        >
      </div>
      <div
        class="flex items-center justify-evenly gap-4"
        v-if="auth.isAuthenticated"
      >
        <NuxtLink class="cursor-pointer" to="/projects">Projects</NuxtLink>
        <NuxtLink class="cursor-pointer" to="/freelancers"
          >Freelancers</NuxtLink
        >
        <NuxtLink class="cursor-pointer" to="/dashboard/freelancer"
          >Dashboard</NuxtLink
        >
      </div>
      <div
        class="flex justify-between items-center gap-3"
        v-if="!auth.isAuthenticated"
      >
        <button
          @click="navigateTo('/auth/login')"
          class="hover:bg-gray-300 cursor:pointer rounded-lg px-4 py-2 w-auto"
        >
          Login
        </button>
        <button
          @click="navigateTo('/auth/register')"
          class="text-white bg-black cursor:pointer rounded-lg px-4 py-2 w-auto"
        >
          Sign Up
        </button>
      </div>
      <div class="flex items-center gap-3" v-if="auth.isAuthenticated">
        <div
          class="hidden md:flex items-center gap-2 px-3 py-1.5 bg-green-50 rounded-lg"
        >
          <Wallet class="h-4 w-4 text-green-600" />
          <span>$12,803</span>
        </div>

        <button class="flex items-center gap-1">
          <User class="h-5 w-5" />
          <span class="hidden md:inline">{{auth.user?.username}}</span>
        </button>
        <NuxtLink><Bell class="h-5 w-5" /></NuxtLink>
        <button @click="auth.logout">Logout</button>
      </div>
    </div>
  </header>
</template>
<script setup>
import { Briefcase, Bell, Wallet, User } from "lucide-vue-next";

const auth = useAuthStore();
</script>
