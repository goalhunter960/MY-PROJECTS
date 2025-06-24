import * as dotenv from "dotenv"
dotenv.config()  // Load env variables from .env

import { defineConfig } from "drizzle-kit"

export default defineConfig({
  schema: "./apps/api/src/schema.ts",
  out: "./drizzle",
  dialect: "postgresql",
  dbCredentials: {
    url: process.env.DATABASE_URL!,
  },
})

