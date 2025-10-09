<template>
  <section class="py-20 px-10 bg-gray-100">
    <div class="flex justify-between items-center">
      <h1 class="text-lg">Featured Projects</h1>
      <button class="flex items-center gap-2 cursor-pointer p-2 hover:bg-gray-200 hover:rounded-lg ">
        <span>View All</span> <ArrowRight class="ml-2 h-4 w-4" />
      </button>
    </div>
    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div></div>
    </div>
  </section>
</template>
<script setup>
import { ArrowRight } from "lucide-vue-next";
</script>
