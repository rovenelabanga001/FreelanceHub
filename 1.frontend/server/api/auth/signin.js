export default defineEventHandler(async (event) => {
  try {
    const body = await readBody(event);
    const config = useRuntimeConfig();

    const response = await $fetch.raw(`${config.public.apiBase}/signin`, {
      method: "POST",
      body,
      credentials: "include",
    });

    // forward Set-Cookie header
    if (response.headers.get("set-cookie")) {
      event.node.res.setHeader(
        "set-cookie",
        response.headers.get("set-cookie")
      );
    }

    // forward rest of the body
    return response._data;
  } catch (error) {
    const message = error?.data?.error || "Login failed. Please try again.";

    throw createError({
      statusCode: error?.statusCode || 500,
      statusMessage: message,
      data: { message },
    });
  }
});
