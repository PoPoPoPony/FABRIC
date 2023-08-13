<script>


export default {
    props: ["icon", "label", "time", "max_time"],
    created () {

    },
    computed() {

    },
    mounted() {
        // 12個 col 中1個給 icon，2個給 labe，7個給 progressive bar，2個給"n次"
        // span 最小設定為1
        // +4 只是為了定位，+3是前面的icon與label的 col，+1是從 progressive bar 的下個 col 開始
        let numerator = Math.max(1, Math.floor(this.time*7/this.max_time))
        // this.progressive_bar_class += 'col-span-'+String(numerator)
        this.progressive_bar_style = {"grid-column": 'span '+numerator+' / span '+numerator}
        // this.text_class = 'col-start-'+String(numerator+4)
        this.text_style = {"grid-column-start": numerator+4}
        this.component_show = true
        
    },
    data() {
        return {
            // progressive_bar_class: ' ',
            // text_class: '',
            component_show: false,
            progressive_bar_style: '',
            text_style: '',
        }
    },
    methods: {

    }
}



</script>

<template>
    <div class="w-full grid grid-cols-12 p-2">
        <img :src="icon" class="col-span-1 col-start-1">
        <div class="col-span-2 col-start-2 text-sm text-center self-center">{{ label }}</div>
        <!-- 不知道為啥col-span-4 or 8 etc 有時候會卡住，有class但沒有render暫時改用style的方式 -->
        <!-- <div v-if="component_show" class="col-start-4 bg-orange-500 my-2 rounded-lg progressive_bar_ani" :class="progressive_bar_class" :key="k"></div>
        <div v-if="component_show" class="text-sm font-bold col-span-2 self-center text-center text_ani" :class="text_class"> {{ time }}次</div> -->
        <div v-if="component_show" class="col-start-4 bg-orange-500 my-2 rounded-lg progressive_bar_ani" :style="progressive_bar_style"></div>
        <div v-if="component_show" class="text-sm font-bold col-span-2 self-center text-center text_ani" :style="text_style"> {{ time }}次</div>
    </div>
</template>


<style lang="scss" scoped>

.progressive_bar_ani {
    animation: p_bar_ani 1s cubic-bezier(.44,1.02,.58,.92);
}

.text_ani {
    animation: t_ani 1s cubic-bezier(.44,1.02,.58,.92);
}


@keyframes p_bar_ani {
    0% {
        width: 0%;
    }
    100% {
        width: 100%;
    }
}

@keyframes t_ani {
    0% {
        opacity: 0%;
    }
    70% {
        opacity: 0%;
    }
    100% {
        opacity: 100%;
    }
}

</style>