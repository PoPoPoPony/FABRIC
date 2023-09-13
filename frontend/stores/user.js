import { defineStore } from "pinia";


export const useUserStore = defineStore('user', {
    state: () => ({
        user_email: ''
    }),

    actions: {
        set_user_email(email) {
            this.user_email = email
        },
    }
})