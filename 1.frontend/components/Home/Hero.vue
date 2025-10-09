<template>
  <section
    class="flex flex-col items-center gap-4 relative bg-gradient-to-br from-blue-600 to-blue-800 text-white py-20"
  >
    <div class="max-w-3xl mx-auto px-10 text-center">
      <h1 class="mb-6 text-lg">Find the Perfect Freelancer for Your Project</h1>
      <p class="text-xl mb-8 text-blue-100 md:text-2xl">
        Connect with talented professionals, manage projects seamlessly, and
        automate payments with confidence
      </p>
    </div>
    <div class="flex gap-2 mx-auto items-center justify-center w-full">
      <input
        type="text"
        placeholder="Search for projects, skills or freelancers..."
        class="bg-white text-gray-900 h-10 px-2 w-[70%] rounded-lg"
      />
      <button class="bg-black rounded-lg h-10 px-2">
        <Search class="h-5 w-5" />
      </button>
    </div>
    <div class="flex gap-6 items-center mt-5">
      <button
        class="rounded-lg bg-white p-2 w-25 h-10 text-black cursor-pointer hover:bg-gray-200"
      >
        Browse projects
      </button>
      <button
        class="rounded-lg bg-none p-2 w-25 border border-white cursor-pointer hover:bg-white hover:text-blue-600"
      >
        Find freelancers
      </button>
    </div>
  </section>
</template>
<script setup>
import { Search } from "lucide-vue-next";
</script>
