const {
  SvelteComponent: bt,
  assign: gt,
  create_slot: ht,
  detach: wt,
  element: pt,
  get_all_dirty_from_scope: kt,
  get_slot_changes: yt,
  get_spread_update: vt,
  init: qt,
  insert: Ft,
  safe_not_equal: Ct,
  set_dynamic_element_data: ze,
  set_style: z,
  toggle_class: D,
  transition_in: it,
  transition_out: st,
  update_slot_base: Lt
} = window.__gradio__svelte__internal;
function St(l) {
  let t, e, n;
  const i = (
    /*#slots*/
    l[18].default
  ), f = ht(
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
    _ = gt(_, o[s]);
  return {
    c() {
      t = pt(
        /*tag*/
        l[14]
      ), f && f.c(), ze(
        /*tag*/
        l[14]
      )(t, _), D(
        t,
        "hidden",
        /*visible*/
        l[10] === !1
      ), D(
        t,
        "padded",
        /*padding*/
        l[6]
      ), D(
        t,
        "border_focus",
        /*border_mode*/
        l[5] === "focus"
      ), D(
        t,
        "border_contrast",
        /*border_mode*/
        l[5] === "contrast"
      ), D(t, "hide-container", !/*explicit_call*/
      l[8] && !/*container*/
      l[9]), z(
        t,
        "height",
        /*get_dimension*/
        l[15](
          /*height*/
          l[0]
        )
      ), z(t, "width", typeof /*width*/
      l[1] == "number" ? `calc(min(${/*width*/
      l[1]}px, 100%))` : (
        /*get_dimension*/
        l[15](
          /*width*/
          l[1]
        )
      )), z(
        t,
        "border-style",
        /*variant*/
        l[4]
      ), z(
        t,
        "overflow",
        /*allow_overflow*/
        l[11] ? "visible" : "hidden"
      ), z(
        t,
        "flex-grow",
        /*scale*/
        l[12]
      ), z(t, "min-width", `calc(min(${/*min_width*/
      l[13]}px, 100%))`), z(t, "border-width", "var(--block-border-width)");
    },
    m(s, a) {
      Ft(s, t, a), f && f.m(t, null), n = !0;
    },
    p(s, a) {
      f && f.p && (!n || a & /*$$scope*/
      131072) && Lt(
        f,
        i,
        s,
        /*$$scope*/
        s[17],
        n ? yt(
          i,
          /*$$scope*/
          s[17],
          a,
          null
        ) : kt(
          /*$$scope*/
          s[17]
        ),
        null
      ), ze(
        /*tag*/
        s[14]
      )(t, _ = vt(o, [
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
      ])), D(
        t,
        "hidden",
        /*visible*/
        s[10] === !1
      ), D(
        t,
        "padded",
        /*padding*/
        s[6]
      ), D(
        t,
        "border_focus",
        /*border_mode*/
        s[5] === "focus"
      ), D(
        t,
        "border_contrast",
        /*border_mode*/
        s[5] === "contrast"
      ), D(t, "hide-container", !/*explicit_call*/
      s[8] && !/*container*/
      s[9]), a & /*height*/
      1 && z(
        t,
        "height",
        /*get_dimension*/
        s[15](
          /*height*/
          s[0]
        )
      ), a & /*width*/
      2 && z(t, "width", typeof /*width*/
      s[1] == "number" ? `calc(min(${/*width*/
      s[1]}px, 100%))` : (
        /*get_dimension*/
        s[15](
          /*width*/
          s[1]
        )
      )), a & /*variant*/
      16 && z(
        t,
        "border-style",
        /*variant*/
        s[4]
      ), a & /*allow_overflow*/
      2048 && z(
        t,
        "overflow",
        /*allow_overflow*/
        s[11] ? "visible" : "hidden"
      ), a & /*scale*/
      4096 && z(
        t,
        "flex-grow",
        /*scale*/
        s[12]
      ), a & /*min_width*/
      8192 && z(t, "min-width", `calc(min(${/*min_width*/
      s[13]}px, 100%))`);
    },
    i(s) {
      n || (it(f, s), n = !0);
    },
    o(s) {
      st(f, s), n = !1;
    },
    d(s) {
      s && wt(t), f && f.d(s);
    }
  };
}
function Vt(l) {
  let t, e = (
    /*tag*/
    l[14] && St(l)
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
      t || (it(e, n), t = !0);
    },
    o(n) {
      st(e, n), t = !1;
    },
    d(n) {
      e && e.d(n);
    }
  };
}
function jt(l, t, e) {
  let { $$slots: n = {}, $$scope: i } = t, { height: f = void 0 } = t, { width: o = void 0 } = t, { elem_id: _ = "" } = t, { elem_classes: s = [] } = t, { variant: a = "solid" } = t, { border_mode: u = "base" } = t, { padding: c = !0 } = t, { type: y = "normal" } = t, { test_id: g = void 0 } = t, { explicit_call: p = !1 } = t, { container: j = !0 } = t, { visible: L = !0 } = t, { allow_overflow: q = !0 } = t, { scale: C = null } = t, { min_width: d = 0 } = t, v = y === "fieldset" ? "fieldset" : "div";
  const S = (r) => {
    if (r !== void 0) {
      if (typeof r == "number")
        return r + "px";
      if (typeof r == "string")
        return r;
    }
  };
  return l.$$set = (r) => {
    "height" in r && e(0, f = r.height), "width" in r && e(1, o = r.width), "elem_id" in r && e(2, _ = r.elem_id), "elem_classes" in r && e(3, s = r.elem_classes), "variant" in r && e(4, a = r.variant), "border_mode" in r && e(5, u = r.border_mode), "padding" in r && e(6, c = r.padding), "type" in r && e(16, y = r.type), "test_id" in r && e(7, g = r.test_id), "explicit_call" in r && e(8, p = r.explicit_call), "container" in r && e(9, j = r.container), "visible" in r && e(10, L = r.visible), "allow_overflow" in r && e(11, q = r.allow_overflow), "scale" in r && e(12, C = r.scale), "min_width" in r && e(13, d = r.min_width), "$$scope" in r && e(17, i = r.$$scope);
  }, [
    f,
    o,
    _,
    s,
    a,
    u,
    c,
    g,
    p,
    j,
    L,
    q,
    C,
    d,
    v,
    S,
    y,
    i,
    n
  ];
}
class Nt extends bt {
  constructor(t) {
    super(), qt(this, t, jt, Vt, Ct, {
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
  SvelteComponent: Mt,
  attr: zt,
  create_slot: It,
  detach: Pt,
  element: Tt,
  get_all_dirty_from_scope: Zt,
  get_slot_changes: Bt,
  init: At,
  insert: Et,
  safe_not_equal: Dt,
  transition_in: Ot,
  transition_out: Rt,
  update_slot_base: Ut
} = window.__gradio__svelte__internal;
function Xt(l) {
  let t, e;
  const n = (
    /*#slots*/
    l[1].default
  ), i = It(
    n,
    l,
    /*$$scope*/
    l[0],
    null
  );
  return {
    c() {
      t = Tt("div"), i && i.c(), zt(t, "class", "svelte-1hnfib2");
    },
    m(f, o) {
      Et(f, t, o), i && i.m(t, null), e = !0;
    },
    p(f, [o]) {
      i && i.p && (!e || o & /*$$scope*/
      1) && Ut(
        i,
        n,
        f,
        /*$$scope*/
        f[0],
        e ? Bt(
          n,
          /*$$scope*/
          f[0],
          o,
          null
        ) : Zt(
          /*$$scope*/
          f[0]
        ),
        null
      );
    },
    i(f) {
      e || (Ot(i, f), e = !0);
    },
    o(f) {
      Rt(i, f), e = !1;
    },
    d(f) {
      f && Pt(t), i && i.d(f);
    }
  };
}
function Yt(l, t, e) {
  let { $$slots: n = {}, $$scope: i } = t;
  return l.$$set = (f) => {
    "$$scope" in f && e(0, i = f.$$scope);
  }, [i, n];
}
class Gt extends Mt {
  constructor(t) {
    super(), At(this, t, Yt, Xt, Dt, {});
  }
}
const {
  SvelteComponent: Ht,
  attr: Ie,
  check_outros: Jt,
  create_component: Kt,
  create_slot: Qt,
  destroy_component: Wt,
  detach: he,
  element: xt,
  empty: $t,
  get_all_dirty_from_scope: el,
  get_slot_changes: tl,
  group_outros: ll,
  init: nl,
  insert: we,
  mount_component: il,
  safe_not_equal: sl,
  set_data: fl,
  space: ol,
  text: _l,
  toggle_class: x,
  transition_in: _e,
  transition_out: pe,
  update_slot_base: al
} = window.__gradio__svelte__internal;
function Pe(l) {
  let t, e;
  return t = new Gt({
    props: {
      $$slots: { default: [rl] },
      $$scope: { ctx: l }
    }
  }), {
    c() {
      Kt(t.$$.fragment);
    },
    m(n, i) {
      il(t, n, i), e = !0;
    },
    p(n, i) {
      const f = {};
      i & /*$$scope, info*/
      10 && (f.$$scope = { dirty: i, ctx: n }), t.$set(f);
    },
    i(n) {
      e || (_e(t.$$.fragment, n), e = !0);
    },
    o(n) {
      pe(t.$$.fragment, n), e = !1;
    },
    d(n) {
      Wt(t, n);
    }
  };
}
function rl(l) {
  let t;
  return {
    c() {
      t = _l(
        /*info*/
        l[1]
      );
    },
    m(e, n) {
      we(e, t, n);
    },
    p(e, n) {
      n & /*info*/
      2 && fl(
        t,
        /*info*/
        e[1]
      );
    },
    d(e) {
      e && he(t);
    }
  };
}
function ul(l) {
  let t, e, n, i;
  const f = (
    /*#slots*/
    l[2].default
  ), o = Qt(
    f,
    l,
    /*$$scope*/
    l[3],
    null
  );
  let _ = (
    /*info*/
    l[1] && Pe(l)
  );
  return {
    c() {
      t = xt("span"), o && o.c(), e = ol(), _ && _.c(), n = $t(), Ie(t, "data-testid", "block-info"), Ie(t, "class", "svelte-22c38v"), x(t, "sr-only", !/*show_label*/
      l[0]), x(t, "hide", !/*show_label*/
      l[0]), x(
        t,
        "has-info",
        /*info*/
        l[1] != null
      );
    },
    m(s, a) {
      we(s, t, a), o && o.m(t, null), we(s, e, a), _ && _.m(s, a), we(s, n, a), i = !0;
    },
    p(s, [a]) {
      o && o.p && (!i || a & /*$$scope*/
      8) && al(
        o,
        f,
        s,
        /*$$scope*/
        s[3],
        i ? tl(
          f,
          /*$$scope*/
          s[3],
          a,
          null
        ) : el(
          /*$$scope*/
          s[3]
        ),
        null
      ), (!i || a & /*show_label*/
      1) && x(t, "sr-only", !/*show_label*/
      s[0]), (!i || a & /*show_label*/
      1) && x(t, "hide", !/*show_label*/
      s[0]), (!i || a & /*info*/
      2) && x(
        t,
        "has-info",
        /*info*/
        s[1] != null
      ), /*info*/
      s[1] ? _ ? (_.p(s, a), a & /*info*/
      2 && _e(_, 1)) : (_ = Pe(s), _.c(), _e(_, 1), _.m(n.parentNode, n)) : _ && (ll(), pe(_, 1, 1, () => {
        _ = null;
      }), Jt());
    },
    i(s) {
      i || (_e(o, s), _e(_), i = !0);
    },
    o(s) {
      pe(o, s), pe(_), i = !1;
    },
    d(s) {
      s && (he(t), he(e), he(n)), o && o.d(s), _ && _.d(s);
    }
  };
}
function cl(l, t, e) {
  let { $$slots: n = {}, $$scope: i } = t, { show_label: f = !0 } = t, { info: o = void 0 } = t;
  return l.$$set = (_) => {
    "show_label" in _ && e(0, f = _.show_label), "info" in _ && e(1, o = _.info), "$$scope" in _ && e(3, i = _.$$scope);
  }, [f, o, n, i];
}
class dl extends Ht {
  constructor(t) {
    super(), nl(this, t, cl, ul, sl, { show_label: 0, info: 1 });
  }
}
const ml = [
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
], Te = {
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
ml.reduce(
  (l, { color: t, primary: e, secondary: n }) => ({
    ...l,
    [t]: {
      primary: Te[t][e],
      secondary: Te[t][n]
    }
  }),
  {}
);
function le(l) {
  let t = ["", "k", "M", "G", "T", "P", "E", "Z"], e = 0;
  for (; l > 1e3 && e < t.length - 1; )
    l /= 1e3, e++;
  let n = t[e];
  return (Number.isInteger(l) ? l : l.toFixed(1)) + n;
}
function ke() {
}
function bl(l, t) {
  return l != l ? t == t : l !== t || l && typeof l == "object" || typeof l == "function";
}
const ft = typeof window < "u";
let Ze = ft ? () => window.performance.now() : () => Date.now(), ot = ft ? (l) => requestAnimationFrame(l) : ke;
const ne = /* @__PURE__ */ new Set();
function _t(l) {
  ne.forEach((t) => {
    t.c(l) || (ne.delete(t), t.f());
  }), ne.size !== 0 && ot(_t);
}
function gl(l) {
  let t;
  return ne.size === 0 && ot(_t), {
    promise: new Promise((e) => {
      ne.add(t = { c: l, f: e });
    }),
    abort() {
      ne.delete(t);
    }
  };
}
const $ = [];
function hl(l, t = ke) {
  let e;
  const n = /* @__PURE__ */ new Set();
  function i(_) {
    if (bl(l, _) && (l = _, e)) {
      const s = !$.length;
      for (const a of n)
        a[1](), $.push(a, l);
      if (s) {
        for (let a = 0; a < $.length; a += 2)
          $[a][0]($[a + 1]);
        $.length = 0;
      }
    }
  }
  function f(_) {
    i(_(l));
  }
  function o(_, s = ke) {
    const a = [_, s];
    return n.add(a), n.size === 1 && (e = t(i, f) || ke), _(l), () => {
      n.delete(a), n.size === 0 && e && (e(), e = null);
    };
  }
  return { set: i, update: f, subscribe: o };
}
function Be(l) {
  return Object.prototype.toString.call(l) === "[object Date]";
}
function qe(l, t, e, n) {
  if (typeof e == "number" || Be(e)) {
    const i = n - e, f = (e - t) / (l.dt || 1 / 60), o = l.opts.stiffness * i, _ = l.opts.damping * f, s = (o - _) * l.inv_mass, a = (f + s) * l.dt;
    return Math.abs(a) < l.opts.precision && Math.abs(i) < l.opts.precision ? n : (l.settled = !1, Be(e) ? new Date(e.getTime() + a) : e + a);
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
function Ae(l, t = {}) {
  const e = hl(l), { stiffness: n = 0.15, damping: i = 0.8, precision: f = 0.01 } = t;
  let o, _, s, a = l, u = l, c = 1, y = 0, g = !1;
  function p(L, q = {}) {
    u = L;
    const C = s = {};
    return l == null || q.hard || j.stiffness >= 1 && j.damping >= 1 ? (g = !0, o = Ze(), a = L, e.set(l = u), Promise.resolve()) : (q.soft && (y = 1 / ((q.soft === !0 ? 0.5 : +q.soft) * 60), c = 0), _ || (o = Ze(), g = !1, _ = gl((d) => {
      if (g)
        return g = !1, _ = null, !1;
      c = Math.min(c + y, 1);
      const v = {
        inv_mass: c,
        opts: j,
        settled: !0,
        dt: (d - o) * 60 / 1e3
      }, S = qe(v, a, l, u);
      return o = d, a = l, e.set(l = S), v.settled && (_ = null), !v.settled;
    })), new Promise((d) => {
      _.promise.then(() => {
        C === s && d();
      });
    }));
  }
  const j = {
    set: p,
    update: (L, q) => p(L(u, l), q),
    subscribe: e.subscribe,
    stiffness: n,
    damping: i,
    precision: f
  };
  return j;
}
const {
  SvelteComponent: wl,
  append: T,
  attr: F,
  component_subscribe: Ee,
  detach: pl,
  element: kl,
  init: yl,
  insert: vl,
  noop: De,
  safe_not_equal: ql,
  set_style: de,
  svg_element: Z,
  toggle_class: Oe
} = window.__gradio__svelte__internal, { onMount: Fl } = window.__gradio__svelte__internal;
function Cl(l) {
  let t, e, n, i, f, o, _, s, a, u, c, y;
  return {
    c() {
      t = kl("div"), e = Z("svg"), n = Z("g"), i = Z("path"), f = Z("path"), o = Z("path"), _ = Z("path"), s = Z("g"), a = Z("path"), u = Z("path"), c = Z("path"), y = Z("path"), F(i, "d", "M255.926 0.754768L509.702 139.936V221.027L255.926 81.8465V0.754768Z"), F(i, "fill", "#FF7C00"), F(i, "fill-opacity", "0.4"), F(i, "class", "svelte-43sxxs"), F(f, "d", "M509.69 139.936L254.981 279.641V361.255L509.69 221.55V139.936Z"), F(f, "fill", "#FF7C00"), F(f, "class", "svelte-43sxxs"), F(o, "d", "M0.250138 139.937L254.981 279.641V361.255L0.250138 221.55V139.937Z"), F(o, "fill", "#FF7C00"), F(o, "fill-opacity", "0.4"), F(o, "class", "svelte-43sxxs"), F(_, "d", "M255.923 0.232622L0.236328 139.936V221.55L255.923 81.8469V0.232622Z"), F(_, "fill", "#FF7C00"), F(_, "class", "svelte-43sxxs"), de(n, "transform", "translate(" + /*$top*/
      l[1][0] + "px, " + /*$top*/
      l[1][1] + "px)"), F(a, "d", "M255.926 141.5L509.702 280.681V361.773L255.926 222.592V141.5Z"), F(a, "fill", "#FF7C00"), F(a, "fill-opacity", "0.4"), F(a, "class", "svelte-43sxxs"), F(u, "d", "M509.69 280.679L254.981 420.384V501.998L509.69 362.293V280.679Z"), F(u, "fill", "#FF7C00"), F(u, "class", "svelte-43sxxs"), F(c, "d", "M0.250138 280.681L254.981 420.386V502L0.250138 362.295V280.681Z"), F(c, "fill", "#FF7C00"), F(c, "fill-opacity", "0.4"), F(c, "class", "svelte-43sxxs"), F(y, "d", "M255.923 140.977L0.236328 280.68V362.294L255.923 222.591V140.977Z"), F(y, "fill", "#FF7C00"), F(y, "class", "svelte-43sxxs"), de(s, "transform", "translate(" + /*$bottom*/
      l[2][0] + "px, " + /*$bottom*/
      l[2][1] + "px)"), F(e, "viewBox", "-1200 -1200 3000 3000"), F(e, "fill", "none"), F(e, "xmlns", "http://www.w3.org/2000/svg"), F(e, "class", "svelte-43sxxs"), F(t, "class", "svelte-43sxxs"), Oe(
        t,
        "margin",
        /*margin*/
        l[0]
      );
    },
    m(g, p) {
      vl(g, t, p), T(t, e), T(e, n), T(n, i), T(n, f), T(n, o), T(n, _), T(e, s), T(s, a), T(s, u), T(s, c), T(s, y);
    },
    p(g, [p]) {
      p & /*$top*/
      2 && de(n, "transform", "translate(" + /*$top*/
      g[1][0] + "px, " + /*$top*/
      g[1][1] + "px)"), p & /*$bottom*/
      4 && de(s, "transform", "translate(" + /*$bottom*/
      g[2][0] + "px, " + /*$bottom*/
      g[2][1] + "px)"), p & /*margin*/
      1 && Oe(
        t,
        "margin",
        /*margin*/
        g[0]
      );
    },
    i: De,
    o: De,
    d(g) {
      g && pl(t);
    }
  };
}
function Ll(l, t, e) {
  let n, i, { margin: f = !0 } = t;
  const o = Ae([0, 0]);
  Ee(l, o, (y) => e(1, n = y));
  const _ = Ae([0, 0]);
  Ee(l, _, (y) => e(2, i = y));
  let s;
  async function a() {
    await Promise.all([o.set([125, 140]), _.set([-125, -140])]), await Promise.all([o.set([-125, 140]), _.set([125, -140])]), await Promise.all([o.set([-125, 0]), _.set([125, -0])]), await Promise.all([o.set([125, 0]), _.set([-125, 0])]);
  }
  async function u() {
    await a(), s || u();
  }
  async function c() {
    await Promise.all([o.set([125, 0]), _.set([-125, 0])]), u();
  }
  return Fl(() => (c(), () => s = !0)), l.$$set = (y) => {
    "margin" in y && e(0, f = y.margin);
  }, [f, n, i, o, _];
}
class Sl extends wl {
  constructor(t) {
    super(), yl(this, t, Ll, Cl, ql, { margin: 0 });
  }
}
const {
  SvelteComponent: Vl,
  append: W,
  attr: O,
  binding_callbacks: Re,
  check_outros: at,
  create_component: jl,
  create_slot: Nl,
  destroy_component: Ml,
  destroy_each: rt,
  detach: h,
  element: X,
  empty: fe,
  ensure_array_like: ye,
  get_all_dirty_from_scope: zl,
  get_slot_changes: Il,
  group_outros: ut,
  init: Pl,
  insert: w,
  mount_component: Tl,
  noop: Fe,
  safe_not_equal: Zl,
  set_data: P,
  set_style: H,
  space: R,
  text: N,
  toggle_class: I,
  transition_in: ie,
  transition_out: se,
  update_slot_base: Bl
} = window.__gradio__svelte__internal, { tick: Al } = window.__gradio__svelte__internal, { onDestroy: El } = window.__gradio__svelte__internal, Dl = (l) => ({}), Ue = (l) => ({});
function Xe(l, t, e) {
  const n = l.slice();
  return n[38] = t[e], n[40] = e, n;
}
function Ye(l, t, e) {
  const n = l.slice();
  return n[38] = t[e], n;
}
function Ol(l) {
  let t, e = (
    /*i18n*/
    l[1]("common.error") + ""
  ), n, i, f;
  const o = (
    /*#slots*/
    l[29].error
  ), _ = Nl(
    o,
    l,
    /*$$scope*/
    l[28],
    Ue
  );
  return {
    c() {
      t = X("span"), n = N(e), i = R(), _ && _.c(), O(t, "class", "error svelte-1yserjw");
    },
    m(s, a) {
      w(s, t, a), W(t, n), w(s, i, a), _ && _.m(s, a), f = !0;
    },
    p(s, a) {
      (!f || a[0] & /*i18n*/
      2) && e !== (e = /*i18n*/
      s[1]("common.error") + "") && P(n, e), _ && _.p && (!f || a[0] & /*$$scope*/
      268435456) && Bl(
        _,
        o,
        s,
        /*$$scope*/
        s[28],
        f ? Il(
          o,
          /*$$scope*/
          s[28],
          a,
          Dl
        ) : zl(
          /*$$scope*/
          s[28]
        ),
        Ue
      );
    },
    i(s) {
      f || (ie(_, s), f = !0);
    },
    o(s) {
      se(_, s), f = !1;
    },
    d(s) {
      s && (h(t), h(i)), _ && _.d(s);
    }
  };
}
function Rl(l) {
  let t, e, n, i, f, o, _, s, a, u = (
    /*variant*/
    l[8] === "default" && /*show_eta_bar*/
    l[18] && /*show_progress*/
    l[6] === "full" && Ge(l)
  );
  function c(d, v) {
    if (
      /*progress*/
      d[7]
    )
      return Yl;
    if (
      /*queue_position*/
      d[2] !== null && /*queue_size*/
      d[3] !== void 0 && /*queue_position*/
      d[2] >= 0
    )
      return Xl;
    if (
      /*queue_position*/
      d[2] === 0
    )
      return Ul;
  }
  let y = c(l), g = y && y(l), p = (
    /*timer*/
    l[5] && Ke(l)
  );
  const j = [Kl, Jl], L = [];
  function q(d, v) {
    return (
      /*last_progress_level*/
      d[15] != null ? 0 : (
        /*show_progress*/
        d[6] === "full" ? 1 : -1
      )
    );
  }
  ~(f = q(l)) && (o = L[f] = j[f](l));
  let C = !/*timer*/
  l[5] && lt(l);
  return {
    c() {
      u && u.c(), t = R(), e = X("div"), g && g.c(), n = R(), p && p.c(), i = R(), o && o.c(), _ = R(), C && C.c(), s = fe(), O(e, "class", "progress-text svelte-1yserjw"), I(
        e,
        "meta-text-center",
        /*variant*/
        l[8] === "center"
      ), I(
        e,
        "meta-text",
        /*variant*/
        l[8] === "default"
      );
    },
    m(d, v) {
      u && u.m(d, v), w(d, t, v), w(d, e, v), g && g.m(e, null), W(e, n), p && p.m(e, null), w(d, i, v), ~f && L[f].m(d, v), w(d, _, v), C && C.m(d, v), w(d, s, v), a = !0;
    },
    p(d, v) {
      /*variant*/
      d[8] === "default" && /*show_eta_bar*/
      d[18] && /*show_progress*/
      d[6] === "full" ? u ? u.p(d, v) : (u = Ge(d), u.c(), u.m(t.parentNode, t)) : u && (u.d(1), u = null), y === (y = c(d)) && g ? g.p(d, v) : (g && g.d(1), g = y && y(d), g && (g.c(), g.m(e, n))), /*timer*/
      d[5] ? p ? p.p(d, v) : (p = Ke(d), p.c(), p.m(e, null)) : p && (p.d(1), p = null), (!a || v[0] & /*variant*/
      256) && I(
        e,
        "meta-text-center",
        /*variant*/
        d[8] === "center"
      ), (!a || v[0] & /*variant*/
      256) && I(
        e,
        "meta-text",
        /*variant*/
        d[8] === "default"
      );
      let S = f;
      f = q(d), f === S ? ~f && L[f].p(d, v) : (o && (ut(), se(L[S], 1, 1, () => {
        L[S] = null;
      }), at()), ~f ? (o = L[f], o ? o.p(d, v) : (o = L[f] = j[f](d), o.c()), ie(o, 1), o.m(_.parentNode, _)) : o = null), /*timer*/
      d[5] ? C && (C.d(1), C = null) : C ? C.p(d, v) : (C = lt(d), C.c(), C.m(s.parentNode, s));
    },
    i(d) {
      a || (ie(o), a = !0);
    },
    o(d) {
      se(o), a = !1;
    },
    d(d) {
      d && (h(t), h(e), h(i), h(_), h(s)), u && u.d(d), g && g.d(), p && p.d(), ~f && L[f].d(d), C && C.d(d);
    }
  };
}
function Ge(l) {
  let t, e = `translateX(${/*eta_level*/
  (l[17] || 0) * 100 - 100}%)`;
  return {
    c() {
      t = X("div"), O(t, "class", "eta-bar svelte-1yserjw"), H(t, "transform", e);
    },
    m(n, i) {
      w(n, t, i);
    },
    p(n, i) {
      i[0] & /*eta_level*/
      131072 && e !== (e = `translateX(${/*eta_level*/
      (n[17] || 0) * 100 - 100}%)`) && H(t, "transform", e);
    },
    d(n) {
      n && h(t);
    }
  };
}
function Ul(l) {
  let t;
  return {
    c() {
      t = N("processing |");
    },
    m(e, n) {
      w(e, t, n);
    },
    p: Fe,
    d(e) {
      e && h(t);
    }
  };
}
function Xl(l) {
  let t, e = (
    /*queue_position*/
    l[2] + 1 + ""
  ), n, i, f, o;
  return {
    c() {
      t = N("queue: "), n = N(e), i = N("/"), f = N(
        /*queue_size*/
        l[3]
      ), o = N(" |");
    },
    m(_, s) {
      w(_, t, s), w(_, n, s), w(_, i, s), w(_, f, s), w(_, o, s);
    },
    p(_, s) {
      s[0] & /*queue_position*/
      4 && e !== (e = /*queue_position*/
      _[2] + 1 + "") && P(n, e), s[0] & /*queue_size*/
      8 && P(
        f,
        /*queue_size*/
        _[3]
      );
    },
    d(_) {
      _ && (h(t), h(n), h(i), h(f), h(o));
    }
  };
}
function Yl(l) {
  let t, e = ye(
    /*progress*/
    l[7]
  ), n = [];
  for (let i = 0; i < e.length; i += 1)
    n[i] = Je(Ye(l, e, i));
  return {
    c() {
      for (let i = 0; i < n.length; i += 1)
        n[i].c();
      t = fe();
    },
    m(i, f) {
      for (let o = 0; o < n.length; o += 1)
        n[o] && n[o].m(i, f);
      w(i, t, f);
    },
    p(i, f) {
      if (f[0] & /*progress*/
      128) {
        e = ye(
          /*progress*/
          i[7]
        );
        let o;
        for (o = 0; o < e.length; o += 1) {
          const _ = Ye(i, e, o);
          n[o] ? n[o].p(_, f) : (n[o] = Je(_), n[o].c(), n[o].m(t.parentNode, t));
        }
        for (; o < n.length; o += 1)
          n[o].d(1);
        n.length = e.length;
      }
    },
    d(i) {
      i && h(t), rt(n, i);
    }
  };
}
function He(l) {
  let t, e = (
    /*p*/
    l[38].unit + ""
  ), n, i, f = " ", o;
  function _(u, c) {
    return (
      /*p*/
      u[38].length != null ? Hl : Gl
    );
  }
  let s = _(l), a = s(l);
  return {
    c() {
      a.c(), t = R(), n = N(e), i = N(" | "), o = N(f);
    },
    m(u, c) {
      a.m(u, c), w(u, t, c), w(u, n, c), w(u, i, c), w(u, o, c);
    },
    p(u, c) {
      s === (s = _(u)) && a ? a.p(u, c) : (a.d(1), a = s(u), a && (a.c(), a.m(t.parentNode, t))), c[0] & /*progress*/
      128 && e !== (e = /*p*/
      u[38].unit + "") && P(n, e);
    },
    d(u) {
      u && (h(t), h(n), h(i), h(o)), a.d(u);
    }
  };
}
function Gl(l) {
  let t = le(
    /*p*/
    l[38].index || 0
  ) + "", e;
  return {
    c() {
      e = N(t);
    },
    m(n, i) {
      w(n, e, i);
    },
    p(n, i) {
      i[0] & /*progress*/
      128 && t !== (t = le(
        /*p*/
        n[38].index || 0
      ) + "") && P(e, t);
    },
    d(n) {
      n && h(e);
    }
  };
}
function Hl(l) {
  let t = le(
    /*p*/
    l[38].index || 0
  ) + "", e, n, i = le(
    /*p*/
    l[38].length
  ) + "", f;
  return {
    c() {
      e = N(t), n = N("/"), f = N(i);
    },
    m(o, _) {
      w(o, e, _), w(o, n, _), w(o, f, _);
    },
    p(o, _) {
      _[0] & /*progress*/
      128 && t !== (t = le(
        /*p*/
        o[38].index || 0
      ) + "") && P(e, t), _[0] & /*progress*/
      128 && i !== (i = le(
        /*p*/
        o[38].length
      ) + "") && P(f, i);
    },
    d(o) {
      o && (h(e), h(n), h(f));
    }
  };
}
function Je(l) {
  let t, e = (
    /*p*/
    l[38].index != null && He(l)
  );
  return {
    c() {
      e && e.c(), t = fe();
    },
    m(n, i) {
      e && e.m(n, i), w(n, t, i);
    },
    p(n, i) {
      /*p*/
      n[38].index != null ? e ? e.p(n, i) : (e = He(n), e.c(), e.m(t.parentNode, t)) : e && (e.d(1), e = null);
    },
    d(n) {
      n && h(t), e && e.d(n);
    }
  };
}
function Ke(l) {
  let t, e = (
    /*eta*/
    l[0] ? `/${/*formatted_eta*/
    l[19]}` : ""
  ), n, i;
  return {
    c() {
      t = N(
        /*formatted_timer*/
        l[20]
      ), n = N(e), i = N("s");
    },
    m(f, o) {
      w(f, t, o), w(f, n, o), w(f, i, o);
    },
    p(f, o) {
      o[0] & /*formatted_timer*/
      1048576 && P(
        t,
        /*formatted_timer*/
        f[20]
      ), o[0] & /*eta, formatted_eta*/
      524289 && e !== (e = /*eta*/
      f[0] ? `/${/*formatted_eta*/
      f[19]}` : "") && P(n, e);
    },
    d(f) {
      f && (h(t), h(n), h(i));
    }
  };
}
function Jl(l) {
  let t, e;
  return t = new Sl({
    props: { margin: (
      /*variant*/
      l[8] === "default"
    ) }
  }), {
    c() {
      jl(t.$$.fragment);
    },
    m(n, i) {
      Tl(t, n, i), e = !0;
    },
    p(n, i) {
      const f = {};
      i[0] & /*variant*/
      256 && (f.margin = /*variant*/
      n[8] === "default"), t.$set(f);
    },
    i(n) {
      e || (ie(t.$$.fragment, n), e = !0);
    },
    o(n) {
      se(t.$$.fragment, n), e = !1;
    },
    d(n) {
      Ml(t, n);
    }
  };
}
function Kl(l) {
  let t, e, n, i, f, o = `${/*last_progress_level*/
  l[15] * 100}%`, _ = (
    /*progress*/
    l[7] != null && Qe(l)
  );
  return {
    c() {
      t = X("div"), e = X("div"), _ && _.c(), n = R(), i = X("div"), f = X("div"), O(e, "class", "progress-level-inner svelte-1yserjw"), O(f, "class", "progress-bar svelte-1yserjw"), H(f, "width", o), O(i, "class", "progress-bar-wrap svelte-1yserjw"), O(t, "class", "progress-level svelte-1yserjw");
    },
    m(s, a) {
      w(s, t, a), W(t, e), _ && _.m(e, null), W(t, n), W(t, i), W(i, f), l[30](f);
    },
    p(s, a) {
      /*progress*/
      s[7] != null ? _ ? _.p(s, a) : (_ = Qe(s), _.c(), _.m(e, null)) : _ && (_.d(1), _ = null), a[0] & /*last_progress_level*/
      32768 && o !== (o = `${/*last_progress_level*/
      s[15] * 100}%`) && H(f, "width", o);
    },
    i: Fe,
    o: Fe,
    d(s) {
      s && h(t), _ && _.d(), l[30](null);
    }
  };
}
function Qe(l) {
  let t, e = ye(
    /*progress*/
    l[7]
  ), n = [];
  for (let i = 0; i < e.length; i += 1)
    n[i] = tt(Xe(l, e, i));
  return {
    c() {
      for (let i = 0; i < n.length; i += 1)
        n[i].c();
      t = fe();
    },
    m(i, f) {
      for (let o = 0; o < n.length; o += 1)
        n[o] && n[o].m(i, f);
      w(i, t, f);
    },
    p(i, f) {
      if (f[0] & /*progress_level, progress*/
      16512) {
        e = ye(
          /*progress*/
          i[7]
        );
        let o;
        for (o = 0; o < e.length; o += 1) {
          const _ = Xe(i, e, o);
          n[o] ? n[o].p(_, f) : (n[o] = tt(_), n[o].c(), n[o].m(t.parentNode, t));
        }
        for (; o < n.length; o += 1)
          n[o].d(1);
        n.length = e.length;
      }
    },
    d(i) {
      i && h(t), rt(n, i);
    }
  };
}
function We(l) {
  let t, e, n, i, f = (
    /*i*/
    l[40] !== 0 && Ql()
  ), o = (
    /*p*/
    l[38].desc != null && xe(l)
  ), _ = (
    /*p*/
    l[38].desc != null && /*progress_level*/
    l[14] && /*progress_level*/
    l[14][
      /*i*/
      l[40]
    ] != null && $e()
  ), s = (
    /*progress_level*/
    l[14] != null && et(l)
  );
  return {
    c() {
      f && f.c(), t = R(), o && o.c(), e = R(), _ && _.c(), n = R(), s && s.c(), i = fe();
    },
    m(a, u) {
      f && f.m(a, u), w(a, t, u), o && o.m(a, u), w(a, e, u), _ && _.m(a, u), w(a, n, u), s && s.m(a, u), w(a, i, u);
    },
    p(a, u) {
      /*p*/
      a[38].desc != null ? o ? o.p(a, u) : (o = xe(a), o.c(), o.m(e.parentNode, e)) : o && (o.d(1), o = null), /*p*/
      a[38].desc != null && /*progress_level*/
      a[14] && /*progress_level*/
      a[14][
        /*i*/
        a[40]
      ] != null ? _ || (_ = $e(), _.c(), _.m(n.parentNode, n)) : _ && (_.d(1), _ = null), /*progress_level*/
      a[14] != null ? s ? s.p(a, u) : (s = et(a), s.c(), s.m(i.parentNode, i)) : s && (s.d(1), s = null);
    },
    d(a) {
      a && (h(t), h(e), h(n), h(i)), f && f.d(a), o && o.d(a), _ && _.d(a), s && s.d(a);
    }
  };
}
function Ql(l) {
  let t;
  return {
    c() {
      t = N(" /");
    },
    m(e, n) {
      w(e, t, n);
    },
    d(e) {
      e && h(t);
    }
  };
}
function xe(l) {
  let t = (
    /*p*/
    l[38].desc + ""
  ), e;
  return {
    c() {
      e = N(t);
    },
    m(n, i) {
      w(n, e, i);
    },
    p(n, i) {
      i[0] & /*progress*/
      128 && t !== (t = /*p*/
      n[38].desc + "") && P(e, t);
    },
    d(n) {
      n && h(e);
    }
  };
}
function $e(l) {
  let t;
  return {
    c() {
      t = N("-");
    },
    m(e, n) {
      w(e, t, n);
    },
    d(e) {
      e && h(t);
    }
  };
}
function et(l) {
  let t = (100 * /*progress_level*/
  (l[14][
    /*i*/
    l[40]
  ] || 0)).toFixed(1) + "", e, n;
  return {
    c() {
      e = N(t), n = N("%");
    },
    m(i, f) {
      w(i, e, f), w(i, n, f);
    },
    p(i, f) {
      f[0] & /*progress_level*/
      16384 && t !== (t = (100 * /*progress_level*/
      (i[14][
        /*i*/
        i[40]
      ] || 0)).toFixed(1) + "") && P(e, t);
    },
    d(i) {
      i && (h(e), h(n));
    }
  };
}
function tt(l) {
  let t, e = (
    /*p*/
    (l[38].desc != null || /*progress_level*/
    l[14] && /*progress_level*/
    l[14][
      /*i*/
      l[40]
    ] != null) && We(l)
  );
  return {
    c() {
      e && e.c(), t = fe();
    },
    m(n, i) {
      e && e.m(n, i), w(n, t, i);
    },
    p(n, i) {
      /*p*/
      n[38].desc != null || /*progress_level*/
      n[14] && /*progress_level*/
      n[14][
        /*i*/
        n[40]
      ] != null ? e ? e.p(n, i) : (e = We(n), e.c(), e.m(t.parentNode, t)) : e && (e.d(1), e = null);
    },
    d(n) {
      n && h(t), e && e.d(n);
    }
  };
}
function lt(l) {
  let t, e;
  return {
    c() {
      t = X("p"), e = N(
        /*loading_text*/
        l[9]
      ), O(t, "class", "loading svelte-1yserjw");
    },
    m(n, i) {
      w(n, t, i), W(t, e);
    },
    p(n, i) {
      i[0] & /*loading_text*/
      512 && P(
        e,
        /*loading_text*/
        n[9]
      );
    },
    d(n) {
      n && h(t);
    }
  };
}
function Wl(l) {
  let t, e, n, i, f;
  const o = [Rl, Ol], _ = [];
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
      t = X("div"), n && n.c(), O(t, "class", i = "wrap " + /*variant*/
      l[8] + " " + /*show_progress*/
      l[6] + " svelte-1yserjw"), I(t, "hide", !/*status*/
      l[4] || /*status*/
      l[4] === "complete" || /*show_progress*/
      l[6] === "hidden"), I(
        t,
        "translucent",
        /*variant*/
        l[8] === "center" && /*status*/
        (l[4] === "pending" || /*status*/
        l[4] === "error") || /*translucent*/
        l[11] || /*show_progress*/
        l[6] === "minimal"
      ), I(
        t,
        "generating",
        /*status*/
        l[4] === "generating"
      ), I(
        t,
        "border",
        /*border*/
        l[12]
      ), H(
        t,
        "position",
        /*absolute*/
        l[10] ? "absolute" : "static"
      ), H(
        t,
        "padding",
        /*absolute*/
        l[10] ? "0" : "var(--size-8) 0"
      );
    },
    m(a, u) {
      w(a, t, u), ~e && _[e].m(t, null), l[31](t), f = !0;
    },
    p(a, u) {
      let c = e;
      e = s(a), e === c ? ~e && _[e].p(a, u) : (n && (ut(), se(_[c], 1, 1, () => {
        _[c] = null;
      }), at()), ~e ? (n = _[e], n ? n.p(a, u) : (n = _[e] = o[e](a), n.c()), ie(n, 1), n.m(t, null)) : n = null), (!f || u[0] & /*variant, show_progress*/
      320 && i !== (i = "wrap " + /*variant*/
      a[8] + " " + /*show_progress*/
      a[6] + " svelte-1yserjw")) && O(t, "class", i), (!f || u[0] & /*variant, show_progress, status, show_progress*/
      336) && I(t, "hide", !/*status*/
      a[4] || /*status*/
      a[4] === "complete" || /*show_progress*/
      a[6] === "hidden"), (!f || u[0] & /*variant, show_progress, variant, status, translucent, show_progress*/
      2384) && I(
        t,
        "translucent",
        /*variant*/
        a[8] === "center" && /*status*/
        (a[4] === "pending" || /*status*/
        a[4] === "error") || /*translucent*/
        a[11] || /*show_progress*/
        a[6] === "minimal"
      ), (!f || u[0] & /*variant, show_progress, status*/
      336) && I(
        t,
        "generating",
        /*status*/
        a[4] === "generating"
      ), (!f || u[0] & /*variant, show_progress, border*/
      4416) && I(
        t,
        "border",
        /*border*/
        a[12]
      ), u[0] & /*absolute*/
      1024 && H(
        t,
        "position",
        /*absolute*/
        a[10] ? "absolute" : "static"
      ), u[0] & /*absolute*/
      1024 && H(
        t,
        "padding",
        /*absolute*/
        a[10] ? "0" : "var(--size-8) 0"
      );
    },
    i(a) {
      f || (ie(n), f = !0);
    },
    o(a) {
      se(n), f = !1;
    },
    d(a) {
      a && h(t), ~e && _[e].d(), l[31](null);
    }
  };
}
let me = [], ve = !1;
async function xl(l, t = !0) {
  if (!(window.__gradio_mode__ === "website" || window.__gradio_mode__ !== "app" && t !== !0)) {
    if (me.push(l), !ve)
      ve = !0;
    else
      return;
    await Al(), requestAnimationFrame(() => {
      let e = [0, 0];
      for (let n = 0; n < me.length; n++) {
        const f = me[n].getBoundingClientRect();
        (n === 0 || f.top + window.scrollY <= e[0]) && (e[0] = f.top + window.scrollY, e[1] = n);
      }
      window.scrollTo({ top: e[0] - 20, behavior: "smooth" }), ve = !1, me = [];
    });
  }
}
function $l(l, t, e) {
  let n, { $$slots: i = {}, $$scope: f } = t, { i18n: o } = t, { eta: _ = null } = t, { queue_position: s } = t, { queue_size: a } = t, { status: u } = t, { scroll_to_output: c = !1 } = t, { timer: y = !0 } = t, { show_progress: g = "full" } = t, { message: p = null } = t, { progress: j = null } = t, { variant: L = "default" } = t, { loading_text: q = "Loading..." } = t, { absolute: C = !0 } = t, { translucent: d = !1 } = t, { border: v = !1 } = t, { autoscroll: S } = t, r, k = !1, Y = 0, M = 0, G = null, B = null, ae = 0, U = null, J, A = null, re = !0;
  const m = () => {
    e(0, _ = e(26, G = e(19, ce = null))), e(24, Y = performance.now()), e(25, M = 0), k = !0, E();
  };
  function E() {
    requestAnimationFrame(() => {
      e(25, M = (performance.now() - Y) / 1e3), k && E();
    });
  }
  function ue() {
    e(25, M = 0), e(0, _ = e(26, G = e(19, ce = null))), k && (k = !1);
  }
  El(() => {
    k && ue();
  });
  let ce = null;
  function dt(b) {
    Re[b ? "unshift" : "push"](() => {
      A = b, e(16, A), e(7, j), e(14, U), e(15, J);
    });
  }
  function mt(b) {
    Re[b ? "unshift" : "push"](() => {
      r = b, e(13, r);
    });
  }
  return l.$$set = (b) => {
    "i18n" in b && e(1, o = b.i18n), "eta" in b && e(0, _ = b.eta), "queue_position" in b && e(2, s = b.queue_position), "queue_size" in b && e(3, a = b.queue_size), "status" in b && e(4, u = b.status), "scroll_to_output" in b && e(21, c = b.scroll_to_output), "timer" in b && e(5, y = b.timer), "show_progress" in b && e(6, g = b.show_progress), "message" in b && e(22, p = b.message), "progress" in b && e(7, j = b.progress), "variant" in b && e(8, L = b.variant), "loading_text" in b && e(9, q = b.loading_text), "absolute" in b && e(10, C = b.absolute), "translucent" in b && e(11, d = b.translucent), "border" in b && e(12, v = b.border), "autoscroll" in b && e(23, S = b.autoscroll), "$$scope" in b && e(28, f = b.$$scope);
  }, l.$$.update = () => {
    l.$$.dirty[0] & /*eta, old_eta, timer_start, eta_from_start*/
    218103809 && (_ === null && e(0, _ = G), _ != null && G !== _ && (e(27, B = (performance.now() - Y) / 1e3 + _), e(19, ce = B.toFixed(1)), e(26, G = _))), l.$$.dirty[0] & /*eta_from_start, timer_diff*/
    167772160 && e(17, ae = B === null || B <= 0 || !M ? null : Math.min(M / B, 1)), l.$$.dirty[0] & /*progress*/
    128 && j != null && e(18, re = !1), l.$$.dirty[0] & /*progress, progress_level, progress_bar, last_progress_level*/
    114816 && (j != null ? e(14, U = j.map((b) => {
      if (b.index != null && b.length != null)
        return b.index / b.length;
      if (b.progress != null)
        return b.progress;
    })) : e(14, U = null), U ? (e(15, J = U[U.length - 1]), A && (J === 0 ? e(16, A.style.transition = "0", A) : e(16, A.style.transition = "150ms", A))) : e(15, J = void 0)), l.$$.dirty[0] & /*status*/
    16 && (u === "pending" ? m() : ue()), l.$$.dirty[0] & /*el, scroll_to_output, status, autoscroll*/
    10493968 && r && c && (u === "pending" || u === "complete") && xl(r, S), l.$$.dirty[0] & /*status, message*/
    4194320, l.$$.dirty[0] & /*timer_diff*/
    33554432 && e(20, n = M.toFixed(1));
  }, [
    _,
    o,
    s,
    a,
    u,
    y,
    g,
    j,
    L,
    q,
    C,
    d,
    v,
    r,
    U,
    J,
    A,
    ae,
    re,
    ce,
    n,
    c,
    p,
    S,
    Y,
    M,
    G,
    B,
    f,
    i,
    dt,
    mt
  ];
}
class en extends Vl {
  constructor(t) {
    super(), Pl(
      this,
      t,
      $l,
      Wl,
      Zl,
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
  SvelteComponent: tn,
  append: ee,
  assign: ln,
  attr: V,
  binding_callbacks: nt,
  create_component: Ce,
  destroy_component: Le,
  detach: K,
  element: te,
  get_spread_object: nn,
  get_spread_update: sn,
  init: fn,
  insert: Q,
  listen: oe,
  mount_component: Se,
  run_all: on,
  safe_not_equal: _n,
  set_data: ct,
  set_input_value: be,
  space: ge,
  text: Ve,
  to_number: je,
  transition_in: Ne,
  transition_out: Me
} = window.__gradio__svelte__internal, { afterUpdate: an } = window.__gradio__svelte__internal;
function rn(l) {
  let t;
  return {
    c() {
      t = Ve(
        /*label*/
        l[5]
      );
    },
    m(e, n) {
      Q(e, t, n);
    },
    p(e, n) {
      n[0] & /*label*/
      32 && ct(
        t,
        /*label*/
        e[5]
      );
    },
    d(e) {
      e && K(t);
    }
  };
}
function un(l) {
  let t, e, n, i, f, o, _, s, a, u, c, y, g, p, j, L, q, C, d;
  const v = [
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
  let S = {};
  for (let r = 0; r < v.length; r += 1)
    S = ln(S, v[r]);
  return t = new en({ props: S }), o = new dl({
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
      Ce(t.$$.fragment), e = ge(), n = te("div"), i = te("div"), f = te("label"), Ce(o.$$.fragment), _ = ge(), s = te("input"), u = ge(), c = te("input"), g = ge(), p = te("p"), j = Ve("Value: "), L = Ve(
        /*value*/
        l[0]
      ), V(
        f,
        "for",
        /*id*/
        l[18]
      ), V(s, "aria-label", a = `number input for ${/*label*/
      l[5]}`), V(s, "data-testid", "number-input"), V(s, "type", "number"), V(
        s,
        "min",
        /*minimum*/
        l[10]
      ), V(
        s,
        "max",
        /*maximum*/
        l[11]
      ), V(
        s,
        "step",
        /*step*/
        l[12]
      ), s.disabled = /*disabled*/
      l[17], s.readOnly = !0, V(s, "class", "svelte-o2qgeu"), V(i, "class", "head svelte-o2qgeu"), V(n, "class", "wrap svelte-o2qgeu"), V(c, "type", "range"), V(
        c,
        "id",
        /*id*/
        l[18]
      ), V(c, "name", "cowbell"), V(
        c,
        "min",
        /*minimum*/
        l[10]
      ), V(
        c,
        "max",
        /*maximum*/
        l[11]
      ), V(
        c,
        "step",
        /*step*/
        l[12]
      ), c.disabled = /*disabled*/
      l[17], V(c, "aria-label", y = `range slider for ${/*label*/
      l[5]}`), V(c, "class", "svelte-o2qgeu");
    },
    m(r, k) {
      Se(t, r, k), Q(r, e, k), Q(r, n, k), ee(n, i), ee(i, f), Se(o, f, null), ee(i, _), ee(i, s), be(
        s,
        /*value*/
        l[0]
      ), l[24](s), Q(r, u, k), Q(r, c, k), be(
        c,
        /*value*/
        l[0]
      ), l[26](c), Q(r, g, k), Q(r, p, k), ee(p, j), ee(p, L), q = !0, C || (d = [
        oe(
          s,
          "input",
          /*input0_input_handler*/
          l[23]
        ),
        oe(
          s,
          "blur",
          /*clamp*/
          l[19]
        ),
        oe(
          c,
          "change",
          /*input1_change_input_handler*/
          l[25]
        ),
        oe(
          c,
          "input",
          /*input1_change_input_handler*/
          l[25]
        ),
        oe(
          c,
          "input",
          /*adjustValue*/
          l[20]
        )
      ], C = !0);
    },
    p(r, k) {
      const Y = k[0] & /*gradio, loading_status*/
      16386 ? sn(v, [
        k[0] & /*gradio*/
        2 && { autoscroll: (
          /*gradio*/
          r[1].autoscroll
        ) },
        k[0] & /*gradio*/
        2 && { i18n: (
          /*gradio*/
          r[1].i18n
        ) },
        k[0] & /*loading_status*/
        16384 && nn(
          /*loading_status*/
          r[14]
        )
      ]) : {};
      t.$set(Y);
      const M = {};
      k[0] & /*show_label*/
      8192 && (M.show_label = /*show_label*/
      r[13]), k[0] & /*info*/
      64 && (M.info = /*info*/
      r[6]), k[0] & /*label*/
      32 | k[1] & /*$$scope*/
      1 && (M.$$scope = { dirty: k, ctx: r }), o.$set(M), (!q || k[0] & /*label*/
      32 && a !== (a = `number input for ${/*label*/
      r[5]}`)) && V(s, "aria-label", a), (!q || k[0] & /*minimum*/
      1024) && V(
        s,
        "min",
        /*minimum*/
        r[10]
      ), (!q || k[0] & /*maximum*/
      2048) && V(
        s,
        "max",
        /*maximum*/
        r[11]
      ), (!q || k[0] & /*step*/
      4096) && V(
        s,
        "step",
        /*step*/
        r[12]
      ), (!q || k[0] & /*disabled*/
      131072) && (s.disabled = /*disabled*/
      r[17]), k[0] & /*value*/
      1 && je(s.value) !== /*value*/
      r[0] && be(
        s,
        /*value*/
        r[0]
      ), (!q || k[0] & /*minimum*/
      1024) && V(
        c,
        "min",
        /*minimum*/
        r[10]
      ), (!q || k[0] & /*maximum*/
      2048) && V(
        c,
        "max",
        /*maximum*/
        r[11]
      ), (!q || k[0] & /*step*/
      4096) && V(
        c,
        "step",
        /*step*/
        r[12]
      ), (!q || k[0] & /*disabled*/
      131072) && (c.disabled = /*disabled*/
      r[17]), (!q || k[0] & /*label*/
      32 && y !== (y = `range slider for ${/*label*/
      r[5]}`)) && V(c, "aria-label", y), k[0] & /*value*/
      1 && be(
        c,
        /*value*/
        r[0]
      ), (!q || k[0] & /*value*/
      1) && ct(
        L,
        /*value*/
        r[0]
      );
    },
    i(r) {
      q || (Ne(t.$$.fragment, r), Ne(o.$$.fragment, r), q = !0);
    },
    o(r) {
      Me(t.$$.fragment, r), Me(o.$$.fragment, r), q = !1;
    },
    d(r) {
      r && (K(e), K(n), K(u), K(c), K(g), K(p)), Le(t, r), Le(o), l[24](null), l[26](null), C = !1, on(d);
    }
  };
}
function cn(l) {
  let t, e;
  return t = new Nt({
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
      n[9]), i[0] & /*value, minimum, maximum, step, disabled, label, rangeInput, numberInput, show_label, info, gradio, loading_status*/
      261219 | i[1] & /*$$scope*/
      1 && (f.$$scope = { dirty: i, ctx: n }), t.$set(f);
    },
    i(n) {
      e || (Ne(t.$$.fragment, n), e = !0);
    },
    o(n) {
      Me(t.$$.fragment, n), e = !1;
    },
    d(n) {
      Le(t, n);
    }
  };
}
let dn = 0;
function mn(l, t, e) {
  let n, { gradio: i } = t, { elem_id: f = "" } = t, { elem_classes: o = [] } = t, { visible: _ = !0 } = t, { value: s = 0 } = t, { label: a = i.i18n("slider.slider") } = t, { info: u = void 0 } = t, { container: c = !0 } = t, { scale: y = null } = t, { min_width: g = void 0 } = t, { minimum: p } = t, { maximum: j = 100 } = t, { step: L } = t, { show_label: q } = t, { interactive: C } = t, { loading_status: d } = t, { value_is_output: v = !1 } = t, S, r;
  const k = `range_id_${dn++}`;
  function Y() {
    i.dispatch("change"), v || i.dispatch("input");
  }
  an(() => {
    e(21, v = !1), G();
  });
  function M() {
    i.dispatch("release", s), e(0, s = Math.min(Math.max(s, p), j));
  }
  function G() {
    B(), S.addEventListener("input", B), r.addEventListener("input", B);
  }
  function B() {
    const m = Number(S.value) - Number(S.min), E = Number(S.max) - Number(S.min), ue = E === 0 ? 0 : m / E;
    e(15, S.style.backgroundSize = ue * 100 + "% 100%", S);
  }
  function ae(m) {
    let E = parseFloat(m.target.value);
    Number.isInteger(E) && (E += E + L <= m.target.max ? L : -L, e(0, s = E));
  }
  function U() {
    s = je(this.value), e(0, s);
  }
  function J(m) {
    nt[m ? "unshift" : "push"](() => {
      r = m, e(16, r);
    });
  }
  function A() {
    s = je(this.value), e(0, s);
  }
  function re(m) {
    nt[m ? "unshift" : "push"](() => {
      S = m, e(15, S);
    });
  }
  return l.$$set = (m) => {
    "gradio" in m && e(1, i = m.gradio), "elem_id" in m && e(2, f = m.elem_id), "elem_classes" in m && e(3, o = m.elem_classes), "visible" in m && e(4, _ = m.visible), "value" in m && e(0, s = m.value), "label" in m && e(5, a = m.label), "info" in m && e(6, u = m.info), "container" in m && e(7, c = m.container), "scale" in m && e(8, y = m.scale), "min_width" in m && e(9, g = m.min_width), "minimum" in m && e(10, p = m.minimum), "maximum" in m && e(11, j = m.maximum), "step" in m && e(12, L = m.step), "show_label" in m && e(13, q = m.show_label), "interactive" in m && e(22, C = m.interactive), "loading_status" in m && e(14, d = m.loading_status), "value_is_output" in m && e(21, v = m.value_is_output);
  }, l.$$.update = () => {
    l.$$.dirty[0] & /*interactive*/
    4194304 && e(17, n = !C), l.$$.dirty[0] & /*value*/
    1 && Y();
  }, [
    s,
    i,
    f,
    o,
    _,
    a,
    u,
    c,
    y,
    g,
    p,
    j,
    L,
    q,
    d,
    S,
    r,
    n,
    k,
    M,
    ae,
    v,
    C,
    U,
    J,
    A,
    re
  ];
}
class bn extends tn {
  constructor(t) {
    super(), fn(
      this,
      t,
      mn,
      cn,
      _n,
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
