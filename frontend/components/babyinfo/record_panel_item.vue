<script>
export default {
    props: ["img_src", "label"],
    created () {

    },
    computed() {

    },
    mounted() {

    },
    data() {
        return {

        }
    },
    methods: {
        on_click() {
            navigateTo({
                path: '/record', 
                query: {
                    record_type: this.label
                }
            })
        },

    }
}


</script>



<template>
    <div class="grid">
        <button class="w-14 h-14 rounded-full bg-white self-center justify-self-center" @click="on_click">
            <img :src="img_src" class="object-contain p-3">
        </button>
        <!-- <div class="rounded-full col-start-2 text-slate-950 text-end justify-self-center"> -->
        <div class="text-slate-950 font-bold text-end justify-self-center">
            {{ label }}
        </div>
    </div>
</template>