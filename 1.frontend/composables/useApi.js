export const useApi = () => {
  const baseUrl = "/api";

  const apiFetch = async (endpoint, options = {}) => {
    try {
      const res = await $fetch(`${baseUrl}${endpoint}`, {
        credentials: "include",
        headers: {
          "Content-Type": "application/json",
          ...(options.headers || {}),
        },
        ...options,
      });

      return res;
    } catch (error) {
      console.error("API error:", error);
      throw error;
    }
  };

  return { apiFetch };
};
