var state = -1;

$(document).ready(function()  {
  $.ajax({
    type: "POST",
    url: '/state/',
    success: function(t) {
      state = t.state;
    }
  });
});

var check = setInterval(function()  {
  $.ajax({
  	type: "POST",
  	url: '/state/',
  	success: function(t) {
      if(state != t.state)  {
        location.reload();
      }
  	}
  });
}, 100);
