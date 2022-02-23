import { terser } from "rollup-plugin-terser";
import babel from "rollup-plugin-babel";
import commonjs from "rollup-plugin-commonjs";
import postcss from "rollup-plugin-postcss";
import resolve from "@rollup/plugin-node-resolve";
import postCssImport from "postcss-import";
import postcssPresetEnv from "postcss-preset-env";
import postcssReporter from "postcss-reporter";
import stylelint from "stylelint";

const production = process.env.BUILD === "production";

export default [
  {
    input: "src/js/django-fontawesome.js",
    output: {
      file: "fontawesome_6/static/fontawesome_6/js/django-fontawesome.js",
      format: "iife"
    },
    plugins: [resolve(), commonjs(), babel(), ...(production ? [terser()] : [])]
  },
  {
    input: "src/scss/django-fontawesome.scss",
    output: {
      file: "fontawesome_6/static/fontawesome_6/css/django-fontawesome.css",
      format: "es"
    },
    plugins: [
      postcss({
        extract: true,
        minimize: production,
        plugins: [
          postCssImport({
            plugins: [stylelint()]
          }),
          postcssPresetEnv({ clearReportedMessages: true }),
          postcssReporter()
        ]
      })
    ]
  }
];
