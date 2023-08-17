<template>
	<div
		class="relative text-black dark:text-black"
		v-show="timepicker_show"
		ref="time_picker"
	>
		<input
			type="text"
			class="block w-full rounded border-0 bg-transparent px-3 py-1 data-[te-input-state-active] font-bold"
			style="background-color: #eeeeef; color: black"
			ref="time_picker_text"
		/>

	</div>
</template>

<script>
import { Timepicker, Input, initTE } from "tw-elements";

export default {
	props: ["default_time"],
	created() {
		initTE({ Timepicker, Input });
	},
	mounted() {
		new Timepicker(
			this.$refs.time_picker,
			{
				defaultTime: this.time,
				iconSVG: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="black" class="w-5 h-5"> <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z" /> </svg>'
			},
			{
				timepickerToggleButton:
					'[&>svg]:w-5 [&>svg]:h-5 ml-auto absolute outline-none border-none bg-transparent right-0.5 top-1/2 -translate-x-1/2 -translate-y-1/2 transition-all duration-300 ease-[cubic-bezier(0.25,0.1,0.25,1)] cursor-pointer hover:text-[#3b71ca] focus:text-[#3b71ca] dark:hover:text-[#3b71ca] dark:focus:text-[#3b71ca] dark:text-blak',
			}
		);

		this.$refs.time_picker.addEventListener(
			"input.te.timepicker",
			(_) => {
				// 超傻眼= = tw-element picker的callback沒有時間
				console.log(this.$refs.time_picker_text.value) 
			}
		);

		this.timepicker_show = true;
	},
	data() {
		return {
			time: this.default_time,
			timepicker_show: false,
		};
	},
	methods: {},
};
</script>

<style scoped></style>
