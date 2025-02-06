// @ts-check
import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
    site: "https://evolvconsulting.github.io/snowflake-cards/",
    base: '/snowflake-cards',
    vite: {
        plugins: [tailwindcss()]
    },
});