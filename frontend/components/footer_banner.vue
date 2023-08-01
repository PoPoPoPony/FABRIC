<script>

export default {
    props: ["page_type"],
    created () {

    },
    computed() {

    },
    mounted() {

    },
    data() {
        // four page name: babyinfo / statistic / knowledge / account
        return 0
    },
    methods: {
        onBabyinfoClick() {
            navigateTo("/babyinfo")
        },
        onStatisticClick() {
            navigateTo("/statistic")
        },
        onKnowledgeClick() {
            navigateTo("/knowledge")
        },
        onAccountClick() {
            navigateTo("/account")
        },
    }
}



</script>

<template>
<!-- text-slate-950  -->
    <div class="bg-neutral-50 relative grid grid-rows-6 grid-cols-10 justify-evenly mx-5 overflow-visible">
        <button @click="onBabyinfoClick" class="w-12 h-6 col-start-1 col-span-2 row-start-1 row-span-4 place-self-center items-center">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-12 h-6"  :class="page_type == 'babyinfo' ? 'text-orange-400' : 'text-slate-400'">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6.75 7.5l3 2.25-3 2.25m4.5 0h3m-9 8.25h13.5A2.25 2.25 0 0021 18V6a2.25 2.25 0 00-2.25-2.25H5.25A2.25 2.25 0 003 6v12a2.25 2.25 0 002.25 2.25z" />
            </svg>
            <p :class="page_type == 'babyinfo' ? 'text-orange-400' : 'text-slate-400'" class="text-xs text-center" >
                寶貝動態
            </p>
        </button>
        <button @click="onStatisticClick" class="w-6 h-6 col-start-3 col-span-2 row-start-1 row-span-4 place-self-center items-center">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" :class="page_type == 'statistic' ? 'text-orange-400' : 'text-slate-400'" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6.75 7.5l3 2.25-3 2.25m4.5 0h3m-9 8.25h13.5A2.25 2.25 0 0021 18V6a2.25 2.25 0 00-2.25-2.25H5.25A2.25 2.25 0 003 6v12a2.25 2.25 0 002.25 2.25z" />
            </svg>
            <p :class="page_type == 'statistic' ? 'text-orange-400' : 'text-slate-400'" class="text-center text-xs">
                統計
            </p>
        </button>

        <div class="absolute -top-3 w-12 h-12 col-start-5 col-span-2 row-start-1 row-span-6 place-self-center items-center">
            <button class="w-12 w-12 p-1 rounded-full bg-orange-400 justify-self-center shadow-2xl shadow-black">
                <svg xmlns="http://www.w3.org/2000/svg" fill="#ffffff" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-10 h-10 col-start-5 col-span-2 row-start-1 row-span-6 text-white justify-self-center">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
                </svg>
            </button>
        </div>



        <button @click="onKnowledgeClick" class="w-6 h-6 col-start-7 col-span-2 row-start-1 row-span-4 place-self-center items-center">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" :class="page_type == 'knowledge' ? 'text-orange-400' : 'text-slate-400'" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6.75 7.5l3 2.25-3 2.25m4.5 0h3m-9 8.25h13.5A2.25 2.25 0 0021 18V6a2.25 2.25 0 00-2.25-2.25H5.25A2.25 2.25 0 003 6v12a2.25 2.25 0 002.25 2.25z" />
            </svg>
            <div :class="page_type == 'knowledge' ? 'text-orange-400' : 'text-slate-400'" class="text-center text-xs">
                知識
            </div>
        </button>


        <button @click="onAccountClick" class="w-6 h-6 col-start-9 col-span-2 row-start-1 row-span-4 place-self-center items-center">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" :class="page_type == 'account' ? 'text-orange-400' : 'text-slate-400'" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6.75 7.5l3 2.25-3 2.25m4.5 0h3m-9 8.25h13.5A2.25 2.25 0 0021 18V6a2.25 2.25 0 00-2.25-2.25H5.25A2.25 2.25 0 003 6v12a2.25 2.25 0 002.25 2.25z" />
            </svg>
            <div  :class="page_type == 'account' ? 'text-orange-400' : 'text-slate-400'" class="text-center text-xs">
                帳戶
            </div>
        </button>
    </div>
    
    
    
</template>





<style scoped>





</style>