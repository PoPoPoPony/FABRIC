<script>

export default {
    props: ["message"],
    created () {

    },
    computed() {
        this.set_clock_data()
        // this.set_rotate_back()
    },
    mounted() {
        this.$nextTick(() => {
            // reset clock data after parent element rendered
            this.clock_width = window.innerWidth
            this.clock_show_able = true
        })
    },
    data() {
        // width="48" height="48"
        return {
            linear_gradient_1: "#CBCBCB 0%",
            linear_gradient_2: "#CBCBCB 20%",
            linear_gradient_3: "#ff9416 30%",
            linear_gradient_4: "#ff9416 100%",
            rotate_degree: "162deg",
            // 
            clock_width: 0,
            clock_key: 0,
            sub_clock_key: 0,
            clock_show_able: false,
            kk:0,
        }
    },
    methods: {
        // set_clock_data() {
        //     // transform: `rotate(${this.rotate_degree})`

        //     // `linear-gradient(${this.linear_gradient_1}, ${this.linear_gradient_2}, ${this.linear_gradient_3}, ${this.linear_gradient_4})`

        //     return {
        //         position: 'relative',
        //         background: `linear-gradient(${this.linear_gradient_1}, ${this.linear_gradient_2}, ${this.linear_gradient_3}, ${this.linear_gradient_4})`,
        //         // background: 'rgb(206, 206, 206)',
        //         // background: 'linear-gradient(180deg, rgba(206, 206, 206, 1) 10%, rgba(255,148,22,1) 52%)',
        //         // 'border-width': '10px',
        //         'border-radius': '50%',
        //         'border-color': 'rgba(255,148,22,1) rgba(206, 206, 206, 1)',
        //         // 'background-color': '#eee 35%',
        //         width: `${this.clock_width*0.8}px`,
        //         height: `${this.clock_width*0.8}px`,
        //     };
        // },

        set_clock_data() {
            // transform: `rotate(${this.rotate_degree})`

            // `linear-gradient(${this.linear_gradient_1}, ${this.linear_gradient_2}, ${this.linear_gradient_3}, ${this.linear_gradient_4})`

            return {
                width: `${this.clock_width*0.8}px`,
                height: `${this.clock_width*0.8}px`,
                overflow: "visible"
            };
        },

        // set_sub_clock_data() {
        //     return {
        //         position: 'absolute',
        //         display: 'block',
        //         top: `${this.clock_width*0.05}px`,
        //         left: `${this.clock_width*0.05}px`,
        //         content: "",
        //         width: `${this.clock_width*0.7}px`,
        //         height: `${this.clock_width*0.7}px`,
        //         'background-color': '#e5e5e5',
        //         'background-repeat': 'no-repeat',
        //         'background-size': 'cover',
        //         'border-radius': '50%',
        //         overflow: 'hidden'
        //     }
        // },


        set_sub_clock_data() {
            return {
                position: 'absolute',
                // display: 'block',
                top: `${this.clock_width*0.09}px`,
                left: `${this.clock_width*0.125}px`,
                // content: "",
                width: `${this.clock_width*0.7}px`,
                height: `${this.clock_width*0.7}px`,
                'background-color': '#e5e5e5',
                'background-repeat': 'no-repeat',
                'background-size': 'cover',
                'border-radius': '50%',
                // overflow: 'hidden'
            }
        },





        // set_rotate_back() {
        //     // 
        //     return {
        //         transform: `rotate(-178deg)`,
        //     };
        // },

    }
}



</script>

<template>
    <div class="content-center">
        <div class="content-center clock" :style="set_clock_data()" v-if="clock_show_able">
            <!-- <div :style="set_sub_clock_data()" :key="sub_clock_key" v-if="clock_show_able"> -->
            <div class="grid grid-rows-5 grid-cols-5 w-full h-full gap-1">
                <div class="row-start-2 row-span-1 col-span-5 text-center font-bold text-lg">
                    {{ message }}
                </div>
                <div class="row-start-3 row-span-1 col-span-5 text-center font-bold text-lg">
                    <span class="font-bold text-5xl">2</span>
                    <span class="font-bold text-lg mx-2">小時</span>
                    <span class="font-bold text-5xl">34</span>
                    <span class="font-bold text-lg ml-2">分</span>
                </div>
                <div class="row-start-4 row-span-2 col-start-2 col-span-3 mx-auto">
                    <div class="text-center top-0 ">
                        下午 3:23
                    </div>
                    <button class="rounded-full bg-orange-400 ml-1 mt-2 w-15 h-15 justify-self-center p-1">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="#ffffff" viewBox="0 0 24 24" stroke-width="0" stroke="currentColor" class="w-11 h-11 justify-self-center">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M14.857 17.082a23.848 23.848 0 005.454-1.31A8.967 8.967 0 0118 9.75v-.7V9A6 6 0 006 9v.75a8.967 8.967 0 01-2.312 6.022c1.733.64 3.56 1.085 5.455 1.31m5.714 0a24.255 24.255 0 01-5.714 0m5.714 0a3 3 0 11-5.714 0" />
                        </svg>
                    </button>
                </div>
            </div>
            <!-- </div> -->
        </div>
    </div>
</template>


<style lang="scss" scoped>

@mixin border-ring($colors, $border, $degree) {
    // $tail_x: math.percentage(math.cos(math.div(math.$pi*2, 360) * 90));
    // $tail_y: math.percentage(math.sin(math.div(math.$pi*2, 360) * 90));
    $tail_x: math.cos(math.div(math.$pi*2, 360) * (90 - $degree));
    $tail_y: math.sin(math.div(math.$pi*2, 360) * (90 - $degree));

    $r: $border*0.5;
    // calc(100% - $r) 50%
    $round_end: (
        radial-Gradient(circle at 50% $r, nth($colors, 1) calc(#{$r} - 1px), transparent $r),
        radial-Gradient(circle at calc(50% + ( 50% - #{$r} ) * #{$tail_x}) calc(50% - ( 50% - #{$r} ) * #{$tail_y}), nth($colors, 1) calc(#{$r} - 1px), transparent $r),
        radial-Gradient(circle at center, #e5e5e5 0% calc(100% - 30% - #{$border}), transparent calc(100% - 30% - #{$border} + 1px) 100%),
    );

    background: $round_end, conic-gradient(nth($colors, 1) 0% #{$degree}deg, nth($colors, 2) 0% 360deg);
    border: solid $border transparent;
    background-origin: border-box;
    
    

    border-radius: 50%;
	// mask: 
    //     radial-Gradient(
    //         closest-side, 
    //         transparent 0% calc(100% - #{$border}),
    //         red calc(100% - #{$border} + 1px),
    //         red 100%
    //     );
        // transparent




    // -webkit-mask: var(--mask);
    // mask: var(--mask);
}



.clock {
    @include border-ring(#FF9416 #CBCBCB, 10px, 330);
    animation-name: clock_animation;
    animation-duration: 1s;
    animation-timing-function: cubic-bezier(0,1.08,0,1.01);
}


@keyframes clock_animation {
    $degree: 330;
    // $degree_frame: ();

    @for $i from 1 through 100 {
        // @if $i % 2 == 0 {
        // $degree_frame: append($degree_frame, $i)
        #{$i}% { @include border-ring(#FF9416 #CBCBCB, 10px, math.div($degree, 100) * $i);}
        // }
    }


    // 0%{ @include border-ring(#FF9416 #CBCBCB, 10px, 0);}
    // 50% { @include border-ring(#FF9416 #CBCBCB, 10px, 35);}
    // 100% { @include border-ring(#FF9416 #CBCBCB, 10px, 70);}
}

</style>