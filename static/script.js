$(document).ready(function() {
	$("#operation").change(function() {
		var val = $(this).val();
        console.log("from script.js: " + val);
		if (val === "power") {
			$("#num2-div").show();
		} else {
			$("#num2-div").hide();
		}
	});
});

