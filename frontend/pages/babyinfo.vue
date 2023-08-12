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
    <div class="relative bg-no-repeat bg-cover w-full h-screen bg-neutral-200">
        <div class="grid grid-cols-8 gap-1 pt-10">
            <p class="col-start-2 col-span-8 text-center text-lg font-sans font-bold">寶貝動態</p>
            <div class="col-start-10 col-span-1 justify-self-end pr-3">
                <svg xmlns="http://www.w3.org/2000/svg" fill="000000" viewBox="0 0 24 24" stroke-width="0" stroke="currentColor" class="w-7 h-7">
                    <g clip-path="url(#clip0_78_990)">
                    <path d="M12.0002 2C11.289 2 10.7145 2.55859 10.7145 3.25V4C7.78146 4.57812 5.57164 7.10156 5.57164 10.125V10.8594C5.57164 12.6953 4.87655 14.4688 3.62298 15.8438L3.32565 16.168C2.98815 16.5352 2.9078 17.0625 3.11271 17.5117C3.31762 17.9609 3.77967 18.25 4.28592 18.25H19.7145C20.2207 18.25 20.6788 17.9609 20.8877 17.5117C21.0966 17.0625 21.0123 16.5352 20.6748 16.168L20.3774 15.8438C19.1239 14.4688 18.4288 12.6992 18.4288 10.8594V10.125C18.4288 7.10156 16.219 4.57812 13.2859 4V3.25C13.2859 2.55859 12.7114 2 12.0002 2ZM13.8203 21.2695C14.3024 20.8008 14.5716 20.1641 14.5716 19.5H12.0002H9.42878C9.42878 20.1641 9.69798 20.8008 10.1801 21.2695C10.6623 21.7383 11.3172 22 12.0002 22C12.6832 22 13.3382 21.7383 13.8203 21.2695Z" fill="black"/>
                    </g>
                    <defs>
                    <clipPath id="clip0_78_990">
                    <rect width="18" height="20" fill="white" transform="translate(3 2)"/>
                    </clipPath>
                    </defs>
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
        <div>
            <el-scrollbar :always="true" id="scroll_bar" class="justify-evenly ">
                <div class="scrollbar-flex-content mt-5">
                    <babyinfo-clock class="px-7" message="距離下次更換尿布"/>
                    <babyinfo-clock class="px-7" message="距離下次起床"/>
                    <babyinfo-clock class="px-7" message="距離下次餵奶"/>
                    <babyinfo-clock class="px-7" message="距離下次睡覺"/>
                    <babyinfo-clock class="px-7" message="距離下次散步"/>
                </div>
            </el-scrollbar>
        </div>



        <div class=" pt-2 w-full h-96  bg-neutral-50 rounded-t-3xl drop-shadow-2xl" >
            <div class="grid grid-cols-2 mt-6 mx-5 items-end">
                <span class="font-bold col-start-1 col-span-1 text-xl">快速紀錄</span>
                <span class="font-bold col-start-2 col-span-1 text-sm text-end text-orange-500">編輯</span>
                <babyinfo-record-panel class="py-3 mt-3 col-span-2"/>
                <babyinfo-record-panel class="py-3 mt-3 col-span-2"/>

            </div>
            
        </div>
        <div class="fixed bottom-0 pt-2 w-full h-12 bg-neutral-50" >
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