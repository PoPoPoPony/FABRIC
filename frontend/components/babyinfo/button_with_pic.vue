<script>
import capoo_1 from '~/assets/babyinfo/capoo_1.png'
import capoo_2 from '~/assets/babyinfo/capoo_2.png'
import capoo_3 from '~/assets/babyinfo/capoo_3.png'
import capoo_4 from '~/assets/babyinfo/capoo_4.png'
import capoo_5 from '~/assets/babyinfo/capoo_5.png'
import capoo_6 from '~/assets/babyinfo/capoo_6.png'

export default {
    props: ["name"],
    created () {


        
    },
    data() {
        // width="48" height="48"
        return { 
            capoo_pic_lst: [
                capoo_1, capoo_2, capoo_3, capoo_4, capoo_5, capoo_6
            ],
            capoo_name_lst: [
                "capoo_1", "capoo_2", "capoo_3", "capoo_4", "capoo_5", "capoo_6"
            ]
        }
    },
    methods: {

    }
}



</script>

<template>
    <button class="rounded-full bg-zinc-200 px-5 py-1 self-center mb-5">
        <div class="flex items-center justify-center ">
            <img :src="capoo_pic_lst[name]" class="object-contain h-8 w-12 rounded-full">
            <span class="mr-2">{{capoo_name_lst[name]}}</span>
        </div>
    </button>
</template>