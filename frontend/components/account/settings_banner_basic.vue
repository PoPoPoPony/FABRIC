<template>
    <button class="w-full h-10 py-2 grid grid-cols-10" @click="banner_click">
        <div class="col-span-3 font-bold text-left pl-4"> {{ label }}</div>
        <div class="col-start-4 col-span-6 text-right text-neutral-300"> {{ user_label }}</div>
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="col-start-10 col-span-1 text-neutral-300 p-1.5 place-self-center">
            <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
        </svg>
    </button>
</template>
<script>
export default {
    props: ["label", "user_label"],
    data() {
        return {

        }
    },
    methods: {
        banner_click() {
            if (this.label == "寶貝") {
                navigateTo("/baby_detail_list")
            }
        }
    }
}
</script>
<style lang="scss">
    
</style>