<template>
  <section class="text-lg flex flex-col gap-5 items-center justify-center py-20">
    <h2>Browse by Category</h2>
    <div class="grid grid-cols-2 gap-4 items-center px-10 md:grid-cols-3 md:gap-10 lg:grid-cols-6">
        <div v-for="cat in categories" class="border rounded-xl aspect-square flex items-center justify-center text-center px-5 hover:shadow-lg cursor-pointer">
            <span>{{ cat }}</span>
        </div>
    </div>
  </section>
</template>
<script setup>
const categories = reactive([
  "Web Development",
  "Mobile Development",
  "Design",
  "Content Writing",
  "Marketing",
  "Data Science",
]);
</script>
