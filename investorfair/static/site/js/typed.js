! function(t) {
	"use strict";
	var s = function(s, e) {
		this.el = t(s), this.options = t.extend({}, t.fn.typed.defaults, e), this.text = this.el.text(), this.typeSpeed = this.options.typeSpeed, this.startDelay = this.options.startDelay, this.backSpeed = this.options.backSpeed, this.backDelay = this.options.backDelay, this.strings = this.options.strings, this.strPos = 0, this.arrayPos = 0, this.stopNum = 0, this.loop = this.options.loop, this.loopCount = this.options.loopCount, this.curLoop = 0, this.stop = !1, this.build()
	};
	s.prototype = {
		constructor: s,
		init: function() {
			var t = this;
			t.timeout = setTimeout(function() {
				t.typewrite(t.strings[t.arrayPos], t.strPos)
			}, t.startDelay)
		},
		build: function() {
			this.cursor = t('<span class="typed-cursor">|</span>'), this.el.after(this.cursor), this.init()
		},
		typewrite: function(t, s) {
			if (this.stop !== !0) {
				var e = Math.round(70 * Math.random()) + this.typeSpeed,
					o = this;
				o.timeout = setTimeout(function() {
					var e = 0,
						i = t.substr(s);
					if ("^" === i.charAt(0)) {
						var r = 1;
						i.match(/^\^\d+/) && (i = i.replace(/^\^(\d+).*/, "$1"), r += i.length, e = parseInt(i)), t = t.substring(0, s) + t.substring(s + r)
					}
					o.timeout = setTimeout(function() {
						if (s === t.length) {
							if (o.options.onStringTyped(o.arrayPos), o.arrayPos === o.strings.length - 1 && (o.options.callback(), o.curLoop++, o.loop === !1 || o.curLoop === o.loopCount)) return;
							o.timeout = setTimeout(function() {
								o.backspace(t, s)
							}, o.backDelay)
						} else 0 === s && o.options.preStringTyped(o.arrayPos), o.el.text(o.text + t.substr(0, s + 1)), s++, o.typewrite(t, s)
					}, e)
				}, e)
			}
		},
		backspace: function(t, s) {
			if (this.stop !== !0) {
				var e = Math.round(70 * Math.random()) + this.backSpeed,
					o = this;
				o.timeout = setTimeout(function() {
					o.el.text(o.text + t.substr(0, s)), s > o.stopNum ? (s--, o.backspace(t, s)) : s <= o.stopNum && (o.arrayPos++, o.arrayPos === o.strings.length ? (o.arrayPos = 0, o.init()) : o.typewrite(o.strings[o.arrayPos], s))
				}, e)
			}
		},
		reset: function() {
			var t = this;
			clearInterval(t.timeout);
			var s = this.el.attr("id");
			this.el.after('<span id="' + s + '"/>'), this.el.remove(), this.cursor.remove(), t.options.resetCallback()
		}
	}, t.fn.typed = function(e) {
		return this.each(function() {
			var o = t(this),
				i = o.data("typed"),
				r = "object" == typeof e && e;
			i || o.data("typed", i = new s(this, r)), "string" == typeof e && i[e]()
		})
	}, t.fn.typed.defaults = {
		strings: ["These are the default values...", "You know what you should do?", "Use your own!", "Have a great day!"],
		typeSpeed: 0,
		startDelay: 0,
		backSpeed: 0,
		backDelay: 500,
		loop: !1,
		loopCount: !1,
		callback: function() {},
		preStringTyped: function() {},
		onStringTyped: function() {},
		resetCallback: function() {}
	}
}(window.jQuery);

function TickerScrambler(a, b) {
	function c() {
		o = setTimeout(d, k)
	}

	function d() {
		q ? (p = a.textContent.length - 1, o = setInterval(g, j), q = !1) : (p = 0, o = setInterval(f, j), q = !0)
	}

	function e() {
		return l ? Math.floor(m.length * Math.random()) : i < m.length - 1 ? i + 1 : 0
	}

	function f() {
		var b, c;
		if (p < m[i].length) {
			var f = m[i].substr(p, 1);
			b = a.textContent.length - p - 1, c = h(b), a.textContent = a.textContent.substr(0, p) + f + c, p++
		} else p < a.textContent.length && (b = a.textContent.length - m[i].length - 1, c = h(b), a.textContent = a.textContent.substr(0, m[i].length) + c, a.textContent.length == m[i].length && p++);
		p >= m[i].length && p >= a.textContent.length && (p = 0, i = e(), clearInterval(o), setTimeout(d, k))
	}

	function g() {
		var b = a.textContent.length - p,
			c = h(b);
		a.textContent = a.textContent.substr(0, p) + c, p--, 0 === p && (clearInterval(o), d())
	}

	function h(a) {
		for (var b = "", c = 0; a > c; c++) b += n.charAt(Math.floor(Math.random() * n.length));
		return b
	}
	if (a && 1 == a.nodeType && b && b.list && b.list.length) {
		var i = b.index || 0,
			j = b.speed || 33,
			k = b.pause || 1e3,
			l = b.random || !1,
			m = b.list || [],
			n = b.charset || "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=`~<>?,./;:[]\{}|",
			o = null,
			p = null,
			q = !0;
		c()
	}
}
window.jQuery && ! function() {
	$.fn.TickerScrambler = function(a) {
		return this.each(function() {
			$(this).data("TickerScrambler", new TickerScrambler($(this)[0], a))
		})
	}
}(window.jQuery);


function scramble(strings) {
	$('.array').TickerScrambler({
		list: strings,
		pause: 1500,
		random: true,
		speed: 30
	});
}
