<template>
  <div class="flex flex-col items-center gap-5 py-20 bg-gray-100 min-h-screen">
    <div class="flex flex-col items-center text-center gap-4">
      <Briefcase class="text-blue-600 h-10 w-10" />
      <h2 class="text-lg">Welcome Back</h2>
      <p class="text-lg text-gray-500">Sign in to your FreelanceHub Account</p>
    </div>
    <div class="w-full px-3">
     <AuthForm />
    </div>
  </div>
</template>
<script setup>
import { Briefcase } from "lucide-vue-next";
</script>
