<template>
    <!-- <button v-if="show_btn" class="rounded-md bg-zinc-200 px-2" :class="btn_class" @focus="on_focus" @blur="on_blur" autofocus> -->
    <button v-if="show_btn" class="rounded-md bg-zinc-200 px-2" :class="btn_class" :key="current_title" @click="on_click">
        <div class="w-max font-bold text-sm" :class="text_class">{{ title }}</div>
    </button>
</template>
<script>
export default {
    props: ["title", "current_title"],
    mounted () {
        if (this.title == this.current_title) {
            this.on_focus()
        }
        this.show_btn = true
    },
    data () {
        return {
            btn_class: "",
            text_class: "text-black",
            show_btn: false
        }
    }
,    methods: {
        on_focus() {
            this.btn_class = "ring-2 ring-orange-400"
            this.text_class = "text-orange-400"
        },

        on_blur() {
            this.btn_class = ""
            this.text_class = "text-black"
        },
        on_click() {
            this.$emit('change_current_title', this.title)
        },
    },
}
</script>