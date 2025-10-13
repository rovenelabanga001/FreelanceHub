import { usePinia } from '#imports'
import CryptoJS from "crypto-js"

export default defineNuxtPlugin(() => {
 
  const pinia = usePinia()
  const config = useRuntimeConfig()
  const SECRET_KEY = config.public.secretKey

  
  pinia.use(({ store }) => {
    if (store.$id !== "auth") return

    const storedData = localStorage.getItem(`pinia-${store.$id}`)
    if (storedData) {
      try {
        const parsed = JSON.parse(storedData)

        // Decrypt token
        if (parsed.encryptedToken) {
          const bytes = CryptoJS.AES.decrypt(parsed.encryptedToken, SECRET_KEY)
          parsed.token = bytes.toString(CryptoJS.enc.Utf8)
          delete parsed.encryptedToken
        }

        // Decrypt user
        if (parsed.encryptedUser) {
          const bytes = CryptoJS.AES.decrypt(parsed.encryptedUser, SECRET_KEY)
          parsed.user = JSON.parse(bytes.toString(CryptoJS.enc.Utf8))
          delete parsed.encryptedUser
        }

        store.$patch(parsed)
      } catch (error) {
        console.error("Failed to decrypt auth store:", error)
      }
    }

    // Watch and persist changes
    store.$subscribe((_, state) => {
      try {
        const dataToStore = { ...state }

        if (state.token) {
          dataToStore.encryptedToken = CryptoJS.AES.encrypt(
            state.token,
            SECRET_KEY
          ).toString()
          delete dataToStore.token
        }

        if (state.user) {
          dataToStore.encryptedUser = CryptoJS.AES.encrypt(
            JSON.stringify(state.user),
            SECRET_KEY
          ).toString()
          delete dataToStore.user
        }

        localStorage.setItem(`pinia-${store.$id}`, JSON.stringify(dataToStore))
      } catch (error) {
        console.error("Failed to encrypt auth store:", error)
      }
    })
  })
})
