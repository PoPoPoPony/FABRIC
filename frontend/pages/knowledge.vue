<script>

export default {
    props: [],
    created () {


        
    },
    mounted() {
        this.$nextTick(() => {
            this.swiper_show = true
        })
    },
    data() {
        return {
            page_type: "knowledge",
            swiper_show: false,
            titles: ["珍藏", "產後護理", "心情調適", "育兒心得", "夫妻溝通"],
            few_news: ["news1", "news2", "news3"]
        }

    },
    methods: {

    }

}

</script>



<template>
    <div class="bg-no-repeat bg-cover w-full h-screen bg-neutral-200">
        <!-- absolute inset-x-0  -->
        <div class=" bg-neutral-50 grid grid-cols-1 grid-rows-10">
            <p class="text-center text-lg font-bold font-sans pt-10 row-start-1 row-span-2  col-start-1 col-span-1">知識</p> 
            <div class="text-start text-lg font-bold font-sans mx-5 mt-3 row-start-3 row-span-1 col-start-1 col-span-1">
                <span class="text-slate-800">為</span>
                <span class="text-orange-400">品軒</span>
                <span class="text-slate-800">推薦</span>
            </div>
            <div class="mx-5 mt-3 rounded-lg row-start-4 row-span-5 col-start-1 col-span-1">
                <Swiper
                    :modules="[SwiperPagination, SwiperEffectCreative]"
                    :slides-per-view="1"
                    :pagination="{
                        el: $refs.pagination_container,
                        clickable: true
                    }"
                    :loop="true"
                    :effect="'creative'"
                    
                    :creative-effect="{
                        prev: {
                            shadow: false,
                            translate: ['-30%', 0, -1],
                        },
                        next: {
                            translate: ['100%', 0, 0],
                        },
                    }"
                    class="rounded-lg swiper-container"
                    v-if="swiper_show"
                > 
            
                    <SwiperSlide class="rounded-lg swiper-slide" v-for="slide in 5" :key="slide">
                        <knowledge-slider-with-caption class="rounded-lg" :idx="slide" />
                    </SwiperSlide>
                </Swiper>
                <div id="swiper-pagination-container" class="text-center -mt-2" ref="pagination_container">
                    <!-- The swiper-pagination will be appended here -->
                </div>
            </div>
        </div>
        <!-- grid grid-cols-1 grid-rows-10 -->
        <div class="mt-2 no-repeat w-full bg-cover bg-neutral-50 ">
            <div class="px-3 flex scroll-smooth w-full h-12 py-2 overflow-x-scroll justify-start gap-x-3 null_scroll_bar"> 
                <knowledge-title-btn v-for="idx in titles.length" :title="titles[idx-1]" :key="idx"></knowledge-title-btn>
            </div>
            <div class="px-3 w-full h-full overflow-y-hidden grid grid-cols-1 divide-y"> 
                <knowledge-news v-for="idx in few_news.length" :key="idx"></knowledge-news>
            </div>
        </div>
        <div class="absolute inset-x-0 bottom-0 h-12 bg-neutral-50" >
            <footer_banner :page_type="page_type" class=""></footer_banner>
        </div>
    </div>
</template>


<style scoped>
.swiper-container {
    height: 9rem; 
}

/* If you want to make the swiper slides fill the height of the container */
.swiper-slide {
  height: 100%; /* This will make the slides fill the container height */
  /* Add any other styles you need for the slides */
}

.null_scroll_bar::-webkit-scrollbar {
    display: none;
}

</style>