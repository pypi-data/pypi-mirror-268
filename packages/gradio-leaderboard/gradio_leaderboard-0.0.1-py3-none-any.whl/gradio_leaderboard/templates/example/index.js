const {
  SvelteComponent: z,
  append: w,
  attr: b,
  destroy_each: A,
  detach: a,
  element: h,
  empty: B,
  ensure_array_like: m,
  init: D,
  insert: u,
  listen: v,
  noop: g,
  run_all: F,
  safe_not_equal: G,
  space: E,
  text: H,
  toggle_class: _
} = window.__gradio__svelte__internal;
function k(f, e, l) {
  const t = f.slice();
  return t[9] = e[l], t[11] = l, t;
}
function y(f, e, l) {
  const t = f.slice();
  return t[12] = e[l], t[14] = l, t;
}
function I(f) {
  let e, l, t;
  function c(s, n) {
    return typeof /*loaded_value*/
    s[5] == "string" ? K : J;
  }
  let i = c(f)(f);
  return {
    c() {
      e = h("div"), i.c(), b(e, "class", "svelte-1bq8l1x"), _(
        e,
        "table",
        /*type*/
        f[1] === "table"
      ), _(
        e,
        "gallery",
        /*type*/
        f[1] === "gallery"
      ), _(
        e,
        "selected",
        /*selected*/
        f[2]
      );
    },
    m(s, n) {
      u(s, e, n), i.m(e, null), l || (t = [
        v(
          e,
          "mouseenter",
          /*mouseenter_handler*/
          f[7]
        ),
        v(
          e,
          "mouseleave",
          /*mouseleave_handler*/
          f[8]
        )
      ], l = !0);
    },
    p(s, n) {
      i.p(s, n), n & /*type*/
      2 && _(
        e,
        "table",
        /*type*/
        s[1] === "table"
      ), n & /*type*/
      2 && _(
        e,
        "gallery",
        /*type*/
        s[1] === "gallery"
      ), n & /*selected*/
      4 && _(
        e,
        "selected",
        /*selected*/
        s[2]
      );
    },
    d(s) {
      s && a(e), i.d(), l = !1, F(t);
    }
  };
}
function J(f) {
  let e, l, t = m(
    /*loaded_value*/
    f[5].slice(0, 3)
  ), c = [];
  for (let i = 0; i < t.length; i += 1)
    c[i] = q(k(f, t, i));
  let o = (
    /*value*/
    f[0].length > 3 && C(f)
  );
  return {
    c() {
      e = h("table");
      for (let i = 0; i < c.length; i += 1)
        c[i].c();
      l = E(), o && o.c(), b(e, "class", " svelte-1bq8l1x");
    },
    m(i, s) {
      u(i, e, s);
      for (let n = 0; n < c.length; n += 1)
        c[n] && c[n].m(e, null);
      w(e, l), o && o.m(e, null);
    },
    p(i, s) {
      if (s & /*loaded_value*/
      32) {
        t = m(
          /*loaded_value*/
          i[5].slice(0, 3)
        );
        let n;
        for (n = 0; n < t.length; n += 1) {
          const d = k(i, t, n);
          c[n] ? c[n].p(d, s) : (c[n] = q(d), c[n].c(), c[n].m(e, l));
        }
        for (; n < c.length; n += 1)
          c[n].d(1);
        c.length = t.length;
      }
      /*value*/
      i[0].length > 3 ? o ? o.p(i, s) : (o = C(i), o.c(), o.m(e, null)) : o && (o.d(1), o = null);
    },
    d(i) {
      i && a(e), A(c, i), o && o.d();
    }
  };
}
function K(f) {
  let e;
  return {
    c() {
      e = H(
        /*loaded_value*/
        f[5]
      );
    },
    m(l, t) {
      u(l, e, t);
    },
    p: g,
    d(l) {
      l && a(e);
    }
  };
}
function p(f) {
  let e;
  return {
    c() {
      e = h("td"), e.textContent = `${/*cell*/
      f[12]}`, b(e, "class", "svelte-1bq8l1x");
    },
    m(l, t) {
      u(l, e, t);
    },
    p: g,
    d(l) {
      l && a(e);
    }
  };
}
function L(f) {
  let e;
  return {
    c() {
      e = h("td"), e.textContent = "…", b(e, "class", "svelte-1bq8l1x");
    },
    m(l, t) {
      u(l, e, t);
    },
    d(l) {
      l && a(e);
    }
  };
}
function q(f) {
  let e, l, t = m(
    /*row*/
    f[9].slice(0, 3)
  ), c = [];
  for (let i = 0; i < t.length; i += 1)
    c[i] = p(y(f, t, i));
  let o = (
    /*row*/
    f[9].length > 3 && L()
  );
  return {
    c() {
      e = h("tr");
      for (let i = 0; i < c.length; i += 1)
        c[i].c();
      l = E(), o && o.c();
    },
    m(i, s) {
      u(i, e, s);
      for (let n = 0; n < c.length; n += 1)
        c[n] && c[n].m(e, null);
      w(e, l), o && o.m(e, null);
    },
    p(i, s) {
      if (s & /*loaded_value*/
      32) {
        t = m(
          /*row*/
          i[9].slice(0, 3)
        );
        let n;
        for (n = 0; n < t.length; n += 1) {
          const d = y(i, t, n);
          c[n] ? c[n].p(d, s) : (c[n] = p(d), c[n].c(), c[n].m(e, l));
        }
        for (; n < c.length; n += 1)
          c[n].d(1);
        c.length = t.length;
      }
    },
    d(i) {
      i && a(e), A(c, i), o && o.d();
    }
  };
}
function C(f) {
  let e;
  return {
    c() {
      e = h("div"), b(e, "class", "overlay svelte-1bq8l1x"), _(
        e,
        "odd",
        /*index*/
        f[3] % 2 != 0
      ), _(
        e,
        "even",
        /*index*/
        f[3] % 2 == 0
      ), _(
        e,
        "button",
        /*type*/
        f[1] === "gallery"
      );
    },
    m(l, t) {
      u(l, e, t);
    },
    p(l, t) {
      t & /*index*/
      8 && _(
        e,
        "odd",
        /*index*/
        l[3] % 2 != 0
      ), t & /*index*/
      8 && _(
        e,
        "even",
        /*index*/
        l[3] % 2 == 0
      ), t & /*type*/
      2 && _(
        e,
        "button",
        /*type*/
        l[1] === "gallery"
      );
    },
    d(l) {
      l && a(e);
    }
  };
}
function M(f) {
  let e, l = (
    /*loaded*/
    f[6] && I(f)
  );
  return {
    c() {
      l && l.c(), e = B();
    },
    m(t, c) {
      l && l.m(t, c), u(t, e, c);
    },
    p(t, [c]) {
      /*loaded*/
      t[6] && l.p(t, c);
    },
    i: g,
    o: g,
    d(t) {
      t && a(e), l && l.d(t);
    }
  };
}
function N(f, e, l) {
  let { value: t } = e, { type: c } = e, { selected: o = !1 } = e, { index: i } = e, s = !1, n = t, d = Array.isArray(n);
  const S = () => l(4, s = !0), j = () => l(4, s = !1);
  return f.$$set = (r) => {
    "value" in r && l(0, t = r.value), "type" in r && l(1, c = r.type), "selected" in r && l(2, o = r.selected), "index" in r && l(3, i = r.index);
  }, [
    t,
    c,
    o,
    i,
    s,
    n,
    d,
    S,
    j
  ];
}
class O extends z {
  constructor(e) {
    super(), D(this, e, N, M, G, { value: 0, type: 1, selected: 2, index: 3 });
  }
}
export {
  O as default
};
