<template>
  <div class="text-start flex justify-between items-center mb-4">
    <div>
      <h1 class="mb-4">Page Header</h1>
      <p class="text-gray-500">Find your next opportunity</p>
    </div>
    <button
      class="flex items-center text-white bg-black rounded-lg px-3 py-2 cursor-pointer"
    >
      <Plus class="h-4 w-4 mr-2 text-white" />
      Post project
    </button>
  </div>
  <div class="flex flex-col bg-white border border-gray-500 rounded-lg p-5">
    <div class="bg-gray-200 flex items-center gap-3 p-3 rounded-lg">
      <Search class="text-gray-500" />
      <input type="text" placeholder="Search projects.." class="bg-gray-200" />
    </div>
  </div>
</template>
<script setup>
import { Plus, Search } from "lucide-vue-next";
</script>
