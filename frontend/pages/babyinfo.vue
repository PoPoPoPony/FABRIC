<script>
import capoo_1 from '~/assets/babyinfo/capoo_1.png'
import capoo_2 from '~/assets/babyinfo/capoo_2.png'
import capoo_3 from '~/assets/babyinfo/capoo_3.png'
import capoo_4 from '~/assets/babyinfo/capoo_4.png'
import capoo_5 from '~/assets/babyinfo/capoo_5.png'
import capoo_6 from '~/assets/babyinfo/capoo_6.png'
import baby_bottle_icon from '~/assets/babyinfo/baby_bottle@3x.png'
import mother_icon from '~/assets/babyinfo/mother@3x.png'
import bread_icon from '~/assets/babyinfo/bread@3x.png'
import happy_icon from '~/assets/babyinfo/happy@3x.png'
import heart_icon from '~/assets/babyinfo/heart@3x.png'
import poop_icon from '~/assets/babyinfo/poop@3x.png'
import sleep_icon from '~/assets/babyinfo/sleep@3x.png'
import water_icon from '~/assets/babyinfo/water@3x.png'
import { get_role } from '@/apis/user'
import { useUserStore } from '@/stores/user'


export default {
    props: [],
    created () {
        

        
    },
    mounted() {
        // const cookie_access_token = useCookie("access_token", {
        //     httpOnly: true,
        // })

        // console.log(cookie_access_token)

        // console.log(retv)




    },
    computed() {
    },
    data() {
        return { 
            page_type: "babyinfo",
            capoo_pic_lst: [
                capoo_1, capoo_2, capoo_3, capoo_4, capoo_5, capoo_6
            ],
            capoo_name_lst: [
                "capoo_1", "capoo_2", "capoo_3", "capoo_4", "capoo_5", "capoo_6"
            ],
            current_baby_idx: 0,
            baby_idx_keys: [
                0, 100, 200, 300, 400, 500
            ],
            mother_icon: mother_icon,
            baby_bottle_icon: baby_bottle_icon,
            bread_icon: bread_icon,
            happy_icon: happy_icon,
            heart_icon: heart_icon,
            poop_icon: poop_icon,
            sleep_icon: sleep_icon,
            water_icon: water_icon
        }
    },
    methods: {
        change_current_baby_idx (idx) {
            if (idx != this.current_baby_idx) {
                let past_idx = this.current_baby_idx
                this.current_baby_idx = idx
                this.baby_idx_keys[past_idx]+=1
                this.baby_idx_keys[idx]+=1
            }
        },
        temp () {
            // let t = getCookie("access_token")
            // console.log(t)
            get_role()
        },
    }
}

</script>



<template>
    <div class="relative bg-no-repeat bg-cover w-full h-screen bg-neutral-200">
        <!-- <button @click="temp">TEST</button> -->
        <div class="grid grid-cols-3 gap-1 pt-10">
            <p class="col-start-2 col-span-1 text-center text-lg font-sans font-bold">寶貝動態</p>
            <div class="col-start-3 col-span-1 justify-self-end mr-4">
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
        <div class="flex scroll-smooth overflow-x-scroll w-full mt-8 px-3 justify-start gap-x-3 null_scroll_bar mb-3">
            <!-- key 只是先暫時讓每個key間隔很遠(更新時+1才不會重複)，需找到比較好的方法更新 -->
            <babyinfo-button-with-pic v-for="i in 6" :label_idx="i-1" :current_idx="current_baby_idx" :key="baby_idx_keys[i-1]" :img_src="capoo_pic_lst[i-1]" :name="capoo_name_lst[i-1]" @change_current_idx="change_current_baby_idx"/>
        </div>
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
                <div class="bg-no-repeat bg-cover w-full bg-neutral-100 rounded-3xl py-3 mt-3 col-span-2">
                    <div class="grid grid-rows-2 grid-cols-4 mt-3 mx-3 justify-evenly gap-4">
                        <babyinfo-record-panel-item class="col-start-1 col-span-1 row-start-1 row-span-1" :img_src="mother_icon" label="母乳"/>
                        <babyinfo-record-panel-item class="col-start-2 col-span-1 row-start-1 row-span-1" :img_src="baby_bottle_icon" label="配方奶"/>
                        <babyinfo-record-panel-item class="col-start-3 col-span-1 row-start-1 row-span-1" :img_src="bread_icon" label="點心"/>
                        <babyinfo-record-panel-item class="col-start-4 col-span-1 row-start-1 row-span-1" :img_src="sleep_icon" label="睡覺"/>
                        <babyinfo-record-panel-item class="col-start-1 col-span-1 row-start-2 row-span-1" :img_src="water_icon" label="尿尿"/>
                        <babyinfo-record-panel-item class="col-start-2 col-span-1 row-start-2 row-span-1" :img_src="poop_icon" label="便便"/>
                        <babyinfo-record-panel-item class="col-start-3 col-span-1 row-start-2 row-span-1" :img_src="happy_icon" label="散步"/>
                        <babyinfo-record-panel-item class="col-start-4 col-span-1 row-start-2 row-span-1" :img_src="heart_icon" label="擠奶"/>
                    </div>
                </div>
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