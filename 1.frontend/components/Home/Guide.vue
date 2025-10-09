<template>
  <section class="text-center py-20 px-10 flex flex-col gap-10">
    <h2 class="text-lg">How it works</h2>
    <div class="grid md:grid-cols-3 gap-8 px-10">
      <div class="text-center" v-for="step in steps">
        <div
          class="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-4"
        >
          <span class="text-2xl text-blue-600">{{ step.number }}</span>
        </div>
        <h3 class="mb-3">{{ step.title }}</h3>
        <p class="text-gray-600">
          {{ step.description }}
        </p>
      </div>
    </div>
  </section>
</template>
<script setup>
const steps = reactive([
  {
    number: 1,
    title: "Post your project",
    description: "Describe your requirements and set milestones with budgets",
  },
  {
    number: 2,
    title: "Review proposals",
    description:
      "Receive bids from qualified freelancers and choose the best fit",
  },
  {
    number: 3,
    title: "Get it done",
    description: "Collaborate, track progress, and automate milestone payments",
  },
]);
</script>
