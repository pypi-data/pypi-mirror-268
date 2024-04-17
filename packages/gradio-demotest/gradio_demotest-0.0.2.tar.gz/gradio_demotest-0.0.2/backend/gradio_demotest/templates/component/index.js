const {
  SvelteComponent: dt,
  assign: mt,
  create_slot: bt,
  detach: gt,
  element: ht,
  get_all_dirty_from_scope: wt,
  get_slot_changes: pt,
  get_spread_update: kt,
  init: yt,
  insert: vt,
  safe_not_equal: qt,
  set_dynamic_element_data: Ce,
  set_style: V,
  toggle_class: P,
  transition_in: lt,
  transition_out: nt,
  update_slot_base: Ft
} = window.__gradio__svelte__internal;
function Ct(n) {
  let e, t, l;
  const s = (
    /*#slots*/
    n[18].default
  ), i = bt(
    s,
    n,
    /*$$scope*/
    n[17],
    null
  );
  let f = [
    { "data-testid": (
      /*test_id*/
      n[7]
    ) },
    { id: (
      /*elem_id*/
      n[2]
    ) },
    {
      class: t = "block " + /*elem_classes*/
      n[3].join(" ") + " svelte-nl1om8"
    }
  ], o = {};
  for (let r = 0; r < f.length; r += 1)
    o = mt(o, f[r]);
  return {
    c() {
      e = ht(
        /*tag*/
        n[14]
      ), i && i.c(), Ce(
        /*tag*/
        n[14]
      )(e, o), P(
        e,
        "hidden",
        /*visible*/
        n[10] === !1
      ), P(
        e,
        "padded",
        /*padding*/
        n[6]
      ), P(
        e,
        "border_focus",
        /*border_mode*/
        n[5] === "focus"
      ), P(
        e,
        "border_contrast",
        /*border_mode*/
        n[5] === "contrast"
      ), P(e, "hide-container", !/*explicit_call*/
      n[8] && !/*container*/
      n[9]), V(
        e,
        "height",
        /*get_dimension*/
        n[15](
          /*height*/
          n[0]
        )
      ), V(e, "width", typeof /*width*/
      n[1] == "number" ? `calc(min(${/*width*/
      n[1]}px, 100%))` : (
        /*get_dimension*/
        n[15](
          /*width*/
          n[1]
        )
      )), V(
        e,
        "border-style",
        /*variant*/
        n[4]
      ), V(
        e,
        "overflow",
        /*allow_overflow*/
        n[11] ? "visible" : "hidden"
      ), V(
        e,
        "flex-grow",
        /*scale*/
        n[12]
      ), V(e, "min-width", `calc(min(${/*min_width*/
      n[13]}px, 100%))`), V(e, "border-width", "var(--block-border-width)");
    },
    m(r, _) {
      vt(r, e, _), i && i.m(e, null), l = !0;
    },
    p(r, _) {
      i && i.p && (!l || _ & /*$$scope*/
      131072) && Ft(
        i,
        s,
        r,
        /*$$scope*/
        r[17],
        l ? pt(
          s,
          /*$$scope*/
          r[17],
          _,
          null
        ) : wt(
          /*$$scope*/
          r[17]
        ),
        null
      ), Ce(
        /*tag*/
        r[14]
      )(e, o = kt(f, [
        (!l || _ & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          r[7]
        ) },
        (!l || _ & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          r[2]
        ) },
        (!l || _ & /*elem_classes*/
        8 && t !== (t = "block " + /*elem_classes*/
        r[3].join(" ") + " svelte-nl1om8")) && { class: t }
      ])), P(
        e,
        "hidden",
        /*visible*/
        r[10] === !1
      ), P(
        e,
        "padded",
        /*padding*/
        r[6]
      ), P(
        e,
        "border_focus",
        /*border_mode*/
        r[5] === "focus"
      ), P(
        e,
        "border_contrast",
        /*border_mode*/
        r[5] === "contrast"
      ), P(e, "hide-container", !/*explicit_call*/
      r[8] && !/*container*/
      r[9]), _ & /*height*/
      1 && V(
        e,
        "height",
        /*get_dimension*/
        r[15](
          /*height*/
          r[0]
        )
      ), _ & /*width*/
      2 && V(e, "width", typeof /*width*/
      r[1] == "number" ? `calc(min(${/*width*/
      r[1]}px, 100%))` : (
        /*get_dimension*/
        r[15](
          /*width*/
          r[1]
        )
      )), _ & /*variant*/
      16 && V(
        e,
        "border-style",
        /*variant*/
        r[4]
      ), _ & /*allow_overflow*/
      2048 && V(
        e,
        "overflow",
        /*allow_overflow*/
        r[11] ? "visible" : "hidden"
      ), _ & /*scale*/
      4096 && V(
        e,
        "flex-grow",
        /*scale*/
        r[12]
      ), _ & /*min_width*/
      8192 && V(e, "min-width", `calc(min(${/*min_width*/
      r[13]}px, 100%))`);
    },
    i(r) {
      l || (lt(i, r), l = !0);
    },
    o(r) {
      nt(i, r), l = !1;
    },
    d(r) {
      r && gt(e), i && i.d(r);
    }
  };
}
function Lt(n) {
  let e, t = (
    /*tag*/
    n[14] && Ct(n)
  );
  return {
    c() {
      t && t.c();
    },
    m(l, s) {
      t && t.m(l, s), e = !0;
    },
    p(l, [s]) {
      /*tag*/
      l[14] && t.p(l, s);
    },
    i(l) {
      e || (lt(t, l), e = !0);
    },
    o(l) {
      nt(t, l), e = !1;
    },
    d(l) {
      t && t.d(l);
    }
  };
}
function jt(n, e, t) {
  let { $$slots: l = {}, $$scope: s } = e, { height: i = void 0 } = e, { width: f = void 0 } = e, { elem_id: o = "" } = e, { elem_classes: r = [] } = e, { variant: _ = "solid" } = e, { border_mode: a = "base" } = e, { padding: c = !0 } = e, { type: m = "normal" } = e, { test_id: b = void 0 } = e, { explicit_call: p = !1 } = e, { container: C = !0 } = e, { visible: F = !0 } = e, { allow_overflow: L = !0 } = e, { scale: v = null } = e, { min_width: d = 0 } = e, y = m === "fieldset" ? "fieldset" : "div";
  const S = (u) => {
    if (u !== void 0) {
      if (typeof u == "number")
        return u + "px";
      if (typeof u == "string")
        return u;
    }
  };
  return n.$$set = (u) => {
    "height" in u && t(0, i = u.height), "width" in u && t(1, f = u.width), "elem_id" in u && t(2, o = u.elem_id), "elem_classes" in u && t(3, r = u.elem_classes), "variant" in u && t(4, _ = u.variant), "border_mode" in u && t(5, a = u.border_mode), "padding" in u && t(6, c = u.padding), "type" in u && t(16, m = u.type), "test_id" in u && t(7, b = u.test_id), "explicit_call" in u && t(8, p = u.explicit_call), "container" in u && t(9, C = u.container), "visible" in u && t(10, F = u.visible), "allow_overflow" in u && t(11, L = u.allow_overflow), "scale" in u && t(12, v = u.scale), "min_width" in u && t(13, d = u.min_width), "$$scope" in u && t(17, s = u.$$scope);
  }, [
    i,
    f,
    o,
    r,
    _,
    a,
    c,
    b,
    p,
    C,
    F,
    L,
    v,
    d,
    y,
    S,
    m,
    s,
    l
  ];
}
class St extends dt {
  constructor(e) {
    super(), yt(this, e, jt, Lt, qt, {
      height: 0,
      width: 1,
      elem_id: 2,
      elem_classes: 3,
      variant: 4,
      border_mode: 5,
      padding: 6,
      type: 16,
      test_id: 7,
      explicit_call: 8,
      container: 9,
      visible: 10,
      allow_overflow: 11,
      scale: 12,
      min_width: 13
    });
  }
}
const {
  SvelteComponent: Vt,
  attr: Mt,
  create_slot: Nt,
  detach: zt,
  element: Tt,
  get_all_dirty_from_scope: Pt,
  get_slot_changes: Zt,
  init: Bt,
  insert: At,
  safe_not_equal: Dt,
  transition_in: It,
  transition_out: Et,
  update_slot_base: Xt
} = window.__gradio__svelte__internal;
function Yt(n) {
  let e, t;
  const l = (
    /*#slots*/
    n[1].default
  ), s = Nt(
    l,
    n,
    /*$$scope*/
    n[0],
    null
  );
  return {
    c() {
      e = Tt("div"), s && s.c(), Mt(e, "class", "svelte-1hnfib2");
    },
    m(i, f) {
      At(i, e, f), s && s.m(e, null), t = !0;
    },
    p(i, [f]) {
      s && s.p && (!t || f & /*$$scope*/
      1) && Xt(
        s,
        l,
        i,
        /*$$scope*/
        i[0],
        t ? Zt(
          l,
          /*$$scope*/
          i[0],
          f,
          null
        ) : Pt(
          /*$$scope*/
          i[0]
        ),
        null
      );
    },
    i(i) {
      t || (It(s, i), t = !0);
    },
    o(i) {
      Et(s, i), t = !1;
    },
    d(i) {
      i && zt(e), s && s.d(i);
    }
  };
}
function Gt(n, e, t) {
  let { $$slots: l = {}, $$scope: s } = e;
  return n.$$set = (i) => {
    "$$scope" in i && t(0, s = i.$$scope);
  }, [s, l];
}
class Ot extends Vt {
  constructor(e) {
    super(), Bt(this, e, Gt, Yt, Dt, {});
  }
}
const {
  SvelteComponent: Rt,
  attr: Le,
  check_outros: Ut,
  create_component: Ht,
  create_slot: Jt,
  destroy_component: Kt,
  detach: re,
  element: Qt,
  empty: Wt,
  get_all_dirty_from_scope: xt,
  get_slot_changes: $t,
  group_outros: el,
  init: tl,
  insert: _e,
  mount_component: ll,
  safe_not_equal: nl,
  set_data: il,
  space: sl,
  text: fl,
  toggle_class: U,
  transition_in: le,
  transition_out: ae,
  update_slot_base: ol
} = window.__gradio__svelte__internal;
function je(n) {
  let e, t;
  return e = new Ot({
    props: {
      $$slots: { default: [rl] },
      $$scope: { ctx: n }
    }
  }), {
    c() {
      Ht(e.$$.fragment);
    },
    m(l, s) {
      ll(e, l, s), t = !0;
    },
    p(l, s) {
      const i = {};
      s & /*$$scope, info*/
      10 && (i.$$scope = { dirty: s, ctx: l }), e.$set(i);
    },
    i(l) {
      t || (le(e.$$.fragment, l), t = !0);
    },
    o(l) {
      ae(e.$$.fragment, l), t = !1;
    },
    d(l) {
      Kt(e, l);
    }
  };
}
function rl(n) {
  let e;
  return {
    c() {
      e = fl(
        /*info*/
        n[1]
      );
    },
    m(t, l) {
      _e(t, e, l);
    },
    p(t, l) {
      l & /*info*/
      2 && il(
        e,
        /*info*/
        t[1]
      );
    },
    d(t) {
      t && re(e);
    }
  };
}
function _l(n) {
  let e, t, l, s;
  const i = (
    /*#slots*/
    n[2].default
  ), f = Jt(
    i,
    n,
    /*$$scope*/
    n[3],
    null
  );
  let o = (
    /*info*/
    n[1] && je(n)
  );
  return {
    c() {
      e = Qt("span"), f && f.c(), t = sl(), o && o.c(), l = Wt(), Le(e, "data-testid", "block-info"), Le(e, "class", "svelte-22c38v"), U(e, "sr-only", !/*show_label*/
      n[0]), U(e, "hide", !/*show_label*/
      n[0]), U(
        e,
        "has-info",
        /*info*/
        n[1] != null
      );
    },
    m(r, _) {
      _e(r, e, _), f && f.m(e, null), _e(r, t, _), o && o.m(r, _), _e(r, l, _), s = !0;
    },
    p(r, [_]) {
      f && f.p && (!s || _ & /*$$scope*/
      8) && ol(
        f,
        i,
        r,
        /*$$scope*/
        r[3],
        s ? $t(
          i,
          /*$$scope*/
          r[3],
          _,
          null
        ) : xt(
          /*$$scope*/
          r[3]
        ),
        null
      ), (!s || _ & /*show_label*/
      1) && U(e, "sr-only", !/*show_label*/
      r[0]), (!s || _ & /*show_label*/
      1) && U(e, "hide", !/*show_label*/
      r[0]), (!s || _ & /*info*/
      2) && U(
        e,
        "has-info",
        /*info*/
        r[1] != null
      ), /*info*/
      r[1] ? o ? (o.p(r, _), _ & /*info*/
      2 && le(o, 1)) : (o = je(r), o.c(), le(o, 1), o.m(l.parentNode, l)) : o && (el(), ae(o, 1, 1, () => {
        o = null;
      }), Ut());
    },
    i(r) {
      s || (le(f, r), le(o), s = !0);
    },
    o(r) {
      ae(f, r), ae(o), s = !1;
    },
    d(r) {
      r && (re(e), re(t), re(l)), f && f.d(r), o && o.d(r);
    }
  };
}
function al(n, e, t) {
  let { $$slots: l = {}, $$scope: s } = e, { show_label: i = !0 } = e, { info: f = void 0 } = e;
  return n.$$set = (o) => {
    "show_label" in o && t(0, i = o.show_label), "info" in o && t(1, f = o.info), "$$scope" in o && t(3, s = o.$$scope);
  }, [i, f, l, s];
}
class ul extends Rt {
  constructor(e) {
    super(), tl(this, e, al, _l, nl, { show_label: 0, info: 1 });
  }
}
const cl = [
  { color: "red", primary: 600, secondary: 100 },
  { color: "green", primary: 600, secondary: 100 },
  { color: "blue", primary: 600, secondary: 100 },
  { color: "yellow", primary: 500, secondary: 100 },
  { color: "purple", primary: 600, secondary: 100 },
  { color: "teal", primary: 600, secondary: 100 },
  { color: "orange", primary: 600, secondary: 100 },
  { color: "cyan", primary: 600, secondary: 100 },
  { color: "lime", primary: 500, secondary: 100 },
  { color: "pink", primary: 600, secondary: 100 }
], Se = {
  inherit: "inherit",
  current: "currentColor",
  transparent: "transparent",
  black: "#000",
  white: "#fff",
  slate: {
    50: "#f8fafc",
    100: "#f1f5f9",
    200: "#e2e8f0",
    300: "#cbd5e1",
    400: "#94a3b8",
    500: "#64748b",
    600: "#475569",
    700: "#334155",
    800: "#1e293b",
    900: "#0f172a",
    950: "#020617"
  },
  gray: {
    50: "#f9fafb",
    100: "#f3f4f6",
    200: "#e5e7eb",
    300: "#d1d5db",
    400: "#9ca3af",
    500: "#6b7280",
    600: "#4b5563",
    700: "#374151",
    800: "#1f2937",
    900: "#111827",
    950: "#030712"
  },
  zinc: {
    50: "#fafafa",
    100: "#f4f4f5",
    200: "#e4e4e7",
    300: "#d4d4d8",
    400: "#a1a1aa",
    500: "#71717a",
    600: "#52525b",
    700: "#3f3f46",
    800: "#27272a",
    900: "#18181b",
    950: "#09090b"
  },
  neutral: {
    50: "#fafafa",
    100: "#f5f5f5",
    200: "#e5e5e5",
    300: "#d4d4d4",
    400: "#a3a3a3",
    500: "#737373",
    600: "#525252",
    700: "#404040",
    800: "#262626",
    900: "#171717",
    950: "#0a0a0a"
  },
  stone: {
    50: "#fafaf9",
    100: "#f5f5f4",
    200: "#e7e5e4",
    300: "#d6d3d1",
    400: "#a8a29e",
    500: "#78716c",
    600: "#57534e",
    700: "#44403c",
    800: "#292524",
    900: "#1c1917",
    950: "#0c0a09"
  },
  red: {
    50: "#fef2f2",
    100: "#fee2e2",
    200: "#fecaca",
    300: "#fca5a5",
    400: "#f87171",
    500: "#ef4444",
    600: "#dc2626",
    700: "#b91c1c",
    800: "#991b1b",
    900: "#7f1d1d",
    950: "#450a0a"
  },
  orange: {
    50: "#fff7ed",
    100: "#ffedd5",
    200: "#fed7aa",
    300: "#fdba74",
    400: "#fb923c",
    500: "#f97316",
    600: "#ea580c",
    700: "#c2410c",
    800: "#9a3412",
    900: "#7c2d12",
    950: "#431407"
  },
  amber: {
    50: "#fffbeb",
    100: "#fef3c7",
    200: "#fde68a",
    300: "#fcd34d",
    400: "#fbbf24",
    500: "#f59e0b",
    600: "#d97706",
    700: "#b45309",
    800: "#92400e",
    900: "#78350f",
    950: "#451a03"
  },
  yellow: {
    50: "#fefce8",
    100: "#fef9c3",
    200: "#fef08a",
    300: "#fde047",
    400: "#facc15",
    500: "#eab308",
    600: "#ca8a04",
    700: "#a16207",
    800: "#854d0e",
    900: "#713f12",
    950: "#422006"
  },
  lime: {
    50: "#f7fee7",
    100: "#ecfccb",
    200: "#d9f99d",
    300: "#bef264",
    400: "#a3e635",
    500: "#84cc16",
    600: "#65a30d",
    700: "#4d7c0f",
    800: "#3f6212",
    900: "#365314",
    950: "#1a2e05"
  },
  green: {
    50: "#f0fdf4",
    100: "#dcfce7",
    200: "#bbf7d0",
    300: "#86efac",
    400: "#4ade80",
    500: "#22c55e",
    600: "#16a34a",
    700: "#15803d",
    800: "#166534",
    900: "#14532d",
    950: "#052e16"
  },
  emerald: {
    50: "#ecfdf5",
    100: "#d1fae5",
    200: "#a7f3d0",
    300: "#6ee7b7",
    400: "#34d399",
    500: "#10b981",
    600: "#059669",
    700: "#047857",
    800: "#065f46",
    900: "#064e3b",
    950: "#022c22"
  },
  teal: {
    50: "#f0fdfa",
    100: "#ccfbf1",
    200: "#99f6e4",
    300: "#5eead4",
    400: "#2dd4bf",
    500: "#14b8a6",
    600: "#0d9488",
    700: "#0f766e",
    800: "#115e59",
    900: "#134e4a",
    950: "#042f2e"
  },
  cyan: {
    50: "#ecfeff",
    100: "#cffafe",
    200: "#a5f3fc",
    300: "#67e8f9",
    400: "#22d3ee",
    500: "#06b6d4",
    600: "#0891b2",
    700: "#0e7490",
    800: "#155e75",
    900: "#164e63",
    950: "#083344"
  },
  sky: {
    50: "#f0f9ff",
    100: "#e0f2fe",
    200: "#bae6fd",
    300: "#7dd3fc",
    400: "#38bdf8",
    500: "#0ea5e9",
    600: "#0284c7",
    700: "#0369a1",
    800: "#075985",
    900: "#0c4a6e",
    950: "#082f49"
  },
  blue: {
    50: "#eff6ff",
    100: "#dbeafe",
    200: "#bfdbfe",
    300: "#93c5fd",
    400: "#60a5fa",
    500: "#3b82f6",
    600: "#2563eb",
    700: "#1d4ed8",
    800: "#1e40af",
    900: "#1e3a8a",
    950: "#172554"
  },
  indigo: {
    50: "#eef2ff",
    100: "#e0e7ff",
    200: "#c7d2fe",
    300: "#a5b4fc",
    400: "#818cf8",
    500: "#6366f1",
    600: "#4f46e5",
    700: "#4338ca",
    800: "#3730a3",
    900: "#312e81",
    950: "#1e1b4b"
  },
  violet: {
    50: "#f5f3ff",
    100: "#ede9fe",
    200: "#ddd6fe",
    300: "#c4b5fd",
    400: "#a78bfa",
    500: "#8b5cf6",
    600: "#7c3aed",
    700: "#6d28d9",
    800: "#5b21b6",
    900: "#4c1d95",
    950: "#2e1065"
  },
  purple: {
    50: "#faf5ff",
    100: "#f3e8ff",
    200: "#e9d5ff",
    300: "#d8b4fe",
    400: "#c084fc",
    500: "#a855f7",
    600: "#9333ea",
    700: "#7e22ce",
    800: "#6b21a8",
    900: "#581c87",
    950: "#3b0764"
  },
  fuchsia: {
    50: "#fdf4ff",
    100: "#fae8ff",
    200: "#f5d0fe",
    300: "#f0abfc",
    400: "#e879f9",
    500: "#d946ef",
    600: "#c026d3",
    700: "#a21caf",
    800: "#86198f",
    900: "#701a75",
    950: "#4a044e"
  },
  pink: {
    50: "#fdf2f8",
    100: "#fce7f3",
    200: "#fbcfe8",
    300: "#f9a8d4",
    400: "#f472b6",
    500: "#ec4899",
    600: "#db2777",
    700: "#be185d",
    800: "#9d174d",
    900: "#831843",
    950: "#500724"
  },
  rose: {
    50: "#fff1f2",
    100: "#ffe4e6",
    200: "#fecdd3",
    300: "#fda4af",
    400: "#fb7185",
    500: "#f43f5e",
    600: "#e11d48",
    700: "#be123c",
    800: "#9f1239",
    900: "#881337",
    950: "#4c0519"
  }
};
cl.reduce(
  (n, { color: e, primary: t, secondary: l }) => ({
    ...n,
    [e]: {
      primary: Se[e][t],
      secondary: Se[e][l]
    }
  }),
  {}
);
function J(n) {
  let e = ["", "k", "M", "G", "T", "P", "E", "Z"], t = 0;
  for (; n > 1e3 && t < e.length - 1; )
    n /= 1e3, t++;
  let l = e[t];
  return (Number.isInteger(n) ? n : n.toFixed(1)) + l;
}
function ue() {
}
function dl(n, e) {
  return n != n ? e == e : n !== e || n && typeof n == "object" || typeof n == "function";
}
const it = typeof window < "u";
let Ve = it ? () => window.performance.now() : () => Date.now(), st = it ? (n) => requestAnimationFrame(n) : ue;
const Q = /* @__PURE__ */ new Set();
function ft(n) {
  Q.forEach((e) => {
    e.c(n) || (Q.delete(e), e.f());
  }), Q.size !== 0 && st(ft);
}
function ml(n) {
  let e;
  return Q.size === 0 && st(ft), {
    promise: new Promise((t) => {
      Q.add(e = { c: n, f: t });
    }),
    abort() {
      Q.delete(e);
    }
  };
}
const H = [];
function bl(n, e = ue) {
  let t;
  const l = /* @__PURE__ */ new Set();
  function s(o) {
    if (dl(n, o) && (n = o, t)) {
      const r = !H.length;
      for (const _ of l)
        _[1](), H.push(_, n);
      if (r) {
        for (let _ = 0; _ < H.length; _ += 2)
          H[_][0](H[_ + 1]);
        H.length = 0;
      }
    }
  }
  function i(o) {
    s(o(n));
  }
  function f(o, r = ue) {
    const _ = [o, r];
    return l.add(_), l.size === 1 && (t = e(s, i) || ue), o(n), () => {
      l.delete(_), l.size === 0 && t && (t(), t = null);
    };
  }
  return { set: s, update: i, subscribe: f };
}
function Me(n) {
  return Object.prototype.toString.call(n) === "[object Date]";
}
function me(n, e, t, l) {
  if (typeof t == "number" || Me(t)) {
    const s = l - t, i = (t - e) / (n.dt || 1 / 60), f = n.opts.stiffness * s, o = n.opts.damping * i, r = (f - o) * n.inv_mass, _ = (i + r) * n.dt;
    return Math.abs(_) < n.opts.precision && Math.abs(s) < n.opts.precision ? l : (n.settled = !1, Me(t) ? new Date(t.getTime() + _) : t + _);
  } else {
    if (Array.isArray(t))
      return t.map(
        (s, i) => me(n, e[i], t[i], l[i])
      );
    if (typeof t == "object") {
      const s = {};
      for (const i in t)
        s[i] = me(n, e[i], t[i], l[i]);
      return s;
    } else
      throw new Error(`Cannot spring ${typeof t} values`);
  }
}
function Ne(n, e = {}) {
  const t = bl(n), { stiffness: l = 0.15, damping: s = 0.8, precision: i = 0.01 } = e;
  let f, o, r, _ = n, a = n, c = 1, m = 0, b = !1;
  function p(F, L = {}) {
    a = F;
    const v = r = {};
    return n == null || L.hard || C.stiffness >= 1 && C.damping >= 1 ? (b = !0, f = Ve(), _ = F, t.set(n = a), Promise.resolve()) : (L.soft && (m = 1 / ((L.soft === !0 ? 0.5 : +L.soft) * 60), c = 0), o || (f = Ve(), b = !1, o = ml((d) => {
      if (b)
        return b = !1, o = null, !1;
      c = Math.min(c + m, 1);
      const y = {
        inv_mass: c,
        opts: C,
        settled: !0,
        dt: (d - f) * 60 / 1e3
      }, S = me(y, _, n, a);
      return f = d, _ = n, t.set(n = S), y.settled && (o = null), !y.settled;
    })), new Promise((d) => {
      o.promise.then(() => {
        v === r && d();
      });
    }));
  }
  const C = {
    set: p,
    update: (F, L) => p(F(a, n), L),
    subscribe: t.subscribe,
    stiffness: l,
    damping: s,
    precision: i
  };
  return C;
}
const {
  SvelteComponent: gl,
  append: z,
  attr: k,
  component_subscribe: ze,
  detach: hl,
  element: wl,
  init: pl,
  insert: kl,
  noop: Te,
  safe_not_equal: yl,
  set_style: fe,
  svg_element: T,
  toggle_class: Pe
} = window.__gradio__svelte__internal, { onMount: vl } = window.__gradio__svelte__internal;
function ql(n) {
  let e, t, l, s, i, f, o, r, _, a, c, m;
  return {
    c() {
      e = wl("div"), t = T("svg"), l = T("g"), s = T("path"), i = T("path"), f = T("path"), o = T("path"), r = T("g"), _ = T("path"), a = T("path"), c = T("path"), m = T("path"), k(s, "d", "M255.926 0.754768L509.702 139.936V221.027L255.926 81.8465V0.754768Z"), k(s, "fill", "#FF7C00"), k(s, "fill-opacity", "0.4"), k(s, "class", "svelte-43sxxs"), k(i, "d", "M509.69 139.936L254.981 279.641V361.255L509.69 221.55V139.936Z"), k(i, "fill", "#FF7C00"), k(i, "class", "svelte-43sxxs"), k(f, "d", "M0.250138 139.937L254.981 279.641V361.255L0.250138 221.55V139.937Z"), k(f, "fill", "#FF7C00"), k(f, "fill-opacity", "0.4"), k(f, "class", "svelte-43sxxs"), k(o, "d", "M255.923 0.232622L0.236328 139.936V221.55L255.923 81.8469V0.232622Z"), k(o, "fill", "#FF7C00"), k(o, "class", "svelte-43sxxs"), fe(l, "transform", "translate(" + /*$top*/
      n[1][0] + "px, " + /*$top*/
      n[1][1] + "px)"), k(_, "d", "M255.926 141.5L509.702 280.681V361.773L255.926 222.592V141.5Z"), k(_, "fill", "#FF7C00"), k(_, "fill-opacity", "0.4"), k(_, "class", "svelte-43sxxs"), k(a, "d", "M509.69 280.679L254.981 420.384V501.998L509.69 362.293V280.679Z"), k(a, "fill", "#FF7C00"), k(a, "class", "svelte-43sxxs"), k(c, "d", "M0.250138 280.681L254.981 420.386V502L0.250138 362.295V280.681Z"), k(c, "fill", "#FF7C00"), k(c, "fill-opacity", "0.4"), k(c, "class", "svelte-43sxxs"), k(m, "d", "M255.923 140.977L0.236328 280.68V362.294L255.923 222.591V140.977Z"), k(m, "fill", "#FF7C00"), k(m, "class", "svelte-43sxxs"), fe(r, "transform", "translate(" + /*$bottom*/
      n[2][0] + "px, " + /*$bottom*/
      n[2][1] + "px)"), k(t, "viewBox", "-1200 -1200 3000 3000"), k(t, "fill", "none"), k(t, "xmlns", "http://www.w3.org/2000/svg"), k(t, "class", "svelte-43sxxs"), k(e, "class", "svelte-43sxxs"), Pe(
        e,
        "margin",
        /*margin*/
        n[0]
      );
    },
    m(b, p) {
      kl(b, e, p), z(e, t), z(t, l), z(l, s), z(l, i), z(l, f), z(l, o), z(t, r), z(r, _), z(r, a), z(r, c), z(r, m);
    },
    p(b, [p]) {
      p & /*$top*/
      2 && fe(l, "transform", "translate(" + /*$top*/
      b[1][0] + "px, " + /*$top*/
      b[1][1] + "px)"), p & /*$bottom*/
      4 && fe(r, "transform", "translate(" + /*$bottom*/
      b[2][0] + "px, " + /*$bottom*/
      b[2][1] + "px)"), p & /*margin*/
      1 && Pe(
        e,
        "margin",
        /*margin*/
        b[0]
      );
    },
    i: Te,
    o: Te,
    d(b) {
      b && hl(e);
    }
  };
}
function Fl(n, e, t) {
  let l, s, { margin: i = !0 } = e;
  const f = Ne([0, 0]);
  ze(n, f, (m) => t(1, l = m));
  const o = Ne([0, 0]);
  ze(n, o, (m) => t(2, s = m));
  let r;
  async function _() {
    await Promise.all([f.set([125, 140]), o.set([-125, -140])]), await Promise.all([f.set([-125, 140]), o.set([125, -140])]), await Promise.all([f.set([-125, 0]), o.set([125, -0])]), await Promise.all([f.set([125, 0]), o.set([-125, 0])]);
  }
  async function a() {
    await _(), r || a();
  }
  async function c() {
    await Promise.all([f.set([125, 0]), o.set([-125, 0])]), a();
  }
  return vl(() => (c(), () => r = !0)), n.$$set = (m) => {
    "margin" in m && t(0, i = m.margin);
  }, [i, l, s, f, o];
}
class Cl extends gl {
  constructor(e) {
    super(), pl(this, e, Fl, ql, yl, { margin: 0 });
  }
}
const {
  SvelteComponent: Ll,
  append: G,
  attr: Z,
  binding_callbacks: Ze,
  check_outros: ot,
  create_component: jl,
  create_slot: Sl,
  destroy_component: Vl,
  destroy_each: rt,
  detach: h,
  element: A,
  empty: $,
  ensure_array_like: ce,
  get_all_dirty_from_scope: Ml,
  get_slot_changes: Nl,
  group_outros: _t,
  init: zl,
  insert: w,
  mount_component: Tl,
  noop: be,
  safe_not_equal: Pl,
  set_data: N,
  set_style: E,
  space: B,
  text: q,
  toggle_class: M,
  transition_in: W,
  transition_out: x,
  update_slot_base: Zl
} = window.__gradio__svelte__internal, { tick: Bl } = window.__gradio__svelte__internal, { onDestroy: Al } = window.__gradio__svelte__internal, Dl = (n) => ({}), Be = (n) => ({});
function Ae(n, e, t) {
  const l = n.slice();
  return l[38] = e[t], l[40] = t, l;
}
function De(n, e, t) {
  const l = n.slice();
  return l[38] = e[t], l;
}
function Il(n) {
  let e, t = (
    /*i18n*/
    n[1]("common.error") + ""
  ), l, s, i;
  const f = (
    /*#slots*/
    n[29].error
  ), o = Sl(
    f,
    n,
    /*$$scope*/
    n[28],
    Be
  );
  return {
    c() {
      e = A("span"), l = q(t), s = B(), o && o.c(), Z(e, "class", "error svelte-1yserjw");
    },
    m(r, _) {
      w(r, e, _), G(e, l), w(r, s, _), o && o.m(r, _), i = !0;
    },
    p(r, _) {
      (!i || _[0] & /*i18n*/
      2) && t !== (t = /*i18n*/
      r[1]("common.error") + "") && N(l, t), o && o.p && (!i || _[0] & /*$$scope*/
      268435456) && Zl(
        o,
        f,
        r,
        /*$$scope*/
        r[28],
        i ? Nl(
          f,
          /*$$scope*/
          r[28],
          _,
          Dl
        ) : Ml(
          /*$$scope*/
          r[28]
        ),
        Be
      );
    },
    i(r) {
      i || (W(o, r), i = !0);
    },
    o(r) {
      x(o, r), i = !1;
    },
    d(r) {
      r && (h(e), h(s)), o && o.d(r);
    }
  };
}
function El(n) {
  let e, t, l, s, i, f, o, r, _, a = (
    /*variant*/
    n[8] === "default" && /*show_eta_bar*/
    n[18] && /*show_progress*/
    n[6] === "full" && Ie(n)
  );
  function c(d, y) {
    if (
      /*progress*/
      d[7]
    )
      return Gl;
    if (
      /*queue_position*/
      d[2] !== null && /*queue_size*/
      d[3] !== void 0 && /*queue_position*/
      d[2] >= 0
    )
      return Yl;
    if (
      /*queue_position*/
      d[2] === 0
    )
      return Xl;
  }
  let m = c(n), b = m && m(n), p = (
    /*timer*/
    n[5] && Ye(n)
  );
  const C = [Hl, Ul], F = [];
  function L(d, y) {
    return (
      /*last_progress_level*/
      d[15] != null ? 0 : (
        /*show_progress*/
        d[6] === "full" ? 1 : -1
      )
    );
  }
  ~(i = L(n)) && (f = F[i] = C[i](n));
  let v = !/*timer*/
  n[5] && Ke(n);
  return {
    c() {
      a && a.c(), e = B(), t = A("div"), b && b.c(), l = B(), p && p.c(), s = B(), f && f.c(), o = B(), v && v.c(), r = $(), Z(t, "class", "progress-text svelte-1yserjw"), M(
        t,
        "meta-text-center",
        /*variant*/
        n[8] === "center"
      ), M(
        t,
        "meta-text",
        /*variant*/
        n[8] === "default"
      );
    },
    m(d, y) {
      a && a.m(d, y), w(d, e, y), w(d, t, y), b && b.m(t, null), G(t, l), p && p.m(t, null), w(d, s, y), ~i && F[i].m(d, y), w(d, o, y), v && v.m(d, y), w(d, r, y), _ = !0;
    },
    p(d, y) {
      /*variant*/
      d[8] === "default" && /*show_eta_bar*/
      d[18] && /*show_progress*/
      d[6] === "full" ? a ? a.p(d, y) : (a = Ie(d), a.c(), a.m(e.parentNode, e)) : a && (a.d(1), a = null), m === (m = c(d)) && b ? b.p(d, y) : (b && b.d(1), b = m && m(d), b && (b.c(), b.m(t, l))), /*timer*/
      d[5] ? p ? p.p(d, y) : (p = Ye(d), p.c(), p.m(t, null)) : p && (p.d(1), p = null), (!_ || y[0] & /*variant*/
      256) && M(
        t,
        "meta-text-center",
        /*variant*/
        d[8] === "center"
      ), (!_ || y[0] & /*variant*/
      256) && M(
        t,
        "meta-text",
        /*variant*/
        d[8] === "default"
      );
      let S = i;
      i = L(d), i === S ? ~i && F[i].p(d, y) : (f && (_t(), x(F[S], 1, 1, () => {
        F[S] = null;
      }), ot()), ~i ? (f = F[i], f ? f.p(d, y) : (f = F[i] = C[i](d), f.c()), W(f, 1), f.m(o.parentNode, o)) : f = null), /*timer*/
      d[5] ? v && (v.d(1), v = null) : v ? v.p(d, y) : (v = Ke(d), v.c(), v.m(r.parentNode, r));
    },
    i(d) {
      _ || (W(f), _ = !0);
    },
    o(d) {
      x(f), _ = !1;
    },
    d(d) {
      d && (h(e), h(t), h(s), h(o), h(r)), a && a.d(d), b && b.d(), p && p.d(), ~i && F[i].d(d), v && v.d(d);
    }
  };
}
function Ie(n) {
  let e, t = `translateX(${/*eta_level*/
  (n[17] || 0) * 100 - 100}%)`;
  return {
    c() {
      e = A("div"), Z(e, "class", "eta-bar svelte-1yserjw"), E(e, "transform", t);
    },
    m(l, s) {
      w(l, e, s);
    },
    p(l, s) {
      s[0] & /*eta_level*/
      131072 && t !== (t = `translateX(${/*eta_level*/
      (l[17] || 0) * 100 - 100}%)`) && E(e, "transform", t);
    },
    d(l) {
      l && h(e);
    }
  };
}
function Xl(n) {
  let e;
  return {
    c() {
      e = q("processing |");
    },
    m(t, l) {
      w(t, e, l);
    },
    p: be,
    d(t) {
      t && h(e);
    }
  };
}
function Yl(n) {
  let e, t = (
    /*queue_position*/
    n[2] + 1 + ""
  ), l, s, i, f;
  return {
    c() {
      e = q("queue: "), l = q(t), s = q("/"), i = q(
        /*queue_size*/
        n[3]
      ), f = q(" |");
    },
    m(o, r) {
      w(o, e, r), w(o, l, r), w(o, s, r), w(o, i, r), w(o, f, r);
    },
    p(o, r) {
      r[0] & /*queue_position*/
      4 && t !== (t = /*queue_position*/
      o[2] + 1 + "") && N(l, t), r[0] & /*queue_size*/
      8 && N(
        i,
        /*queue_size*/
        o[3]
      );
    },
    d(o) {
      o && (h(e), h(l), h(s), h(i), h(f));
    }
  };
}
function Gl(n) {
  let e, t = ce(
    /*progress*/
    n[7]
  ), l = [];
  for (let s = 0; s < t.length; s += 1)
    l[s] = Xe(De(n, t, s));
  return {
    c() {
      for (let s = 0; s < l.length; s += 1)
        l[s].c();
      e = $();
    },
    m(s, i) {
      for (let f = 0; f < l.length; f += 1)
        l[f] && l[f].m(s, i);
      w(s, e, i);
    },
    p(s, i) {
      if (i[0] & /*progress*/
      128) {
        t = ce(
          /*progress*/
          s[7]
        );
        let f;
        for (f = 0; f < t.length; f += 1) {
          const o = De(s, t, f);
          l[f] ? l[f].p(o, i) : (l[f] = Xe(o), l[f].c(), l[f].m(e.parentNode, e));
        }
        for (; f < l.length; f += 1)
          l[f].d(1);
        l.length = t.length;
      }
    },
    d(s) {
      s && h(e), rt(l, s);
    }
  };
}
function Ee(n) {
  let e, t = (
    /*p*/
    n[38].unit + ""
  ), l, s, i = " ", f;
  function o(a, c) {
    return (
      /*p*/
      a[38].length != null ? Rl : Ol
    );
  }
  let r = o(n), _ = r(n);
  return {
    c() {
      _.c(), e = B(), l = q(t), s = q(" | "), f = q(i);
    },
    m(a, c) {
      _.m(a, c), w(a, e, c), w(a, l, c), w(a, s, c), w(a, f, c);
    },
    p(a, c) {
      r === (r = o(a)) && _ ? _.p(a, c) : (_.d(1), _ = r(a), _ && (_.c(), _.m(e.parentNode, e))), c[0] & /*progress*/
      128 && t !== (t = /*p*/
      a[38].unit + "") && N(l, t);
    },
    d(a) {
      a && (h(e), h(l), h(s), h(f)), _.d(a);
    }
  };
}
function Ol(n) {
  let e = J(
    /*p*/
    n[38].index || 0
  ) + "", t;
  return {
    c() {
      t = q(e);
    },
    m(l, s) {
      w(l, t, s);
    },
    p(l, s) {
      s[0] & /*progress*/
      128 && e !== (e = J(
        /*p*/
        l[38].index || 0
      ) + "") && N(t, e);
    },
    d(l) {
      l && h(t);
    }
  };
}
function Rl(n) {
  let e = J(
    /*p*/
    n[38].index || 0
  ) + "", t, l, s = J(
    /*p*/
    n[38].length
  ) + "", i;
  return {
    c() {
      t = q(e), l = q("/"), i = q(s);
    },
    m(f, o) {
      w(f, t, o), w(f, l, o), w(f, i, o);
    },
    p(f, o) {
      o[0] & /*progress*/
      128 && e !== (e = J(
        /*p*/
        f[38].index || 0
      ) + "") && N(t, e), o[0] & /*progress*/
      128 && s !== (s = J(
        /*p*/
        f[38].length
      ) + "") && N(i, s);
    },
    d(f) {
      f && (h(t), h(l), h(i));
    }
  };
}
function Xe(n) {
  let e, t = (
    /*p*/
    n[38].index != null && Ee(n)
  );
  return {
    c() {
      t && t.c(), e = $();
    },
    m(l, s) {
      t && t.m(l, s), w(l, e, s);
    },
    p(l, s) {
      /*p*/
      l[38].index != null ? t ? t.p(l, s) : (t = Ee(l), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(l) {
      l && h(e), t && t.d(l);
    }
  };
}
function Ye(n) {
  let e, t = (
    /*eta*/
    n[0] ? `/${/*formatted_eta*/
    n[19]}` : ""
  ), l, s;
  return {
    c() {
      e = q(
        /*formatted_timer*/
        n[20]
      ), l = q(t), s = q("s");
    },
    m(i, f) {
      w(i, e, f), w(i, l, f), w(i, s, f);
    },
    p(i, f) {
      f[0] & /*formatted_timer*/
      1048576 && N(
        e,
        /*formatted_timer*/
        i[20]
      ), f[0] & /*eta, formatted_eta*/
      524289 && t !== (t = /*eta*/
      i[0] ? `/${/*formatted_eta*/
      i[19]}` : "") && N(l, t);
    },
    d(i) {
      i && (h(e), h(l), h(s));
    }
  };
}
function Ul(n) {
  let e, t;
  return e = new Cl({
    props: { margin: (
      /*variant*/
      n[8] === "default"
    ) }
  }), {
    c() {
      jl(e.$$.fragment);
    },
    m(l, s) {
      Tl(e, l, s), t = !0;
    },
    p(l, s) {
      const i = {};
      s[0] & /*variant*/
      256 && (i.margin = /*variant*/
      l[8] === "default"), e.$set(i);
    },
    i(l) {
      t || (W(e.$$.fragment, l), t = !0);
    },
    o(l) {
      x(e.$$.fragment, l), t = !1;
    },
    d(l) {
      Vl(e, l);
    }
  };
}
function Hl(n) {
  let e, t, l, s, i, f = `${/*last_progress_level*/
  n[15] * 100}%`, o = (
    /*progress*/
    n[7] != null && Ge(n)
  );
  return {
    c() {
      e = A("div"), t = A("div"), o && o.c(), l = B(), s = A("div"), i = A("div"), Z(t, "class", "progress-level-inner svelte-1yserjw"), Z(i, "class", "progress-bar svelte-1yserjw"), E(i, "width", f), Z(s, "class", "progress-bar-wrap svelte-1yserjw"), Z(e, "class", "progress-level svelte-1yserjw");
    },
    m(r, _) {
      w(r, e, _), G(e, t), o && o.m(t, null), G(e, l), G(e, s), G(s, i), n[30](i);
    },
    p(r, _) {
      /*progress*/
      r[7] != null ? o ? o.p(r, _) : (o = Ge(r), o.c(), o.m(t, null)) : o && (o.d(1), o = null), _[0] & /*last_progress_level*/
      32768 && f !== (f = `${/*last_progress_level*/
      r[15] * 100}%`) && E(i, "width", f);
    },
    i: be,
    o: be,
    d(r) {
      r && h(e), o && o.d(), n[30](null);
    }
  };
}
function Ge(n) {
  let e, t = ce(
    /*progress*/
    n[7]
  ), l = [];
  for (let s = 0; s < t.length; s += 1)
    l[s] = Je(Ae(n, t, s));
  return {
    c() {
      for (let s = 0; s < l.length; s += 1)
        l[s].c();
      e = $();
    },
    m(s, i) {
      for (let f = 0; f < l.length; f += 1)
        l[f] && l[f].m(s, i);
      w(s, e, i);
    },
    p(s, i) {
      if (i[0] & /*progress_level, progress*/
      16512) {
        t = ce(
          /*progress*/
          s[7]
        );
        let f;
        for (f = 0; f < t.length; f += 1) {
          const o = Ae(s, t, f);
          l[f] ? l[f].p(o, i) : (l[f] = Je(o), l[f].c(), l[f].m(e.parentNode, e));
        }
        for (; f < l.length; f += 1)
          l[f].d(1);
        l.length = t.length;
      }
    },
    d(s) {
      s && h(e), rt(l, s);
    }
  };
}
function Oe(n) {
  let e, t, l, s, i = (
    /*i*/
    n[40] !== 0 && Jl()
  ), f = (
    /*p*/
    n[38].desc != null && Re(n)
  ), o = (
    /*p*/
    n[38].desc != null && /*progress_level*/
    n[14] && /*progress_level*/
    n[14][
      /*i*/
      n[40]
    ] != null && Ue()
  ), r = (
    /*progress_level*/
    n[14] != null && He(n)
  );
  return {
    c() {
      i && i.c(), e = B(), f && f.c(), t = B(), o && o.c(), l = B(), r && r.c(), s = $();
    },
    m(_, a) {
      i && i.m(_, a), w(_, e, a), f && f.m(_, a), w(_, t, a), o && o.m(_, a), w(_, l, a), r && r.m(_, a), w(_, s, a);
    },
    p(_, a) {
      /*p*/
      _[38].desc != null ? f ? f.p(_, a) : (f = Re(_), f.c(), f.m(t.parentNode, t)) : f && (f.d(1), f = null), /*p*/
      _[38].desc != null && /*progress_level*/
      _[14] && /*progress_level*/
      _[14][
        /*i*/
        _[40]
      ] != null ? o || (o = Ue(), o.c(), o.m(l.parentNode, l)) : o && (o.d(1), o = null), /*progress_level*/
      _[14] != null ? r ? r.p(_, a) : (r = He(_), r.c(), r.m(s.parentNode, s)) : r && (r.d(1), r = null);
    },
    d(_) {
      _ && (h(e), h(t), h(l), h(s)), i && i.d(_), f && f.d(_), o && o.d(_), r && r.d(_);
    }
  };
}
function Jl(n) {
  let e;
  return {
    c() {
      e = q(" /");
    },
    m(t, l) {
      w(t, e, l);
    },
    d(t) {
      t && h(e);
    }
  };
}
function Re(n) {
  let e = (
    /*p*/
    n[38].desc + ""
  ), t;
  return {
    c() {
      t = q(e);
    },
    m(l, s) {
      w(l, t, s);
    },
    p(l, s) {
      s[0] & /*progress*/
      128 && e !== (e = /*p*/
      l[38].desc + "") && N(t, e);
    },
    d(l) {
      l && h(t);
    }
  };
}
function Ue(n) {
  let e;
  return {
    c() {
      e = q("-");
    },
    m(t, l) {
      w(t, e, l);
    },
    d(t) {
      t && h(e);
    }
  };
}
function He(n) {
  let e = (100 * /*progress_level*/
  (n[14][
    /*i*/
    n[40]
  ] || 0)).toFixed(1) + "", t, l;
  return {
    c() {
      t = q(e), l = q("%");
    },
    m(s, i) {
      w(s, t, i), w(s, l, i);
    },
    p(s, i) {
      i[0] & /*progress_level*/
      16384 && e !== (e = (100 * /*progress_level*/
      (s[14][
        /*i*/
        s[40]
      ] || 0)).toFixed(1) + "") && N(t, e);
    },
    d(s) {
      s && (h(t), h(l));
    }
  };
}
function Je(n) {
  let e, t = (
    /*p*/
    (n[38].desc != null || /*progress_level*/
    n[14] && /*progress_level*/
    n[14][
      /*i*/
      n[40]
    ] != null) && Oe(n)
  );
  return {
    c() {
      t && t.c(), e = $();
    },
    m(l, s) {
      t && t.m(l, s), w(l, e, s);
    },
    p(l, s) {
      /*p*/
      l[38].desc != null || /*progress_level*/
      l[14] && /*progress_level*/
      l[14][
        /*i*/
        l[40]
      ] != null ? t ? t.p(l, s) : (t = Oe(l), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(l) {
      l && h(e), t && t.d(l);
    }
  };
}
function Ke(n) {
  let e, t;
  return {
    c() {
      e = A("p"), t = q(
        /*loading_text*/
        n[9]
      ), Z(e, "class", "loading svelte-1yserjw");
    },
    m(l, s) {
      w(l, e, s), G(e, t);
    },
    p(l, s) {
      s[0] & /*loading_text*/
      512 && N(
        t,
        /*loading_text*/
        l[9]
      );
    },
    d(l) {
      l && h(e);
    }
  };
}
function Kl(n) {
  let e, t, l, s, i;
  const f = [El, Il], o = [];
  function r(_, a) {
    return (
      /*status*/
      _[4] === "pending" ? 0 : (
        /*status*/
        _[4] === "error" ? 1 : -1
      )
    );
  }
  return ~(t = r(n)) && (l = o[t] = f[t](n)), {
    c() {
      e = A("div"), l && l.c(), Z(e, "class", s = "wrap " + /*variant*/
      n[8] + " " + /*show_progress*/
      n[6] + " svelte-1yserjw"), M(e, "hide", !/*status*/
      n[4] || /*status*/
      n[4] === "complete" || /*show_progress*/
      n[6] === "hidden"), M(
        e,
        "translucent",
        /*variant*/
        n[8] === "center" && /*status*/
        (n[4] === "pending" || /*status*/
        n[4] === "error") || /*translucent*/
        n[11] || /*show_progress*/
        n[6] === "minimal"
      ), M(
        e,
        "generating",
        /*status*/
        n[4] === "generating"
      ), M(
        e,
        "border",
        /*border*/
        n[12]
      ), E(
        e,
        "position",
        /*absolute*/
        n[10] ? "absolute" : "static"
      ), E(
        e,
        "padding",
        /*absolute*/
        n[10] ? "0" : "var(--size-8) 0"
      );
    },
    m(_, a) {
      w(_, e, a), ~t && o[t].m(e, null), n[31](e), i = !0;
    },
    p(_, a) {
      let c = t;
      t = r(_), t === c ? ~t && o[t].p(_, a) : (l && (_t(), x(o[c], 1, 1, () => {
        o[c] = null;
      }), ot()), ~t ? (l = o[t], l ? l.p(_, a) : (l = o[t] = f[t](_), l.c()), W(l, 1), l.m(e, null)) : l = null), (!i || a[0] & /*variant, show_progress*/
      320 && s !== (s = "wrap " + /*variant*/
      _[8] + " " + /*show_progress*/
      _[6] + " svelte-1yserjw")) && Z(e, "class", s), (!i || a[0] & /*variant, show_progress, status, show_progress*/
      336) && M(e, "hide", !/*status*/
      _[4] || /*status*/
      _[4] === "complete" || /*show_progress*/
      _[6] === "hidden"), (!i || a[0] & /*variant, show_progress, variant, status, translucent, show_progress*/
      2384) && M(
        e,
        "translucent",
        /*variant*/
        _[8] === "center" && /*status*/
        (_[4] === "pending" || /*status*/
        _[4] === "error") || /*translucent*/
        _[11] || /*show_progress*/
        _[6] === "minimal"
      ), (!i || a[0] & /*variant, show_progress, status*/
      336) && M(
        e,
        "generating",
        /*status*/
        _[4] === "generating"
      ), (!i || a[0] & /*variant, show_progress, border*/
      4416) && M(
        e,
        "border",
        /*border*/
        _[12]
      ), a[0] & /*absolute*/
      1024 && E(
        e,
        "position",
        /*absolute*/
        _[10] ? "absolute" : "static"
      ), a[0] & /*absolute*/
      1024 && E(
        e,
        "padding",
        /*absolute*/
        _[10] ? "0" : "var(--size-8) 0"
      );
    },
    i(_) {
      i || (W(l), i = !0);
    },
    o(_) {
      x(l), i = !1;
    },
    d(_) {
      _ && h(e), ~t && o[t].d(), n[31](null);
    }
  };
}
let oe = [], de = !1;
async function Ql(n, e = !0) {
  if (!(window.__gradio_mode__ === "website" || window.__gradio_mode__ !== "app" && e !== !0)) {
    if (oe.push(n), !de)
      de = !0;
    else
      return;
    await Bl(), requestAnimationFrame(() => {
      let t = [0, 0];
      for (let l = 0; l < oe.length; l++) {
        const i = oe[l].getBoundingClientRect();
        (l === 0 || i.top + window.scrollY <= t[0]) && (t[0] = i.top + window.scrollY, t[1] = l);
      }
      window.scrollTo({ top: t[0] - 20, behavior: "smooth" }), de = !1, oe = [];
    });
  }
}
function Wl(n, e, t) {
  let l, { $$slots: s = {}, $$scope: i } = e, { i18n: f } = e, { eta: o = null } = e, { queue_position: r } = e, { queue_size: _ } = e, { status: a } = e, { scroll_to_output: c = !1 } = e, { timer: m = !0 } = e, { show_progress: b = "full" } = e, { message: p = null } = e, { progress: C = null } = e, { variant: F = "default" } = e, { loading_text: L = "Loading..." } = e, { absolute: v = !0 } = e, { translucent: d = !1 } = e, { border: y = !1 } = e, { autoscroll: S } = e, u, ee = !1, ie = 0, X = 0, O = null, R = null, ye = 0, Y = null, te, D = null, ve = !0;
  const at = () => {
    t(0, o = t(26, O = t(19, se = null))), t(24, ie = performance.now()), t(25, X = 0), ee = !0, qe();
  };
  function qe() {
    requestAnimationFrame(() => {
      t(25, X = (performance.now() - ie) / 1e3), ee && qe();
    });
  }
  function Fe() {
    t(25, X = 0), t(0, o = t(26, O = t(19, se = null))), ee && (ee = !1);
  }
  Al(() => {
    ee && Fe();
  });
  let se = null;
  function ut(g) {
    Ze[g ? "unshift" : "push"](() => {
      D = g, t(16, D), t(7, C), t(14, Y), t(15, te);
    });
  }
  function ct(g) {
    Ze[g ? "unshift" : "push"](() => {
      u = g, t(13, u);
    });
  }
  return n.$$set = (g) => {
    "i18n" in g && t(1, f = g.i18n), "eta" in g && t(0, o = g.eta), "queue_position" in g && t(2, r = g.queue_position), "queue_size" in g && t(3, _ = g.queue_size), "status" in g && t(4, a = g.status), "scroll_to_output" in g && t(21, c = g.scroll_to_output), "timer" in g && t(5, m = g.timer), "show_progress" in g && t(6, b = g.show_progress), "message" in g && t(22, p = g.message), "progress" in g && t(7, C = g.progress), "variant" in g && t(8, F = g.variant), "loading_text" in g && t(9, L = g.loading_text), "absolute" in g && t(10, v = g.absolute), "translucent" in g && t(11, d = g.translucent), "border" in g && t(12, y = g.border), "autoscroll" in g && t(23, S = g.autoscroll), "$$scope" in g && t(28, i = g.$$scope);
  }, n.$$.update = () => {
    n.$$.dirty[0] & /*eta, old_eta, timer_start, eta_from_start*/
    218103809 && (o === null && t(0, o = O), o != null && O !== o && (t(27, R = (performance.now() - ie) / 1e3 + o), t(19, se = R.toFixed(1)), t(26, O = o))), n.$$.dirty[0] & /*eta_from_start, timer_diff*/
    167772160 && t(17, ye = R === null || R <= 0 || !X ? null : Math.min(X / R, 1)), n.$$.dirty[0] & /*progress*/
    128 && C != null && t(18, ve = !1), n.$$.dirty[0] & /*progress, progress_level, progress_bar, last_progress_level*/
    114816 && (C != null ? t(14, Y = C.map((g) => {
      if (g.index != null && g.length != null)
        return g.index / g.length;
      if (g.progress != null)
        return g.progress;
    })) : t(14, Y = null), Y ? (t(15, te = Y[Y.length - 1]), D && (te === 0 ? t(16, D.style.transition = "0", D) : t(16, D.style.transition = "150ms", D))) : t(15, te = void 0)), n.$$.dirty[0] & /*status*/
    16 && (a === "pending" ? at() : Fe()), n.$$.dirty[0] & /*el, scroll_to_output, status, autoscroll*/
    10493968 && u && c && (a === "pending" || a === "complete") && Ql(u, S), n.$$.dirty[0] & /*status, message*/
    4194320, n.$$.dirty[0] & /*timer_diff*/
    33554432 && t(20, l = X.toFixed(1));
  }, [
    o,
    f,
    r,
    _,
    a,
    m,
    b,
    C,
    F,
    L,
    v,
    d,
    y,
    u,
    Y,
    te,
    D,
    ye,
    ve,
    se,
    l,
    c,
    p,
    S,
    ie,
    X,
    O,
    R,
    i,
    s,
    ut,
    ct
  ];
}
class xl extends Ll {
  constructor(e) {
    super(), zl(
      this,
      e,
      Wl,
      Kl,
      Pl,
      {
        i18n: 1,
        eta: 0,
        queue_position: 2,
        queue_size: 3,
        status: 4,
        scroll_to_output: 21,
        timer: 5,
        show_progress: 6,
        message: 22,
        progress: 7,
        variant: 8,
        loading_text: 9,
        absolute: 10,
        translucent: 11,
        border: 12,
        autoscroll: 23
      },
      null,
      [-1, -1]
    );
  }
}
const {
  SvelteComponent: $l,
  append: Qe,
  assign: en,
  attr: I,
  binding_callbacks: tn,
  check_outros: ln,
  create_component: we,
  destroy_component: pe,
  detach: ge,
  element: We,
  flush: j,
  get_spread_object: nn,
  get_spread_update: sn,
  group_outros: fn,
  init: on,
  insert: he,
  listen: xe,
  mount_component: ke,
  run_all: rn,
  safe_not_equal: _n,
  set_data: an,
  set_input_value: $e,
  space: et,
  text: un,
  toggle_class: cn,
  transition_in: K,
  transition_out: ne
} = window.__gradio__svelte__internal, { tick: dn } = window.__gradio__svelte__internal;
function tt(n) {
  let e, t;
  const l = [
    { autoscroll: (
      /*gradio*/
      n[1].autoscroll
    ) },
    { i18n: (
      /*gradio*/
      n[1].i18n
    ) },
    /*loading_status*/
    n[10]
  ];
  let s = {};
  for (let i = 0; i < l.length; i += 1)
    s = en(s, l[i]);
  return e = new xl({ props: s }), {
    c() {
      we(e.$$.fragment);
    },
    m(i, f) {
      ke(e, i, f), t = !0;
    },
    p(i, f) {
      const o = f & /*gradio, loading_status*/
      1026 ? sn(l, [
        f & /*gradio*/
        2 && { autoscroll: (
          /*gradio*/
          i[1].autoscroll
        ) },
        f & /*gradio*/
        2 && { i18n: (
          /*gradio*/
          i[1].i18n
        ) },
        f & /*loading_status*/
        1024 && nn(
          /*loading_status*/
          i[10]
        )
      ]) : {};
      e.$set(o);
    },
    i(i) {
      t || (K(e.$$.fragment, i), t = !0);
    },
    o(i) {
      ne(e.$$.fragment, i), t = !1;
    },
    d(i) {
      pe(e, i);
    }
  };
}
function mn(n) {
  let e;
  return {
    c() {
      e = un(
        /*label*/
        n[2]
      );
    },
    m(t, l) {
      he(t, e, l);
    },
    p(t, l) {
      l & /*label*/
      4 && an(
        e,
        /*label*/
        t[2]
      );
    },
    d(t) {
      t && ge(e);
    }
  };
}
function bn(n) {
  let e, t, l, s, i, f, o, r, _, a, c = (
    /*loading_status*/
    n[10] && tt(n)
  );
  return l = new ul({
    props: {
      show_label: (
        /*show_label*/
        n[7]
      ),
      info: void 0,
      $$slots: { default: [mn] },
      $$scope: { ctx: n }
    }
  }), {
    c() {
      c && c.c(), e = et(), t = We("label"), we(l.$$.fragment), s = et(), i = We("input"), I(i, "data-testid", "textbox"), I(i, "type", "text"), I(i, "class", "scroll-hide svelte-2jrh70"), I(
        i,
        "placeholder",
        /*placeholder*/
        n[6]
      ), i.disabled = f = !/*interactive*/
      n[11], I(i, "dir", o = /*rtl*/
      n[12] ? "rtl" : "ltr"), I(t, "class", "svelte-2jrh70"), cn(t, "container", hn);
    },
    m(m, b) {
      c && c.m(m, b), he(m, e, b), he(m, t, b), ke(l, t, null), Qe(t, s), Qe(t, i), $e(
        i,
        /*value*/
        n[0]
      ), n[17](i), r = !0, _ || (a = [
        xe(
          i,
          "input",
          /*input_input_handler*/
          n[16]
        ),
        xe(
          i,
          "keypress",
          /*handle_keypress*/
          n[14]
        )
      ], _ = !0);
    },
    p(m, b) {
      /*loading_status*/
      m[10] ? c ? (c.p(m, b), b & /*loading_status*/
      1024 && K(c, 1)) : (c = tt(m), c.c(), K(c, 1), c.m(e.parentNode, e)) : c && (fn(), ne(c, 1, 1, () => {
        c = null;
      }), ln());
      const p = {};
      b & /*show_label*/
      128 && (p.show_label = /*show_label*/
      m[7]), b & /*$$scope, label*/
      524292 && (p.$$scope = { dirty: b, ctx: m }), l.$set(p), (!r || b & /*placeholder*/
      64) && I(
        i,
        "placeholder",
        /*placeholder*/
        m[6]
      ), (!r || b & /*interactive*/
      2048 && f !== (f = !/*interactive*/
      m[11])) && (i.disabled = f), (!r || b & /*rtl*/
      4096 && o !== (o = /*rtl*/
      m[12] ? "rtl" : "ltr")) && I(i, "dir", o), b & /*value*/
      1 && i.value !== /*value*/
      m[0] && $e(
        i,
        /*value*/
        m[0]
      );
    },
    i(m) {
      r || (K(c), K(l.$$.fragment, m), r = !0);
    },
    o(m) {
      ne(c), ne(l.$$.fragment, m), r = !1;
    },
    d(m) {
      m && (ge(e), ge(t)), c && c.d(m), pe(l), n[17](null), _ = !1, rn(a);
    }
  };
}
function gn(n) {
  let e, t;
  return e = new St({
    props: {
      visible: (
        /*visible*/
        n[5]
      ),
      elem_id: (
        /*elem_id*/
        n[3]
      ),
      elem_classes: (
        /*elem_classes*/
        n[4]
      ),
      scale: (
        /*scale*/
        n[8]
      ),
      min_width: (
        /*min_width*/
        n[9]
      ),
      allow_overflow: !1,
      padding: !0,
      $$slots: { default: [bn] },
      $$scope: { ctx: n }
    }
  }), {
    c() {
      we(e.$$.fragment);
    },
    m(l, s) {
      ke(e, l, s), t = !0;
    },
    p(l, [s]) {
      const i = {};
      s & /*visible*/
      32 && (i.visible = /*visible*/
      l[5]), s & /*elem_id*/
      8 && (i.elem_id = /*elem_id*/
      l[3]), s & /*elem_classes*/
      16 && (i.elem_classes = /*elem_classes*/
      l[4]), s & /*scale*/
      256 && (i.scale = /*scale*/
      l[8]), s & /*min_width*/
      512 && (i.min_width = /*min_width*/
      l[9]), s & /*$$scope, placeholder, interactive, rtl, value, el, show_label, label, gradio, loading_status*/
      539847 && (i.$$scope = { dirty: s, ctx: l }), e.$set(i);
    },
    i(l) {
      t || (K(e.$$.fragment, l), t = !0);
    },
    o(l) {
      ne(e.$$.fragment, l), t = !1;
    },
    d(l) {
      pe(e, l);
    }
  };
}
const hn = !0;
function wn(n, e, t) {
  let { gradio: l } = e, { label: s = "Textbox" } = e, { elem_id: i = "" } = e, { elem_classes: f = [] } = e, { visible: o = !0 } = e, { value: r = "" } = e, { placeholder: _ = "" } = e, { show_label: a } = e, { scale: c = null } = e, { min_width: m = void 0 } = e, { loading_status: b = void 0 } = e, { value_is_output: p = !1 } = e, { interactive: C } = e, { rtl: F = !1 } = e, L;
  function v() {
    l.dispatch("change"), p || l.dispatch("input");
  }
  async function d(u) {
    await dn(), u.key === "Enter" && (u.preventDefault(), l.dispatch("submit"));
  }
  function y() {
    r = this.value, t(0, r);
  }
  function S(u) {
    tn[u ? "unshift" : "push"](() => {
      L = u, t(13, L);
    });
  }
  return n.$$set = (u) => {
    "gradio" in u && t(1, l = u.gradio), "label" in u && t(2, s = u.label), "elem_id" in u && t(3, i = u.elem_id), "elem_classes" in u && t(4, f = u.elem_classes), "visible" in u && t(5, o = u.visible), "value" in u && t(0, r = u.value), "placeholder" in u && t(6, _ = u.placeholder), "show_label" in u && t(7, a = u.show_label), "scale" in u && t(8, c = u.scale), "min_width" in u && t(9, m = u.min_width), "loading_status" in u && t(10, b = u.loading_status), "value_is_output" in u && t(15, p = u.value_is_output), "interactive" in u && t(11, C = u.interactive), "rtl" in u && t(12, F = u.rtl);
  }, n.$$.update = () => {
    n.$$.dirty & /*value*/
    1 && r === null && t(0, r = ""), n.$$.dirty & /*value*/
    1 && v();
  }, [
    r,
    l,
    s,
    i,
    f,
    o,
    _,
    a,
    c,
    m,
    b,
    C,
    F,
    L,
    d,
    p,
    y,
    S
  ];
}
class pn extends $l {
  constructor(e) {
    super(), on(this, e, wn, gn, _n, {
      gradio: 1,
      label: 2,
      elem_id: 3,
      elem_classes: 4,
      visible: 5,
      value: 0,
      placeholder: 6,
      show_label: 7,
      scale: 8,
      min_width: 9,
      loading_status: 10,
      value_is_output: 15,
      interactive: 11,
      rtl: 12
    });
  }
  get gradio() {
    return this.$$.ctx[1];
  }
  set gradio(e) {
    this.$$set({ gradio: e }), j();
  }
  get label() {
    return this.$$.ctx[2];
  }
  set label(e) {
    this.$$set({ label: e }), j();
  }
  get elem_id() {
    return this.$$.ctx[3];
  }
  set elem_id(e) {
    this.$$set({ elem_id: e }), j();
  }
  get elem_classes() {
    return this.$$.ctx[4];
  }
  set elem_classes(e) {
    this.$$set({ elem_classes: e }), j();
  }
  get visible() {
    return this.$$.ctx[5];
  }
  set visible(e) {
    this.$$set({ visible: e }), j();
  }
  get value() {
    return this.$$.ctx[0];
  }
  set value(e) {
    this.$$set({ value: e }), j();
  }
  get placeholder() {
    return this.$$.ctx[6];
  }
  set placeholder(e) {
    this.$$set({ placeholder: e }), j();
  }
  get show_label() {
    return this.$$.ctx[7];
  }
  set show_label(e) {
    this.$$set({ show_label: e }), j();
  }
  get scale() {
    return this.$$.ctx[8];
  }
  set scale(e) {
    this.$$set({ scale: e }), j();
  }
  get min_width() {
    return this.$$.ctx[9];
  }
  set min_width(e) {
    this.$$set({ min_width: e }), j();
  }
  get loading_status() {
    return this.$$.ctx[10];
  }
  set loading_status(e) {
    this.$$set({ loading_status: e }), j();
  }
  get value_is_output() {
    return this.$$.ctx[15];
  }
  set value_is_output(e) {
    this.$$set({ value_is_output: e }), j();
  }
  get interactive() {
    return this.$$.ctx[11];
  }
  set interactive(e) {
    this.$$set({ interactive: e }), j();
  }
  get rtl() {
    return this.$$.ctx[12];
  }
  set rtl(e) {
    this.$$set({ rtl: e }), j();
  }
}
export {
  pn as default
};
