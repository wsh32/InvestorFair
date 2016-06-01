// $.ajax({
//   type: "POST",
//   url: '/state_set/',
//   success: function(t) {
//     console.log(t.state);
//     return t.state;
//   }
// });

function go(state) {
  var formData = new FormData();
	formData.append( 'state', state );

	$.ajax({
		type: 'POST',
		url: '/set/',
		data: formData,
		dataType: 'JSON',
		processData: false,
		contentType: false,
		success: function(t)
		{
			if( t.success == true )
			{
        Materialize.toast("OK", 1500);
			}
		}
	});
}

function normal() {
  go(0);
}

function commercial() {
  go(1);
}

function blank() {
  go(2);
}

function rickroll() {
  go(3);
}

function justdoit() {
  go(4);
}

function darude() {
  go(5);
}
