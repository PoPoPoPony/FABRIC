<script>

export default {
    props: ["message"],
    created () {

    },
    computed() {
        this.set_clock_data()
        this.set_rotate_back()
    },
    mounted() {
        this.$nextTick(() => {
            // reset clock data after parent element rendered
            const element = this.$refs.clock_container
            this.clock_width = element.offsetWidth
            this.set_clock_data()
            this.set_sub_clock_data()
            // console.log(this.clock_width)
            this.clock_key+=1
            this.sub_clock_key+=1
        })
    },
    data() {
        // width="48" height="48"
        return { 
            linear_gradient_1: "#ffffff 0%",
            linear_gradient_2: "#ffffff 20%",
            linear_gradient_3: "#f97316 30%",
            linear_gradient_4: "#f97316 100%",
            rotate_degree: "162deg",
            clock_width: 300,
            clock_key: 0,
            sub_clock_key: 0,
        }
    },
    methods: {
        set_clock_data() {
            // transform: `rotate(${this.rotate_degree})`
            return {
                position: 'relative',
                background: `linear-gradient(${this.linear_gradient_1}, ${this.linear_gradient_2}, ${this.linear_gradient_3}, ${this.linear_gradient_4})`,
                'border-radius': '50%',
                'background-color': '#f97316',
                width: `${this.clock_width*0.9}px`,
                height: `${this.clock_width*0.9}px`,
                
            };
        },

        set_sub_clock_data() {
            return {
                position: 'absolute',
                display: 'block',
                top: `${this.clock_width*0.05}px`,
                left: `${this.clock_width*0.05}px`,
                content: "",
                width: `${this.clock_width*0.8}px`,
                height: `${this.clock_width*0.8}px`,
                'background-color': '#d4d4d4',
                'background-repeat': 'no-repeat',
                'background-size': 'cover',
                'border-radius': '50%',
                overflow: 'hidden'
            }
        },
        set_rotate_back() {
            // 
            return {
                transform: `rotate(-178deg)`,
            };
        },

    }
}



</script>

<template>
    <div class="content-center" ref="clock_container">
        <div :style="set_clock_data()" :key="clock_key">
            <div :style="set_sub_clock_data()" :key="sub_clock_key">
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
                        <button class="rounded-full bg-orange-500 ml-1 mt-2 ">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="#ffffff" viewBox="0 0 24 24" stroke-width="0" stroke="currentColor" class="w-14 h-14">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M14.857 17.082a23.848 23.848 0 005.454-1.31A8.967 8.967 0 0118 9.75v-.7V9A6 6 0 006 9v.75a8.967 8.967 0 01-2.312 6.022c1.733.64 3.56 1.085 5.455 1.31m5.714 0a24.255 24.255 0 01-5.714 0m5.714 0a3 3 0 11-5.714 0" />
                            </svg>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<style scoped>

/* :root {
    --linear-gradient_1: #000000 0%;
    --linear-gradient_2: #000000 90%;
    --linear-gradient_3: #ffffff 91%;
    --linear-gradient_4: #ffffff 100%;
    --rotate_degree: 162deg;
} */


/*     
    width:100px;
    height:100px;
 */
/* 
    width: 90px;
    height: 90px;
*/



/* 
    background-image: url("images/profilePic.jpg");
*/

/* .CircleBorder{
    position: relative;
    background: `linear-gradient(${this.linear_gradient_1}, ${this.linear_gradient_2}, ${this.linear_gradient_3}, ${this.linear_gradient_4})`;
    -webkit-border-radius:50px;
    -moz-border-radius:50px;
    border-radius:50%;
    background-color: #f97316;
    width:100px;
    height:100px;
    transform: `rotate(${rotate_degree})`;
} */
/* .CircleBorder:after {
    position: absolute;
    display: block;
    top: 20px;
    left: 20px;
    content: "";
    width: var(clock_width)px;
    height: var(clock_width)px;
    background-color: #d4d4d4;
    background-repeat: no-repeat;
    background-size: cover;
    border-radius: 50%;
    overflow: hidden;
} */




</style>