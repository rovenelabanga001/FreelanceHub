export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig();

  try {
    // Extract cookies from the incoming request
    const cookieHeader = getHeader(event, "cookie");

    // Make the backend logout call with those cookies
    const response = await $fetch.raw(`${config.public.apiBase}/signout`, {
      method: "POST",
      headers: {
        cookie: cookieHeader || "",
      },
      credentials: "include",
    });

    // Forward the Set-Cookie header back to the browser
    const setCookieHeader = response.headers.get("Set-Cookie");
    if (setCookieHeader) {
      event.node.res.setHeader("Set-Cookie", setCookieHeader);
      console.log("Forwarded Set-Cookie:", setCookieHeader);
    }

    return response._data;
  } catch (error) {
    console.error("Logout proxy error:", error);

    throw createError({
      statusCode: error?.statusCode || 500,
      message:
        error?.data?.error ||
        error?.data?.message ||
        "Logout failed. Please try again.",
    });
  }
});
