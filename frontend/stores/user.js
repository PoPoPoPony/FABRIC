import { defineStore } from "pinia";


export const useUserStore = defineStore('user', {
    state: () => ({
        user_email: '',
        user_role: ''
    }),
    persist: {
        storage: persistedState.localStorage,
    },

    actions: {
        set_user_email(email) {
            this.user_email = email
        },
        set_user_role(role) {
            this.user_role = role
        }
    }
})