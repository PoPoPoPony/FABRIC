<script>


export default {
    props: ["color", "index", "user_poop_index"],
    created () {

    },
    computed() {

    },
    mounted() {
        if (this.index == 0) {
            this.rouned_class+='rounded-l-lg '
        } 
        if (this.index == this.user_poop_index) {
            this.rouned_class+='rounded-r-lg'
        }
        
    },
    data() {
        return {
            rouned_class: '',
        }
    },
    methods: {
        
    }
}



</script>

<template>
    <div class="w-full h-2" :style="{'background-color': color}" :class="rouned_class">
        
    </div>
</template>

