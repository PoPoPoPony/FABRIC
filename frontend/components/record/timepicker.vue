<template>
	<div
		class="relative text-black dark:text-black"
		v-show="timepicker_show"
		data-te-input-wrapper-init
		ref="time_picker"
	>
		<input
			type="text"
			class="block w-full rounded border-0 bg-transparent px-3 py-1 data-[te-input-state-active] font-bold"

			style="background-color: #eeeeef; color: black"
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
		this.time = this.default_time;

		new Timepicker(
			this.$refs.time_picker,
			{
				// format: "yyyy/mm/dd",
				// startDate: this.time,
			},
			{
				// datepickerToggleButton:
				// 	"flex items-center justify-content-center [&>svg]:w-5 [&>svg]:h-5 absolute outline-none border-none bg-transparent right-0.5 top-1/2 -translate-x-1/2 -translate-y-1/2 text-black dark:text-black",
			}
		);

		// this.$refs.time_picker.addEventListener(
		// 	"dateChange.te.datepicker",
		// 	(event) => {
    //     console.log(event)
    //   }
		// );

		this.timepicker_show = true;
	},
	data() {
		return {
			time: "",
			timepicker_show: false,
		};
	},
	methods: {},
};
</script>

<style scoped></style>
