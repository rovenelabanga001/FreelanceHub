<template>
  <section class="px-20 border border-b bg-gray-100">
    <div class="grid grid-cols-2 items-center py-20 gap-10 min-w-full md:grid-cols-4">
      <div
        class="flex flex-col items-center"
        v-for="stat in stats"
        :key="stat.label"
      >
        <component :is="stat.icon" class="w-10 h-10 text-blue-600" />
        <span class="text-2xl">{{ stat.value }}</span>
        <h5 class="text-gray-500 text-sm">{{ stat.label }}</h5>
      </div>
    </div>
  </section>
</template>
<script setup>
import { Briefcase } from "lucide-vue-next";
import { Users } from "lucide-vue-next";
import { DollarSign } from "lucide-vue-next";
import { TrendingUp } from "lucide-vue-next";

const stats = reactive([
  { label: "Active Projects", value: "389", icon: Briefcase },
  { label: "Freelancers", value: "1,247", icon: Users },
  { label: "Total Paid Out", value: "$2.4M", icon: DollarSign },
  { label: "Success Rate", value: "96%", icon: TrendingUp },
]);
</script>
