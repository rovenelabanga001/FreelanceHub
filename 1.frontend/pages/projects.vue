<template>
  <section class="min-h-screen px-4 py-10 bg-gray-200">
    <ProjectsPageHeader />
  </section>
</template>
<script setup>
const { apiFetch } = useApi();

let projects = [];

try {
  projects = await apiFetch("/projects");
} catch (err) {
  console.error("API error:", err);
}

console.log(projects)
</script>
