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
        return {
            
        }
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
                <g clip-path="url(#clip0_78_994)">
                <path d="M6.75 2C4.67969 2 3 3.67969 3 5.75V18.25C3 20.3203 4.67969 22 6.75 22H18H19.25C19.9414 22 20.5 21.4414 20.5 20.75C20.5 20.0586 19.9414 19.5 19.25 19.5V17C19.9414 17 20.5 16.4414 20.5 15.75V3.25C20.5 2.55859 19.9414 2 19.25 2H18H6.75ZM6.75 17H16.75V19.5H6.75C6.05859 19.5 5.5 18.9414 5.5 18.25C5.5 17.5586 6.05859 17 6.75 17ZM8 7.625C8 7.28125 8.28125 7 8.625 7H16.125C16.4688 7 16.75 7.28125 16.75 7.625C16.75 7.96875 16.4688 8.25 16.125 8.25H8.625C8.28125 8.25 8 7.96875 8 7.625ZM8.625 9.5H16.125C16.4688 9.5 16.75 9.78125 16.75 10.125C16.75 10.4688 16.4688 10.75 16.125 10.75H8.625C8.28125 10.75 8 10.4688 8 10.125C8 9.78125 8.28125 9.5 8.625 9.5Z" :fill="page_type == 'babyinfo' ? 'text-orange-400' : 'text-slate-400'"/>
                </g>
            </svg>
            <p :class="page_type == 'babyinfo' ? 'text-orange-400' : 'text-slate-400'" class="text-xs text-center" >
                寶貝動態
            </p>
        </button>
        <button @click="onStatisticClick" class="w-6 h-6 col-start-3 col-span-2 row-start-1 row-span-4 place-self-center items-center">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" :class="page_type == 'statistic' ? 'text-orange-400' : 'text-slate-400'" class="w-6 h-6">
                <path d="M4.5 4.5C4.5 3.80859 3.94141 3.25 3.25 3.25C2.55859 3.25 2 3.80859 2 4.5V17.625C2 19.3516 3.39844 20.75 5.125 20.75H20.75C21.4414 20.75 22 20.1914 22 19.5C22 18.8086 21.4414 18.25 20.75 18.25H5.125C4.78125 18.25 4.5 17.9688 4.5 17.625V4.5ZM20.3828 7.88281C20.8711 7.39453 20.8711 6.60156 20.3828 6.11328C19.8945 5.625 19.1016 5.625 18.6133 6.11328L14.5 10.2305L12.2578 7.98828C11.7695 7.5 10.9766 7.5 10.4883 7.98828L6.11328 12.3633C5.625 12.8516 5.625 13.6445 6.11328 14.1328C6.60156 14.6211 7.39453 14.6211 7.88281 14.1328L11.375 10.6445L13.6172 12.8867C14.1055 13.375 14.8984 13.375 15.3867 12.8867L20.3867 7.88672L20.3828 7.88281Z" :fill="page_type == 'statistic' ? 'text-orange-400' : 'text-slate-400'"/>
            </svg>
            <p :class="page_type == 'statistic' ? 'text-orange-400' : 'text-slate-400'" class="text-center text-xs">
                統計
            </p>
        </button>

        <div class="absolute -top-5 w-12 h-12 col-start-5 col-span-2 row-start-1 row-span-6 place-self-center items-center">
            <button class="w-12 p-1 rounded-full bg-orange-400 justify-self-center shadow-2xl shadow-black">
                <svg xmlns="http://www.w3.org/2000/svg" fill="#ffffff" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-10 h-10 col-start-5 col-span-2 row-start-1 row-span-6 text-white justify-self-center">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
                </svg>
            </button>
        </div>



        <button @click="onKnowledgeClick" class="w-6 h-6 col-start-7 col-span-2 row-start-1 row-span-4 place-self-center items-center">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" :class="page_type == 'knowledge' ? 'text-orange-400' : 'text-slate-400'" class="w-6 h-6">
                <g clip-path="url(#clip0_78_992)">
                <path d="M22.0002 11.375C22.0002 15.8633 17.5236 19.5 12.0002 19.5C10.551 19.5 9.17596 19.25 7.93377 18.8008C7.46893 19.1406 6.71112 19.6055 5.81268 19.9961C4.87518 20.4023 3.74628 20.75 2.62518 20.75C2.37128 20.75 2.14471 20.5977 2.04706 20.3633C1.9494 20.1289 2.00409 19.8633 2.17987 19.6836L2.19159 19.6719C2.20331 19.6602 2.21893 19.6445 2.24237 19.6172C2.28534 19.5703 2.35174 19.4961 2.43378 19.3945C2.59393 19.1992 2.80878 18.9102 3.02753 18.5508C3.41815 17.9023 3.78924 17.0508 3.86346 16.0938C2.69159 14.7656 2.00018 13.1367 2.00018 11.375C2.00018 6.88672 6.47674 3.25 12.0002 3.25C17.5236 3.25 22.0002 6.88672 22.0002 11.375Z" :fill="page_type == 'knowledge' ? 'text-orange-400' : 'text-slate-400'"/>
                </g>
            </svg>
            <div :class="page_type == 'knowledge' ? 'text-orange-400' : 'text-slate-400'" class="text-center text-xs">
                知識
            </div>
        </button>


        <button @click="onAccountClick" class="w-6 h-6 col-start-9 col-span-2 row-start-1 row-span-4 place-self-center items-center">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" :class="page_type == 'account' ? 'text-orange-400' : 'text-slate-400'" class="w-6 h-6">
                <g clip-path="url(#clip0_78_991)">
                <path d="M11.75 12C13.0761 12 14.3479 11.4732 15.2855 10.5355C16.2232 9.59785 16.75 8.32608 16.75 7C16.75 5.67392 16.2232 4.40215 15.2855 3.46447C14.3479 2.52678 13.0761 2 11.75 2C10.4239 2 9.15215 2.52678 8.21447 3.46447C7.27678 4.40215 6.75 5.67392 6.75 7C6.75 8.32608 7.27678 9.59785 8.21447 10.5355C9.15215 11.4732 10.4239 12 11.75 12ZM9.96484 13.875C6.11719 13.875 3 16.9922 3 20.8398C3 21.4805 3.51953 22 4.16016 22H19.3398C19.9805 22 20.5 21.4805 20.5 20.8398C20.5 16.9922 17.3828 13.875 13.5352 13.875H9.96484Z" :fill="page_type == 'account' ? 'text-orange-400' : 'text-slate-400'"/>
                </g>
            </svg>
            <div  :class="page_type == 'account' ? 'text-orange-400' : 'text-slate-400'" class="text-center text-xs">
                帳戶
            </div>
        </button>
    </div>
    
    
    
</template>





<style scoped>





</style>