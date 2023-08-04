<script>
export default {
    props: [],
    created () {


        
    },
    mounted() {

    },
    data() {
        return {
            page_type: "statistic",
        }
    },
    methods: {

    }

}

</script>



<template>
    <div class="bg-no-repeat bg-cover w-full h-screen bg-neutral-200">
        <!-- <div class="box m-10 test rounded-full bg-neutral-500" style="width: 200px; height: 200px;">
            <div class="box-top"></div>
            <div class="box-right"></div>
            <div class="box-bottom"></div>
        </div> -->
        <div class="clock-wrap">
            <img src="https://picsum.photos/id/1069/200/200">
        </div>



            <!-- <div class="test col-span-2 bg-orange-300 rounded-full">
                {{ message }}
            </div>
        </div> -->



        <div class="absolute inset-x-0 bottom-0 h-12 bg-neutral-50" >
            <footer_banner :page_type="page_type" class=""></footer_banner>
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
        radial-Gradient(circle at calc(50% + ( 50% - #{$r} ) * #{$tail_x}) calc(50% - ( 50% - #{$r} ) * #{$tail_y}), nth($colors, 1) calc(#{$r} - 1px), transparent $r)
    );
    
    // #{$degree}deg

    background: $round_end, conic-gradient(nth($colors, 1) 0% #{$degree}deg, nth($colors, 2) 0% 360deg);
    border: solid $border transparent;
    background-origin: border-box;
    
    

    border-radius: 50%;
    --mask:
        radial-Gradient(
            closest-side, 
            red calc(100% - #{$border} - 1px), 
            transparent calc(100% - #{$border}) calc(100% - #{$border}), 
            red  calc(100% - #{$border} + 1px) calc(100% - 1px), 
            transparent
        );
}



img {
    width: calc(100vw - 80px);
    height: auto;
    @include border-ring(#FF9416 #CBCBCB, 10px, 330);
}
</style>