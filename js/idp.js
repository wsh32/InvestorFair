var api = impress();
var action = setTimeout(function()  {
  api.next();
}, 60000);

$.fn.extend({
	animateCss: function (animationName) {
		var animationEnd = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
		$(this).addClass('animated ' + animationName).one(animationEnd, function () {
			$(this).removeClass('animated ' + animationName);
		});
	}
});

$(document).ready(function () {
	api.init();
  clearTimeout(action);
});

// probably not the best way but eh
// comment out for debug
// $('.step').on('impress:stepenter', function () {
//   clearTimeout(action);
// 	action = setTimeout(function() {
// 	  api.next();
// 	}, $(this).attr('timeout'));
// });

$('#group').on('impress:stepenter', function () {
	$(this).find('img').animateCss('tada');
});
