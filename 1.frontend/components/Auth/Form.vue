<template>
  <form
    class="border bg-white rounded-xl w-full px-5 py-10 flex flex-col gap-4 md:w-[50%] md:mx-auto"
  >
    <div class="text-start flex flex-col gap-2 w-[75%]">
      <span class="font-bold">{{ isSignUp ? "SignUp" : "Login" }}</span>
      <p class="text-gray-500">
        {{
          isSignUp
            ? "Fill in your details to create a new account"
            : "Enter your credentials to access your account"
        }}
      </p>
    </div>
    <div>
      <template v-if="isSignUp">
        <span class="text-lg font-bold">I am a...</span>
        <label class="flex items-center gap-2 cursor-pointer">
          <input type="radio" name="theme" value="light" class="hidden peer" />
          <div
            class="w-2 h-2 rounded-full bg-gray-200 peer-checked:bg-black peer-checked:shadow-lg transition-all"
          ></div>
          <span class="peer-checked:text-black"
            >Freelancer - I want to work on projects</span
          >
        </label>

        <label class="flex items-center gap-2 cursor-pointer">
          <input type="radio" name="theme" value="dark" class="hidden peer" />
          <div
            class="w-2 h-2 rounded-full bg-gray-200 peer-checked:bg-black peer-checked:shadow-lg transition-all"
          ></div>
          <span class="peer-checked:text-black"
            >Client - I want to hire freelancers</span
          >
        </label>
      </template>
    </div>
    <div class="flex flex-col" v-if="isSignUp">
      <label for="username"><span class="font-bold">Username</span></label>
      <input
        type="email"
        name="username"
        placeholder="johndoe"
        class="bg-gray-200 px-2 h-10 rounded-lg focus:outline-none focus:border focus:border-black"
      />
    </div>
    <div class="flex flex-col">
      <label for="email"><span class="font-bold">Email</span></label>
      <input
        type="email"
        name="email"
        placeholder="your@email.com"
        class="bg-gray-200 px-2 h-10 rounded-lg focus:outline-none focus:border focus:border-black"
      />
    </div>
    <div class="flex flex-col">
      <label for="password"><span class="font-bold">Password</span></label>
      <input
        type="password"
        name="password"
        placeholder="*****"
        class="bg-gray-200 px-2 h-10 rounded-lg focus:outline-none focus:border focus:border-black"
      />
    </div>
    <div class="flex flex-col" v-if="isSignUp">
      <label for="confirm_password"
        ><span class="font-bold">Confirm Password</span></label
      >
      <input
        type="password"
        name="confirm_password"
        placeholder="*****"
        class="bg-gray-200 px-2 h-10 rounded-lg focus:outline-none focus:border focus:border-black"
      />
    </div>
    <button
      type="submit"
      class="bg-black text-white rounded-lg h-10 cursor-pointer"
    >
      Sign In
    </button>
    <div class="mt-4 border-b text-center pb-10">
      <template v-if="isSignUp">
        <p class="text-gray-500">
          Already have an account?
          <span
            ><NuxtLink to="/auth/login" class="text-blue-600"
              >Sign In</NuxtLink
            ></span
          >
        </p>
      </template>
      <template v-else>
        <p class="text-gray-500">
          Dont have an account?
          <span
            ><NuxtLink to="/auth/register" class="text-blue-600"
              >Sign Up</NuxtLink
            ></span
          >
        </p>
      </template>
    </div>
  </form>
</template>
<script setup>
const props = defineProps({
  isSignUp: {
    type: Boolean,
    default: false,
  },
});
</script>
