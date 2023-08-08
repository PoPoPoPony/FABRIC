<template>
    <button class="rounded-md bg-zinc-200 px-2" :class="btn_class" @focus="on_focus" @blur="on_blur">
        <div class="w-max font-bold text-sm" :class="text_class">{{ title }}</div>
    </button>
</template>
<script>
export default {
    props: ["title"],
    data () {
        return {
            btn_class: "",
            text_class: "text-black",
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

    },
}
</script>
<style lang="scss">
    
</style>