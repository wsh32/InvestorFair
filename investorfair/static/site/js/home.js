$(document).ready(function() {
	$('.typed').typed({
		strings: ["Experience: "],
		typeSpeed: 50,
		callback: function() {
			scramble(['Blast Off', 'Pit Stop', 'Hot Tires', 'Super Track', 'Infinite Loop', 'Crazy Copter', 'Jetpack Jolts', 'Viking Ship'])
		}
	});
});
