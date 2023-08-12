<script>

export default {
    props: ["label_idx", "current_idx", "img_src", "name"],
    created () {



    },
    mounted () {
        if (this.label_idx == this.current_idx) {
            this.bg_class = this.bg_focus
            this.text_class = this.text_focus
        } else {
            this.bg_class = this.bg_blur
            this.text_class = this.text_blur
        }
        this.btn_show = true

    },
    data() {
        return { 
            // settings of focus / blur classes
            bg_focus: 'bg-slate-700',
            bg_blur: 'bg-neutral-50',
            text_focus: 'text-neutral-50',
            text_blur: 'text-orange-500',


            bg_class: '',
            text_class: '',
            btn_show: false
        }
    },
    methods: {
        on_click() {
            this.$emit('change_current_idx', this.label_idx)
        },
    }
}



</script>

<template>
    <button v-if="btn_show" class="rounded-full drop-shadow-md px-5 py-1 self-center mb-5" :class="bg_class" @click="on_click">
        <div class="flex items-center justify-center ">
            <img :src="img_src" class="object-contain h-8 w-12 rounded-full">
            <span class="mr-2" :class="text_class">{{ name }}</span>
        </div>
    </button>
</template>