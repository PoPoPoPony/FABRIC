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
                            <g clip-path="url(#clip0_78_990)">
                            <path d="M12.0002 2C11.289 2 10.7145 2.55859 10.7145 3.25V4C7.78146 4.57812 5.57164 7.10156 5.57164 10.125V10.8594C5.57164 12.6953 4.87655 14.4688 3.62298 15.8438L3.32565 16.168C2.98815 16.5352 2.9078 17.0625 3.11271 17.5117C3.31762 17.9609 3.77967 18.25 4.28592 18.25H19.7145C20.2207 18.25 20.6788 17.9609 20.8877 17.5117C21.0966 17.0625 21.0123 16.5352 20.6748 16.168L20.3774 15.8438C19.1239 14.4688 18.4288 12.6992 18.4288 10.8594V10.125C18.4288 7.10156 16.219 4.57812 13.2859 4V3.25C13.2859 2.55859 12.7114 2 12.0002 2ZM13.8203 21.2695C14.3024 20.8008 14.5716 20.1641 14.5716 19.5H12.0002H9.42878C9.42878 20.1641 9.69798 20.8008 10.1801 21.2695C10.6623 21.7383 11.3172 22 12.0002 22C12.6832 22 13.3382 21.7383 13.8203 21.2695Z" fill="white"/>
                            </g>
                            <defs>
                            <clipPath id="clip0_78_990">
                            <rect width="18" height="20" fill="white" transform="translate(3 2)"/>
                            </clipPath>
                            </defs>
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
    @include border-ring(#FF9416 #CBCBCB, 10px, 170);
    animation-name: clock_animation;
    animation-duration: 1s;
    animation-timing-function: cubic-bezier(0,1.08,0,1.01);
}


@keyframes clock_animation {
    $degree: 170;
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