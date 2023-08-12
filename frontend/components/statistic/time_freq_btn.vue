<script>

export default {
    props: ["time_freq", "current_time_freq"],
    created () {

    },
    computed() {

    },
    mounted() {
        if (this.time_freq == this.current_time_freq) {
            this.on_focus()
        }
        this.show_btn = true
    },
    data() {
        // four page name: babyinfo / statistic / knowledge / account
        return {
            show_btn: false,
            btn_class: "",
        }
    },
    methods: {
        on_focus() {
            this.btn_class = "bg-zinc-50 drop-shadow-lg"
        },
        on_click() {
            this.$emit('time_freq_change', this.time_freq)
        }
    }
}



</script>

<template>
    <div class="px-1 my-1 w-full">
        <button v-if="show_btn" class="rounded-md  w-full -my-3" :class="btn_class" @click="on_click">
            <span class="text-xs">{{ time_freq }}</span>
        </button>
    </div>
    
</template>


