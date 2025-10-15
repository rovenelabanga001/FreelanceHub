<template>
  <div class="text-start flex justify-between items-center mb-4">
    <div>
      <h1 class="mb-4 text-2xl font-bold">Browse Projects</h1>
      <p class="text-gray-500">Find your next opportunity</p>
    </div>
    <button
      class="flex items-center text-white bg-black rounded-lg px-3 py-2 cursor-pointer"
    >
      <Plus class="h-4 w-4 mr-2 text-white" />
      Post project
    </button>
  </div>
  <div
    class="flex flex-col bg-white border border-gray-500 rounded-lg p-5 gap-2 md:grid md:grid-cols-2 lg:grid-cols-4"
  >
    <div class="relative w-full">
      <Search
        class="absolute left-3 top-1/2 -translate-y-1/2 text-gray-500 w-5 h-5"
      />
      <input
        type="text"
        placeholder="Search projects..."
        class="w-full md:w-64 pl-10 pr-3 py-2 bg-gray-100 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
      />
    </div>
    <select
      class="w-full md:w-64 py-2 px-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-100 text-gray-700"
    >
      <option class="bg-gray-200" selected>All categories</option>
      <option class="bg-gray-200">Web Development</option>
      <option class="bg-gray-200">Cyber Security</option>
      <option class="bg-gray-200">AI/ML</option>
    </select>
    <select
      class="w-full md:w-64 p-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-100 text-gray-700"
    >
      <option class="bg-gray-200" selected>All status</option>
      <option class="bg-gray-200">Open</option>
      <option class="bg-gray-200">In progress</option>
      <option class="bg-gray-200">Completed</option>
    </select>
    <select
      class="w-full md:w-64 p-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-100 text-gray-700"
    >
      <option class="bg-gray-200" selected>Newest First</option>
      <option class="bg-gray-200">Oldest First</option>
      <option class="bg-gray-200">Budget: Low to High</option>
      <option class="bg-gray-200">Budget: High to Low</option>
    </select>
  </div>
</template>
<script setup>
import { Plus, Search } from "lucide-vue-next";
</script>
