<script>
import capoo_1 from '~/assets/babyinfo/capoo_1.png'
import capoo_2 from '~/assets/babyinfo/capoo_2.png'
import capoo_3 from '~/assets/babyinfo/capoo_3.png'
import capoo_4 from '~/assets/babyinfo/capoo_4.png'
import capoo_5 from '~/assets/babyinfo/capoo_5.png'
import capoo_6 from '~/assets/babyinfo/capoo_6.png'
import mother_icon from '~/assets/babyinfo/mother@3x.png'
import water_icon from '~/assets/babyinfo/water@3x.png'
import poop_icon from '~/assets/babyinfo/poop@3x.png'
import sleep_icon from '~/assets/babyinfo/sleep@3x.png'


export default {
    props: [],
    created () {


        
    },
    mounted() {
        this.date_swiper_show = true
        this.max_time = Math.max(...this.event_report_infos.map((x)=>x.time))
        this.event_report_banner_show = true
    },
    computed () {
        
    },
    data() {
        return {
            page_type: "statistic",
            time_freqs: ["日", "週", "月", "年"],
            current_time_freq: "日",
            time_freq_keys: {
                "日": 1,
                "週": 100,
                "月": 200,
                "年": 300,
            },
            date_labels: [
                "2023年6月1日",
                "2023年6月2日",
                "2023年6月3日",
                "2023年6月4日",
                "2023年6月5日",
                "2023年6月6日",
                "2023年6月7日",
                "2023年6月8日",
                "2023年6月9日",
                "2023年6月10日",
                "2023年6月11日",
            ],
            date_swiper_show: false,

            // 寶貝
            capoo_pic_lst: [
                capoo_1, capoo_2, capoo_3, capoo_4, capoo_5, capoo_6
            ],
            capoo_name_lst: [
                "capoo_1", "capoo_2", "capoo_3", "capoo_4", "capoo_5", "capoo_6"
            ],
            current_baby_idx: 0,
            baby_idx_keys: [
                400, 500, 600, 700, 800, 900
            ],
            
            // 活動摘要
            event_report_infos: [{
                icon: water_icon,
                label: "尿尿",
                time: 15
            }, {
                icon: mother_icon,
                label: "母乳",
                time: 4
            }, {
                icon: poop_icon,
                label: "便便",
                time: 6
            }, {
                icon: sleep_icon,
                label: "睡覺",
                time: 4
            }],
            max_time: 0,
            event_report_banner_show: false,

            // 排泄狀況
            poop_colors: ["#F26262", "#FFA843", "#FFCC4A", "#AFE867", "#5FD680"],
            user_poop_idx: 2,
            poop_label: ["非常慘", "慘", "普通", "正常", "很棒"]
        }
    },
    methods: {
        time_freq_change(time_freq) {
            if (time_freq != this.current_time_freq) {
                let past_time_freq = this.current_time_freq
                this.current_time_freq = time_freq
                this.time_freq_keys[past_time_freq]+=1
                this.time_freq_keys[time_freq]+=1
            }
        },
        change_current_baby_idx (idx) {
            if (idx != this.current_baby_idx) {
                let past_idx = this.current_baby_idx
                this.current_baby_idx = idx
                this.baby_idx_keys[past_idx]+=1
                this.baby_idx_keys[idx]+=1
            }
        },
    }
}

</script>



<template>
    <div class="bg-no-repeat bg-cover w-full h-screen bg-neutral-200">
        <div class="bg-neutral-50 absolute inset-x-0 top-0 h-44">
            <div class="grid grid-cols-8 gap-1 pt-10">
                <p class="col-start-2 col-span-8 text-center text-lg font-sans font-bold">統計</p>
                <div class="col-start-10 col-span-1 justify-self-end pr-3 text-orange-400 font-bold">
                    今日
                </div>
            </div>
            <div class="mx-4 mt-4">
                <div class="divide-x divide-neutral-400 w-full h-8 grid grid-cols-4 rounded-md bg-neutral-200">
                    <statistic-time-freq-btn class="col-span-1" v-for="time_freq in time_freqs" :time_freq="time_freq" :current_time_freq="current_time_freq" :key="time_freq_keys[time_freq]" @time_freq_change="time_freq_change" />
                </div>
            </div>
            <div class="grid grid-cols-10">
                <div class="col-start-1 col-span-2 relative">
                    <button ref="navigation_prev" class="absolute inset-x-6 bottom-0">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-6 h-6 text-orange-400">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 19.5L8.25 12l7.5-7.5" />
                        </svg>
                    </button>
                </div>
                <div class="col-start-3 col-span-6">
                    <Swiper
                    :modules="[SwiperNavigation, SwiperEffectCreative]"
                    :slides-per-view="1"
                    :loop="true"
                    :effect="'creative'"
                    :navigation="{
                        prevEl: $refs.navigation_prev,
                        nextEl: $refs.navigation_next
                    }"
                    :creative-effect="{
                        prev: {
                            shadow: false,
                            translate: ['-100%', 0, -1],
                        },
                        next: {
                            translate: ['100%', 0, 0],
                        },
                    }"
                    class="mt-5 place-self-center"
                    v-if="date_swiper_show"
                    >
                        <SwiperSlide class="text-center swiper-slide font-bold" v-for="date_label of date_labels" :key="date_label">
                            {{ date_label }}
                        </SwiperSlide>
                    </Swiper>
                </div>
                <div class="col-start-9 col-span-2 relative">
                    <button ref="navigation_next" class="absolute bottom-0 right-6">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-6 h-6 text-orange-400">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
                        </svg>
                    </button>
                </div>
            </div>
            <div class="flex scroll-smooth overflow-x-scroll w-full mt-8 px-3 justify-start gap-x-3 null_scroll_bar">
                <babyinfo-button-with-pic v-for="i in 6" :label_idx="i-1" :current_idx="current_baby_idx" :key="baby_idx_keys[i-1]" :img_src="capoo_pic_lst[i-1]" :name="capoo_name_lst[i-1]" @change_current_idx="change_current_baby_idx"/>
            </div>
            <div class="my-6 mx-4">
                <p class="text-start text-xl font-bold font-sans ">活動摘要</p>
                <div v-if="event_report_banner_show" class="rounded-lg bg-neutral-50 w-full px-4 py-2">
                    <statistic-event-report-banner v-for="i in 4" :icon="event_report_infos[i-1].icon" :label="event_report_infos[i-1].label" :time="event_report_infos[i-1].time " :max_time="max_time"/>
                </div>
            </div>
            <div class="my-8 mx-4">
                <p class="text-start text-xl font-bold font-sans ">排泄狀況</p>
                <div class="rounded-lg bg-neutral-50 w-full px-4 py-2">
                    <div class="grid grid-cols-5 gap-0.5 mt-10 mb-5">
                        <statistic-p-bar-diff-color-rounded class="col-span-1" v-for="i in user_poop_idx+1" :color="poop_colors[i-1]" :index="i-1" :user_poop_index="user_poop_idx"/>
                    </div>
                    <div class="font-bold text-2xl text-center" :style="{'color': poop_colors[user_poop_idx]}">
                        {{ poop_label[user_poop_idx] }}
                    </div>
                    <div class="font-bold text-xs text-center mt-2">
                        依據您的寶貝排泄狀況與我們<br>的匿名資料庫比對結果
                    </div>
                </div>
            </div>
        </div>
        











        <div class="fixed bottom-0 pt-2 w-full h-12 bg-neutral-50">
            <footer_banner :page_type="page_type" class=""/>
        </div>
    </div>
</template>


<style lang="scss" scoped>
.null_scroll_bar::-webkit-scrollbar {
    display: none;
}


</style>