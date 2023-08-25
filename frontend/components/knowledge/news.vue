<template>
    <div class="grid grid-cols-5 grid-rows-1 h-32">
        <div class="col-span-3 col-start-1 rol-span-1 grid grid-rows-2 py-2"> <!-- title and content container -->
            <div class="row-start-1 overflow-hidden text-sm font-bold text-black"> {{ news_title }}</div>
            <div class="text-ellipsis overflow-hidden row-start-2 overflow-hidden -mt-1 text-xs text-neutral-400"> {{ news_content }}</div>
        </div>
        <div class="col-span-2 col-start-4 rol-span-1 py-5 px-3">
            <img :src="capoo_slider_1" class="rounded-lg place-self-center"/>
        </div>
    </div>
</template>
<script>

import capoo_slider_1 from '~/assets/knowledge/capoo_slider_1.jpg'


export default {
    
    data() {
        return {
            news_title: "產後照護指南：幫助新媽媽重建身心靈健康的寶貴建議",
            news_content: "提供給新媽媽們一個全面的產後照護指南。從身體的恢復到心理的調適，我們將分享寶貴的建議，幫助您重建身心靈健康，並享受寶貴的媽媽時光。",
            capoo_slider_1: capoo_slider_1,

        }
    },
}
</script>
<style lang="scss">
    
</style>