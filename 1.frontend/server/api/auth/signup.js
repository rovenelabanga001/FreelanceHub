export default defineEventHandler(async (event) => {
  const body = await readBody(event);
  const config = useRuntimeConfig();

  try {
    const response = await $fetch(`${config.public.apiBase}/signup`, {
      method: "POST",
      body,
      credentials: "include", 
    });

    return response;
  } catch (error) {
    throw createError({
      statusCode: error?.statusCode || 500,
      message: error?.data?.error || error?.data?.message || "Signup failed",
    });
  }
});
