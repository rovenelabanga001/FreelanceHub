<template>
  <header>
    <div class="fixed top-0 z-50 border-b w-full flex p-4 h-16 justify-between bg-white">
      <div>
        <NuxtLink to="/" class="flex items-center gap-2 cursor-pointer"
          ><Briefcase class="text-blue-600 h-6 w-6" /><span
            >FreelanceHub</span
          ></NuxtLink
        >
      </div>
      <div class="flex justify-between items-center gap-3">
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
    </div>
  </header>
</template>
<script setup>
import { Briefcase } from "lucide-vue-next";
</script>
