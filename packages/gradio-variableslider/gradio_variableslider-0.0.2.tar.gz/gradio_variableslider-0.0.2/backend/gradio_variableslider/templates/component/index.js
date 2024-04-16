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
  set_dynamic_element_data: Me,
  set_style: V,
  toggle_class: A,
  transition_in: nt,
  transition_out: it,
  update_slot_base: Ft
} = window.__gradio__svelte__internal;
function Ct(l) {
  let t, e, n;
  const i = (
    /*#slots*/
    l[18].default
  ), f = bt(
    i,
    l,
    /*$$scope*/
    l[17],
    null
  );
  let o = [
    { "data-testid": (
      /*test_id*/
      l[7]
    ) },
    { id: (
      /*elem_id*/
      l[2]
    ) },
    {
      class: e = "block " + /*elem_classes*/
      l[3].join(" ") + " svelte-nl1om8"
    }
  ], _ = {};
  for (let s = 0; s < o.length; s += 1)
    _ = mt(_, o[s]);
  return {
    c() {
      t = ht(
        /*tag*/
        l[14]
      ), f && f.c(), Me(
        /*tag*/
        l[14]
      )(t, _), A(
        t,
        "hidden",
        /*visible*/
        l[10] === !1
      ), A(
        t,
        "padded",
        /*padding*/
        l[6]
      ), A(
        t,
        "border_focus",
        /*border_mode*/
        l[5] === "focus"
      ), A(
        t,
        "border_contrast",
        /*border_mode*/
        l[5] === "contrast"
      ), A(t, "hide-container", !/*explicit_call*/
      l[8] && !/*container*/
      l[9]), V(
        t,
        "height",
        /*get_dimension*/
        l[15](
          /*height*/
          l[0]
        )
      ), V(t, "width", typeof /*width*/
      l[1] == "number" ? `calc(min(${/*width*/
      l[1]}px, 100%))` : (
        /*get_dimension*/
        l[15](
          /*width*/
          l[1]
        )
      )), V(
        t,
        "border-style",
        /*variant*/
        l[4]
      ), V(
        t,
        "overflow",
        /*allow_overflow*/
        l[11] ? "visible" : "hidden"
      ), V(
        t,
        "flex-grow",
        /*scale*/
        l[12]
      ), V(t, "min-width", `calc(min(${/*min_width*/
      l[13]}px, 100%))`), V(t, "border-width", "var(--block-border-width)");
    },
    m(s, a) {
      vt(s, t, a), f && f.m(t, null), n = !0;
    },
    p(s, a) {
      f && f.p && (!n || a & /*$$scope*/
      131072) && Ft(
        f,
        i,
        s,
        /*$$scope*/
        s[17],
        n ? pt(
          i,
          /*$$scope*/
          s[17],
          a,
          null
        ) : wt(
          /*$$scope*/
          s[17]
        ),
        null
      ), Me(
        /*tag*/
        s[14]
      )(t, _ = kt(o, [
        (!n || a & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          s[7]
        ) },
        (!n || a & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          s[2]
        ) },
        (!n || a & /*elem_classes*/
        8 && e !== (e = "block " + /*elem_classes*/
        s[3].join(" ") + " svelte-nl1om8")) && { class: e }
      ])), A(
        t,
        "hidden",
        /*visible*/
        s[10] === !1
      ), A(
        t,
        "padded",
        /*padding*/
        s[6]
      ), A(
        t,
        "border_focus",
        /*border_mode*/
        s[5] === "focus"
      ), A(
        t,
        "border_contrast",
        /*border_mode*/
        s[5] === "contrast"
      ), A(t, "hide-container", !/*explicit_call*/
      s[8] && !/*container*/
      s[9]), a & /*height*/
      1 && V(
        t,
        "height",
        /*get_dimension*/
        s[15](
          /*height*/
          s[0]
        )
      ), a & /*width*/
      2 && V(t, "width", typeof /*width*/
      s[1] == "number" ? `calc(min(${/*width*/
      s[1]}px, 100%))` : (
        /*get_dimension*/
        s[15](
          /*width*/
          s[1]
        )
      )), a & /*variant*/
      16 && V(
        t,
        "border-style",
        /*variant*/
        s[4]
      ), a & /*allow_overflow*/
      2048 && V(
        t,
        "overflow",
        /*allow_overflow*/
        s[11] ? "visible" : "hidden"
      ), a & /*scale*/
      4096 && V(
        t,
        "flex-grow",
        /*scale*/
        s[12]
      ), a & /*min_width*/
      8192 && V(t, "min-width", `calc(min(${/*min_width*/
      s[13]}px, 100%))`);
    },
    i(s) {
      n || (nt(f, s), n = !0);
    },
    o(s) {
      it(f, s), n = !1;
    },
    d(s) {
      s && gt(t), f && f.d(s);
    }
  };
}
function Lt(l) {
  let t, e = (
    /*tag*/
    l[14] && Ct(l)
  );
  return {
    c() {
      e && e.c();
    },
    m(n, i) {
      e && e.m(n, i), t = !0;
    },
    p(n, [i]) {
      /*tag*/
      n[14] && e.p(n, i);
    },
    i(n) {
      t || (nt(e, n), t = !0);
    },
    o(n) {
      it(e, n), t = !1;
    },
    d(n) {
      e && e.d(n);
    }
  };
}
function St(l, t, e) {
  let { $$slots: n = {}, $$scope: i } = t, { height: f = void 0 } = t, { width: o = void 0 } = t, { elem_id: _ = "" } = t, { elem_classes: s = [] } = t, { variant: a = "solid" } = t, { border_mode: u = "base" } = t, { padding: d = !0 } = t, { type: k = "normal" } = t, { test_id: m = void 0 } = t, { explicit_call: y = !1 } = t, { container: S = !0 } = t, { visible: F = !0 } = t, { allow_overflow: N = !0 } = t, { scale: c = null } = t, { min_width: r = 0 } = t, v = k === "fieldset" ? "fieldset" : "div";
  const C = (b) => {
    if (b !== void 0) {
      if (typeof b == "number")
        return b + "px";
      if (typeof b == "string")
        return b;
    }
  };
  return l.$$set = (b) => {
    "height" in b && e(0, f = b.height), "width" in b && e(1, o = b.width), "elem_id" in b && e(2, _ = b.elem_id), "elem_classes" in b && e(3, s = b.elem_classes), "variant" in b && e(4, a = b.variant), "border_mode" in b && e(5, u = b.border_mode), "padding" in b && e(6, d = b.padding), "type" in b && e(16, k = b.type), "test_id" in b && e(7, m = b.test_id), "explicit_call" in b && e(8, y = b.explicit_call), "container" in b && e(9, S = b.container), "visible" in b && e(10, F = b.visible), "allow_overflow" in b && e(11, N = b.allow_overflow), "scale" in b && e(12, c = b.scale), "min_width" in b && e(13, r = b.min_width), "$$scope" in b && e(17, i = b.$$scope);
  }, [
    f,
    o,
    _,
    s,
    a,
    u,
    d,
    m,
    y,
    S,
    F,
    N,
    c,
    r,
    v,
    C,
    k,
    i,
    n
  ];
}
class jt extends dt {
  constructor(t) {
    super(), yt(this, t, St, Lt, qt, {
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
  SvelteComponent: Nt,
  attr: Vt,
  create_slot: Mt,
  detach: zt,
  element: It,
  get_all_dirty_from_scope: Pt,
  get_slot_changes: Tt,
  init: Zt,
  insert: Bt,
  safe_not_equal: At,
  transition_in: Et,
  transition_out: Dt,
  update_slot_base: Ot
} = window.__gradio__svelte__internal;
function Rt(l) {
  let t, e;
  const n = (
    /*#slots*/
    l[1].default
  ), i = Mt(
    n,
    l,
    /*$$scope*/
    l[0],
    null
  );
  return {
    c() {
      t = It("div"), i && i.c(), Vt(t, "class", "svelte-1hnfib2");
    },
    m(f, o) {
      Bt(f, t, o), i && i.m(t, null), e = !0;
    },
    p(f, [o]) {
      i && i.p && (!e || o & /*$$scope*/
      1) && Ot(
        i,
        n,
        f,
        /*$$scope*/
        f[0],
        e ? Tt(
          n,
          /*$$scope*/
          f[0],
          o,
          null
        ) : Pt(
          /*$$scope*/
          f[0]
        ),
        null
      );
    },
    i(f) {
      e || (Et(i, f), e = !0);
    },
    o(f) {
      Dt(i, f), e = !1;
    },
    d(f) {
      f && zt(t), i && i.d(f);
    }
  };
}
function Ut(l, t, e) {
  let { $$slots: n = {}, $$scope: i } = t;
  return l.$$set = (f) => {
    "$$scope" in f && e(0, i = f.$$scope);
  }, [i, n];
}
class Xt extends Nt {
  constructor(t) {
    super(), Zt(this, t, Ut, Rt, At, {});
  }
}
const {
  SvelteComponent: Yt,
  attr: ze,
  check_outros: Gt,
  create_component: Ht,
  create_slot: Jt,
  destroy_component: Kt,
  detach: ge,
  element: Qt,
  empty: Wt,
  get_all_dirty_from_scope: xt,
  get_slot_changes: $t,
  group_outros: el,
  init: tl,
  insert: he,
  mount_component: ll,
  safe_not_equal: nl,
  set_data: il,
  space: sl,
  text: fl,
  toggle_class: Q,
  transition_in: se,
  transition_out: we,
  update_slot_base: ol
} = window.__gradio__svelte__internal;
function Ie(l) {
  let t, e;
  return t = new Xt({
    props: {
      $$slots: { default: [_l] },
      $$scope: { ctx: l }
    }
  }), {
    c() {
      Ht(t.$$.fragment);
    },
    m(n, i) {
      ll(t, n, i), e = !0;
    },
    p(n, i) {
      const f = {};
      i & /*$$scope, info*/
      10 && (f.$$scope = { dirty: i, ctx: n }), t.$set(f);
    },
    i(n) {
      e || (se(t.$$.fragment, n), e = !0);
    },
    o(n) {
      we(t.$$.fragment, n), e = !1;
    },
    d(n) {
      Kt(t, n);
    }
  };
}
function _l(l) {
  let t;
  return {
    c() {
      t = fl(
        /*info*/
        l[1]
      );
    },
    m(e, n) {
      he(e, t, n);
    },
    p(e, n) {
      n & /*info*/
      2 && il(
        t,
        /*info*/
        e[1]
      );
    },
    d(e) {
      e && ge(t);
    }
  };
}
function al(l) {
  let t, e, n, i;
  const f = (
    /*#slots*/
    l[2].default
  ), o = Jt(
    f,
    l,
    /*$$scope*/
    l[3],
    null
  );
  let _ = (
    /*info*/
    l[1] && Ie(l)
  );
  return {
    c() {
      t = Qt("span"), o && o.c(), e = sl(), _ && _.c(), n = Wt(), ze(t, "data-testid", "block-info"), ze(t, "class", "svelte-22c38v"), Q(t, "sr-only", !/*show_label*/
      l[0]), Q(t, "hide", !/*show_label*/
      l[0]), Q(
        t,
        "has-info",
        /*info*/
        l[1] != null
      );
    },
    m(s, a) {
      he(s, t, a), o && o.m(t, null), he(s, e, a), _ && _.m(s, a), he(s, n, a), i = !0;
    },
    p(s, [a]) {
      o && o.p && (!i || a & /*$$scope*/
      8) && ol(
        o,
        f,
        s,
        /*$$scope*/
        s[3],
        i ? $t(
          f,
          /*$$scope*/
          s[3],
          a,
          null
        ) : xt(
          /*$$scope*/
          s[3]
        ),
        null
      ), (!i || a & /*show_label*/
      1) && Q(t, "sr-only", !/*show_label*/
      s[0]), (!i || a & /*show_label*/
      1) && Q(t, "hide", !/*show_label*/
      s[0]), (!i || a & /*info*/
      2) && Q(
        t,
        "has-info",
        /*info*/
        s[1] != null
      ), /*info*/
      s[1] ? _ ? (_.p(s, a), a & /*info*/
      2 && se(_, 1)) : (_ = Ie(s), _.c(), se(_, 1), _.m(n.parentNode, n)) : _ && (el(), we(_, 1, 1, () => {
        _ = null;
      }), Gt());
    },
    i(s) {
      i || (se(o, s), se(_), i = !0);
    },
    o(s) {
      we(o, s), we(_), i = !1;
    },
    d(s) {
      s && (ge(t), ge(e), ge(n)), o && o.d(s), _ && _.d(s);
    }
  };
}
function rl(l, t, e) {
  let { $$slots: n = {}, $$scope: i } = t, { show_label: f = !0 } = t, { info: o = void 0 } = t;
  return l.$$set = (_) => {
    "show_label" in _ && e(0, f = _.show_label), "info" in _ && e(1, o = _.info), "$$scope" in _ && e(3, i = _.$$scope);
  }, [f, o, n, i];
}
class ul extends Yt {
  constructor(t) {
    super(), tl(this, t, rl, al, nl, { show_label: 0, info: 1 });
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
], Pe = {
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
  (l, { color: t, primary: e, secondary: n }) => ({
    ...l,
    [t]: {
      primary: Pe[t][e],
      secondary: Pe[t][n]
    }
  }),
  {}
);
function x(l) {
  let t = ["", "k", "M", "G", "T", "P", "E", "Z"], e = 0;
  for (; l > 1e3 && e < t.length - 1; )
    l /= 1e3, e++;
  let n = t[e];
  return (Number.isInteger(l) ? l : l.toFixed(1)) + n;
}
function pe() {
}
function dl(l, t) {
  return l != l ? t == t : l !== t || l && typeof l == "object" || typeof l == "function";
}
const st = typeof window < "u";
let Te = st ? () => window.performance.now() : () => Date.now(), ft = st ? (l) => requestAnimationFrame(l) : pe;
const $ = /* @__PURE__ */ new Set();
function ot(l) {
  $.forEach((t) => {
    t.c(l) || ($.delete(t), t.f());
  }), $.size !== 0 && ft(ot);
}
function ml(l) {
  let t;
  return $.size === 0 && ft(ot), {
    promise: new Promise((e) => {
      $.add(t = { c: l, f: e });
    }),
    abort() {
      $.delete(t);
    }
  };
}
const W = [];
function bl(l, t = pe) {
  let e;
  const n = /* @__PURE__ */ new Set();
  function i(_) {
    if (dl(l, _) && (l = _, e)) {
      const s = !W.length;
      for (const a of n)
        a[1](), W.push(a, l);
      if (s) {
        for (let a = 0; a < W.length; a += 2)
          W[a][0](W[a + 1]);
        W.length = 0;
      }
    }
  }
  function f(_) {
    i(_(l));
  }
  function o(_, s = pe) {
    const a = [_, s];
    return n.add(a), n.size === 1 && (e = t(i, f) || pe), _(l), () => {
      n.delete(a), n.size === 0 && e && (e(), e = null);
    };
  }
  return { set: i, update: f, subscribe: o };
}
function Ze(l) {
  return Object.prototype.toString.call(l) === "[object Date]";
}
function qe(l, t, e, n) {
  if (typeof e == "number" || Ze(e)) {
    const i = n - e, f = (e - t) / (l.dt || 1 / 60), o = l.opts.stiffness * i, _ = l.opts.damping * f, s = (o - _) * l.inv_mass, a = (f + s) * l.dt;
    return Math.abs(a) < l.opts.precision && Math.abs(i) < l.opts.precision ? n : (l.settled = !1, Ze(e) ? new Date(e.getTime() + a) : e + a);
  } else {
    if (Array.isArray(e))
      return e.map(
        (i, f) => qe(l, t[f], e[f], n[f])
      );
    if (typeof e == "object") {
      const i = {};
      for (const f in e)
        i[f] = qe(l, t[f], e[f], n[f]);
      return i;
    } else
      throw new Error(`Cannot spring ${typeof e} values`);
  }
}
function Be(l, t = {}) {
  const e = bl(l), { stiffness: n = 0.15, damping: i = 0.8, precision: f = 0.01 } = t;
  let o, _, s, a = l, u = l, d = 1, k = 0, m = !1;
  function y(F, N = {}) {
    u = F;
    const c = s = {};
    return l == null || N.hard || S.stiffness >= 1 && S.damping >= 1 ? (m = !0, o = Te(), a = F, e.set(l = u), Promise.resolve()) : (N.soft && (k = 1 / ((N.soft === !0 ? 0.5 : +N.soft) * 60), d = 0), _ || (o = Te(), m = !1, _ = ml((r) => {
      if (m)
        return m = !1, _ = null, !1;
      d = Math.min(d + k, 1);
      const v = {
        inv_mass: d,
        opts: S,
        settled: !0,
        dt: (r - o) * 60 / 1e3
      }, C = qe(v, a, l, u);
      return o = r, a = l, e.set(l = C), v.settled && (_ = null), !v.settled;
    })), new Promise((r) => {
      _.promise.then(() => {
        c === s && r();
      });
    }));
  }
  const S = {
    set: y,
    update: (F, N) => y(F(u, l), N),
    subscribe: e.subscribe,
    stiffness: n,
    damping: i,
    precision: f
  };
  return S;
}
const {
  SvelteComponent: gl,
  append: I,
  attr: q,
  component_subscribe: Ae,
  detach: hl,
  element: wl,
  init: pl,
  insert: kl,
  noop: Ee,
  safe_not_equal: yl,
  set_style: ce,
  svg_element: P,
  toggle_class: De
} = window.__gradio__svelte__internal, { onMount: vl } = window.__gradio__svelte__internal;
function ql(l) {
  let t, e, n, i, f, o, _, s, a, u, d, k;
  return {
    c() {
      t = wl("div"), e = P("svg"), n = P("g"), i = P("path"), f = P("path"), o = P("path"), _ = P("path"), s = P("g"), a = P("path"), u = P("path"), d = P("path"), k = P("path"), q(i, "d", "M255.926 0.754768L509.702 139.936V221.027L255.926 81.8465V0.754768Z"), q(i, "fill", "#FF7C00"), q(i, "fill-opacity", "0.4"), q(i, "class", "svelte-43sxxs"), q(f, "d", "M509.69 139.936L254.981 279.641V361.255L509.69 221.55V139.936Z"), q(f, "fill", "#FF7C00"), q(f, "class", "svelte-43sxxs"), q(o, "d", "M0.250138 139.937L254.981 279.641V361.255L0.250138 221.55V139.937Z"), q(o, "fill", "#FF7C00"), q(o, "fill-opacity", "0.4"), q(o, "class", "svelte-43sxxs"), q(_, "d", "M255.923 0.232622L0.236328 139.936V221.55L255.923 81.8469V0.232622Z"), q(_, "fill", "#FF7C00"), q(_, "class", "svelte-43sxxs"), ce(n, "transform", "translate(" + /*$top*/
      l[1][0] + "px, " + /*$top*/
      l[1][1] + "px)"), q(a, "d", "M255.926 141.5L509.702 280.681V361.773L255.926 222.592V141.5Z"), q(a, "fill", "#FF7C00"), q(a, "fill-opacity", "0.4"), q(a, "class", "svelte-43sxxs"), q(u, "d", "M509.69 280.679L254.981 420.384V501.998L509.69 362.293V280.679Z"), q(u, "fill", "#FF7C00"), q(u, "class", "svelte-43sxxs"), q(d, "d", "M0.250138 280.681L254.981 420.386V502L0.250138 362.295V280.681Z"), q(d, "fill", "#FF7C00"), q(d, "fill-opacity", "0.4"), q(d, "class", "svelte-43sxxs"), q(k, "d", "M255.923 140.977L0.236328 280.68V362.294L255.923 222.591V140.977Z"), q(k, "fill", "#FF7C00"), q(k, "class", "svelte-43sxxs"), ce(s, "transform", "translate(" + /*$bottom*/
      l[2][0] + "px, " + /*$bottom*/
      l[2][1] + "px)"), q(e, "viewBox", "-1200 -1200 3000 3000"), q(e, "fill", "none"), q(e, "xmlns", "http://www.w3.org/2000/svg"), q(e, "class", "svelte-43sxxs"), q(t, "class", "svelte-43sxxs"), De(
        t,
        "margin",
        /*margin*/
        l[0]
      );
    },
    m(m, y) {
      kl(m, t, y), I(t, e), I(e, n), I(n, i), I(n, f), I(n, o), I(n, _), I(e, s), I(s, a), I(s, u), I(s, d), I(s, k);
    },
    p(m, [y]) {
      y & /*$top*/
      2 && ce(n, "transform", "translate(" + /*$top*/
      m[1][0] + "px, " + /*$top*/
      m[1][1] + "px)"), y & /*$bottom*/
      4 && ce(s, "transform", "translate(" + /*$bottom*/
      m[2][0] + "px, " + /*$bottom*/
      m[2][1] + "px)"), y & /*margin*/
      1 && De(
        t,
        "margin",
        /*margin*/
        m[0]
      );
    },
    i: Ee,
    o: Ee,
    d(m) {
      m && hl(t);
    }
  };
}
function Fl(l, t, e) {
  let n, i, { margin: f = !0 } = t;
  const o = Be([0, 0]);
  Ae(l, o, (k) => e(1, n = k));
  const _ = Be([0, 0]);
  Ae(l, _, (k) => e(2, i = k));
  let s;
  async function a() {
    await Promise.all([o.set([125, 140]), _.set([-125, -140])]), await Promise.all([o.set([-125, 140]), _.set([125, -140])]), await Promise.all([o.set([-125, 0]), _.set([125, -0])]), await Promise.all([o.set([125, 0]), _.set([-125, 0])]);
  }
  async function u() {
    await a(), s || u();
  }
  async function d() {
    await Promise.all([o.set([125, 0]), _.set([-125, 0])]), u();
  }
  return vl(() => (d(), () => s = !0)), l.$$set = (k) => {
    "margin" in k && e(0, f = k.margin);
  }, [f, n, i, o, _];
}
class Cl extends gl {
  constructor(t) {
    super(), pl(this, t, Fl, ql, yl, { margin: 0 });
  }
}
const {
  SvelteComponent: Ll,
  append: J,
  attr: E,
  binding_callbacks: Oe,
  check_outros: _t,
  create_component: Sl,
  create_slot: jl,
  destroy_component: Nl,
  destroy_each: at,
  detach: w,
  element: U,
  empty: le,
  ensure_array_like: ke,
  get_all_dirty_from_scope: Vl,
  get_slot_changes: Ml,
  group_outros: rt,
  init: zl,
  insert: p,
  mount_component: Il,
  noop: Fe,
  safe_not_equal: Pl,
  set_data: z,
  set_style: Y,
  space: D,
  text: j,
  toggle_class: M,
  transition_in: ee,
  transition_out: te,
  update_slot_base: Tl
} = window.__gradio__svelte__internal, { tick: Zl } = window.__gradio__svelte__internal, { onDestroy: Bl } = window.__gradio__svelte__internal, Al = (l) => ({}), Re = (l) => ({});
function Ue(l, t, e) {
  const n = l.slice();
  return n[38] = t[e], n[40] = e, n;
}
function Xe(l, t, e) {
  const n = l.slice();
  return n[38] = t[e], n;
}
function El(l) {
  let t, e = (
    /*i18n*/
    l[1]("common.error") + ""
  ), n, i, f;
  const o = (
    /*#slots*/
    l[29].error
  ), _ = jl(
    o,
    l,
    /*$$scope*/
    l[28],
    Re
  );
  return {
    c() {
      t = U("span"), n = j(e), i = D(), _ && _.c(), E(t, "class", "error svelte-1yserjw");
    },
    m(s, a) {
      p(s, t, a), J(t, n), p(s, i, a), _ && _.m(s, a), f = !0;
    },
    p(s, a) {
      (!f || a[0] & /*i18n*/
      2) && e !== (e = /*i18n*/
      s[1]("common.error") + "") && z(n, e), _ && _.p && (!f || a[0] & /*$$scope*/
      268435456) && Tl(
        _,
        o,
        s,
        /*$$scope*/
        s[28],
        f ? Ml(
          o,
          /*$$scope*/
          s[28],
          a,
          Al
        ) : Vl(
          /*$$scope*/
          s[28]
        ),
        Re
      );
    },
    i(s) {
      f || (ee(_, s), f = !0);
    },
    o(s) {
      te(_, s), f = !1;
    },
    d(s) {
      s && (w(t), w(i)), _ && _.d(s);
    }
  };
}
function Dl(l) {
  let t, e, n, i, f, o, _, s, a, u = (
    /*variant*/
    l[8] === "default" && /*show_eta_bar*/
    l[18] && /*show_progress*/
    l[6] === "full" && Ye(l)
  );
  function d(r, v) {
    if (
      /*progress*/
      r[7]
    )
      return Ul;
    if (
      /*queue_position*/
      r[2] !== null && /*queue_size*/
      r[3] !== void 0 && /*queue_position*/
      r[2] >= 0
    )
      return Rl;
    if (
      /*queue_position*/
      r[2] === 0
    )
      return Ol;
  }
  let k = d(l), m = k && k(l), y = (
    /*timer*/
    l[5] && Je(l)
  );
  const S = [Hl, Gl], F = [];
  function N(r, v) {
    return (
      /*last_progress_level*/
      r[15] != null ? 0 : (
        /*show_progress*/
        r[6] === "full" ? 1 : -1
      )
    );
  }
  ~(f = N(l)) && (o = F[f] = S[f](l));
  let c = !/*timer*/
  l[5] && tt(l);
  return {
    c() {
      u && u.c(), t = D(), e = U("div"), m && m.c(), n = D(), y && y.c(), i = D(), o && o.c(), _ = D(), c && c.c(), s = le(), E(e, "class", "progress-text svelte-1yserjw"), M(
        e,
        "meta-text-center",
        /*variant*/
        l[8] === "center"
      ), M(
        e,
        "meta-text",
        /*variant*/
        l[8] === "default"
      );
    },
    m(r, v) {
      u && u.m(r, v), p(r, t, v), p(r, e, v), m && m.m(e, null), J(e, n), y && y.m(e, null), p(r, i, v), ~f && F[f].m(r, v), p(r, _, v), c && c.m(r, v), p(r, s, v), a = !0;
    },
    p(r, v) {
      /*variant*/
      r[8] === "default" && /*show_eta_bar*/
      r[18] && /*show_progress*/
      r[6] === "full" ? u ? u.p(r, v) : (u = Ye(r), u.c(), u.m(t.parentNode, t)) : u && (u.d(1), u = null), k === (k = d(r)) && m ? m.p(r, v) : (m && m.d(1), m = k && k(r), m && (m.c(), m.m(e, n))), /*timer*/
      r[5] ? y ? y.p(r, v) : (y = Je(r), y.c(), y.m(e, null)) : y && (y.d(1), y = null), (!a || v[0] & /*variant*/
      256) && M(
        e,
        "meta-text-center",
        /*variant*/
        r[8] === "center"
      ), (!a || v[0] & /*variant*/
      256) && M(
        e,
        "meta-text",
        /*variant*/
        r[8] === "default"
      );
      let C = f;
      f = N(r), f === C ? ~f && F[f].p(r, v) : (o && (rt(), te(F[C], 1, 1, () => {
        F[C] = null;
      }), _t()), ~f ? (o = F[f], o ? o.p(r, v) : (o = F[f] = S[f](r), o.c()), ee(o, 1), o.m(_.parentNode, _)) : o = null), /*timer*/
      r[5] ? c && (c.d(1), c = null) : c ? c.p(r, v) : (c = tt(r), c.c(), c.m(s.parentNode, s));
    },
    i(r) {
      a || (ee(o), a = !0);
    },
    o(r) {
      te(o), a = !1;
    },
    d(r) {
      r && (w(t), w(e), w(i), w(_), w(s)), u && u.d(r), m && m.d(), y && y.d(), ~f && F[f].d(r), c && c.d(r);
    }
  };
}
function Ye(l) {
  let t, e = `translateX(${/*eta_level*/
  (l[17] || 0) * 100 - 100}%)`;
  return {
    c() {
      t = U("div"), E(t, "class", "eta-bar svelte-1yserjw"), Y(t, "transform", e);
    },
    m(n, i) {
      p(n, t, i);
    },
    p(n, i) {
      i[0] & /*eta_level*/
      131072 && e !== (e = `translateX(${/*eta_level*/
      (n[17] || 0) * 100 - 100}%)`) && Y(t, "transform", e);
    },
    d(n) {
      n && w(t);
    }
  };
}
function Ol(l) {
  let t;
  return {
    c() {
      t = j("processing |");
    },
    m(e, n) {
      p(e, t, n);
    },
    p: Fe,
    d(e) {
      e && w(t);
    }
  };
}
function Rl(l) {
  let t, e = (
    /*queue_position*/
    l[2] + 1 + ""
  ), n, i, f, o;
  return {
    c() {
      t = j("queue: "), n = j(e), i = j("/"), f = j(
        /*queue_size*/
        l[3]
      ), o = j(" |");
    },
    m(_, s) {
      p(_, t, s), p(_, n, s), p(_, i, s), p(_, f, s), p(_, o, s);
    },
    p(_, s) {
      s[0] & /*queue_position*/
      4 && e !== (e = /*queue_position*/
      _[2] + 1 + "") && z(n, e), s[0] & /*queue_size*/
      8 && z(
        f,
        /*queue_size*/
        _[3]
      );
    },
    d(_) {
      _ && (w(t), w(n), w(i), w(f), w(o));
    }
  };
}
function Ul(l) {
  let t, e = ke(
    /*progress*/
    l[7]
  ), n = [];
  for (let i = 0; i < e.length; i += 1)
    n[i] = He(Xe(l, e, i));
  return {
    c() {
      for (let i = 0; i < n.length; i += 1)
        n[i].c();
      t = le();
    },
    m(i, f) {
      for (let o = 0; o < n.length; o += 1)
        n[o] && n[o].m(i, f);
      p(i, t, f);
    },
    p(i, f) {
      if (f[0] & /*progress*/
      128) {
        e = ke(
          /*progress*/
          i[7]
        );
        let o;
        for (o = 0; o < e.length; o += 1) {
          const _ = Xe(i, e, o);
          n[o] ? n[o].p(_, f) : (n[o] = He(_), n[o].c(), n[o].m(t.parentNode, t));
        }
        for (; o < n.length; o += 1)
          n[o].d(1);
        n.length = e.length;
      }
    },
    d(i) {
      i && w(t), at(n, i);
    }
  };
}
function Ge(l) {
  let t, e = (
    /*p*/
    l[38].unit + ""
  ), n, i, f = " ", o;
  function _(u, d) {
    return (
      /*p*/
      u[38].length != null ? Yl : Xl
    );
  }
  let s = _(l), a = s(l);
  return {
    c() {
      a.c(), t = D(), n = j(e), i = j(" | "), o = j(f);
    },
    m(u, d) {
      a.m(u, d), p(u, t, d), p(u, n, d), p(u, i, d), p(u, o, d);
    },
    p(u, d) {
      s === (s = _(u)) && a ? a.p(u, d) : (a.d(1), a = s(u), a && (a.c(), a.m(t.parentNode, t))), d[0] & /*progress*/
      128 && e !== (e = /*p*/
      u[38].unit + "") && z(n, e);
    },
    d(u) {
      u && (w(t), w(n), w(i), w(o)), a.d(u);
    }
  };
}
function Xl(l) {
  let t = x(
    /*p*/
    l[38].index || 0
  ) + "", e;
  return {
    c() {
      e = j(t);
    },
    m(n, i) {
      p(n, e, i);
    },
    p(n, i) {
      i[0] & /*progress*/
      128 && t !== (t = x(
        /*p*/
        n[38].index || 0
      ) + "") && z(e, t);
    },
    d(n) {
      n && w(e);
    }
  };
}
function Yl(l) {
  let t = x(
    /*p*/
    l[38].index || 0
  ) + "", e, n, i = x(
    /*p*/
    l[38].length
  ) + "", f;
  return {
    c() {
      e = j(t), n = j("/"), f = j(i);
    },
    m(o, _) {
      p(o, e, _), p(o, n, _), p(o, f, _);
    },
    p(o, _) {
      _[0] & /*progress*/
      128 && t !== (t = x(
        /*p*/
        o[38].index || 0
      ) + "") && z(e, t), _[0] & /*progress*/
      128 && i !== (i = x(
        /*p*/
        o[38].length
      ) + "") && z(f, i);
    },
    d(o) {
      o && (w(e), w(n), w(f));
    }
  };
}
function He(l) {
  let t, e = (
    /*p*/
    l[38].index != null && Ge(l)
  );
  return {
    c() {
      e && e.c(), t = le();
    },
    m(n, i) {
      e && e.m(n, i), p(n, t, i);
    },
    p(n, i) {
      /*p*/
      n[38].index != null ? e ? e.p(n, i) : (e = Ge(n), e.c(), e.m(t.parentNode, t)) : e && (e.d(1), e = null);
    },
    d(n) {
      n && w(t), e && e.d(n);
    }
  };
}
function Je(l) {
  let t, e = (
    /*eta*/
    l[0] ? `/${/*formatted_eta*/
    l[19]}` : ""
  ), n, i;
  return {
    c() {
      t = j(
        /*formatted_timer*/
        l[20]
      ), n = j(e), i = j("s");
    },
    m(f, o) {
      p(f, t, o), p(f, n, o), p(f, i, o);
    },
    p(f, o) {
      o[0] & /*formatted_timer*/
      1048576 && z(
        t,
        /*formatted_timer*/
        f[20]
      ), o[0] & /*eta, formatted_eta*/
      524289 && e !== (e = /*eta*/
      f[0] ? `/${/*formatted_eta*/
      f[19]}` : "") && z(n, e);
    },
    d(f) {
      f && (w(t), w(n), w(i));
    }
  };
}
function Gl(l) {
  let t, e;
  return t = new Cl({
    props: { margin: (
      /*variant*/
      l[8] === "default"
    ) }
  }), {
    c() {
      Sl(t.$$.fragment);
    },
    m(n, i) {
      Il(t, n, i), e = !0;
    },
    p(n, i) {
      const f = {};
      i[0] & /*variant*/
      256 && (f.margin = /*variant*/
      n[8] === "default"), t.$set(f);
    },
    i(n) {
      e || (ee(t.$$.fragment, n), e = !0);
    },
    o(n) {
      te(t.$$.fragment, n), e = !1;
    },
    d(n) {
      Nl(t, n);
    }
  };
}
function Hl(l) {
  let t, e, n, i, f, o = `${/*last_progress_level*/
  l[15] * 100}%`, _ = (
    /*progress*/
    l[7] != null && Ke(l)
  );
  return {
    c() {
      t = U("div"), e = U("div"), _ && _.c(), n = D(), i = U("div"), f = U("div"), E(e, "class", "progress-level-inner svelte-1yserjw"), E(f, "class", "progress-bar svelte-1yserjw"), Y(f, "width", o), E(i, "class", "progress-bar-wrap svelte-1yserjw"), E(t, "class", "progress-level svelte-1yserjw");
    },
    m(s, a) {
      p(s, t, a), J(t, e), _ && _.m(e, null), J(t, n), J(t, i), J(i, f), l[30](f);
    },
    p(s, a) {
      /*progress*/
      s[7] != null ? _ ? _.p(s, a) : (_ = Ke(s), _.c(), _.m(e, null)) : _ && (_.d(1), _ = null), a[0] & /*last_progress_level*/
      32768 && o !== (o = `${/*last_progress_level*/
      s[15] * 100}%`) && Y(f, "width", o);
    },
    i: Fe,
    o: Fe,
    d(s) {
      s && w(t), _ && _.d(), l[30](null);
    }
  };
}
function Ke(l) {
  let t, e = ke(
    /*progress*/
    l[7]
  ), n = [];
  for (let i = 0; i < e.length; i += 1)
    n[i] = et(Ue(l, e, i));
  return {
    c() {
      for (let i = 0; i < n.length; i += 1)
        n[i].c();
      t = le();
    },
    m(i, f) {
      for (let o = 0; o < n.length; o += 1)
        n[o] && n[o].m(i, f);
      p(i, t, f);
    },
    p(i, f) {
      if (f[0] & /*progress_level, progress*/
      16512) {
        e = ke(
          /*progress*/
          i[7]
        );
        let o;
        for (o = 0; o < e.length; o += 1) {
          const _ = Ue(i, e, o);
          n[o] ? n[o].p(_, f) : (n[o] = et(_), n[o].c(), n[o].m(t.parentNode, t));
        }
        for (; o < n.length; o += 1)
          n[o].d(1);
        n.length = e.length;
      }
    },
    d(i) {
      i && w(t), at(n, i);
    }
  };
}
function Qe(l) {
  let t, e, n, i, f = (
    /*i*/
    l[40] !== 0 && Jl()
  ), o = (
    /*p*/
    l[38].desc != null && We(l)
  ), _ = (
    /*p*/
    l[38].desc != null && /*progress_level*/
    l[14] && /*progress_level*/
    l[14][
      /*i*/
      l[40]
    ] != null && xe()
  ), s = (
    /*progress_level*/
    l[14] != null && $e(l)
  );
  return {
    c() {
      f && f.c(), t = D(), o && o.c(), e = D(), _ && _.c(), n = D(), s && s.c(), i = le();
    },
    m(a, u) {
      f && f.m(a, u), p(a, t, u), o && o.m(a, u), p(a, e, u), _ && _.m(a, u), p(a, n, u), s && s.m(a, u), p(a, i, u);
    },
    p(a, u) {
      /*p*/
      a[38].desc != null ? o ? o.p(a, u) : (o = We(a), o.c(), o.m(e.parentNode, e)) : o && (o.d(1), o = null), /*p*/
      a[38].desc != null && /*progress_level*/
      a[14] && /*progress_level*/
      a[14][
        /*i*/
        a[40]
      ] != null ? _ || (_ = xe(), _.c(), _.m(n.parentNode, n)) : _ && (_.d(1), _ = null), /*progress_level*/
      a[14] != null ? s ? s.p(a, u) : (s = $e(a), s.c(), s.m(i.parentNode, i)) : s && (s.d(1), s = null);
    },
    d(a) {
      a && (w(t), w(e), w(n), w(i)), f && f.d(a), o && o.d(a), _ && _.d(a), s && s.d(a);
    }
  };
}
function Jl(l) {
  let t;
  return {
    c() {
      t = j(" /");
    },
    m(e, n) {
      p(e, t, n);
    },
    d(e) {
      e && w(t);
    }
  };
}
function We(l) {
  let t = (
    /*p*/
    l[38].desc + ""
  ), e;
  return {
    c() {
      e = j(t);
    },
    m(n, i) {
      p(n, e, i);
    },
    p(n, i) {
      i[0] & /*progress*/
      128 && t !== (t = /*p*/
      n[38].desc + "") && z(e, t);
    },
    d(n) {
      n && w(e);
    }
  };
}
function xe(l) {
  let t;
  return {
    c() {
      t = j("-");
    },
    m(e, n) {
      p(e, t, n);
    },
    d(e) {
      e && w(t);
    }
  };
}
function $e(l) {
  let t = (100 * /*progress_level*/
  (l[14][
    /*i*/
    l[40]
  ] || 0)).toFixed(1) + "", e, n;
  return {
    c() {
      e = j(t), n = j("%");
    },
    m(i, f) {
      p(i, e, f), p(i, n, f);
    },
    p(i, f) {
      f[0] & /*progress_level*/
      16384 && t !== (t = (100 * /*progress_level*/
      (i[14][
        /*i*/
        i[40]
      ] || 0)).toFixed(1) + "") && z(e, t);
    },
    d(i) {
      i && (w(e), w(n));
    }
  };
}
function et(l) {
  let t, e = (
    /*p*/
    (l[38].desc != null || /*progress_level*/
    l[14] && /*progress_level*/
    l[14][
      /*i*/
      l[40]
    ] != null) && Qe(l)
  );
  return {
    c() {
      e && e.c(), t = le();
    },
    m(n, i) {
      e && e.m(n, i), p(n, t, i);
    },
    p(n, i) {
      /*p*/
      n[38].desc != null || /*progress_level*/
      n[14] && /*progress_level*/
      n[14][
        /*i*/
        n[40]
      ] != null ? e ? e.p(n, i) : (e = Qe(n), e.c(), e.m(t.parentNode, t)) : e && (e.d(1), e = null);
    },
    d(n) {
      n && w(t), e && e.d(n);
    }
  };
}
function tt(l) {
  let t, e;
  return {
    c() {
      t = U("p"), e = j(
        /*loading_text*/
        l[9]
      ), E(t, "class", "loading svelte-1yserjw");
    },
    m(n, i) {
      p(n, t, i), J(t, e);
    },
    p(n, i) {
      i[0] & /*loading_text*/
      512 && z(
        e,
        /*loading_text*/
        n[9]
      );
    },
    d(n) {
      n && w(t);
    }
  };
}
function Kl(l) {
  let t, e, n, i, f;
  const o = [Dl, El], _ = [];
  function s(a, u) {
    return (
      /*status*/
      a[4] === "pending" ? 0 : (
        /*status*/
        a[4] === "error" ? 1 : -1
      )
    );
  }
  return ~(e = s(l)) && (n = _[e] = o[e](l)), {
    c() {
      t = U("div"), n && n.c(), E(t, "class", i = "wrap " + /*variant*/
      l[8] + " " + /*show_progress*/
      l[6] + " svelte-1yserjw"), M(t, "hide", !/*status*/
      l[4] || /*status*/
      l[4] === "complete" || /*show_progress*/
      l[6] === "hidden"), M(
        t,
        "translucent",
        /*variant*/
        l[8] === "center" && /*status*/
        (l[4] === "pending" || /*status*/
        l[4] === "error") || /*translucent*/
        l[11] || /*show_progress*/
        l[6] === "minimal"
      ), M(
        t,
        "generating",
        /*status*/
        l[4] === "generating"
      ), M(
        t,
        "border",
        /*border*/
        l[12]
      ), Y(
        t,
        "position",
        /*absolute*/
        l[10] ? "absolute" : "static"
      ), Y(
        t,
        "padding",
        /*absolute*/
        l[10] ? "0" : "var(--size-8) 0"
      );
    },
    m(a, u) {
      p(a, t, u), ~e && _[e].m(t, null), l[31](t), f = !0;
    },
    p(a, u) {
      let d = e;
      e = s(a), e === d ? ~e && _[e].p(a, u) : (n && (rt(), te(_[d], 1, 1, () => {
        _[d] = null;
      }), _t()), ~e ? (n = _[e], n ? n.p(a, u) : (n = _[e] = o[e](a), n.c()), ee(n, 1), n.m(t, null)) : n = null), (!f || u[0] & /*variant, show_progress*/
      320 && i !== (i = "wrap " + /*variant*/
      a[8] + " " + /*show_progress*/
      a[6] + " svelte-1yserjw")) && E(t, "class", i), (!f || u[0] & /*variant, show_progress, status, show_progress*/
      336) && M(t, "hide", !/*status*/
      a[4] || /*status*/
      a[4] === "complete" || /*show_progress*/
      a[6] === "hidden"), (!f || u[0] & /*variant, show_progress, variant, status, translucent, show_progress*/
      2384) && M(
        t,
        "translucent",
        /*variant*/
        a[8] === "center" && /*status*/
        (a[4] === "pending" || /*status*/
        a[4] === "error") || /*translucent*/
        a[11] || /*show_progress*/
        a[6] === "minimal"
      ), (!f || u[0] & /*variant, show_progress, status*/
      336) && M(
        t,
        "generating",
        /*status*/
        a[4] === "generating"
      ), (!f || u[0] & /*variant, show_progress, border*/
      4416) && M(
        t,
        "border",
        /*border*/
        a[12]
      ), u[0] & /*absolute*/
      1024 && Y(
        t,
        "position",
        /*absolute*/
        a[10] ? "absolute" : "static"
      ), u[0] & /*absolute*/
      1024 && Y(
        t,
        "padding",
        /*absolute*/
        a[10] ? "0" : "var(--size-8) 0"
      );
    },
    i(a) {
      f || (ee(n), f = !0);
    },
    o(a) {
      te(n), f = !1;
    },
    d(a) {
      a && w(t), ~e && _[e].d(), l[31](null);
    }
  };
}
let de = [], ye = !1;
async function Ql(l, t = !0) {
  if (!(window.__gradio_mode__ === "website" || window.__gradio_mode__ !== "app" && t !== !0)) {
    if (de.push(l), !ye)
      ye = !0;
    else
      return;
    await Zl(), requestAnimationFrame(() => {
      let e = [0, 0];
      for (let n = 0; n < de.length; n++) {
        const f = de[n].getBoundingClientRect();
        (n === 0 || f.top + window.scrollY <= e[0]) && (e[0] = f.top + window.scrollY, e[1] = n);
      }
      window.scrollTo({ top: e[0] - 20, behavior: "smooth" }), ye = !1, de = [];
    });
  }
}
function Wl(l, t, e) {
  let n, { $$slots: i = {}, $$scope: f } = t, { i18n: o } = t, { eta: _ = null } = t, { queue_position: s } = t, { queue_size: a } = t, { status: u } = t, { scroll_to_output: d = !1 } = t, { timer: k = !0 } = t, { show_progress: m = "full" } = t, { message: y = null } = t, { progress: S = null } = t, { variant: F = "default" } = t, { loading_text: N = "Loading..." } = t, { absolute: c = !0 } = t, { translucent: r = !1 } = t, { border: v = !1 } = t, { autoscroll: C } = t, b, G = !1, K = 0, O = 0, X = null, T = null, _e = 0, R = null, H, Z = null, ae = !0;
  const g = () => {
    e(0, _ = e(26, X = e(19, ue = null))), e(24, K = performance.now()), e(25, O = 0), G = !0, B();
  };
  function B() {
    requestAnimationFrame(() => {
      e(25, O = (performance.now() - K) / 1e3), G && B();
    });
  }
  function re() {
    e(25, O = 0), e(0, _ = e(26, X = e(19, ue = null))), G && (G = !1);
  }
  Bl(() => {
    G && re();
  });
  let ue = null;
  function ut(h) {
    Oe[h ? "unshift" : "push"](() => {
      Z = h, e(16, Z), e(7, S), e(14, R), e(15, H);
    });
  }
  function ct(h) {
    Oe[h ? "unshift" : "push"](() => {
      b = h, e(13, b);
    });
  }
  return l.$$set = (h) => {
    "i18n" in h && e(1, o = h.i18n), "eta" in h && e(0, _ = h.eta), "queue_position" in h && e(2, s = h.queue_position), "queue_size" in h && e(3, a = h.queue_size), "status" in h && e(4, u = h.status), "scroll_to_output" in h && e(21, d = h.scroll_to_output), "timer" in h && e(5, k = h.timer), "show_progress" in h && e(6, m = h.show_progress), "message" in h && e(22, y = h.message), "progress" in h && e(7, S = h.progress), "variant" in h && e(8, F = h.variant), "loading_text" in h && e(9, N = h.loading_text), "absolute" in h && e(10, c = h.absolute), "translucent" in h && e(11, r = h.translucent), "border" in h && e(12, v = h.border), "autoscroll" in h && e(23, C = h.autoscroll), "$$scope" in h && e(28, f = h.$$scope);
  }, l.$$.update = () => {
    l.$$.dirty[0] & /*eta, old_eta, timer_start, eta_from_start*/
    218103809 && (_ === null && e(0, _ = X), _ != null && X !== _ && (e(27, T = (performance.now() - K) / 1e3 + _), e(19, ue = T.toFixed(1)), e(26, X = _))), l.$$.dirty[0] & /*eta_from_start, timer_diff*/
    167772160 && e(17, _e = T === null || T <= 0 || !O ? null : Math.min(O / T, 1)), l.$$.dirty[0] & /*progress*/
    128 && S != null && e(18, ae = !1), l.$$.dirty[0] & /*progress, progress_level, progress_bar, last_progress_level*/
    114816 && (S != null ? e(14, R = S.map((h) => {
      if (h.index != null && h.length != null)
        return h.index / h.length;
      if (h.progress != null)
        return h.progress;
    })) : e(14, R = null), R ? (e(15, H = R[R.length - 1]), Z && (H === 0 ? e(16, Z.style.transition = "0", Z) : e(16, Z.style.transition = "150ms", Z))) : e(15, H = void 0)), l.$$.dirty[0] & /*status*/
    16 && (u === "pending" ? g() : re()), l.$$.dirty[0] & /*el, scroll_to_output, status, autoscroll*/
    10493968 && b && d && (u === "pending" || u === "complete") && Ql(b, C), l.$$.dirty[0] & /*status, message*/
    4194320, l.$$.dirty[0] & /*timer_diff*/
    33554432 && e(20, n = O.toFixed(1));
  }, [
    _,
    o,
    s,
    a,
    u,
    k,
    m,
    S,
    F,
    N,
    c,
    r,
    v,
    b,
    R,
    H,
    Z,
    _e,
    ae,
    ue,
    n,
    d,
    y,
    C,
    K,
    O,
    X,
    T,
    f,
    i,
    ut,
    ct
  ];
}
class xl extends Ll {
  constructor(t) {
    super(), zl(
      this,
      t,
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
  append: me,
  assign: en,
  attr: L,
  binding_callbacks: lt,
  create_component: Ce,
  destroy_component: Le,
  detach: fe,
  element: ne,
  get_spread_object: tn,
  get_spread_update: ln,
  init: nn,
  insert: oe,
  listen: ie,
  mount_component: Se,
  run_all: sn,
  safe_not_equal: fn,
  set_data: on,
  set_input_value: be,
  space: ve,
  text: _n,
  to_number: je,
  transition_in: Ne,
  transition_out: Ve
} = window.__gradio__svelte__internal, { afterUpdate: an } = window.__gradio__svelte__internal;
function rn(l) {
  let t;
  return {
    c() {
      t = _n(
        /*label*/
        l[5]
      );
    },
    m(e, n) {
      oe(e, t, n);
    },
    p(e, n) {
      n[0] & /*label*/
      32 && on(
        t,
        /*label*/
        e[5]
      );
    },
    d(e) {
      e && fe(t);
    }
  };
}
function un(l) {
  let t, e, n, i, f, o, _, s, a, u, d, k, m, y, S;
  const F = [
    { autoscroll: (
      /*gradio*/
      l[1].autoscroll
    ) },
    { i18n: (
      /*gradio*/
      l[1].i18n
    ) },
    /*loading_status*/
    l[14]
  ];
  let N = {};
  for (let c = 0; c < F.length; c += 1)
    N = en(N, F[c]);
  return t = new xl({ props: N }), o = new ul({
    props: {
      show_label: (
        /*show_label*/
        l[13]
      ),
      info: (
        /*info*/
        l[6]
      ),
      $$slots: { default: [rn] },
      $$scope: { ctx: l }
    }
  }), {
    c() {
      Ce(t.$$.fragment), e = ve(), n = ne("div"), i = ne("div"), f = ne("label"), Ce(o.$$.fragment), _ = ve(), s = ne("input"), u = ve(), d = ne("input"), L(
        f,
        "for",
        /*id*/
        l[18]
      ), L(s, "aria-label", a = `number input for ${/*label*/
      l[5]}`), L(s, "data-testid", "number-input"), L(s, "type", "number"), L(
        s,
        "min",
        /*minimum*/
        l[10]
      ), L(
        s,
        "max",
        /*maximum*/
        l[11]
      ), L(
        s,
        "step",
        /*step*/
        l[12]
      ), s.disabled = /*disabled*/
      l[17], s.readOnly = !0, L(s, "class", "svelte-o2qgeu"), L(i, "class", "head svelte-o2qgeu"), L(n, "class", "wrap svelte-o2qgeu"), L(d, "type", "range"), L(
        d,
        "id",
        /*id*/
        l[18]
      ), L(d, "name", "cowbell"), L(
        d,
        "min",
        /*minimum*/
        l[10]
      ), L(
        d,
        "max",
        /*maximum*/
        l[11]
      ), L(
        d,
        "step",
        /*step*/
        l[12]
      ), d.disabled = /*disabled*/
      l[17], L(d, "aria-label", k = `range slider for ${/*label*/
      l[5]}`), L(d, "class", "svelte-o2qgeu");
    },
    m(c, r) {
      Se(t, c, r), oe(c, e, r), oe(c, n, r), me(n, i), me(i, f), Se(o, f, null), me(i, _), me(i, s), be(
        s,
        /*value*/
        l[0]
      ), l[24](s), oe(c, u, r), oe(c, d, r), be(
        d,
        /*value*/
        l[0]
      ), l[26](d), m = !0, y || (S = [
        ie(
          s,
          "input",
          /*input0_input_handler*/
          l[23]
        ),
        ie(
          s,
          "blur",
          /*clamp*/
          l[19]
        ),
        ie(
          d,
          "change",
          /*input1_change_input_handler*/
          l[25]
        ),
        ie(
          d,
          "input",
          /*input1_change_input_handler*/
          l[25]
        ),
        ie(
          d,
          "input",
          /*adjustValue*/
          l[20]
        )
      ], y = !0);
    },
    p(c, r) {
      const v = r[0] & /*gradio, loading_status*/
      16386 ? ln(F, [
        r[0] & /*gradio*/
        2 && { autoscroll: (
          /*gradio*/
          c[1].autoscroll
        ) },
        r[0] & /*gradio*/
        2 && { i18n: (
          /*gradio*/
          c[1].i18n
        ) },
        r[0] & /*loading_status*/
        16384 && tn(
          /*loading_status*/
          c[14]
        )
      ]) : {};
      t.$set(v);
      const C = {};
      r[0] & /*show_label*/
      8192 && (C.show_label = /*show_label*/
      c[13]), r[0] & /*info*/
      64 && (C.info = /*info*/
      c[6]), r[0] & /*label*/
      32 | r[1] & /*$$scope*/
      1 && (C.$$scope = { dirty: r, ctx: c }), o.$set(C), (!m || r[0] & /*label*/
      32 && a !== (a = `number input for ${/*label*/
      c[5]}`)) && L(s, "aria-label", a), (!m || r[0] & /*minimum*/
      1024) && L(
        s,
        "min",
        /*minimum*/
        c[10]
      ), (!m || r[0] & /*maximum*/
      2048) && L(
        s,
        "max",
        /*maximum*/
        c[11]
      ), (!m || r[0] & /*step*/
      4096) && L(
        s,
        "step",
        /*step*/
        c[12]
      ), (!m || r[0] & /*disabled*/
      131072) && (s.disabled = /*disabled*/
      c[17]), r[0] & /*value*/
      1 && je(s.value) !== /*value*/
      c[0] && be(
        s,
        /*value*/
        c[0]
      ), (!m || r[0] & /*minimum*/
      1024) && L(
        d,
        "min",
        /*minimum*/
        c[10]
      ), (!m || r[0] & /*maximum*/
      2048) && L(
        d,
        "max",
        /*maximum*/
        c[11]
      ), (!m || r[0] & /*step*/
      4096) && L(
        d,
        "step",
        /*step*/
        c[12]
      ), (!m || r[0] & /*disabled*/
      131072) && (d.disabled = /*disabled*/
      c[17]), (!m || r[0] & /*label*/
      32 && k !== (k = `range slider for ${/*label*/
      c[5]}`)) && L(d, "aria-label", k), r[0] & /*value*/
      1 && be(
        d,
        /*value*/
        c[0]
      );
    },
    i(c) {
      m || (Ne(t.$$.fragment, c), Ne(o.$$.fragment, c), m = !0);
    },
    o(c) {
      Ve(t.$$.fragment, c), Ve(o.$$.fragment, c), m = !1;
    },
    d(c) {
      c && (fe(e), fe(n), fe(u), fe(d)), Le(t, c), Le(o), l[24](null), l[26](null), y = !1, sn(S);
    }
  };
}
function cn(l) {
  let t, e;
  return t = new jt({
    props: {
      visible: (
        /*visible*/
        l[4]
      ),
      elem_id: (
        /*elem_id*/
        l[2]
      ),
      elem_classes: (
        /*elem_classes*/
        l[3]
      ),
      container: (
        /*container*/
        l[7]
      ),
      scale: (
        /*scale*/
        l[8]
      ),
      min_width: (
        /*min_width*/
        l[9]
      ),
      $$slots: { default: [un] },
      $$scope: { ctx: l }
    }
  }), {
    c() {
      Ce(t.$$.fragment);
    },
    m(n, i) {
      Se(t, n, i), e = !0;
    },
    p(n, i) {
      const f = {};
      i[0] & /*visible*/
      16 && (f.visible = /*visible*/
      n[4]), i[0] & /*elem_id*/
      4 && (f.elem_id = /*elem_id*/
      n[2]), i[0] & /*elem_classes*/
      8 && (f.elem_classes = /*elem_classes*/
      n[3]), i[0] & /*container*/
      128 && (f.container = /*container*/
      n[7]), i[0] & /*scale*/
      256 && (f.scale = /*scale*/
      n[8]), i[0] & /*min_width*/
      512 && (f.min_width = /*min_width*/
      n[9]), i[0] & /*minimum, maximum, step, disabled, label, value, rangeInput, numberInput, show_label, info, gradio, loading_status*/
      261219 | i[1] & /*$$scope*/
      1 && (f.$$scope = { dirty: i, ctx: n }), t.$set(f);
    },
    i(n) {
      e || (Ne(t.$$.fragment, n), e = !0);
    },
    o(n) {
      Ve(t.$$.fragment, n), e = !1;
    },
    d(n) {
      Le(t, n);
    }
  };
}
let dn = 0;
function mn(l, t, e) {
  let n, { gradio: i } = t, { elem_id: f = "" } = t, { elem_classes: o = [] } = t, { visible: _ = !0 } = t, { value: s = 0 } = t, { label: a = i.i18n("slider.slider") } = t, { info: u = void 0 } = t, { container: d = !0 } = t, { scale: k = null } = t, { min_width: m = void 0 } = t, { minimum: y } = t, { maximum: S = 100 } = t, { step: F } = t, { show_label: N } = t, { interactive: c } = t, { loading_status: r } = t, { value_is_output: v = !1 } = t, C, b;
  const G = `range_id_${dn++}`;
  function K() {
    i.dispatch("change"), v || i.dispatch("input");
  }
  an(() => {
    e(21, v = !1), X();
  });
  function O() {
    i.dispatch("release", s), e(0, s = Math.min(Math.max(s, y), S));
  }
  function X() {
    T(), C.addEventListener("input", T), b.addEventListener("input", T);
  }
  function T() {
    const g = Number(C.value) - Number(C.min), B = Number(C.max) - Number(C.min), re = B === 0 ? 0 : g / B;
    e(15, C.style.backgroundSize = re * 100 + "% 100%", C);
  }
  function _e(g) {
    let B = parseFloat(g.target.value);
    Number.isInteger(B) && (B += B + F <= g.target.max ? F : -F, e(0, s = B));
  }
  function R() {
    s = je(this.value), e(0, s);
  }
  function H(g) {
    lt[g ? "unshift" : "push"](() => {
      b = g, e(16, b);
    });
  }
  function Z() {
    s = je(this.value), e(0, s);
  }
  function ae(g) {
    lt[g ? "unshift" : "push"](() => {
      C = g, e(15, C);
    });
  }
  return l.$$set = (g) => {
    "gradio" in g && e(1, i = g.gradio), "elem_id" in g && e(2, f = g.elem_id), "elem_classes" in g && e(3, o = g.elem_classes), "visible" in g && e(4, _ = g.visible), "value" in g && e(0, s = g.value), "label" in g && e(5, a = g.label), "info" in g && e(6, u = g.info), "container" in g && e(7, d = g.container), "scale" in g && e(8, k = g.scale), "min_width" in g && e(9, m = g.min_width), "minimum" in g && e(10, y = g.minimum), "maximum" in g && e(11, S = g.maximum), "step" in g && e(12, F = g.step), "show_label" in g && e(13, N = g.show_label), "interactive" in g && e(22, c = g.interactive), "loading_status" in g && e(14, r = g.loading_status), "value_is_output" in g && e(21, v = g.value_is_output);
  }, l.$$.update = () => {
    l.$$.dirty[0] & /*interactive*/
    4194304 && e(17, n = !c), l.$$.dirty[0] & /*value*/
    1 && K();
  }, [
    s,
    i,
    f,
    o,
    _,
    a,
    u,
    d,
    k,
    m,
    y,
    S,
    F,
    N,
    r,
    C,
    b,
    n,
    G,
    O,
    _e,
    v,
    c,
    R,
    H,
    Z,
    ae
  ];
}
class bn extends $l {
  constructor(t) {
    super(), nn(
      this,
      t,
      mn,
      cn,
      fn,
      {
        gradio: 1,
        elem_id: 2,
        elem_classes: 3,
        visible: 4,
        value: 0,
        label: 5,
        info: 6,
        container: 7,
        scale: 8,
        min_width: 9,
        minimum: 10,
        maximum: 11,
        step: 12,
        show_label: 13,
        interactive: 22,
        loading_status: 14,
        value_is_output: 21
      },
      null,
      [-1, -1]
    );
  }
}
export {
  bn as default
};
