<script>
export default {
    props: [],
    created () {


        
    },
    mounted() {
        this.date_swiper_show = true
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
            date_swiper_show: false
        }
    },
    methods: {
        time_freq_change(time_freq) {
            let past_time_freq = this.current_time_freq
            this.current_time_freq = time_freq
            this.time_freq_keys[past_time_freq]+=1
            this.time_freq_keys[time_freq]+=1
        }
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
            <!-- :navigation="{
                        prevEl: $refs.navigation_prev,
                        nextEl: $refs.navigation_next
                    }" -->
            <div class="grid grid-cols-10">
                <div class="col-start-1 col-span-2 place-self-center">
                    <button ref="navigation_prev">123</button>
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
                <div class="col-start-9 col-span-2 place-self-center">
                    <button ref="navigation_next">456</button>
                </div>
                
                
            </div>
        </div>
        











        <div class="fixed bottom-0 pt-2 w-full h-12 bg-neutral-50">
            <footer_banner :page_type="page_type" class=""/>
        </div>
    </div>
</template>


<style lang="scss" scoped>
// .swiper-button-prev::after {
//     color: orange
// }

// .swiper::part(button-prev) {
//     color: orange;
// }

// .swiper-button-next::after {
//     color: orange
// }

.swiper>.swiper-button-next::after {
    color: red;
}

</style>