<script>
import capoo_slider_1 from '~/assets/knowledge/capoo_slider_1.jpg'
import capoo_slider_2 from '~/assets/knowledge/capoo_slider_2.jpg'
import capoo_slider_3 from '~/assets/knowledge/capoo_slider_3.jpg'
import capoo_slider_4 from '~/assets/knowledge/capoo_slider_4.jpg'
import capoo_slider_5 from '~/assets/knowledge/capoo_slider_5.jpg'

export default {
    props: ["idx"],
    created () {


        
    },
    data() {
        return { 
            capoo_slider_imgs: [
                capoo_slider_1,
                capoo_slider_2,
                capoo_slider_3,
                capoo_slider_4,
                capoo_slider_5
            ]
        }
    },
    methods: {

    }
}



</script>

<template>
    <!-- <div class="grid grid-cols-1 grid-rows-6 rounded-lg">
        <img :src="capoo_slider_imgs[idx]" class="rounded-lg col-span-1 row-span-3">
        <span class="col-span-1 row-start-4 row-span-1 text-lg font-bold font-sans">Caption {{ idx }}</span>
    </div> -->
    <div class="rounded-lg">
        <!-- <img :src="capoo_slider_imgs[idx-1]" class="rounded-lg"> -->
        
        <div class="rounded-lg h-28 w-full overflow-hidden">
            <img :src="capoo_slider_imgs[idx-1]" class="object-cover rounded-lg zoom_in h-full w-full" style="margin-bottom: 5px">
        </div>
        <text class="text-lg font-bold font-sans">Caption {{ idx-1 }}</text>
        
        
    </div>
</template>



<style scoped>

.zoom_in { 
    transition: all .2s ease-out; 
}
.zoom_in:hover { transform: scale(1.5); }
</style>