<template>
  <form
    @submit.prevent="onSubmit"
    class="border bg-white rounded-xl w-full px-5 py-10 flex flex-col gap-4 md:w-[50%] md:mx-auto"
  >
    <!-- Title -->
    <div class="text-start flex flex-col gap-2 w-[75%]">
      <span class="font-bold">{{ isSignUp ? "Sign Up" : "Login" }}</span>
      <p class="text-gray-500">
        {{
          isSignUp
            ? "Fill in your details to create a new account"
            : "Enter your credentials to access your account"
        }}
      </p>
    </div>

    <!-- Radio: Role -->
    <div v-if="isSignUp">
      <span class="text-lg font-bold">I am a...</span>
      <div class="flex flex-col gap-2">
        <label class="flex items-center gap-2 cursor-pointer">
          <input
            type="radio"
            value="freelancer"
            v-model="form.role"
            class="hidden peer"
          />
          <div
            class="w-2 h-2 rounded-full bg-gray-200 peer-checked:bg-black transition-all"
          ></div>
          <span class="peer-checked:text-black"
            >Freelancer - I want to work on projects</span
          >
        </label>

        <label class="flex items-center gap-2 cursor-pointer">
          <input
            type="radio"
            value="client"
            v-model="form.role"
            class="hidden peer"
          />
          <div
            class="w-2 h-2 rounded-full bg-gray-200 peer-checked:bg-black transition-all"
          ></div>
          <span class="peer-checked:text-black"
            >Client - I want to hire freelancers</span
          >
        </label>
      </div>
      <small v-if="v$.form.role.$error" class="text-red-500"
        >Please select a role</small
      >
    </div>

    <!-- Username -->
    <div class="flex flex-col" v-if="isSignUp">
      <label for="username"><span class="font-bold">Username</span></label>
      <input
        type="text"
        v-model.trim="form.username"
        name="username"
        placeholder="johndoe"
        class="bg-gray-200 px-2 h-10 rounded-lg focus:outline-none focus:border focus:border-black"
      />
      <small v-if="v$.form.username.$error" class="text-red-500"
        >Username is required</small
      >
    </div>

    <!-- Email -->
    <div class="flex flex-col">
      <label for="email"><span class="font-bold">Email</span></label>
      <input
        type="email"
        v-model.trim="form.email"
        name="email"
        placeholder="your@email.com"
        class="bg-gray-200 px-2 h-10 rounded-lg focus:outline-none focus:border focus:border-black"
      />
      <small v-if="v$.form.email.$error" class="text-red-500">
        <span v-if="!v$.form.email.required.$response">Email is required</span>
        <span v-else-if="!v$.form.email.email.$response">Invalid email</span>
      </small>
    </div>

    <!-- Password -->
    <div class="flex flex-col">
      <label for="password"><span class="font-bold">Password</span></label>
      <input
        type="password"
        v-model="form.password"
        name="password"
        placeholder="*****"
        class="bg-gray-200 px-2 h-10 rounded-lg focus:outline-none focus:border focus:border-black"
      />

      <!-- Show validation messages one at a time -->
      <small v-if="v$.form.password.$error" class="text-red-500">
        <span v-if="!v$.form.password.required.$response"
          >Password is required</span
        >
        <span v-else-if="!v$.form.password.minLength.$response"
          >At least 8 characters</span
        >
        <span v-else-if="!v$.form.password.hasUppercase.$response"
          >Must contain an uppercase letter</span
        >
        <span v-else-if="!v$.form.password.hasLowercase.$response"
          >Must contain a lowercase letter</span
        >
        <span v-else-if="!v$.form.password.hasNumber.$response"
          >Must contain a number</span
        >
        <span v-else-if="!v$.form.password.hasSpecial.$response"
          >Must contain a special character</span
        >
      </small>
    </div>

    <!-- Confirm Password -->
    <div class="flex flex-col" v-if="isSignUp">
      <label for="confirm_password"
        ><span class="font-bold">Confirm Password</span></label
      >
      <input
        type="password"
        v-model="form.confirm_password"
        name="confirm_password"
        placeholder="*****"
        class="bg-gray-200 px-2 h-10 rounded-lg focus:outline-none focus:border focus:border-black"
      />
      <small v-if="v$.form.confirm_password.$error" class="text-red-500">
        <span v-if="!v$.form.confirm_password.required.$response"
          >Confirm password is required</span
        >
        <span v-else-if="!v$.form.confirm_password.sameAsPassword.$response"
          >Passwords do not match</span
        >
      </small>
    </div>

    <button
      type="submit"
      class="bg-black text-white rounded-lg h-10 cursor-pointer"
    >
      {{ isSignUp ? "Sign Up" : "Login" }}
    </button>

    <div class="mt-4 border-b text-center pb-10">
      <template v-if="isSignUp">
        <p class="text-gray-500">
          Already have an account?
          <NuxtLink to="/auth/login" class="text-blue-600">Sign In</NuxtLink>
        </p>
      </template>
      <template v-else>
        <p class="text-gray-500">
          Don’t have an account?
          <NuxtLink to="/auth/register" class="text-blue-600">Sign Up</NuxtLink>
        </p>
      </template>
    </div>
  </form>
</template>

<script setup>
import useVuelidate from "@vuelidate/core";
import { required, email, minLength, helpers } from "@vuelidate/validators";
import { useAuthStore } from "~/stores/authStore";

const props = defineProps({
  isSignUp: { type: Boolean, default: false },
});

const auth = useAuthStore();

const form = reactive({
  role: "",
  username: "",
  email: "",
  password: "",
  confirm_password: "",
});

// Custom password validators (each returns true/false cleanly)
const hasUppercase = helpers.withMessage(
  "Must contain an uppercase letter",
  (value) => /[A-Z]/.test(value || "")
);

const hasLowercase = helpers.withMessage(
  "Must contain a lowercase letter",
  (value) => /[a-z]/.test(value || "")
);

const hasNumber = helpers.withMessage("Must contain a number", (value) =>
  /\d/.test(value || "")
);

const hasSpecial = helpers.withMessage(
  "Must contain a special character",
  (value) => /[^A-Za-z0-9]/.test(value || "")
);

const sameAsPassword = helpers.withMessage(
  "Passwords do not match",
  (value) => value === form.password
);

// Dynamic rules
const rules = computed(() => ({
  form: {
    role: props.isSignUp ? { required } : {},
    username: props.isSignUp ? { required } : {},
    email: { required, email },
    password: props.isSignUp
      ? {
          required,
          minLength: minLength(8),
          hasUppercase,
          hasLowercase,
          hasNumber,
          hasSpecial,
        }
      : { required },
    confirm_password: props.isSignUp ? { required, sameAsPassword } : {},
  },
}));

const v$ = useVuelidate(rules, { form });

// Handle form submission
const onSubmit = async () => {
  v$.value.$touch();
  if (props.isSignUp && !v$.value.$invalid) {
    await auth.signup(form);
  } else if (!props.isSignUp && !v$.value.$invalid) {
    await auth.signin(form);
  }
};
</script>
