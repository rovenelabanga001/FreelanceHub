export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig();

  try {
    const response = await $fetch(`${config.public.apiBase}/projects`, {
      credentials: "include",
      headers: {
        cookie: getHeader(event, "cookie") || "",
      },
    });

    return response;
  } catch (error) {
    console.error("Proxy error (projects):", error);
    throw createError({
      statusCode: error.statusCode || 500,
      message:
        error?.data?.error ||
        error?.data?.message ||
        "Failed to fetch projects. Please try again later.",
    });
  }
});
