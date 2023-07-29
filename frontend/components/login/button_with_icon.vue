<script>
// import bg_screen from '~/assets/login/bg.jpg'
// import bg_smart_phone from '~/assets/login/smart_phone_bg.jpg'

export default {
    props: ["icon_name"],
    created () {
        // const { isMobile } = useDevice()
        // if(isMobile) {
        //     this.bg = bg_smart_phone
        // } else {
        //     this.bg = bg_screen
        // }
        if (this.icon_name == 'Apple') {
            this.svg_tag = this.apple_svg_tag
        } else if (this.icon_name == 'Google') {
            this.svg_tag = this.google_svg_tag
        }

        
    },
    data() {
        // width="48" height="48"
        return { 
            google_svg_tag: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><path fill="#ffc107" d="M43.611 20.083H42V20H24v8h11.303c-1.649 4.657-6.08 8-11.303 8-6.627 0-12-5.373-12-12s5.373-12 12-12c3.059 0 5.842 1.154 7.961 3.039l5.657-5.657C34.046 6.053 29.268 4 24 4 12.955 4 4 12.955 4 24s8.955 20 20 20 20-8.955 20-20c0-1.341-.138-2.65-.389-3.917z"/><path fill="#ff3d00" d="m6.306 14.691 6.571 4.819C14.655 15.108 18.961 12 24 12c3.059 0 5.842 1.154 7.961 3.039l5.657-5.657C34.046 6.053 29.268 4 24 4 16.318 4 9.656 8.337 6.306 14.691z"/><path fill="#4caf50" d="M24 44c5.166 0 9.86-1.977 13.409-5.192l-6.19-5.238A11.91 11.91 0 0 1 24 36c-5.202 0-9.619-3.317-11.283-7.946l-6.522 5.025C9.505 39.556 16.227 44 24 44z"/><path fill="#1976d2" d="M43.611 20.083H42V20H24v8h11.303a12.04 12.04 0 0 1-4.087 5.571l.003-.002 6.19 5.238C36.971 39.205 44 34 44 24c0-1.341-.138-2.65-.389-3.917z"/></svg>',
            apple_svg_tag: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><path d="M33 25c0 7 6 9 6 9l-3 7c-2 3-4 6-8 6l-8-2-7 2c-4 0-6-3-8-6-4-6-7-16-3-24 2-3 6-5 10-6l8 2 9-2c2 0 6 1 9 5 0 0-5 3-5 9M27 7l2-7-7 4c-2 1-3 4-3 7 3 0 6-2 8-4" style="stroke:none;fill-rule:nonzero;fill:#000;fill-opacity:1"/></svg>',

            svg_tag: 0
        }
    },
    methods: {

    }
}



</script>

<template>
    <button class="rounded-3xl bg-zinc-200 p-2 self-center">
        <div class="flex items-center justify-center">
            <!-- <img src="path/to/image.jpg"> -->
            <div class="mr-3 w-8 h-8" v-html="svg_tag"></div>
            <div>
                <strong>Continue with {{icon_name}}</strong>
            </div>
        </div>
    </button>
</template>