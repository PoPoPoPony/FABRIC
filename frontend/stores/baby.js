import { defineStore } from "pinia";


export const useBabyStore = defineStore('baby', {
    state: () => ({
        baby_ids: [],
        baby_avatars: [],
        baby_names: [],
    }),
    persist: {
        storage: persistedState.localStorage,
    },

    actions: {
        add_baby_id(id) {
            this.baby_ids.push(id)
        },
        add_baby_avatar(avatar) {
            this.baby_avatars.push(avatar)
        },
        add_baby_name(name) {
            this.baby_names.push(name)
        },
        clear_all_babys() {
            this.baby_ids = []
            this.baby_avatars = []
            this.baby_names = []
        }


    }
})