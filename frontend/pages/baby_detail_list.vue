<script>
// import capoo_1 from '~/assets/babyinfo/capoo_1.png'
// import capoo_2 from '~/assets/babyinfo/capoo_2.png'
// import capoo_3 from '~/assets/babyinfo/capoo_3.png'
// import capoo_4 from '~/assets/babyinfo/capoo_4.png'
// import capoo_5 from '~/assets/babyinfo/capoo_5.png'
// import capoo_6 from '~/assets/babyinfo/capoo_6.png'
// import mother_icon from '~/assets/babyinfo/mother@3x.png'
// import water_icon from '~/assets/babyinfo/water@3x.png'
// import poop_icon from '~/assets/babyinfo/poop@3x.png'
// import sleep_icon from '~/assets/babyinfo/sleep@3x.png'
import { ElLoading } from 'element-plus'
import { APIGetUserBabys } from '@/apis/user'
import { useBabyStore } from "@/stores/baby"


export default {
    props: [],
    created() {
    },
    mounted() {
        this.loading = ElLoading.service({
            lock: true,
            text: 'Loading',
            background: 'rgba(0, 0, 0, 0.7)',
        })
        this.fetching_user_babys()
        this.cells_key+=1
    },
    computed() {
        
    },
    data() {
        return {
            loading: '',
            baby_infos: [],
            cells_key: 1000
        }
    },
    methods: {
        create_baby_click() {
            navigateTo({
                path: "/create_baby",
                query: {
                    "idx": -1
                }
            })
        },
        async fetching_user_babys() {
            let babyStore = useBabyStore()
            babyStore.clear_all_babys()

            let retv = await APIGetUserBabys()

            if (retv['status_code'] == 200) {
                // this.baby_infos = retv['data']
                // console.log(retv['data'])
                for (let baby_info of retv['data']) {
                    babyStore.add_baby_id(baby_info['baby_id'])
                    babyStore.add_baby_avatar(baby_info['baby_avatar'])
                    babyStore.add_baby_name(baby_info['baby_name'])
                    this.baby_infos.push(baby_info)
                }
            } else {
                ElMessage({
                    message: retv['message'],
                    type: 'error',
                })
            }





            

            // only store baby_id, baby_avatr, baby_name in the pinia
            this.loading.close()
        }
    }
}

</script>



<template>
    <div class="bg-no-repeat bg-cover w-full h-screen bg-neutral-200">
        <div class="bg-neutral-50 top-0 h-20">
            <div class="grid grid-cols-3 gap-1 pt-10">
                <div class="col-start-1 col-span-1 ml-4 justify-self-start text-orange-400 font-bold">
                    <button>
                        <svg xmlns="http://www.w3.org/2000/svg" style="display: inline;" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 place-self-center">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 19.5L8.25 12l7.5-7.5" />
                        </svg>
                        <span>返回</span>
                    </button>
                </div>
                <p class="col-start-2 col-span-1 text-center text-lg font-sans font-bold">寶貝</p>
                <button class="justify-self-end" @click="create_baby_click">
                    <div class="col-start-3 col-span-1 mr-4 justify-self-end text-orange-400 font-bold">
                        新增寶貝
                    </div>
                </button>
            </div>
        </div>
        <div class="bg-white rounded-xl mt-8 mx-8 px-3" :key="cells_key">
            <!-- "baby_id", "baby_name", "baby_avatar", "baby_birth", "baby_sex", "baby_diseases" -->
            <baby-detail-list-baby-info-cell v-for="(baby_info, idx) in baby_infos" :key="idx" :idx="idx"
                :baby_id="baby_info['baby_id']" :baby_name="baby_info['baby_name']" :baby_avatar="baby_info['baby_avatar']" :baby_birth="baby_info['baby_birth']" :baby_sex="baby_info['baby_sex']" :baby_diseases="baby_info['baby_diseases']"
            >

            </baby-detail-list-baby-info-cell>
        </div>


        <!-- <div class="fixed bottom-0 pt-2 w-full h-12 bg-neutral-50">
            <footer_banner :page_type="page_type" class="" />
        </div> -->
    </div>
</template>


<style lang="scss" scoped>
.null_scroll_bar::-webkit-scrollbar {
    display: none;
}
</style>