<script>
export default {
    props: [],
    created () {


        
    },
    mounted() {

    },
    data() {
        return {
            page_type: "knowledge",
        }
    },
    methods: {

    }

}

</script>



<template>
    <div class="bg-no-repeat bg-cover w-full h-screen bg-neutral-200">
        <div class="absolute inset-x-0 top-0 h-60 bg-neutral-50">
            <p class="text-center text-lg font-bold font-sans pt-10">知識</p>
            <div class="text-start text-lg font-bold font-sans mx-5 mt-3">
                <span class="text-slate-800">為</span>
                <span class="text-orange-400">品軒</span>
                <span class="text-slate-800">推薦</span>
            </div>
            <div class="mx-5 mt-3">
                <Swiper
                    :modules="[SwiperPagination, SwiperEffectCreative]"
                    :slides-per-view="1"
                    :pagination="true"
                    :loop="false"
                    :effect="'creative'"
                    :autoplay="{
                    delay: 8000,
                    disableOnInteraction: true,
                    }"
                    :creative-effect="{
                        prev: {
                            shadow: false,
                            translate: ['-20%', 0, -1],
                        },
                        next: {
                            translate: ['100%', 0, 0],
                        },
                    }"
                > 
            
                <SwiperSlide>
                    <div style="background-color: red;"></div>
                </SwiperSlide>
                <SwiperSlide>
                    <div style="background-color: green;"></div>
                </SwiperSlide>
                <SwiperSlide>
                    <div style="background-color: blue;"></div>
                </SwiperSlide>
                <SwiperSlide>
                    <div style="background-color: yellow;"></div>
                </SwiperSlide>

            
                </Swiper>



            </div>





            
        </div>
        
















        <div class="absolute inset-x-0 bottom-0 h-12 bg-neutral-50" >
            <footer_banner :page_type="page_type" class=""></footer_banner>
        </div>
    </div>
</template>


<style scoped>

</style>