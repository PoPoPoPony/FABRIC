<script>
import mother_icon from '~/assets/babyinfo/mother@3x.png'
import baby_bottle_icon from '~/assets/babyinfo/baby_bottle@3x.png'
import bread_icon from '~/assets/babyinfo/bread@3x.png'
import happy_icon from '~/assets/babyinfo/happy@3x.png'
import heart_icon from '~/assets/babyinfo/heart@3x.png'
import poop_icon from '~/assets/babyinfo/poop@3x.png'
import sleep_icon from '~/assets/babyinfo/sleep@3x.png'
import water_icon from '~/assets/babyinfo/water@3x.png'


export default {
    props: [],
    created () {

    },
    computed() {

    },
    mounted() {

    },
    data() {
        return {
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
        

    }
}



</script>

<template>
    <div class="bg-no-repeat bg-cover w-full bg-neutral-100 rounded-3xl">
        <div class="grid grid-rows-6 grid-cols-4 mt-3 mx-3 justify-evenly">
            <button class="w-14 h-14 rounded-full bg-white col-start-1 col-span-1 row-start-1 row-span-4 place-self-center items-center">
                <img :src="mother_icon" class="object-contain p-3">
            </button>
            <div class="rounded-full col-start-1 text-slate-950 text-end col-span-1 row-start-5 row-span-2 justify-self-center">
                母乳
            </div>

            <button class="w-14 h-14 rounded-full bg-white col-start-2 col-span-1 row-start-1 row-span-4 place-self-center items-center">
                <img :src="baby_bottle_icon" class="object-contain p-3">
            </button>
            <div class="rounded-full col-start-2 text-slate-950 text-end col-span-1 row-start-5 row-span-2 justify-self-center">
                配方奶
            </div>

            <button class="w-14 h-14 rounded-full bg-white col-start-3 col-span-1 row-start-1 row-span-4 place-self-center items-center">
                <img :src="bread_icon" class="object-contain p-3">
            </button>
            <div class="rounded-full col-start-3 text-slate-950 text-end col-span-1 row-start-5 row-span-2 justify-self-center">
                點心
            </div>

            <button class="w-14 h-14 rounded-full bg-white col-start-4 col-span-1 row-start-1 row-span-4 place-self-center items-center">
                <img :src="sleep_icon" class="object-contain p-3">
            </button>
            <div class="rounded-full col-start-4 text-slate-950 text-end col-span-1 row-start-5 row-span-2 justify-self-center">
                睡覺
            </div>
        </div>
        
    </div>
</template>





<style scoped>





</style>