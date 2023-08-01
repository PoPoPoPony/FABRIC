<script>
export default {
    props: [],
    created () {


        
    },
    mounted() {
        this.$nextTick(() => {
            this.key+=1
        })
        
    },
    data() {
        // width="48" height="48"
        return { 
            key:0,
            page_type: "babyinfo",
        }
    },
    methods: {
        on_clock_change(scope) {
            console.log(scope.$index)
        }
    }
}

</script>



<template>
    <div class="bg-no-repeat bg-cover w-full h-screen bg-neutral-200">
        <div class="grid grid-cols-8 gap-1 pt-10">
            <p class="col-start-2 col-span-8 text-center text-lg font-sans font-bold">寶貝動態</p>
            <div class="col-start-10 col-span-1 justify-self-end pr-3">
                <svg xmlns="http://www.w3.org/2000/svg" fill="000000" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-7 h-7">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M14.857 17.082a23.848 23.848 0 005.454-1.31A8.967 8.967 0 0118 9.75v-.7V9A6 6 0 006 9v.75a8.967 8.967 0 01-2.312 6.022c1.733.64 3.56 1.085 5.455 1.31m5.714 0a24.255 24.255 0 01-5.714 0m5.714 0a3 3 0 11-5.714 0" />
                </svg>
            </div>
        </div>
        <div class="flex scroll-smooth overflow-x-scroll w-full mt-8 px-3 justify-start gap-x-3 null_scroll_bar">
            <babyinfo-button-with-pic v-for="i in 6" :name="i-1"/>
        </div>
        

        <!-- <div class="px-3">
            <ul class="snap-x flex  overflow-x-scroll justify-start mt-5 w-full mr-auto scroll_bar_padding" :key="key">
                <li class="snap-center" >
                    <babyinfo-clock message="距離下次更換尿布"/>
                </li>
                <li class="snap-center">
                    <babyinfo-clock message="距離下次起床"/>
                </li>
                <li class="snap-center">
                    <babyinfo-clock message="距離下次餵奶"/>
                </li>
                <li class="snap-center">
                    <babyinfo-clock message="距離下次睡覺"/>
                </li>
                <li class="snap-center">
                    <babyinfo-clock message="距離下次散步"/>
                </li>
            </ul> -->
            <!-- <div class="rounded ..."></div> -->
        <!-- </div> -->

        <!-- class="px-3"  -->
        <el-scrollbar :always="true" id="scroll_bar" class="justify-evenly ">
            <div class="scrollbar-flex-content mt-5">
                <babyinfo-clock class="px-7" message="距離下次更換尿布"/>
                <babyinfo-clock class="px-7" message="距離下次起床"/>
                <babyinfo-clock class="px-7" message="距離下次餵奶"/>
                <babyinfo-clock class="px-7" message="距離下次睡覺"/>
                <babyinfo-clock class="px-7" message="距離下次散步"/>
            </div>
        </el-scrollbar>
        <div class="absolute inset-x-0 bottom-0 h-60 bg-neutral-50 rounded-t-3xl drop-shadow-2xl" >
            <div class="grid grid-cols-2 mt-6 mx-5 items-end">
                <span class="font-bold col-start-1 col-span-1 text-xl">快速紀錄</span>
                <span class="font-bold col-start-2 col-span-1 text-sm text-end text-orange-500">編輯</span>
                <babyinfo-record-panel class="py-3 mt-3 col-span-2"/>
            </div>
            
        </div>
        <div class="absolute inset-x-0 bottom-0 h-12" >
            <footer_banner :page_type="page_type" class=""></footer_banner>
        </div>
    </div>
</template>


<style scoped>
.null_scroll_bar::-webkit-scrollbar {
    display: none;
}

.scroll_bar_padding::-webkit-scrollbar {
    top: 20px;
}


.scrollbar-flex-content {
    display: flex;
}

.el-scrollbar {
    height: auto;
}
:deep(#scroll_bar>.el-scrollbar__bar) {
    position: relative;
    margin-top: 10px;
}



#scroll_bar::-webkit-scrollbar-track {
    margin-top: 10px;
}





/* .scrollbar-demo-item {
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100px;
    height: 50px;
    margin: 10px;
    text-align: center;
    border-radius: 4px;
    background: var(--el-color-danger-light-9);
    color: var(--el-color-danger);
} */

/* .el-carousel__item h3 {
    color: #475669;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
    text-align: center;
}

.el-carousel__item:nth-child(2n) {
    background-color: transparent;
}
.el-carousel__item:nth-child(2n+1) {
    background-color: transparent;
} */
</style>